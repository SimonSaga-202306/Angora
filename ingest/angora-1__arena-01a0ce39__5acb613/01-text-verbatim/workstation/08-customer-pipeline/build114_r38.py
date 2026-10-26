# -*- coding: utf-8 -*-
# r38 构建：114 号土耳其客户总档（单 XLSX 多 sheet）
# 来源全部为仓内既有底稿（111 CSV / 110 CSV / 99-raw TSV+JSON / 112 MD 结构化）
# 用法: cd workstation/08-customer-pipeline && python3 build114_r38.py
import csv, json, io, re, unicodedata
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

BASE = '/home/user/Angora'
OUT = f'{BASE}/workstation/08-customer-pipeline/114-turkey-customer-all-in-one-2026-10-25.xlsx'

# ---------- 读取源 ----------
def rd_csv(p):
    return list(csv.reader(open(p, encoding='utf-8-sig', newline='')))
r111 = rd_csv(f'{BASE}/workstation/08-customer-pipeline/111-turkey-customer-pipeline.csv')
assert len(r111) == 146 and all(len(r) == 17 for r in r111)
r110 = rd_csv(f'{BASE}/workstation/06-competitors/110-turkey-local-competitors.csv')
assert len(r110) == 99 and all(len(r) == 20 for r in r110)
r98 = json.load(open(f'{BASE}/workstation/99-raw/r37-isaf-union.json', encoding='utf-8'))
assert len(r98) == 98
master = rd_csv(f'{BASE}/workstation/99-raw/r37-ai-kehu-eval-master.tsv') if False else \
    list(csv.reader(open(f'{BASE}/workstation/99-raw/r37-ai-kehu-eval-master.tsv', encoding='utf-8-sig'), delimiter='\t'))
assert len(master) == 301, len(master)         # 表头 + 300（51-300 空模板）
tcl = list(csv.reader(open(f'{BASE}/workstation/99-raw/r37-turkey-client-list-299.tsv', encoding='utf-8-sig'), delimiter='\t'))
assert len(tcl) == 300, len(tcl)               # 表头 + 299

# ---------- 工具 ----------
TR_MAP = str.maketrans('çğıöşüÇĞİÖŞÜ', 'cgiosuCGIOSU')
def norm(s):
    s = (s or '').lower().translate(TR_MAP)
    s = re.sub(r'[^a-z0-9&]', '', s)
    return s

def style_sheet(ws, widths, n_data_rows):
    hdr_fill = PatternFill('solid', fgColor='1F4E78')
    for c in range(1, ws.max_column + 1):
        cell = ws.cell(row=1, column=c)
        cell.font = Font(bold=True, color='FFFFFF')
        cell.fill = hdr_fill
        cell.alignment = Alignment(vertical='center', wrap_text=False)
        ws.column_dimensions[get_column_letter(c)].width = widths[c - 1] if c - 1 < len(widths) else 24
    ws.freeze_panes = 'A2'
    if n_data_rows > 0:
        ws.auto_filter.ref = f'A1:{get_column_letter(ws.max_column)}{n_data_rows + 1}'

wb = openpyxl.Workbook()

# ---------- Sheet 1: README 说明 ----------
ws = wb.active
ws.title = 'README说明'
readme = [
    ['土耳其客户总档（统一整理，单文件多 sheet）'],
    ['生成', '2026-10-25 第 38 轮 · build114_r38.py（只读视图；权威底稿 = 111/110 三件套 + 99-raw r37 逐字件，只增不删）'],
    ['来源', '① origin/main AI客户评估_TR 10.06.xlsx（master No.1-50 双 AI 评估）② origin/main Turkey Client List.xlsx（299 行原始名单）③ origin/main 2025土耳其ISAF客户.xlsx（ISAF 2025 展会现场接待，去重 98）④ 111 管线（r19-r37 累计 145 行）⑤ 110 竞对/供应地图（98 行）⑥ 112 号跟进推荐主档'],
    ['Sheet 索引', '跟进推荐112（55 行：Tier1 20 / Tier2 12 / Tier3 21 / 战略留档 2）｜全管线111（145 行×17 列）｜ISAF2025（98 条=TR 新增 66 家 76 条〔10 家跨 sheet 重复×2〕+在库 2+TR 已分析 3〔Karaal×2 r20 未入库+CESS=Shnrise 在库行 37〕+非土 14 条/13 家+特殊 3〔equinix 不跟进/Maipu 竞情/Vatankhah Tiandy 员工〕）｜用户双评估50（50 行+库映射）｜TCL原始299（299 行+映射状态）｜110竞对地图（98 行×20 列）'],
    ['口径 1', 'Tier1=立即跟进（双 A/暖线/现场明确项目）；Tier2=暖渠道（面见/老板级/授权分销）；Tier3=监控（红灯黄灯绑定或规模小）；战略留档=非客户（集团线）'],
    ['口径 2', '只看土耳其（r22 常设）：ISAF 非土 13 条只留档不入场；eu.equinix.com 不跟进（r22）'],
    ['口径 3', '111 行 56-79 的 24 家 = r19「排除 24 家」同一批，用户 10.06 双评估 = 重新定级（r12 只增不删，r19 留痕保留）'],
    ['口径 4', '111 行 80-145 = ISAF 2025 展会现场记录（A 级 12 + A- 8 + B/C 46）；r21「16 无法核实」ISAF 线索的现场补全'],
    ['口径 5', 'bypass 产品线专项 8 条明确需求（IHM/Aycan CAM/BİLGEN/ONSIS/Netmax/ORAL/Serkan/SFP Turkey）→ 下轮 bypass 专刊+样品策略（STC-424DGGPM 系）'],
    ['口径 6', '110 竞对地图含 Netaş 等「竞对兼客户」边界实体（曾购我方 3 台样品），列「与Angora关系」可查'],
]
for row in readme:
    ws.append(row)
