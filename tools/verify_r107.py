#!/usr/bin/env python3
"""Offline integrity checks for r107; no network, old verifier, PDF or devices.

Hashes identify saved bytes, not source truth, historical chronology, or fidelity
of manual transcriptions. Search-result metadata may mention excluded PDF URLs;
this program never fetches or opens those URLs.
"""
from __future__ import annotations

import copy
import csv
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
I = ROOT / "ingest/angora-1__arena-01a0ce39__5acb613"
W = I / "01-text-verbatim/workstation"
P = I / "52-entry-safety-r107-2026-10-26"
S = I / "53-source-evidence-r107-2026-10-26"
OLD = I / "49-source-evidence-r106-2026-10-26"
BASE = "ef45d8165a55267f6f583cdc16af89ef6b698af8"


def need(condition, message):
    if not condition:
        raise AssertionError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def rows(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def path_for(path):
    p = (ROOT / path).resolve()
    need(p.is_relative_to(ROOT), "path outside workspace")
    return p


def check_bytes(data, size, sha, exact=True):
    need(len(data) == size if exact else len(data) >= size, "byte length mismatch")
    need(digest(data[:size]) == sha, "byte hash mismatch")


def check_inventory(record, size_key="bytes", sha_key="sha256", path_key="repository_relative_path"):
    name = record[path_key]
    data = path_for(name).read_bytes()
    n = int(record[size_key])
    check_bytes(data, n, record[sha_key], exact=name not in APPENDED)
    return data[:n]


def source_line(name, number, bound=None):
    data = path_for(name).read_bytes()
    if bound is not None:
        data = data[:bound]
    lines = data.decode("utf-8").split("\n")
    n = int(number) - 1
    need(0 <= n < len(lines), "line out of range")
    return lines[n]


def check_anchor(r):
    b = check_inventory(r, size_key="bytes_bound")
    lines = b.decode("utf-8").split("\n")
    n = int(r["line"]) - 1
    need(0 <= n < len(lines), "anchor line out of range")
    need(r["anchor"] in lines[n] and digest(lines[n].encode()) == r["line_sha256"], "anchor text/hash mismatch")


def check_url(url):
    p = urlsplit(url)
    need(p.scheme == "https" and p.netloc == "www.angoranetworks.com", "unexpected fetched host")
    need(not p.path.lower().endswith(".pdf"), "PDF fetch prohibited")
    need(not p.path.startswith(("/download/", "/qr/")), "download or QR fetch prohibited")


def check_web(r):
    check_url(r["url"])
    need(r["status"] == "success" and r["chunks"] == "1" and r["has_more"] == "false", "web tool metadata mismatch")
    need("not original HTML" in r["representation"] or "not raw HTML" in r["representation"], "missing source representation")
    check_inventory(r)


def check_failed(r):
    need(r["status"] == "error" and r["body_obtained"] == "false", "failed webpage was used as successful source")
    need("excluded" in r["analysis_use"], "failed source not excluded")


def check_early_pages(export, teacher, posts):
    need("İhracata Tam Gaz Devam" in export["title_from_tool"], "export page title mismatch")
    need("Öğretmenler Günü" in teacher["title_from_tool"], "Teacher's Day title mismatch")
    export_text = path_for(export["repository_relative_path"]).read_text(encoding="utf-8")
    teacher_text = path_for(teacher["repository_relative_path"]).read_text(encoding="utf-8")
    statement = "Sadece yerli değiliz ihracat da yapıyoruz."
    need(statement in export_text and statement not in teacher_text, "export sentence assigned to wrong page")
    index = {r["id"]: r for r in posts}
    need(index["64"]["r39_slug_literal"] in urlsplit(export["url"]).path, "export old-ID link mismatch")
    need(index["62"]["r39_slug_literal"] in urlsplit(teacher["url"]).path, "teacher old-ID link mismatch")
    need("Post_20201124_instapsd_1200x900-1200x675.jpg" in export_text and "Post_20201124-1200x675.jpg" in teacher_text, "image URL strings mismatch")


def check_single_revision(r):
    src = path_for(r["source_path"]).read_bytes()
    dst = path_for(r["destination_path"]).read_bytes()
    check_bytes(src, int(r["source_bytes"]), r["source_sha256"])
    check_bytes(dst, int(r["corrected_bytes"]), r["corrected_sha256"])
    old = r["prior_manual_transcription"].encode()
    new = r["r106_tool_response_literal"].encode()
    need(src.count(old) == 1 and src.count(new) == 0, "old correction occurrence")
    need(dst == src.replace(old, new, 1) and dst.replace(new, old, 1) == src, "correction changed more than one span")
    need(src[:src.index(old)].count(b"\n") + 1 == int(r["source_line"]) == 105, "correction line")
    return src, dst


def check_post(r):
    parts = {}
    for name in ("r39", "r40"):
        line = source_line(r[name + "_path"], r[name + "_line"])
        need(digest(line.encode()) == r[name + "_line_sha256"], "stored post row hash")
        c = line.split("\t")
        need(len(c) == 4 and c[0] == r["id"], "stored post row shape")
        need(c[1] == r[name + "_date_literal"] and c[2] == r[name + "_modified_literal"] and c[3] == r[name + "_slug_literal"], "stored post fields")
        parts[name] = c
    for field, index in (("date_fields_equal", 1), ("modified_fields_equal", 2), ("slug_strings_equal", 3)):
        need((r[field] == "True") == (parts["r39"][index] == parts["r40"][index]), "stored post equality mismatch")


def check_impact(r, prior, src, dst):
    need(r["claim_id"] in prior, "unknown r106 prior claim")
    oldrow = prior[r["claim_id"]]
    need(oldrow["source_line"] == r["source_line"], "claim line changed")
    n = int(r["source_line"]) - 1
    old_lines, new_lines = src.decode("utf-8").split("\n"), dst.decode("utf-8").split("\n")
    need(0 <= n < len(old_lines) == len(new_lines), "claim line outside revised transcription")
    need(old_lines[n] == new_lines[n] and r["literal_line_unchanged"] == "True", "prior claim line changed")
    need(digest(old_lines[n].encode()) == r["old_line_sha256"] == r["revised_line_sha256"] == oldrow["source_line_sha256"], "prior claim line hash")
    need(oldrow["anchor"] in old_lines[n], "prior claim anchor")


def check_local_link(doc, link):
    if link.startswith(("https://", "http://", "mailto:", "#")):
        return False
    target = (doc.parent / unquote(urlsplit(link).path)).resolve()
    need(target.is_relative_to(ROOT) and target.is_file(), "missing local link")
    return True


def check_links(doc, text):
    return sum(int(check_local_link(doc, link)) for link in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text))


