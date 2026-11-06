# 145 · r76：**DMO 价格地图打通** + **土耳其有自己的交换机厂（Angora Networks）** + **XPS 身份解开**

> **轮次**：r76 ｜ **日期**：2026-11-06（+0800）｜ **上一轮**：r75（`144-…`）
> **用户指令（第 29 次「继续」）**：继续挖客户信息，**每次把工作时间拉长**，不必过度关注 Saga 的价格。
> **本轮方法**：用 **「供应商 K 码 → 品牌 → 单价」** 三件套反查 DMO，把「谁在政府渠道卖什么价」一次拉平；再顺手解开上轮两个身份空白。

---

## 0 · 本轮七句话

1. **DMO 是公开的价格数据库。** 只要拿到供应商的 **K 码**，就能翻出它**在售型号 + 单价 + 合同起止**。本轮拿到 **4 个 K 码**：**TeleOne = K2887**、**Telkolink/GelecekBT = K291**、**FS Grup = K4702**、**Han 的 FOREDGE 走多家供应商**。
2. **TeleOne 的 K2887 是僵尸码**：合同 **2021-09-09 → 2023-09-09** 已过期，页面写「temin edilememektedir」（无法供货）⇒ **它现在的 DMO 势力是历史，不是现在**。这修正了 r75「2014 起进 DMO、自述前三」的时间感。
3. **Han Elektronik 的 FOREDGE 有 10 个型号在 DMO 目录里**，且**同一型号不同供应商价差最高 29%**。其中 **8 口工业千兆 PoE（`IS108GPS-2F`，240 W）卖 44,929–57,784 ₺ ≈ $898–1,155** —— **这就是「白牌层价格伞」最硬的一个数。**
4. **土耳其有自己的交换机厂**：**Angora Networks Bilişim Teknoloji Ticaret Sanayi A.Ş.**（**2016-11-28**，安卡拉，**VERGE** 交换机家族，8/24/32/48×GbE + 4×10G，还有 **Data Diode「Arrow」**）。它既是**本土竞争对手**，也是**最理想的 OEM/联合品牌对象**。
5. **XPS 身份解开，r73 的说法被推翻**：`XPS Active Systems` = **XPcable Group（台北 11F, 51 HENGYANG ROAD）**，与 `XPCABLE` 布线**同一集团** —— **不是 ONV 贴牌**。ErETE 同时是这两个品牌的土耳其分销。
6. **BDCOM 在土耳其是「独家」**：`bdcom.com.tr` 原文「**Öncü Güvenlik, BDCOM'un Türkiye'deki exclusive distribütörüdür**」，22 个型号 ⇒ **BDCOM 的 $399 锚价是独家代理价，不是市场价。**
7. **Sec-on `SC-E208-4FH` 的完整规格拿到了**（8×GbE PoE + 4×GbE SFP，**240 W**，−40~75 ℃，L2+ managed）⇒ **这是我们最该对标的机型，不是 Moxa。**

---

## 1 · ⭐⭐⭐ DMO 反查总表（本轮核心成果）

> 方法：DMO 产品页 URL 形如 `/Katalog/Urun/Detay/{供应商ID}_{产品ID}`，页面正文含 **`产品码-K供应商码`**、**单价（+Vergiler）**、**含税价**、**合同起止**、**供应商全称**。
> ⚠ 所有 DMO 价格为 **TL，未税（+Vergiler）**，含税另列（KDV 18% 或 20%）。换算用 USD/TRY **50.02**（沿用）。

### 1.1 TeleOne —— **K2887（僵尸码：合同 2021-09-09 → 2023-09-09）**

