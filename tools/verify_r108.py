#!/usr/bin/env python3
"""Offline r108 integrity and arithmetic checks; no network, PDF, old verifier, or devices.

Hashes identify saved bytes, not actual source truth, historical chronology,
complete transcription fidelity, audio, or company compliance/transactions.
"""
from __future__ import annotations

import copy
import csv
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
I = ROOT / "ingest/angora-1__arena-01a0ce39__5acb613"
W = I / "01-text-verbatim/workstation"
P = I / "56-entry-safety-r108-2026-10-26"
S = I / "57-source-evidence-r108-2026-10-26"
PRIOR = I / "53-source-evidence-r107-2026-10-26"
BASE = "d78a855e196b4ded8b8ca5e67c1373b5c180fa86"


def need(value, message):
    if not value:
        raise AssertionError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def rows(path):
    with path.open(encoding="utf8", newline="") as f:
        return list(csv.DictReader(f))


def safe_path(name):
    path = (ROOT / name).resolve()
    need(path.is_relative_to(ROOT), "path outside repository")
    return path


def check_bytes(data, count, sha, exact=True):
    need((len(data) == count) if exact else (len(data) >= count), "unexpected byte length")
    need(digest(data[:count]) == sha, "byte hash mismatch")


def check_inv(r, size_key="bytes", sha_key="sha256", path_key="repository_relative_path"):
    path = r[path_key]
    data = safe_path(path).read_bytes()
    count = int(r[size_key])
    check_bytes(data, count, r[sha_key], exact=path not in APPENDED)
    return data[:count]


def check_eligible_source(name):
    need("/quarantine/" not in name, "quarantined source cannot supply evidence")


def check_anchor(r):
    check_eligible_source(r["repository_relative_path"])
    data = check_inv(r, size_key="bytes_bound")
    text = data.decode("utf8").split("\n")
    index = int(r["line"]) - 1
    need(0 <= index < len(text), "anchor line out of range")
    need(r["anchor"] in text[index] and digest(text[index].encode()) == r["line_sha256"], "anchor differs")


def check_url(url):
    u = urlsplit(url)
    need(u.scheme == "https" and u.netloc in {"ictmedia.com.tr", "www.tubisad.org.tr", "www.globaltechmagazine.com", "www.youtube.com"}, "unexpected analyzed host")
    need(not u.path.lower().endswith(".pdf") and not u.path.startswith(("/download/", "/qr/")), "PDF or download URL prohibited")


def check_chunk_group(inv, chunks):
    check_url(inv["url"])
    data = check_inv(inv)
    need(data.endswith(b"\n"), "stored newline missing")
    need(len(chunks) == int(inv["chunks"]), "chunk count mismatch")
    offset = 0
    for index, r in enumerate(chunks):
        need(r["url"] == inv["url"] and int(r["chunk_index"]) == index, "chunk source/index mismatch")
        need(r["has_more"] == str(index < len(chunks) - 1).lower(), "chunk has_more mismatch")
        start, end = int(r["start_byte"]), int(r["end_byte_exclusive"])
        need(start == offset and end >= start and end - start == int(r["bytes"]), "chunk offsets")
        need(digest(data[start:end]) == r["sha256"], "chunk hash")
        offset = end
    need(offset == len(data) - 1, "chunk coverage or stored newline")


def check_whitespace(r):
    data = check_inv(r)
    hits = [f"{i}:{len(line) - len(line.rstrip(bytes([32, 9])))}" for i, line in enumerate(data.split(b"\n"), 1) if line.rstrip(bytes([32, 9])) != line]
    need(len(hits) == int(r["trailing_space_line_count"]) and ";".join(hits) == r["line_number_and_byte_count"], "source whitespace mismatch")
    need((r["git_diff_attribute"] == "unset") == bool(hits), "source whitespace diff policy")


def check_ratio(r):
    a, b = Decimal(r["numerator_TL"]), Decimal(r["denominator_TL"])
    need(a >= 0 and b > 0, "invalid arithmetic inputs")
    ratio = (100 * a / b).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    need(ratio == Decimal(r["ratio_percent"]), "incorrect ratio")


def check_component(r):
    total = Decimal(r["reported_total_billion_TL"])
    summed = sum(Decimal(r[f"component{i}_billion_TL"]) for i in (1, 2, 3))
    need(total - summed == Decimal(r["total_minus_components_billion_TL"]), "component mismatch")


