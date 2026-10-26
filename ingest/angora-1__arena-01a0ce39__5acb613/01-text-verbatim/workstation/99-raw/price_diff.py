#!/usr/bin/env python3
"""Diff SmartByte pricelists across years -> price-increase curve per model."""
import re, os, json
from openpyxl import load_workbook

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

FILES = {
    "2024-02": "SmartByte Managed Industrial Ethernet switch  pricelist on CNY for Simon-20240227.xlsx",
    "2026-09": "SmartByte Managed Industrial Ethernet switch  pricelist on CNY for Simon-价格有效期2026.09.1--2026.12.30.xlsx",
    "ENT-2024-05": "SmartByte managed Ethernet switch pricelist for Simon-20240516 更新.xlsx",
    "ENT-2026-09": "SmartByte managed Ethernet switch pricelist for Simon-价格有效期2026.09.1--2026.12.30.xlsx",
}

MODEL = re.compile(r"(LT-[A-Z0-9\-]+)", re.I)


def extract(fn):
    p = os.path.join(ROOT, fn)
    if not os.path.exists(p):
        return {}, "MISSING"
    wb = load_workbook(p, data_only=True)
    out = {}
    for ws in wb.worksheets:
        for row in ws.iter_rows(values_only=True):
            cells = [str(c).strip() for c in row if c is not None]
            if not cells:
                continue
            joined = " ".join(cells)
            m = MODEL.search(joined)
            if not m:
                continue
            model = m.group(1).upper()
            # find numeric price: prefer a cell that looks like a price
            nums = []
            for c in cells:
                if re.fullmatch(r"[\d,]+(\.\d+)?", c) and "," not in c:
                    v = float(c)
                    if 50 <= v <= 200000:
                        nums.append(v)
            if nums:
                out.setdefault(model, nums)
    return out, "OK"


def main():
    data = {}
    for tag, fn in FILES.items():
        d, st = extract(fn)
        data[tag] = d
        print(f"== {tag} [{st}] models={len(d)}")

    def cmp(a_tag, b_tag, label):
        a, b = data.get(a_tag, {}), data.get(b_tag, {})
        print(f"\n### {label}  ({a_tag} -> {b_tag})")
        rows = []
        for m in sorted(set(a) & set(b)):
            pa = min(a[m])
            pb = min(b[m])
            if pa <= 0:
                continue
            chg = (pb - pa) / pa * 100
            rows.append((m, pa, pb, chg))
        rows.sort(key=lambda r: -abs(r[3]))
        for m, pa, pb, chg in rows:
            print(f"{m:38s} {pa:>9.0f} -> {pb:>9.0f}  {chg:+7.1f}%")
        if rows:
            avg = sum(r[3] for r in rows) / len(rows)
            med = sorted(r[3] for r in rows)[len(rows) // 2]
            print(f"-- n={len(rows)}  mean={avg:+.1f}%  median={med:+.1f}%")
        only_new = sorted(set(b) - set(a))
        only_old = sorted(set(a) - set(b))
        print(f"-- only in {b_tag} ({len(only_new)}): {', '.join(only_new)}")
        print(f"-- only in {a_tag} ({len(only_old)}): {', '.join(only_old)}")

    cmp("2024-02", "2026-09", "INDUSTRIAL managed")
    cmp("ENT-2024-05", "ENT-2026-09", "ENTERPRISE managed")


if __name__ == "__main__":
    main()
