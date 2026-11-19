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
    R69 = {}
    R70 = {}
    R71 = {}
    R72 = {}
    R73 = {}
    R74 = {}
    R75 = {}
    R76 = {}
    R77 = {}
    R78 = {}
    R79 = {}
    R80 = {}
    R81 = {}
    R82 = {}
    R83 = {}
    R84 = {}
    R85 = {}
    R86 = {}
    R87 = {}
    R88 = {}
    R89 = {}
    R90 = {}
    R91 = {}
    R92 = {}
    for _m in ('r48_appendix_data', 'r49_appendix_data', 'r50_appendix_data', 'r51_appendix_data', 'r52_appendix_data', 'r53_appendix_data', 'r54_appendix_data', 'r55_appendix_data', 'r56_appendix_data', 'r57_appendix_data', 'r58_appendix_data', 'r59_appendix_data', 'r60_appendix_data', 'r61_appendix_data', 'r62_appendix_data', 'r63_appendix_data', 'r64_appendix_data', 'r65_appendix_data', 'r66_appendix_data', 'r67_appendix_data', 'r68_appendix_data', 'r69_appendix_data', 'r70_appendix_data', 'r71_appendix_data', 'r72_appendix_data', 'r73_appendix_data', 'r74_appendix_data', 'r75_appendix_data', 'r76_appendix_data', 'r77_appendix_data', 'r78_appendix_data', 'r79_appendix_data', 'r80_appendix_data', 'r81_appendix_data', 'r82_appendix_data', 'r83_appendix_data', 'r84_appendix_data', 'r85_appendix_data', 'r86_appendix_data', 'r87_appendix_data', 'r88_appendix_data', 'r89_appendix_data', 'r90_appendix_data', 'r91_appendix_data', 'r92_appendix_data'):
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
            if _m == 'r69_appendix_data':
                R69.update(_mod.D)
            if _m == 'r70_appendix_data':
                R70.update(_mod.D)
            if _m == 'r71_appendix_data':
                R71.update(_mod.D)
            if _m == 'r72_appendix_data':
                R72.update(_mod.D)
            if _m == 'r73_appendix_data':
                R73.update(_mod.D)
            if _m == 'r74_appendix_data':
                R74.update(_mod.D)
            if _m == 'r75_appendix_data':
                R75.update(_mod.D)
            if _m == 'r76_appendix_data':
                R76.update(_mod.D)
            if _m == 'r77_appendix_data':
                R77.update(_mod.D)
            if _m == 'r78_appendix_data':
                R78.update(_mod.D)
            if _m == 'r79_appendix_data':
                R79.update(_mod.D)
            if _m == 'r80_appendix_data':
                R80.update(_mod.D)
            if _m == 'r81_appendix_data':
                R81.update(_mod.D)
            if _m == 'r82_appendix_data':
                R82.update(_mod.D)
            if _m == 'r83_appendix_data':
                R83.update(_mod.D)
            if _m == 'r84_appendix_data':
                R84.update(_mod.D)
            if _m == 'r85_appendix_data':
                R85.update(_mod.D)
            if _m == 'r86_appendix_data':
                R86.update(_mod.D)
            if _m == 'r87_appendix_data':
                R87.update(_mod.D)
            if _m == 'r88_appendix_data':
                R88.update(_mod.D)
            if _m == 'r89_appendix_data':
                R89.update(_mod.D)
            if _m == 'r90_appendix_data':
                R90.update(_mod.D)
            if _m == 'r91_appendix_data':
                R91.update(_mod.D)
            if _m == 'r92_appendix_data':
                R92.update(_mod.D)
    # r88：避免同一 key 同时被 r48 通用块与 r88 标记块重复输出
    for _k in list(R48.keys()):
        if _k in R88 or _k in R89 or _k in R90 or _k in R91 or _k in R92:
            R48.pop(_k)
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
R69_MARK = '## 附：r69 $412 是僵尸合同 + DMO 比零售贵 1.7 倍（2026-11-06）'
R70_MARK = '## 附：r70 8 口是血海 + 24 口两个口径（2026-11-06）'
R71_MARK = '## 附：r71 24 口地板 $278 / 渠道 $403（2026-11-06）'
R72_MARK = '## 附：r72 客户身份档案（法人 / 税号 / 人 / 代理品牌）'
R73_MARK = '## 附：r73 B 级客户身份卡（法名 / 税号 / 代理 / 自有品牌）'
R74_MARK = '## 附：r74 供货线拆解（Koptek / Portel / CCS / TeleOne）'
R75_MARK = '## 附：r75 白牌层与身份订正（OEM 池 / Perpa B K:8 / İzmir 路线）'
R76_MARK = '## 附：r76 DMO 价格地图（供应商 K 码 / 型号 / 单价 / 合同）'
R77_MARK = '## 附：r77 串价修正与 FS Grup 主体（详情页可信价）'
R78_MARK = '## 附：r78 离岸品牌模板与身份卡（RUBISEC / Birkil / 四家客户）'
R79_MARK = '## 附：r79 工商级身份（VKN/MERSİS）与工业货架空位'
R80_MARK = '## 附：r80 定价双轨与电力段代理地图'
R81_MARK = '## 附：r81 三条新线索落地与 RUBISEC 认证缺口'
R82_MARK = '## 附：r82 KGYS「C 型边缘交换机」市场与五家新渠道'
R83_MARK = '## 附：r83 Ewind 全渠道与 Angora 复爬对照（2026-11-17）'
R84_MARK = '## 附：r84 2026-04 KGYS/ÇGKS 招标解剖与我方逐条合规矩阵（2026-11-17）'
R85_MARK = '## 附：r85 LINK Bilgisayar 全档案与 Angora 五条交换机线（2026-11-17）'
R86_MARK = '## 附：r86 EGM 现场交换机单价与六家 KGYS 交换机包中标商（2026-11-17）'
R87_MARK = '## 附：r87 2026「仅限本国投标人」结构与 ÇŞB 单价册天花板（2026-11-17）'
R88_MARK = '## 附：r88 TTK 交换机规格书是 D-Link 指纹与 Angora 的四条差距（2026-10-26）'
R89_MARK = '## 附：r89 Angora 持有 EGM KGYS 合格证书与 TTK 全单适配（2026-10-26）'
R90_MARK = '## 附：r90 能源渠道（EDAŞ/EÜAŞ/İSU）—— 唯一能查到交换机真实成交价的公共采购市场（2026-10-26）'
R91_MARK = '## 附：r91 公共标的技术壁垒不在参数、在生态（锁死条款）与公示地图 v2（2026-10-26）'
R92_MARK = '## 附：r92 投标资格是可审计的 —— Kamu Bilişim Yetki Belgesi（STB01）全解（2026-10-26）'


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
        body_r69 = R69.get(no)
        if body_r69:
            L.append('---')
            L.append('')
            L.append(R69_MARK)
            L.append('')
            L.append('> 本节为 **r69（2026-11-06）**；**它把上一节的 $412 判为僵尸价，并首次证明 DMO 价比零售高 —— 报价前必读。**')
            L.append('')
            L.append(body_r69.strip('\n'))
            L.append('')
        body_r70 = R70.get(no)
        if body_r70:
            L.append('---')
            L.append('')
            L.append(R70_MARK)
            L.append('')
            L.append('> 本节为 **r70（2026-11-06）**；**它推翻了「8 口我方有优势」，并把 24 口拆成「市价」与「渠道」两个口径 —— 报价前必读。**')
            L.append('')
            L.append(body_r70.strip('\n'))
            L.append('')
        body_r71 = R71.get(no)
        if body_r71:
            L.append('---')
            L.append('')
            L.append(R71_MARK)
            L.append('')
            L.append('> 本节为 **r71（2026-11-06）**；**地板再降两格，且 24 口 L3 470 W 只要 $240 —— 报价前必读。**')
            L.append('')
            L.append(body_r71.strip('\n'))
            L.append('')
        body_r72 = R72.get(no)
        if body_r72:
            L.append('---')
            L.append('')
            L.append(R72_MARK)
            L.append('')
            L.append('> 本节为 **r72（2026-11-06）**：**工商身份与联系人档案 —— 打电话前先读这一节。**')
            L.append('')
            L.append(body_r72.strip('\n'))
            L.append('')
        body_r73 = R73.get(no)
        if body_r73:
            L.append('---')
            L.append('')
            L.append(R73_MARK)
            L.append('')
            L.append('> 本节为 **r73（2026-11-06）**：**B 级客户工商档案 —— 打电话前先读这一节。**')
            L.append('')
            L.append(body_r73.strip('\n'))
            L.append('')
        body_r74 = R74.get(no)
        if body_r74:
            L.append('---')
            L.append('')
            L.append(R74_MARK)
            L.append('')
            L.append('> 本节为 **r74（2026-11-06）**：**它现在卖谁的东西 —— 决定我们该说什么话。**')
            L.append('')
            L.append(body_r74.strip('\n'))
            L.append('')
        body_r75 = R75.get(no)
        if body_r75:
            L.append('---')
            L.append('')
            L.append(R75_MARK)
            L.append('')
            L.append('> 本节为 **r75（2026-11-06）**：**身份订正 + 白牌层（OEM）视角。**')
            L.append('')
            L.append(body_r75.strip('\n'))
            L.append('')
        body_r76 = R76.get(no)
        if body_r76:
            L.append('---')
            L.append('')
            L.append(R76_MARK)
            L.append('')
            L.append('> 本节为 **r76（2026-11-06）**：**它在政府渠道（DMO）卖什么、卖多少钱、合同还有效吗。**')
            L.append('')
            L.append(body_r76.strip('\n'))
            L.append('')
        body_r77 = R77.get(no)
        if body_r77:
            L.append('---')
            L.append('')
            L.append(R77_MARK)
            L.append('')
            L.append('> 本节为 **r77（2026-11-06）**：**只引用 DMO 详情页价格；它在政府渠道到底由谁挂单。**')
            L.append('')
            L.append(body_r77.strip('\n'))
            L.append('')
        body_r78 = R78.get(no)
        if body_r78:
            L.append('---')
            L.append('')
            L.append(R78_MARK)
            L.append('')
            L.append('> 本节为 **r78（2026-11-06）**：**身份卡到「可以打电话」的密度；以及「挂牌价 ÷2.3–3.0 = 成交价」这条纪律。**')
            L.append('')
            L.append(body_r78.strip('\n'))
            L.append('')
        body_r79 = R79.get(no)
        if body_r79:
            L.append('---')
            L.append('')
            L.append(R79_MARK)
            L.append('')
            L.append('> 本节为 **r79（2026-11-06）**：**它的税号/地址/关键人；以及「挂牌 ÷2.95 = 成交」这条被实价验证的规则。**')
            L.append('')
            L.append(body_r79.strip('\n'))
            L.append('')
        body_r80 = R80.get(no)
        if body_r80:
            L.append('---')
            L.append('')
            L.append(R80_MARK)
            L.append('')
            L.append('> 本节为 **r80（2026-11-06）**：**「挂牌 ÷2.95」什么时候成立、什么时候不成立；以及电力段（IEC 61850-3）的代理地图。**')
            L.append('')
            L.append(body_r80.strip('\n'))
            L.append('')
        body_r81 = R81.get(no)
        if body_r81:
            L.append('---')
            L.append('')
            L.append(R81_MARK)
            L.append('')
            L.append('> 本节为 **r81（2026-11-06）**：**三条新线索（İNFOGEN / İSAC / RİVO）的完整档案；以及「RUBISEC 没有 IEC 61850-3」这一条硬结论。**')
            L.append('')
            L.append(body_r81.strip('\n'))
            L.append('')
        body_r82 = R82.get(no)
        if body_r82:
            L.append('---')
            L.append('')
            L.append(R82_MARK)
            L.append('')
            L.append('> 本节为 **r82（2026-11-06）**：**KGYS 是 8 口工业 PoE 的全国性市场，门票是 EGM 一张测试报告；五家新渠道线索（Teslakom / Proline / Areskom / GGS / Netmon）落地。**')
            L.append('')
            L.append(body_r82.strip('\n'))
            L.append('')
        body_r83 = R83.get(no)
        if body_r83:
            L.append('---')
            L.append('')
            L.append(R83_MARK)
            L.append('')
            L.append('> 本节为 **r83（2026-11-17）**：**Ewind 官网连续第 3 轮零新增，但 Alibaba 店铺、FOB 价格与渠道结构全变了；以及对自家语料的回头核对，推翻了 r82「EGM 证书是唯一硬门槛、我方没有」的判断。**')
            L.append('')
            L.append(body_r83.strip('\n'))
            L.append('')
        body_r84 = R84.get(no)
        if body_r84:
            L.append('---')
            L.append('')
            L.append(R84_MARK)
            L.append('')
            L.append('> 本节为 **r84（2026-11-17 晚）**：**把「3,294 台」拆成五包招标、把两份规格书逐条对我方机型、并把三条价格线（D-Link $135 全包 / 我方 855 RMB / 工厂 780 RMB）摆在同一张表上。** 三条判断修正 r83。')
            L.append('')
            L.append(body_r84.strip('\n'))
            L.append('')
        body_r85 = R85.get(no)
        if body_r85:
            L.append('---')
            L.append('')
            L.append(R85_MARK)
            L.append('')
            L.append('> 本节为 **r85（2026-11-17）**：**把 LINK Bilgisayar 挖到能打电话的程度（BIST 上市公司、三个月三个 EGM 单、自己没有交换机产品线），补上 Angora 从未记录的 SYNAPSE 五型号，并把 r84 的「外置 shaping 盒子」方案证伪。** 两条修正：C-Tipi 后门已关闭、56 Gbps 陷阱要看光口。')
            L.append('')
            L.append(body_r85.strip('\n'))
            L.append('')
        body_r86 = R86.get(no)
        if body_r86:
            L.append('---')
            L.append('')
            L.append(R86_MARK)
            L.append('')
            L.append('> 本节为 **r86（2026-11-17 深夜）**：**一份 KAP 披露把「政府为一颗 8 口现场机付多少钱」钉死（6,050 TL ≈ $152，LINK 一年交 3,000 台）；并把过去两年 KGYS「交换机包」的六家中标集成商全部具名。** 三条修正：SFP 利润池要分标、LINK 定级升 A、Volza 47 票 = 45 进 + 2 出。')
            L.append('')
            L.append(body_r86.strip('\n'))
            L.append('')
        body_r87 = R87.get(no)
        if body_r87:
            L.append('---')
            L.append('')
            L.append(R87_MARK)
            L.append('')
            L.append('> 本节为 **r87（2026-11-17）**：**把「土耳其 2026 交换机采购到底允许谁投标」查成法条 —— 8 单全部「仅限本国投标人 + 本国货 15%」，白牌只能挂在持 YMB 的土耳其法人身上；同时用 ÇŞB 弱电单价册把 8/16/24/48 口 PoE 的工程口径天花板钉死（20,036 / 30,846 / 40,415 / 94,936 TL），并与 r86 的集采 6,050 TL 形成 3.3 倍落差。** 修正：Angora「81 省渠道」不可公开核实。')
            L.append('')
            L.append(body_r87.strip('\n'))
            L.append('')
        body_r88 = R88.get(no)
        if body_r88:
            L.append('---')
            L.append('')
            L.append(R88_MARK)
            L.append('')
            L.append('> 本节为 **r88（2026-10-26）**：**把 TTK 两轮交换机标的技术规格书逐条拆到数据表级 —— 95.23 Mpps / MTBF 760,000 h / −10~50 ℃ / 4 kV 全部指向 D-Link DGS-F1500-28XS，2.3 指向 F1500-52MP，而 2.2 用的是上一代 DGS-1510 的 95.24 与 768 ACL。** 三条修正：`Tamamlandı` 不等于成交（该页标题即"历史/已取消"）、「同品牌 SFP」不是 2026 新增、24×SFP 骨干不是缺口（全国通用桩号 `KTB-ELK.17.008`）。并且：**Angora 已有 `ANW-5713-24S8T6X`，只差 ACL 768 / jumbo 12K / 路由 124-50 / OAM 四条数据表条款。**')
            L.append('')
            L.append(body_r88.strip('\n'))
            L.append('')
        body_r89 = R89.get(no)
        if body_r89:
            L.append('---')
            L.append('')
            L.append(R89_MARK)
            L.append('')
            L.append('> 本节为 **r89（2026-10-26）**：**Angora 官网显示它早在 2019 年就通过了 EGM 的 KGYS「交通整形 + 丢包」合格测试并取得参与证书 —— 第五家持票方，长期口径「只有 Extreme/Allied/Cryptolink/D-Link 四家」作废。** 同时：**VERGE 官方数据表（ACL 512 / jumbo 9,216 / MTBF 328,650 h / 0~50 ℃ / 24G 71.3 Mpps）证明 TTK 的 `MTBF ≥760,000 h` 是"排除本地低价机"的筛子**；**而 Synapse 的铜口机 ANW-2712-24T4X（128 G / 99 Mpps）与 48T6X（216 G / 162 Mpps）纸面可过 TTK 2.2 / 2.3 ⇒ 推翻 r88 的「只能投 2 台」与「一张标拆两半」。** 另：**Yerli Malı 法规明文排除「境外零件 + 境内简单组装」⇒ r87 的 SKD 建议作废**；**DMO 新增两个判例（贸易部 Omurga/Kenar → Trio 2025-12-09；财政部 50 台 → Elit Arge 2022-12-14，均无金额）**。')
            L.append('')
            L.append(body_r89.strip('\n'))
            L.append('')
        body_r90 = R90.get(no)
        if body_r90:
            L.append('---')
            L.append('')
            L.append(R90_MARK)
            L.append('')
            L.append('> 本节为 **r90（2026-10-26）**：**换轴到能源渠道 —— 土耳其 21 家 EDAŞ / EÜAŞ / 水务公司不走 EKAP、以美元计价、并把中标方与金额贴在自家官网。** 三条判例：**İSU 2025/944195（100 台工业 Tip1 + 9 台 PoE Tip2 + 2 台骨干，约成本 ₺30,081,000，Turkcell ₺29,446,000，Türk Telekom ₺27,995,000 中标，仅 2 家投标，15% 本地优惠没救 Turkcell）**；**AYEDAŞ 2025 防火墙+交换机 材料 $109,000.02 + 人工 ₺1,280,000.19 → ULTRON BİLİŞİM**（GDZ 11-18 截标的同型标，预算锚 $120k–165k）；**EÜAŞ 2026/1545558 十一座水/火电站 ICS 网络打包（götürü、有 eksiltme、交付 150 天、需 ICS 分段/隔离履历 ≥20%）**。单位经济：**İSU 反推单台 $3,400–4,100（8/24 口加权 $1,800–2,600），是我方 FOB 的 9–17 倍** ⇒ **对手是运营商与 OT 集成商，不是本地品牌；Angora 缺的是项目履历，不是产品。**')
            L.append('')
            L.append(body_r90.strip('\n'))
            L.append('')
        body_r91 = R91.get(no)
        if body_r91:
            L.append('---')
            L.append('')
            L.append(R91_MARK)
            L.append('')
            L.append('> 本节为 **r91（2026-10-26）**：**r89 把参数对完、r90 拿到成交价，本轮回答"参数全过为什么还是进不去" —— 因为墙是生态。** 范本是 **ETİ MADEN 技术规格书（44 台交换机 + 28 AP + 6,400 条跳线）**：**全部交换机必须同一品牌 + 必须列入 `Forescout 8.2` 兼容矩阵 + 光模块必须原厂（OEM 不接受）+ 无线须兼容现网 `Huawei AC6605` + 有线须被 `Huawei E-Sight` 纳管 + 48 口须能与 `Huawei S5735-S48P4X` 堆叠** ⇒ **这不是买 44 台交换机，这是买华为**。⇒ **修正 r89 的 SFP 结论**：出现"原厂光模块"条款时，SFP 只能做**隐形 ODM**（Angora 出标签/质保），不能直接卖。⇒ **TTK 中标方第四次不可查并给出机制**：**取消标不产生结果公告 ⇒ 应记为"不存在"而非"未获得"**。⇒ **渠道公示地图 v2**：Enerjisa 系网页表 + **UEDAŞ 一标一 PDF（含中标方与美元金额）** + OEDAŞ 编号页 + **TaahhütHaber 每日公报（专设 BOTAŞ/TPAO-ETİ MADEN-TKİ-TTK 组）**。⇒ **唯一不需换供应商就能解的生态门槛：`Forescout 8.2` 矩阵**。')
            L.append('')
            L.append(body_r91.strip('\n'))
            L.append('')
        body_r92 = R92.get(no)
        if body_r92:
            L.append('---')
            L.append('')
            L.append(R92_MARK)
            L.append('')
            L.append('> 本节为 **r92（2026-10-26）**：**把 r91 的第三层门槛（投标人层）拆到底 —— 那张证叫 `Kamu Bilişim Yetki Belgesi`（`STB01-####`），由 Sanayi ve Teknoloji Bakanlığı / Milli Teknoloji Genel Müdürlüğü 依 29.06.2022/31881 号 Yönetmelik 电子签发。** 门槛低得出奇：**MADDE 5(1)(a) 只要一份覆盖「至少一类 bilişim hizmet」的 TÜRKAK 抬头 `TS EN ISO/IEC 27001`** —— 不要业绩、不要资本、不要 62443、不要 CMMI（后两者只属 Yazılım / Sızma 证）；**≤2 个月审结**；**有效期 = 所交材料中最早到期者之日**（7 张实测 **197–355 天，无一张 3 年** ⇒ 二手「3 年」说法作废）。**但它是 e-Devlet + 土耳其税号专属 ⇒ 境外主体结构上不可得。** **KİK 的强制条款 `89/A`（2023-09-29 生效）只管 bilişim hizmet 标（含 doğrudan temin 与 4734 豁免），对 mal alımı 无强制** —— 而 2026 年已有 6 张货物标把它写进 `4.3.2`（含 Çankırı `2026/1967649`）⇒ **r91 的歧义答案是「KİK 未扩、采购人普遍自行扩用」：法律上可争议，事实上是硬墙。** **⭐ 唯一合法窗口：`Hizmet Alımı İhaleleri Uygulama Yönetmeliği 16.6.4` —— 采购人漏写的法定文件，评标阶段不得再索取、不得补交。** **⭐ 名单侧：Angora / Ultron / Trio / Cyberwise / GelecekBT / Snexus / Nokta / LINK 八家全部「未公示」**（对照组 10 家有公示）⇒ **r91 的「Angora = 投标资格壳」降级为未证实，壳更可能在持证集成商身上**；**最干净通道是货物标：我们卖裸机 → 持证集成商去投**（货物标分包不受 `89/A.5` 约束）。**核验**：`kamubilisim.sanayi.gov.tr/belgedogrulama`（按编号；⚠ 本沙箱不可达，界面未实证）。**⚠ 发证机关未随 2026-10-31 部委改组而变**（新设的是管部委自身基建的 Bilgi Teknolojileri GM，不是 Milli Teknoloji GM）。')
            L.append('')
            L.append(body_r92.strip('\n'))
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