def check_hypothesis(r):
    if r["hypothesis_id"] == "H1":
        need("未能证明" in r["speaker_reported_result"], "H1 was overclaimed")
    elif r["hypothesis_id"] == "H2":
        need("有作用" in r["speaker_reported_result"] and "不影响" in r["initial_hypothesis"], "H2 hypothesis/result confused")
        need("不能证实" in r["boundary"], "H2 generalization not limited")
    elif r["hypothesis_id"] == "H3":
        need("风险" in r["speaker_reported_result"], "H3 result missing")
    else:
        need(False, "unknown hypothesis")


def check_link(doc, link):
    if link.startswith(("https://", "http://", "mailto:", "#")):
        return False
    target = (doc.parent / unquote(urlsplit(link).path)).resolve()
    need(target.is_relative_to(ROOT) and target.is_file(), "missing local link")
    return True


def links_in(doc, text):
    return sum(int(check_link(doc, link)) for link in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text))


append = rows(S / "append-log.csv")
APPENDED = {r["repository_relative_path"]: r for r in append}
plans = rows(S / "append-plan-before-write.csv")
need(len(append) == len(APPENDED) == len(plans) == 4, "append target count")
need({r["repository_relative_path"] for r in plans} == set(APPENDED), "append plan mismatch")
for plan in plans:
    name = plan["repository_relative_path"]
    row = APPENDED[name]
    need(plan["original_bytes"] == row["original_bytes"] and plan["original_sha256"] == row["original_sha256"], "append prefix mismatch")
    data = safe_path(name).read_bytes()
    n, m = int(row["original_bytes"]), int(row["appended_bytes"])
    need(len(data) == n + m == int(row["new_bytes"]), "append size")
    check_bytes(data[:n], n, row["original_sha256"])
    check_bytes(data[n:], m, row["appended_sha256"])
    need(digest(data) == row["new_sha256"], "append final hash")
    original = subprocess.run(["git", "show", f"{BASE}:{name}"], cwd=ROOT, stdout=subprocess.PIPE, check=True).stdout
    need(original == data[:n], "historical Git prefix altered")
need(sum(int(r["original_bytes"]) for r in append) == 132111, "prefix bytes sum")
need(sum(int(r["appended_bytes"]) for r in append) == 4196, "suffix bytes sum")
rev_plan = rows(S / "append-revision-plan-before-write.csv")
revision = rows(S / "append-revision-log.csv")
need(len(rev_plan) == len(revision) == 2, "revision count")
need(len({r["repository_relative_path"] for r in revision}) == 2, "revision targets")
for plan, r in zip(rev_plan, revision):
    need(all(plan[k] == r[k] for k in plan), "revision plan")
    after = safe_path(r["repository_relative_path"]).read_bytes()
    check_bytes(after, int(r["after_bytes"]), r["after_sha256"])
    old, new = r["old_suffix_phrase"].encode(), r["new_suffix_phrase"].encode()
    prefix = int(r["preexisting_original_bytes"])
    need(new not in after[:prefix] and after[prefix:].count(new) == 1, "revision not confined to new suffix")
    before = after.replace(new, old, 1)
    check_bytes(before, int(r["before_bytes"]), r["before_sha256"])
    need(before[:prefix] == after[:prefix], "revision changed original prefix")

scope, inventory = rows(S / "local-scope-before-topic-read.csv"), rows(S / "local-read-inventory.csv")
social_scope = rows(S / "social-selection-scope-before-read.csv")
social = rows(S / "social-selection-read-inventory.csv")
need(len(scope) == len(inventory) == 23 and len(social_scope) == len(social) == 1, "local group counts")
need(sum(int(r["bytes"]) for r in inventory) == 197292 and sum(int(r["bytes"]) for r in social) == 17662, "local group sizes")
need([(r["repository_relative_path"], r["bytes"]) for r in scope] == [(r["repository_relative_path"], r["bytes"]) for r in inventory], "local scopes mismatch")
need([(r["repository_relative_path"], r["bytes"]) for r in social_scope] == [(r["repository_relative_path"], r["bytes"]) for r in social], "social scope mismatch")
need(sum(r["first_read_under_safety_scope"] == "True" for r in scope) == 5, "safe-first count")
all_local = inventory + social
need(len({r["repository_relative_path"] for r in all_local}) == 24, "duplicate local source")
for r in all_local:
    check_inv(r)
