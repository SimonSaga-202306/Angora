#!/usr/bin/env python3
"""Read-only verification of r100's *local derivatives*, not source authenticity.

No network access, customer contact, package execution or archive extraction.
Hashes do not verify that human reading happened, that OCR is accurate, that
historical metadata identifies an unavailable original, or that a device ever
received, installed, or ran any firmware.
"""
from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
from collections import Counter
from hashlib import sha256
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
I = ROOT / "ingest/angora-1__arena-01a0ce39__5acb613"
W = I / "01-text-verbatim/workstation"
S = I / "25-source-evidence-r100-2026-10-26"
F = I / "05-nontext-content/firmware/3rd order 176台2光16电 L2 PoE/lite-hotfix-7.3.13.bin"
T = F / "rootfs-text"
R = W / "08-customer-pipeline/169-angora-firmware-traceability-r100-2026-10-26.md"
M = W / "09-orders/120-angora-orders-master-2026-10-21.mapping-r100.md"
A = I / "27-audit-r100-2026-10-26.md"
FOLLOW = I / "26-followup-angora-r100-2026-10-26"


def require(ok: bool, why: str) -> None:
    if not ok:
        raise ValueError(why)


def rows(path: Path, delimiter: str = ",") -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter=delimiter))


def validate(data: bytes, size: int, digest: str, label: str) -> None:
    require(len(data) == size, f"size mismatch: {label}")
    require(sha256(data).hexdigest() == digest, f"SHA-256 mismatch: {label}")


def inventory() -> tuple[list[dict[str, str]], str]:
    specs = [
        ("selected-scope-before-read.csv", "selected-read-inventory.csv", 15, 840574),
        ("rootfs-text-scope-before-read.csv", "rootfs-text-read-inventory.csv", 4881, 39164587),
        ("supplement-wechat-scope-before-read.csv", "supplement-wechat-read-inventory.csv", 4, 1569064),
        ("supplement-ocr-scope-before-read.csv", "supplement-ocr-read-inventory.csv", 3, 70196),
    ]
    allrows: list[dict[str, str]] = []
    for before_name, read_name, n, total in specs:
        before, read = rows(S / before_name), rows(S / read_name)
        require(len(before) == len(read) == n, f"count: {read_name}")
        require([int(r["seq"]) for r in before] == list(range(1, n + 1)), f"pre-read sequence: {before_name}")
        require([int(r["seq"]) for r in read] == list(range(1, n + 1)), f"read sequence: {read_name}")
        require(sum(int(r["size_bytes"]) for r in read) == total, f"total bytes: {read_name}")
        for b, r in zip(before, read):
            require(b["path_from_ingest_root"] == r["path_from_ingest_root"], f"scope path differs: {read_name}")
            require(b["size_bytes"] == r["size_bytes"], f"scope size differs: {read_name}")
            rel = Path(r["path_from_ingest_root"])
            p = I / rel
            require(not rel.is_absolute() and ".." not in rel.parts, f"unsafe path: {rel}")
            require(p.is_file() and not p.is_symlink() and p.resolve().is_relative_to(I.resolve()), f"not a local regular file: {rel}")
            validate(p.read_bytes(), int(r["size_bytes"]), r["sha256"], str(rel))
        allrows.extend(read)
    paths = {r["path_from_ingest_root"] for r in allrows}
    require(len(paths) == len(allrows) == 4903, "duplicate representation paths")
    require(sum(int(r["size_bytes"]) for r in allrows) == 41644421, "overall byte total")
    old97 = {r["representation_path"] for r in rows(I / "15-source-evidence-r97-2026-10-26/local-first-second-inventory.csv")}
    old98 = {r["artifact_path"] for r in rows(I / "18-source-evidence-r98-2026-10-26/local-order-dc-inventory.csv")}
    old99 = {r["path_from_ingest_root"] for r in rows(I / "22-source-evidence-r99-2026-10-26/scope-inventory.csv")}
    partial99 = {r["path_from_ingest_root"] for r in rows(I / "22-source-evidence-r99-2026-10-26/context-partial-inventory.csv")}
    require((len(paths & old97), len(paths & old98), len(paths & old99), len(paths & partial99)) == (1, 9, 5, 5), "previous-round path overlap")
    return allrows, "4,903 unique local paths / 41,644,421 bytes; old path overlaps 1/9/5 plus 5 partial"


