#!/usr/bin/env python3
"""Ingest legacy .xls / .xlsx commercial documents (quotations, proforma
invoices, packing lists, contracts) into MD + JSON.

These are the *source of truth* for counterparty contact details, addresses,
tax IDs, model/price/qty lines and payment terms.
Run: python3 workstation/99-raw/ingest_xls_docs.py
"""
import os, re, json, glob
import xlrd
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, "workstation", "01-knowledge-base", "commercial-docs")
os.makedirs(OUT, exist_ok=True)

SKIP_DIRS = {"workstation", ".git"}
NOISE = re.compile(r"^\*+$|^\s*$")


def rows_xls(p):
    wb = xlrd.open_workbook(p)
    out = []
    for sh in wb.sheets():
        for r in range(sh.nrows):
            vals = [str(sh.cell_value(r, c)).strip() for c in range(sh.ncols)]
            if any(vals):
                out.append((sh.name, vals))
    return out


def rows_xlsx(p):
    wb = load_workbook(p, data_only=True)
    out = []
    for ws in wb.worksheets:
        for row in ws.iter_rows(values_only=True):
            vals = [("" if c is None else str(c).strip()) for c in row]
            if any(vals):
                out.append((ws.title, vals))
    return out


def fact_scan(rows):
    """pull out counterparty facts that are easy to lose"""
    flat = " | ".join(x for _, r in rows for x in r if x)
    facts = {}
    pats = {
        "seller": r"(Zhengzhou Saga Telecom[^\n|]*)",
        "buyer": r"Buyer:\s*\|?\s*([^\n|]+)",
        "invoice_no": r"Invoice No\.?:?\s*\|?\s*([A-Z0-9]+)",
        "date": r"(?:Invoice Date|Date):\s*\|?\s*([^\n|]+)",
        "payment_term": r"Payment Term:\s*\|?\s*([^\n|]+)",
        "price_term": r"Price Term:\s*\|?\s*([^\n|]+)",
        "issued_by": r"Issued By:\s*\|?\s*([^\n|]+)",
        "contact": r"Contact Person:\s*\|?\s*([^\n|]+)",
        "email": r"([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})",
        "phone_tr": r"(\+?90\s*\(?\d{3}\)?[\s\d]{6,})",
        "tax_id": r"(?:Tax Information|Vergi|VKN)[^\d|]{0,20}(\d[\d\s]{8,})",
        "address_ankara": r"([^\n|]*Ankara[^\n|]*)",
        "amount": r"(?:Total|Amount)[\s\S]{0,40}?([\d,]+\.\d{2})",
    }
    for k, pat in pats.items():
        m = re.search(pat, flat, re.I)
        if m:
            facts[k] = " ".join(m.group(1).split())[:160]
    # emails can repeat
    ems = sorted(set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", flat)))
    if ems:
        facts["emails"] = ems
    # model lines (Saga / SmartByte part numbers)
    mods = sorted(set(re.findall(r"\b(?:STC|STI|LT)-[A-Z0-9\-]+", flat)))
    if mods:
        facts["models"] = mods
    return facts


def main():
    files = []
    for ext in ("xls", "xlsx"):
        for p in glob.glob(os.path.join(ROOT, "**", "*." + ext), recursive=True):
            rel = os.path.relpath(p, ROOT)
            if rel.split(os.sep)[0] in SKIP_DIRS:
                continue
            files.append(rel)
    files.sort()
    print(f"scanning {len(files)} commercial docs\n")
    index = []
    for rel in files:
        p = os.path.join(ROOT, rel)
        try:
            rows = rows_xls(p) if rel.lower().endswith(".xls") else rows_xlsx(p)
        except Exception as e:
            print(f"  ⚠️ {rel}: {e}")
            continue
        if not rows:
            continue
        facts = fact_scan(rows)
        slug = re.sub(r"[^a-z0-9]+", "-", rel.lower()).strip("-")
        md = [f"# {rel}", "", f"> 原始文件：`{rel}`", ""]
        if facts:
            md += ["## 关键字段", ""]
            for k, v in facts.items():
                md.append(f"- **{k}**：{v if isinstance(v, str) else ', '.join(v)}")
            md.append("")
        md += ["## 原文表格", "", "```"]
        last = None
        for sh, vals in rows[:200]:
            if sh != last:
                md.append(f"\n--- sheet: {sh} ---")
                last = sh
            line = " | ".join(x for x in vals if x)
            if line and not NOISE.match(line):
                md.append(line[:400])
        md += ["```"]
        if len(rows) > 200:
            md += ["", f"_(截断，原文共 {len(rows)} 行)_"]
        with open(os.path.join(OUT, slug + ".md"), "w", encoding="utf-8") as f:
            f.write("\n".join(md))
        index.append({"file": rel, "slug": slug, "rows": len(rows), "facts": facts})
        print(f"  ✅ {rel[:70]:70s} rows={len(rows):5d} facts={len(facts)}")
    json.dump(index, open(os.path.join(OUT, "_index.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"\nwrote {len(index)} docs + _index.json")


if __name__ == "__main__":
    main()
