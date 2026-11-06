# -*- coding: utf-8 -*-
"""r79 附录数据：客户工商级身份（VKN/MERSİS）+ ÷2.95 规则验证 + 工业货架空位 + Cebeci 名字撞车排雷。"""

D = {}

D['2'] = """
#### r79 补：**身份与定位订正 —— 它的根是「弱电/卫星电视」，不是网络**

| 字段 | 内容 |
|---|---|
| 法定全称 | **NOVA GRUP MÜHENDİSLİK**（安卡拉） |
| **成立** | **2002** |
| **品牌归属** | **NOVACOM 是 Nova Grup Mühendislik 的注册商标**（原文 `novAcom, Nova Grup Mühendislik Firmasının ®Tescilli Markasıdır`） |
| 站点 | `novacom.com.tr` · `nova-grup.com` |
| 品类 | **「Zayıf Akım」（弱电）**：中央天线/卫星电视（SMATV）· CCTV · 楼宇与环境电子系统 · 安防 · 门禁 |
| 三项业务 | 销售营销 · **进出口** · **系统集成** |
| 产品线 | `NV-02/03/04/08`（5–1000 MHz 分配器/放大器）· `NVC-PD 4×1 / PDWP 4×1 / PDM 8×1`（DiSEqC 开关）· NVC-/NCV-/ND- 系列（含 **31 款自有 PoE 交换机**，r72 已录） |

**⇒ 分级由 86 下调到 84**
**理由**：**它的根是弱电与卫星电视**，PoE 交换机是「顺手延伸」，**技术判断力弱于 Nokta/Cenova**。
**⇒ 但反过来是优点**：**网络不是它的主场 ⇒ 它没有既有立场要守 ⇒ SKU 更新意愿最强**。
**⇒ 话术**：「**你现在的 31 款 PoE 全是商用。我不劝你换全部 —— 只加一条工业 8 口，你就能接以前接不了的标。**」
**⚠ 空白**：VKN / MERSİS 仍缺；具体地址只有「安卡拉」。
"""

D['3'] = """
#### r79 补：**真正的主体 = HEMMAH GROUP（MERSİS + VKN 齐了）**

| 字段 | 内容 |
|---|---|
| **法定全称** | **HEMMAH GROUP BİLİŞİM VE MİMARLIK TİCARET LİMİTED ŞİRKETİ** |
| **MERSİS** | **0461092236500001** |
| **VKN（税号）** | **4610922365** |
| 地址 | **Turgut Özal Bulvarı No:2 A6 No:145, Çekmeköy / İstanbul** |
| 邮箱 / 站点 | **`info@hemmahgroup.com`** · `www.hemmah.com.tr` |
| 规模 | **11–50 人** |
| 品牌关系 | **`snexus.com.tr` 域名注册人 = HEMMAH GROUP**；销售合同抬头 = Hemmah → **Snexus 只是品牌壳** |
| 渠道结构 | **经销商页只列 HEMMAH GROUP 一家** ⇒ **品牌方 = 唯一分销商**；且**自己在 Trendyol 与 Allesgo 开店零售/B2B** |
| 产品线（本轮补） | `SN-XGS5300-28F`（24×GbE + 4×10G，**L3**）· `SN-GS1300-27FP`（24×GbE PoE + 2 GbE + 1 SFP）· `SN-ES1300-26FP`（24×100M PoE + 2 GbE + 1 SFP，**300 W**）· `SN-ES1300-10P/6P`（8/4 口 PoE）· `SN-GS1300-6FP`（**4 口 PoE，65 W**）· 8 口千兆 PoE + 4×GbE SFP + 控制台（240 W）· SFP · 媒体转换器 |

**⇒ 三条**
1. **「一人两角」：品牌方 + 唯一分销商** ⇒ **决策链最短**，找 Hemmah 的老板就能定。
2. **它在 Trendyol 开店** ⇒ **库存压力在自己身上** ⇒ **对新供应商的报价敏感度高于 Han / Öncü**。
3. **产品线在「工业」这一格完全空白**（4/8/16/24/48 口全是商用 + 云管理）⇒ **工业 8 口 −40~75 ℃ 是我们唯一的切口，它没有替代方案。**
**⇒ 分级 85 → 87。**
**⚠ 空白**：Hemmah 的员工数（仅 11–50）与营收；老板姓名待查。
"""

