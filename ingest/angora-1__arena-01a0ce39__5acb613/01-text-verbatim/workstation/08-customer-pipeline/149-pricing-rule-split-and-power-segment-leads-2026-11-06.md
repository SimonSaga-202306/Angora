# 149 · r80：**「÷2.95」只对白牌成立 —— 定价规则必须拆成双轨** + **Nokta 工商级身份补完（VKN/MERSİS/实缴资本）** + **三条新线索（电力段）**

> **轮次**：r80 ｜ **日期**：2026-11-06（+0800）｜ **上一轮**：r79（`148-…`）
> **用户指令（第 33 次「继续」）**：继续挖客户信息，**每次把工作时间拉长 10 分钟以上**。
> **本轮主线**：r79 把「挂牌 ÷2.95 = 成交」当通用规则写进了方法库。**本轮找到反例，规则必须拆轨。** 同时电力段挖出三条新线索。

---

## 0 · 本轮六句话

1. **🛑 修正 r79：`÷2.95` 不是通用规律，是「白牌挂牌虚高」的特例。** 反例：**PLANET `IGS-801T` 美国 MSRP $172 / Newegg $179**，**DMO 净价 6,955.49 ₺ ≈ $139（含税 8,346.59 ₺ ≈ $167）** ⇒ **DMO 只有 MSRP 的 0.81 倍**。**有真实 MSRP 的品牌，DMO 比海外零售还便宜；只有「挂牌是锚」的白牌才需要 ÷2.95。**
2. **新 K 码：İNFOGEN `K5884`** —— PLANET 在 DMO 的挂单方，**合同 2026-03-10 → 2028-03-10（刚续两年）**，电话 **0216 706 1845**。
3. **三条新线索（都在电力/工业自动化段，不在安防段）**：**İNFOGEN（D-Link + PLANET）· Simgenet（3onedata 代理 + 自研 SMGOS，TEİAŞ OPGW）· İSAC（Advantech 工业交换机授权伙伴）**。
4. **Nokta 的工商身份补完，并推翻 r79 的「2000 年成立」**：注册 **2005-05-26**，**VKN `6310730521` · MERSİS `0631-0730-5210-0020` · 商业登记 `555138-0`**，**实缴资本 30,000,000 ₺（≈$600k）**，**`upTech` 是它注册的商标**。
5. **DMO 工业 8 口现在是完整的两条轴**（PoE / 非 PoE），**四个节点：$139（PLANET 非 PoE）→ $380（Dahua PoE 120 W）→ $584–770（RUBISEC 工业 PoE）→ $2,315（Cisco IE-3300）**。
6. **电力段（IEC 61850-3）是安防段之外的第二战场，而且我们之前的客户表里一个都没有** —— 这一段的代理权在 **GSL（Moxa/Kyland）· ErETE（EtherWan）· Simgenet（3onedata）· Beijer（JetNet）· İSAC（Advantech）** 手里。

---

## 1 · 🛑 定价规则的修正：拆成双轨

| 类型 | 案例 | 挂牌 | DMO 净价 | 倍率 | 结论 |
|---|---|---|---|---|---|
| **白牌（挂牌是锚）** | RUBISEC `RS-ES-200-28PS` | $1,200 | **$406** | **2.96×** | **必须 ÷2.3–3.0** |
| | RUBISEC `RS-IS-300-12GPX` | $3,600 | **$1,221** | **2.95×** | 同上 |
| **真实 MSRP 品牌** | **PLANET `IGS-801T`** | **US MSRP $172** | **$139** | **0.81×** | **DMO 低于海外零售，不能用除法** |
| | PLANET（Newegg 零售） | $179 | $139 | 0.78× | 同上 |

**⇒ 新规则（替代 r79 的单一规则）**
1. **先判断品牌类型**：**有公开 MSRP / 有全球零售价（PLANET、Moxa、Cisco、HPE…）** ⇒ **DMO 价 ≈ 0.8–1.0× MSRP**，直接引用即可。
2. **只有「官网自己挂一张 price list、没有第三方零售可比」的白牌（RUBISEC 这类）** ⇒ **÷2.3–3.0 还原**。
3. **拿不准时用这个探针**：**去美国零售站（Newegg / planetechusa / DigiKey）搜同一型号**。**能搜到 ⇒ 走第 1 条；搜不到 ⇒ 走第 2 条。**

