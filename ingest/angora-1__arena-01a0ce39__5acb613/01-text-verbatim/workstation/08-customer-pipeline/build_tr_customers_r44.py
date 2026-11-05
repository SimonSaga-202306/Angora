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
TIERS = ('A', 'B', 'C')

# r46 · B 档深挖数据（b_deepdig_data_1.py / _2.py）。缺失则跳过，不影响 A/C 生成。
B_DEEPDIG = {}
A_DEEPDIG = {}
try:
    import importlib.util as _ilu
    for _m in ('a_deepdig_data_1',):
        _p = os.path.join(os.path.dirname(os.path.abspath(__file__)), _m + '.py')
        if os.path.exists(_p):
            _spec = _ilu.spec_from_file_location(_m, _p)
            _mod = _ilu.module_from_spec(_spec)
            _spec.loader.exec_module(_mod)
            A_DEEPDIG.update(_mod.D)
    R48 = {}
    R49 = {}
    R50 = {}
    R51 = {}
    R52 = {}
    R53 = {}
    R54 = {}
    R55 = {}
    R56 = {}
    R57 = {}
    R58 = {}
    R59 = {}
    R60 = {}
    R61 = {}
    R62 = {}
    R63 = {}
    R64 = {}
    R65 = {}
    R66 = {}
    R67 = {}
    R68 = {}
    for _m in ('r48_appendix_data', 'r49_appendix_data', 'r50_appendix_data', 'r51_appendix_data', 'r52_appendix_data', 'r53_appendix_data', 'r54_appendix_data', 'r55_appendix_data', 'r56_appendix_data', 'r57_appendix_data', 'r58_appendix_data', 'r59_appendix_data', 'r60_appendix_data', 'r61_appendix_data', 'r62_appendix_data', 'r63_appendix_data', 'r64_appendix_data', 'r65_appendix_data', 'r66_appendix_data', 'r67_appendix_data', 'r68_appendix_data'):
        _p = os.path.join(os.path.dirname(os.path.abspath(__file__)), _m + '.py')
        if os.path.exists(_p):
            _spec = _ilu.spec_from_file_location(_m, _p)
            _mod = _ilu.module_from_spec(_spec)
            _spec.loader.exec_module(_mod)
            R48.update(_mod.D)
            if _m == 'r49_appendix_data':
                R49.update(_mod.D)
            if _m == 'r50_appendix_data':
                R50.update(_mod.D)
            if _m == 'r51_appendix_data':
                R51.update(_mod.D)
            if _m == 'r52_appendix_data':
                R52.update(_mod.D)
            if _m == 'r53_appendix_data':
                R53.update(_mod.D)
            if _m == 'r54_appendix_data':
                R54.update(_mod.D)
            if _m == 'r55_appendix_data':
                R55.update(_mod.D)
            if _m == 'r56_appendix_data':
                R56.update(_mod.D)
            if _m == 'r57_appendix_data':
                R57.update(_mod.D)
            if _m == 'r58_appendix_data':
                R58.update(_mod.D)
            if _m == 'r59_appendix_data':
                R59.update(_mod.D)
            if _m == 'r60_appendix_data':
                R60.update(_mod.D)
            if _m == 'r61_appendix_data':
                R61.update(_mod.D)
            if _m == 'r62_appendix_data':
                R62.update(_mod.D)
            if _m == 'r63_appendix_data':
                R63.update(_mod.D)
            if _m == 'r64_appendix_data':
                R64.update(_mod.D)
            if _m == 'r65_appendix_data':
                R65.update(_mod.D)
            if _m == 'r66_appendix_data':
                R66.update(_mod.D)
            if _m == 'r67_appendix_data':
                R67.update(_mod.D)
            if _m == 'r68_appendix_data':
                R68.update(_mod.D)
    for _m in ('b_deepdig_data_1', 'b_deepdig_data_2'):
        _p = os.path.join(os.path.dirname(os.path.abspath(__file__)), _m + '.py')
        if os.path.exists(_p):
            _spec = _ilu.spec_from_file_location(_m, _p)
            _mod = _ilu.module_from_spec(_spec)
            _spec.loader.exec_module(_mod)
            B_DEEPDIG.update(_mod.D)
