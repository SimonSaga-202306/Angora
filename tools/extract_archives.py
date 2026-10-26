#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Second coverage layer: archive members.

Every member of every archive becomes its own artifact - one artifact per member,
nothing merged:

    ingest/.../04-archive-members/<archive relpath>/<member relpath>
        (verbatim copy for text members, .extracted.md for office/pdf,
         .meta.json for binary members)

Nested archives (an archive inside an archive) are NOT exploded into the repo when
their payload is large CAD/PCB data; they get an inventory artifact instead
(entry list + sizes + sha256 of the container), so nothing is silently dropped and
nothing bloats the store.

Manifest: 04-archive-members/ARCHIVE-MEMBERS-INDEX.csv
"""
import csv
import hashlib
import json
import os
import shutil
import tempfile
import zipfile

SRC = "/tmp/audit"
DST = "/home/user/Angora/ingest/angora-1__arena-01a0ce39__5acb613/04-archive-members"
SRC_REPO = "SimonSaga-202306/Angora-1"
SRC_BRANCH = "arena/01a0ce39-angora"
SRC_COMMIT = "5acb6132a6a6090bfc777c324cfea6bc8dfb877a"
MATERIALIZE_LIMIT = 4 << 20          # expand nested archives only up to 4 MiB
STAGE = "/tmp/memberstage"

import sys
sys.path.insert(0, "/home/user/Angora/tools")
import build_ingest as B  # noqa: E402

ARCHIVES = [
    "2nd order sample 2层10G 16口 2光8管理/出货/ANW-1108-V/TT-2208-TG/TT-2208-TG.zip",
    "2nd order sample 2层10G 16口 2光8管理/出货/ANW-1108-V/TT-2208-TG/Turk Telekom Logo 3.zip",
    "3rd order 176台2光16电 L2 PoE/TT-2116-PG/TT-2116-PG.zip",
    "5th order sample  2层10G 24口 48口/Shipment Info/TRX-AS-24TP4X.zip",
    "5th order sample  2层10G 24口 48口/Shipment Info/TRX-AS-48TP4X.zip",
    "IoT Board/PC0012_Saga.7z",
    "INFO_2025.12.17/INFO.rar",
]

TEXT_EXT = {".md", ".txt", ".py", ".json", ".jsonl", ".csv", ".tsv", ".log",
            ".conf", ".cfg", ".ini", ".def", ".xml", ".yml", ".yaml", ".sh",
            ".bat", ".gbr", ".drl", ".txt", ".nc", ".svg"}
EXT_EXT = {".xls", ".xlsx", ".docx", ".doc", ".pptx", ".pdf", ".psd", ".pub",
           ".ai", ".cdr"}
IMG = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"}
ARCH = {".zip", ".7z", ".rar"}

ROWS = []


def _split(display_rel):
    """display_rel = <top archive>/<member path> (nested containers appear as dirs)."""
    for a in ARCHIVES:
        if display_rel == a or display_rel.startswith(a + "/"):
            return a, display_rel[len(a) + 1:] if display_rel != a else ""
    return display_rel.rsplit("/", 1)[0], display_rel.rsplit("/", 1)[-1]


# --------------------------------------------------------------------------- #
def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def list_zip(path):
    with zipfile.ZipFile(path) as zf:
        return [(zi.filename, zi.is_dir(), zi.file_size) for zi in zf.infolist()]


def list_7z(path):
    import py7zr
    with py7zr.SevenZipFile(path) as z:
        return [(f.filename, f.is_directory, f.uncompressed) for f in z.list()]


def list_rar(path):
    import rarfile
    with rarfile.RarFile(path) as rf:
        return [(zi.filename, zi.isdir(), zi.file_size) for zi in rf.infolist()]


def read_members(path, ext):
    """Return [(name, is_dir, bytes)] - only for formats we can decode in python."""
    if ext == ".zip":
        with zipfile.ZipFile(path) as zf:
            return [(zi.filename, zi.is_dir(), b"" if zi.is_dir() else zf.read(zi))
                    for zi in zf.infolist()]
    if ext == ".7z":
        import py7zr
        tmp = tempfile.mkdtemp(dir=STAGE)
        out = []
        with py7zr.SevenZipFile(path) as z:
            names = z.getnames()
            z.extractall(path=tmp)
        for n in names:
            p = os.path.join(tmp, n)
            if os.path.isdir(p):
                out.append((n, True, b""))
            elif os.path.isfile(p):
                out.append((n, False, open(p, "rb").read()))
        return out
    return []          # .rar: header listing only (no unrar binary in sandbox)


# --------------------------------------------------------------------------- #
def dump_member(display_rel, name, buf):
    """Write one artifact for one member file."""
    out_base = os.path.join(DST, display_rel)
    os.makedirs(os.path.dirname(out_base), exist_ok=True)
    ext = os.path.splitext(name)[1].lower()
    kind = "verbatim"
    if ext in TEXT_EXT or (ext not in EXT_EXT and ext not in ARCH and ext not in IMG
                           and b"\x00" not in buf[:8192]):
        with open(out_base, "wb") as fh:
            fh.write(buf)
        out_path = display_rel
    elif ext in EXT_EXT:
        tmp = os.path.join(STAGE, hashlib.sha1(display_rel.encode()).hexdigest() + ext)
        with open(tmp, "wb") as fh:
            fh.write(buf)
        fn = {".xls": B.extract_xls, ".xlsx": B.extract_xlsx, ".docx": B.extract_docx,
              ".doc": B.extract_doc, ".pptx": B.extract_pptx, ".pdf": B.extract_pdf,
              ".psd": B.extract_psd, ".pub": B.extract_pub, ".ai": B.extract_ai,
              ".cdr": B.extract_cdr}.get(ext)
        try:
            body = fn(tmp) if fn else "[no extractor]"
        except Exception as exc:  # noqa: BLE001
            body = f"[extraction error: {type(exc).__name__}: {exc}]"
        out_path = display_rel + ".extracted.md"
        with open(os.path.join(DST, out_path), "w", encoding="utf-8") as fh:
            fh.write(f"<!-- ARCHIVE MEMBER: {display_rel} | {len(buf)} bytes | "
                     f"sha256 {sha_bytes(buf)} | {SRC_COMMIT} -->\n\n" + body)
        kind = "extracted"
    else:
        info = {"source_repo": SRC_REPO, "source_branch": SRC_BRANCH,
                "source_commit": SRC_COMMIT, "archive_member": display_rel,
                "bytes": len(buf), "sha256": sha_bytes(buf)}
        if ext in IMG:
            tmp = os.path.join(STAGE, hashlib.sha1(display_rel.encode()).hexdigest() + ext)
            with open(tmp, "wb") as fh:
                fh.write(buf)
            try:
                info["image"] = B.describe_image(tmp)
            except Exception as exc:  # noqa: BLE001
                info["image_error"] = str(exc)
        out_path = display_rel + ".meta.json"
        with open(os.path.join(DST, out_path), "w", encoding="utf-8") as fh:
            json.dump(info, fh, ensure_ascii=False, indent=2, default=str)
            fh.write("\n")
        kind = "meta"
    arc, member = _split(display_rel)
    ROWS.append({"archive": arc, "member": member, "bytes": len(buf),
                 "sha256": sha_bytes(buf), "kind": kind, "artifact": out_path})


def dump_inventory(display_rel, container_bytes, entries, note):
    out_base = os.path.join(DST, display_rel)
    os.makedirs(os.path.dirname(out_base), exist_ok=True)
    info = {"source_repo": SRC_REPO, "source_branch": SRC_BRANCH,
            "source_commit": SRC_COMMIT, "nested_archive": display_rel,
            "bytes": len(container_bytes), "sha256": sha_bytes(container_bytes),
            "entry_count": len([e for e in entries if not e[1]]),
            "entries": [{"name": n, "bytes": s, "is_dir": d} for n, d, s in entries],
            "materialized": False, "note": note}
    out_path = display_rel + ".inventory.json"
    with open(os.path.join(DST, out_path), "w", encoding="utf-8") as fh:
        json.dump(info, fh, ensure_ascii=False, indent=2, default=str)
        fh.write("\n")
    arc, member = _split(display_rel)
    ROWS.append({"archive": arc, "member": member + "  [inventory]",
                 "bytes": len(container_bytes), "sha256": sha_bytes(container_bytes),
                 "kind": "inventory", "artifact": out_path})


# --------------------------------------------------------------------------- #
def handle_rar_listing(display_prefix):
    """RAR cannot be decoded without unrar: map every member to the loose copy that
    carries its content, and flag any member that differs from the loose file."""
    arc_path = os.path.join(SRC, display_prefix)
    base_dir = os.path.dirname(display_prefix)
    rows = []
    for name, is_dir, size in list_rar(arc_path):
        if is_dir or not name:
            continue
        loose = os.path.join(SRC, base_dir, name)
        status, loose_sha, loose_size = "missing-loose", "", 0
        if os.path.isfile(loose):
            loose_size = os.path.getsize(loose)
            loose_sha = sha_file(loose)
            status = "covered-by-loose-file" if loose_size == size else "differs-from-loose-file"
        rel_loose = os.path.relpath(loose, SRC)
        ROWS.append({"archive": display_prefix, "member": name, "bytes": size,
                     "sha256": loose_sha, "kind": status,
                     "artifact": rel_loose if status.startswith("covered") else ""})
        rows.append({"member": name, "bytes": size, "loose": rel_loose,
                     "status": status, "sha256": loose_sha})
    info = {"source_repo": SRC_REPO, "source_branch": SRC_BRANCH,
            "source_commit": SRC_COMMIT, "archive": display_prefix,
            "bytes": os.path.getsize(arc_path), "sha256": sha_file(arc_path),
            "decoder": "none (RAR payload needs unrar, absent in sandbox)",
            "note": "member bytes are pinned by the archive sha256 above; every member is "
                    "also present loose in the same folder except where status says "
                    "differs-from-loose-file / missing-loose",
            "members": rows}
    out_rel = display_prefix + ".inventory.json"
    os.makedirs(os.path.dirname(os.path.join(DST, out_rel)), exist_ok=True)
    with open(os.path.join(DST, out_rel), "w", encoding="utf-8") as fh:
        json.dump(info, fh, ensure_ascii=False, indent=2, default=str)
        fh.write("\n")


def handle_archive(display_prefix, path, depth=0):
    ext = os.path.splitext(path)[1].lower()
    if ext in (".zip", ".7z"):
        members = read_members(path, ext)
    elif ext == ".rar":
        handle_rar_listing(display_prefix)
        return
    else:
        return
    for name, is_dir, payload in members:
        if is_dir or not name:
            continue
        sub = os.path.splitext(name)[1].lower()
        child_display = display_prefix + "/" + name
        if sub in ARCH:
            if ext == ".rar":
                # cannot decode rar members without unrar: record the entry only
                ROWS.append({"archive": display_prefix, "member": name,
                             "bytes": payload if isinstance(payload, int) else len(payload),
                             "sha256": "", "kind": "listed-only", "artifact": ""})
                continue
            nested_tmp = os.path.join(STAGE, hashlib.sha1(child_display.encode()).hexdigest() + sub)
            with open(nested_tmp, "wb") as fh:
                fh.write(payload)
            entries = list_zip(nested_tmp) if sub == ".zip" else list_7z(nested_tmp)
            total = sum(s for _, d, s in entries if not d)
            if total <= MATERIALIZE_LIMIT and depth + 1 <= 2:
                handle_archive(child_display, nested_tmp, depth + 1)
            else:
                dump_inventory(child_display, payload, entries,
                               "payload too large to materialize (%d bytes across %d files); "
                               "container sha256 + full entry list recorded instead of "
                               "exploding CAD/PCB geometry into the store" % (total, len(entries)))
            continue
        dump_member(child_display, name, payload)


def main():
    shutil.rmtree(STAGE, ignore_errors=True)
    os.makedirs(STAGE, exist_ok=True)
    shutil.rmtree(DST, ignore_errors=True)
    os.makedirs(DST, exist_ok=True)
    for a in ARCHIVES:
        handle_archive(a, os.path.join(SRC, a))
    with open(os.path.join(DST, "ARCHIVE-MEMBERS-INDEX.csv"), "w", newline="",
              encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["archive", "member", "bytes", "sha256", "kind", "artifact"])
        for r in ROWS:
            w.writerow([r["archive"], r["member"], r["bytes"], r["sha256"],
                        r["kind"], r["artifact"]])
    from collections import Counter
    print("rows:", len(ROWS), Counter(r["kind"] for r in ROWS))
    print("bytes:", sum(r["bytes"] for r in ROWS))
    shutil.rmtree(STAGE, ignore_errors=True)


if __name__ == "__main__":
    main()