**⇒ 这条修正的实际影响**：**r78/r79 里所有「÷2.95 还原」的数只对 RUBISEC 有效**。**Moxa、Planet、Cisco 的历史价格锚不需要重算 —— 它们本来就在市场价附近。** 这省掉了一整轮返工。

---

## 2 · ⭐⭐ 新 K 码：İNFOGEN `K5884`（PLANET 在 DMO 的挂单方）

| 字段 | 内容 |
|---|---|
| **供应商** | **İNFOGEN DANIŞMANLIK VE BİLİŞİM A.Ş.** |
| **K 码** | **`K5884`**（另有 `K3193` / `K4329`，r76 记录） |
| 电话 | **0216 706 1845** |
| **合同** | **2026-03-10 → 2028-03-10（刚续，两年）** |
| 挂单产品 | **PLANET `IGS-801T`**（8 口工业千兆**非** PoE，−40~75 ℃，IP30，16 Gbps，4K MAC） |
| 价格 | **6,955.49 ₺ 未税 / 8,346.59 ₺ 含税（KDV 20%）≈ $139 / $167** |
| DMO 产品码 | **131798** |
| 其他在册品牌 | **D-LINK**（r76 已记录） |

**⇒ 三条**
- **İNFOGEN 是「D-Link + PLANET」两条线的 DMO 挂单方** ⇒ **它是「中低端进口网络设备」在政府渠道的实际操盘手**，**不是安防商**。**这是客户表里没有的一类角色。**
- **它的合同刚在 2026 年 3 月续到 2028 年** ⇒ **两年内不会换供应商，但会换「补充型号」** ⇒ **我要进的不是替代 PLANET，是补 PLANET 缺的那一格（8 口工业 PoE）。**
- **PLANET 自己的产品线里 `IGS-801T` 是非 PoE** ⇒ **PLANET 的 8 口工业 PoE（`IGS-1000` 系列）不在 DMO** ⇒ **这一格在 İNFOGEN 这里也是空的。**

---

## 3 · ⭐⭐⭐ 三条新线索：电力段（IEC 61850-3）

> **为什么重要**：我们的 146 家客户里，**没有一家是电力自动化集成商**。而 **IEC 61850-3 是唯一「认证即壁垒」的段位** —— 一旦进了，价格敏感度立刻下降。

### 3.1 Simgenet Mühendislik（**3onedata 土耳其代理**）

| 字段 | 内容 |
|---|---|
| 法定全称 | **SİMGENET MÜHENDİSLİK ENERJİ SANAYİ VE TİCARET LİMİTED ŞİRKETİ** |
| **成立** | **2020-04-05** |
| 地址 | **Orhantepe Mah. Girne Sk. No:25A, 34865 Kartal / İstanbul**（已迁：Orhantepe Mah. Tomurcuk Sok. 4B） |
| 电话 / 邮箱 | **+90 555 600 45 06** · `info@simgenet.net` |
| **核心代理** | **3onedata（中国）** —— `MES5400`（30 口模块化 L3，**IEC 61850-3**，HSR/PRP，IEEE 1588v2）· `MES5300-28GS` · `MES5300-24GT4GS` · `MES5200` · `MES6400PHR-8GT4XS`（**8GT + 4XS HSR/PRP**）· `ICS5400TSN` |
| **自研** | **SMGOS 平台**（土耳其自研网络操作系统）· `Simgenet Teleprotection Unit V2` |
| 业务 | **TEİAŞ OPGW 通信 · PAX 通信 · PLC（电力线载波）· TPU 保护单元 · RTU · 本地 SCADA · IP/MPLS 路由 · SDH/PDH** |
| 资质 | **ISO 9001 · CE · TSE** |

**⇒ 判读**
- **它是「电力通信总包 + 中国品牌代理 + 自研 OS」的三合一**，**规模小（2020 年成立、手机号做总机）但段位极高**（TEİAŞ 是土耳其国家电网）。
- **3onedata 与我们的产品重叠度极高**（工业 PoE、IEC 61850、HSR/PRP）⇒ **它是「潜在客户」也是「潜在对手的渠道」**。
- **⇒ 打法**：**不打价格，打「第二供应源」** —— 「**3onedata 的 `MES6400PHR-8GT4XS` 交期多久？我给你一个同规格、能并行投标的第二源。**」

### 3.2 İSAC（**Advantech 工业交换机授权伙伴**）