need(social[0]["stopped_subject_token_present"] == "False", "social source must be quarantined")

listing = rows(S / "social-directory-complete-metadata.csv")
root = W / "02-social-intel"
need(len(listing) == 5 and {str(p.relative_to(ROOT)) for p in root.iterdir()} == {r["repository_relative_path"] for r in listing}, "social top-level directory differs")
for r in listing:
    p = safe_path(r["repository_relative_path"])
    need((r["type"] == "directory") == p.is_dir(), "directory metadata type")
    if p.is_file():
        if r["repository_relative_path"] in APPENDED:
            need(int(APPENDED[r["repository_relative_path"]]["original_bytes"]) == int(r["bytes"]), "social pre-append size")
        else:
            need(p.stat().st_size == int(r["bytes"]), "social original size")

prior_scope, prior_inv = rows(P / "prior-ledgers-scope-before-read.csv"), rows(P / "prior-ledgers-read-inventory.csv")
need(len(prior_scope) == len(prior_inv) == 6, "prior ledger count")
need([(r["repository_relative_path"], r["bytes"]) for r in prior_scope] == [(r["repository_relative_path"], r["bytes"]) for r in prior_inv], "prior ledger scope mismatch")
for r in prior_inv:
    check_inv(r)
protected_scope = rows(P / "protected-variants-scope-before-read.csv")
protected = rows(P / "protected-variants-read-inventory.csv")
need(len(protected_scope) == len(protected) == 31 and sum(int(r["bytes"]) for r in protected) == 17455599, "protected variants count")
for a, b in zip(protected_scope, protected):
    need(all(a[k] == b[k] for k in ("repository_relative_path", "bytes", "expected_sha256")), "protected scope")
    need(b["expected_sha256"] == b["sha256"], "protected expected hash")
    check_inv(b)
hist_scope = rows(P / "historical-append-final-scope-before-read.csv")
history = rows(P / "historical-append-final-read-inventory.csv")
need(len(hist_scope) == len(history) == 7, "historical final count")
for a, b in zip(hist_scope, history):
    need(all(a[k] == b[k] for k in ("repository_relative_path", "bytes", "expected_sha256", "basis")), "historical scope")
    need(b["expected_sha256"] == b["sha256"], "historical expected hash")
    check_inv(b)
need(sum(r["repository_relative_path"] in APPENDED for r in history) == 2, "historical continuation count")
baseline = json.loads((P / "baseline.json").read_text(encoding="utf8"))
need(baseline["head"] == baseline["remote_branch_head"] == BASE, "entry heads")
need(baseline["session_date_supplied_utc"] == "2026-10-26" and baseline["environment_start_observed_utc"].startswith("2026-11-19T"), "date conflict not recorded")

prior_inputs = set()
for name in ("initial-local-read-inventory.csv", "news-index-read-inventory.csv", "additional-read-inventory.csv", "previous-index-read-inventory.csv"):
    prior_inputs.update(r["repository_relative_path"] for r in rows(PRIOR / name))
need(len(prior_inputs) == 20, "prior scope count")
overlap = rows(S / "overlap-r107-20.csv")
need(len(overlap) == 24 and {r["repository_relative_path"] for r in overlap} == {r["repository_relative_path"] for r in all_local}, "overlap scope")
need(all((r["in_r107_20"] == "True") == (r["repository_relative_path"] in prior_inputs) for r in overlap), "overlap values")
need(sum(r["in_r107_20"] == "True" for r in overlap) == 9, "overlap total")

web_event = rows(S / "web-event-visible-inventory.csv")
web_other = rows(S / "web-market-video-visible-inventory.csv")
all_web = web_event + web_other
need(len(web_event) == 1 and len(web_other) == 3 and len({r["url"] for r in all_web}) == 4, "completed web sources")
need(sum(int(r["bytes"]) for r in all_web) == 55878 and sum(int(r["chunks"]) for r in all_web) == 9, "web bytes or chunks")
prelisted = rows(S / "web-event-scope-before-fetch.csv") + rows(S / "web-market-scope-before-fetch.csv") + rows(S / "web-video-scope-before-fetch.csv")
need({r["url"] for r in prelisted} == {r["url"] for r in all_web}, "web URL scope")
for r in prelisted:
    item = next(x for x in all_web if x["url"] == r["url"])
    need((S / r["planned_path_from_r108_source_dir"]).resolve() == safe_path(item["repository_relative_path"]), "web output path")