def firmware() -> str:
    filelist = rows(F / "rootfs-FILELIST.tsv", "\t")
    binary = rows(F / "rootfs-binary-index.tsv", "\t")
    require(len(filelist) == 9655, "historical filelist rows")
    require(Counter(r["type"] for r in filelist) == {"file": 6999, "dir": 627, "symlink": 2029}, "historical filelist types")
    orig = {r["path"]: r for r in filelist if r["type"] == "file"}
    historical_bins = {r["path"]: r for r in binary}
    texts = {p.relative_to(T).as_posix(): p for p in T.rglob("*") if p.is_file() and not p.is_symlink()}
    require(len(orig) == 6999 and len(binary) == len(historical_bins) == 2118 and len(texts) == 4881, "file partition counts")
    require(set(orig) == set(texts) | set(historical_bins) and not (set(texts) & set(historical_bins)), "file partition names")
    require(all(int(orig[k]["bytes"]) == p.stat().st_size for k, p in texts.items()), "text vs historical size")
    require(all(int(orig[k]["bytes"]) == int(r["bytes"]) and re.fullmatch(r"[0-9a-f]{64}", r["sha256"]) for k, r in historical_bins.items()), "binary historic index")
    require(sum(int(r["bytes"]) for r in binary) == 118280374, "binary indexed byte total")
    c: Counter[str] = Counter()
    needles = (b"anw-2116-pg", b"sti-21616dggpm", b"lt-is6318gp-2gx16gt")
    for p in texts.values():
        b = p.read_bytes()
        c["empty"] += not b
        c["nul"] += b"\0" in b
        try:
            b.decode("utf-8")
        except UnicodeDecodeError:
            c["not_utf8"] += 1
        for needle in needles:
            c[needle.decode()] += needle in b.lower()
    require((c["empty"], c["not_utf8"], c["nul"]) == (95, 392, 2), "text-encoding observations")
    require(all(c[n.decode()] == 0 for n in needles), "model literal appeared in text tree")
    meta = json.loads((I / "03-binary-meta/3rd order 176台2光16电 L2 PoE/lite-hotfix-7.3.13.bin.meta.json").read_text(encoding="utf-8"))
    require(meta["bytes"] == 62289840 and meta["sha256"] == "7fe48e24a87cdd731f9f238f3607ae9b1d41cb46b20ba8b64fa6feb52e5a70d4", "historical package metadata")
    require("hotfix/7.3.13 (r1431 25e364a)" in (T / "version.txt").read_text(encoding="utf-8"), "system version marker")
    require("dkweb: 7.3.9" in (T / "www/version.txt").read_text(encoding="utf-8"), "web component marker")
    cfg = (F / "upgrade.cfg").read_text(encoding="utf-8")
    require('version = "";' in cfg and 'title  = "MAC3L"' in cfg and 'title  = "LTIE"' in cfg, "upgrade config tokens")
    c16 = (T / "etc/capcfg/sai/product/sw_ltie_mac3l_16gt2gs_6xp.cfg").read_bytes().decode("latin-1")
    require('port_num = 18;' in c16, "16+2 port_num")
    require(len(re.findall(r'(?m)^\s*intf_style\s*=\s*"1000_T";', c16)) == 16, "16 copper-style config entries")
    require(len(re.findall(r'(?m)^\s*intf_style\s*=\s*"1000_X";', c16)) == 2, "2 optical-style config entries")
    require(len(re.findall(r'(?m)^\s*poe_support\s*=\s*true;', c16)) == 16, "16 PoE config entries")
    c8 = (T / "etc/capcfg/sai/product/sw_ltie_mac5_8gt2gs_6xrp.cfg").read_text(encoding="utf-8")
    require('name = "SWITCH_LTID_MAC3L_8GT4GS_6X";' in c8 and 'port_num = 10;' in c8, "path/name example")
    require(len(re.findall(r"(?m)^\s*ifindex\s*=", c8)) == 10, "10 configured interfaces")
    return "historical TSV partition 4,881+2,118=6,999; selected config/versions and exact model scan (no original binary verification)"