append_rows = rows(S / "append-log.csv")
APPENDED = {r["repository_relative_path"]: r for r in append_rows}
plans = rows(S / "append-plan-before-write.csv")
need(len(append_rows) == len(APPENDED) == len(plans) == 5, "append target count")
need({r["repository_relative_path"] for r in plans} == set(APPENDED), "append plan paths")
for plan in plans:
    name = plan["repository_relative_path"]
    entry = APPENDED[name]
    need(plan["original_bytes"] == entry["original_bytes"] and plan["original_sha256"] == entry["original_sha256"], "append plan prefix")
    data = path_for(name).read_bytes()
    before, added = int(entry["original_bytes"]), int(entry["appended_bytes"])
    need(len(data) == before + added == int(entry["new_bytes"]), "append total size")
    check_bytes(data[:before], before, entry["original_sha256"])
    check_bytes(data[before:], added, entry["appended_sha256"])
    need(digest(data) == entry["new_sha256"], "append total hash")
    git_original = subprocess.run(["git", "show", f"{BASE}:{name}"], cwd=ROOT, stdout=subprocess.PIPE, check=True).stdout
    need(data[:before] == git_original, "historical Git prefix changed")
need(sum(int(r["original_bytes"]) for r in append_rows) == 108050, "append prefix sum")
need(sum(int(r["appended_bytes"]) for r in append_rows) == 4385, "append suffix sum")

# Local sources: two were first read under earlier safety scopes; one was listed late.
groups = [
    ("initial-local-scope-before-topic-read.csv", "initial-local-read-inventory.csv", 12, 163154),
    ("news-index-scope-before-read.csv", "news-index-read-inventory.csv", 1, 5695),
    ("additional-scope-after-first-read.csv", "additional-read-inventory.csv", 1, 4323),
    ("previous-index-scope-before-read.csv", "previous-index-read-inventory.csv", 6, 3981),
]
seen = set()
for scope_name, inv_name, count, byte_count in groups:
    scope, inventory = rows(S / scope_name), rows(S / inv_name)
    need(len(scope) == len(inventory) == count, "source group count")
    need(sum(int(r["bytes"]) for r in inventory) == byte_count, "source group size")
    need([(r["repository_relative_path"], r["bytes"]) for r in scope] == [(r["repository_relative_path"], r["bytes"]) for r in inventory], "source scope/inventory mismatch")
    for r in inventory:
        need(r["repository_relative_path"] not in seen, "duplicate analytical input")
        seen.add(r["repository_relative_path"])
        check_inventory(r)