all_chunks = rows(S / "web-event-chunk-inventory.csv") + rows(S / "web-association-chunk-inventory.csv") + rows(S / "web-market-video-chunk-inventory.csv")
for r in all_web:
    chunks = sorted((c for c in all_chunks if c["url"] == r["url"]), key=lambda x: int(x["chunk_index"]))
    check_chunk_group(r, chunks)
    data = safe_path(r["repository_relative_path"]).read_bytes().lower()
    need(not any(term in data for term in (b"larch", b"scodeno", b"lanaotek")), "stopped-subject content quarantined")
assoc = next(r for r in web_other if "tubisad.org.tr" in r["url"])
need("body absent" in assoc["body_disposition"], "missing association body not disclosed")
need(b"152,7" not in safe_path(assoc["repository_relative_path"]).read_bytes(), "association page body unexpectedly changed")
market_video = next(r for r in web_other if "32J3cYQXCyM" in r["url"])
video = safe_path(market_video["repository_relative_path"]).read_text(encoding="utf8")
need("**Uploaded at**: 2022-12-06" in video and "**Published at**: \n" in video, "video date fields")
need("duyguları işe yarıyor Tabii ki" in video and "etkilemezdi hipotez ancak burada" in video, "hypothesis/result source text")
need("20 milyar liralık" in video and "156 milyon" in video and "153 milyon" in video, "transcript literal unit fields")
need("tasarımımız ama White Label ürünlerimiz" in video, "white-label source text")
recheck = rows(S / "web-manual-transcription-check.csv")
need(len(recheck) == 1 and recheck[0]["manual_retype_matches_saved"] == "true", "manual recheck status")
media_chunk = next(r for r in all_chunks if "globaltechmagazine.com" in r["url"] and r["chunk_index"] == "1")
need(media_chunk["sha256"] == recheck[0]["saved_chunk_sha256"] == recheck[0]["independently_manually_retyped_sha256"], "manual recheck hash")

incomplete = rows(S / "web-channel-video-incomplete-result.csv")
need(len(incomplete) == 1 and "INCOMPLETE QUARANTINED" in incomplete[0]["disposition"], "partial source not quarantined")
fragment = incomplete[0]
need(fragment["canonical_url"] == rows(S / "web-channel-video-scope-before-fetch.csv")[0]["url"], "incomplete canonical scope")
need(fragment["alias_url"] == rows(S / "web-channel-video-alias-scope-before-fetch.csv")[0]["url"], "incomplete alias scope")
partial = check_inv(fragment)
need(len(partial) == 17465 and "2-3 unavailable" in fragment["missing_or_inconsistent_chunks"], "partial size/completeness")
partial_chunks = rows(S / "web-channel-video-partial-chunk-inventory.csv")
need(len(partial_chunks) == 2, "partial chunk count")
offset = 0
for idx, row in enumerate(partial_chunks):
    start, end = int(row["start_byte"]), int(row["end_byte_exclusive"])
    need(int(row["chunk_index"]) == idx and row["tool_total_chunks"] == "4" and start == offset, "partial chunk metadata")
    need(end - start == int(row["bytes"]) and digest(partial[start:end]) == row["sha256"], "partial chunk bytes")
    need("QUARANTINED" in row["disposition"], "partial chunk disposition")
    offset = end
need(offset == len(partial) - 1, "partial chunk coverage")
responses = rows(S / "web-channel-video-response-metadata.csv")
need(len(responses) == 9 and {r["total_chunks_reported"] for r in responses} == {"4", "5", "6"}, "drift metadata")

characteristics = rows(S / "tool-text-byte-characteristics.csv")
need(len(characteristics) == 5 and sum(int(r["trailing_space_line_count"]) for r in characteristics) == 3, "source whitespace inventory")
need({r["repository_relative_path"] for r in characteristics} == {r["repository_relative_path"] for r in all_web} | {fragment["repository_relative_path"]}, "source whitespace paths")
for row in characteristics:
    check_whitespace(row)
