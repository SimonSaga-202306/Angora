# -*- coding: utf-8 -*-
"""r76 附录数据：DMO K 码价格地图 + 土耳其本土交换机厂 + XPS 身份订正。"""

D = {}

D['1'] = """
#### r76 补：**它在 DMO 有一个活目录 —— K291**

| 项 | 内容 |
|---|---|
| **DMO 供应商码** | **K291**（目录文件标题即 **`DMO ÜRÜN KATALOĞU -K291`**） |
| DMO 批准 | **2018-08-03，文号 55238** |
| **进目录的 CLR 自有型号** | `CLR-SW-811P`（8×10/100 PoE + 2 GbE SFP 非受管）· `CLR-SWG-822P`（8×100M PoE + 2 Combo）· `CLR-SWG-1621P`（16 口 PoE）· `CLR-SWF-2422P`（24×100M PoE + 2 GbE）· `CLR-IES-G42P`（4×GbE + 2 SFP 工业非受管 PoE）· `CLR-IES-G82P`（8×GbE PoE + 2 SFP 工业非受管）· `CLR-IES-G802P`（8×RJ45 PoE + 2 SFP **受管**）· `CLR-IES-G824P`（14 口受管）· `CLR-IES-T884P`（**DIN 导轨 24 口 10G L2+ 骨干 PoE**）· `CLR-SWG-28`（8 SFP + 2 GbE 骨干）· `CLR-SWT-4244`（光纤骨干 L2+）· `CLR-FXS/FXO` 电话光端机 · `CLR-VTR` 模拟视频光端机 · `CLR-MCT-SFP+` 10G 转换器 · `CLR-PSE-100` PoE 注入器 |
| **⭐ 底牌** | **同一份目录里并列出现 `TG-NET` 的 PoE 交换机**（`P3010M-8POE` 150 W、`P3018M-16POE` 300 W、`P1000` 系列、`S5500` L3 骨干）⇒ **TG-NET（中国 ODM）就是 CLR 的上游** |
| **⭐ 另一本目录** | **`IEC61850 Ethernet switch`** —— 它已经能做电力标 |

⇒ **A 级第一名手里握着一个活的 DMO 目录（K291）+ 一本 IEC 61850 目录 + 一条中国 ODM 上游。**
⇒ **话术**：「**TG-NET 那条线，我给你换一代：千兆 PoE + 802.3bt + 环网 G.8032，规格直接进你 K291 的下一版。**」
"""

D['8'] = """
#### r76 补：**FOREDGE 在 DMO 有 10 个型号 —— 这是「白牌层价格伞」最硬的一张表**

| FOREDGE 型号 | 规格 | DMO 价（₺ 未税） | 折 USD | 价差 |
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

（DMO 产品码段 **`119852`–`119881`**；同一型号由**多家供应商**挂价）

**⇒ 三条判读**
- **一台「8 口工业千兆 PoE 240 W」在政府目录里卖 $898–1,155**；而国际大牌的**地板价**是 **PLANET `IGS-801T`（8 口工业非 PoE）8,346.59 ₺ ≈ $167**。
- **28.6% 的价差不是成本差，是渠道差** —— 同一台机器，不同供应商挂两个价。**谁拿到更低工厂价，谁就吃下那个 28.6%。**
- **FOREDGE 的规格已经接近我们**（GbE + SFP + 240 W + 云管理）⇒ **对标不是 Moxa，是这一栏。**

**⭐ 下游渠道样本：FS Grup Bilişim Ltd. Şti.（DMO K4702）**
2017 年成立 · **Cevizlidere Mah. 1243. Sok. No:6/4, Öveçler / Çankaya / Ankara** · **0312 473 32 00**（Faks 473 32 01）· `fsgrup.com.tr` · DMO 目录 **44 个产品**：**FOREDGE 全部交换机**（`119853-K4702` … `119881-K4702`）+ **MILESIGHT** 摄像机/VMS + **AXXON** 视频软件。
⇒ **它不生产，它把 Han 的 FOREDGE 挂进 DMO（且价常低于同行，在打价格）**。**要找的不是它，是它上游的工厂 —— 也就是我们。**
"""