D['5'] = """
#### r79 补：**身份卡 —— A 级里「最纯的政府项目商」**

| 字段 | 内容 |
|---|---|
| 法定全称 | **CRYPTOLINK ELEKTRONİK GÜVENLİK SİSTEMLERİ SAN. VE TİC. LTD. ŞTİ.** |
| 地址 | **Çankaya Mah. Bükreş Cad. No:19/1, Çankaya / Ankara** |
| 电话 / 邮箱 | **+90 312 557 64 00** · `info@cryptolink.com.tr` |
| 业务线 | **边境安全（Sınır Güvenliği）· 网络方案 · 网络安全 · 车牌识别（Plaka Tanıma）· 在线培训 · 信号干扰系统（Sinyal Kesici）** |
| 客户性质 | **政府机构为主**（原文 `kamu kurum ve kuruluşları`） |

**⇒ 判读**
它**不靠货架、靠标书**：边境安全 + 车牌识别 + 信号干扰，**全部是招标型业务**。
⇒ **它最需要的不是「便宜」，是「能写进标书的技术条款」** ⇒ **我方 −40~75 ℃ 整机认证 + 5 年保修 +（若有）IEC 61850-3 正是标书条款。**
⇒ **话术**：「**你投标的时候，'−40~75 ℃ 整机（含电源）'这一条有没有？没有就写我这一台。**」
**⇒ 分级 80 → 81。**
**⚠ 空白**：VKN / MERSİS 未取；员工数未见。
"""

D['7'] = """
#### r79 补：**身份卡 —— 工程商 + 小批发，不是纯分销**

| 字段 | 内容 |
|---|---|
| 法定全称 | **KARER GÜVENLİK SİSTEMLERİ SANAYİ VE TİCARET LTD. ŞTİ.** |
| **成立** | **2006** |
| 地址 | **Yayalar Mah. Atasever Cad. No:44, Pendik / İstanbul**（PESİAD 另记 Velibaba Mah. Mimar Sinan Cad. Filika Sok. No:1/G） |
| 电话 | **0216 397 33 88** · GSM **0552 294 72 40** / **0555 084 72 40** |
| 邮箱 | `info@karerguvenlik.com` |
| **关键人** | **Nurbaki Karataş —— CEO**（ZoomInfo 列 C-Level）· **Ebru Tekin —— Muhasebe（会计）** |
| 规模 | **11–50 人** |
| 场地 | **1,000 ㎡ 封闭仓储**（PESİAD 会员页原文） |
| 副业 | **DESİ 智能锁/报警授权服务商**（服务码 **Desi 34/16**） |

**⇒ 判读**
**1,000 ㎡ 仓库 + 自有安装队 + 智能锁服务商身份** ⇒ **它是「工程商 + 小批发」，不是纯分销**。
⇒ **它最在意的是「一站式配齐 + 有现货」，不是「最低价」** ⇒ **话术不要打价格，打「备货 + 8 口工业 + 5 年保修」。**
**⇒ 分级 76 → 77。**
**⚠ 空白**：VKN / MERSİS 未取。
"""

D['52'] = """
#### r79 补：**身份卡 —— A 级里唯一「自称有生产设施 + AR-GE」的分销商**

| 字段 | 内容 |
|---|---|
| 法定全称 | **NOKTA ELEKTRONİK VE BİLİŞİM SİSTEMLERİ SANAYİ TİCARET A.Ş.** |
| **成立** | **2000** |
| **人数** | **75–99**（Kariyer.net）· SignalHire 记 38（**冲突，以 75–99 为准**） |
| 地址 | **Perpa Ticaret Merkezi A Blok Kat:2 No:1, 34384 Okmeydanı / Şişli / İstanbul**（另一记录 Perpa B Blok K:8 No:907） |
| 电话 / 传真 | **0212 222 87 80** · 传真 **0212 220 85 44** · **0850 333 02 08** |
| 官网 | `noktaelektronik.net` |
| **产能/设施** | **伊斯坦布尔设有生产设施，并在该设施内做 AR-GE**（原文 `İstanbul'da bulunan üretim tesisinde Ar-Ge faaliyetlerini sürdürerek`） |
| 网点 | **伊斯坦布尔 + 安卡拉 项目/销售办** |
| 出口 | **中东 · 巴尔干 · 突厥语共和国** |
| 定位 | 世界品牌**分销 + 进口 + 自有生产**三合一；专长：网络 · 电子 · 自动化 · **工业通信** · 结构化布线 · 专业音视频 · **RF** |

**⇒ 判读**
**它是 A 级里唯一（除 Angora 外）自称有生产设施 + AR-GE 的分销商** ⇒ **不能按「纯贸易商」对待**。
⇒ **见面第一句不要问「你有没有工厂」**（会显得没做功课），**直接问**：「**你的产线现在跑哪几个型号、贴谁的牌？**」
**⇒ 分级 78 → 80。**
**⚠ 空白**：**VKN / MERSİS 未取**；**生产设施地址未取**（现有只是 Perpa 办公室）。
"""