| 字段 | 内容 |
|---|---|
| 站点 | `isac.com.tr` |
| 电话 / 邮箱 | **0850 60 60 180** · `bilgi@isac.com.tr` |
| **授权范围** | **Advantech 工业以太网交换机全线**：`EKI-2000` / `EKI-5000` / `EKI-7000` / `EKI-9000`（含 `EKI-2525P`、`EKI-2728` 等 DIN 导轨型号） |
| 自我定位 | 「**Türkiye'nin endüstriyel sensör ve otomasyon tedarikçisi**」（工业传感器 + 自动化） |
| 品类 | 工业交换机 · PoE 交换机 · 工业平板/HMI · 传感器 · IoT 网关（`WISE-2410`、`ICR-1601`） |

**⇒ 判读**：**它是「工业自动化分销商」，不是安防商** —— **和我们的 146 家客户完全不重叠**。**它卖的 Advantech EKI 系列是「工业级但非 IEC 61850」** ⇒ **它缺电力认证那一格。**

### 3.3 电力段的完整代理地图（本轮补全）

| 品牌 | 土耳其代理 | 认证强项 |
|---|---|---|
| **Moxa** | **GSL Mühendislik**（2003 起，22 年） | **IEC 61850-3 · EN 50155 · NEMA TS2 · IEC 62443** |
| **Kyland** | **GSL Mühendislik** | **IEC 61850-3 · EN 50155**（L2/L3 骨干） |
| **EtherWan** | **ErETE**（`EX47000` 系列，`EX47080-00B`，**IEC 61850 / IEEE 1613**，−40~75 ℃） | **IEC 61850-3 / IEEE 1613** |
| **3onedata** | **Simgenet**（`MES5400/5300/5200/6400PHR/ICS5400TSN`） | **IEC 61850-3 · HSR/PRP · IEEE 1588v2** |
| **JetNet（Korenix）** | **Beijer Electronics Türkiye** | **IEC 61850-3 · DNV · eMark · ITxPT · EN 50155** |
| **Advantech** | **İSAC** | CE/FCC/UL（**工业级，非变电站认证**） |
| **RUBISEC** | **Birkil Savunma**（`RS-IS-300-12GPX`，−40~80 ℃） | ⚠ **未见 IEC 61850-3 声明** |
| **Alcatel / Cisco / Extreme** | 多家 DMO 渠道 | 有，但价格在 $1,300–2,300 |

**⇒ 结论**：**「IEC 61850-3」这一格的土耳其代理权已经被 6 家分完，而且全部是「欧美/台/中品牌 + 本土代理」。**
**⇒ 我方进这一段的唯一路线**：**做「第二源」而不是「第三品牌」** —— 找 Simgenet / ErETE / İSAC 这类**已有电力客户但品牌单一的代理**，给他们一个**同规格、能并行投标**的备份。

---

## 4 · ⭐⭐ Nokta 的工商级身份（并推翻 r79 的成立年）

| 字段 | 内容 |
|---|---|
| 法定全称 | **NOKTA ELEKTRONİK VE BİLİŞİM SİSTEMLERİ SANAYİ TİCARET ANONİM ŞİRKETİ** |
| **VKN（税号）** | **6310730521**（**Şişli** 税务局） |
| **MERSİS** | **0631-0730-5210-0020** |
| **商业登记号** | **555138-0**（登记号 555138） |
| **注册成立** | **2005-05-26**（原为 **LTD. ŞTİ.**，后转为 **A.Ş.**） |
| **实缴资本** | **30,000,000.00 ₺**（≈$600k） |
| NACE | **#465202** 电子器件与零件批发 |
| 地址 | **Perpa Ticaret Merkezi A Blok Kat:2 No:1**（信函址：**B Blok Kat:8 No:906**, 34384 Şişli） |
| 电话 / 邮箱 | **0212 222 87 80** · `nokta@noktaelektronik.net` |
| KEP | `noktaelektronikvebilisim@hs03.kep.tr` |
| **ETBİS 登记** | **2024-05-02** |
| **商标** | **`upTech` 是 Nokta 注册的商标**（土耳其专利商标局） |

**🛑 修正 r79**：r79 依 SignalHire 记「成立 2000」。**工商登记是 2005-05-26**；「2000」是公司自我表述（可能指前身/个体经营起点）。**对外一律用 2005-05-26 + VKN 6310730521。**

**⇒ 三条**
1. **实缴资本 3,000 万 ₺（≈$600k）** ⇒ **在 A 级里属于「中等偏上」的重资产分销商**，比 Cenova（Perpa 三层但 LTD）更「公司化」。
2. **「2000 → 2005」这个差** 说明**它喜欢把历史讲长 5 年** ⇒ **谈判中任何「我们做了 25 年」的说法都要打折听。**
3. **`upTech` 是注册商标** ⇒ **它不会轻易换牌**，**但可以换「牌下面的机器」** ⇒ **话术：不换 `upTech`，换里面的板子。**

