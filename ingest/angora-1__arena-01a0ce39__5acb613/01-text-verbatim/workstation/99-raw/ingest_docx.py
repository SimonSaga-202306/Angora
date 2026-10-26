#!/usr/bin/env python3
"""Extract every .docx in the repo into the knowledge base (MD + JSON).

Preserves paragraph order and keeps embedded tables as pipe-tables.
Run: python3 workstation/99-raw/ingest_docx.py
"""
import os, re, json, glob, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, "workstation", "01-knowledge-base", "docx")
os.makedirs(OUT, exist_ok=True)

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def para_text(p):
    return "".join(t.text or "" for t in p.iter(W_NS + "t"))


def extract(path):
    """-> list of blocks: ('p', text) | ('table', [[..]])"""
    z = zipfile.ZipFile(path)
    xml = z.read("word/document.xml").decode("utf8", "ignore")
    import xml.etree.ElementTree as ET
    root = ET.fromstring(xml)
    body = root.find(W_NS + "body")
    blocks = []
    if body is None:
        return blocks
    for el in body.iter():
        pass
    for child in body:
        tag = child.tag.replace(W_NS, "")
        if tag == "p":
            t = para_text(child)
            if t.strip():
                blocks.append(("p", t.strip()))
        elif tag == "tbl":
            rows = []
            for tr in child.findall(W_NS + "tr"):
                cells = []
                for tc in tr.findall(W_NS + "tc"):
                    ct = " ".join(para_text(p) for p in tc.findall(W_NS + "p"))
                    cells.append(ct.strip())
                rows.append(cells)
            if rows:
                blocks.append(("table", rows))
    return blocks


def render(blocks):
    out = []
    for kind, v in blocks:
        if kind == "p":
            out.append(v)
        else:
            width = max(len(r) for r in v)
            out.append("")
            out.append("| " + " | ".join(v[0]) + " |")
            out.append("|" + "|".join("---" for _ in range(width)) + "|")
            for r in v[1:]:
                cells = (r + [""] * width)[:width]
                out.append("| " + " | ".join(c.replace("|", "\\|") for c in cells) + " |")
            out.append("")
    return "\n".join(out)


def main():
    files = [f for f in glob.glob(os.path.join(ROOT, "**", "*.docx"), recursive=True)
             if not os.path.relpath(f, ROOT).startswith(("workstation", ".git", "~$"))]
    files.sort()
    print(f"found {len(files)} docx\n")
    index = []
    for p in files:
        rel = os.path.relpath(p, ROOT)
        slug = re.sub(r"[^a-z0-9]+", "-", rel.lower()).strip("-")
        try:
            blocks = extract(p)
        except Exception as e:
            print(f"  ⚠️ {rel}: {e}")
            continue
        text = render(blocks)
        chars = len(text)
        md = [f"# {os.path.basename(rel)}", "", f"> 来源：`{rel}`　·　字符数：{chars:,}", "",
              "---", "", text]
        with open(os.path.join(OUT, slug + ".md"), "w", encoding="utf-8") as f:
            f.write("\n".join(md))
        json.dump({"source": rel, "chars": chars,
                   "blocks": [{"type": k, "data": v} for k, v in blocks]},
                  open(os.path.join(OUT, slug + ".json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        index.append({"file": rel, "slug": slug, "chars": chars})
        print(f"  ✅ {rel[:64]:64s} chars={chars:>9,}")
    json.dump(index, open(os.path.join(OUT, "_index.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"\nwrote {len(index)} docx transcriptions + _index.json")


if __name__ == "__main__":
    main()