| 型号 | 品名 | DMO 价（未税） | 含税 | 折 USD |
|---|---|---|---|---|
| **`BRICKCOM PS-7242IL-AT`** | **24 口 10/100 PoE+ Web Smart 交换机** | **14,645.16 ₺** | — | **≈$293** |
| `BRICKCOM NR-8232-RM-D` | 32 路 IP NVR | 39,501.00 ₺ | 46,611.18 ₺（KDV 18%） | ≈$790 |
| `BRICKCOM OB-H200NP-WDRPRO-H265` | 枪机 2MP | 10,534.01 ₺ | 12,430.13 ₺ | ≈$211 |
| `BRICKCOM VD-300NP-VIA` | 半球 3MP | — | — | — |
| `LANDE LN-SBO-IP5509U6060-LG` | 室外机柜 | 5,088.39 ₺ | — | ≈$102 |

**⇒ 三条判读**
- **它确实卖过交换机**（`PS-7242IL-AT`，美国挂牌 $1,113，DMO 折 $293）⇒ **交换机在它的 DMO 品类里是存在的，只是靠 Brickcom 供**。
- **BRICKCOM 是台湾品牌**，型号老（10/100、Web Smart）⇒ **这一格现在是空的：DMO 目录里没有一台「千兆 + 802.3at + 工业」的 TeleOne 货**。
- **K2887 合同已过期两年** ⇒ 若 TeleOne 要重回 DMO，**它需要新的 SKU 与新的技术规格**，这就是我们的窗口。**谈的时候直接问：「你的 DMO 合同 2023 年 9 月就到期了，新一期准备放什么型号？」**

### 1.2 Telkolink / GelecekBT（A 级，Perpa A K:5 No:295）—— **K291**

- **DMO 目录文件标题即 `DMO ÜRÜN KATALOĞU -K291`**，DMO 批准 **2018-08-03，文号 55238**。
- 进目录的 **CLR 自有型号**（部分）：
  `CLR-SW-811P`（8×10/100 PoE + 2 GbE SFP，非受管）· `CLR-SWG-822P`（8×100M PoE + 2 Combo）· `CLR-SWG-1621P`（16 口 PoE）· `CLR-SWF-2422P`（24×100M PoE + 2 GbE）· `CLR-IES-G42P`（**4×GbE + 2 SFP 非受管工业 PoE**）· `CLR-IES-G82P`（**8×GbE PoE + 2 SFP 工业非受管**）· `CLR-IES-G802P`（**8×RJ45 PoE + 2 SFP 受管**）· `CLR-IES-G824P`（14 口受管）· `CLR-IES-T884P`（**DIN 导轨 24 口 10G L2+ 骨干 PoE**）· `CLR-SWG-28`（**8 SFP + 2 GbE 骨干**）· `CLR-SWT-4244`（光纤骨干 L2+）· `CLR-FXS/FXO` 电话光端机 · `CLR-VTR` 模拟视频光端机 · `CLR-MCT-SFP+` 10G 转换器。
- **⭐ 同一份目录里并列出现 `TG-NET` 的 PoE 交换机**（`P3010M-8POE`、`P3018M-16POE`、P1000 系列、S5500 L3 骨干）⇒ **TG-NET = 中国 ODM，CLR 的货就是它贴的**（这是「CLR 自有品牌」的底牌）。
- **它还有一本 `IEC61850 Ethernet switch` 目录** ⇒ **GelecekBT 已经能做电力标**。

**⇒ 判读**：**A 级第一名手里握着一个活的 DMO 目录（K291）+ 一本 IEC 61850 目录 + 一条中国 ODM 上游。**
**⇒ 话术**：「**TG-NET 那条线，我给你换一代：千兆 PoE + 802.3bt + 环网 G.8032，规格直接进你 K291 的下一版。**」

### 1.3 Han Elektronik 的 **FOREDGE** —— DMO 在售 **10 个型号**，同一型号价差最高 29%

