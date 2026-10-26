#!/usr/bin/env python3
"""Generic xlsx -> knowledge-base (.md + .json) ingester.

Every sheet, every non-empty row becomes a JSON record; a readable markdown
table (or fenced block when the row is long) is emitted alongside.
Run: python3 workstation/99-raw/ingest_xlsx.py
"""
import os, re, json
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, "workstation", "01-knowledge-base", "spreadsheets")
os.makedirs(OUT, exist_ok=True)

TARGETS = [
    ("Turkey Client List.xlsx", "turkey-client-list",
     "Angora 的土耳其客户 / 潜在线索名单（姓名、公司、邮箱、网址、意向产品）"),
    ("Saga Feature List_7.5.x_L2+.xlsx", "saga-feature-list-7.5-l2plus",
     "Saga 7.5.x L2+ 软件能力全量清单（应答 Levent 技术提问的权威底稿）"),
    ("RFP/Saga Software Function List-release 7.3.0.xlsx", "saga-software-function-list-7.3.0",
     "Saga 软件功能清单 release 7.3.0（含 AlleyCat3 / AlleyCat5 两代平台对照）"),
    ("RFP/Turk_Telekom_Test_Items.xlsx", "turk-telekom-test-items",
     "Turk Telekom 验收测试项"),
    ("PVCs.xlsx", "pvcs-inventory",
     "PVC 标签 / 铭牌耗材库存（订单号、已用量、单位成本，对应 2026-02-05 微信对话）"),
    ("成本统计.xlsx", "cost-breakdown", "成本统计"),
    ("运费一览表.xlsx", "freight-table", "运费一览表"),
    ("mac_address&serial_number.xlsx", "mac-serial", "MAC 地址与序列号"),
]


def cellstr(v):
    if v is None:
        return ""
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return str(v).strip()


def sheet_rows(ws):
    """return list of (row_values,); stop after 400 empty rows"""
    rows, empty = [], 0
    for r in ws.iter_rows(values_only=True):
        vals = [cellstr(c) for c in r]
        if any(vals):
            rows.append(vals)
            empty = 0
        else:
            empty += 1
            if empty > 400:
                break
    return rows


def to_records(rows):
    """first non-empty row that has >=2 filled cells is treated as the header"""
    if not rows:
        return [], []
    hi = 0
    for i, r in enumerate(rows[:12]):
        if sum(1 for c in r if c) >= 2:
            hi = i
            break
    header = [c if c else f"col{j+1}" for j, c in enumerate(rows[hi])]
    recs = []
    for r in rows[hi + 1:]:
        if not any(r):
            continue
        rec = {}
        for j, c in enumerate(r):
            k = header[j] if j < len(header) else f"col{j+1}"
            if c:
                rec[k] = c
        if rec:
            recs.append(rec)
    return header, recs


def md_for(title, desc, sheets):
    out = [f"# {title}", "", f"> {desc}", ""]
    for name, header, recs, rows in sheets:
        out += [f"\n## Sheet: {name}", "", f"记录数：**{len(recs)}**", ""]
        if not recs:
            continue
        # markdown table if the header is short enough
        if len(header) <= 8 and all(len(str(h)) <= 28 for h in header):
            out.append("| " + " | ".join(str(h) for h in header) + " |")
            out.append("|" + "|".join("---" for _ in header) + "|")
            for rec in recs[:500]:
                cells = []
                for h in header:
                    v = str(rec.get(h, "")).replace("|", "\\|").replace("\n", " ")
                    cells.append(v[:120])
                out.append("| " + " | ".join(cells) + " |")
            if len(recs) > 500:
                out.append(f"\n_(表格截断，完整数据见同名 .json，共 {len(recs)} 条)_")
        else:
            out.append("```")
            for r in rows[:500]:
                out.append(" | ".join(x for x in r if x))
            out.append("```")
        out.append("")
    return "\n".join(out)


def main():
    written = []
    for rel, slug, desc in TARGETS:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            print("  skip (missing):", rel)
            continue
        wb = load_workbook(p, data_only=True)
        sheets = []
        total = 0
        for ws in wb.worksheets:
            rows = sheet_rows(ws)
            header, recs = to_records(rows)
            total += len(recs)
            sheets.append((ws.title, header, recs, rows))
        md = md_for(slug, f"来源：`{rel}`　·　{desc}", sheets)
        open(os.path.join(OUT, slug + ".md"), "w", encoding="utf-8").write(md)
        json.dump({"source": rel, "description": desc,
                   "sheets": [{"name": n, "header": h, "records": r} for n, h, r, _ in sheets]},
                  open(os.path.join(OUT, slug + ".json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        print(f"  ✅ {slug:38s} sheets={len(sheets):2d} records={total}")
        written.append((slug, len(sheets), total))
    print("\nwritten:", len(written))
    return written


if __name__ == "__main__":
    main()