except Exception as _e:  # 数据缺失不应阻断主生成
    print('WARN: B deep-dig data not loaded:', _e)
B_MARK = '## 附：B 档深挖（r46 · 2026-11-01）'
A_MARK = '## 附：A 档深挖（r47 · 2026-11-01）'
R48_MARK = '## 附：r48 抓站补录（2026-11-01）'
R49_MARK = '## 附：r49 复查收口（2026-11-01 深夜）'
R50_MARK = '## 附：r50 全量点算与结论回收（2026-11-01）'
R51_MARK = '## 附：r51 自有品牌线型号级对位（2026-11-01）'
R52_MARK = '## 附：r52 全目录点算与品牌归属推翻（2026-11-01）'
R53_MARK = '## 附：r53 规格实锤与目录空位（2026-11-01）'
R54_MARK = '## 附：r54 B 档型号级点算与价格锚点重建（2026-11-01）'
R55_MARK = '## 附：r55 收尾取证与 FOREDGE 反证（2026-11-01）'
R56_MARK = '## 附：r56 关格与落地主体（2026-11-01）'
R57_MARK = '## 附：r57 上游 FOREDGE 的 DMO 挂牌价（2026-11-01）'
R58_MARK = '## 附：r58 交换机 SKU 为零 → ODM 缺口（2026-11-01）'
R59_MARK = '## 附：r59 用真实 FOB 重算 ODM 报价（2026-11-01）'
R60_MARK = '## 附：r60 2.5G 全线（本文不适用）与 24 口一刀换的精确型号（2026-11-01）'
R61_MARK = '## 附：r61 渠道加价链与 8 口 B2B 反证（2026-11-01）'
R62_MARK = '## 附：r62 DMO 工业段与同型号多档报价（2026-11-01）'
R63_MARK = '## 附：r63 8 口真实锚价与 DMO 价格锁定（2026-11-05）'
R64_MARK = '## 附：r64 FX2120 修正与安防货架价（2026-11-05）'
R65_MARK = '## 附：r65 8 倍来自 PoE 而非工业（2026-11-05）'
R66_MARK = '## 附：r66 工业 8 口是平价位（2026-11-06）'
R67_MARK = '## 附：r67 FOREDGE 全价目与 8 口双口径（2026-11-06）'
R68_MARK = '## 附：r68 24 口地板 $412 与 SFP 价差（2026-11-06）'