---

## 5 · DMO「工业 8 口」完整两轴（本轮定稿）

| 轴 | 型号 | 关键规格 | DMO 净价 | ≈USD | 供应商 |
|---|---|---|---|---|---|
| **非 PoE** | **PLANET `IGS-801T`** | 8×GbE，**−40~75 ℃**，IP30，16 Gbps，非受管 | **6,955.49 ₺** | **$139** | **İNFOGEN `K5884`**（2026-03-10→2028-03-10） |
| **PoE 白牌** | **DAHUA `DH-PFSC28GT1-120D`** | 8×GbE PoE **120 W** + 1 GbE + 2 SFP，非受管，−30~65 ℃ | **18,993.83 ₺** | **$380** | （`55483`）· AKTİF GRUP 另挂 22,586.84 |
| **PoE 白牌 12 口** | **RUBISEC `RS-IS-300-12GP`** | 8×GbE PoE + 2 GbE + 4×1G SFP，**暂时无货** | **29,204.18 ₺** | **$584** | **Birkil `K4525`** |
| **PoE 白牌 8 口** | **RUBISEC `RS-IS-200-10GP`** | 8×GbE PoE + 2 SFP | **33,405–38,522 ₺** | **$668–770** | `K4525` |
| **PoE + 10G + 宽温** | **RUBISEC `RS-IS-300-12GPX`** | 8×PoE + 2 + **4×10G**，**−40~80 ℃**，IP40 DIN，**240 W** | **61,075.68 ₺** | **$1,221** | `K4525` |
| **PoE 工业 12 口** | ALCATEL `OS6465T-P12` | 工业 12 口 | 65,342–66,451 ₺ | $1,306–1,328 | — |
| **PoE+ 天花板** | **CISCO `IE-3300-8P2S-E`** | 8×PoE+ + 2 SFP，工业 | **115,787.25 ₺** | **$2,315** | **4S BİLİŞİM `K4427`** |

**⇒ 我方 $500–700 的定位现在有三条支撑**：① **Dahua 的 $380 是「非受管 + 120 W + −30 ℃」**；② **RUBISEC 的 $584–770 档「无货 / 非宽温 / 资料不全」**；③ **Cisco 的 $2,315 是天花板**。**「受管 + 240 W + 整机 −40~75 ℃ + 有货」在 $500–700 = 唯一解。**

---

## 6 · 客户与线索的变动（r80）

| 对象 | 类型 | 状态 | 分数/说明 |
|---|---|---|---|
| **Nokta / upTech** | A 级客户 | **身份补完** | 78 → **81**（实缴 30M ₺、VKN/MERSİS 齐、`upTech` 自有商标） |
| **İNFOGEN** | 🆕 **新线索（渠道）** | 待建档 | **`K5884` · D-Link + PLANET · 合同至 2028-03 · 0216 706 1845** |
| **Simgenet** | 🆕 **新线索（电力）** | 待建档 | **3onedata 代理 + 自研 SMGOS + TEİAŞ OPGW · 2020-04-05 · +90 555 600 45 06** |
| **İSAC** | 🆕 **新线索（自动化）** | 待建档 | **Advantech EKI 全线授权 · 0850 60 60 180** |
| Beijer TR / ErETE | 竞对渠道 | 地图补全 | JetNet / EtherWan `EX47000`（IEC 61850-3） |

---

## 7 · 证据等级与空白