| FOREDGE 型号 | 规格 | DMO 价区间（₺ 未税） | 折 USD | 价差 |
|---|---|---|---|---|
| `AI2010GX` | 安防用 PoE 交换 | **29,036.10 – 32,102.24** | $580–642 | 10.6% |
| `AI8024` | 24 口 | **25,681.80 – 58,072.20** | $513–1,161 | **126%** ⚠ |
| `AI1016GC` | 16×GbE + 2 SFP，250 W 云管理 | **43,554.16 – 48,153.37** | $871–963 | 10.6% |
| `AI1024GC` | 24×GbE，300/360 W | **58,072.20 – 64,204.49** | $1,161–1,284 | 10.6% |
| `PS2024GR` | 24 口 PoE | **70,624.93** | $1,412 | — |
| `S5700-24GP-4TFR` | 24×GbE PoE **360 W** + 4×10G SFP+ | **62,401.27 – 80,255.62** | $1,248–1,604 | 28.6% |
| `S5700-48GP-4TFR` | 48×GbE PoE 360 W + 4×10G | **84,865.72 – 109,147.63** | $1,697–2,182 | 28.6% |
| `S5700-24F-8G-4TF` | 24×SFP + 8×GbE + 4×10G | **104,834.12 – 134,829.42** | $2,096–2,695 | 28.6% |
| **`IS104GPS-2F`** | **工业 4×GbE + 2 GbE SFP，120 W** | **34,944.71 – 44,943.14** | **$699–898** | 28.6% |
| **`IS108GPS-2F`** | **工业 8×GbE + 2 GbE SFP，240 W** | **44,928.91 – 57,784.04** | **$898–1,155** | 28.6% |

**⇒ 这是全项目最有杀伤力的一张表**
- **一台「8 口工业千兆 PoE 240 W」在土耳其政府采购里卖 $898–1,155**（FOREDGE），而**国际大牌的地板价是 PLANET `IGS-801T`（8 口工业**非**PoE）8,346.59 ₺ ≈ $167**。
- **价差 28.6% 不是成本差，是渠道差** —— 同一台机器，不同供应商在 DMO 目录里挂两个价。⇒ **「谁拿到更低的工厂价，谁就能在那个 28.6% 里赢」。**
- **FOREDGE 的规格书已经很接近我们**（GbE + SFP + 240 W + 云管理）⇒ **我们的对标不是 Moxa，是 FOREDGE 的这一栏。**

### 1.4 **FS Grup Bilişim Ltd. Şti.**（DMO **K4702**）—— Han 的下游渠道，本轮新线索

| 项 | 内容 |
|---|---|
| 成立 / 地址 | **2017** · **Cevizlidere Mah. 1243. Sok. No:6/4, Öveçler / Çankaya / Ankara** |
| 电话 / 传真 | **0312 473 32 00** · Faks 0312 473 32 01 · `fsgrup.com.tr` |
| DMO 目录 | **44 个产品**，含 **FOREDGE 全部交换机**（`119853-K4702` … `119881-K4702`）+ **MILESIGHT** 摄像机/VMS + **AXXON** 视频软件 |
| 身份判读 | **它不生产，它把 Han 的 FOREDGE 挂进 DMO**（同一型号 K4702 价通常**低于**其他供应商 ⇒ 它在打价格） |

**⇒ 这是「DMO 渠道商」这一类客户的样本**：**不碰工厂、只碰目录**。我们要找的不是它，而是**它上游的那家工厂**（也就是我们自己这一类）。

### 1.5 DMO 里顺带看到的「地板价参照」

| 型号 | 品名 | DMO 价 | 折 USD |
|---|---|---|---|
| `PLANET IGS-801T` | 8 口工业**非**受管 | **8,346.59 ₺** | **≈$167** |
| `PLANET GS-4210-8P2S` | 8 口 PoE + 2 SFP 受管（商用） | — | — |
| `D-LINK DGS-3000-52X` | 48 口 L2+ | 35,179.47 ₺（KDV 20%） | ≈$703 |
| `HPE JG932A`（5130 24G 4SFP+） | 24 口 | 19,993.19 ₺（KDV 18%） | ≈$400 |
| `HUAWEI S5735-L48T4XE-A-V2`（NETCOM K4716） | 48 口 | 65,946.95 ₺（KDV 20%） | ≈$1,318 |

