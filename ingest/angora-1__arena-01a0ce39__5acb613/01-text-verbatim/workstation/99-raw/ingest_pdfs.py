#!/usr/bin/env python3
"""Extract every not-yet-extracted PDF in the repo into the knowledge base
(MD + JSON). Skips the Gmail PDFs already converted under gmail-threads/.
Run: python3 workstation/99-raw/ingest_pdfs.py
"""
import os, re, json, glob, hashlib
try:
    from pypdf import PdfReader
except ImportError:
    from PyPDF2 import PdfReader

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, "workstation", "01-knowledge-base", "pdfs")
os.makedirs(OUT, exist_ok=True)

ALREADY = ("Gmail - ",)


def slug(rel):
    return re.sub(r"[^a-z0-9]+", "-", rel.lower()).strip("-")


def main():
    files = []
    for p in glob.glob(os.path.join(ROOT, "**", "*.pdf"), recursive=True) + \
             glob.glob(os.path.join(ROOT, "**", "*.PDF"), recursive=True):
        rel = os.path.relpath(p, ROOT)
        if rel.split(os.sep)[0] in ("workstation", ".git"):
            continue
        files.append(rel)
    files.sort()
    print(f"found {len(files)} PDFs\n")
    index = []
    for rel in files:
        base = os.path.basename(rel)
        if base.startswith(ALREADY):
            print(f"  skip (already in gmail-threads): {rel}")
            continue
        p = os.path.join(ROOT, rel)
        try:
            r = PdfReader(p)
            pages = []
            for i, pg in enumerate(r.pages):
                try:
                    pages.append((i + 1, (pg.extract_text() or "").strip()))
                except Exception as e:
                    pages.append((i + 1, f"[page extract error: {e}]"))
        except Exception as e:
            print(f"  ⚠️ {rel}: {e}")
            continue
        text = "\n".join(t for _, t in pages)
        chars = len(text)
        s = slug(rel)
        if chars < 40:
            print(f"  ⚠️ {rel}: only {chars} chars (scanned / image-only?)")
        md = [f"# {base}", "", f"> 来源：`{rel}`　·　页数：{len(pages)}　·　提取字符数：{chars}", ""]
        if chars < 40:
            md += ["> ⚠️ **本文件为扫描件或图片型 PDF，无可提取文本层**，需 OCR。原文已保留在仓库。", ""]
        md += ["---", ""]
        for n, t in pages:
            md += [f"\n## Page {n}\n", t if t else "_(无文本)_", ""]
        with open(os.path.join(OUT, s + ".md"), "w", encoding="utf-8") as f:
            f.write("\n".join(md))
        json.dump({"source": rel, "pages": len(pages), "chars": chars,
                   "content": [{"page": n, "text": t} for n, t in pages]},
                  open(os.path.join(OUT, s + ".json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        index.append({"file": rel, "slug": s, "pages": len(pages), "chars": chars})
        print(f"  ✅ {rel[:62]:62s} pages={len(pages):3d} chars={chars}")
    json.dump(index, open(os.path.join(OUT, "_index.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"\nwrote {len(index)} PDF transcriptions + _index.json")


if __name__ == "__main__":
    main()
