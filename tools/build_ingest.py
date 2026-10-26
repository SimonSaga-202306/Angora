#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Full-fidelity, file-by-file ingest of:

    repo   : SimonSaga-202306/Angora-1
    branch : arena/01a0ce39-angora
    commit : 5acb6132a6a6090bfc777c324cfea6bc8dfb877a
    files  : 781 (git ls-files, recursive, hidden files included)

Rules
-----
* ONE source file  ->  ONE ingest artifact. Nothing is merged, nothing is summarised.
* Text-native files are copied byte-for-byte (sha256 verified after copy).
* Office / PDF files are converted to full plain text (every sheet, row, cell,
  paragraph, table, slide, page - no row/character truncation).
* Binary media (images, video, PSD, archives, firmware, CAD) get a metadata
  artifact: sha256 of the original bytes + intrinsic properties. The bytes
  themselves are pinned by sha256 + the source commit, which makes the original
  byte-exactly recoverable; they are not re-encoded into the knowledge base.

Output layout
-------------
    ingest/angora-1__arena-01a0ce39__5acb613/
        00-manifest/  FULL-TREE.md  FILE-INDEX.csv  FILE-INDEX.json
                      INGEST-CATALOG.md  VERIFICATION.md  SUMMARY.json
        01-text-verbatim/<original relative path>
        02-extracted/<original relative path>.extracted.md
        03-binary-meta/<original relative path>.meta.json