⇒ **结论**：**DMO 的「工业 8 口」价格带从 $167（PLANET 非 PoE）一路开到 $1,155（FOREDGE 8 口 PoE 240 W）。我们的位置在 $167 与 $898 之间，空间极大。**

---

## 2 · ⭐⭐⭐ 土耳其有自己的交换机厂：**Angora Networks**

> 这一家**此前完全不在档案里**。它可能是全表里**唯一一家真正的土耳其交换机厂商**。

| 项 | 内容 |
|---|---|
| **法定全称** | **ANGORA NETWORKS BİLİŞİM TEKNOLOJİ TİCARET SANAYİ ANONİM ŞİRKETİ** |
| **成立** | **2016-11-28**（NACE **620902**） |
| **销售办公室** | **Nergiz Sok. No:7, Kat:3, Via Flat / Plaza Cubes, Söğütözü / Ankara 06560** |
| **⭐ 制造基地** | **Çamlıca Mah. Anadolu Blv. Timko Sk. Z Blok No:20/1, Yenimahalle / Ankara 06200** |
| **注册地址** | Alacaatlı Mah. Park Cad. 47/31, Yenimahalle / Ankara |
| **电话 / 邮箱** | **+90 312 241 77 47** · `sales@angoranetworks.com` |
| **人数** | **10–50**（LinkedIn 11–50 / rocketreach 10 / Crunchbase 11–50） |
| **口号** | **「Yerli Akıl, Küresel Teknoloji」**（本土智慧，全球技术） |
| **产品** | **VERGE 交换机家族**（**8 / 24 / 32 / 48 × GbE + 4×10G 光纤骨干**，受管）· **SFP 模块** · **瘦客户机** · **数据二极管「Arrow」（Data Diode，支持 ModBUS 与 OPC）** · WiFi / VoIP 方案 · **PacketFence NAC 集成** |
| **自我定位** | 官网原文「**The official website of Turkey's network equipment manufacturer**」「**a disruptive Turkish manufacturer of Communications Networking equipment**」 |

**⇒ 三种可能性，都要准备**
1. **对手**：它在做「国产交换机」叙事，政府标里「yerli üretici」（本土制造商）身份在 DMO 评级里是加分项（见 DMO 第 6 部分：**供应商分 A/B/C/D 四档，其中一项就是「是否本土制造商」**）。
2. **客户（OEM）**：10–50 人的公司，**不可能自建 SMT 线**。它的 VERGE 全系大概率是**台湾/中国大陆 ODM 后贴牌**。⇒ **它是我方最理想的「土耳其品牌 + 中国制造」合作对象**。
3. **合作者**：它的**数据二极管 / NAC / 政企方案**需要配套工业交换 ⇒ **可以配我们的货进它的方案。**

**⇒ 第一句话**：「**VERGE 现在在哪家工厂做？8 口工业那一段我给你补上，贴 VERGE 的牌。**」

---

## 3 · ⭐⭐ 修正：**`XPS Active Systems` = XPcable Group（台北），不是 ONV 贴牌**

**🛑 被推翻的说法（r73/B/010 备注）**：「XPS（XP Active Systems，= ONV 贴牌，用户口径）」。

| 证据 | 内容 |
|---|---|
| 产品 PDF 页脚 | **`XPcable Group · 11F, 51 HENGYANG ROAD, 100 TAIPEI, TAIWAN, R.O.C. · info@xpcable.com`** |
| 品牌关系 | **`XPCABLE`（布线）= `XPS / XP Active Systems`（交换机）= 同一集团**，ErETE 同时代理两者 |
| 产地口径 | 「**生产在台湾，研发在美国加州**」（rocketreach / ErETE 自述）；XPCABLE 持 **ETL / UL / DELTA** 证书 |
| 已确认型号 | **商用**：`XPS-1220-18`（16×GbE + 2 SFP，L2+ 受管，30 W）· `XPS-1220-28P`（24×PoE + 4 SFP，**400 W**）· `XPS-1220-10P`（8×PoE + 2 SFP）<br>**工业非受管**：`XPS-I7100-4 / -6 / -10`<br>**工业受管**：`XPS-I7120-6P / 10P / 14 / 14P（8 PoE，**240 W**，G.8032 ERPS）/ 24 / 24P` · `XPS-I8120-24F / 24PF`（+4×10G SFP+） |
| 交货期 | **4–6 周**（`eretekne.com` 商品页原文） |
| ErETE 的渠道 | **约 200 家「Yetkili Sistem Kurucu」**（授权系统集成商）—— 这是它真正的护城河 |