attr_input = b"".join(r["repository_relative_path"].encode() + b"\0" for r in characteristics)
attributes = subprocess.run(["git", "check-attr", "-z", "--stdin", "text", "diff"], cwd=ROOT, input=attr_input, stdout=subprocess.PIPE, check=True).stdout.split(b"\0")
need(attributes.pop() == b"" and len(attributes) == 6 * len(characteristics), "Git attribute output")
attr_map = {(attributes[i].decode(), attributes[i + 1].decode()): attributes[i + 2].decode() for i in range(0, len(attributes), 3)}
for row in characteristics:
    name = row["repository_relative_path"]
    need(attr_map[(name, "text")] == "unset", "source text conversion disabled")
    if row["git_diff_attribute"] == "unset":
        need(attr_map[(name, "diff")] == "unset", "source whitespace Git diff policy")

anchors = rows(S / "evidence-traceability.csv")
need(len(anchors) == len({r["anchor_id"] for r in anchors}) == 57, "trace count")
for index, r in enumerate(anchors, 1):
    need(int(r["seq"]) == index and r["repository_relative_path"] != fragment["repository_relative_path"], "anchor sequence or partial used")
    check_anchor(r)
anchor_ids = {r["anchor_id"] for r in anchors}
issues = rows(S / "issues-and-corrections.csv")
hyp = rows(S / "hypothesis-versus-presented-result.csv")
samples = rows(S / "survey-accounting.csv")
ratios = rows(S / "market-unit-arithmetic.csv")
components = rows(S / "market-component-check.csv")
events = rows(S / "event-and-recording-chronology.csv")
need(len(issues) == 13 and len(hyp) == 3 and len(samples) == 8 and len(ratios) == 6 and len(components) == len(events) == 2, "matrix counts")
for r in issues + hyp + samples + ratios + components + events:
    need(set(r["anchors"].split(";")) <= anchor_ids, "unknown anchor reference")
for r in hyp:
    check_hypothesis(r)
for r in ratios:
    check_ratio(r)
for r in components:
    check_component(r)
lookup = {r["case"]: r for r in ratios}
need((lookup["old-156"]["numerator_TL"], lookup["old-156"]["denominator_TL"]) == ("2000000000", "156000000"), "old literal units")
need((lookup["video-156"]["numerator_TL"], lookup["video-156"]["denominator_TL"]) == ("20000000000", "156000000"), "caption literal units")
need((lookup["press-sector"]["numerator_TL"], lookup["press-sector"]["denominator_TL"], lookup["press-sector"]["ratio_percent"]) == ("20400000000", "152700000000", "13.3595"), "press units")
need(Decimal(20) * Decimal(10) ** 9 == Decimal(200) * Decimal(10) ** 8, "milyar to Chinese hundred million")
sample_map = {r["item"]: r["value"] for r in samples}
need(int(sample_map["responses_assessed"]) - int(sample_map["excluded"]) == int(sample_map["remaining_if_arithmetic"]) == 46, "sample difference")
for item, a, b in (("evaluated_divided_sent", 115, 1000), ("retained_divided_evaluated", 46, 115), ("retained_divided_sent", 46, 1000)):
    val = (Decimal(a) * 100 / Decimal(b)).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP)
    need(Decimal(sample_map[item].rstrip("%")) == val, "conditional sample ratio")

search_plans = rows(S / "discovery-plan-before-search.csv") + rows(S / "discovery-study-plan-before-search.csv")
search_results = rows(S / "discovery-metadata.csv") + rows(S / "discovery-study-metadata.csv")
need(len(search_plans) == len({r["query_id"] for r in search_plans}) == 9 and len(search_results) == 33, "search metadata counts")
need(all("-filetype:pdf" in r["query"] for r in search_plans), "search PDF guardrail")
pdf_results = [r for r in search_results if urlsplit(r["url"]).path.lower().endswith(".pdf")]
need(len(pdf_results) == 1 and pdf_results[0]["query_id"] == "Q06" and "not opened" in pdf_results[0]["disposition"], "unexpected PDF metadata")
need(all(r["query_id"] in {p["query_id"] for p in search_plans} for r in search_results), "unplanned query")

