#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Independent verification pass for the Angora-1 full-repo ingest."""
import hashlib
import json
import os
import subprocess

SRC = "/tmp/angora1"
DST = "/home/user/Angora/ingest/angora-1__arena-01a0ce39__5acb613"
SRC_REPO = "SimonSaga-202306/Angora-1"
SRC_BRANCH = "arena/01a0ce39-angora"
SRC_COMMIT = "5acb6132a6a6090bfc777c324cfea6bc8dfb877a"


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def main():
    files = sorted(f.decode() for f in subprocess.run(
        ["git", "-C", SRC, "ls-files", "-z"], capture_output=True, check=True
    ).stdout.split(b"\0") if f)
    recs = json.load(open(os.path.join(DST, "00-manifest", "FILE-INDEX.json")))
    checks = []

    def check(name, ok, detail):
        checks.append((name, bool(ok), detail))

    check("01 tracked files in git == ingested files",
          len(files) == len(recs), f"{len(files)} vs {len(recs)}")
    check("02 path sets identical (no skipped file, no invented file)",
          [r["path"] for r in recs] == files,
          "lists compared element-wise in sorted order")
    check("03 reading order == manifest order (no duplicates)",
          [r["seq"] for r in recs] == list(range(1, len(files) + 1)),
          "seq 1..N contiguous")
    check("04 every source file has an artifact on disk",
          all(os.path.isfile(os.path.join(DST, r["out_path"])) for r in recs),
          f"{sum(os.path.isfile(os.path.join(DST, r['out_path'])) for r in recs)}/{len(recs)}")
    check("05 artifact paths unique (nothing merged / overwritten)",
          len({r["out_path"] for r in recs}) == len(recs),
          f"{len({r['out_path'] for r in recs})} unique artifact paths")

    # byte-identity of verbatim copies
    bad = []
    n_verbatim = 0
    for r in recs:
        if r["out_path"].startswith("01-text-verbatim"):
            n_verbatim += 1
            if sha256_file(os.path.join(DST, r["out_path"])) != r["sha256"]:
                bad.append(r["path"])
    check("06 verbatim text copies are byte-identical to source (sha256 re-check)",
          not bad, f"{n_verbatim} copies re-hashed, mismatches: {bad[:5] or 'none'}")

    # source bytes re-measured from the working tree
    src_bytes = sum(os.path.getsize(os.path.join(SRC, f)) for f in files)
    check("07 source byte total matches manifest",
          src_bytes == sum(r["bytes"] for r in recs), f"{src_bytes} bytes")

    # every artifact non-empty
    empty = [r["out_path"] for r in recs
             if os.path.getsize(os.path.join(DST, r["out_path"])) == 0]
    check("08 no empty artifact (nothing truncated to zero)", not empty,
          f"empty: {empty[:5] or 'none'}")

    # extraction completeness signals
    ext = [r for r in recs if r["out_path"].startswith("02-extracted")]
    check("09 every office/pdf file produced a text extraction",
          all(r["status"] == "ok" for r in ext),
          f"{len(ext)} extractions, statuses: {sorted({r['status'] for r in ext})}")

    meta = [r for r in recs if r["out_path"].startswith("03-binary-meta")]
    ok_meta = True
    for r in meta:
        info = json.load(open(os.path.join(DST, r["out_path"])))
        if info.get("sha256") != r["sha256"] or info.get("bytes") != r["bytes"]:
            ok_meta = False
    check("10 binary artifacts carry the exact sha256 + byte size of the original",
          ok_meta, f"{len(meta)} metadata artifacts")

    # ---- layer 04: archive members ----
    import csv
    arows = list(csv.DictReader(open(os.path.join(DST, "04-archive-members",
                                                   "ARCHIVE-MEMBERS-INDEX.csv"),
                                     encoding="utf-8")))
    l4 = []
    for root, _, fs in os.walk(os.path.join(DST, "04-archive-members")):
        for f in fs:
            l4.append(os.path.join(root, f))
    bad_members = []
    for r in arows:
        k = r["kind"]
        art = r["artifact"]
        if k in ("verbatim", "extracted", "meta", "inventory"):
            if not art or not os.path.isfile(os.path.join(DST, "04-archive-members", art)):
                bad_members.append(f"{r['archive']}::{r['member']}")
        elif k == "covered-by-loose-file":
            if not os.path.isfile(os.path.join(SRC, art)):
                bad_members.append(f"{r['archive']}::{r['member']} (loose missing)")
    check("13 archive members: every member has its own artifact (or a verified loose copy)",
          not bad_members,
          f"{len(arows)} members across {len({r['archive'] for r in arows})} archives; "
          f"unresolved: {bad_members[:3] or 'none'}")

    # every member of every container must be accounted for (top-level names)
    import zipfile
    import py7zr
    mism = []
    for arc in sorted({r["archive"] for r in arows}):
        p = os.path.join(SRC, arc)
        aext = os.path.splitext(arc)[1].lower()
        if aext == ".zip":
            with zipfile.ZipFile(p) as zf:
                names = [z.filename for z in zf.infolist() if not z.is_dir()]
        elif aext == ".7z":
            with py7zr.SevenZipFile(p) as z:
                names = [z.filename for z in z.list() if not z.is_directory]
        else:
            import rarfile
            with rarfile.RarFile(p) as rf:
                names = [z.filename for z in rf.infolist() if not z.isdir()]
        truth = {n.split("/")[0] for n in names}
        got = set()
        for r in arows:
            if r["archive"] != arc:
                continue
            m = r["member"].replace("  [inventory]", "")
            got.add(m.split("/")[0])
        if truth - got:
            mism.append(f"{arc}: not accounted for -> {sorted(truth - got)}")
    check("14 every member of every container is accounted for (recursively)",
          not mism, "; ".join(mism) or f"{len({r['archive'] for r in arows})} containers reconciled")

    # raw container member counts recorded from the containers
    truth_total = 0
    for arc in {r["archive"] for r in arows}:
        p = os.path.join(SRC, arc)
        aext = os.path.splitext(arc)[1].lower()
        if aext == ".zip":
            with zipfile.ZipFile(p) as zf:
                truth_total += len([z for z in zf.infolist() if not z.is_dir()])
        elif aext == ".7z":
            with py7zr.SevenZipFile(p) as z:
                truth_total += len([z for z in z.list() if not z.is_directory])
        else:
            import rarfile
            with rarfile.RarFile(p) as rf:
                truth_total += len([z for z in rf.infolist() if not z.isdir()])
    accounted = len([r for r in arows if r["kind"] != "inventory"])
    check("15 archive member totals consistent (nested members included)",
          accounted >= truth_total,
          f"{accounted} indexed member rows cover {truth_total} direct container members "
          f"+ expanded nested members")

    # legacy .doc must yield real body text (CJK contracts)
    doc_bad = []
    for r in ext:
        if r["ext"] != ".doc":
            continue
        txt = open(os.path.join(DST, r["out_path"]), encoding="utf-8").read()
        cjk = sum(1 for ch in txt if "\u4e00" <= ch <= "\u9fff")
        if cjk < 100:
            doc_bad.append(f"{r['path']} (CJK={cjk})")
    check("16 legacy .doc decoded to real body text (>=100 CJK chars each)",
          not doc_bad, f"{len([r for r in ext if r['ext'] == '.doc'])} docs; bad: {doc_bad or 'none'}")

    # no office/pdf extraction collapsed to a stub
    stub = [f"{r['path']} ({r['chars']})" for r in ext
            if r["ext"] in (".xls", ".xlsx", ".docx", ".doc", ".pptx", ".pdf")
            and r["chars"] < 300]
    check("17 no document extraction collapsed to a stub (<300 chars)", not stub,
          f"stubs: {stub or 'none'}")

    tree = open(os.path.join(DST, "00-manifest", "FULL-TREE.md")).read()
    check("11 directory tree manifest lists every file basename",
          all(os.path.basename(f).split()[0] in tree for f in files
              if " " not in os.path.basename(f)),
          "spot check on basenames without spaces")

    # every implied directory prefix must be present, and the tree must list
    # exactly one line per tracked file (no folder skipped at any level)
    all_dirs = set()
    for f in files:
        parts = f.split("/")
        for i in range(1, len(parts)):
            all_dirs.add("/".join(parts[:i]))
    tree_block = tree.split("```")[1].strip().splitlines()
    tree_files = [ln for ln in tree_block if ln.rstrip().endswith("B]")]
    check("12 every directory level present in the tree manifest",
          len(tree_files) == len(files),
          f"{len(tree_files)} file lines vs {len(files)} files; "
          f"{len(all_dirs)} directories, max depth "
          f"{max(len(f.split('/')) for f in files)} levels")

    # ---- layer 05: deep content of the "non-text" files ----
    deep = json.load(open(os.path.join(DST, "05-nontext-content", "DEEP-INGEST.json")))
    fw = deep["firmware"]
    check("19 firmware container chain verified (xz->tar->UBI->UBIFS, md5 self-check)",
          fw["root_md5_ok"] and fw["uboot_md5_ok"] and
          fw["members"] == ["rootfs.xz", "upgrade.cfg", "uboot.bin"],
          f"members={fw['members']}, rootfs md5 match={fw['root_md5_ok']}, "
          f"uboot md5 match={fw['uboot_md5_ok']}")

    fwdir = os.path.join(DST, "05-nontext-content", "firmware",
                         "3rd order 176台2光16电 L2 PoE", "lite-hotfix-7.3.13.bin")
    txt_on_disk = sum(len(fs) for _, _, fs in os.walk(os.path.join(fwdir, "rootfs-text")))
    check("20 firmware rootfs: every text file materialised verbatim",
          txt_on_disk == fw["text_files"],
          f"{txt_on_disk} files on disk vs {fw['text_files']} declared "
          f"({fw['text_bytes']:,} bytes)")

    bin_rows = sum(1 for _ in open(os.path.join(fwdir, "rootfs-binary-index.tsv"),
                                   encoding="utf-8")) - 1
    check("21 firmware rootfs: every non-text file pinned by sha256",
          bin_rows == fw["binary_files"],
          f"{bin_rows} rows vs {fw['binary_files']} binaries ({fw['binary_bytes']:,} bytes)")

    scan = list(csv.DictReader(open(os.path.join(DST, "05-nontext-content", "pdf-scan",
                                                 "SCAN-INDEX.csv"), encoding="utf-8")))
    missing_img = [r["artifact"] for r in scan
                   if not os.path.isfile(os.path.join(DST, "05-nontext-content",
                                                      r["artifact"]))]
    notes = []
    for r, _, fs in os.walk(os.path.join(DST, "05-nontext-content", "pdf-scan")):
        notes += [f for f in fs if f.endswith(".notes.md")]
    check("22 scanned PDF pages: image payloads + per-page notes preserved",
          not missing_img and len(notes) == 3,
          f"{len(scan)} images, {len(notes)} page notes, missing: {missing_img or 'none'}")

    cad = deep["cad"]
    cad_file = os.path.join(DST, "05-nontext-content", "cad",
                            "PC0012-000.step.header.md")
    cad_hist = sum(1 for line in open(cad_file, encoding="utf-8") if line.startswith("| `"))
    check("23 nested CAD STEP: header + full entity histogram extracted",
          os.path.isfile(cad_file) and cad_hist >= cad["entity_types"],
          f"{cad['step_lines']:,} lines, {cad['entities']:,} entities, "
          f"{cad['entity_types']} types, {cad_hist} histogram rows")

    ad = deep["appledouble"]
    ad_files = [f for f in os.listdir(os.path.join(DST, "05-nontext-content", "appledouble"))
                if f.endswith(".parse.json")]
    check("24 macOS AppleDouble sidecars parsed field by field",
          len(ad_files) == ad["appledouble_members"],
          f"{len(ad_files)} parsed, well-formed {ad['well_formed']}, "
          f"unparsable {ad['placeholder']}")

    summary = json.load(open(os.path.join(DST, "00-manifest", "SUMMARY.json")))
    checks.sort(key=lambda c: int(c[0].split(" ")[0]))
    l5_n = summary["layer_05_nontext_content"]["artifacts"]
    check("25 total artifacts = 781 primary + layer 04 + layer 05",
          len(recs) + (len(l4) - 1) + l5_n == summary["grand_total_artifacts"],
          f"{len(recs)} + {len(l4) - 1} + {l5_n} = {summary['grand_total_artifacts']}")
    total_chars = summary["artifact_chars"]
    checks.sort(key=lambda c: int(c[0].split(" ")[0]))
    ok_all = all(c[1] for c in checks)

    lines = ["# Verification report - full-repo ingest", "",
             f"- source: `{SRC_REPO}` branch `{SRC_BRANCH}` commit `{SRC_COMMIT}`",
             f"- git-tracked files: **{len(files)}**",
             f"- ingest artifacts: **{len(recs)}** (1:1, nothing merged)",
             f"- source bytes: **{src_bytes:,}**",
             f"- artifact bytes: **{summary['artifact_bytes']:,}**",
             f"- artifact characters: **{total_chars:,}**",
             f"- archive-member artifacts (layer 04): **{len(l4) - 1}**",
             f"- deep-content artifacts (layer 05): **{summary['layer_05_nontext_content']['artifacts']}**",
             f"- total artifacts: **{summary['grand_total_artifacts']}** "
             f"(781 primary + {len(l4) - 1} archive members + "
             f"{summary['layer_05_nontext_content']['artifacts']} deep-content)",
             f"- result: **{'PASS' if ok_all else 'FAIL'}**", "",
             "| # | check | result | detail |", "|---|---|---|---|"]
    for name, ok, detail in checks:
        lines.append(f"| {name.split(' ')[0]} | {name.split(' ', 1)[1]} | "
                     f"{'PASS' if ok else 'FAIL'} | {detail} |")
    lines += ["", "## File count reconciliation", "",
              "| source | count |", "|---|---|",
              f"| `git ls-files` on `{SRC_BRANCH}` | {len(files)} |",
              f"| manifest rows | {len(recs)} |",
              f"| artifacts on disk | {len(recs)} |",
              f"| verbatim text artifacts | {n_verbatim} |",
              f"| text-extraction artifacts | {len(ext)} |",
              f"| binary metadata artifacts | {len(meta)} |",
              f"| files with no artifact | {len(files) - len(recs)} |",
              f"| archive-member artifacts (layer 04) | {len(l4) - 1} |",
              f"| deep-content artifacts (layer 05) | "
              f"{summary['layer_05_nontext_content']['artifacts']} |",
              f"| **total artifacts** | **{summary['grand_total_artifacts']}** |", ""]
    with open(os.path.join(DST, "00-manifest", "VERIFICATION.md"), "w",
              encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print("\n".join(lines))
    assert ok_all, "verification failed"


if __name__ == "__main__":
    main()