ws.column_dimensions['A'].width = 12
ws.column_dimensions['B'].width = 150
ws['A1'].font = Font(bold=True, size=14)
for r in range(2, len(readme) + 1):
    ws.cell(row=r, column=1).font = Font(bold=True)
    ws.cell(row=r, column=2).alignment = Alignment(wrap_text=True, vertical='top')

# ---------- Sheet 2: 跟进推荐 112（55 行结构化） ----------
ws = wb.create_sheet('跟进推荐112')
ws.append(['优先级', '客户', '管线行', '双评(AI/CL)', '核心钩子(verified)', '我方打法', '产品线/需求', '联系人(本轮新得/核验)'])
TIER1 = [
    ['Tier1 立即', 'NovaCom', '111 #2', '40A/30B', '31 SKU 自有 NVC/NCV/ND PoE 线在售，NCV-HIF2421GBL-C 2026-01 上新=持续采购中；评估明示「正积极寻找工业 switch 供应商」', '工业线切入（商业线已有源）：工业 PoE 完整线+OEM，报价对 E-wind/新桥', '工业 PoE 8/16 口+ERPS', '库内既有'],
    ['Tier1 立即', 'Snexus', '111 #3', '35A/50A', 'Wix 站新宣称 L3 硬件路由 RIP/OSPF/BGP（r19 时仅 L2 品牌）=产品线升级中；自有 logo 商业+工业 switch', 'L2+→L3 升级配套：L2+ PoE 完整 model list+L3 方案（CENTEC 补 L3）+OEM 全套（logo/UI/包装）', '商业 PoE 8/16/24+L2+/L3', '90 53340 48364（TCL 新得）+info@snexus.com.tr'],
    ['Tier1 立即', 'OPAX', '111 #20', '30A/40A', 'OPAX-08120W=8+2 口 120W $35/1,750TL 2 年保（HRUI 贴牌同源型）=OEM 成熟、价格锚已知', '替换+升级：同价段多型号（100M→GbE）+GB 系列+OEM 全套；2 年保口径对齐', '商业 PoE 8/16/24（100M+GbE）+工业 PoE', 'opax.com 站联'],
    ['Tier1 立即', 'CryptoLink', '111 #5', '35A/35B', '自有 CRL 系全列（CRLISW-08/14P 工业+24 口 L3 10G+CRL-MC02+SFP-10G-LC）+KGYS 警队项目现场在用实证（VLAN/IGMP/traffic shaping）', '工业 L3 升级：L3 10G 核心方案（STH 系/Marvell NPB 带）+ERPS+工业 PoE 补型号；KGYS 口径（公安联网）', '工业 L3 10G+工业 PoE+SFP', '+90 312 557 64 00（本轮新得）/info@cryptolink.com.tr'],
    ['Tier1 立即', 'Telkolink+GelecekBT（同集团）', '111 #1', '38A/35B', '双入口：Telkolink=三旺/TG-NET/CLR 多源+贴自有 logo（外观一般=品质升级空间）；GelecekBT=HRUI 工业 switch', '双品牌替换：商业 PoE（对 CLR/TG-NET）+工业 PoE（对 HRUI/三旺）+OEM 全套；model list 覆盖+管理界面定制', '商业 PoE+工业 PoE+ERPS', 'info@telkolink.com'],
    ['Tier1 立即', 'Entegron / LONGLINE', '110 #20', '30A/45A', '⭐双品牌同一母公司（LONGLINE 2000 起 Bayrampaşa）：Entegron 线=Ethernet 11/PoE 31/EPON ONU 9/GPON ONU 6；兴趣=PON switch+PoE+商业（有 E-wind）', '双入口报价：LONGLINE 渠道（对 E-wind）+Entegron OEM（PoE 31 型替换/扩型）+PON 邻接留档', '商业/工业 PoE+L2 managed 8-28 口', 'info@entegronnetwork.com'],
    ['Tier1 立即', 'Cenova', '111 #4', '30A/40A', '自有 CCTV 品牌+在售 E-wind PoE/工业 switch 实页（dl-end3308pfg）；CCTV 为主营', 'E-wind 替换：CCTV 场景 PoE（IGMP Snooping+PoE++ 长距）+OEM 贴 Cenova', '商业 PoE 8/16/24+CCTV 专用', 'info@cenova.com.tr'],
    ['Tier1 ISAF', 'Telemobil（tbi.com.tr）', '111 #80', '—', '现场记录「可重点跟进，有具体项目」—2光2电 PoE 询价+问交期（现场展示 2光4电 PoE）', '发价格+交期', '2光2电 PoE（具体项目）', '0533 419 16 16（savas@3s.com.tr 关联展会）'],
    ['Tier1 ISAF', 'Makros A.Ş. / DEMIREL', '111 #81', '—', '130/150USD 已报，要 DDP 双清包税', 'DDP 双清包税报价跟进', '工业交换机（工程用）', 'ISAF 现场（Evelyn）'],
    ['Tier1 ISAF', 'HAFYA', '111 #82', '—', '⭐军项目+防水 4光8电 PoE+grundig-security.tr 双域名（与 111 行 8 Hane=Grundig 分销生态待核）', '军项目防水工业 PoE 报价+Grundig 生态关系核验', '工业 4光8电 PoE 网管（防水）', 'grundig-security.tr'],
    ['Tier1 ISAF', 'SFP Turkey', '111 #83', '—', 'Evelyn 既有客户，修图级深度服务+10G 光+bypass', '持续深度服务+bypass 样品', '万兆光/2光2电/2光4电+bypass', 'sfpturkey.com.tr'],
    ['Tier1 ISAF', 'ONSIS ELEKTRONIK', '111 #84', '—', '2光8 PoE 网管 bypass 105USD，要样品', '寄样+bypass 方案（STC-424DGGPM 系）', '2光8 PoE 网管 bypass（要 L2）', 'ISAF 现场'],
    ['Tier1 ISAF', 'Netmax（Ugur Simsek）', '111 #85', '—', '2光8 PoE 带管理 bypass 120USD', '价格跟进+bypass 方案', '2光8 PoE 带管理 bypass', 'ISAF 现场'],
    ['Tier1 ISAF', 'bilimsat（Muharrem KILIC）', '111 #86', '—', '8光8电 PoE 110USD，「最近在找这种产品」', '8光8电 PoE 方案', '8光8电 PoE 网管', 'ISAF 现场（Ady）'],
    ['Tier1 ISAF', 'UGUR IMRE', '111 #87', '—', '分销商（不需要 OEM），2光8 瑞昱 PoE+内置 DC48V 70USD，回「Not bad」', '分销价格表+DC48V 口径', '2光8 瑞昱 PoE 网管+DC48V', 'ISAF 现场'],
    ['Tier1 ISAF', 'ORAL GUVENLIK', '111 #88', '—', '150/90USD 已报，嫌贵', '替代档/折扣', '工业 PoE 网管+bypass（12光12电/2光8电两档）', 'oralcompanies.com'],
    ['Tier1 ISAF', 'DE secure', '111 #89', '—', '工业 8 口 30W，要含 20% 关税报价', 'all-in 报价（含 20% 关税）', '工业 8 口 PoE 30W', 'desecuretechnology.com'],
    ['Tier1 ISAF', 'cansis（Ahmet CAN）', '111 #90', '—', '12光12电 PoE 150USD', '12光12电 PoE 方案', '12光12电 PoE 带网管', 'ISAF 现场'],
    ['Tier1 ISAF', 'Sami CEUIK', '111 #91', '—', '⭐政府项目，500 台量 2光8 PoE 已报 80-90USD（r21 头号信号坐实）', '催单（500 台）+交期确认', '2光8 PoE 网管（500 台量）', 'ISAF 现场（Ady）'],
    ['Tier1 ISAF ★最高优先', 'Selim Kalaka（供应商侧线）', '111 #92', '—', '⭐郑州供应商拟在土耳其开厂→找新供应商=换源窗口（r21 信号坐实）', '换源报价+样品+工厂参观安排', '工业 switch（找新供应商）', 'ISAF 现场/微信'],
]
TIER2 = [
    ['Tier2 暖渠道', 'Optima / Optima Engineering', '111 #56', '28A/5C', '⭐IFSEC 2023 面见+计划来深圳采购+曾受邀参观（最暖线）；物理安防制造商（安卡拉 Sincan 厂+Perpa 销售办）=LPR/停车/闸机场景 PoE 需求', '厂访接待+LPR 场景 PoE 方案（8 口 120W 带+长距）+OEM「Optima」贴牌', '8 口 120W 带+长距 PoE', 'Furkan Kalkan 技术经理 90507 463 05 66 / furkan@optima.tc；Perpa 办 +90 212 210 70 00'],
    ['Tier2 暖渠道', 'Filiz Güvenlik', '111 #57', '22B/5C', '⭐迪拜展面见+25 年（1994 伊兹密尔）+51-200 人+土首批 7/24 报警监控中心（自有监控中心=switch 采购主体）', 'CCTV 场景 PoE+报警中心汇聚；用已有关系推进', '商业 PoE（CCTV 场景）', 'Sadik Yildiz（Ali 员工）M90533 74 63788；+90 232 441 71 74 / info@filizguvenlik.com.tr'],
    ['Tier2 暖渠道', 'Okisan', '111 #58', '18B/20C', '⭐Tiandy+Dahua 土耳其授权分销商（dahuasecurity 分销商页实证）+5,000+ 经销网络+$8.6M+1986 起；商业 PoE 现用丰润达（深圳）', '丰润达替换/第二供应商：商业 PoE 完整线（绑定其 Dahua/Tiandy 摄像头出货）+OEM', '商业 PoE 完整线', '444 1 309 / (0212) 320 28 20 / okisan@okisan.com（Okisan Plaza Şişli）'],
    ['Tier2 暖渠道', 'Karer Güvenlik', '111 #7', '18B/40A', '自有 KARER 品牌 PoE Switch 4/8/16/24 口（深圳 OEM，自组 NVR）=品牌方直接', 'KARER OEM 全套（logo/UI/包装）+NVR 配套 PoE；老板直联', 'PoE 4/8/16/24+NVR 配套', 'Nurbaki Karatas（老板）/ info@karerguvenlik.com'],
    ['Tier2 暖渠道', 'CCTV Depo', '111 #21', '15B/25B', '2004 起 51-200 人「土首个 B2B 安防平台」（Perpa）+2025 自有品牌 SECUZI（CES 展）+IASF 2025 面见', 'SECUZI 品牌 PoE OEM（新品牌=无固定源）+B2B 批发价', '商业 PoE（SECUZI OEM）', 'Can Gurcan CTO / Asuman Ozuedogru（IASF 面见）/ can@cctvdepo.com'],
    ['Tier2 ISAF', 'HCS', '111 #93', '—', '问 L2/L3', 'L2/L3 方案+价格', '商业 PoE（L2/L3 询问）', 'hescs.com'],
    ['Tier2 ISAF', 'KLASNET', '111 #94', '—', '问怎么成为分销商', '分销商招募（价格梯度+政策）', 'MC switch / patch cord', 'ISAF 现场'],
    ['Tier2 ISAF', 'F.A.S.T', '111 #95', '—', '工业 5 口+PLC/IO 代理', '工业 5 口 PoE+PLC/IO 配套', '工业 5 口 PoE', 'fasttr.com'],
    ['Tier2 ISAF', 'voltec', '111 #96', '—', '工业 PoE 网管', '工业 PoE 网管方案', '工业 PoE 网管', 'voltechelektronik.com'],
    ['Tier2 ISAF', 'LABOR Mühendislik（Ramazan DAS）', '111 #97', '—', '要价格表', '价格表+工业 PoE', '工业 PoE', 'ISAF 现场'],
    ['Tier2 ISAF', 'MEPA Elektronik', '111 #98', '—', '4/8/16/24 口全线=产品线级需求', '产品线级报价（全口数）', 'PoE 4/8/16/24 口', 'ISAF 现场'],
    ['Tier2 ISAF', 'viva bilgisayar（ismet Yavuz 老板）', '111 #99', '—', 'Hatay 老板直联', '老板直联+工业 switch', '工业交换机', 'ISAF 现场'],
]
TIER3 = [
    ['Tier3 监控', 'MFD', '111 #61', '15B/8C', 'Siemens SCALANCE 红灯深度绑定', '**不跟进**（红灯）', '—', '—'],
    ['Tier3 监控', 'Bimel', '111 #76', '15B/15C', 'Planet+Ruijie 黄灯+Cisco 红灯；安卡拉 1984；工业页 DPTEK（搜索副产物）', '仅 DPTEK 工业类目缝隙，低成本推送', '工业 PoE（缝隙）', 'Goenuel Ilbeyli'],
    ['Tier3 监控', 'Areskom', '111 #63', '15B/20C', '代理台湾 CTS（黄灯）多品牌', '监控', '多品牌', '—'],
    ['Tier3 监控', 'Teamon', '111 #65', '15B/15C', '多品牌（Planet 台湾黄灯为主）', '监控', '多品牌', '—'],
    ['Tier3 监控', 'İntenet', '111 #64', '18B/15C', '工业网络方案，代理 Raisecom（中国黄灯）', '监控', '工业网络', 'Ercan Ozturk GM-Owner'],
    ['Tier3 监控', 'Dacel Solutions', '111 #77', '15B/8C', '工业自动化（PLC/WECON），switch 极边缘', '监控（自动化边缘）', '自动化边缘', 'Erkan Cirit 股东'],
    ['Tier3 监控', 'Fiberden', '111 #78', '15B/10C', '光纤 MC/光缆/SFP 为主，switch 无明确痕迹', '监控（光纤边缘）', '光纤 MC/SFP', '—'],
    ['Tier3 监控', 'BaburTech', '111 #71', '18B/5C', 'switch 含海思（中国品牌），安卡拉 IT 零售', '监控（海思零售）', '多品牌零售', '—'],
    ['Tier3 监控', 'TekmarShop', '111 #70', '15B/5C', '电商多品牌商业 PoE（=Asya Telekom 系/TEKMAR）', '监控（多品牌电商）', '商业 PoE', '—'],
    ['Tier3 监控', 'İnovatech', '111 #66', '18B/5C', '安防/光纤/网络，IP CCTV 专区', '监控（CCTV 服务）', 'CCTV 场景', '—'],
    ['Tier3 监控', 'Kiracı=ZKR Kıraç 集团', '111 #73', '15B/5C', '澳视摄像头+天地伟业认知；跳转 zkr.com.tr=Kıraç 集团（与 111 #10 ErETE 同集团）', '按 Kıraç 集团统一接触（战略留档线）', '集团安防', '—'],
    ['Tier3 监控', 'RadioTeknoloji', '111 #74', '12B/未确认', 'IASF 2022 展接触（页面无法验证主营）', '监控（老线）', '—', 'Salih Yildirim PM'],
    ['Tier3 监控', 'Egemenelektronik', '111 #68', '20B/10C', 'CCTV 为主+商业 PoE；WhatsApp 已添加=低成本推 PoE 款', '低成本推送', '商业 PoE', '两老板 Belkiz/Levent（WhatsApp）'],
    ['Tier3 监控', 'Metcom', '111 #67', '18B/20B', 'PoE/CCTV 配件/机架/工业 MC 品类广小单', '监控（小单）', '配件品类', '—'],
    ['Tier3 绿灯', 'GMT Control', '111 #60', '15B/15C', '工控分销，Uotek（深圳）贴自有 logo=绿灯替换窗口', '绿灯供应商替换窗口', '工业 switch（Uotek 贴牌）', 'Abdullah Aydin PM'],
    ['Tier3 绿灯', 'Cebeci Grup', '111 #62', '25B/20C', '在售 ONV 工业 switch+串口设备，「有国内的」=绿灯', '绿灯替换窗口', 'ONV 工业 switch', '—'],
    ['Tier3 绿灯', 'TeknolojiPazar', '111 #69', '28A/10C', 'Freelink（疑自有品牌）+HRUI 商业 PoE（伊兹密尔）', '绿灯（Freelink 疑自有）', '商业 PoE', '—'],
    ['Tier3 绿灯', 'LeMax', '111 #72', '22A/10C', '自有品牌（LG 前缀）PoE 源自新桥（绿灯），有 OEM 经验', 'OEM 经验=绿灯替换窗口', '自有 PoE 线', '—'],
    ['Tier3 绿灯', 'Öncü Güvenlik', '111 #9', '35A/30B', '丰润达+Utepo 双绿灯工业/PoE/CCTV（既有档案）', '绿灯替换（既有档案跟进）', '工业 PoE/CCTV', '既有档案'],
    ['Tier3 绿灯', 'Hane Elektronik', '111 #8', '25A/35B', 'Milesight（中国绿灯）土耳其唯一授权分销商（2025 新增 Grundig Security+Panasonic）', '绿灯（Milesight 授权线，注意其渠道身份）', '商业 PoE 多外壳', 'info@haneelektronik.com'],
    ['Tier3 监控', 'EuroCam', '111 #79', '15B/核心业务未确认', 'IASF 2021 面见 Gokhan DEMİR CEO；CL 建议人工介入（无法确认核心业务）', '先核主体再定级', '待核', 'Gokhan DEMİR CEO / info@eurocamguvenlik.com.tr'],
]
STRAT = [
    ['战略留档（非客户）', 'PavoTek', '111 #59 / 110 #1', '32A/8C', '⭐=Pavo Group 电子/嵌入式子公司（导航全链 pavo-group.com+同批新闻流）：军通网络/avionics/电源/IoT；=PNetworks 母集团', '110 行 1（PNetworks 母集团）监控线扩展，非跟进客户', '集团监控', 'Gizem KIZILTAN（TCL #5）'],
    ['战略留档（非客户）', 'Kıraç 集团（ZKR）双入口', '111 #10 ErETE + #73 Kiracı', '28A/5C', '两行均跳转 zkr.com.tr=土耳其大型安防集团 ZKR', '按 Kıraç 集团统一接触', '集团安防', '—'],
]
for r in TIER1 + TIER2 + TIER3 + STRAT:
    ws.append(r)