need(len(seen) == 20 and sum(x[3] for x in groups) == 177153, "source totals")
need(rows(S / "additional-scope-after-first-read.csv")[0]["first_access_before_this_list"] == "yes", "late-listed source not disclosed")

prior_scope, prior_inv = rows(P / "prior-ledgers-scope-before-read.csv"), rows(P / "prior-ledgers-read-inventory.csv")
need(len(prior_scope) == len(prior_inv) == 6, "prior ledger count")
need([(r["repository_relative_path"], r["bytes"]) for r in prior_scope] == [(r["repository_relative_path"], r["bytes"]) for r in prior_inv], "prior ledger scope")
for r in prior_inv:
    check_inventory(r)
protected_scope, protected = rows(P / "protected-variants-scope-before-read.csv"), rows(P / "protected-variants-read-inventory.csv")
need(len(protected_scope) == len(protected) == 31 and sum(int(r["bytes"]) for r in protected) == 17455599, "protected copy count/size")
for a, b in zip(protected_scope, protected):
    need(all(a[k] == b[k] for k in ("repository_relative_path", "bytes", "expected_sha256")), "protected scope mismatch")
    need(b["sha256"] == b["expected_sha256"], "protected expected hash")
    check_inventory(b)
hist_scope, hist = rows(P / "historical-append-final-scope-before-read.csv"), rows(P / "historical-append-final-read-inventory.csv")
need(len(hist_scope) == len(hist) == 4, "historic final target count")
for a, b in zip(hist_scope, hist):
    need(all(a[k] == b[k] for k in ("repository_relative_path", "bytes", "expected_sha256", "last_append_round")), "historic scope mismatch")
    need(b["expected_sha256"] == b["sha256"], "historic final hash mismatch")
    check_inventory(b)
need(sum(r["repository_relative_path"] in APPENDED for r in hist) == 2, "historic target append count")
baseline = json.loads((P / "baseline.json").read_text(encoding="utf-8"))
need(baseline["head"] == baseline["remote_branch_head"] == BASE, "entry commit")
need(baseline["session_date_supplied_utc"] == "2026-10-26" and baseline["environment_start_observed_utc"].startswith("2026-11-19T"), "clock conflict record")

web1 = rows(S / "web-first-visible-inventory.csv")
web2 = rows(S / "web-2021-visible-inventory.csv")
plan1 = rows(S / "web-first-scope-before-fetch.csv")
plan2 = rows(S / "web-2021-scope-before-fetch.csv") + rows(S / "web-training-english-scope-before-fetch.csv")
need(len(web1) == len(web2) == len(plan1) == len(plan2) == 3, "web scope count")
need(sum(int(r["bytes"]) for r in web1) == 9547 and sum(int(r["bytes"]) for r in web2) == 12165, "web byte totals")
for plan, entry in zip(plan1 + plan2, web1 + web2):
    need(plan["url"] == entry["url"], "web URL plan mismatch")
    need((S / plan["planned_path_from_r107_source_dir"]).resolve() == path_for(entry["repository_relative_path"]), "web artifact path mismatch")
    check_web(entry)
need(len({r["url"] for r in web1 + web2}) == 6, "web duplicate URLs")
failed = rows(S / "web-agency-fetch-result.csv")
failed_plan = rows(S / "web-agency-scope-before-fetch.csv")
need(len(failed) == len(failed_plan) == 1 and failed[0]["url"] == failed_plan[0]["url"], "failed URL scope")
check_failed(failed[0])
need(not (S / failed_plan[0]["planned_path_from_r107_source_dir"]).exists(), "failed source unexpectedly has body")

# One known old omission corrected in a second version, original remains untouched.
revision_plan = rows(S / "r106-transcription-correction-plan-before-write.csv")
revision_log = rows(S / "r106-transcription-correction-log.csv")
need(len(revision_plan) == len(revision_log) == 1, "old revision count")
revision = revision_log[0]
need(all(revision_plan[0][k] == revision[k] for k in revision_plan[0]), "old revision plan mismatch")
src, dst = check_single_revision(revision)
git_source = subprocess.run(["git", "show", f"{BASE}:{revision['source_path']}"], cwd=ROOT, stdout=subprocess.PIPE, check=True).stdout
need(src == git_source, "r106 original transcript changed")
prior_claim_rows = rows(OLD / "interview-claim-matrix.csv")
prior_claims = {r["claim_id"]: r for r in prior_claim_rows}
impact = rows(S / "r106-transcription-claim-impact.csv")
need(len(prior_claims) == len(impact) == 9 and {r["claim_id"] for r in impact} == set(prior_claims), "claim impact count")
for r in impact:
    check_impact(r, prior_claims, src, dst)

