#!/usr/bin/env python3
"""Offline verification of the bounded r105 Angora source ledger and arithmetic.

No network, no old verifiers, no archive extraction, no device operation.  A
hash proves which local bytes were recorded, not that a web transcription is
identical to its tool response or that a vendor's claims are true.  Historical
read order is an explicitly disclosed session-record claim, not reconstructible
from a file's hash.
"""
from __future__ import annotations

import copy
import csv
import hashlib
import json
import re
import subprocess
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
I = ROOT / "ingest/angora-1__arena-01a0ce39__5acb613"
S = I / "45-source-evidence-r105-2026-10-26"
E = S / "external-visible/www.angoranetworks.com"
W = I / "01-text-verbatim/workstation"
BASE = "73d2c9d010ac36875a19fe23edfcd885234c73a6"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def rows(path):
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def local(path):
    candidate = (ROOT / path).resolve()
    require(candidate.is_relative_to(ROOT), f"path outside repository: {path}")
    return candidate


def decimal2(value):
    return str(Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def validate_bytes(data, length, expected_hash, exact=True):
    require(len(data) == length if exact else len(data) >= length, "byte length mismatch")
    require(digest(data[:length]) == expected_hash, "SHA-256 mismatch")


def validated_record(record, pathkey="repository_relative_path", lengthkey="bytes", hashkey="sha256"):
    path = record[pathkey]
    data = local(path).read_bytes()
    validate_bytes(data, int(record[lengthkey]), record[hashkey], exact=path not in APPENDED)
    return data[: int(record[lengthkey])]


def line_at(path, line_number, bound=None):
    data = local(path).read_bytes()
    if bound is not None:
        data = data[:bound]
    lines = data.decode("utf-8").split("\n")
    index = int(line_number) - 1
    require(0 <= index < len(lines), f"line not found: {path}:{line_number}")
    return lines[index]


def validate_anchor(record):
    prefix = validated_record(record, lengthkey="bytes_bound")
    lines = prefix.decode("utf-8").split("\n")
    index = int(record["line"]) - 1
    require(0 <= index < len(lines), f"bad anchor line: {record['claim_id']}")
    require(record["anchor"] in lines[index], f"bad anchor text: {record['claim_id']}")


def validate_url(url):
    parsed = urlsplit(url)
    require(parsed.scheme == "https" and parsed.netloc == "www.angoranetworks.com", "unexpected URL host")
    require(not parsed.path.lower().endswith(".pdf"), "PDF URL prohibited")
    require(not parsed.path.startswith(("/download/", "/qr/")), "download/QR URL prohibited")


def parse_table_row(line):
    require(line.startswith("|"), "not a Markdown table row")
    return [part.strip() for part in line.strip().strip("|").split("|")]


def validate_poe(row, web_cells):
    sku = row["sku"]
    count = int(row["poe_port_count_assumed"])
    per_port = int(row["hypothetical_watts_per_PSE_port"])
    budget = int(row["web_budget_watts"])
    require(web_cells[(sku, "Gigabit PoE+")] == str(count), "PoE port assumption not tied to source")
    cell = web_cells[(sku, "PoE Bütçesi")]
    config = row["web_budget_configuration"]
    if config in ("AC", "DC"):
        require(f"{budget}W ({config})" in cell, "AC/DC budget not tied to source")
    else:
        require(config == "unspecified in cell" and cell == f"{budget}W", "budget not tied to source")
    require(per_port in (15, 30), "unexpected hypothetical per-port power")
    require(int(row["hypothetical_total_watts"]) == count * per_port, "PoE total incorrect")
    require(int(row["budget_minus_hypothetical_watts"]) == budget - count * per_port, "PoE difference incorrect")
    require(row["equal_share_budget_watts_per_port"] == decimal2(Decimal(budget) / count), "PoE average incorrect")
    require("not" in row["limit"].lower() or "neither" in row["limit"].lower(), "missing PoE limit")


def validate_switch(row, web_cells):
    sku = row["sku"]
    access = int(row["access_ports_assumed"])
    uplinks = int(row["uplink_ports_assumed"])
    require(web_cells[(sku, "Gigabit PoE+")] == str(access), "access count not tied to source")
    require(web_cells[(sku, "10G/GE SFP+")] == str(uplinks), "uplink count not tied to source")
    require(int(row["access_max_gbps_assumed"]) == 1 and int(row["uplink_max_gbps_assumed"]) == 10, "unexpected speed assumption")
    gbps = access + 10 * uplinks
    require(int(row["sum_one_direction_gbps"]) == gbps, "port-rate sum incorrect")
    require(int(row["sum_full_duplex_gbps"]) == 2 * gbps, "duplex-rate sum incorrect")
    require(row["web_switching_gbps"] == web_cells[(sku, "Anahtarlama Kapasitesi (Gbps)")], "source switching capacity mismatch")
    require(row["web_forwarding_mpps"] == web_cells[(sku, "Paket İletim Hızı (Mpps)")], "source forwarding Mpps mismatch")
    minimum_packet_mpps = Fraction(gbps * 1000, 84 * 8)
    expected = decimal2(Decimal(minimum_packet_mpps.numerator) / minimum_packet_mpps.denominator)
    require(row["nominal_one_direction_min_frame_mpps"] == expected, "minimum-frame estimate incorrect")
    require("no throughput test" in row["limit"], "missing switch calculation limit")


def check_local_link(document, target):
    if target.startswith(("https://", "http://", "mailto:", "#")):
        return False
    parts = urlsplit(target)
    candidate = (document.parent / unquote(parts.path)).resolve()
    require(candidate.is_relative_to(ROOT), f"link outside repository: {document}: {target}")
    require(candidate.is_file(), f"missing local link: {document}: {target}")
    return True


def validate_links(document, text):
    count = 0
    for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
        count += int(check_local_link(document, target))
    return count


append_rows = rows(S / "append-log.csv")
APPENDED = {r["repository_relative_path"]: r for r in append_rows}
require(len(APPENDED) == len(append_rows) == 4, "expected four append-only targets")
plan = rows(S / "append-plan-before-write.csv")
require({r["repository_relative_path"] for r in plan} == set(APPENDED), "append plan mismatch")
for r in plan:
    p = r["repository_relative_path"]
    log = APPENDED[p]
    require(r["original_bytes"] == log["original_bytes"] and r["original_sha256"] == log["original_sha256"], "append plan differs")
    full = local(p).read_bytes()
    original_length, suffix_length = int(log["original_bytes"]), int(log["appended_bytes"])
    require(len(full) == original_length + suffix_length == int(log["new_bytes"]), "append total mismatch")
    validate_bytes(full[:original_length], original_length, log["original_sha256"])
    validate_bytes(full[original_length:], suffix_length, log["appended_sha256"])
    require(digest(full) == log["new_sha256"], "final append hash mismatch")
    baseline = subprocess.run(["git", "show", f"{BASE}:{p}"], cwd=ROOT, check=True, stdout=subprocess.PIPE).stdout
    require(baseline == full[:original_length], "Git baseline prefix changed")
require(sum(int(r["original_bytes"]) for r in append_rows) == 95306, "prefix byte total mismatch")
require(sum(int(r["appended_bytes"]) for r in append_rows) == 3755, "suffix byte total mismatch")
revision = rows(S / "append-suffix-revision-log.csv")
require(len(revision) == 1, "expected one recorded suffix wording revision")
revision = revision[0]
changed = APPENDED[revision["repository_relative_path"]]
require(revision["original_prefix_sha256"] == changed["original_sha256"], "revision prefix mismatch")
suffix = local(revision["repository_relative_path"]).read_bytes()[int(changed["original_bytes"]):]
require(len(suffix) == int(revision["revised_suffix_bytes"]) and digest(suffix) == revision["revised_suffix_sha256"] == changed["appended_sha256"], "revised suffix mismatch")
old_wording = '把“单口 up to 30W”扩展为全口同时 30W'.encode("utf-8")
new_wording = '把厂商“Up to 30Watts from all ports”直接解读为全口同时各 30W'.encode("utf-8")
require(suffix.count(new_wording) == 1, "new wording must occur exactly once")
reconstructed = suffix.replace(new_wording, old_wording)
require(len(reconstructed) == int(revision["previous_suffix_bytes"]) and digest(reconstructed) == revision["previous_suffix_sha256"], "previous suffix revision hash mismatch")

# Four disjoint, fully read local groups. The fourth was listed only after first access.
groups = [
    ("local-scope-before-read.csv", "local-read-inventory.csv", 7, 22889),
    ("context-scope-before-read.csv", "context-prefix-read-inventory.csv", 7, 153411),
    ("previous-index-scope-before-read.csv", "previous-index-read-inventory.csv", 6, 8979),
    ("additional-scope-after-first-read.csv", "additional-read-inventory.csv", 4, 18967),
]
all_paths = set()
for scope_name, inventory_name, count, total in groups:
    scope, inventory = rows(S / scope_name), rows(S / inventory_name)
    require(len(scope) == len(inventory) == count, f"count mismatch: {inventory_name}")
    require(sum(int(r["bytes"]) for r in inventory) == total, f"byte total mismatch: {inventory_name}")
    require([(r["repository_relative_path"], r["bytes"]) for r in scope] == [(r["repository_relative_path"], r["bytes"]) for r in inventory], "scope/inventory mismatch")
    for record in inventory:
        require(record["repository_relative_path"] not in all_paths, "duplicate path in the four groups")
        all_paths.add(record["repository_relative_path"])
        validated_record(record)
require(len(all_paths) == 24 and sum(g[3] for g in groups) == 204246, "local scope total mismatch")

# Safety copies are separate from the 24 analytical inputs.
P = I / "44-entry-safety-r105-2026-10-26"
ledger = rows(P / "prior-ledger-read-inventory.csv")
require(len(ledger) == 1, "prior safety ledger count")
validated_record(ledger[0])
protected = rows(P / "protected-variants-read-inventory.csv")
protected_scope = rows(P / "protected-variants-scope-before-read.csv")
require(len(protected) == len(protected_scope) == 31, "protected variants count")
require(sum(int(r["bytes"]) for r in protected) == 17455599, "protected variants byte total")
for actual, scoped in zip(protected, protected_scope):
    for key in ("seq", "repository_relative_path", "bytes", "expected_incoming_sha256"):
        require(actual[key] == scoped[key], f"protected scope mismatch: {key}")
    require(actual["sha256"] == actual["expected_incoming_sha256"], "protected copy differs from recorded incoming hash")
    validated_record(actual)
prior_final = rows(S / "r104-final-protection-inventory.csv")
require(len(prior_final) == 6, "r104 final protection count")
for r in prior_final:
    validated_record(r)
require(sum(r["repository_relative_path"] in APPENDED for r in prior_final) == 2, "two r104 protected files should be appended only")

baseline = json.loads((P / "baseline.json").read_text(encoding="utf-8"))
require(baseline["session_date_supplied_utc"] == "2026-10-26", "session date should not be replaced by environment clock")
require(baseline["environment_start_observed_utc"].startswith("2026-11-19T"), "environment-clock observation missing")
require(baseline["head"] == BASE, "baseline commit mismatch")

# Five separately transcribed manufacturer pages; no network requests.
plans = rows(S / "web-initial-scope-before-fetch.csv") + rows(S / "web-supplement-scope-before-fetch.csv")
web = rows(S / "web-visible-inventory.csv")
require(len(plans) == len(web) == 5 and len({r["url"] for r in web}) == 5, "website scope count")
require(sum(int(r["bytes"]) for r in web) == 22840, "saved website bytes")
for planned, saved in zip(plans, web):
    require(planned["url"] == saved["url"], "planned/saved URL mismatch")
    require((S / planned["planned_path_from_r105_source_dir"]).resolve() == local(saved["repository_relative_path"]), "planned/saved file mismatch")
    validate_url(saved["url"])
    require(saved["chunk_count"] == "1" and saved["fetch_status"] == "success", "unexpected tool chunk or status")
    require("not original HTML" in saved["representation"], "representation must be explicit")
    validated_record(saved)
queries, discovery = rows(S / "web-query-plan-02-before-search.csv"), rows(S / "web-discovery-metadata.csv")
require(len(queries) == 3 and len(discovery) == 15, "discovery metadata count")
require({q["query_id"] for q in queries} == {r["query_id"] for r in discovery}, "discovery query IDs")
require(all(sum(r["query_id"] == q["query_id"] for r in discovery) == 5 for q in queries), "search-result counts")

# Line anchors bind to exact original bytes, including original prefix if appended.
anchors = rows(S / "evidence-traceability.csv")
require(len(anchors) == 50 and len({r["claim_id"] for r in anchors}) == 50, "anchor count/IDs")
for index, record in enumerate(anchors, 1):
    require(int(record["seq"]) == index, "anchor order")
    validate_anchor(record)
issues = rows(S / "issues-and-corrections.csv")
require(len(issues) == 13 and len({r["case"] for r in issues}) == 13, "issue count")
anchor_ids = {r["claim_id"] for r in anchors}
for r in issues:
    require(set(r["evidence_anchor_ids"].split(";")) <= anchor_ids, "unknown issue anchor")

# Hitit: compare exact table cells and old-summary SKU strings, not hardware identity.
hitit_source = E / "hitit-yerli-network-switch-ailesi/index.tr.extracted.md"
hitit_lines = hitit_source.read_text(encoding="utf-8").split("\n")
hitit_rows = rows(S / "hitit-web-model-rows.csv")
require(len(hitit_rows) == 11 and len({r["sku"] for r in hitit_rows}) == 11, "Hitit model count")
for r in hitit_rows:
    line = line_at(r["source_path"], r["source_line"])
    require(digest(line.encode()) == r["source_line_sha256"], "Hitit line hash")
    cells = [value.replace("**", "") for value in parse_table_row(line)]
    require(cells == [r["sku"], r["ports_as_visible"], r["poe_budget_as_visible"], r["mount_as_visible"], r["segment_as_visible"]], "Hitit literal cells mismatch")
require(sum(bool(re.match(r"^\| (?:\*\*)?ANW-", line)) for line in hitit_lines) == 11, "Hitit page row coverage")
crossrefs = rows(S / "hitit-model-name-crossrefs.csv")
require({r["sku"] for r in crossrefs} == {r["sku"] for r in hitit_rows} and len(crossrefs) == 11, "Hitit name crossrefs")
for r in crossrefs:
    for prefix, field in (("live", "live"), ("old_summary", "old_summary")):
        line = line_at(r[f"{field}_source_path"] if field == "live" else r["old_summary_path"], r[f"{prefix}_line"])
        require(r["sku"] in line and digest(line.encode()) == r[f"{prefix}_line_sha256"], "Hitit crossref line mismatch")

hitit_budget = rows(S / "hitit-budget-conditional.csv")
require(len(hitit_budget) == 8 and len({r["sku"] for r in hitit_budget}) == 8, "Hitit PoE row count")
hitit_lookup = {r["sku"]: r for r in hitit_rows}
for r in hitit_budget:
    src = hitit_lookup[r["sku"]]
    match = re.match(r"^(\d+) port", src["ports_as_visible"])
    require(match is not None and int(match.group(1)) == int(r["listed_poe_port_count"]), "Hitit assumed port count")
    require(src["poe_budget_as_visible"] == r["poe_budget_watts"] + "W", "Hitit budget value")
    require(r["equal_share_budget_watts_per_port"] == decimal2(Decimal(r["poe_budget_watts"]) / int(r["listed_poe_port_count"])), "Hitit equal-share arithmetic")
    require(r["source_line_sha256"] == src["source_line_sha256"] and r["source_line"] == src["source_line"], "Hitit budget provenance")

# Synapse: retain only full five-column rows; don't fill merged single-cell rows.
synapse_source = E / "synapse-network-switch-ailesi/index.tr.extracted.md"
synapse_lines = synapse_source.read_text(encoding="utf-8").split("\n")
header = next(parse_table_row(line) for line in synapse_lines if line.startswith("| Özellik | ANW-2712-"))
models = header[1:]
require(len(models) == 5, "Synapse model header")
literal = rows(S / "synapse-five-model-literal-cells.csv")
require(len(literal) == 55, "Synapse cell count")
web_cells = {}
for r in literal:
    line = line_at(r["source_path"], r["source_line"])
    require(digest(line.encode()) == r["source_line_sha256"], "Synapse source line hash")
    cells = parse_table_row(line)
    require(len(cells) == 6 and cells[0] == r["website_row_literal"], "Synapse row shape")
    require(r["sku"] in models and cells[1 + models.index(r["sku"])] == r["website_cell_literal"], "Synapse literal cell mismatch")
    key = (r["sku"], r["website_row_literal"])
    require(key not in web_cells, "duplicate Synapse cell")
    web_cells[key] = r["website_cell_literal"]
require(len({r["website_row_literal"] for r in literal}) == 11 and len(web_cells) == 5 * 11, "Synapse matrix shape")
selected = rows(S / "synapse-selected-models.csv")
require(len(selected) == 3 and len({r["sku"] for r in selected}) == 3, "Synapse selected models")
field_map = {"poe_ports_cell": "Gigabit PoE+", "uplink_cell": "10G/GE SFP+", "switching_gbps_cell": "Anahtarlama Kapasitesi (Gbps)", "forwarding_mpps_cell": "Paket İletim Hızı (Mpps)", "poe_budget_cell": "PoE Bütçesi", "fans_cell": "Fan Sayısı"}
for r in selected:
    for field, website in field_map.items():
        require(r[field] == web_cells[(r["sku"], website)], "selected Synapse cell mismatch")
    historic = line_at(r["historic_summary_path"], r["historic_summary_line"])
    require(r["sku"] in historic and digest(historic.encode()) == r["historic_summary_line_sha256"], "historic Synapse row")
poe = rows(S / "poe-conditional-arithmetic.csv")
require(len(poe) == 12 and len({(r["sku"], r["web_budget_configuration"], r["hypothetical_watts_per_PSE_port"]) for r in poe}) == 12, "PoE cases")
for r in poe:
    validate_poe(r, web_cells)
switching = rows(S / "switching-conditional-arithmetic.csv")
require(len(switching) == 4 and len({r["sku"] for r in switching}) == 4, "switching cases")
for r in switching:
    validate_switch(r, web_cells)

# Four old saved CMS fields in two independent paths; neither path is a live API call.
times = rows(S / "page-timestamp-fields.csv")
require(len(times) == 4 and len({r["wp_id"] for r in times}) == 4, "stored page time count")
for r in times:
    for prefix in ("r39", "r40"):
        line = line_at(r[prefix + "_index_path"], r[prefix + "_line"])
        require(digest(line.encode()) == r[prefix + "_line_sha256"], "old TSV line hash")
        cells = line.split("\t")
        require(cells[0] == r["wp_id"] and cells[1] == r["date_literal"] and cells[2] == r["modified_literal"] and cells[-1] == r["url"], "old TSV literal mismatch")

prior_names = ["local-product-read-inventory.csv", "local-method-read-inventory.csv", "date-audit-read-inventory.csv", "context-prefix-read-inventory.csv", "overlap-check-inputs-after-first-read.csv"]
prior = set()
for name in prior_names:
    prior.update(r["repository_relative_path"] for r in rows(I / "41-source-evidence-r104-2026-10-26" / name))
require(len(prior) == 35, "r104 comparison scope")
for group, overlap, expected in [("local-read-inventory.csv", "overlap-r104-local.csv", 4), ("context-prefix-read-inventory.csv", "overlap-r104-context.csv", 6)]:
    recorded = rows(S / overlap)
    paths = [r["repository_relative_path"] for r in rows(S / group)]
    require([r["repository_relative_path"] for r in recorded] == paths, "overlap row order")
    require(all((r["in_r104_35"] == "True") == (r["repository_relative_path"] in prior) for r in recorded), "overlap membership")
    require(sum(r["in_r104_35"] == "True" for r in recorded) == expected, "overlap count")

# Check links only in r105-created documents and appended suffixes; old documents are not reprocessed.
new_documents = [
    P / "README.md", S / "README.md",
    W / "08-customer-pipeline/174-angora-switch-portfolio-lifecycle-r105-2026-10-26.md",
    W / "09-orders/120-angora-orders-dossier-2026-10-21.r105-appendix.md",
    W / "09-orders/120-angora-orders-master-2026-10-21.mapping-r105.md",
    I / "46-followup-angora-r105-2026-10-26/angora-networks.md",
    I / "47-audit-r105-2026-10-26.md",
]
link_count = sum(validate_links(path, path.read_text(encoding="utf-8")) for path in new_documents)
for record in append_rows:
    path = local(record["repository_relative_path"])
    suffix = path.read_bytes()[int(record["original_bytes"]):].decode("utf-8")
    link_count += validate_links(path, suffix)

# In-memory mutation tests. None modifies disk, a source, or a device.
negative = []


def reject(label, action):
    try:
        action()
    except (AssertionError, KeyError):
        negative.append(label)
        return
    raise AssertionError("negative test unexpectedly accepted: " + label)


reject("modified source hash", lambda: validate_bytes(b"different", 9, "0" * 64))
reject("short original prefix", lambda: validate_bytes(b"abc", 4, digest(b"abcd"), exact=False))
bad_anchor = copy.deepcopy(anchors[0]); bad_anchor["anchor"] = "__missing_anchor__"
reject("changed anchor", lambda: validate_anchor(bad_anchor))
bad_anchor_line = copy.deepcopy(anchors[0]); bad_anchor_line["line"] = "999999"
reject("invalid anchor line", lambda: validate_anchor(bad_anchor_line))
reject("prohibited PDF URL", lambda: validate_url("https://www.angoranetworks.com/example.pdf"))
reject("prohibited download URL", lambda: validate_url("https://www.angoranetworks.com/download/123/"))
bad_poe = copy.deepcopy(poe[0]); bad_poe["hypothetical_total_watts"] = "0"
reject("incorrect PoE arithmetic", lambda: validate_poe(bad_poe, web_cells))
bad_budget = copy.deepcopy(poe[0]); bad_budget["web_budget_watts"] = "999"
reject("unfounded PoE budget", lambda: validate_poe(bad_budget, web_cells))
bad_switch = copy.deepcopy(switching[0]); bad_switch["nominal_one_direction_min_frame_mpps"] = "0"
reject("incorrect packet rate", lambda: validate_switch(bad_switch, web_cells))
bad_source_value = copy.deepcopy(switching[0]); bad_source_value["web_switching_gbps"] = "999"
reject("unfounded switching value", lambda: validate_switch(bad_source_value, web_cells))
reject("missing local link", lambda: check_local_link(S / "README.md", "__no_such_file__.md"))
require(len(negative) == 11, "negative test count")

print("PASS r105 offline verifier")
print("local research inputs 24/24, 204246 bytes; 4 additional inputs accessed before list")
print("safety: 31/31 protected copies, 17455599 bytes; 4/4 append prefixes and suffixes; 6/6 r104 prefixes")
print("web: 5/5 URLs, 5/5 chunks, 22840 locally saved bytes; 3 discovery queries, 15 metadata rows")
print(f"anchors {len(anchors)}; issues {len(issues)}; Hitit 11 rows/11 crossrefs/8 budget cases")
print("Synapse 55 literal cells, 12 PoE cases, 4 switching cases; 4 old timestamp rows")
print(f"local links {link_count}; negative in-memory tests {len(negative)}")
print("Not verified: webpage raw-byte fidelity, historic execution chronology, vendor claims, hardware, deployment, or certification.")