n_rec = len(TIER1) + len(TIER2) + len(TIER3) + len(STRAT)
assert n_rec == 55, n_rec
assert len(TIER1) == 20 and len(TIER2) == 12 and len(TIER3) == 21 and len(STRAT) == 2
style_sheet(ws, [16, 30, 18, 12, 60, 45, 28, 46], n_rec)

# ---------- Sheet 3: 全管线 111（145 行×17 列，原样） ----------
ws = wb.create_sheet('全管线111(145)')
for r in r111:
    ws.append(r)
style_sheet(ws, [6, 8, 26, 22, 18, 30, 28, 16, 20, 10, 12, 12, 10, 30, 30, 12, 60], 145)

# ---------- Sheet 4: ISAF 2025（98 行） ----------
ws = wb.create_sheet('ISAF2025(98)')
ws.append(['No.(原表)', 'Sheet', '重复来源', '国家', '现场接待(dup)', '原始文本(mid)', 'web', 'email', '手机', 'interest(原列)', '处理状态'])

# 111 行 80-145 公司名（关键词匹配用）
row_co = {i + 80: r111[i + 79][2] for i in range(66)}
KW = {
    80: ['telemobil'], 81: ['makros'], 82: ['hafya'], 83: ['sfpturkey', 'sfpturkeycomtr'],
    84: ['onsis'], 85: ['netmax'], 86: ['bilimsat'], 87: ['ugurimre'],
    88: ['oralcompanies', 'oralguvenlik'], 89: ['desecure'], 90: ['cansis'],
    91: ['ceuik', 'samicelik'], 92: ['kalaka'], 93: ['hcs', 'hescs'], 94: ['klasnet'],
    95: ['fasttr', 'fast'], 96: ['voltec'], 97: ['labor'], 98: ['mepa'], 99: ['viva'],
    100: ['proves'], 101: ['necdet'], 102: ['fiberix'], 103: ['acusense'], 104: ['duzgun'],
    105: ['ihm'], 106: ['sinerjik'], 107: ['marbim', 'ecevit'], 108: ['dimas'],
    109: ['basaran'], 110: ['fadi'], 111: ['goktork'], 112: ['d&n', 'dnelektrik', 'dnElektrik'.lower()],
    113: ['fourline'], 114: ['aycan', 'agbilgisayar'], 115: ['3scomtr'],
    116: ['fhguvenlik', 'goller'], 117: ['bilgen'], 118: ['aniltelekom', 'anil'],
    119: ['btm'], 120: ['ebatek'], 121: ['turkuaz'], 122: ['gungor'], 123: ['sedat'],
    124: ['interland'], 125: ['smali'], 126: ['nazemco'], 127: ['serkan'], 128: ['fatih'],
    129: ['celali'], 130: ['905437802223'], 131: ['tet529'], 132: ['ertan'],
    133: ['karaslan', 'enestalha'], 134: ['gokhan'], 135: ['nortel'], 136: ['zeytek'],
    137: ['bilge'], 138: ['pelikan'], 139: ['interpos'], 140: ['camsan'], 141: ['teknokta'],
    142: ['foline'], 143: ['holil'], 144: ['marmaris'], 145: ['hiperonline'],
}
TIER_OF = {**{i: 'A' for i in range(80, 92)}, **{i: 'A-' for i in range(92, 100)}, **{i: 'B/C' for i in range(100, 146)}}

