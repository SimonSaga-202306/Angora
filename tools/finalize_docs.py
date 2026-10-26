#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate the ingest README + SUMMARY layer-4 stats from the manifests."""
import csv
import json
import os
from collections import Counter, OrderedDict

D = "/home/user/Angora/ingest/angora-1__arena-01a0ce39__5acb613"
COMMIT = "5acb6132a6a6090bfc777c324cfea6bc8dfb877a"
BRANCH = "arena/01a0ce39-angora"


def fmt(n):
    return f"{n:,}"


def main():
    recs = json.load(open(f"{D}/00-manifest/FILE-INDEX.json"))
    summary = json.load(open(f"{D}/00-manifest/SUMMARY.json"))
    arows = list(csv.DictReader(open(f"{D}/04-archive-members/ARCHIVE-MEMBERS-INDEX.csv",
                                     encoding="utf-8")))
    l4_files = []
    for root, _, files in os.walk(f"{D}/04-archive-members"):
        for f in files:
            if f == "ARCHIVE-MEMBERS-INDEX.csv":
                continue                     # index, not a member artifact
            p = os.path.join(root, f)
            l4_files.append((os.path.relpath(p, D), os.path.getsize(p)))
    l4_bytes = sum(b for _, b in l4_files)
    l5_files = []
    for root, _, files in os.walk(f"{D}/05-nontext-content"):
        for f in files:
            p = os.path.join(root, f)
            l5_files.append((os.path.relpath(p, D), os.path.getsize(p)))
    l5_bytes = sum(b for _, b in l5_files)
    l5dirs = {}
    for rel, b in l5_files:
        k = rel.split("/")[1] if len(rel.split("/")) > 1 else rel
        t = l5dirs.setdefault(k, [0, 0])
        t[0] += 1
        t[1] += b
    deep = json.load(open(f"{D}/05-nontext-content/DEEP-INGEST.json"))

    by_kind = Counter(r["kind"] for r in arows)
    top = OrderedDict()
    for r in recs:
        k = r["path"].split("/")[0] if "/" in r["path"] else "(root)"
        t = top.setdefault(k, {"f": 0, "b": 0, "c": 0})
        t["f"] += 1
        t["b"] += r["bytes"]
        t["c"] += r["chars"]

    summary["layer_04_archive_members"] = {
        "member_rows": len(arows),
        "artifacts": len(l4_files),
        "artifact_bytes": l4_bytes,
        "by_kind": dict(by_kind),
        "archives": sorted({r["archive"] for r in arows}),
    }
    summary["layer_05_nontext_content"] = {
        "artifacts": len(l5_files), "artifact_bytes": l5_bytes,
        "by_area": {k: {"files": v[0], "bytes": v[1]} for k, v in sorted(l5dirs.items())},
        "firmware": deep["firmware"], "pdf_scan": deep["pdf_scan"],
        "appledouble": deep["appledouble"], "cad": deep["cad"],
    }
    summary["grand_total_artifacts"] = summary["artifacts"] + len(l4_files) + len(l5_files)
    summary["grand_total_artifact_bytes"] = (summary["artifact_bytes"] + l4_bytes + l5_bytes)
    json.dump(summary, open(f"{D}/00-manifest/SUMMARY.json", "w"),
              ensure_ascii=False, indent=2)

    L = []
    L.append("# 全量读取入库 — SimonSaga-202306/Angora-1 @ arena/01a0ce39-angora\n")
    L.append("> **入库原则：不合并（NO MERGING）。** 一个源文件 = 一个产物；压缩包内每个成员也各自成产物。"
             f"781 个源文件 → {len(recs)} 个一级产物 + {len(l4_files)} 个压缩包成员产物。"
             "保留原始相对路径、原始字节哈希、原始文件名（含中文、空格、大小写）。\n")
    L.append("## 1. 源信息\n")
    L.append("| 项目 | 值 |\n|---|---|")
    L.append("| 仓库 | https://github.com/SimonSaga-202306/Angora-1 |")
    L.append(f"| 分支 | `{BRANCH}` |")
    L.append(f"| commit | `{COMMIT}` |")
    L.append(f"| 文件总数（`git ls-files`，递归） | **{fmt(summary['source_files'])}** |")
    L.append("| 目录 | 57 个子目录 + 根目录，最深 5 层 |")
    L.append(f"| 源字节总量 | **{fmt(summary['source_bytes'])}** bytes (≈787.97 MB) |")
    L.append(f"| 产物文件总数 | **{fmt(summary['grand_total_artifacts'])}**"
             f"（{fmt(summary['artifacts'])} 一级 + {fmt(len(l4_files))} 压缩包成员"
             f" + {fmt(len(l5_files))} 深层内容） |")
    L.append(f"| 产物字节总量 | **{fmt(summary['grand_total_artifact_bytes'])}** bytes |")
    L.append(f"| 产物字符总量 | **{fmt(summary['artifact_chars'])}** 字符 / {fmt(summary['artifact_lines'])} 行 |")
    L.append("| 缺漏文件数 | **0** |\n")

    L.append("## 2. 目录结构总览（先结构、后内容）\n")
    L.append("完整逐文件目录树（带字节数）见 [`00-manifest/FULL-TREE.md`](00-manifest/FULL-TREE.md)。\n")
    L.append("| 顶层目录 / 文件 | 文件数 | 源字节 | 产物字符 |\n|---|---:|---:|---:|")
    for k, v in sorted(top.items(), key=lambda x: -x[1]["f"]):
        L.append(f"| `{k}` | {v['f']} | {fmt(v['b'])} | {fmt(v['c'])} |")
    L.append(f"| **合计** | **{fmt(summary['source_files'])}** | "
             f"**{fmt(summary['source_bytes'])}** | **{fmt(summary['artifact_chars'])}** |\n")

    L.append("## 3. 按扩展名统计\n")
    L.append("| 扩展名 | 文件数 | 源字节 |\n|---|---:|---:|")
    for k, v in sorted(summary["by_ext"].items(), key=lambda x: -x[1]["files"]):
        L.append(f"| `{k}` | {v['files']} | {fmt(v['bytes'])} |")
    L.append("")

    L.append("## 4. 产物布局（四层，逐文件，不合并）\n")
    L.append("""```
ingest/angora-1__arena-01a0ce39__5acb613/
├── 00-manifest/             FULL-TREE.md · FILE-INDEX.csv/.json · INGEST-CATALOG.md
│                            VERIFICATION.md · SUMMARY.json
├── 01-text-verbatim/        392 个文本类文件：逐字节原样副本（sha256 已复验）
├── 02-extracted/            178 个 Office/PDF/PSD/AI/CDR：全量文本抽取
├── 03-binary-meta/          211 个图片/视频/固件：字节身份 + 内在属性
├── 04-archive-members/      压缩包解层：每个成员各自成产物 + ARCHIVE-MEMBERS-INDEX.csv
└── 05-nontext-content/      “无法文本化”项目的深层内容：固件全解 / 扫描 PDF / AppleDouble / CAD
```\n""")
    L.append("### 4.1 一级层（781 源文件 → 781 产物，1:1）\n")
    L.append("| 产物类别 | 文件数 | 处理方式 | 完整性保证 |\n|---|---:|---|---|")
    L.append("| `01-text-verbatim` | 392 | 原样复制，未格式化/重排/改写 | sha256 逐字节复验一致 |")
    L.append("| `02-extracted` | 178 | xls/xlsx 逐 sheet 逐行逐单元格（公式保留）；docx 段落+表格+页眉页脚+文本框+脚注；"
             "pptx 逐 slide 逐 shape+表格+备注；pdf 逐页文本层；**legacy .doc 走 Word97 CLX 分片表解码，全文正文逐字还原**；"
             "psd 图层树；ai/cdr/pub 结构+文本串 | 无行/无字符截断，页/表/行计数写在产物内 |")
    L.append("| `03-binary-meta` | 211 | 原文件 sha256 + 字节数 + 内在属性（分辨率/EXIF/时长/压缩包条目表/RIFF 块表/图层树） "
             "| 由 sha256 + commit 双向锁定，可逐字节复原 |")
    L.append("")
    L.append("### 4.2 压缩包解层（`04-archive-members`，额外一层，不替代原文件）\n")
    L.append("| 成员类型 | 数量 | 说明 |\n|---|---:|---|")
    names = {"verbatim": "文本/配置/Gerber 成员：逐字节原样副本",
             "extracted": "Office/PDF 成员：全量文本抽取",
             "meta": "图片等二进制成员：sha256 + 内在属性",
             "covered-by-loose-file": "RAR 成员：仓库内已有同名同大小独立文件，按散文件覆盖（sha256 已记）",
             "differs-from-loose-file": "RAR 成员：与散文件大小不同（不同版本），已标注",
             "inventory": "嵌套大体积包（3D STEP 展开 86 MB）：记录容器 sha256 + 完整条目表，不展开入库"}
    for k, v in by_kind.most_common():
        L.append(f"| `{k}` | {v} | {names.get(k, '')} |")
    L.append(f"\n涉及压缩包 {len(summary['layer_04_archive_members']['archives'])} 个，"
             f"成员记录 {fmt(len(arows))} 条，落盘成员产物 {fmt(len(l4_files))} 个 / {fmt(l4_bytes)} bytes。"
             "逐条见 [`04-archive-members/ARCHIVE-MEMBERS-INDEX.csv`]"
             "(04-archive-members/ARCHIVE-MEMBERS-INDEX.csv)。\n")

    L.append("### 4.3 为什么二进制媒体不入正文\n")
    L.append("图片(192)、视频(11)、PSD(8)、固件 bin(1)、CDR(2)、CAD(1) 等占源体积 787.97 MB 的 700+ MB，"
             "无法无损转文本；摘要化会违反“不得以摘要代替原文”。因此保留原始字节的密码学身份"
             "（sha256 + 源 commit + 字节数），**原文可逐字节复原**，不做任何有损转录。"
             "可还原成员的原文件另有 `04-archive-members` 一层逐成员入库。\n")

    L.append("## 5. 读取顺序（先结构、后内容）\n")
    L.append("1. `00-manifest/FULL-TREE.md` — 完整递归目录树（781 个文件全部列出，含字节数）")
    L.append("2. `00-manifest/INGEST-CATALOG.md` — 按 seq 0001→0781，每个文件先标注 **路径 + 大小 + sha256**，再给出产物")
    L.append("3. `01-text-verbatim/` → `02-extracted/` → `03-binary-meta/` — 逐文件全文")
    L.append("4. `04-archive-members/` — 压缩包内逐成员全文/元数据\n")
    L.append("排序规则：UTF-8 路径字典序（与 `git ls-files` 一致），100% 可复现。\n")

    L.append("## 6. 原先“无法文本化”的五类，现在的实际入库深度\n")
    fw = deep["firmware"]
    L.append("| 项目 | 数量 | 已入库到什么层级 | 产物 |\n|---|---|---|---|")
    L.append(f"| 扫描/矢量 PDF | 3 个文件 3 页 | 页级 notes（尺寸/绘制算子/字体/内嵌图清单）"
             f"+ 内嵌位图原样 4 张 = {deep['pdf_scan']['images']} 个 | `05-nontext-content/pdf-scan/` |")
    L.append(f"| `.bin` 固件 62 MB | 1 | **完全解开**：XZ → tar（3 成员）→ UBI → UBIFS，"
             f"入口 {fmt(fw['entries'])} 条；文本 {fmt(fw['text_files'])} 个 / "
             f"{fmt(fw['text_bytes'])} B 逐字节副本；非文本 {fmt(fw['binary_files'])} 个 "
             f"逐个 sha256；upgrade.cfg 声明的 md5 与实算**一致** | "
             f"`05-nontext-content/firmware/…` |")
    L.append(f"| `.psd` 之外的 CAD STEP | 1（嵌套 7z） | 头段原文 + 全文件 "
             f"{fmt(deep['cad']['step_lines'])} 行实体直方图（{fmt(deep['cad']['entities'])} 条实体 / "
             f"{deep['cad']['entity_types']} 类） | `05-nontext-content/cad/` |")
    L.append(f"| `__MACOSX/._*` AppleDouble | 8 | 逐字段解析（magic/version/Finder type+creator/"
             f"资源叉偏移）；例：`PDF `/`ART5`、`JPEG`/`8BIM` | `05-nontext-content/appledouble/` |")
    L.append(f"| `.pub` ×4 / `.ai` ×2 / `.cdr` ×2 | 8 | OLE 流清单 + 可打印串全量（不抽样）+ "
             "`.cdr` RIFF 块表 + `.ai` PDF 兼容层文本 | `02-extracted/` |")
    L.append("")
    L.append("仍然存在的硬限制（已逐条标注，不是遗漏）：\n")
    L.append("| 项 | 说明 |\n|---|---|")
    L.append("| 扫描件无 OCR | 沙箱无 tesseract，且这些是土耳其语证照/保修书；"
             "已存位图与算子清单，不做文字猜测 |")
    L.append("| RAR 载荷 | 无 unrar 二进制、`unrar-cffi` 编译失败：成员字节由容器 sha256 锁定；"
             "15 个成员中 14 个另有散文件覆盖，1 个版本不同已标注 |")
    L.append("| `.pub` 版式 | MS Publisher 二进制正文流无公开规范解码器：字符全量但版式不可复原 |")
    L.append("| 86 MB STEP | 逐行统计而非整体入库：几何文件本身由 sha256 锁定 |")
    L.append("")
    L.append("## 7. 复核方式\n")
    L.append("```bash\n# 16 项完整性校验（文件数/路径集合/字节总量/逐一 sha256/空产物/目录层级/压缩包成员）\n")
    L.append("/tmp/venv/bin/python tools/verify_ingest.py\n\n")
    L.append("# 任意源文件按哈希找回\ngit -C /tmp/audit show "
             f"{COMMIT}:'<原始路径>' | sha256sum\n```\n")
    open(f"{D}/README.md", "w").write("\n".join(L) + "\n")
    print("README bytes", os.path.getsize(f"{D}/README.md"))
    print("layer4 artifacts", len(l4_files), "bytes", l4_bytes)
    print("summary", summary["artifacts"], "+", len(l4_files), "=", summary["grand_total_artifacts"])


if __name__ == "__main__":
    main()