D['9'] = """
#### r76 补：**BDCOM 是「独家代理」；Sec-on `SC-E208-4FH` 是我们的靶型**

**① BDCOM 独家**
`bdcom.com.tr` 首页原文：「**Öncü Güvenlik, BDCOM'un Türkiye'deki exclusive distribütörüdür**」；站内 **22 个 switch 型号**（`S2900-8T4X` 8 口受管、`S2900-2T10X` 等）。
⇒ **$399 的 BDCOM 工业锚价是「独家代理价」，不是公开市场价。** 我们对着**独家代理的零售价**打，差价比我方成本优势大得多。

**② Sec-on `SC-E208-4FH` 完整规格（官网逐字）**

| 项 | 规格 |
|---|---|
| 端口 | **8 × GbE PoE + 4 × GbE SFP** |
| 管理 | **Layer 2+ 受管** |
| 供电 | **240 W** |
| 温度 | **−40 ℃ ~ +75 ℃（电源除外）** |
| 同型号第二渠道 | **ASR Teknoloji / ASR Güvenlik Teknolojileri A.Ş.** |

⇒ **8×GbE PoE + 4×SFP + 240 W + L2+ = 我们的靶型。**
⇒ **差异点**：它写「电源除外」，**我方可整机 −40~75 ℃** —— 客户一定会追问电源这一条。
"""

D['10'] = """
#### r76 补：**XPS 身份解开 —— 是台北 XPcable Group，不是 ONV 贴牌**

**🛑 修正 r73（B/010 备注）**：被推翻的说法「**XPS（XP Active Systems，= ONV 贴牌，用户口径）**」。

| 证据 | 内容 |
|---|---|
| 产品 PDF 页脚 | **`XPcable Group · 11F, 51 HENGYANG ROAD, 100 TAIPEI, TAIWAN, R.O.C. · info@xpcable.com`** |
| 品牌关系 | **`XPCABLE`（布线）= `XPS / XP Active Systems`（交换机）= 同一集团**，ErETE 同时代理两者 |
| 产地口径 | 「**生产在台湾，研发在美国加州**」（ErETE/rocketreach）；XPCABLE 持 **ETL / UL / DELTA** 证书 |
| **已确认型号** | 商用：`XPS-1220-18`（16×GbE + 2 SFP，L2+，30 W）· `XPS-1220-28P`（24×PoE + 4 SFP，**400 W**）· `XPS-1220-10P`（8×PoE + 2 SFP）<br>工业非受管：`XPS-I7100-4 / -6 / -10`<br>工业受管：`XPS-I7120-6P / 10P / 14 / 14P`（8 PoE，**240 W**，**G.8032 ERPS**）/ `24 / 24P` · `XPS-I8120-24F / 24PF`（+4×10G SFP+） |
| **交货期** | **4–6 周**（`eretekne.com` 商品页原文） |
| **ErETE 的护城河** | **约 200 家「Yetkili Sistem Kurucu」**（授权系统集成商） |

⇒ **XPS 是台湾品牌，但产品形态与大陆公模高度接近**（L2+ / G.8032 / 240 W / IP30）⇒ 它大概率也是 ODM 出来，只是品牌在台北。
⇒ **弱点 = 交期 4–6 周 + 台系价格。**
⇒ **话术**：「**XPS 那条线，4–6 周太久。同规格我 5–7 天出货，贴 XPS 的牌也行。**」
"""

D['22'] = """
#### r76 补：**DMO 反查到了它的供应商码 K2887 —— 而且是僵尸码**

**method**：DMO 产品页正文含 **`产品码-K供应商码`**、单价（+Vergiler）、含税价、**合同起止**。

| 型号 | 品名 | DMO 价（未税） | 含税 | ≈USD |
|---|---|---|---|---|
| **`BRICKCOM PS-7242IL-AT`** | **24 口 10/100 PoE+ Web Smart 交换机** | **14,645.16 ₺** | — | **≈$293** |
| `BRICKCOM NR-8232-RM-D` | 32 路 IP NVR | 39,501.00 ₺ | 46,611.18 ₺（KDV 18%） | ≈$790 |
| `BRICKCOM OB-H200NP-WDRPRO-H265` | 枪机 2MP | 10,534.01 ₺ | 12,430.13 ₺ | ≈$211 |
| `BRICKCOM VD-300NP-VIA` | 半球 3MP | — | — | — |
| `LANDE LN-SBO-IP5509U6060-LG` | 室外机柜 | 5,088.39 ₺ | — | ≈$102 |

**⭐ 关键：供应商码 K2887，合同 2021-09-09 → 2023-09-09（已过期），页面状态「temin edilememektedir（无法供货）」**

**🛑 修正 r75（B/022）**：被推翻的说法是「**2014 年起进 DMO，自述本领域前三**」给人的「现在仍在册」印象 —— **实际上它最后一个可见合同在 2023-09-09 已到期**。**它是 DMO 的历史玩家，不是当下玩家。**

⇒ **三条判读**
- 它**确实卖过交换机**（`PS-7242IL-AT`，美国挂牌 $1,113，DMO 折 $293）⇒ **交换机品类是通的，只是靠 Brickcom 供**。
- **BRICKCOM 是台湾品牌，型号老**（10/100、Web Smart）⇒ **DMO 目录里没有一台「千兆 + 802.3at + 工业」的 TeleOne 货。这一格是空的。**
- **谈的时候第一句就问**：「**你的 DMO 合同 2023 年 9 月就到期了，新一期准备放什么型号？**」—— 这句话能立刻把它从「客套」拉到「要不要一起报下一期」。
"""