**⇒ 判读**
- **XPS 是台湾品牌，但产品形态与大陆公模高度接近**（L2+、G.8032、240 W、IP30）⇒ **它大概率也是 ODM 出来的**，只是品牌在台北。
- **它的弱点 = 交期 4–6 周 + 台系价格**。我们的 5–7 天是**可以直接打的**。
- **话术**：「**XPS 那条线，4–6 周太久。同规格我 5–7 天出货，贴 XPS 的牌也行。**」

---

## 4 · ⭐⭐ 顺手两条：BDCOM 是独家；Sec-on 的规格就是我们的靶子

### 4.1 BDCOM 在土耳其是**独家代理**

`bdcom.com.tr` 首页原文：「**Öncü Güvenlik, BDCOM'un Türkiye'deki exclusive distribütörüdür**」，站内 **22 个 switch 型号**，含 `S2900-8T4X`（8 口受管）、`S2900-2T10X` 等。

**⇒ 影响**：**$399 的 BDCOM 工业锚价是「独家代理价」**，不是公开市场价。
**⇒ 报价逻辑**：我们对着**独家代理的零售价**打，而不是对着「中国出厂价」打 —— **这中间的差价比我方成本优势大得多。**

### 4.2 Sec-on `SC-E208-4FH` —— 八口工业 PoE 的**标准靶型**

| 项 | 规格（官网逐字） |
|---|---|
| 端口 | **8 × GbE PoE + 4 × GbE SFP** |
| 管理 | **Layer 2+ 受管** |
| 供电 | **240 W** |
| 温度 | **−40 ℃ ~ +75 ℃（电源除外）** |
| 渠道 | Öncü 官网 + **ASR Teknoloji / ASR Güvenlik Teknolojileri A.Ş.**（也在卖同一型号） |

**⇒ 这条规格 = 我们的靶型**：8×GbE PoE + 4×SFP + 240 W + L2+。**任何客户问「你们有没有」，答这一条。**
⇒ 注意它「**电源除外**」的 −40~75 ℃ 写法 ⇒ 客户会追问电源。**我方可整机 −40~75 ℃，这是差异点。**

---

## 5 · ⭐ 路线补两站

| 站 | 公司 | 价值 |
|---|---|---|
| **İzmir（路线 B 加一站）** | **BİMEL**（全国网络分销，**İzmir 分部 0232 489 0755**；İstanbul 0212 347 7540） | **在伊兹密尔有实体的全国分销商**，一天路线里顺路可加 |
| **Ankara（新增路线 C）** | **Angora Networks**（Söğütözü Via Flat 销售 + Yenimahalle Timko 工厂）+ **GSL**（İlkbahar Mah. 612. Cd. No:9）+ **FS Grup**（Cevizlidere 1243. Sk. No:6/4） | **安卡拉一天：本土厂商 + 头号对手 + DMO 渠道商，三站互距 15 分钟** |

---

## 6 · ⭐⭐ OEM 客户池（正式成表，11 家）

> 判定标准：**有自有品牌 + 有实际进口/贴牌动作**。这一池比代理池更肥：**他们有品牌、有渠道、缺工厂。**