def isaf_status(e):
    t = ' '.join([e.get('mid', ''), e.get('web', ''), e.get('email', ''), e.get('mobile', ''), e.get('interest', '')])
    nt = norm(t)
    if 'equinix' in nt:
        return '不跟进（r22 用户裁定）'
    if 'maipu' in nt:
        return '竞情（中国参展商，ONV 80USD 对位价情）'
    if 'vatankhah' in nt:
        return 'Tiandy 员工（关联 111 行 58 Okisan 渠道线，留档）'
    if 'novacom' in nt:
        return '在库 → 111 行 2（ISAF 面见备注已加）'
    if 'snexus' in nt:
        return '在库 → 111 行 3（ISAF 面见备注已加）'
    if 'shnrise' in nt or 'govalik' in nt or 'sahinozturk' in nt:
        return '在库 → 111 行 37（CESS Govalik=Shnrise，r20 已录，现场口误记录）'
    NTC = [('predrag', '塞尔维亚'), ('stasanet', '塞尔维亚'), ('miroslav', '塞尔维亚'),
           ('todorov', '保加利亚'), ('ezzarrough', '利比亚'), ('arcanlibya', '利比亚'),
           ('piperis', '希腊'), ('ghodayyah', '巴勒斯坦'), ('goit', '巴勒斯坦'),
           ('fetury', '黎巴嫩/利比亚'), ('alhossan', '黎巴嫩/利比亚'), ('kdaizim', '利比亚'),
           ('alamthal', '利比亚'), ('megatrade', '乌克兰'), ('shvetsov', '乌克兰'),
           ('amz', '突尼斯'), ('stormict', '科索沃'), ('beqiri', '科索沃'),
           ('0770', '叙利亚'), ('zahed', '伊朗'), ('netpardazco', '伊朗')]
    for kw, ctry in NTC:
        if kw in nt:
            return f'非土留档（r21 只留档，{ctry}）'
    country = (e.get('country') or '').strip()
    if country and country.lower() != 'turkey':
        return f'非土留档（r21 只留档，{country}）'
    if 'karaal' in nt:
        return '土耳其已分析（r20：仅手机+WhatsApp ❌无法核实，未入库）→ 本轮留档，90 543 908 36 06 要工业级 Price List（可再核实升级）'
    for rowno, kws in KW.items():
        for kw in kws:
            if kw in nt:
                return rowno  # 命中 111 行号（待二遍拼状态）
    return '既库/已分析（r20/r21）→ 见 111 行 1-79 / 99-raw 对应行'