def source_tokens() -> str:
    ext = I / "02-extracted"
    reply = (ext / "Reply on SAGA Enterprise L3 Recommendation Report.docx.extracted.md").read_text(encoding="utf-8")
    require("lite-hotfix-7.3.13 is the last version which I shared and believed that you have integrated it to your NMS system" in reply, "reply qualification")
    feature = (ext / "Saga Feature List_7.5.x_L2+.xlsx.extracted.md").read_text(encoding="utf-8")
    for text in ("Marvell 98DX2515/2518 (AC5 Lite)", "Static Route", "PIM-SM"):
        require(text in feature, f"feature list token: {text}")
    second = (ext / "2nd order sample 2层10G 16口 2光8管理/CI.xls.extracted.md").read_text(encoding="utf-8")
    third = (ext / "3rd order 176台2光16电 L2 PoE/STSC20250117007.xls.extracted.md").read_text(encoding="utf-8")
    purchase = (ext / "3rd order 176台2光16电 L2 PoE/采购_Smartbyte/采购合同_STSC20250117007.xls.extracted.md").read_text(encoding="utf-8")
    for text in ("STC-416DGGPM", "ANW-2116-PG", "4*1G/2.5G SFP+16*10/100/1000M"):
        require(text in second, f"second CI token: {text}")
    for text in ("STI-21616DGGPM", "ANW-2116-PG", "2*100M/1G/2.5G Fiber+16*10/100M/1000M"):
        require(text in third, f"third PI token: {text}")
    require("LT-IS6318GP-2GX16GT" in purchase and "ANW-2116-PG" in purchase, "supplier mapping")
    sixth = (ext / "6th order 6台工业2光8/STSC20250619007_R1.xls.extracted.md").read_text(encoding="utf-8")
    require("TT-2208-PG" in sixth and "Marvell AC5 Chip" in sixth, "sixth PI model")
    mac = (ext / "mac_address&serial_number.xlsx.extracted.md").read_text(encoding="utf-8")
    entries = [line.split("\t") for line in mac.splitlines() if "STSC20250619007" in line]
    require(len(entries) == 6 and all(len(x) == 4 and "TT-2208-PG" in x[3] for x in entries), "sixth order six ledger rows")
    require(len({x[0] for x in entries}) == len({x[1] for x in entries}) == 6, "sixth order unique MAC/SN in ledger")
    require("MAC: 98:06:37:A5:00:13~98:06:37:A5:00:18 Serial Info: 25052208C0103~25052208C0603" in sixth, "sixth PI range")
    for index, x in enumerate(entries, 1):
        require(x[0] == f"98:06:37:A5:00:{0x12 + index:02X}" and x[1] == f"25052208C{index:02d}03", "sixth PI and ledger row mismatch")
    warranty = (ext / "3rd order 176台2光16电 L2 PoE/Shipment Info/Certificate of Warranty.psd.extracted.md").read_text(encoding="utf-8")
    for text in ("2501211600103~2501211617603", "2501211617703~2501211617803", "Total Quantity: 178 pieces only"):
        require(text in warranty, f"third order PSD serial-range token: {text}")
    require(176 + 2 == 178, "third order primary/RMA range arithmetic")
    cross = rows(S / "model-record-crossrefs.csv")
    require(len(cross) == 13, "model cross-reference count")
    require(len({(x["source_artifact_path_from_ingest_root"], x["source_locator"]) for x in cross}) == 13, "model cross-reference duplicate source row")
    selected = {x["path_from_ingest_root"] for x in rows(S / "selected-read-inventory.csv")}
    for x in cross:
        rel = x["source_artifact_path_from_ingest_root"]
        require(rel in selected, "model cross-reference source outside selected inventory")
        m = re.fullmatch(r"line ([1-9][0-9]*)", x["source_locator"])
        require(bool(m), "model cross-reference locator")
        source_lines = (I / rel).read_text(encoding="utf-8").splitlines()
        n = int(m.group(1)) - 1
        require(n < len(source_lines), "model cross-reference line out of range")
        context = "\n".join(source_lines[max(0, n - 2):n + 3])
        for field in ("buyer_model", "seller_model"):
            if x[field]:
                require(x[field] in context, f"model cross-reference {field} absent from source context")
        if x["mac_if_individually_listed"]:
            prefix = "\t".join((x["mac_if_individually_listed"], x["sn_if_individually_listed"], x["order_identifier"]))
            require(source_lines[n].startswith(prefix + "\t"), "individual MAC/SN cross-reference differs")
    require(sum(bool(x["mac_if_individually_listed"]) for x in cross) == 6, "individual MAC/SN cross-reference count")
    chat = json.loads((W / "01-knowledge-base/wechat-conversation-aligned.json").read_text(encoding="utf-8"))
    match = [r for r in chat if r.get("datetime") == "2026-07-08 13:34" and "lite-hotfix-7.3.13.bin" in r.get("text", "")]
    require(len(match) == 1 and match[0].get("speaker") == "Simon" and "59.4M" in match[0]["text"], "aligned OCR card")
    require("**[13:34] Taylan：**" in (W / "01-knowledge-base/wechat-2026.md").read_text(encoding="utf-8"), "alternative OCR speaker")
    ocr = [json.loads(x) for x in (W / "99-raw/wechat-ocr-aligned/Weixin Image_2026-09-23_225232_904.jsonl").read_text(encoding="utf-8").splitlines()]
    words = {x["text"] for x in ocr}
    for text in ("7/8Wednesday13:34", "lite-hotfix-7.3.13.bin", "59.4M", "pls transfer this to Taylan"):
        require(text in words, f"OCR token: {text}")
    require(round(62289840 / 1024 / 1024, 1) == 59.4, "conditional MiB conversion")
    return "reply qualifications, model documents and two differing OCR speaker labels found; size conversion conditional"