D['62'] = """
#### r76 补：**DMO 价格地图打通 + 土耳其本土交换机厂 + XPS 身份解开（本轮要点）**

> 用户第 29 次「继续」。完整版见 `145-dmo-price-map-and-turkish-switch-maker-2026-11-06.md`。

**① ⭐⭐⭐ DMO 反查方法成立：`供应商 K 码 → 品牌 → 单价 → 合同起止`**

| 客户 | DMO K 码 | 状态 | 已抓到的在售 |
|---|---|---|---|
| **TeleOne** | **K2887** | **僵尸（2021-09-09 → 2023-09-09，无法供货）** | BRICKCOM 交换机 14,645.16 ₺（≈$293）/ NVR 39,501 ₺ / 相机 10,534.01 ₺ / LANDE 机柜 5,088.39 ₺ |
| **Telkolink / GelecekBT** | **K291** | **活目录（2018-08-03 批准，文号 55238）** | **CLR 全线 15+ 型号**（`CLR-IES-G42P/G82P/G802P/G824P`、`CLR-IES-T884P` 24 口 10G 骨干 PoE、`CLR-SWG-28` 8 SFP 骨干…）+ **TG-NET 并列**（CLR 的中国 ODM 上游）+ **IEC61850 目录** |
| **Han Elektronik（FOREDGE）** | 多家（含 **K4702 FS Grup**） | **活，10 个型号** | 见下 |
| **FS Grup Bilişim** | **K4702** | 活，44 产品 | FOREDGE 全系 + MILESIGHT + AXXON |

**② ⭐⭐⭐ 价格伞硬数：8 口工业千兆 PoE 在 DMO 卖 $898–1,155**

| 型号 | 规格 | ₺ | ≈USD |
|---|---|---|---|
| **FOREDGE `IS108GPS-2F`** | **工业 8×GbE + 2 GbE SFP，240 W** | **44,928.91 – 57,784.04** | **$898–1,155** |
| FOREDGE `IS104GPS-2F` | 工业 4×GbE + 2 SFP，120 W | 34,944.71 – 44,943.14 | $699–898 |
| FOREDGE `S5700-24GP-4TFR` | 24×GbE PoE 360 W + 4×10G | 62,401.27 – 80,255.62 | $1,248–1,604 |
| FOREDGE `AI1016GC` | 16×GbE + 2 SFP，250 W 云管理 | 43,554.16 – 48,153.37 | $871–963 |
| **PLANET `IGS-801T`** | 8 口工业**非** PoE | **8,346.59** | **≈$167** |
| D-LINK `DGS-3000-52X` | 48 口 L2+ | 35,179.47（KDV20%） | ≈$703 |
| HPE `JG932A`（5130 24G） | 24 口 | 19,993.19（KDV18%） | ≈$400 |

⇒ **同一型号不同供应商价差最高 28.6%（`AI8024` 甚至 126%）—— 这是渠道差，不是成本差。**
⇒ **DMO 的「工业 8 口」价格带 $167 → $1,155，我们的位置在中间，空间极大。**

**③ ⭐⭐⭐ 土耳其有自己的交换机厂：Angora Networks**

| 项 | 内容 |
|---|---|
| 法定全称 | **ANGORA NETWORKS BİLİŞİM TEKNOLOJİ TİCARET SANAYİ ANONİM ŞİRKETİ** |
| 成立 | **2016-11-28**（NACE 620902） |
| 销售 / 制造 | **Nergiz Sok. No:7 K:3 Via Flat / Plaza Cubes, Söğütözü / Ankara** · **Çamlıca Mah. Anadolu Blv. Timko Sk. Z Blok No:20/1, Yenimahalle / Ankara 06200** |
| 电话 / 邮箱 | **+90 312 241 77 47** · `sales@angoranetworks.com` |
| 人数 | **10–50** |
| 口号 | **「Yerli Akıl, Küresel Teknoloji」** |
| 产品 | **VERGE 交换机家族**（8/24/32/48×GbE + 4×10G，受管）· SFP · 瘦客户机 · **数据二极管「Arrow」（支持 ModBUS / OPC）** · WiFi/VoIP · PacketFence NAC |

⇒ **三种可能都成立**：① **对手**（「本土制造商」在 DMO 评级里是加分项）；② **OEM 客户**（10–50 人不可能自建 SMT 线，VERGE 大概率台/陆 ODM 贴牌）；③ **合作者**（数据二极管方案需要配套工业交换）。
⇒ **第一句话**：「**VERGE 现在在哪家工厂做？8 口工业那一段我给你补上，贴 VERGE 的牌。**」

**④ ⭐⭐ 两条身份订正**
- **`XPS Active Systems` = XPcable Group（台北 11F, 51 HENGYANG ROAD, 100 TAIPEI）**，与 XPCABLE 布线同一集团 ⇒ **不是 ONV 贴牌**（推翻 r73）；型号 `XPS-1220-18/28P/10P`、`XPS-I7100-4/6/10`、`XPS-I7120-6P/10P/14/14P/24/24P`、`XPS-I8120-24F/24PF`；**交期 4–6 周**；ErETE 有 **~200 家授权系统集成商**。
- **BDCOM 在土耳其是「独家」**：`bdcom.com.tr` 原文「Öncü Güvenlik, BDCOM'un Türkiye'deki **exclusive** distribütörüdür」，22 个型号 ⇒ **$399 是独家代理价，不是市场价。**

**⑤ ⭐ Sec-on `SC-E208-4FH` = 我们的靶型**
**8×GbE PoE + 4×GbE SFP · L2+ 受管 · 240 W · −40~+75 ℃（电源除外）**；第二渠道在卖的是 **ASR Teknoloji A.Ş.**。
⇒ 差异点：**它「电源除外」，我方整机 −40~75 ℃。**

**⑥ ⭐ 路线补站**
- **İzmir 路线 B 加一站**：**BİMEL**（İzmir 分部 **0232 489 0755**；İstanbul 0212 347 7540）。
- **新路线 C · 安卡拉一天**：**Angora Networks（Söğütözü 销售 + Yenimahalle 工厂）+ GSL（İlkbahar Mah. 612. Cd. No:9）+ FS Grup（Cevizlidere 1243. Sk. No:6/4）**，三站互距 15 分钟。

**⑦ ⭐⭐ OEM 客户池正式成表：11 家**
**Angora Networks（VERGE）· Asya/ISEE · HAN（FOREDGE/VIDEOPARK/SPY/AVer/M-Sight）· Telkolink（CLR，上游 TG-NET）· Nokta（upTech）· Öncü（Sec-on）· Lansan（LNS-）· Karer（KR-*）· Snexus（SN-）· Cenova（SWP/DL）· Novacom（NVC-）**
⇒ **11 家里 10 家「有牌没厂」，只有 Angora 声称有厂（且只有 10–50 人）。**

**⑧ GSL 目录进度：56/311**
家族结构已明：**Moxa** `EDS-205/208/208A/308/316/2005-ELP/2008-ELP/P206A-4PoE` + `EOM-104` 模块；**Kyland** `Opal5/Opal5L/Opal5-E`、`Opal8/Opal8L/Opal8-E-2S6T`、`SICOM3000A-8T/16T/2SFP8T/2GX8GE/2GX8T`、`SICOM3000A-LITE-2S6T-SC40/ST40`、`SICOM3000S-4GX8P`（IEEE1588）、`SICOM3307S-3G7P`、`KIEN1009-3M6T-SC05`、`KIEN7009-2S6T-SDSC40`；**SFP** `SFP-1GSXLC/1GLXLC-T/1GLSXLC/1FESLC-T/1FEMLC-T`。
⇒ **Kyland 的 Opal 系列（5/8 口非受管）是它最便宜的一层，也是我们最容易打穿的一层。**

**证据等级**：DMO 产品页 + `docplayer` 的 K291 目录全文 + `fsgrup.com.tr` + `angoranetworks.com` + `erete/xp-networks` PDF + `bdcom.com.tr` + `oncuguvenlik/asrteknoloji` + `store.gsl.com.tr` + `bimel.com.tr`，均逐字。
**空白**：GSL 只剩 **255/311 未抓** · FOREDGE 的完整供应商名单 · **TeleOne 是否已续签新 K 码** · **Angora 的工厂是组装还是贴牌** · **Angora 的 DMO K 码未查** · CLR↔TG-NET 贴牌关系 · **所有电话仍未试拨**。
"""