first_pass = [(i, isaf_status(e)) for i, e in enumerate(r98)]
row_hits = {}
for i, st in first_pass:
    if isinstance(st, int):
        row_hits.setdefault(st, []).append(i)
missing = [r for r in range(80, 146) if r not in row_hits]
over = {r: len(v) for r, v in row_hits.items() if len(v) > 2}
assert not missing and not over, ('missing', missing, 'over', over)
x2 = {r: [r98[i].get('no', '?') for i in idx] for r, idx in row_hits.items() if len(idx) > 1}
assert len(x2) == 10 and sum(len(v) for v in x2.values()) == 20, x2  # 跨 sheet 同人 10 行×2
# 状态拼装（第二遍）
for i, e in enumerate(r98):
    st = first_pass[i][1]
    if isinstance(st, int):
        if st in x2:
            nos = '、'.join(n for n in x2[st])
            st = f'TR 新增 → 111 行 {st}（{row_co[st][:20]}…）· {TIER_OF[st]}〔×2 条〔跨 sheet 重复记录：No.{nos}〕〕'
        else:
            st = f'TR 新增 → 111 行 {st}（{row_co[st][:20]}…）· {TIER_OF[st]}'
    n_row = re.match(r'TR 新增 → 111 行 (\d+)', st or '')
    ws.append([e.get('no', ''), e.get('sheet', ''), '、'.join(e.get('dup', [])), e.get('country', ''),
               '、'.join(e.get('dup', [])), e.get('mid', ''), e.get('web', ''), e.get('email', ''),
               e.get('mobile', ''), e.get('interest', ''), st])