D['62'] = """
#### r79 补：**名字撞车排雷 + 六家身份总表 + 工业货架空位**

**① 🛑 Cebeci 有两个主体 —— 必须带 VKN 才能说清是哪一家**

| 主体 | **我们 `B/062` 要的那一家** | **不是**这一家 |
|---|---|---|
| 法定全称 | **CEBECİ TELETEKS SANAYİ TİCARET LTD. ŞTİ.** | **CEBECİ GRUP İNŞ. TUR. TİC. A.Ş.** |
| **VKN** | **2040018047** | 未取 |
| 地址 | **Halil Rıfat Paşa Mah. Yüzer Havuz Sok. No:8 Kat:3 D:24, 34384 Okmeydanı / Şişli / İstanbul** | Şekerhane Mah. Yayla Yolu Cad. Cebeci İş Merkezi No:22/1, **Alanya / Antalya** |
| 电话 | **0212 320 08 88**（传真 320 08 85） | — |
| 行业 | **电信测试仪表 + ONV 工业交换机 + 结构化布线测试** | **建筑 / 房地产** |
| 规模 | 小型（Perpa 商圈办公） | **66 人 · 营收 $50.5M · 1982 年** |
| 关键人 | — | Polathan Çiftçi（创始人）· GIGDER 代表 **Ahmet Cebeci** |

**⇒ `cebecigrup.com` 的域名归「电信测试」这一家**（页面全是 **Greenlee 711K / Argus 166 / Tempo TM-500 / NC-500 NETcat** 测试仪表），**不是建筑集团**。
**⇒ 纪律**：**任何提到「Cebeci」的材料必须带 VKN `2040018047` 或地址「Yüzer Havuz Sok.」**，否则一律标 ⚠ 主体未确认。
**⇒ 分级 45 → 47**（身份确认，但**它在卖 ONV（深圳）** ⇒ 是我方直接竞品的下游）。

**② ⭐⭐ 工业货架上有空位：RUBISEC 的 $584 档「有价无货」**
- `RS-IS-300-12GP`（8×GbE PoE + 2 GbE + 4×1G SFP）：**29,204.18 ₺ ≈ $584** —— 详情页原文 **`Ürün geçici olarak temin edilememektedir`（暂时无法供货）**。
- `RS-IS-300-12GPX`（8×GbE PoE + 2 + 4×**10G** SFP+，−40~80 ℃，IP40 DIN，**240 W**）：**61,075.68 ₺ ≈ $1,221**（含税 73,290.82）。
- `RS-IS-200-10GP`（8×PoE + 2 SFP）：**33,405.85 / 35,109.80 / 38,522.69 ₺ ≈ $668–770**。
**⇒ DMO 的「8 口工业 PoE」现在是「三档 + 一个空洞」**：**Dahua $380** · **RUBISEC $584（无货）/ $668–770** · **Cisco IE-3300 $2,315**。
**⇒ 我方 $500–700 正好落在「有货 + 有认证」这一格。**

**③ ⭐⭐⭐ 「÷2.95」规则被实价验证**
| 型号 | 官方挂牌 | r78 预测 | **DMO 实价** | 实际倍率 | 误差 |
|---|---|---|---|---|---|
| `RS-IS-300-12GPX` | **$3,600** | ≈$1,225 | **61,075.68 ₺ ≈ $1,221** | **2.95×** | **−0.3%** ✅ |
| `RS-IS-200-10GP` | $1,800 | ≈$610 | $668–770（聚合） | 2.34–2.70× | +10~26% |
| `RS-IS-300-12GP` | $1,950 | ≈$660 | **$584**（无货） | 2.61× | −11% |
⇒ **工业段溢价结构**：商用 8 口 `RS-ES-200-10PS` **$257** → 工业 `RS-IS-300-12GP` **$584**（**2.3×**）→ 工业 + 4×10G + −40~80 ℃ **$1,221**（**再 2.1×**）。
⇒ **「工业」这一层值 2.3 倍，「10G 上行 + 宽温」再值 2.1 倍。**

**④ ⭐⭐ FOREDGE 的 DMO 实价收口（r76 区间成立）**
`IS108GPS-2F`（工业 8×GbE PoE + 2×GbE SFP + 控制台，**240 W**）在 **FS Grup（K4702）详情页 = 52,264.98 ₺ ≈ $1,045**；其他聚合页出现 44,928.91 / 57,262.43 / 57,784.04。
**FS Grup 的 FOREDGE 交换机共 12 个 SKU，价位 5,807.00 – 121,951.00 ₺（≈$116–2,438）。**
⇒ **它是「一站式报单」逻辑（每个价位放一台），不是「专业工业」逻辑** ⇒ **这就是我方在 8 口工业能赢的结构性原因。**

**⑤ 六家身份总表（本轮补齐）**
| 客户 | 关键新增 | 分级 |
|---|---|---|
| **Snexus / Hemmah** | **MERSİS 0461092236500001 · VKN 4610922365** · Çekmeköy Turgut Özal Blv No:2 A6 No:145 · **品牌方=唯一分销商** | 85→**87** |
| **Nokta / upTech** | **2000 · 75–99 人 · Perpa A Blok K:2 No:1 · 0212 222 87 80 · 自有生产设施 + AR-GE · 出口中东/巴尔干/突厥** | 78→**80** |
| **CryptoLink** | **Çankaya Bükreş Cd No:19/1 · 0312 557 64 00 · 边境安全/网安/车牌识别/信号干扰** | 80→**81** |
| **Novacom / Nova Grup** | **2002 · NOVACOM 注册商标 · 弱电/卫星电视出身** | 86→**84** ↓ |
| **Karer** | **2006 · Pendik Atasever Cd No:44 · 1,000 ㎡ · CEO Nurbaki Karataş · DESİ 34/16** | 76→**77** |
| **Cebeci Teleteks** | **VKN 2040018047 · Yüzer Havuz Sok. No:8 K:3 D:24 · 0212 320 08 88** | 45→**47** |

**证据等级**：`dmo.gov.tr/Katalog/Urun/Detay/4360378_1224029` · `dmo.tr/rapor/UrunDetay/4360378_1224035` · `dmo.gov.tr/Arama` 三处 · **`www.dmo.gov.tr/EMagaza/Magaza/Standart/1145171`**（FS Grup 12 SKU / 价位带）· `webrate.org`（Snexus 域名注册人）· `snexus.com.tr/sözleşme` · `trendyol.com`（**MERSİS/VKN**）· `allesgo.com` · `snexus.com.tr/dağıtıcılar` · `eguvenlik.com.tr` · `lusha.com` · `kariyer.net` · `guvenlikonline.com` · `signalhire.com` · `yenibiris.com` · `pesiad.org.tr` · `karerguvenlik.com` · `zoominfo.com` · `desi.com.tr` · `cryptolink.com.tr` · `novacom.com.tr` ×2 · `nova-grup.com` · `success.ai` · `cebecigrup.com` ×2 · **`tet.org.tr/.../EEIB_GK_KATILMAYA_HAIZ_FIRMALAR.pdf`（VKN 2040018047）** · `gigder.org.tr` · `rocketreach.co` —— **共 21 个来源，逐字/结构化**。

**空白**：`RS-IS-200-10GP` 详情页价 · `RS-IS-300-12GP` 何时恢复供货 · **Nokta 的 VKN/MERSİS + 生产设施地址** · **Karer / CryptoLink / Novacom 的 VKN/MERSİS** · Hemmah 的员工数与老板 · FS Grup 的 12 个 SKU 完整清单 · **所有电话未试拨**（新增 Nokta 0212 222 87 80 / 0850 333 02 08 · Karer 0216 397 33 88 · CryptoLink 0312 557 64 00 · Cebeci 0212 320 08 88）。
"""