"""

import csv
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile

SRC = "/tmp/angora1"
DST = "/home/user/Angora/ingest/angora-1__arena-01a0ce39__5acb613"
SRC_REPO = "SimonSaga-202306/Angora-1"
SRC_BRANCH = "arena/01a0ce39-angora"
SRC_COMMIT = "5acb6132a6a6090bfc777c324cfea6bc8dfb877a"

TEXT_EXT = {".md", ".txt", ".py", ".json", ".jsonl", ".csv", ".tsv", ".log",
            ".dxf", ".gitignore", ".gitattributes"}
OFFICE_EXT = {".xls", ".xlsx", ".docx", ".doc", ".pptx", ".pdf", ".pub", ".cdr", ".ai"}
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp", ".psd"}
MEDIA_EXT = {".mp4", ".mov", ".avi"}
ARCHIVE_EXT = {".zip", ".rar", ".7z", ".tar", ".gz"}
BIN_EXT = {".bin"}


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def sha256_file(path, chunk=1 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(chunk), b""):
            h.update(blk)
    return h.hexdigest()


def decode_text(data):
    """Decode bytes to str, returning (text, encoding). Never raises."""
    for enc in ("utf-8-sig", "utf-8", "gb18030", "cp1254", "latin-1"):
        try:
            return data.decode(enc), enc
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", "replace"), "utf-8/replace"


def numbers_to_text(v):
    if v is None:
        return ""
    if isinstance(v, float):
        if v == int(v) and abs(v) < 1e16:
            return str(int(v))
        return repr(v)
    if isinstance(v, bytes):
        return v.decode("utf-8", "replace")
    s = str(v)
    return s.replace("\r\n", " ").replace("\n", " ").replace("\t", " ")


def md_escape_cell(s):
    return s.replace("|", "\\|")


def ensure_parent(path):
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)


def header_block(seq, total, relpath, size, sha, method):
    return (
        "<!-- ============================================================ -->\n"
        f"<!-- FILE {seq}/{total} -->\n"
        f"<!-- PATH: {relpath} -->\n"
        f"<!-- SIZE: {size} bytes -->\n"
        f"<!-- SHA256: {sha} -->\n"
        f"<!-- EXTRACTION: {method} -->\n"
        "<!-- ============================================================ -->\n\n"
    )


# --------------------------------------------------------------------------- #
# extractors
# --------------------------------------------------------------------------- #
def extract_xls(path):
    import xlrd
    out = []
    wb = xlrd.open_workbook(path, formatting_info=False, on_demand=False)
    out.append(f"Workbook: sheets={wb.nsheets}\n")
    for sh in wb.sheets():
        out.append(f"\n## SHEET: {sh.name}  (rows={sh.nrows}, cols={sh.ncols})\n")
        out.append("```tsv\n")
        for r in range(sh.nrows):
            cells = []
            for c in range(sh.ncols):
                cell = sh.cell(r, c)
                if cell.ctype == xlrd.XL_CELL_DATE:
                    try:
                        val = str(xlrd.xldate.xldate_as_datetime(cell.value, wb.datemode))
                    except Exception:
                        val = numbers_to_text(cell.value)
                elif cell.ctype == xlrd.XL_CELL_EMPTY:
                    val = ""
                else:
                    val = numbers_to_text(cell.value)
                cells.append(val)
            line = "\t".join(cells).rstrip("\t")
            out.append(line + "\n")
        out.append("```\n")
    return "".join(out)


def extract_xlsx(path):
    import openpyxl
    out = []
    wb = openpyxl.load_workbook(path, read_only=True, data_only=False)
    out.append(f"Workbook: sheets={len(wb.sheetnames)}\n")
    for ws in wb.worksheets:
        out.append(f"\n## SHEET: {ws.title}  (dims={ws.calculate_dimension()}, "
                   f"max_row={ws.max_row}, max_column={ws.max_column})\n")
        out.append("```tsv\n")
        for row in ws.iter_rows(values_only=True):
            cells = [numbers_to_text(v) for v in row]
            while cells and cells[-1] == "":
                cells.pop()
            out.append("\t".join(cells) + "\n")
        out.append("```\n")
    wb.close()
    return "".join(out)


DOCX_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def iter_docx_body(doc):
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    body = doc.element.body
    for child in body.iterchildren():
        if child.tag == DOCX_NS + "p":
            yield Paragraph(child, doc)
        elif child.tag == DOCX_NS + "tbl":
            yield Table(child, doc)


def extract_docx(path):
    import docx
    doc = docx.Document(path)
    out = []
    p_i = 0
    t_i = 0
    for block in iter_docx_body(doc):
        if block.__class__.__name__ == "Paragraph":
            p_i += 1
            style = ""
            try:
                style = block.style.name or ""
            except Exception:
                pass
            out.append(f"[P{p_i}|{style}] {block.text}\n")
        else:  # Table
            t_i += 1
            out.append(f"\n[TABLE {t_i}] rows={len(block.rows)} cols={len(block.columns)}\n")
            for ri, row in enumerate(block.rows, 1):
                cells = [md_escape_cell(" ".join(c.text.split())) for c in row.cells]
                out.append(f"R{ri}\t" + "\t".join(cells) + "\n")
            out.append("\n")

    # headers / footers of every section
    for si, sec in enumerate(doc.sections, 1):
        for label, part in (("header", sec.header), ("footer", sec.footer),
                            ("first_page_header", sec.first_page_header),
                            ("first_page_footer", sec.first_page_footer),
                            ("even_page_header", sec.even_page_header),
                            ("even_page_footer", sec.even_page_footer)):
            try:
                txt = "\n".join(p.text for p in part.paragraphs)
                if txt.strip():
                    out.append(f"\n[SECTION {si} {label}]\n{txt}\n")
            except Exception:
                pass

    # text boxes (txbxContent) - only when present, keeps fidelity for callouts
    tbx = doc.element.body.findall(".//" + DOCX_NS + "txbxContent")
    if tbx:
        out.append(f"\n[TEXT BOXES: {len(tbx)}]\n")
        for bi, box in enumerate(tbx, 1):
            texts = [t.text for t in box.findall(".//" + DOCX_NS + "t") if t.text]
            out.append(f"[TEXT BOX {bi}] " + " | ".join(texts) + "\n")

    # footnotes / endnotes
    for part_name in ("footnotes", "endnotes"):
        try:
            part = doc.part.package.part_related_by(
                "http://schemas.openxmlformats.org/officeDocument/2006/relationships/" + part_name)
            texts = [t.text for t in part.element.findall(".//" + DOCX_NS + "t") if t.text]
            if texts:
                out.append(f"\n[{part_name.upper()}]\n" + " | ".join(texts) + "\n")
        except Exception:
            pass
    return "".join(out)


def extract_pptx(path):
    from pptx import Presentation
    prs = Presentation(path)
    out = [f"Presentation: slides={len(prs.slides)}\n"]
    for si, slide in enumerate(prs.slides, 1):
        out.append(f"\n## SLIDE {si}\n")
        for shi, shape in enumerate(slide.shapes, 1):
            if shape.has_text_frame:
                txt = shape.text_frame.text
                if txt.strip():
                    out.append(f"[shape {shi} | {shape.shape_type} | {shape.name}]\n{txt}\n\n")
            if getattr(shape, "has_table", False) and shape.has_table:
                tbl = shape.table
                out.append(f"[table {shi} rows={len(tbl.rows)} cols={len(tbl.columns)}]\n")
                for row in tbl.rows:
                    out.append("\t".join(c.text.replace("\n", " ") for c in row.cells) + "\n")
                out.append("\n")
        try:
            if slide.has_notes_slide:
                notes = slide.notes_slide.notes_text_frame.text
                if notes.strip():
                    out.append(f"[NOTES]\n{notes}\n\n")
        except Exception:
            pass
    return "".join(out)


def extract_pdf(path):
    from pypdf import PdfReader
    reader = PdfReader(path)
    out = [f"PDF: pages={len(reader.pages)}\n"]
    try:
        meta = reader.metadata or {}
        if meta:
            out.append("Metadata: " + json.dumps({k: str(v) for k, v in meta.items()},
                                                 ensure_ascii=False) + "\n")
    except Exception:
        pass
    empty = 0
    for pi, page in enumerate(reader.pages, 1):
        try:
            txt = page.extract_text() or ""
        except Exception as exc:  # pragma: no cover
            txt = f"[extraction error: {exc}]"
        if not txt.strip():
            empty += 1
            txt = "[page has no extractable text layer - scanned image / vector only]"
        out.append(f"\n## PAGE {pi}/{len(reader.pages)}\n{txt}\n")
    out.append(f"\nPages without text layer: {empty}/{len(reader.pages)}\n")
    return "".join(out)


def strings_from_binary(data, min_len=4):
    """Printable ASCII + UTF-16LE runs, with byte offsets."""
    res = []
    ascii_re = re.compile(rb"[\x20-\x7e]{%d,}" % min_len)
    for m in ascii_re.finditer(data):
        res.append((m.start(), m.group().decode("ascii")))
    utf16_re = re.compile((r"(?:[\x20-\x7e]\x00){%d,}" % min_len).encode())
    for m in utf16_re.finditer(data):
        try:
            s = m.group().decode("utf-16-le")
        except Exception:
            continue
        res.append((m.start(), s))
    res.sort()
    return res


def extract_doc(path):
    """Legacy .doc (OLE2). Best effort: WordDocument stream + printable runs."""
    out = []
    try:
        import olefile
        ole = olefile.OleFileIO(path)
        out.append("OLE streams: " + ", ".join("/".join(s) for s in ole.listdir()) + "\n\n")
        if ole.exists("WordDocument"):
            data = ole.openstream("WordDocument").read()
        else:
            data = open(path, "rb").read()
        ole.close()
    except Exception:
        data = open(path, "rb").read()
    runs = strings_from_binary(data, min_len=4)
    out.append(f"Printable runs extracted: {len(runs)}\n"
               "NOTE: legacy binary .doc - text recovered via run extraction "
               "(character order preserved as stored; layout/formatting not representable).\n\n")
    for off, s in runs:
        out.append(f"{off:>10}\t{s}\n")
    return "".join(out)


def extract_pub(path):
    data = open(path, "rb").read()
    runs = strings_from_binary(data, min_len=4)
    out = [f"Microsoft Publisher binary. size={len(data)} bytes\n"
           f"Printable runs extracted: {len(runs)}\n\n"]
    for off, s in runs:
        out.append(f"{off:>10}\t{s}\n")
    return "".join(out)


def extract_psd(path):
    from psd_tools import PSDImage
    psd = PSDImage.open(path)
    out = [f"PSD: width={psd.width} height={psd.height} "
           f"channels={psd.channels} depth={psd.depth} mode={psd.color_mode}\n"]
    def walk(layers, depth=0):
        for l in layers:
            pad = "  " * depth
            out.append(f"{pad}- [{l.kind}] {l.name!r} bbox={l.bbox} "
                       f"visible={l.visible} opacity={l.opacity}\n")
            try:
                if l.kind == "type":
                    out.append(f"{pad}    TEXT: {l.text}\n")
            except Exception:
                pass
            if l.is_group():
                walk(l, depth + 1)
    try:
        walk(list(psd))
    except Exception as exc:
        out.append(f"[layer walk error: {exc}]\n")
    return "".join(out)


def extract_ai(path):
    out = []
    try:
        from pypdf import PdfReader
        reader = PdfReader(path)
        out.append(f"AI (PDF-compatible): pages={len(reader.pages)}\n")
        for pi, page in enumerate(reader.pages, 1):
            out.append(f"\n## PAGE {pi}\n{page.extract_text() or '[no text layer]'}\n")
        return "".join(out)
    except Exception:
        pass
    data = open(path, "rb").read()
    runs = strings_from_binary(data, min_len=6)
    out.append(f"AI binary. size={len(data)} printable runs={len(runs)}\n\n")
    for off, s in runs:
        out.append(f"{off:>10}\t{s}\n")
    return "".join(out)


def describe_image(path):
    from PIL import Image
    info = {}
    with Image.open(path) as im:
        info.update(format=im.format, width=im.width, height=im.height,
                    mode=im.mode, frames=getattr(im, "n_frames", 1))
        exif = {}
        try:
            raw = im.getexif()
            for k, v in raw.items():
                exif[str(k)] = str(v)[:400]
        except Exception:
            pass
        if exif:
            info["exif"] = exif
        try:
            if im.info.get("dpi"):
                info["dpi"] = tuple(im.info["dpi"])
        except Exception:
            pass
    return info


def describe_mp4(path):
    """Minimal MP4 atom walk: ftyp brand, mvhd duration."""
    info = {}
    with open(path, "rb") as fh:
        data = fh.read(1 << 20)
    if len(data) > 12 and data[4:8] == b"ftyp":
        info["ftyp_brand"] = data[8:12].decode("latin-1")
    with open(path, "rb") as fh:
        fh.seek(0)
        while True:
            head = fh.read(8)
            if len(head) < 8:
                break
            size = int.from_bytes(head[:4], "big")
            name = head[4:8].decode("latin-1", "replace")
            if size == 1:
                size = int.from_bytes(fh.read(8), "big")
                body_off = 16
            else:
                body_off = 8
            if name == "moov":
                buf = fh.read(size - body_off)
                i = buf.find(b"mvhd")
                if i >= 0:
                    ver = buf[i + 4]
                    if ver == 0:
                        ts = int.from_bytes(buf[i + 16:i + 20], "big")
                        du = int.from_bytes(buf[i + 20:i + 24], "big")
                    else:
                        ts = int.from_bytes(buf[i + 24:i + 28], "big")
                        du = int.from_bytes(buf[i + 28:i + 36], "big")
                    if ts:
                        info["duration_seconds"] = round(du / ts, 3)
                break
            if size <= 0:
                break
            fh.seek(size - 8, 1)
    return info


def archive_listing(path, ext):
    entries = []
    if ext == ".zip":
        with zipfile.ZipFile(path) as zf:
            for zi in zf.infolist():
                entries.append({"name": zi.filename, "bytes": zi.file_size,
                                "compressed": zi.compress_size,
                                "crc32": f"{zi.CRC:08x}",
                                "modified": list(zi.date_time)})
    elif ext == ".7z":
        import py7zr
        with py7zr.SevenZipFile(path) as z:
            for zi in z.getnames():
                entries.append({"name": zi})
            for f in z.list():
                for e in entries:
                    if e["name"] == f.filename:
                        e.update(bytes=f.uncompressed, crc32=f.crc32,
                                 compressed=f.compressed, is_dir=f.is_directory)
    elif ext == ".rar":
        with open(path, "rb") as fh:
            head = fh.read(16)
        entries.append({"note": "RAR archive - listing requires unrar/7z binary "
                                "(not available in this sandbox); bytes pinned by sha256",
                        "signature": head[:8].hex(),
                        "is_rar5": head[:8] == b"Rar!\x1a\x07\x01\x00"})
    return entries


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def main():
    files = subprocess.run(["git", "-C", SRC, "ls-files", "-z"],
                           capture_output=True, check=True).stdout.split(b"\0")
    files = sorted(f.decode("utf-8") for f in files if f)
    total = len(files)

    head_commit = subprocess.run(["git", "-C", SRC, "rev-parse", "HEAD"],
                                 capture_output=True, check=True).stdout.decode().strip()
    assert head_commit == SRC_COMMIT, head_commit

    for sub in ("00-manifest", "01-text-verbatim", "02-extracted", "03-binary-meta"):
        os.makedirs(os.path.join(DST, sub), exist_ok=True)

    records = []
    for seq, rel in enumerate(files, 1):
        src_path = os.path.join(SRC, rel)
        size = os.path.getsize(src_path)
        sha = sha256_file(src_path)
        ext = os.path.splitext(rel)[1].lower()
        with open(src_path, "rb") as fh:
            head = fh.read(8192)

        rec = dict(seq=seq, path=rel, bytes=size, sha256=sha, ext=ext,
                   out_path="", out_bytes=0, chars=0, lines=0,
                   encoding="", method="", status="ok")

        is_text = ext in TEXT_EXT or b"\x00" not in head
        if is_text and ext not in (".pdf", ".doc", ".ai", ".pub", ".psd"):
            raw = open(src_path, "rb").read()
            text, enc = decode_text(raw)
            out_rel = os.path.join("01-text-verbatim", rel)
            dst = os.path.join(DST, out_rel)
            ensure_parent(dst)
            shutil.copyfile(src_path, dst)
            assert sha256_file(dst) == sha, f"copy mismatch {rel}"
            rec.update(out_path=out_rel.replace(os.sep, "/"),
                       out_bytes=os.path.getsize(dst), chars=len(text),
                       lines=text.count("\n") + (0 if text.endswith("\n") or not text else 1),
                       encoding=enc,
                       method="verbatim byte-for-byte copy (UTF-8/GB18030 decoded for char count)")
            records.append(rec)
            continue

        method = None
        body = None
        err = None
        try:
            if ext == ".xls":
                body = extract_xls(src_path); method = "xlrd 2.x - every sheet, every row, every cell (date cells rendered as datetime)"
            elif ext == ".xlsx":
                body = extract_xlsx(src_path); method = "openpyxl read-only - every sheet, every row, every cell, formulas preserved (data_only=False)"
            elif ext == ".docx":
                body = extract_docx(src_path); method = "python-docx - body paragraphs + tables + headers/footers + text boxes + notes, document order"
            elif ext == ".pptx":
                body = extract_pptx(src_path); method = "python-pptx - every slide, every shape text, every table, notes"
            elif ext == ".pdf":
                body = extract_pdf(src_path); method = "pypdf - every page text layer (image-only pages flagged, not dropped)"
            elif ext == ".doc":
                body = extract_doc(src_path); method = "olefile + printable-run extraction (legacy binary .doc)"
            elif ext == ".pub":
                body = extract_pub(src_path); method = "Microsoft Publisher binary + printable-run extraction"
            elif ext == ".psd":
                body = extract_psd(src_path); method = "psd-tools - full layer tree, names, bboxes, text layers"
            elif ext == ".ai":
                body = extract_ai(src_path); method = "pypdf (PDF-compatible AI) else printable-run extraction"
        except Exception as exc:  # noqa: BLE001
            err = f"{type(exc).__name__}: {exc}"

        if body is not None:
            out_rel = os.path.join("02-extracted", rel + ".extracted.md")
            dst = os.path.join(DST, out_rel)
            ensure_parent(dst)
            text = header_block(seq, total, rel, size, sha, method) + body
            with open(dst, "w", encoding="utf-8") as fh:
                fh.write(text)
            rec.update(out_path=out_rel.replace(os.sep, "/"), method=method,
                       out_bytes=os.path.getsize(dst), chars=len(text),
                       lines=text.count("\n"), encoding="utf-8")
            if err:
                rec["status"] = "partial: " + err
            records.append(rec)
            continue

        # binary / media / archive / firmware
        info = {"source_repo": SRC_REPO, "source_branch": SRC_BRANCH,
                "source_commit": SRC_COMMIT, "path": rel, "bytes": size,
                "sha256": sha, "seq": seq, "note":
                "Binary payload pinned by sha256 + commit (byte-exact recovery: "
                "git show 5acb6132a6a6090bfc777c324cfea6bc8dfb877a:" + rel + ")"}
        if err:
            info["extraction_error"] = err
            rec["status"] = "metadata-only: " + err
        try:
            if ext in IMAGE_EXT and ext != ".psd":
                info["image"] = describe_image(src_path)
            elif ext in MEDIA_EXT:
                info["video"] = describe_mp4(src_path)
            elif ext in ARCHIVE_EXT:
                info["archive"] = archive_listing(src_path, ext)
            elif ext == ".bin":
                runs = strings_from_binary(head, min_len=6)
                info["magic_hex"] = head[:16].hex()
                info["head_strings"] = [s for _, s in runs][:50]
                info["head_strings_note"] = ("first 8 KiB only; full payload is firmware "
                                             "and is pinned by sha256, not text-extracted")
        except Exception as exc:  # noqa: BLE001
            info["extraction_error"] = f"{type(exc).__name__}: {exc}"
            rec["status"] = "metadata-only: " + str(exc)

        out_rel = os.path.join("03-binary-meta", rel + ".meta.json")
        dst = os.path.join(DST, out_rel)
        ensure_parent(dst)
        payload = json.dumps(info, ensure_ascii=False, indent=2, default=str)
        with open(dst, "w", encoding="utf-8") as fh:
            fh.write(payload + "\n")
        rec.update(out_path=out_rel.replace(os.sep, "/"),
                   method=info.get("method") or "binary metadata (sha256 + intrinsic properties)",
                   out_bytes=os.path.getsize(dst), chars=len(payload) + 1,
                   lines=payload.count("\n") + 2, encoding="utf-8")
        records.append(rec)

    # ---------------- manifests ---------------- #
    with open(os.path.join(DST, "00-manifest", "FILE-INDEX.csv"), "w",
              newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["seq", "path", "bytes", "sha256", "ext", "kind", "method",
                    "artifact_path", "artifact_bytes", "chars", "lines",
                    "encoding", "status"])
        for r in records:
            kind = r["out_path"].split("/")[0]
            w.writerow([r["seq"], r["path"], r["bytes"], r["sha256"], r["ext"],
                        kind, r["method"], r["out_path"], r["out_bytes"],
                        r["chars"], r["lines"], r["encoding"], r["status"]])

    with open(os.path.join(DST, "00-manifest", "FILE-INDEX.json"), "w",
              encoding="utf-8") as fh:
        json.dump(records, fh, ensure_ascii=False, indent=1, default=str)

    # tree
    tree = ["# Full directory structure - Angora-1 @ arena/01a0ce39-angora", ""]
    tree.append(f"- repo: https://github.com/{SRC_REPO}")
    tree.append(f"- branch: `{SRC_BRANCH}`")
    tree.append(f"- commit: `{SRC_COMMIT}`")
    tree.append(f"- tracked files: {total}")
    tree.append(f"- total bytes: {sum(r['bytes'] for r in records)}")
    tree.append("")
    tree.append("```")
    last_parts = []
    for r in records:
        parts = r["path"].split("/")
        for i in range(len(parts) - 1):
            if i >= len(last_parts) or last_parts[i] != parts[i]:
                tree.append("  " * i + parts[i] + "/")
        last_parts = parts
        tree.append("  " * (len(parts) - 1) + parts[-1] + f"  [{r['bytes']} B]")
    tree.append("```")
    with open(os.path.join(DST, "00-manifest", "FULL-TREE.md"), "w",
              encoding="utf-8") as fh:
        fh.write("\n".join(tree) + "\n")

    # catalog (reading order, path + size before each artifact)
    cat = ["# Ingest catalog - one entry per source file, in reading order", "",
           f"Source: `{SRC_REPO}` @ `{SRC_BRANCH}` (`{SRC_COMMIT}`) - {total} files", ""]
    for r in records:
        cat.append(f"## {r['seq']:04d}/{total}  `{r['path']}`  ({r['bytes']} bytes)")
        cat.append(f"- sha256: `{r['sha256']}`")
        cat.append(f"- artifact: `{r['out_path']}` ({r['out_bytes']} bytes, {r['chars']} chars)")
        cat.append(f"- method: {r['method']}")
        cat.append(f"- status: {r['status']}")
        cat.append("")
    with open(os.path.join(DST, "00-manifest", "INGEST-CATALOG.md"), "w",
              encoding="utf-8") as fh:
        fh.write("\n".join(cat) + "\n")

    summary = {
        "source_repo": SRC_REPO,
        "source_branch": SRC_BRANCH,
        "source_commit": SRC_COMMIT,
        "source_files": total,
        "artifacts": len(records),
        "source_bytes": sum(r["bytes"] for r in records),
        "artifact_bytes": sum(r["out_bytes"] for r in records),
        "artifact_chars": sum(r["chars"] for r in records),
        "artifact_lines": sum(r["lines"] for r in records),
        "by_kind": {},
        "by_ext": {},
        "statuses": {},
    }
    for r in records:
        k = r["out_path"].split("/")[0]
        s = summary["by_kind"].setdefault(k, {"files": 0, "bytes": 0, "chars": 0})
        s["files"] += 1
        s["bytes"] += r["out_bytes"]
        s["chars"] += r["chars"]
        e = summary["by_ext"].setdefault(r["ext"] or "(none)", {"files": 0, "bytes": 0})
        e["files"] += 1
        e["bytes"] += r["bytes"]
        summary["statuses"][r["status"]] = summary["statuses"].get(r["status"], 0) + 1
    with open(os.path.join(DST, "00-manifest", "SUMMARY.json"), "w",
              encoding="utf-8") as fh:
        json.dump(summary, fh, ensure_ascii=False, indent=2)

    print(json.dumps({k: summary[k] for k in
                      ("source_files", "artifacts", "source_bytes",
                       "artifact_bytes", "artifact_chars", "by_kind")},
                     ensure_ascii=False, indent=2))
    print("STATUS-COUNT:", json.dumps(summary["statuses"], ensure_ascii=False))


if __name__ == "__main__":
    main()