# The r107 English related-thumbnail transcription revision is independently reconstructed.
transcription = rows(S / "r107-transcription-revision-log.csv")
need(len(transcription) == 1, "new revision log count")
t = transcription[0]
current = path_for(t["path"]).read_bytes()
check_bytes(current, int(t["after_bytes"]), t["after_sha256"])
new = b"Post_20210902_web_en-1-480x360.png"
old = b"Post_20210902_web_en-1-480x80.png"
need(current.count(new) == 1 and current.count(old) == 0, "new revision occurrence")
draft = current.replace(new, old, 1)
check_bytes(draft, int(t["before_bytes"]), t["before_sha256"])

anchors = rows(S / "evidence-traceability.csv")
need(len(anchors) == len({r["claim_id"] for r in anchors}) == 33, "anchor count")
for n, r in enumerate(anchors, 1):
    need(int(r["seq"]) == n, "anchor sequence")
    check_anchor(r)
anchor_ids = {r["claim_id"] for r in anchors}
events, issues = rows(S / "event-evidence-matrix.csv"), rows(S / "issues-and-corrections.csv")
need(len(events) == len({r["event_id"] for r in events}) == 6, "event count")
need(len(issues) == len({r["case"] for r in issues}) == 9, "issue count")
for r in events + issues:
    need(set(r["anchors"].split(";")) <= anchor_ids, "unknown anchor reference")
posts = rows(S / "saved-post-tsv-10-row-comparison.csv")
need(len(posts) == len({r["id"] for r in posts}) == 10, "stored post count")
for r in posts:
    check_post(r)
need(all(r["date_fields_equal"] == r["modified_fields_equal"] == "True" for r in posts), "date fields comparison")
need({r["id"] for r in posts if r["slug_strings_equal"] == "False"} == {"803", "777"}, "slug difference IDs")
check_early_pages(web1[0], web1[1], posts)
english_training = path_for(web2[2]["repository_relative_path"]).read_text(encoding="utf-8")
need(english_training.count("Angora Networks works hard to support its customers with the highest quality products and services.") == 2, "English training repeated sentence")
index_date = next(r for r in anchors if r["claim_id"] == "TRAIN-index-date")["anchor"]
need(index_date == "05/03/2021" and (5, 3) != (2, 12) and (3, 5) != (2, 12), "ambiguous index date comparison")
for name in ("r39_path", "r40_path"):
    ts = path_for(posts[0][name]).read_text(encoding="utf-8").splitlines()
    ids = [line.split("\t")[0] for line in ts if line.split("\t")[0].isdigit()]
    need(len(ids) == len(set(ids)) == 10, "TSV numeric-ID count")

prior_scope = set()
for name in ("local-cms-read-inventory.csv", "local-method-read-inventory.csv", "context-read-inventory.csv", "local-existing-web-read-inventory.csv", "local-direct-read-inventory.csv", "previous-index-read-inventory.csv"):
    prior_scope.update(r["repository_relative_path"] for r in rows(OLD / name))
need(len(prior_scope) == 20, "r106 analytical inputs")
overlap = rows(S / "overlap-r106-20.csv")
need(len(overlap) == len({r["repository_relative_path"] for r in overlap}) == 14, "overlap input count")
need(all((r["in_r106_20"] == "True") == (r["repository_relative_path"] in prior_scope) for r in overlap), "overlap membership")
need(sum(r["in_r106_20"] == "True" for r in overlap) == 5, "overlap total")

# Search outcomes are metadata only. Two unexpected PDF snippets were not opened or used.
plans = rows(S / "discovery-plan-before-search.csv") + rows(S / "discovery-organizations-plan-before-search.csv") + rows(S / "discovery-primary-plan-before-search.csv")
results = rows(S / "discovery-metadata.csv") + rows(S / "discovery-organizations-metadata.csv") + rows(S / "discovery-primary-metadata.csv")
summary = rows(S / "discovery-query-summary.csv")
need(len(plans) == len(summary) == len({r["query_id"] for r in plans}) == 9 and len(results) == 27, "search scope counts")
counts = Counter(r["query_id"] for r in results)
need({r["query_id"] for r in plans} == {r["query_id"] for r in summary}, "search summary IDs")
for r in summary:
    need(int(r["result_count"]) == counts[r["query_id"]], "search result count")
