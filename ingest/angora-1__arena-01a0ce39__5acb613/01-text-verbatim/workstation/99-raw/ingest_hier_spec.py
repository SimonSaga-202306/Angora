#!/usr/bin/env python3
"""Render hierarchical switch-spec spreadsheets (merged category cells) into
nested markdown + json.

Layout understood:
    col A : (blank / section banner)
    col B : TOP category     (merged across rows)
    col C : SUB category     (merged across rows)
    col D : feature name
    col E..: value(s)
Merged cells are forward-filled so every row carries its category.
Run: python3 workstation/99-raw/ingest_hier_spec.py
"""
import os, re, json
from openpyxl import load_workbook

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, "workstation", "01-knowledge-base", "spreadsheets")
os.makedirs(OUT, exist_ok=True)

TARGETS = [
    ("Saga Feature List_7.5.x_L2+.xlsx", "saga-feature-list-7.5-l2plus",
     "Saga 7.5.x L2+ 软件能力全量清单",
     "应答 Levent 技术提问（如 RIP/OSPF/BGP/ECMP/VRRP）的权威底稿；芯片平台 Marvell 98DX2515/2518 (AC5 Lite)"),
    ("RFP/Saga Software Function List-release 7.3.0.xlsx", "saga-software-function-list-7.3.0",
     "Saga 软件功能清单 release 7.3.0",
     "含 Marvell AlleyCat 3 与 AlleyCat 5 两代平台逐项对照"),
]


def grid(ws):
    g = [[("" if c is None else str(c).strip()) for c in row]
         for row in ws.iter_rows(values_only=True)]
    return g


def fill_merged(ws, g):
    """forward-fill merged ranges with the anchor value"""
    for rng in ws.merged_cells.ranges:
        c1, r1, c2, r2 = rng.min_col - 1, rng.min_row - 1, rng.max_col - 1, rng.max_row - 1
        val = g[r1][c1] if r1 < len(g) and c1 < len(g[r1]) else ""
        for r in range(r1, min(r2 + 1, len(g))):
            for c in range(c1, min(c2 + 1, len(g[r]))):
                g[r][c] = val
    return g


def parse(g):
    """-> (banner, [(top, sub, item, value)])"""
    banner, rows = None, []
    for r in g:
        a = r[0] if len(r) > 0 else ""
        b = r[1] if len(r) > 1 else ""
        c = r[2] if len(r) > 2 else ""
        d = r[3] if len(r) > 3 else ""
        vals = [x for x in r[4:] if x]
        if not any([b, c, d]) and not vals:
            if a and not banner:
                banner = a
            continue
        if a:
            banner = a
        if not d and not vals:
            continue
        rows.append((b, c, d, " / ".join(vals)))
    return banner, rows


def render(slug, title, desc, banner, rows):
    md = [f"# {title}", "", f"> 来源：`{slug}`", "", f"> {desc}", ""]
    if banner:
        md += [f"> 表头：{banner}", ""]
    cur_top = cur_sub = None
    n = 0
    for top, sub, item, val in rows:
        if top and top != cur_top:
            md += [f"\n## {top}\n"]
            cur_top, cur_sub = top, None
        if sub and sub != cur_sub:
            md += [f"\n### {sub}\n"]
            cur_sub = sub
        if item:
            md.append(f"- **{item}**" + (f" — `{val}`" if val and val != "☑️" else
                                        (" — ✅" if val == "☑️" else "")))
            n += 1
    md += ["", f"\n_共 {n} 项特性_"]
    return "\n".join(md)


def main():
    for rel, slug, title, desc in TARGETS:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            print("  skip:", rel)
            continue
        wb = load_workbook(p, data_only=True)
        ws = wb.worksheets[0]
        g = fill_merged(ws, grid(ws))
        banner, rows = parse(g)
        md = render(rel, title, desc, banner, rows)
        open(os.path.join(OUT, slug + ".md"), "w", encoding="utf-8").write(md)
        json.dump({"source": rel, "title": title, "description": desc, "banner": banner,
                   "rows": [{"category": a, "subcategory": b, "feature": c, "value": d}
                            for a, b, c, d in rows]},
                  open(os.path.join(OUT, slug + ".json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        print(f"  ✅ {slug:36s} features={len(rows)}")
        # quick capability probe
        blob = " ".join(c for _, _, c, _ in rows).lower()
        for k in ["rip", "ospf", "bgp", "ecmp", "vrrp", "macsec", "stack", "iec61850", "tsn"]:
            if k in blob:
                print(f"       ↳ mentions '{k}'")


if __name__ == "__main__":
    main()
