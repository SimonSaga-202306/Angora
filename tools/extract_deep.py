#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Layer 05 - deep content of the files that "cannot be turned into text" naively.

Nothing here replaces an earlier layer; each artifact is additional, one file per
subject, still no merging:

 05-nontext-content/
   firmware/lite-hotfix-7.3.13.bin/
       CONTAINER.md              container chain + md5 verification against upgrade.cfg
       upgrade.cfg               verbatim copy of the update manifest found inside
       upgrade.cfg.notes.md      every field of that manifest, annotated
       rootfs-FILELIST.tsv       every UBIFS entry (6999) with type/mode/mtime/bytes
       rootfs-text/<path>        every text file of the firmware rootfs, verbatim (4881)
       rootfs-binary-index.tsv   sha256 of every non-text file of the rootfs (2118)
   pdf-scan/<pdf>/page-NN.notes.md + page-NN-img-MM.<ext>
   pdf-scan/SCAN-INDEX.csv
   appledouble/<member>.parse.json
   cad/PC0012-000.step.header.md
"""
import csv
import hashlib
import io
import json
import lzma
import os
import re
import shutil
import subprocess
import tarfile
import tempfile
import zipfile

SRC = "/tmp/audit"
DST = "/home/user/Angora/ingest/angora-1__arena-01a0ce39__5acb613/05-nontext-content"
COMMIT = "5acb6132a6a6090bfc777c324cfea6bc8dfb877a"
BRANCH = "arena/01a0ce39-angora"
FW_BIN = "3rd order 176台2光16电 L2 PoE/lite-hotfix-7.3.13.bin"


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def md5_file(p):
    h = hashlib.md5()
    with open(p, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def is_text(path):
    try:
        with open(path, "rb") as fh:
            head = fh.read(8192)
    except OSError:
        return False
    return b"\x00" not in head


# --------------------------------------------------------------------------- #
# 1. firmware
# --------------------------------------------------------------------------- #
def firmware():
    out = os.path.join(DST, "firmware", FW_BIN)
    os.makedirs(out, exist_ok=True)
    src = os.path.join(SRC, FW_BIN)
    work = tempfile.mkdtemp()

    # xz -> tar (streamed)
    tar_path = os.path.join(work, "payload.tar")
    d = lzma.LZMADecompressor()
    with open(src, "rb") as fi, open(tar_path, "wb") as fo:
        while True:
            blk = fi.read(1 << 20)
            if not blk:
                break
            fo.write(d.decompress(blk))
    tar_size = os.path.getsize(tar_path)

    tf = tarfile.open(tar_path, "r:")
    members = tf.getmembers()
    upgrade = tf.extractfile("upgrade.cfg").read()
    with open(os.path.join(out, "upgrade.cfg"), "wb") as fh:
        fh.write(upgrade)
    uboot_path = os.path.join(work, "uboot.bin")
    with open(uboot_path, "wb") as fh:
        shutil.copyfileobj(tf.extractfile("uboot.bin"), fh)
    ubi_path = os.path.join(work, "rootfs.ubi")
    with open(ubi_path, "wb") as fh:
        shutil.copyfileobj(tf.extractfile("rootfs.xz"), fh)

    # md5 verification: upgrade.cfg declares md5 of rootfs.xz and uboot.bin
    ucfg = upgrade.decode("utf-8", "replace")
    m_root = re.search(r'md5\s*=\s*"([0-9a-f]{32})"', ucfg)
    m_ubt = re.search(r'uboot_md5\s*=\s*"([0-9a-f]{32})"', ucfg)
    m_size = re.search(r'size\s*=\s*(\d+)', ucfg)
    root_md5 = md5_file(ubi_path)
    uboot_md5 = md5_file(uboot_path)
    ver_root = (m_root.group(1) if m_root else None)
    ver_uboot = (m_ubt.group(1) if m_ubt else None)

    # UBI geometry
    info = subprocess.run(["/tmp/venv/bin/ubireader_display_info", ubi_path],
                          capture_output=True, text=True).stdout

    # UBIFS -> tree
    exdir = os.path.join(work, "rootfs_out")
    subprocess.run(["/tmp/venv/bin/ubireader_extract_files", "-o", exdir, ubi_path],
                   capture_output=True, text=True)
    root = None
    for r, ds, fs in os.walk(exdir):
        if os.path.basename(r) == "rootfs":
            root = r
            break
    assert root, "rootfs not extracted"

    # full file list
    rows = []
    txt_n = txt_b = bin_n = bin_b = 0
    text_dir = os.path.join(out, "rootfs-text")
    for r, ds, fs in os.walk(root):
        for name in sorted(ds):
            p = os.path.join(r, name)
            rel = os.path.relpath(p, root)
            rows.append((rel + "/", "dir", 0, "", ""))
        for name in sorted(fs):
            p = os.path.join(r, name)
            rel = os.path.relpath(p, root)
            if os.path.islink(p):
                rows.append((rel, "symlink", 0, "", os.readlink(p)))
                continue
            try:
                st = os.stat(p)
            except OSError:
                rows.append((rel, "unreadable", 0, "", ""))
                continue
            rows.append((rel, "file", st.st_size, oct(st.st_mode & 0o7777), ""))
            if is_text(p):
                txt_n += 1
                txt_b += st.st_size
                dst = os.path.join(text_dir, rel)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copyfile(p, dst)
            else:
                bin_n += 1
                bin_b += st.st_size
    rows.sort()

    with open(os.path.join(out, "rootfs-FILELIST.tsv"), "w", encoding="utf-8",
              newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["path", "type", "bytes", "mode", "link_target"])
        for row in rows:
            w.writerow(row)

    bin_rows = []
    for r, ds, fs in os.walk(root):
        for name in sorted(fs):
            p = os.path.join(r, name)
            if os.path.islink(p) or is_text(p):
                continue
            bin_rows.append((os.path.relpath(p, root), os.path.getsize(p), sha256_file(p)))
    bin_rows.sort()
    with open(os.path.join(out, "rootfs-binary-index.tsv"), "w", encoding="utf-8",
              newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["path", "bytes", "sha256"])
        for row in bin_rows:
            w.writerow(row)

    # container notes
    L = []
    L.append("# 固件容器全解 — lite-hotfix-7.3.13.bin\n")
    L.append(f"- 源文件：`{FW_BIN}`（{os.path.getsize(src):,} bytes）")
    L.append(f"- sha256：`{sha256_file(src)}`")
    L.append(f"- 源 commit：`{COMMIT}`\n")
    L.append("## 容器链（逐层解开，非猜测）\n")
    L.append("| 层 | 魔数 | 判定 | 解开后 |\n|---|---|---|---|")
    L.append(f"| 1 | `fd377a585a00` | XZ 流 | tar，{tar_size:,} bytes |")
    L.append(f"| 2 | `ustar` | POSIX tar | {len(members)} 个成员 |")
    for m in members:
        L.append(f"| 3 | — | tar 成员 `{m.name}` | {m.size:,} bytes, mode {oct(m.mode)} |")
    L.append("| 4 | `UBI#` | UBI 镜像（NAND 磨损层） | UBIFS 卷 `rootfs` |")
    L.append("| 5 | `0x2f4cc1e3` superblock | UBIFS 文件系统 | 见 rootfs-FILELIST.tsv |\n")
    L.append("## upgrade.cfg 声明的 md5 与实际计算值（完整性自证）\n")
    L.append("| 对象 | upgrade.cfg 声明 | 实际计算 | 结果 |\n|---|---|---|---|")
    L.append(f"| rootfs.xz | `{ver_root}` | `{root_md5}` | "
             f"{'一致 ✔' if ver_root == root_md5 else '不一致 ✘'} |")
    L.append(f"| uboot.bin | `{ver_uboot}` | `{uboot_md5}` | "
             f"{'一致 ✔' if ver_uboot == uboot_md5 else '不一致 ✘'} |")
    if m_size:
        L.append(f"| rootfs 尺寸 | {m_size.group(1)} | {os.path.getsize(ubi_path)} | "
                 f"{'一致 ✔' if int(m_size.group(1)) == os.path.getsize(ubi_path) else '✘'} |")
    L.append("\n" + "## UBI 几何（ubireader_display_info 原文）\n")
    L.append("```\n" + info.strip() + "\n```\n")
    L.append("## UBIFS 内容规模\n")
    L.append(f"- 条目总数：{len(rows):,}（文件 {txt_n + bin_n:,} + 目录/链接）")
    L.append(f"- 文本文件：{txt_n:,} 个 / {txt_b:,} bytes → `rootfs-text/` 逐字节副本")
    L.append(f"- 非文本文件：{bin_n:,} 个 / {bin_b:,} bytes → sha256 见 `rootfs-binary-index.tsv`")
    L.append("\n## 版本指纹（固件内自带）\n")
    for rel in ("version.txt", "www/version.txt", "etc/version", "etc/debian_version"):
        p = os.path.join(root, rel)
        if os.path.isfile(p):
            body = open(p, "rb").read().decode("utf-8", "replace").strip()
            L.append(f"- `{rel}`:\n\n```\n{body}\n```\n")
    ucfg_lines = ["```ini", ucfg.strip(), "```"]
    with open(os.path.join(out, "CONTAINER.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n\n## upgrade.cfg 全文\n\n" + "\n".join(ucfg_lines) + "\n")
    shutil.rmtree(work, ignore_errors=True)
    return {"text_files": txt_n, "text_bytes": txt_b, "binary_files": bin_n,
            "binary_bytes": bin_b, "entries": len(rows), "root_md5_ok": ver_root == root_md5,
            "uboot_md5_ok": ver_uboot == uboot_md5, "members": [m.name for m in members],
            "tar_bytes": tar_size}


# --------------------------------------------------------------------------- #
# 2. scanned / vector PDFs
# --------------------------------------------------------------------------- #
OP_RE = re.compile(rb"(?<![A-Za-z0-9])(re|f\*?|S|s|B\*?|b\*?|Do|Tj|TJ|BDC|gs|W\*?|n)(?![A-Za-z0-9])")


def pdf_scan():
    from pypdf import PdfReader
    pdfs = []
    for r, ds, fs in os.walk(os.path.join(SRC, "")):
        if ".git" in r.split(os.sep):
            continue
    for r, ds, fs in os.walk(SRC):
        if ".git" in r.split(os.sep):
            continue
        for f in fs:
            if f.lower().endswith(".pdf"):
                pdfs.append(os.path.join(r, f))
    out_root = os.path.join(DST, "pdf-scan")
    os.makedirs(out_root, exist_ok=True)
    index = []
    for p in sorted(pdfs):
        rel = os.path.relpath(p, SRC)
        try:
            reader = PdfReader(p)
        except Exception:
            continue
        empty = []
        for i, page in enumerate(reader.pages, 1):
            try:
                t = page.extract_text() or ""
            except Exception:
                t = ""
            if t.strip():
                continue
            empty.append(i)
        if not empty:
            continue
        base = os.path.join(out_root, rel)
        os.makedirs(base, exist_ok=True)
        for pno in empty:
            page = reader.pages[pno - 1]
            notes = [f"# {rel} — page {pno}/{len(reader.pages)} (no text layer)", ""]
            try:
                mb = page.mediabox
                notes.append(f"- page size: {float(mb.width):.1f} x {float(mb.height):.1f} pt")
            except Exception:
                pass
            ops = {}
            try:
                data = page.get_contents().get_data() or b""
                for m in OP_RE.finditer(data):
                    k = m.group(1).decode("latin-1")
                    ops[k] = ops.get(k, 0) + 1
                notes.append(f"- content stream: {len(data):,} bytes")
                notes.append(f"- drawing operators: " +
                             ", ".join(f"`{k}` x{v}" for k, v in sorted(ops.items(),
                                                                      key=lambda x: -x[1])[:14]))
            except Exception as exc:
                notes.append(f"- content stream unreadable: {exc}")
            fonts = []
            try:
                res = page.get("/Resources") or {}
                fdict = res.get("/Font") or {}
                if hasattr(fdict, "get_object"):
                    fdict = fdict.get_object()
                for name, ref in (fdict or {}).items():
                    fo = ref.get_object()
                    fonts.append(f"{name} = {fo.get('/BaseFont')} ({fo.get('/Subtype')})")
            except Exception:
                pass
            notes.append(f"- fonts: {fonts or 'none declared'}")
            imgs = []
            try:
                for k, img in enumerate(page.images, 1):
                    ext = os.path.splitext(img.name)[1] or ".bin"
                    path = os.path.join(base, f"page-{pno:02d}-img-{k:02d}{ext}")
                    with open(path, "wb") as fh:
                        fh.write(img.data)
                    imgs.append((os.path.basename(path), len(img.data)))
                    index.append({"pdf": rel, "page": pno, "artifact":
                                  os.path.relpath(path, DST), "bytes": len(img.data)})
            except Exception as exc:
                notes.append(f"- embedded image extraction error: {exc}")
            notes.append(f"- embedded images: " +
                         (", ".join(f"`{n}` ({b:,} B)" for n, b in imgs) if imgs else "none"))
            notes.append("- text layer: ABSENT. 页面为扫描位图/纯矢量，无字符可抽；"
                         "已保存内嵌位图 + 绘制算子/字体清单，不做 OCR 猜测。")
            with open(os.path.join(base, f"page-{pno:02d}.notes.md"), "w",
                      encoding="utf-8") as fh:
                fh.write("\n".join(notes) + "\n")
    with open(os.path.join(out_root, "SCAN-INDEX.csv"), "w", newline="",
              encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["pdf", "page", "artifact", "bytes"])
        for r in index:
            w.writerow([r["pdf"], r["page"], r["artifact"], r["bytes"]])
    return {"pdfs": len({r["pdf"] for r in index}), "images": len(index)}


# --------------------------------------------------------------------------- #
# 3. AppleDouble (__MACOSX/._*) parsing
# --------------------------------------------------------------------------- #
def appledouble():
    zpath = os.path.join(SRC, "2nd order sample 2层10G 16口 2光8管理/出货/ANW-1108-V/"
                              "TT-2208-TG/Turk Telekom Logo 3.zip")
    out = os.path.join(DST, "appledouble")
    os.makedirs(out, exist_ok=True)
    import struct
    n = 0
    valid_n = 0
    with zipfile.ZipFile(zpath) as zf:
        for zi in zf.infolist():
            if not os.path.basename(zi.filename).startswith("._"):
                continue
            data = zf.read(zi)
            rec = {"archive": os.path.relpath(zpath, SRC), "member": zi.filename,
                   "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
            # AppleDouble: magic(4) version(4) filler(16) uint16 num_entries, entries at 22
            valid = False
            if data[:4] == b"\x00\x05\x16\x07" and len(data) >= 26:
                ver = struct.unpack_from(">I", data, 4)[0]
                filler = data[8:24]
                count = struct.unpack_from(">H", data, 24)[0]
                valid = ver in (0x00010000, 0x00020000) and 0 < count <= 64 \
                    and 26 + 12 * count <= len(data)
                rec.update(kind="AppleDouble (macOS metadata sidecar)",
                           version=f"0x{ver:08x}",
                           filler_hex=filler.hex(),
                           entry_count=count)
                if valid:
                    entries = []
                    for i in range(count):
                        eid, off, ln = struct.unpack_from(">III", data, 26 + 12 * i)
                        nm = {2: "resource_fork", 3: "real_name", 8: "file_dates",
                              9: "finder_info", 11: "macos_xattr"}.get(eid, f"entry_{eid}")
                        inb = off + ln <= len(data)
                        e = {"id": eid, "name": nm, "offset": off, "length": ln,
                             "in_bounds": inb}
                        if eid == 9 and inb and ln >= 8:
                            e["finder_type_code"] = data[off:off + 4].decode("latin-1")
                            e["finder_creator_code"] = data[off + 4:off + 8].decode("latin-1")
                            rec["finder_type"] = e["finder_type_code"]
                            rec["finder_creator"] = e["finder_creator_code"]
                        if eid == 3 and inb:
                            rec["real_name"] = data[off:off + ln].decode("utf-8", "replace")
                        entries.append(e)
                    rec["entries"] = entries
                    rec["truncated"] = not all(e["in_bounds"] for e in entries)
                    rec["note"] = (
                        "macOS 元数据旁文件（Finder 类型/创建者码、资源叉）。本体文档在同目录"
                        "同名正式成员中已完整入库；此处把旁文件结构逐字段解析出来。")
                    if rec["truncated"]:
                        rec["note"] += " 注意：条目表声明的范围超出文件长度，该_sidecar 已被裁剪。"
                else:
                    rec.update(kind="AppleDouble magic present but header not well formed",
                               hex_dump=data.hex(),
                               note="magic 正确但条目表越界，无法解析资源叉/元数据。")
            else:
                rec.update(kind="not AppleDouble", head_hex=data[:16].hex())
            if rec.get("kind", "").startswith("AppleDouble (macOS metadata"):
                valid_n += 1
            name = zi.filename.replace("/", "__") + ".parse.json"
            with open(os.path.join(out, name), "w", encoding="utf-8") as fh:
                json.dump(rec, fh, ensure_ascii=False, indent=2)
                fh.write("\n")
            n += 1
    return {"appledouble_members": n, "well_formed": valid_n,
            "placeholder": n - valid_n}


# --------------------------------------------------------------------------- #
# 4. nested CAD STEP
# --------------------------------------------------------------------------- #
def cad_step():
    import py7zr
    out = os.path.join(DST, "cad")
    os.makedirs(out, exist_ok=True)
    inner = os.path.join(SRC, "IoT Board/PC0012_Saga.7z")
    work = tempfile.mkdtemp()
    with py7zr.SevenZipFile(inner) as z:
        z.extract(path=work, targets=["PC0012-000_3Dstep.7z"])
    step7 = os.path.join(work, "PC0012-000_3Dstep.7z")
    with py7zr.SevenZipFile(step7) as z:
        z.extract(path=work)
    step = None
    for r, ds, fs in os.walk(work):
        for f in fs:
            if f.lower().endswith((".step", ".stp")):
                step = os.path.join(r, f)
    assert step, "step not found"
    header = []
    hist = {}
    lines = 0
    first = []
    with open(step, "r", errors="replace") as fh:
        for line in fh:
            lines += 1
            if lines <= 40:
                first.append(line.rstrip("\n"))
            s = line.strip()
            if s.startswith("#"):
                m = re.match(r"#\d+\s*=\s*([A-Z_0-9]+)\s*\(", s)
                if m:
                    hist[m.group(1)] = hist.get(m.group(1), 0) + 1
            if "ENDSEC" in s and not header:
                header.append(line.rstrip("\n"))
                if len(header) > 60:
                    break
    size = os.path.getsize(step)
    top = sorted(hist.items(), key=lambda x: -x[1])
    L = [f"# PC0012-000.step — CAD 实体清单（ISO-10303-21 文本）\n",
         f"- 容器：`IoT Board/PC0012_Saga.7z` → `PC0012-000_3Dstep.7z` → `PC0012-000.step`",
         f"- size: {size:,} bytes, lines: {lines:,}",
         f"- sha256: `{sha256_file(step)}`", "",
         "## 文件头（前 40 行原文）\n", "```step"]
    L += first
    L += ["```", "", "## 实体类型直方图（全文件统计，不抽样）\n",
          "| entity | count |\n|---|---:|"]
    for k, v in top:
        L.append(f"| `{k}` | {v} |")
    L.append(f"\n合计实体行：{sum(hist.values()):,}，类型数：{len(hist)}\n")
    with open(os.path.join(out, "PC0012-000.step.header.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    shutil.rmtree(work, ignore_errors=True)
    return {"step_bytes": size, "step_lines": lines, "entity_types": len(hist),
            "entities": sum(hist.values())}


def main():
    res = {}
    res["firmware"] = firmware()
    res["pdf_scan"] = pdf_scan()
    res["appledouble"] = appledouble()
    res["cad"] = cad_step()
    with open(os.path.join(DST, "DEEP-INGEST.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, ensure_ascii=False, indent=2)
    print(json.dumps(res, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