| # | 公司 | 自有品牌 | 城市 / 楼层 | DMO 状态 | 现有上游 | 我方切入点 |
|---|---|---|---|---|---|---|
| 1 | **Angora Networks A.Ş.** ⭐新 | **VERGE** | Ankara / Söğütözü + Yenimahalle 工厂 | 待查 | 疑台/陆 ODM | **「VERGE 的 8 口工业段我给你做」** |
| 2 | **Asya Telekom / ISEE** | **ISEE**（ISS-） | İstanbul / **Perpa B K:7-8-9 No:908** | 未查到 | 132 批 / 5 家供应商 | **补齐工业 / 2.5G / bt** |
| 3 | **HAN Elektronik A.Ş.** | **FOREDGE · VIDEOPARK · SPY · AVer · M-Sight** | İstanbul / Küçükçekmece | **⭐ 在售 10 型号（多家供应商）** | 深圳工厂（未定名） | **「换掉现在那个深圳工厂」** |
| 4 | **Telkolink / GelecekBT** | **CLR**（+ TG-NET 上游） | İstanbul / Perpa A K:5 No:295 | **⭐ K291 活目录 + IEC61850 目录** | **TG-NET（中国）** | **「TG-NET 换一代」** |
| 5 | **Nokta Elektronik A.Ş.** | **upTech** | İstanbul / Perpa B 906-907 + A 841 | 待查 | 自研/贴牌 | **「upTech 的工厂换我」** |
| 6 | **Öncü Güvenlik A.Ş.** | **Sec-on** | İstanbul / Beykoz | 待查 | 自研 + **BDCOM 独家** | **L2+ 240 W 同规格** |
| 7 | **Lansan Teknoloji A.Ş.** | **LNS-** | İstanbul / **Perpa B No:989** | 未查到 | 未定 | **价格（8 口 PoE 它卖 $1,000）** |
| 8 | **Karer Güvenlik** | **KARER / KR-** | İstanbul / Pendik | 待查 | 白牌 | 已在 r73 建档 |
| 9 | **Snexus Networks** | **SN-** | İstanbul | 待查 | 白牌 | 已在 r72 建档 |
| 10 | **Cenova Bilişim** | **Cenova / SWP-/DL-** | İstanbul / Perpa B 902-904 | 待查 | Tiandy + GVD | 已在 r72 建档 |
| 11 | **NOVA Group / Novacom** | **NVC-/NCV-/ND-** | Ankara | 待查 | 白牌 | 已在 r72 建档 |

**⇒ 一句话**：**11 家里 10 家是「有牌没厂」，只有 Angora 声称有厂（且只有 10–50 人）。**

---

## 7 · GSL 目录（本轮只抓了 56/311，先给家族结构）

**已确认的「入门级非受管」家族**（这正是我们最想替换的一层）：
- **Moxa**：`EDS-205`（5 口）· `EDS-208 / 208A / 208A-T / 208A-MM-SC`（8 口）· `EDS-308 / 308-S-SC`（8 口 + 光）· `EDS-316-MM-ST-T`（14 口 + 2 光）· `EDS-2005-ELP / 2008-ELP`（塑料壳入门）· `EDS-P206A-4PoE-S-SC-T`（4 口 PoE + 光，−40~75 ℃）
- **Kyland**：`Opal5 / Opal5L / Opal5-E`（5 口）· `Opal8 / Opal8L / Opal8-E-2S6T`（8 口）· `SICOM3000A-8T / 16T / 2SFP8T / 2GX8GE / 2GX8T`（受管 DIN 导轨）· `SICOM3000A-LITE-2S6T-SC40/ST40`（2 光 + 6 电，40 km）· `SICOM3000S-4GX8P`（4 光 + 8 PoE，IEEE1588，IP30，−40~75 ℃）· `SICOM3307S-3G7P`（3 光 + 7 PoE）· `KIEN1009-3M6T-SC05` · `KIEN7009-2S6T-SDSC40`
- **SFP**：`SFP-1GSXLC / 1GLXLC-T / 1GLSXLC / 1FESLC-T / 1FEMLC-T`
- **Moxa 模块**：`EOM-104`（4 口嵌入式受管，−40~75 ℃）

