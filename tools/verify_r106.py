#!/usr/bin/env python3
"""Offline integrity and scope checks for the r106 Angora service dossier.

No network access, old verifier, device operation, or archive extraction. Hashes
identify saved bytes; they do not establish chronology, source truth, or that a
manual webpage transcription is byte-identical to a tool response.
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
P = I / "48-entry-safety-r106-2026-10-26"
S = I / "49-source-evidence-r106-2026-10-26"
BASE = "61d47150ce7c73854225d69b9c3bc72dc7c90547"
EXCLUDED_WEB = S / "external-visible/www.angoranetworks.com/angora-networks-_en/index.en.extracted.md"
EXCLUDED_OLD = I / "15-source-evidence-r97-2026-10-26/www.angoranetworks.com/angora-nms_en/index.en.extracted.md"
EXCLUDED = {str(EXCLUDED_WEB.relative_to(ROOT)), str(EXCLUDED_OLD.relative_to(ROOT))}


def need(condition, message):
    if not condition:
        raise AssertionError(message)


def readcsv(path):
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def path_for(path):
    result = (ROOT / path).resolve()
    need(result.is_relative_to(ROOT), f"outside workspace: {path}")
    return result


def check_bytes(data, size, sha, exact=True):
    need(len(data) == size if exact else len(data) >= size, "length mismatch")
    need(digest(data[:size]) == sha, "SHA-256 mismatch")


def check_inventory(record, size_key="bytes", path_key="repository_relative_path", sha_key="sha256"):
    path = record[path_key]
    data = path_for(path).read_bytes()
    size = int(record[size_key])
    check_bytes(data, size, record[sha_key], exact=path not in APPENDED)
    return data[:size]


def source_line(path, number, limit=None):
    data = path_for(path).read_bytes()
    if limit is not None:
        data = data[:limit]
    lines = data.decode("utf-8").split("\n")
    n = int(number) - 1
    need(0 <= n < len(lines), f"invalid line {path}:{number}")
    return lines[n]


def check_not_excluded(path):
    need(path not in EXCLUDED, "excluded page cannot be used as analysis evidence")


def check_anchor(record):
    check_not_excluded(record["repository_relative_path"])
    prefix = check_inventory(record, size_key="bytes_bound")
    lines = prefix.decode("utf-8").split("\n")
    n = int(record["line"]) - 1
    need(0 <= n < len(lines), "anchor line out of range")
    need(record["anchor"] in lines[n], "anchor text mismatch")


def check_url(url):
    parsed = urlsplit(url)
    need(parsed.scheme == "https" and parsed.netloc == "www.angoranetworks.com", "unexpected manufacturer URL")
    need(not parsed.path.lower().endswith(".pdf"), "PDF URL prohibited")
    need(not parsed.path.startswith(("/download/", "/qr/")), "download/QR URL prohibited")


def check_interview_url(url):
    parsed = urlsplit(url)
    need(parsed.scheme == "https" and parsed.netloc == "ictmedia.com.tr" and parsed.path.startswith("/haber/"), "unexpected interview URL")
    need(not parsed.path.lower().endswith(".pdf"), "interview PDF prohibited")


def check_chunk(data, record):
    start, end = int(record["start_byte"]), int(record["end_byte_exclusive"])
    need(0 <= start < end <= len(data), "invalid chunk offsets")
    part = data[start:end]
    need(len(part) == int(record["bytes"]) and digest(part) == record["sha256"], "interview chunk hash mismatch")


def single_replacements(data, needle, replacement):
    cursor = 0
    while True:
        index = data.find(needle, cursor)
        if index < 0:
            return
        yield data[:index] + replacement + data[index + len(needle):]
        cursor = index + 1


def check_service(record):
    for lang in ("tr", "en"):
        p = record[lang + "_path"]
        check_not_excluded(p)
        line = source_line(p, record[lang + "_line"])
        need(line == record[lang + "_literal"], "service literal mismatch")
        need(digest(line.encode()) == record[lang + "_line_sha256"], "service line hash mismatch")
    need("not contract" in record["limit"], "missing service evidence limit")


def check_training(record, service_by_id):
    row = service_by_id[record["item_id"]]
    need(row["category"] == "training", "course category mismatch")
    days = int(record["listed_duration_days"])
    for lang, suffix in (("tr", "gün"), ("en", "days")):
        need(record[lang + "_literal"] == row[lang + "_literal"], "training literal mismatch")
        need(record[lang + "_path"] == row[lang + "_path"] and record[lang + "_line"] == row[lang + "_line"], "training provenance mismatch")
        match = re.search(r"(\d+)\s*" + suffix, record[lang + "_literal"], flags=re.I)
        need(match is not None and int(match.group(1)) == days, "training duration mismatch")
    need("no class" in record["limit"], "training limit missing")


def check_cms_count(record):
    data = path_for(record["source_path"]).read_text(encoding="utf-8").split("\n")
    items = [line.split("\t")[0] for line in data if line.split("\t")[0].isdigit()]
    need(len(items) == len(set(items)) == int(record["numeric_id_data_rows"]) == int(record["distinct_ids"]), "stored TSV data count mismatch")
    need(int(record["saved_header_reported_rows"]) == 24, "expected saved header 24")
    need(len(items) - 24 == int(record["difference_data_rows_minus_header"]), "saved TSV header difference mismatch")


def check_web_entry(record):
    check_url(record["url"])
    need(record["chunk_count"] == "1" and record["has_more"] == "false" and record["fetch_status"] == "success", "web chunk mismatch")
    is_quarantined = record["repository_relative_path"] in EXCLUDED
    need(("quarantined" in record["analysis_status"]) == is_quarantined, "quarantine status mismatch")
    need("not original HTML" in record["representation"], "representation missing")
    check_inventory(record)


def check_local_link(doc, target):
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return False
    candidate = (doc.parent / unquote(urlsplit(target).path)).resolve()
    need(candidate.is_relative_to(ROOT) and candidate.is_file(), f"bad local link: {doc}: {target}")
    return True


def check_links(doc, text):
    return sum(int(check_local_link(doc, x)) for x in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text))


append_rows = readcsv(S / "append-log.csv")
APPENDED = {r["repository_relative_path"]: r for r in append_rows}
need(len(append_rows) == len(APPENDED) == 2, "append target count")
plans = readcsv(S / "append-plan-before-write.csv")
need({r["repository_relative_path"] for r in plans} == set(APPENDED), "append plan mismatch")
for plan in plans:
    p = plan["repository_relative_path"]
    r = APPENDED[p]
    need(plan["original_bytes"] == r["original_bytes"] and plan["original_sha256"] == r["original_sha256"], "append prefix plan mismatch")
    data = path_for(p).read_bytes()
    old, new = int(r["original_bytes"]), int(r["appended_bytes"])
    need(len(data) == old + new == int(r["new_bytes"]), "append length mismatch")
    check_bytes(data[:old], old, r["original_sha256"])
    check_bytes(data[old:], new, r["appended_sha256"])
    need(digest(data) == r["new_sha256"], "append final hash mismatch")
    git_original = subprocess.run(["git", "show", f"{BASE}:{p}"], cwd=ROOT, stdout=subprocess.PIPE, check=True).stdout
    need(git_original == data[:old], "Git baseline prefix changed")
need(sum(int(r["original_bytes"]) for r in append_rows) == 79373, "old prefix sum")
need(sum(int(r["appended_bytes"]) for r in append_rows) == 2442, "new suffix sum")

# Six named groups contain 20 distinct original inputs, including four prior indexes.
groups = [
    ("local-cms-scope-before-read.csv", "local-cms-read-inventory.csv", 2, 5858),
    ("local-method-scope-before-read.csv", "local-method-read-inventory.csv", 2, 8555),
    ("context-scope-before-read.csv", "context-read-inventory.csv", 6, 126312),
    ("local-existing-web-scope-before-read.csv", "local-existing-web-read-inventory.csv", 3, 12920),
    ("local-direct-scope-before-interpretation.csv", "local-direct-read-inventory.csv", 3, 20908),
    ("previous-index-scope-before-comparison.csv", "previous-index-read-inventory.csv", 4, 4699),
]
seen = set()
for scope_file, inventory_file, count, byte_count in groups:
    scope, inventory = readcsv(S / scope_file), readcsv(S / inventory_file)
    need(len(scope) == len(inventory) == count, f"group count: {inventory_file}")
    need(sum(int(r["bytes"]) for r in inventory) == byte_count, f"group bytes: {inventory_file}")
    need([(r["repository_relative_path"], r["bytes"]) for r in scope] == [(r["repository_relative_path"], r["bytes"]) for r in inventory], "scope/inventory mismatch")
    for r in inventory:
        need(r["repository_relative_path"] not in seen, "duplicate input path")
        seen.add(r["repository_relative_path"])
        check_inventory(r)
need(len(seen) == 20 and sum(g[3] for g in groups) == 179252, "local total mismatch")

# Safety data are checked by bytes only; no analysis of their business contents.
prior_scope, prior_read = readcsv(P / "prior-ledger-scope-before-read.csv"), readcsv(P / "prior-ledger-read-inventory.csv")
need(len(prior_scope) == len(prior_read) == 4, "prior ledger count")
need([(r["repository_relative_path"], r["bytes"]) for r in prior_scope] == [(r["repository_relative_path"], r["bytes"]) for r in prior_read], "prior ledger scope mismatch")
for r in prior_read:
    check_inventory(r)
protected_scope = readcsv(P / "protected-variants-scope-before-read.csv")
protected = readcsv(P / "protected-variants-read-inventory.csv")
need(len(protected_scope) == len(protected) == 31, "protected copies count")
need(sum(int(r["bytes"]) for r in protected) == 17455599, "protected copies size")
for scoped, record in zip(protected_scope, protected):
    for key in ("repository_relative_path", "bytes", "expected_sha256"):
        need(scoped[key] == record[key], "protected scope mismatch")
    need(record["sha256"] == record["expected_sha256"], "protected expected hash mismatch")
    check_inventory(record)
r105_scope = readcsv(P / "r105-append-final-scope-before-read.csv")
r105_final = readcsv(P / "r105-append-final-read-inventory.csv")
need(len(r105_scope) == len(r105_final) == 4, "r105 final target count")
for scoped, record in zip(r105_scope, r105_final):
    for key in ("repository_relative_path", "bytes", "expected_r105_final_sha256"):
        need(scoped[key] == record[key], "r105 safety scope mismatch")
    need(record["sha256"] == record["expected_r105_final_sha256"], "r105 original final hash mismatch")
    check_inventory(record)
need(sum(r["repository_relative_path"] in APPENDED for r in r105_final) == 2, "two prior protected files should be appended")
baseline = json.loads((P / "baseline.json").read_text(encoding="utf-8"))
need(baseline["session_date_supplied_utc"] == "2026-10-26" and baseline["environment_start_observed_utc"].startswith("2026-11-19T"), "clock conflict record missing")
need(baseline["head"] == BASE and baseline["remote_branch_head"] == BASE, "entry Git baseline mismatch")

# Saved webpage blocks; the about page is retained but never used as a claim source.
planned, web = readcsv(S / "web-initial-scope-before-fetch.csv"), readcsv(S / "web-visible-inventory.csv")
need(len(planned) == len(web) == 3 and len({r["url"] for r in web}) == 3, "web scope count")
need(sum(int(r["bytes"]) for r in web) == 8767, "web saved-byte count")
for p, r in zip(planned, web):
    need(p["url"] == r["url"], "URL plan mismatch")
    need((S / p["planned_path_from_r106_source_dir"]).resolve() == path_for(r["repository_relative_path"]), "URL artifact path mismatch")
    check_web_entry(r)
need(sum("quarantined" in r["analysis_status"] for r in web) == 1, "quarantined web count")
need(sum(int(r["bytes"]) for r in web if "quarantined" not in r["analysis_status"]) == 3868, "eligible web byte count")
need(sum(int(r["bytes"]) for r in web if "quarantined" in r["analysis_status"]) == 4899, "quarantined web byte count")

# One separately prelisted media URL with four response blocks assembled in source order.
queries = readcsv(S / "web-discovery-plan-before-search.csv")
discovery = readcsv(S / "web-discovery-metadata.csv")
need(len(queries) == 1 and len(discovery) == 5, "discovery metadata count")
need(all(r["query_id"] == queries[0]["query_id"] for r in discovery), "discovery query mismatch")
media_plan = readcsv(S / "web-interview-scope-before-fetch.csv")
media_rows = readcsv(S / "web-interview-visible-inventory.csv")
need(len(media_plan) == len(media_rows) == 1, "interview URL count")
media = media_rows[0]
check_interview_url(media["url"])
need(media["url"] == media_plan[0]["url"] == discovery[0]["url"], "interview URL plan mismatch")
need((S / media_plan[0]["planned_path_from_r106_source_dir"]).resolve() == path_for(media["repository_relative_path"]), "interview path mismatch")
need(media["bytes"] == "33069" and media["chunk_count"] == "4" and media["fetch_status"] == "success", "interview byte/chunk count")
need("not original HTML" in media["representation"], "interview representation missing")
media_bytes = check_inventory(media)
chunks = readcsv(S / "web-interview-chunk-inventory.csv")
need(len(chunks) == 4, "interview block count")
position = 0
for index, r in enumerate(chunks):
    need(int(r["chunk_index"]) == index and int(r["start_byte"]) == position and r["repository_relative_path"] == media["repository_relative_path"], "interview block ordering")
    check_chunk(media_bytes, r)
    position = int(r["end_byte_exclusive"])
need(position == len(media_bytes), "interview block coverage")
parts = [media_bytes[int(r["start_byte"]):int(r["end_byte_exclusive"])] for r in chunks]
need(parts[0].endswith(b"ekl") and parts[1].startswith(b"edik.") and parts[1].endswith(b"yapamayacak") and parts[2].startswith(b" ama") and parts[2].endswith(b"Mehmet Fatih K") and parts[3].startswith("ÖKSAL:".encode()), "interview block boundaries")
corrections = readcsv(S / "web-interview-transcription-corrections.csv")
need(len(corrections) == 2 and {r["chunk_index"] for r in corrections} == {"2", "3"}, "transcription correction log")
for r in corrections:
    index = int(r["chunk_index"])
    need(r["start_byte"] == chunks[index]["start_byte"] and r["after_bytes"] == chunks[index]["bytes"] and r["after_sha256"] == chunks[index]["sha256"], "transcription correction final state")
    need(len(r["before_sha256"]) == 64 and r["before_sha256"] != r["after_sha256"], "transcription correction prior hash")
# Reconstruct each prior draft in memory from the documented corrections, without changing source files.
by_chunk = {int(r["chunk_index"]): r for r in corrections}
new_spacing = "ürettiğimiz katma değerinde kalitesi".encode()
old_spacing = "ürettiğimiz katma değerin de kalitesi".encode()
need(parts[2].count(new_spacing) == 1, "spacing correction occurrence")
draft2 = parts[2].replace(new_spacing, old_spacing)
new_link = "](https://ictmedia.com.tr/haber/applycoder-kurucusu-mehmet-fatih-koksal-turkiyede-basaran-avrupa-ve-amerikada-cok-rahat-yapar-2)".encode()
old_link = "](https://ictmedia.com.tr/haber/applycoder-kurucusu-mehmet-fatih-koksal-roportaji-bolum-2-1783931981.webp)](https://ictmedia.com.tr/haber/applycoder-kurucusu-mehmet-fatih-koksal-turkiyede-basaran-avrupa-ve-amerikada-cok-rahat-yapar-2)".encode()
possible2 = [x for x in single_replacements(draft2, new_link, old_link) if len(x) == int(by_chunk[2]["before_bytes"]) and digest(x) == by_chunk[2]["before_sha256"]]
need(len(possible2) == 1, "interview block 2 prior draft hash")
new_spelling = b"yenal-arslan-dijital-donusum-teknoloji-satin-almak"
old_spelling = b"yenal-arslan-digital-donusum-teknoloji-satin-almak"
possible3 = [x for x in single_replacements(parts[3], new_spelling, old_spelling) if len(x) == int(by_chunk[3]["before_bytes"]) and digest(x) == by_chunk[3]["before_sha256"]]
need(len(possible3) == 1, "interview block 3 prior draft hash")
need(sum(int(r["bytes"]) for r in web) + int(media["bytes"]) == 41836, "combined web bytes")

anchors = readcsv(S / "evidence-traceability.csv")
need(len(anchors) == len({r["claim_id"] for r in anchors}) == 87, "anchor count or ID collision")
for index, record in enumerate(anchors, 1):
    need(int(record["seq"]) == index, "anchor sequence")
    check_anchor(record)
anchor_ids = {r["claim_id"] for r in anchors}
issues = readcsv(S / "issues-and-corrections.csv")
need(len(issues) == len({r["case"] for r in issues}) == 8, "issue count")
for r in issues:
    need(set(r["anchors"].split(";")) <= anchor_ids, "unknown correction anchor")

services = readcsv(S / "services-cross-language-items.csv")
need(len(services) == len({r["item_id"] for r in services}) == 21, "bilingual service count")
need(Counter(r["category"] for r in services) == {"strategy": 2, "implementation": 4, "outsourcing": 1, "hardware-support": 3, "software-support": 2, "training": 6, "documentation": 3}, "service category shape")
for r in services:
    check_service(r)
service_by_id = {r["item_id"]: r for r in services}
training = readcsv(S / "training-catalog-durations.csv")
need(len(training) == 6 and len({r["item_id"] for r in training}) == 6, "course count")
need(sorted(int(r["listed_duration_days"]) for r in training) == [2, 3, 3, 5, 5, 10], "course durations")
for r in training:
    check_training(r, service_by_id)

oem = readcsv(S / "oem-service-claim-matrix.csv")
need(len(oem) == len({r["capability_id"] for r in oem}) == 6, "OEM matrix count")
for r in oem:
    check_not_excluded(r["source_path"])
    line = source_line(r["source_path"], r["source_line"])
    need(line == r["literal_line"] and digest(line.encode()) == r["source_line_sha256"], "OEM literal/hash mismatch")
    need(r["limit"], "OEM limit missing")
interview_claims = readcsv(S / "interview-claim-matrix.csv")
need(len(interview_claims) == len({r["claim_id"] for r in interview_claims}) == 9, "interview claim count")
for r in interview_claims:
    need(r["source_path"] == media["repository_relative_path"], "interview source path mismatch")
    check_not_excluded(r["source_path"])
    line = source_line(r["source_path"], r["source_line"])
    need(r["anchor"] in line and digest(line.encode()) == r["source_line_sha256"], "interview anchor mismatch")
    need(r["limit"], "interview claim limit missing")
history = readcsv(S / "historical-design-text-lines.csv")
need(len(history) == 17 and Counter(r["record_case"] for r in history) == {"A": 6, "B": 11}, "history line count")
need(len({r["source_path"] for r in history}) == 2, "history source separation")
for r in history:
    check_not_excluded(r["source_path"])
    line = source_line(r["source_path"], r["source_line"])
    need(line == r["literal_line"] and digest(line.encode()) == r["source_line_sha256"], "historical text line mismatch")
    need("not independently established" in r["limit"], "history limit missing")

# Old stored TSVs; not current website requests.
cms_count = readcsv(S / "cms-saved-row-counts.csv")
need(len(cms_count) == 2, "saved TSV count")
for r in cms_count:
    check_cms_count(r)
cms = readcsv(S / "cms-service-fields-comparison.csv")
need(len(cms) == 2 and {r["wp_id"] for r in cms} == {"1152", "275"}, "service CMS comparison count")
for r in cms:
    for version in ("r39", "r40"):
        line = source_line(r[version + "_source_path"], r[version + "_line"])
        need(digest(line.encode()) == r[version + "_line_sha256"], "CMS line hash mismatch")
        cells = line.split("\t")
        need(cells[0] == r["wp_id"] and cells[1] == r["date_literal"] and cells[2] == r["modified_literal"] and cells[-1] == r["url_literal"], "CMS literal field mismatch")
relevant = readcsv(S / "cms-relevant-page-rows.csv")
need(len(relevant) == 6, "CMS metadata rows")
for r in relevant:
    line = source_line(r["source_path"], r["line"])
    cells = line.split("\t")
    need(digest(line.encode()) == r["line_sha256"] and cells[0] == r["id"] and cells[1] == r["date_literal"] and cells[2] == r["modified_literal"] and cells[-1] == r["url"], "CMS metadata mismatch")

prior = set()
for name in ("local-read-inventory.csv", "context-prefix-read-inventory.csv", "previous-index-read-inventory.csv", "additional-read-inventory.csv"):
    prior.update(r["repository_relative_path"] for r in readcsv(I / "45-source-evidence-r105-2026-10-26" / name))
need(len(prior) == 24, "r105 input scope mismatch")
overlap = readcsv(S / "overlap-r105-24.csv")
need(len(overlap) == 16 and len({r["repository_relative_path"] for r in overlap}) == 16, "overlap input count")
need(all((r["in_r105_24"] == "True") == (r["repository_relative_path"] in prior) for r in overlap), "overlap membership mismatch")
need(sum(r["in_r105_24"] == "True" for r in overlap) == 7, "overlap count mismatch")

# Only r106-created Markdown and current suffixes are checked; excluded pages are not scanned.
documents = [P / "README.md", S / "README.md", W / "08-customer-pipeline/175-angora-design-service-delivery-r106-2026-10-26.md", W / "09-orders/120-angora-orders-dossier-2026-10-21.r106-appendix.md", W / "09-orders/120-angora-orders-master-2026-10-21.mapping-r106.md", I / "50-followup-angora-r106-2026-10-26/angora-networks.md", I / "51-audit-r106-2026-10-26.md"]
links = sum(check_links(p, p.read_text(encoding="utf-8")) for p in documents)
for r in append_rows:
    p = path_for(r["repository_relative_path"])
    suffix = p.read_bytes()[int(r["original_bytes"]):].decode("utf-8")
    links += check_links(p, suffix)

# In-memory mutations demonstrate validators reject altered evidence; no source is changed.
negative = []


def reject(label, action):
    try:
        action()
    except (AssertionError, KeyError):
        negative.append(label)
        return
    raise AssertionError("negative test unexpectedly passed: " + label)


reject("bad source hash", lambda: check_bytes(b"abcd", 4, "0" * 64))
reject("short prefix", lambda: check_bytes(b"abc", 4, digest(b"abcd"), exact=False))
bad_anchor = copy.deepcopy(anchors[0]); bad_anchor["anchor"] = "__absent_anchor__"
reject("bad anchor", lambda: check_anchor(bad_anchor))
bad_excluded = copy.deepcopy(anchors[0]); bad_excluded["repository_relative_path"] = str(EXCLUDED_WEB.relative_to(ROOT))
reject("excluded page anchor", lambda: check_anchor(bad_excluded))
reject("PDF URL", lambda: check_url("https://www.angoranetworks.com/example.pdf"))
reject("download URL", lambda: check_url("https://www.angoranetworks.com/download/123/"))
reject("interview PDF URL", lambda: check_interview_url("https://ictmedia.com.tr/haber/example.pdf"))
bad_chunk = copy.deepcopy(chunks[2]); bad_chunk["sha256"] = "0" * 64
reject("changed interview chunk", lambda: check_chunk(media_bytes, bad_chunk))
bad_service = copy.deepcopy(services[0]); bad_service["tr_literal"] = "__altered__"
reject("changed service literal", lambda: check_service(bad_service))
bad_course = copy.deepcopy(training[0]); bad_course["listed_duration_days"] = "99"
reject("changed course duration", lambda: check_training(bad_course, service_by_id))
bad_count = copy.deepcopy(cms_count[0]); bad_count["numeric_id_data_rows"] = "24"
reject("wrong stored TSV count", lambda: check_cms_count(bad_count))
bad_quarantine = copy.deepcopy(next(r for r in web if "quarantined" in r["analysis_status"])); bad_quarantine["analysis_status"] = "eligible"
reject("quarantine mislabel", lambda: check_web_entry(bad_quarantine))
reject("missing local link", lambda: check_local_link(S / "README.md", "__missing__.md"))
need(len(negative) == 13, "negative test count")

print("PASS r106 offline verifier")
print("local scope 20/20 paths, 179252 original bytes; four first listed and read earlier under safety scopes")
print("safety 31/31 protected copies, 17455599 bytes; 4/4 r105 prefixes; 2/2 append baselines and suffixes")
print("web 4/4 URLs, 7/7 chunks, 41836 saved bytes; 3 eligible pages and 1 quarantined; one old NMS page also excluded")
print("87 anchors; 8 named limitations; 21 bilingual items; 6 courses; 6 OEM claims; 9 interview claims; 17 historical text lines")
print("two stored TSVs x 25 IDs; two service-ID field comparisons; 7/16 overlap with r105")
print(f"local links {links}; in-memory negative tests {len(negative)}")
print("Not verified: historical execution order, webpage raw-byte fidelity, vendor claims, contracts, service delivery or devices.")