n_tr_new = sum(1 for i, e in enumerate(r98) if isinstance(first_pass[i][1], int))
assert n_tr_new == 76, n_tr_new   # 66 行新客 = 56 单条 + 10 行跨 sheet 同人×2（20 条）
style_sheet(ws, [10, 10, 14, 10, 14, 70, 22, 26, 16, 24, 40], 98)

# ---------- Sheet 5: 用户双评估 50 ----------
ws = wb.create_sheet('用户双评估50')
M = {1: '111 #18', 2: '新 111 #57', 3: '111 #3', 4: '新 111 #60', 5: '110 #1 关联 / 新 111 #59（战略留档）',
     6: '111 #4', 7: '111 #5', 8: '新 111 #61', 9: '111 #11', 10: '111 #1', 11: '新 111 #56',
     12: '111 #22', 13: '新 111 #62', 14: '111 #16', 15: '111 #19', 16: '新 111 #58', 17: '111 #14',
     18: '111 #17', 19: '新 111 #63', 20: '新 111 #64', 21: '新 111 #65', 22: '新 111 #66', 23: '111 #1',
     24: '111 #9', 25: '新 111 #67', 26: '新 111 #68', 27: '新 111 #69', 28: '新 111 #70', 29: '111 #11',
     30: '111 #10', 31: '111 #6', 32: '新 111 #73', 33: '111 #15', 34: '111 #12', 35: '新 111 #71',
     36: '111 #2', 37: '新 111 #72', 38: '111 #23', 39: '111 #20', 40: '新 111 #75', 41: '111 #8',
     42: '111 #13', 43: '新 111 #74', 44: '110 #20（=LONGLINE 自有 OEM）', 45: '111 #7', 46: '新 111 #76',
     47: '新 111 #77', 48: '新 111 #78', 49: '111 #21', 50: '新 111 #79'}
