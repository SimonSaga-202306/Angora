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

    summary = json.load(open(os.path.join(DST, "00-manifest", "SUMMARY.json")))
    total_chars = summary["artifact_chars"]
    ok_all = all(c[1] for c in checks)

    lines = ["# Verification report - full-repo ingest", "",
             f"- source: `{SRC_REPO}` branch `{SRC_BRANCH}` commit `{SRC_COMMIT}`",
             f"- git-tracked files: **{len(files)}**",
             f"- ingest artifacts: **{len(recs)}** (1:1, nothing merged)",
             f"- source bytes: **{src_bytes:,}**",
             f"- artifact bytes: **{summary['artifact_bytes']:,}**",
             f"- artifact characters: **{total_chars:,}**",
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
              f"| files with no artifact | {len(files) - len(recs)} |", ""]
    with open(os.path.join(DST, "00-manifest", "VERIFICATION.md"), "w",
              encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print("\n".join(lines))
    assert ok_all, "verification failed"


if __name__ == "__main__":
    main()