pdfs = [r for r in results if urlsplit(r["url"]).path.lower().endswith(".pdf")]
need(len(pdfs) == 2 and all(r["query_id"] == "Q07" and "not opened or used" in r["disposition"] for r in pdfs), "unexpected PDF snippet disclosure")

# Strictly parse every r107 CSV and check all new-doc links and append-suffix links.
csv_files = sorted(P.rglob("*.csv")) + sorted(S.rglob("*.csv"))
data_rows = 0
for path in csv_files:
    with path.open(encoding="utf-8", newline="") as f:
        parsed = list(csv.reader(f, strict=True))
    need(parsed and len(set(parsed[0])) == len(parsed[0]), "invalid CSV header")
    need(all(len(row) == len(parsed[0]) for row in parsed[1:]), "inconsistent CSV width")
    data_rows += len(parsed) - 1
docs = [P / "README.md", S / "README.md", W / "08-customer-pipeline/176-angora-early-commercial-evidence-r107-2026-10-26.md", W / "09-orders/120-angora-orders-dossier-2026-10-21.r107-appendix.md", W / "09-orders/120-angora-orders-master-2026-10-21.mapping-r107.md", I / "54-followup-angora-r107-2026-10-26/angora-networks.md", I / "55-audit-r107-2026-10-26.md"]
links = sum(check_links(p, p.read_text(encoding="utf-8")) for p in docs)
for r in append_rows:
    p = path_for(r["repository_relative_path"])
    links += check_links(p, p.read_bytes()[int(r["original_bytes"]):].decode("utf-8"))

negative = []


def reject(label, action):
    try:
        action()
    except (AssertionError, KeyError, ValueError):
        negative.append(label)
        return
    raise AssertionError("negative test unexpectedly passed: " + label)


reject("bad hash", lambda: check_bytes(b"abcd", 4, "0" * 64))
reject("short prefix", lambda: check_bytes(b"abc", 4, digest(b"abcd"), exact=False))
reject("outside workspace", lambda: path_for("../../outside"))
bad_anchor = copy.deepcopy(anchors[0]); bad_anchor["anchor"] = "__missing__"
reject("bad evidence anchor", lambda: check_anchor(bad_anchor))
reject("prohibited PDF URL", lambda: check_url("https://www.angoranetworks.com/example.pdf"))
reject("prohibited download URL", lambda: check_url("https://www.angoranetworks.com/download/123/"))
reject("prohibited QR URL", lambda: check_url("https://www.angoranetworks.com/qr/123/"))
bad_failed = copy.deepcopy(failed[0]); bad_failed["body_obtained"] = "true"
reject("failed source claimed successful", lambda: check_failed(bad_failed))
bad_revision = copy.deepcopy(revision); bad_revision["r106_tool_response_literal"] = "__changed__"
reject("changed old revision", lambda: check_single_revision(bad_revision))
bad_impact = copy.deepcopy(impact[0]); bad_impact["revised_line_sha256"] = "0" * 64
reject("changed claim impact", lambda: check_impact(bad_impact, prior_claims, src, dst))
bad_post = copy.deepcopy(next(r for r in posts if r["id"] == "803")); bad_post["r40_slug_literal"] = bad_post["r39_slug_literal"]
reject("hidden stored slug difference", lambda: check_post(bad_post))
bad_web = copy.deepcopy(web1[0]); bad_web["chunks"] = "2"
reject("wrong tool chunk count", lambda: check_web(bad_web))
bad_teacher = copy.deepcopy(web1[1]); bad_teacher["title_from_tool"] = web1[0]["title_from_tool"]
reject("Teacher's Day/export title confusion", lambda: check_early_pages(web1[0], bad_teacher, posts))
reject("missing link", lambda: check_local_link(S / "README.md", "__missing__.md"))
need(len(negative) == 14, "negative test count")

print("PASS r107 offline verifier")
print("20/20 local inputs, 177153 bytes; 2 first scoped under safety, 1 listed after first read")
print("31/31 protected copies, 17455599 bytes; 4/4 old final states; 5 append baselines and suffixes")
print("6/6 successful URLs and 6 chunks, 21712 bytes; 1 separately planned URL failed")
print("33 evidence anchors; 6 event rows; 9 corrections; 10 compared posts with 2 slug differences")
print("r106 single-span revision, original preserved; 9/9 indexed claim lines unchanged; 1 r107 copy correction logged")
print("9 searches, 27 result metadata, including 2 unexpected PDF snippets (not opened or used)")
print(f"strict CSVs {len(csv_files)} / {data_rows} records; local links {links}; negative tests {len(negative)}")
print("Not verified: actual read order, original HTML, complete transcription fidelity, vendor claims, certificates or delivery.")