hdr = ['No.', '公司(域)', 'AI评估结果', 'CALUDE评估结果', 'Country', 'Person', 'From(渠道)', 'Interested in', 'Contact', 'Remark', '库映射(111/110 行)', '跟进层级']
TIER_OF_M = {1: 'Tier3', 2: 'Tier2', 3: 'Tier1', 4: 'Tier3', 5: '战略留档', 6: 'Tier1', 7: 'Tier1',
             8: 'Tier3 不跟', 9: 'Tier3', 10: 'Tier1', 11: 'Tier2', 12: 'Tier3', 13: 'Tier3', 14: 'Tier3',
             15: 'Tier3', 16: 'Tier2', 17: 'Tier3', 18: 'Tier3', 19: 'Tier3', 20: 'Tier3', 21: 'Tier3',
             22: 'Tier3', 23: 'Tier1', 24: 'Tier3 绿灯', 25: 'Tier3', 26: 'Tier3', 27: 'Tier3', 28: 'Tier3',
             29: 'Tier3', 30: 'Tier3', 31: 'Tier3', 32: 'Tier3 集团', 33: 'Tier3', 34: 'Tier3', 35: 'Tier3',
             36: 'Tier1', 37: 'Tier3 绿灯', 38: 'Tier3', 39: 'Tier1', 40: 'Tier3', 41: 'Tier3 绿灯',
             42: 'Tier3', 43: 'Tier3', 44: 'Tier1', 45: 'Tier2', 46: 'Tier3', 47: 'Tier3', 48: 'Tier3',
             49: 'Tier2', 50: 'Tier3'}