def git_blobs(items: list[dict[str, str]]) -> str:
    """Compare the working bytes with *current Git index* blobs, not source image."""
    paths = [(I / r["path_from_ingest_root"]).relative_to(ROOT).as_posix() for r in items]
    fw_prefix = T.relative_to(ROOT).as_posix() + "/"
    other = [p for p in paths if not p.startswith(fw_prefix)]
    result = subprocess.run(["git", "ls-files", "-s", "-z", "--", fw_prefix, *other], cwd=ROOT, stdout=subprocess.PIPE, check=True)
    tracked: dict[str, str] = {}
    for entry in result.stdout.split(b"\0"):
        if not entry:
            continue
        meta, rawpath = entry.split(b"\t", 1)
        mode, oid, stage = meta.split()
        require(stage == b"0" and mode in (b"100644", b"100755"), "non-regular or unmerged Git index entry")
        tracked[rawpath.decode("utf-8")] = oid.decode("ascii")
    require(set(paths) == set(tracked), "missing/extra Git index paths")
    query = "".join(tracked[p] + "\n" for p in paths).encode("ascii")
    output = subprocess.run(["git", "cat-file", "--batch"], cwd=ROOT, input=query, stdout=subprocess.PIPE, check=True).stdout
    pos = 0
    for row, p in zip(items, paths):
        nl = output.find(b"\n", pos)
        require(nl >= 0, "Git batch header")
        hdr = output[pos:nl].split()
        require(len(hdr) == 3 and hdr[1] == b"blob", f"Git object type: {p}")
        size = int(hdr[2])
        pos = nl + 1
        blob = output[pos:pos + size]
        pos += size
        require(output[pos:pos + 1] == b"\n", "Git batch terminator")
        pos += 1
        validate(blob, int(row["size_bytes"]), row["sha256"], f"Git index blob: {p}")
    require(pos == len(output), "extra Git batch data")
    return "4,903/4,903 Git index blobs match current local derivative bytes; not the absent original"


def links() -> str:
    docs = [R, M, S / "README.md", FOLLOW / "README.md", FOLLOW / "angora-networks.md", A]
    require({p.name for p in FOLLOW.glob("*.md")} == {"README.md", "angora-networks.md"}, "one-customer follow-up")
    pattern = re.compile(r'(?<!!)\[[^\]\n]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
    broken, count = [], 0
    for doc in docs:
        for ref in pattern.findall(doc.read_text(encoding="utf-8")):
            parsed = urlsplit(ref)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            count += 1
            if not (doc.parent / unquote(parsed.path)).exists():
                broken.append(f"{doc.relative_to(ROOT)} -> {ref}")
    require(not broken, "broken local links:\n" + "\n".join(broken))
    return f"{count} local links exist across r100 deliverables"


def negative_test() -> str:
    original = b"local-hash-fixture"
    digest = sha256(original).hexdigest()
    validate(original, len(original), digest, "fixture")
    for data, size, h in ((b"X" + original[1:], len(original), digest), (original, len(original) + 1, digest), (original, len(original), "0" * 64)):
        try:
            validate(data, size, h, "negative fixture")
        except ValueError:
            continue
        raise ValueError("negative hash/size test unexpectedly passed")
    return "three in-memory mutations rejected without altering evidence"


def main() -> int:
    try:
        items, desc = inventory()
        print("PASS Inventory:", desc)
        for label, fn in (("Firmware", firmware), ("Sources", source_tokens), ("Git", lambda: git_blobs(items)), ("Links", links), ("Negative", negative_test)):
            print(f"PASS {label}: {fn()}")
        print("Boundary: local bytes and selected tokens only; no proof of original authenticity, OCR correctness, sharing, installation, compatibility, signature or current status.")
        return 0
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