**逐字 / 结构化来源（本轮 24 个）**：
`www.dmo.gov.tr/Katalog/Urun/Detay/6254602_1277284`（**PLANET `IGS-801T` 6,955.49 ₺ / 8,346.59 ₺ · 131798-K5884 · İNFOGEN · 0216 7061845 · 合同 2026-03-10→2028-03-10 · −40~75 ℃ · 16 Gbps**）· `planet.neteon.net`（**US MSRP $172**）· `newegg.com`（**$179**）· `planetechusa.com`（$172 · 另有 `IGS-800T` $177.53）· `www.dmo.tr/Katalog/Arama?...p=17` 与 `dmo.gov.tr/Arama?...p=14`（`IGS-801T` 131798 · `GSD-1002M` 9,951.70 · PLANET 26 个 SKU · MAIPU 28 · LANDE 5 · PEPLINK 4）。
`eticaret.gov.tr/siteprofil/.../noktaelektronikcomtr`（**MERSİS 0631073052100020**）· `noktaelektronik.net/tr/yasal-bilgiler`（**VKN 6310730521 · MERSİS 0631-0730-5210-0020 · Sicil 555138-0 · Şişli VD · Perpa B K:8**）· `noktaelektronik.com.tr/yasal-bilgiler`（**B Blok K:8 No:906**）· `b2bhint.com`（**成立 2005-05-26 · 实缴 30,000,000 ₺ · NACE 465202 · 原名 LTD**）· `noktaelektronik.net/en/hakkimizda`（**upTech 是注册商标** · 中东/突厥/巴尔干）。
`simgenet.net` + `/urunler.php`（**3onedata `MES5400/5300-28GS/5300-24GT4GS/5200/6400PHR-8GT4XS/ICS5400TSN`** · **SMGOS** · **Teleprotection Unit V2**）· `simgenet.net/photel-sdh`（TEİAŞ OPGW · PLC · RTU · IP/MPLS · SDH/PDH）· `tikla.com.tr` + `firmadan.com`（**Orhantepe Mah. Girne Sk. No:25A Kartal · 05.04.2020 · 0555 600 45 06**）· `yandex.com.tr/maps`（迁址 Tomurcuk Sok. 4B）。
`isac.com.tr` ×3（**Advantech EKI-2000/5000/7000/9000 授权伙伴 · 0850 60 60 180 · bilgi@isac.com.tr**）· `erete.com.tr/Kullanici/Urun/UrunDetay/1147`（**EtherWan `EX47000` / `EX47080-00B` · IEC 61850 / IEEE 1613 · −40~75 ℃**）· `gsl.com.tr/moxa-endustriyel-ethernet-switch.html`（**Moxa 全线 IEC 61850-3 / EN 50155 / NEMA TS2 / IEC 62443，Kyland IEC 61850-3**）· `beijerelektronik.com.tr`（**JetNet · IEC 61850-3 · DNV · eMark · ITxPT · EN 50155**）· `dmo.gov.tr` 早前条目（RUBISEC / DAHUA / CISCO 各 K 码）。

**空白（诚实标注）**
1. **İNFOGEN 的工商身份**（VKN/规模/成立年/总部地址）—— **只有电话与 K 码**。
2. **Simgenet 的员工数与营收**（2020 年成立、手机号做总机 ⇒ 判断为 ≤10 人，**未证实**）。
3. **Simgenet 的 VKN / MERSİS**。
4. **İSAC 的法定全称 / 地址 / VKN**（只有 0850 号与邮箱）。
5. **Karer / CryptoLink / Novacom 的 VKN** —— 本轮检索失败（b2bhint 与 eticaret 均无命中）。
6. **PLANET 的 8 口工业 PoE（`IGS-1000` 系列）在 DMO 是否有货**。
7. **RUBISEC 是否有 IEC 61850-3 声明**（`RS-IS-*` 只写 −40~80 ℃ 与 IP40）。
8. **所有电话仍未试拨**（本轮新增：**İNFOGEN 0216 706 1845** · **Simgenet +90 555 600 45 06** · **İSAC 0850 60 60 180**）。

---

## 8 · r81 建议（按价值排序）

1. **🔥 给 İNFOGEN 建档并打电话**：它是 **D-Link + PLANET 的 DMO 操盘手，合同到 2028-03**，而**它手上没有 8 口工业 PoE** ⇒ **最短路径的一单**。
2. **🔥 电力段三家的「第二源」方案书**：Simgenet（3onedata）· ErETE（EtherWan）· İSAC（Advantech）—— **统一说一句话**：「**你的品牌交期 8–12 周，我给你同规格第二源，能并行投标。**」
3. **⭐ 确认 RUBISEC 有没有 IEC 61850-3** —— **如果没有，那 $1,221 的 `RS-IS-300-12GPX` 在变电站标里根本不能用** ⇒ **我方的认证就是唯一差异点。**
4. **⭐ 把 Nokta 的「2005 vs 2000」写进话术**（对方讲 25 年时，用工商登记年回应，但不要点破）。
5. **⭐ 电力段四家客户的建档优先级**：İNFOGEN（渠道）> Simgenet（电力总包）> İSAC（自动化）> Beijer（外资分公司）。
6. **技术债**：Karer / CryptoLink / Novacom 的 VKN · `G5328P-24-410W` $240 复核 · Lansan 真实 VKN。