ws.append(hdr)
for r in master[1:51]:
    r = (r + [''] * 10)[:10]
    no = int(r[0])
    ws.append([r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], M[no], TIER_OF_M[no]])
style_sheet(ws, [6, 30, 55, 40, 8, 18, 12, 20, 26, 30, 30, 12], 50)

# ---------- Sheet 6: TCL 原始 299 ----------
ws = wb.create_sheet('TCL原始299')
# 111/110 域集合
def domains(rows, col=2):
    ds = set()
    for r in rows:
        for m in re.findall(r'[a-z0-9.-]+\.(?:com|net|org|tr|io)[a-z]?', (r[col] or '').lower().translate(TR_MAP) if col < len(r) else ''):
            ds.add(m)
    return ds
d111 = domains(r111[1:])
d110 = domains(r110[1:])
hdr = ['No.', 'Person', 'Interested in', 'Contact', 'Remark', '公司(域)', '映射状态']
ws.append(hdr)
n_mapped = 0
for r in tcl[1:]:
    r = (r + [''] * 6)[:6]
    dom = re.findall(r'[a-z0-9-]+\.[a-z]{2,}(?:/[a-z0-9./-]*)?', (r[5] or '').lower().translate(TR_MAP))
    hit = ''
    for d in dom:
        dd = d.split('/')[0]
        if dd in d111 or any(dd == x or dd.endswith('.' + x) or x.endswith('.' + dd) for x in d111):
            hit = '在库 → 见 111 全管线（域匹配）'; n_mapped += 1; break
        if dd in d110 or any(dd == x or dd.endswith('.' + x) or x.endswith('.' + dd) for x in d110):
            hit = '在库 → 见 110 竞对地图（域匹配）'; n_mapped += 1; break
    if not hit:
        no = int(r[0])
        if no == 5:
            hit = '⭐110 #1 关联 / 111 #59（PavoTek=Pavo 子公司，战略留档）'; n_mapped += 1
        elif no == 60:
            hit = '⭐110 #20（Entegron=LONGLINE 自有 CN OEM）'; n_mapped += 1
        else:
            hit = '未评估（249 批次池，后续轮次）'
    ws.append([r[0], r[1], r[2], r[3], r[4], r[5], hit])
style_sheet(ws, [6, 20, 24, 28, 24, 46, 40], 299)

# ---------- Sheet 7: 110 竞对地图（98 行×20 列，原样） ----------
ws = wb.create_sheet('110竞对地图(98)')
for r in r110:
    ws.append(r)
style_sheet(ws, [6, 8, 18, 24, 8, 24, 10, 20, 26, 30, 20, 30, 16, 30, 14, 30, 34, 40, 12, 60], 98)

wb.save(OUT)

# ---------- 回读校验 ----------
wb2 = openpyxl.load_workbook(OUT)
names = wb2.sheetnames
assert names == ['README说明', '跟进推荐112', '全管线111(145)', 'ISAF2025(98)', '用户双评估50', 'TCL原始299', '110竞对地图(98)'], names
for nm, rows_expect in [('跟进推荐112', 55), ('全管线111(145)', 145), ('ISAF2025(98)', 98), ('用户双评估50', 50), ('TCL原始299', 299), ('110竞对地图(98)', 98)]:
    w2 = wb2[nm]
    assert w2.max_row == rows_expect + 1, (nm, w2.max_row)
    assert w2.max_column >= 2
print('114 XLSX OK: 7 sheets / 跟进推荐 55 / 管线 145 / ISAF 98 / 双评估 50 / TCL 299 / 110 98')
print('TCL 域匹配在库:', n_mapped)