csv_files = sorted(P.rglob("*.csv")) + sorted(S.rglob("*.csv"))
record_count = 0
for p in csv_files:
    with p.open(encoding="utf8", newline="") as f:
        parsed = list(csv.reader(f, strict=True))
    need(parsed and len(set(parsed[0])) == len(parsed[0]), "invalid CSV header")
    need(all(len(r) == len(parsed[0]) for r in parsed[1:]), "invalid CSV width")
    record_count += len(parsed) - 1
docs = [P / "README.md", S / "README.md", W / "08-customer-pipeline/177-angora-koz-survey-channel-evidence-r108-2026-10-26.md", W / "09-orders/120-angora-orders-dossier-2026-10-21.r108-appendix.md", W / "09-orders/120-angora-orders-master-2026-10-21.mapping-r108.md", I / "58-followup-angora-r108-2026-10-26/angora-networks.md", I / "59-audit-r108-2026-10-26.md"]
links = sum(links_in(p, p.read_text(encoding="utf8")) for p in docs)
for r in append:
    p = safe_path(r["repository_relative_path"])
    links += links_in(p, p.read_bytes()[int(r["original_bytes"]):].decode("utf8"))

negative = []


def reject(label, func):
    try:
        func()
    except (AssertionError, KeyError, ValueError):
        negative.append(label)
        return
    raise AssertionError("negative test unexpectedly passed: " + label)


reject("bad hash", lambda: check_bytes(b"abcd", 4, "0" * 64))
reject("short prefix", lambda: check_bytes(b"abc", 4, digest(b"abcd"), exact=False))
reject("path escapes repo", lambda: safe_path("../../outside"))
bad = copy.deepcopy(anchors[0]); bad["anchor"] = "__not_in_source__"
reject("bad line anchor", lambda: check_anchor(bad))
reject("PDF URL", lambda: check_url("https://ictmedia.com.tr/example.pdf"))
reject("download URL", lambda: check_url("https://ictmedia.com.tr/download/123/"))
reject("unexpected host", lambda: check_url("https://example.org/test"))
bad = copy.deepcopy(ratios[0]); bad["ratio_percent"] = "13"
reject("inconsistent ratio", lambda: check_ratio(bad))
bad = copy.deepcopy(ratios[0]); bad["denominator_TL"] = "0"
reject("zero denominator", lambda: check_ratio(bad))
bad = copy.deepcopy(components[0]); bad["total_minus_components_billion_TL"] = "0"
reject("component mismatch", lambda: check_component(bad))
bad = copy.deepcopy(next(r for r in hyp if r["hypothesis_id"] == "H2")); bad["speaker_reported_result"] = "演讲者证实完全没用"
reject("reversed hypothesis result", lambda: check_hypothesis(bad))
bad = copy.deepcopy(all_chunks[0]); bad["sha256"] = "0" * 64
reject("corrupt chunk", lambda: check_chunk_group(web_event[0], [bad, all_chunks[1]]))
bad = copy.deepcopy(fragment); bad["sha256"] = "0" * 64
reject("corrupt isolated fragment", lambda: check_inv(bad))
reject("incomplete source anchor", lambda: check_eligible_source(fragment["repository_relative_path"]))
bad = copy.deepcopy(next(r for r in characteristics if int(r["trailing_space_line_count"]) > 0)); bad["trailing_space_line_count"] = "0"
reject("silent whitespace change", lambda: check_whitespace(bad))
reject("missing local link", lambda: check_link(S / "README.md", "__missing__.md"))
need(len(negative) == 16, "negative tests")

print("PASS r108 offline verifier")
print("24/24 local inputs, 214954 bytes; 5 first scoped under safety, 19 first listed under topic scope")
print("31/31 protected copies, 17455599 bytes; 7/7 historic finals; 4 append-prefix/suffix chains")
print("4 complete tool presentations, 9 chunks, 55878 bytes; association body unavailable")
print("1 additional channel video incomplete: 2/4 transcript chunks quarantined; 2 aliases not independent")
print("57 bound anchors; 13 issues; 3 hypotheses; 8 sample entries; 6 unit ratios; 2 component checks")
print("9 discovery queries, 33 metadata records; one unexpected unrelated PDF result not opened or used")
print(f"strict CSVs {len(csv_files)} / {record_count} records; local links {links}; negative tests {len(negative)}")
print("Not proven: read order, original HTML, complete transcription fidelity, audio, statements, certificates or delivery.")
