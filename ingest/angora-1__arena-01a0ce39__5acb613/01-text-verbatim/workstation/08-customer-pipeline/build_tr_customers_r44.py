#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_tr_customers_r44.py

生成仓库根目录 `TR Customers/` 文件夹：
  - 每个客户一个 MD（来源 = 01-text-verbatim/workstation/08-customer-pipeline/111-turkey-customer-pipeline.csv，145 行）
  - 若该客户在 08-followup-dossiers-2026-11-01/ 有深度档案（21 家），把档案原文**逐字并入**（不删改、不摘要替代）
  - Entegron / LONGLINE 不在 111 里（只在 110 竞对表 + 原始名单 #44），单独出一份并标注来源

约束：
  - **不合并任何客户记录**。111 里同名/近名的行（如 Makros A.Ş. 出现两次）**各自独立成文件**，
    仅在文件内加「⚠ 疑与 #NNN 同一家」交叉提示。
  - 不改动 `08-followup-dossiers-2026-11-01/` 里的任何原文件（只读取）。
"""
import csv
import io
import os
import re
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..'))
CSV_PATH = os.path.join(
    os.path.dirname(__file__), '111-turkey-customer-pipeline.csv')
DOSSIER_DIR = os.path.join(
    ROOT, 'ingest', 'angora-1__arena-01a0ce39__5acb613',
    '08-followup-dossiers-2026-11-01')
OUT_DIR = os.path.join(ROOT, 'TR Customers')

# 111 序号 -> (深度档案文件名, 档案里的编号)
DOSSIER_MAP = {
    '1':  '01-telkolink-gelecekbt.md',
    '2':  '02-nova-novacom.md',
    '3':  '03-snexus.md',
    '4':  '04-cenova.md',
    '5':  '05-cryptolink.md',
    '7':  '11-karer.md',
    '8':  '18-hane-elektronik.md',
    '9':  '19-oncu-guvenlik.md',
    '20': '20-opax.md',
    '21': '16-cctv-depo.md',
    '56': '10-optima.md',
    '57': '17-filiz-guvenlik.md',
    '58': '09-okisan.md',
    '80': '12-telemobil.md',
    '81': '14-makros.md',
    '82': '15-hafya.md',
    '84': '13-onsis.md',
    '86': '21-bilimsat-kilic.md',
    '91': '07-sami-ceuik.md',
    '92': '08-selim-kalaka.md',
}

TR_MAP = str.maketrans({'ı': 'i', 'İ': 'i', 'ş': 's', 'Ş': 's', 'ğ': 'g', 'Ğ': 'g',
                        'ü': 'u', 'Ü': 'u', 'ö': 'o', 'Ö': 'o', 'ç': 'c', 'Ç': 'c'})


def slug(text):
    t = text.translate(TR_MAP)
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    t = t.lower()
    t = re.sub(r'[^a-z0-9]+', '-', t).strip('-')
    return t[:48].strip('-')


def cell(text):
    """markdown 表格单元：转义竖线、换行转换、空值占位。"""
    t = (text or '').strip()
    if not t:
        return '—'
    t = t.replace('|', '\\|')
    t = re.sub(r'\r?\n+', '<br>', t)
    return t


def plain(text):
    return (text or '').strip()


def strip_md(text, limit=0):
    """给索引表用：去掉 markdown 修饰，避免截断时留下半个 ** 。"""
    t = plain(text)
    t = re.sub(r'\*\*|__|`|\*', '', t)
    t = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = re.sub(r'\s+', ' ', t).strip()
    if limit and len(t) > limit:
        t = t[:limit].rstrip(' -/,' ) + '…'
    return t


def name_key(name):
    n = re.sub(r'\*+', '', name).lower()
    n = re.split(r'[（(]', n)[0]
    return re.sub(r'[^a-z0-9]', '', n.translate(TR_MAP))[:12]


def full_key(name):
    n = re.sub(r'\*+', '', name).lower()
    n = re.split(r'[（(]', n)[0]
    return re.sub(r'[^a-z0-9]', '', n.translate(TR_MAP))


def is_same(a, b):
    """近名判定：短键相同，或整串互相包含（长度 >= 6，避免噪声）。"""
    ka, kb = name_key(a), name_key(b)
    fa, fb = full_key(a), full_key(b)
    if ka and ka == kb:
        return True
    if len(fa) >= 6 and len(fb) >= 6 and (fa in fb or fb in fa):
        return True
    return False


def main():
    rows = list(csv.DictReader(io.open(CSV_PATH, encoding='utf-8-sig')))
    os.makedirs(OUT_DIR, exist_ok=True)

    # 近名索引（只做提示，不合并）
    names = [(r['序号'], r['公司']) for r in rows]

    index_rows = []
    dup_pairs = []
    written = 0

    for r in rows:
        no = r['序号']
        company = plain(r['公司'])
        fname = '%03d-%s.md' % (int(no), slug(company) or 'customer')
        tier = plain(r['层级'])
        score = plain(r['我方评估(0-100)'])
        dossier = DOSSIER_MAP.get(no)
        dup = [x for x, nm in names if x != no and is_same(company, nm)]
        for d in dup:
            pair = tuple(sorted([no, d], key=lambda v: int(v)))
            if pair not in dup_pairs:
                dup_pairs.append(pair)

        L = []
        L.append('# %s · %s' % (no, company))
        L.append('')
        L.append('> **评级**：%s ｜ **我方评估**：%s/100 ｜ **核验日期**：%s'
                 % (tier or '—', score or '—', plain(r['核验日期']) or '—'))
        L.append('> **一句话**：%s' % (plain(r['场景/定位']) or '—'))
        if dup:
            L.append('>')
            L.append('> ⚠ **疑与 #%s 为同一家**（源表未合并，本文件亦不合并）——'
                     '对客户沟通前请人工确认主体。' % ' / #'.join(dup))
        if dossier:
            L.append('>')
            L.append('> 📚 本客户有**完整深度档案**（八段 + 核验补录 + 商业深挖），'
                     '已逐字并入本文末尾「附：完整研究档案」。')
        L.append('')
        L.append('---')
        L.append('')

        L.append('## 身份卡')
        L.append('')
        L.append('| 项 | 内容 |')
        L.append('|---|---|')
        for label, col in [('公司', '公司'), ('层级', '层级'), ('总部/城市', '总部/城市'),
                           ('场景/定位', '场景/定位'), ('自有品牌', '自有品牌'),
                           ('名单来源', '渠道来源'), ('源表位', '序号')]:
            L.append('| %s | %s |' % (label, cell(r.get(col, ''))))
        L.append('')

        L.append('## 我方核实的交换机产品线')
        L.append('')
        L.append(plain(r['我方核实的交换机产品线']) or '—')
        L.append('')

        L.append('## 当前供应链（核实口径）')
        L.append('')
        L.append(plain(r['当前供应链(核实)']) or '—')
        L.append('')

        L.append('## 联系人（逐字抄录）')
        L.append('')
        L.append('```')
        L.append(plain(r['联系人(用户侧)']) or '（源表无联系人）')
        L.append('```')
        L.append('')

        L.append('## 证据与核实等级')
        L.append('')
        L.append('| 项 | 内容 |')
        L.append('|---|---|')
        L.append('| 证据来源（独立核实） | %s |' % cell(r['证据来源(独立核实)']))
        L.append('| 核验日期 | %s |' % cell(r['核验日期']))
        L.append('| AI-1 初筛 | %s |' % cell(r['AI-1初筛']))
        L.append('| AI-2 初筛 | %s |' % cell(r['AI-2初筛']))
        L.append('| 我方评估 | %s / 100 |' % cell(r['我方评估(0-100)']))
        L.append('')
        L.append('> 说明：「联系人」列来自**用户侧**（展会/微信/名单），'
                 '「证据来源」列是**我方独立抓取**到的内容。两者不要混用。')
        L.append('')

        L.append('## 建议动作')
        L.append('')
        L.append(plain(r['建议动作']) or '—')
        L.append('')

        L.append('## 备注')
        L.append('')
        L.append(plain(r['备注']) or '—')
        L.append('')

        if dossier:
            dpath = os.path.join(DOSSIER_DIR, dossier)
            body = io.open(dpath, encoding='utf-8').read().rstrip('\n')
            L.append('---')
            L.append('')
            L.append('## 附：完整研究档案（逐字并入，未删改）')
            L.append('')
            L.append('> 源文件：`ingest/angora-1__arena-01a0ce39__5acb613/'
                     '08-followup-dossiers-2026-11-01/%s`' % dossier)
            L.append('> ')
            L.append('> 该档案含：r41 八段原文 + r42「核验补录 2026-11-01」'
                     '+ r43「商业深挖 2026-11-01」。以下为全文，未做摘要替换。')
            L.append('')
            L.append(body)
            L.append('')

        out = os.path.join(OUT_DIR, fname)
        io.open(out, 'w', encoding='utf-8').write('\n'.join(L))
        written += 1
        index_rows.append((no, company, plain(r['总部/城市']), tier, score,
                           '有' if dossier else '—', fname))

    # 111 之外的补充档案：Entegron / LONGLINE
    extra_src = '06-entegron-longline.md'
    extra = os.path.join(DOSSIER_DIR, extra_src)
    if os.path.exists(extra):
        body = io.open(extra, encoding='utf-8').read().rstrip('\n')
        L = []
        L.append('# 146 · Entegron ／ LONGLINE（同一母公司，双品牌）')
        L.append('')
        L.append('> **评级**：A-（客户侧）／竞对（`110` 第 20 行） ｜ **我方评估**：见档案 ｜ '
                 '**核验日期**：2026-11-01')
        L.append('> **一句话**：土耳其运营体 **Longline Bilişim** + 阿联酋自贸区实体 '
                 '**Entegron Technology FZE**，自有 PoE 31 款 + SFP 全系。')
        L.append('>')
        L.append('> ⚠ **本客户不在 `111` 管线里**（管线只收客户侧），'
                 '它出现在 `06-competitors/110` 第 **20** 行与原始名单 #44。')
        L.append('')
        L.append('---')
        L.append('')
        L.append('## 身份卡')
        L.append('')
        L.append('| 项 | 内容 |')
        L.append('|---|---|')
        L.append('| 公司 | Longline Bilişim Teknolojileri Ltd. Şti. ／ Entegron'
                 '（Entegron Technology FZE，阿联酋自贸区） |')
        L.append('| 总部/城市 | İstanbul / Bayrampaşa（Longline Plaza）；'
                 'Entegron 侧为阿联酋 |')
        L.append('| 场景/定位 | 服务器翻新 + 网络分销 + 自有品牌交换机／SFP／工业交换机｜'
                 '同时是**我方竞对** |')
        L.append('| 源表位 | `06-competitors/110` 第 20 行；原始名单 #44；'
                 '`08-followup-dossiers/06` |')
        L.append('')
        L.append('## 我方核实的交换机产品线')
        L.append('')
        L.append('双品牌：**Longline（LNG 系交换机 + SFP 全线）**；'
                 '**Entegron（entegronnetwork.com）：Ethernet 11 / **PoE 31** / '
                 'EPON ONU 9 / GPON ONU 6**。另有工业交换机与边缘交换机站 '
                 '`longlinenetwork.com`。')
        L.append('')
        L.append('## 当前供应链（核实口径）')
        L.append('')
        L.append('自有品牌（贴牌）+ 服务器翻新/备件贸易；'
                 '⭐ **`Entegron Technology FZE` 是阿联酋自贸区实体**，'
                 '在土耳其进口提单中作为供货方出现 → 合同主体与结算路径需先确认。')
        L.append('')
        L.append('## 联系人（逐字抄录）')
        L.append('')
        L.append('```')
        L.append('info@entegronnetwork.com（Entegron 线）')
        L.append('Longline：经 longline.com.tr / hepsiburada 店铺（顾问式销售 Tolga Y.）')
        L.append('采购经理 Safa Özer ／ 董事 Ercan Çiçekci（2026-11-01 深挖所得，见档案）')
        L.append('```')
        L.append('')
        L.append('## 证据与核实等级')
        L.append('')
        L.append('| 项 | 内容 |')
        L.append('|---|---|')
        L.append('| 证据来源（独立核实） | longline.com.tr、makinaturkiye 企业页、'
                 'LinkedIn 企业页、Crunchbase、Volza 公开提单 |')
        L.append('| 核验日期 | 2026-11-01 |')
        L.append('| 我方评估 | 客户侧 30A／45A；竞对侧见 `110` 第 20 行 |')
        L.append('')
        L.append('> 说明：本表**无 111 源行**，故不填「联系人（用户侧）」以外的字段，'
                 '详细证据见文末并入的完整档案。')
        L.append('')
        L.append('## 建议动作')
        L.append('')
        L.append('- 先定**合同主体与结算**（Longline Ltd. 还是 Entegron FZE？'
                 '货发 İstanbul 还是 Jebel Ali？），再报价。')
        L.append('- 用 **3 年保修**打它「全系 1 年」的短板；报价走 **USD**。')
        L.append('- 首单 **前 T/T 100%**（离岸主体）。')
        L.append('')
        L.append('## 备注')
        L.append('')
        L.append('同时是**我方竞对**（`110` 第 20 行）→ 谈客户的同时按竞对做监控，'
                 '**不要一次性交出完整 BOM 与成本结构**。')
        L.append('')
        L.append('---')
        L.append('')
        L.append('## 附：完整研究档案（逐字并入，未删改）')
        L.append('')
        L.append('> 源文件：`ingest/angora-1__arena-01a0ce39__5acb613/'
                 '08-followup-dossiers-2026-11-01/%s`' % extra_src)
        L.append('')
        L.append(body)
        L.append('')
        io.open(os.path.join(OUT_DIR, '146-entegron-longline.md'), 'w',
                encoding='utf-8').write('\n'.join(L))
        written += 1
        index_rows.append(('146', 'Entegron ／ LONGLINE（双品牌）', 'İstanbul / Bayrampaşa',
                           'A-（客户侧）', '30A/45A', '有', '146-entegron-longline.md'))

    # ---------- README ----------
    R = []
    R.append('# TR Customers · 土耳其客户总表（一客户一 MD）')
    R.append('')
    R.append('**这个文件夹是什么**：把仓库里**已有的土耳其客户底稿**，'
             '拆成**一家一个 Markdown 文件**，方便逐家看、逐家发、逐家跟。')
    R.append('')
    R.append('- 文件数：**%d**（客户 **%d** 家 + 本 README）' % (written + 1, written))
    R.append('- 数据源（唯一权威）：`ingest/angora-1__arena-01a0ce39__5acb613/'
             '01-text-verbatim/workstation/08-customer-pipeline/'
             '111-turkey-customer-pipeline.csv`（**145 行 × 17 列**）')
    R.append('- 额外 1 家：**Entegron / LONGLINE**（`146-…`）—— 它只在 '
             '`06-competitors/110` 第 20 行与原始名单 #44，**不在 111 管线里**。')
    R.append('')
    R.append('---')
    R.append('')
    R.append('## 一、怎么读（三件事）')
    R.append('')
    R.append('1. **每个文件固定七段**：身份卡 → 我方核实的交换机产品线 → '
             '当前供应链 → 联系人（逐字）→ 证据与核实等级 → 建议动作 → 备注。')
    R.append('2. **21 家有「附：完整研究档案」**（文件里带 📚 标记）：'
             '把 `08-followup-dossiers-2026-11-01/` 里的**八段档案 + '
             'r42 核验补录 + r43 商业深挖全文逐字并入**，所以这 21 个文件是'
             '**自包含**的，不用来回跳。')
    R.append('3. **没有合并任何记录**：111 里同一家公司在两批名单里各出现一次'
             '（如 `Makros A.Ş.` = #26 与 #81、`Telemobil` = #46 与 #80、'
             '`HAFYA` = #25 与 #82），**各自独立成文件**，文件顶部用 ⚠ 标出'
             '「疑与 #NNN 同一家」，**要不要合并由人判断**（共 %d 组，见第五节）。'
             % len(dup_pairs))
    R.append('')
    R.append('## 二、诚实边界（必读）')
    R.append('')
    R.append('| 事项 | 实情 |')
    R.append('|---|---|')
    R.append('| 覆盖范围 | **111 的 145 行全覆盖**。你给的两批原始名单'
             '（`Turkey Client List.xlsx` 299 行 + `2025土耳其ISAF客户.xlsx` 98 家）'
             '**已经折进这 145 行**（见 `112-user-customer-lists-deepdive-2026-10-25.md`），'
             '所以这里不是「299+98=397 家」，而是**去重后的 145 家管线**。 |')
    R.append('| 深度差异 | **21 家有深度档案**（八段 + 核验 + 深挖）；'
             '其余 124 家只有管线表的字段（公司/城市/品牌/供应链/联系人/证据/建议动作）。'
             '**不要把 124 家当成「已调研」，它们只是「有档案」。** |')
    R.append('| 联系人来源 | 「联系人」**全部来自用户侧**（展会/微信/名单），'
             '`证据来源` 列才是我方独立抓取的内容。**对外沟通前先分清这两类。** |')
    R.append('| 报价 | 表里所有报价都是**历史口径**，含 DDP/关税的一律要重算。 |')
    R.append('| 第三方数据 | 规模/营收等若来自 Datanyze / ZoomInfo / RocketReach / Volza，'
             '均为**第三方推算**，非财报（详见各家深度档案）。 |')
    R.append('')
    R.append('## 三、索引（按 111 序号）')
    R.append('')
    R.append('| # | 客户 | 城市 | 层级 | 评分 | 深度档案 | 文件 |')
    R.append('|---|---|---|---|---|---|---|')
    for no, company, city, tier, score, deep, fname in index_rows:
        R.append('| %s | %s | %s | %s | %s | %s | [%s](%s) |'
                 % (no, strip_md(company, 42), strip_md(city, 26),
                    strip_md(tier, 22), strip_md(score), deep, fname, fname))
    R.append('')
    R.append('## 四、从哪儿开始（建议顺序）')
    R.append('')
    R.append('1. **A 级 + 有深度档案的 6 家**：#4 Cenova、#9 Öncü、#7 Karer、'
             '#56 Optima、#80 Telemobil、#58 Okisan —— 有产品空档、有联系人、有打法。')
    R.append('2. **订单级/窗口级 3 家**：#91 Sami（500 台）、#92 Selim（换源窗口）、'
             '#84 ONSIS（回头要样品）—— **只能靠人推进，爬虫无效**。')
    R.append('3. **B/C 级 124 家**：先扫 `建议动作` 列，只挑「有具体项目/有自有品牌」的动，'
             '其余作为备选池。')
    R.append('')
    R.append('## 五、重复对（%d 组，两批名单各录一次）' % len(dup_pairs))
    R.append('')
    R.append('> 这里**只做提示，不做合并**。给客户发信前请先确认是同一条线还是两家不同公司。')
    R.append('')
    R.append('| # | 公司 | ↔ | # | 公司 |')
    R.append('|---|---|---|---|---|')
    by_no = {r['序号']: r for r in rows}
    for a, b in dup_pairs:
        R.append('| %s | %s | ↔ | %s | %s |'
                 % (a, strip_md(by_no[a]['公司'], 46), b,
                    strip_md(by_no[b]['公司'], 46)))
    R.append('')
    R.append('## 六、相关目录')
    R.append('')
    R.append('- 深度档案原件：`ingest/angora-1__arena-01a0ce39__5acb613/'
             '08-followup-dossiers-2026-11-01/`（21 份，**仍是 r41–r43 的原始出处**）')
    R.append('- 结构化管线（唯一权威）：`…/08-customer-pipeline/'
             '111-turkey-customer-pipeline.csv`')
    R.append('- 竞对地图（98 家）：`…/06-competitors/110-turkey-local-competitors.csv`')
    R.append('- 生成脚本：`…/08-customer-pipeline/build_tr_customers_r44.py`')
    R.append('')
    io.open(os.path.join(OUT_DIR, 'README.md'), 'w', encoding='utf-8').write('\n'.join(R))

    print('written:', written, 'files; index rows:', len(index_rows))


if __name__ == '__main__':
    main()