**⇒ 结论**：**GSL 的产品结构 = 「Moxa 走量 + Kyland 补位 + SFP/模块粘客户」。**
⇒ **Kyland 的 Opal 系列（5/8 口非受管）是它最便宜的一层，也是我们最容易打穿的一层。**

---

## 8 · 证据等级与空白

**逐字来源**：`esatis.dmo.gov.tr` / `dmo.gov.tr` / `dmo.tr` 产品页（TeleOne K2887 四条、FOREDGE 十条、PLANET、D-LINK、HPE、HUAWEI 对照）· `docplayer.biz.tr`（**DMO ÜRÜN KATALOĞU -K291** 全文，含 CLR 型号与 TG-NET 并列）· `telkolink.com/tr/katalog.html`（CLR 型号表）· `dmo.gov.tr/EMagaza/Magaza/Standart/1145171`（**FS Grup K4702，44 产品**）· `fsgrup.com.tr`（地址/电话/成立）· `angoranetworks.com` + `/contact` + `/verge-network-switch-family`（地址/电话/产品）· `find.com.tr`（Angora 法定名与成立日）· `linkedin`/`crunchbase`/`rocketreach`（规模）· `erete.com.tr` PDF + `xp-networks.com` PDF（**XPcable Group 台北地址与 XPS 型号**）· `eretekne.com`（XPS 全型号与 4–6 周）· `rocketreach`（ErETE: XPCable 代理、ETL/UL/DELTA、台湾生产/加州研发）· `bdcom.com.tr`（**独家代理原文**）· `oncuguvenlik.com.tr` + `asrteknoloji.com.tr`（SC-E208-4FH 规格）· `store.gsl.com.tr`（56/311 SKU）· `bimel.com.tr`（İzmir 分部电话）。

**空白（诚实标注）**
1. **GSL 的 311 个 SKU 只抓了 56 个**（约 18%）—— 剩余 255 个未取。
2. **FOREDGE 在 DMO 的完整供应商名单**（除 K4702 外还有数家未标码的挂价方）。
3. **TeleOne 是否已续签新的 DMO 合同**（K2887 页面只显示 2021–2023；是否换号未知）。
4. **Angora Networks 的工厂是「组装」还是「贴牌」** —— 官网称 manufacturer，但 10–50 人无 SMT 证据；**未取到工商资本额与设备清单**。
5. **Angora 的 DMO K 码未查**（若它有 DMO 目录，会是最重要的一条）。
6. **`CLR` 与 `TG-NET` 的具体贴牌关系**（同目录并列 ≠ 同一工厂）。
7. **TeleOne 的 K2887 合同金额与年销量**未取。
8. **所有电话仍未试拨。**

---

## 9 · r77 建议（按价值排序）

1. **🔥 抓完 GSL 的 311 个 SKU**（还剩 9 页）—— 这是土耳其工业交换机的完整型号地图，一次抓完入库。
2. **🔥 反查 Angora Networks 的 DMO K 码** —— 若它在 DMO 目录里，「本土制造商」这一档是它的王牌，必须知道它的价格。
3. **🔥 把 11 家 OEM 客户按「现有上游」排序** —— 已知上游的只有 Telkolink（TG-NET）与 Han（深圳工厂）；其余 9 家全部空白。
4. **反查其余客户的 K 码**：Nokta/upTech、Öncü/Sec-on、Karer、Snexus、Cenova、Novacom、CIS（若在册）。
5. **Ankara 路线 C 落地**：Angora（Söğütözü）+ GSL（İlkbahar）+ FS Grup（Cevizlidere）。
6. **TeleOne 的 DMO 续签状态**（打电话问一句即可）。
7. **`ASR Teknoloji`**（在卖 Sec-on 的第二家）建档 —— 可能是 Öncü 的分销商，也可能是独立渠道。