def tier_letter(level):
    """111 的 `层级` 列取值很杂（A 核心 / A-（ISAF25 新入）/ B+ / B bypass /
    C 不跟进 …），统一按首字母归入 A/B/C 三档；无法判定归 C 并在 README 标注。"""
    t = (level or '').strip().upper()
    for ch in TIERS:
        if t.startswith(ch):
            return ch
    return 'C'

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
    for t in TIERS:
        os.makedirs(os.path.join(OUT_DIR, t), exist_ok=True)

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

        letter = tier_letter(tier)
        body_bd = B_DEEPDIG.get(no)
        if letter == 'B' and body_bd:
            L.append('---')
            L.append('')
            L.append(B_MARK)
            L.append('')
            L.append('> 本节为 **r46（2026-11-01）B 档深挖**新增，来源为公开网络（官网 / 企业登记 / '
                     '展会名录 / BGP / 第三方企业库），逐条标注证据等级；'
                     '**未核实的项一律标为空白，不推测。**')
            L.append('')
            L.append(body_bd.strip('\n'))
            L.append('')
        body_ad = A_DEEPDIG.get(no)
        if letter == 'A' and body_ad:
            L.append('---')
            L.append('')
            L.append(A_MARK)
            L.append('')
            L.append('> 本节为 **r47（2026-11-01）A 档深挖**新增（A/ 里此前**没有完整档案**的档位），'
                     '来源为公开网络（官网 / 企业登记 / 协会名录 / 商标库 / 第三方企业库），'
                     '**未核实的项一律标为空白，不推测。**')
            L.append('')
            L.append(body_ad.strip('\n'))
            L.append('')
        body_r48 = R48.get(no)
        if body_r48:
            L.append('---')
            L.append('')
            L.append(R48_MARK)
            L.append('')
            L.append('> 本节为 **r48（2026-11-01）第二轮抓站**后的**修正与新证据**，'
                     '逐条标注来源；**与前面小节冲突时，以本节为准**（并已在本节内说明改了什么）。')
            L.append('')
            L.append(body_r48.strip('\n'))
            L.append('')
        body_r49 = R49.get(no)
        if body_r49:
            L.append('---')
            L.append('')
            L.append(R49_MARK)
            L.append('')
            L.append('> 本节为 **r49（2026-11-01 深夜）**的**再次复查与收口**；'
                     '**与前面任何小节冲突时，以本节为准**。')
            L.append('')
            L.append(body_r49.strip('\n'))
            L.append('')
        body_r50 = R50.get(no)
        if body_r50:
            L.append('---')
            L.append('')
            L.append(R50_MARK)
            L.append('')
            L.append('> 本节为 **r50（2026-11-01）**的**全量点算**与**对前两节的回收**；'
                     '**冲突时以本节为准**。')
            L.append('')
            L.append(body_r50.strip('\n'))
            L.append('')
        body_r51 = R51.get(no)
        if body_r51:
            L.append('---')
            L.append('')
            L.append(R51_MARK)
            L.append('')
            L.append('> 本节为 **r51（2026-11-01）**对**自有品牌交换机线**的**型号级**取证与对位；'
                     '冲突时以本节为准。')
            L.append('')
            L.append(body_r51.strip('\n'))
            L.append('')
        body_r52 = R52.get(no)
        if body_r52:
            L.append('---')
            L.append('')
            L.append(R52_MARK)
            L.append('')
            L.append('> 本节为 **r52（2026-11-01）** 的**全目录点算**与**品牌归属推翻**；'
                     '**冲突时以本节为准**。')
            L.append('')
            L.append(body_r52.strip('\n'))
            L.append('')
        body_r53 = R53.get(no)
        if body_r53:
            L.append('---')
            L.append('')
            L.append(R53_MARK)
            L.append('')
            L.append('> 本节为 **r53（2026-11-01）** 的规格实锤；**与 r52 冲突时以本节为准**。')
            L.append('')
            L.append(body_r53.strip('\n'))
            L.append('')
        body_r54 = R54.get(no)
        if body_r54:
            L.append('---')
            L.append('')
            L.append(R54_MARK)
            L.append('')
            L.append('> 本节为 **r54（2026-11-01）** 的 B 档型号级点算；USD/TRY 按 **50.02**（2026-11-04）折算。')
            L.append('')
            L.append(body_r54.strip('\n'))
            L.append('')
        body_r55 = R55.get(no)
        if body_r55:
            L.append('---')
            L.append('')
            L.append(R55_MARK)
            L.append('')
            L.append('> 本节为 **r55（2026-11-01）** 的收尾取证；**与前面各轮冲突时以本节为准**。')
            L.append('')
            L.append(body_r55.strip('\n'))
            L.append('')
        body_r56 = R56.get(no)
        if body_r56:
            L.append('---')
            L.append('')
            L.append(R56_MARK)
            L.append('')
            L.append('> 本节为 **r56（2026-11-01）** 的关格结果；**与前面各轮冲突时以本节为准**。')
            L.append('')
            L.append(body_r56.strip('\n'))
            L.append('')
        body_r57 = R57.get(no)
        if body_r57:
            L.append('---')
            L.append('')
            L.append(R57_MARK)
            L.append('')
            L.append('> 本节为 **r57（2026-11-01）** 的公共采购价取证；**与前面各轮冲突时以本节为准**。')
            L.append('')
            L.append(body_r57.strip('\n'))
            L.append('')
        body_r58 = R58.get(no)
        if body_r58:
            L.append('---')
            L.append('')
            L.append(R58_MARK)
            L.append('')
            L.append('> 本节为 **r58（2026-11-01）** 的取证；**与 r53「空目录」的表述冲突，以本节为准**。')
            L.append('')
            L.append(body_r58.strip('\n'))
            L.append('')
        body_r59 = R59.get(no)
        if body_r59:
            L.append('---')
            L.append('')
            L.append(R59_MARK)
            L.append('')
            L.append('> 本节为 **r59（2026-11-01）** 的验算；**与 r57/r58 的价格口径冲突时以本节为准**。')
            L.append('')
            L.append(body_r59.strip('\n'))
            L.append('')
        body_r60 = R60.get(no)
        if body_r60:
            L.append('---')
            L.append('')
            L.append(R60_MARK)
            L.append('')
            L.append('> 本节为 **r60（2026-11-01）** 的补充；**与前面「讲 2.5G / 讲 3–4 倍空间」的表述冲突时以本节为准**。')
            L.append('')
            L.append(body_r60.strip('\n'))
            L.append('')
        body_r61 = R61.get(no)
        if body_r61:
            L.append('---')
            L.append('')
            L.append(R61_MARK)
            L.append('')
            L.append('> 本节为 **r61（2026-11-01）** 的取证；**与前面「零售价为基准」「8 口有 3 倍空间」的表述冲突时以本节为准**。')
            L.append('')
            L.append(body_r61.strip('\n'))
            L.append('')
        body_r62 = R62.get(no)
        if body_r62:
            L.append('---')
            L.append('')
            L.append(R62_MARK)
            L.append('')
            L.append('> 本节为 **r62（2026-11-01）** 的取证；**与「高端无价格优势」的表述冲突时以本节为准（分渠道看待）**。')
            L.append('')
            L.append(body_r62.strip('\n'))
            L.append('')
        body_r63 = R63.get(no)
        if body_r63:
            L.append('---')
            L.append('')
            L.append(R63_MARK)
            L.append('')
            L.append('> 本节为 **r63（2026-11-05）** 的取证；**第 ① 条修正上一节把 $1,292 当「8 口锚」的说法**。')
            L.append('')
            L.append(body_r63.strip('\n'))
            L.append('')
        body_r64 = R64.get(no)
        if body_r64:
            L.append('---')
            L.append('')
            L.append(R64_MARK)
            L.append('')
            L.append('> 本节为 **r64（2026-11-05）**；**第 ① 条推翻本文 r61 节的最低锚，第 ② 条是我方在该渠道唯一还有优势的档位**。')
            L.append('')
            L.append(body_r64.strip('\n'))
            L.append('')
        body_r65 = R65.get(no)
        if body_r65:
            L.append('---')
            L.append('')
            L.append(R65_MARK)
            L.append('')
            L.append('> 本节为 **r65（2026-11-05 夜）**；**它把前面几节反复出现的「工业 8 倍」拆开：8 倍来自 PoE，不来自「工业」二字。讲话术前先读这一节。**')
            L.append('')
            L.append(body_r65.strip('\n'))
            L.append('')
        body_r66 = R66.get(no)
        if body_r66:
            L.append('---')
            L.append('')
            L.append(R66_MARK)
            L.append('')
            L.append('> 本节为 **r66（2026-11-06）**，**它推翻上一节（r65）的核心判断：`PL-IGS-TS82CM` 其实是 PoE+，DMO 只 $162。据此讲话术之前务必先读本节。**')
            L.append('')
            L.append(body_r66.strip('\n'))
            L.append('')
        body_r67 = R67.get(no)
        if body_r67:
            L.append('---')
            L.append('')
            L.append(R67_MARK)
            L.append('')
            L.append('> 本节为 **r67（2026-11-06）**；**它给了 FOREDGE 在 DMO 的全 12 条价目，并把「8 口有没有优势」这个问题按口径拆开 —— 这是与客户对话前必读的一节。**')
            L.append('')
            L.append(body_r67.strip('\n'))
            L.append('')
        body_r68 = R68.get(no)
        if body_r68:
            L.append('---')
            L.append('')
            L.append(R68_MARK)
            L.append('')
            L.append('> 本节为 **r68（2026-11-06）**；**它把前几节的倍率按「净价口径」重算并下调 —— 报价与讲话术前必须读这一节。**')
            L.append('')
            L.append(body_r68.strip('\n'))
            L.append('')
        out = os.path.join(OUT_DIR, letter, fname)
        io.open(out, 'w', encoding='utf-8').write('\n'.join(L))
        written += 1
        index_rows.append((no, company, plain(r['总部/城市']), tier, score,
                           '有' if dossier else '—', letter + '/' + fname, letter))

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
        if R51.get('146'):
            L.append('---')
            L.append('')
            L.append(R51_MARK)
            L.append('')
            L.append('> 本节为 **r51（2026-11-01）**对 **Longline `LNG` 系**的**型号级**取证与对位。')
            L.append('')
            L.append(R51['146'].strip('\n'))
            L.append('')
        io.open(os.path.join(OUT_DIR, 'A', '146-entegron-longline.md'), 'w',
                encoding='utf-8').write('\n'.join(L))
        written += 1
        index_rows.append(('146', 'Entegron ／ LONGLINE（双品牌）', 'İstanbul / Bayrampaşa',
                           'A-（客户侧）', '30A/45A', '有',
                           'A/146-entegron-longline.md', 'A'))

    # ---------- README ----------
    R = []
    R.append('# TR Customers · 土耳其客户总表（一客户一 MD）')
    R.append('')
    R.append('**这个文件夹是什么**：把仓库里**已有的土耳其客户底稿**，'
             '拆成**一家一个 Markdown 文件**，方便逐家看、逐家发、逐家跟。')
    R.append('')
    n = {t: sum(1 for r in index_rows if r[7] == t) for t in TIERS}
    R.append('- 客户数：**%d** —— **A 档 %d · B 档 %d · C 档 %d**' %
             (written, n['A'], n['B'], n['C']))
    R.append('- 组织方式：**A / B / C 三个子文件夹**（`A/` `B/` `C/`，'
             '按 `111` 的 `层级` 列首字母归档），本 README 放在根部')
    R.append('- 文件数：**%d** 个客户 MD + 本 README' % written)
    R.append('- 数据源（唯一权威）：`ingest/angora-1__arena-01a0ce39__5acb613/'
             '01-text-verbatim/workstation/08-customer-pipeline/'
             '111-turkey-customer-pipeline.csv`（**145 行 × 17 列**）')
    R.append('- 额外 1 家：**Entegron / LONGLINE**（`A/146-entegron-longline.md`）—— '
             '它只在 `06-competitors/110` 第 20 行与原始名单 #44，**不在 111 管线里**，'
             '按客户侧评级归入 `A/`。')
    R.append('')
    R.append('---')
    R.append('')
    R.append('## 一、怎么读（四件事）')
    R.append('')
    R.append('1. **每个文件固定七段**：身份卡 → 我方核实的交换机产品线 → '
             '当前供应链 → 联系人（逐字）→ 证据与核实等级 → 建议动作 → 备注。')
    R.append('2. **21 家有「附：完整研究档案」**（文件里带 📚 标记）：'
             '把 `08-followup-dossiers-2026-11-01/` 里的**八段档案 + '
             'r42 核验补录 + r43 商业深挖全文逐字并入**，所以这 21 个文件是'
             '**自包含**的，不用来回跳。')
    R.append('3. **按档分目录**：`A/` 优先跟进、`B/` 常规维护、`C/` 备选池'
             '（标准见第三节）。**想只打重点，就只看 `A/` 这一个文件夹。**')
    R.append('4. **没有合并任何记录**：111 里同一家公司在两批名单里各出现一次'
             '（如 `Makros A.Ş.` = #26 与 #81、`Telemobil` = #46 与 #80、'
             '`HAFYA` = #25 与 #82），**各自独立成文件**，文件顶部用 ⚠ 标出'
             '「疑与 #NNN 同一家」，**要不要合并由人判断**（共 %d 组，见第八节）。'
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
    R.append('## 三、分档标准（A / B / C 是怎么来的）')
    R.append('')
    R.append('**不是我这轮重新打的印象分**——直接沿用 `111` 管线表 `层级` 列的**首字母**，'
             '该列本身是「双 AI 初筛 + 我方人工核实 + 综合评分」的产物'
             '（详见 `112-user-customer-lists-deepdive-2026-10-25.md`）。')
    R.append('')
    R.append('| 档 | 子标签举例 | 家数 | 含义 |')
    R.append('|---|---|---|---|')
    R.append('| **A** | `A 核心` / `A-` / `A 订单级` / `A 军项目` / `A 战略` / '
             '`A 暖线` / `A 大型分销` | %d | 已有接触 + 有明确需求或产品空档；'
             '**本周就该动手**。 |' % n['A'])
    R.append('| **B** | `B+` / `B` / `B-` / `B 暖线` / `B bypass` / `B 防务客户池` '
             '| %d | 有真实业务，但缺一环（价格、DDP、规模、决策链）；'
             '**季度节奏维护**。 |' % n['B'])
    R.append('| **C** | `C` / `C+` / `C 战略留档` / `C 不跟进` / `C 低` | %d | '
             '只到邮箱/电话，或明确不跟进；**只做群发触达与备选**。 |' % n['C'])
    R.append('')
    R.append('> ⚠ 两处需要人判断的地方：① `C 战略留档`（如 PavoTek）与 `C 不跟进`'
             '（如 MFD/Bimel 类）**同放在 `C/`**，但性质完全不同，看文件里的「备注」；'
             '② 同一家公司在两批名单里可能被分到**不同档**（如 #26 是 B+、#81 是 A），'
             '本文件夹**不做合并**，两份各归各档，请自行裁决以哪份为准。')
    R.append('')
    TIER_DESC = {
        'A': ('A 档 · 优先跟进', '核心客户 / 有明确产品空档或订单信号。**先打这一层。**'),
        'B': ('B 档 · 常规跟进', '有真实业务但无强信号，或有单一短板（价格/DDP/规模小）。'
              '**按季度节奏维护，不投定制资源。**'),
        'C': ('C 档 · 备选池', '信息少 / 只到邮箱电话 / 战略留档 / 明确不跟进。'
              '**只做群发触达与备选，不单独投入人力。**'),
    }
    for t in TIERS:
        rows_t = [r for r in index_rows if r[7] == t]
        title, desc = TIER_DESC[t]
        R.append('## %s、索引 · %s（%d 家）'
                 % ({'A': '四', 'B': '五', 'C': '六'}[t], title, len(rows_t)))
        R.append('')
        R.append('> %s' % desc)
        R.append('')
        R.append('| # | 客户 | 城市 | 层级 | 评分 | 深度档案 | 文件 |')
        R.append('|---|---|---|---|---|---|---|')
        for no, company, city, tier, score, deep, path, letter in rows_t:
            R.append('| %s | %s | %s | %s | %s | %s | [%s](%s) |'
                     % (no, strip_md(company, 42), strip_md(city, 26),
                        strip_md(tier, 22), strip_md(score), deep, path, path))
        R.append('')
    R.append('## 七、从哪儿开始（建议顺序）')
    R.append('')
    R.append('1. **A 级 + 有深度档案的 6 家**：#4 Cenova、#9 Öncü、#7 Karer、'
             '#56 Optima、#80 Telemobil、#58 Okisan —— 有产品空档、有联系人、有打法。')
    R.append('2. **订单级/窗口级 3 家**：#91 Sami（500 台）、#92 Selim（换源窗口）、'
             '#84 ONSIS（回头要样品）—— **只能靠人推进，爬虫无效**。')
    R.append('3. **B/C 级 124 家**：先扫 `建议动作` 列，只挑「有具体项目/有自有品牌」的动，'
             '其余作为备选池。')
    R.append('')
    R.append('## 八、重复对（%d 组，两批名单各录一次）' % len(dup_pairs))
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
    R.append('## 九、A/B 档深挖（r46–r47 · 2026-11-01）')
    R.append('')
    R.append('**`B/` 全部 77 家已做一轮公开网络深挖**，每家文件末尾多出一个小节'
             '「附：B 档深挖（r46 · 2026-11-01）」：主体核实 / 它在卖什么 / '
             '与我方的切入点 / 打法 / **证据等级与空白**。')
    R.append('')
    R.append('- 横向汇总：`…/08-customer-pipeline/115-turkey-b-tier-deepdig-2026-11-01.md`'
             '（77 家分五类：**已在卖交换机 11 · 相邻品类 17 · 工程商 22 · '
             '结构错配 10** …）')
    R.append('- ⭐ **最重要的发现**：B 档被低估——**11 家已经在卖交换机**'
             '（`6 Coptek` `14 NFS` `18 iotsistem` `62 Cebeci` `79 Eurocam` `15 Koza` '
             '`19 Lansan` `33 HCS` `10 ErETE` `35 Antalya Turkuaz` `49 Zeytek`），'
             '其中 6 家有**自有/白牌型号**（`S4600` `S5700` `MLB-E4xxx` `SRX-*` `XPS`）→ '
             '可直接谈 **OEM / 二供**。')
    R.append('- ⚠ **结构调整建议（未执行，需人工拍板）**：升 A 12 家；降 C 6 家'
             '（`34 Stasanet` 实为**塞尔维亚**、`28 Hiperonline` 与 `32 Fiberix` 是 **ISP**、'
             '`43 Düzgün` 是**纺织**、`71 Baburtech` 是**笔电维修**、`55 ULAK` 是**国家级设备商**）；'
             '`30 ORAL` 实为 **KKTC**、`45 Alamthal` 实为**利比亚市场**（伊斯坦布尔采购办）。')
    R.append('- **r47 追加：`A/` 里此前没有完整档案的 17 家已逐家深挖**'
             '（文件末尾多出「附：A 档深挖（r47 · 2026-11-01）」）。'
             '**A 档现在 33/33 全部有深度内容**（15 家原有完整档案 + 17 家 r47 新深挖 + 1 家 Entegron 专档）。')
    R.append('- ⭐ **r47 三个高价值发现**：① `A/052` **upTech 是 Nokta Elektronik 的自有品牌**'
             '（商标 2008/13951，**916 SKU**），且它同时代理 **Edge-Core / Ruijie / Planet / ORing**'
             ' → **A 档最优先的 OEM 目标**；② `A/053` **Winet** 把价格印在网站上：'
             '`OEM-8-PORT-GB-POE`（8 口千兆 PoE，7×PoE 24/48V + 1 上联）= **2,916.76 ₺ + KDV**'
             ' → **唯一公开价格锚点**；③ `A/075` **Technopc**（1998，**27,500 m² / 250+ 人**，'
             '**全土第一张国产货证书**，SAHA İstanbul + Ostim Savunma 双会员）→ **最大 OEM 机会**。')
    R.append('- ⭐ **`…/08-customer-pipeline/116-b-a-model-mapping-2026-11-01.md`**：'
             '**11 家 B + 8 家 A 的「型号对位表」**（客户型号 ↔ 我方型号逐行 + 缺口矩阵 + 打法 + 必问三句）。'
             '**这是真正能直接发出去的那份附件。**')
    R.append('- **C 档本轮仍是零投入**（用户明确：C 不跟进、没精力）。')
    R.append('')
    R.append('## 十、相关目录')
    R.append('')
    R.append('- 深度档案原件：`ingest/angora-1__arena-01a0ce39__5acb613/'
             '08-followup-dossiers-2026-11-01/`（21 份，**仍是 r41–r43 的原始出处**）')
    R.append('- 结构化管线（唯一权威）：`…/08-customer-pipeline/'
             '111-turkey-customer-pipeline.csv`')
    R.append('- 竞对地图（98 家）：`…/06-competitors/110-turkey-local-competitors.csv`')
    R.append('- 生成脚本：`…/08-customer-pipeline/build_tr_customers_r44.py`')
    R.append('')
    io.open(os.path.join(OUT_DIR, 'README.md'), 'w', encoding='utf-8').write('\n'.join(R))

    # 清理旧版平铺文件（v1 曾把 MD 直接放在根目录；现改为 A/B/C 分档）
    removed = 0
    for fn in os.listdir(OUT_DIR):
        if fn.endswith('.md') and fn != 'README.md':
            os.remove(os.path.join(OUT_DIR, fn))
            removed += 1

    print('written:', written, 'files; index rows:', len(index_rows),
          '; removed flat leftovers:', removed)


if __name__ == '__main__':
    main()
