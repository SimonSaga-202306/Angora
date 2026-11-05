# -*- coding: utf-8 -*-
"""r52 补录（2026-11-01）：Telkolink/GelecekBT 全目录点算（推翻 116 多行）+ CryptoLink 品牌归属推翻 + TGD 24V 被动 PoE 切入点。"""

D = {}

# ---------------- A / 001 Telkolink + GelecekBT ----------------
D['1'] = """
### ⭐⭐⭐ r52：**它是我方在土耳其最强的对手，不是最好的客户** —— 全目录点算 + 三项自我证伪

把 `gelecekbt.com/anahtarlar` 全目录（含 facet）点完，结论**与此前所有判断相反**：

#### A. 目录规模（原文 facet）
| 分类 | SKU | 分类 | SKU |
|---|---|---|---|
| Ethernet Switch | **122** | Ethernet POE Switch | **126** |
| Endüstriyel Switch | **73** | Endüstriyel POE Switch | **60** |
| Endüstriyel Omurga | **10** | Omurga Fiber Switch | **57** |
| 10Gigabit Switch | **104** | **Multirate Switch（1G/2.5G/10G）** | **15** |
| SFP Modül | **112** | **POE Switch AI** | **22** |
| PD POE Switch | 7 | | |
→ **交换机全目录 ≈ 291 个 SKU**，25 个品牌，其中**自有可贴牌品牌 `CLR Networks` 占 193 个**。

#### B. ⭐ 品牌真相：**CLR 是它代理的深圳品牌，不是它的自有商标**
- 它自己的幻灯片写明：**「CLR Networks Türkiye dağıtıcısı GelecekBT'dir」**（GelecekBT 是 CLR 的土耳其分销商）。
- `guvenlikonline.com` 企业页：**「CLR Networks、ONET、Telkolink、Netkablo gibi markaların Türkiye dağıtıcısıdır」**。
- → **改写**：本档此前记的「自有品牌 CLR Networks（深圳品牌）」应更正为 **「代理/独家分销的深圳品牌」**；**它同时代理 D-Link / Huawei / HP-Aruba / Netgear / Fortinet / Zyxel / Cisco / TG-NET / Repotec / Planet / Moxa / Advantech / 3Onedata / Kyland / Hirschmann / Harting / Siemens / Schneider / Allied Telesis / Axis / Ruijie**（facet 原文）。

#### C. ⭐⭐ 三项自我证伪（直接推翻 `116` 的三行）

| `116` 原判断 | 本档实测 | 结论 |
|---|---|---|
| **2.5G：11 家 0 家** | ❌ **它有整条 2.5G 线**：`CLR-MRS-8106N`(5×2.5G+1×10G SFP)、`-8106P`(4×2.5G PoE+1+1)、`-8109N`(8×2.5G+1×10G)、`-8109P`(8×2.5G **PoE**+1×10G, 100 W)、`-8218N`(16×2.5G+2×10G, Web 管理)、`-8226N`(**24×2.5G**+2×10G)、`-8312N/P`(8×2.5G + 2×10G RJ45 + 2×10G SFP+ **L3**)、`-8330N/P`(**24×2.5G PoE + 6×10G SFP L3**)、`CLR-SWT-80F`(8×1.25/2.5/10G SFP+)；**另有 `CLR-DCS-2110N/P` = 24×2.5G + 100G 上联 L3** | **2.5G 不是空白，是"已被它做满"** |
| **bt：只有 1–4 口** | ❌ facet 原文：**`POE Tip3 (802.3bt) 60W` = 3 个**、**`POE Tip4 (802.3bt) 90W` = 1 个**、**`IEEE 802.3bt` = 6 个**；`CLR-SWF-9006BT` 单机 **96 W** | **bt 也已覆盖到 90 W 单口** |
| **云管理：0 家** | ❌ facet **`Cloud` = 15 个**、**`Yapay Zeka (AI)` = 12 个**；`CLR-SWT-5736F`、`CLR-SWT-3754F` 均标 **L3 Cloud** | **云也已在线** |
| **40/100G：0 家** | ❌ facet **100G 上联 6 个 / 100G Uplink 交换机 9 个 / 400G 1 个**；`CLR-DCS-6332F`/`6432F` = **32×40/100G QSFP28** | **它已经在卖 100G/400G 数据中心机** |

→ ⭐ **结论：`116` 的"六行缺口矩阵"对 Telkolink/GelecekBT 完全不成立。它是全名单里技术水位最高的一家，也是我方最直接的对手**（同为深圳 ODM、同一客群、同一货架）。

#### D. 那它还有什么缺口？（真正的我方机会）
1. **`CLR-MRS` 的 2.5G PoE 线功率偏小**：`-8109P` 只有 **100 W**、`-8106P` 未标大功率；**24 口 2.5G PoE（`-8330P`）无功率标注** → 我方 **`EW-PIS5728GM-AP-BT`（24 口 bt / 800 W）/ 2.5G + bt 组合** 仍有一档。
2. **工业 bt 几乎空白**：它 73 个工业款里 `802.3bt` 只有 6 个（含商用），**工业 90 W 单口只有 1 个** → 我方 `EW-PIS3810M-8GE-BT` / `EW-PIS5728GM-AP-BT` 可补。
3. **`POE Extend` 只有 18 个、`POE Watchdog` 14 个**（291 个 SKU 里）→ 我方 **300 m 拨码 + Watchdog 全系标配** 是"低成本高感知"的差异点。
4. ⭐ **SFP 模块 112 个 SKU** 是它的现金牛之一 → 我方 **2.5G SFP / 10G SFP+ / 工业 SFP** 可直接对位供货（`EW-810GS-20`、`EW-10GSFP-SR`）。

#### E. 打法定稿（**彻底改写**）
| 之前（错） | 现在（对） |
|---|---|
| "它缺 2.5G / bt / 云，我方去补位" | ❌ **它全都有**。改口：**"同一档位、更低的 ODM 成本 + 可贴 CLR 牌"** |
| 当作"客户" | ⚠ **一半是客户、一半是竞对**（CLR = 同样的深圳供应链）。**不要一次交出完整 BOM 与成本结构** |
| 谈"技术领先" | ✅ 谈 **交期、MOQ、贴牌弹性、2.5G+bt 组合、SFP 整套齐套供货** |

**首封主题**：`CLR hattı için ikinci kaynak: 2.5G PoE + 802.3bt (60/90W) + SFP 套件`
**必问三句**：① `CLR` 是不是你们独家？② 2.5G 那条线今年走多少台？③ 工业 90 W bt 有没有客户在问？

### 证据等级（r52）
- 已核实：**11 个分类的 SKU 数、25 个品牌清单、全部 facet 计数**（`gelecekbt.com/anahtarlar?limit=100` 原文）、**CLR 为代理品牌的原文表述**（自家 slideshare + guvenlikonline）、**CLR-MRS 全 10 个型号名与端口**、**CLR-DCS-2110/6332/6432**。
- 仍空白：**CLR 独家性条款**、各型号实际销量、CLR 的深圳工厂名（与我方是否同厂未知）。
"""

# ---------------- A / 005 CryptoLink ----------------
D['5'] = """
### ⭐⭐ r52：`CRL` 不是它的自有品牌 —— 每份 datasheet 页脚都印着 **"Authorized Dealer"**

把官网 7 份 PDF 打开后，**版式给出决定性证据**：
- 每份 datasheet 的页脚都是 **`CryptoLINK.  Authorized Dealer | Cryptolink Elektronik Güvenlik Sistemleri San ve Tic. Ltd. Şti`**；
- `CRL-SW-2402` 的 PDF 页眉里出现 **`Cryptol.net`** 的 logo 字样 → **`CRL` 品牌属于第三方（深圳 Cryptol 系），CryptoLink 是"授权经销商"**。

→ **改写**：本档此前记的「CRL 线 7 份 datasheet 实锤 … switch+SFP+MC 全自有」应更正为 **"CRL 为代理品牌（Authorized Dealer），非自有商标"**。
→ 与 `Cifocs`（Cebeci）、`CLR`（GelecekBT）**同一模式**：土耳其渠道**普遍用"引入的深圳品牌 + 本地化文档"充当自有品牌**。**这条规律适用于全部 A 档判断：凡"自有品牌"必须先查商标，否则一律按代理处理。**

#### 型号与规格（datasheet 原文）
| 型号 | 端口 / 规格 |
|---|---|
| ⭐ **`CRL-SW-L3-2404-10G`** | **24×10/100/1000 PoE + 8×Combo TP/SFP + 4×10G SFP+ + 1 Console**；**BCM 芯片**；**128 Gbps / 96 Mpps**；MAC 12K；**总功率 360 W**；**af/at 仅 30 W**；ARM Cortex-A9 / 256 MB；**L3 = 静态路由 + RIP + OSPF + VRRP**；−20~50 °C；444×360×44 mm；CE/FCC/RoHS/CCC |
| （变体）`CRL-SW-L3-2404-10G-8C` | **24×1000M SFP + 8 Combo + 4×10G**（全光版） |
| （变体）`CRL-SW-L3-2404-10G-8C-POE` | **24×GE PoE + 8 Combo + 4×10G** |
| **`CRL-SW-2402`** | 24×100/1000 **PoE**（af/at 15.4/30 W）+ **2×SFP**；52 Gbps；MAC 8K；**总 300 W**；**VLAN/Trunk 模式**；1–8 口 QoS；**防雷 6 kV / 差模 4 kV / ESD 15 kV**；−20~50 °C |
| `CRLISW-08` / `CRLISW-14P` | 工业款（8 口 / 8 口 PoE + 上联） |
| `CRL-SFP-10G-LC` / `CRL-SFP-125 LC` | 10G / 1.25G 光模块 |
| `CRL-MC02` | 媒体转换器 |

#### 与我方对位
| 它的型号 | 我方对位 | 差在哪 |
|---|---|---|
| `CRL-SW-L3-2404-10G`（24 PoE + 8 Combo + 4×10G，**360 W**，af/at） | ⭐ **`EW-S2926GM-AP`**（24 PoE + 4 Combo + 2 SFP）/ 升级 **`EW-S5748GM-AP`**（48 PoE + 4×10G） | 我方**48 口同档**、且可上 **bt 60 W** |
| `CRL-SW-2402`（24 PoE + 2 SFP，300 W） | **`EW-S1927CG-AP`**（24 PoE + 1 SFP + 1 RJ45）/ `EW-S2926GM-AP` | 我方上联更多 |
| `CRLISW-14P`（工业 8 PoE） | **`EW-PIS1810-8GE`** / `EW-EPIS3910-8GE` | 我方**12/24 V 被动 + 云** |

**⭐ 它的客户群是"边界安全 / 车牌识别 / 政府项目"**（官网四大业务：Sınır Güvenliği、Siber Güvenlik、Network、Plaka Tanıma）→ 因此**工业宽温、冗余电源、防雷**比"云"重要。首封就谈这两条。
**首封主题**：`CRL yerine ikinci kaynak: 802.3bt 60W + 工業 -40°C + 48 port`
**必问三句**：① CRL 是独家经销吗？② 车牌/边界项目里 PoE 年用量？③ 工业款要不要 -40 °C 与双电源？

### 证据等级（r52）
- 已核实：**7 份 datasheet 中的 2 份完整规格**（`CRL-SW-L3-2404-10G`、`CRL-SW-2402`）、**"Authorized Dealer" 页脚（全部 7 份同版式）**、**Cryptol.net 字样**。
- 仍空白：`CRLISW-08/14P` 详细规格（有 PDF 未读）、CRL 商标真实持有人、它是否也卖别家交换机。
"""

# ---------------- A / 054 TekniksatGroup ----------------
D['54'] = """
### ⭐ r52：TGD 的 PoE 线是**给自家 IP 对讲系统配套**的，而它用的正是 **24 V 被动 PoE**

#### A. TGD PoE 型号全表（官网英文类目 + 产品页原文）
| 型号 | 规格 | 电压制式 |
|---|---|---|
| **`TGD-P4/24`** | 4+2「4FEP + 2FE」PoE，**1,2+ / 3,6−** | **24 V 被动** |
| **`TGD-P8S/24`** | 8 口 PoE（+2 上联） | **24 V 被动** |
| `TGD-P4/48` | 4 口 PoE | 48 V |
| `TGD-P8/48` | 8 口 PoE | 48 V |
| **`TGD-P16S/48`** | 16 口 PoE | 48 V |
| **`TGD-P24S/48`** | 24 口 PoE | 48 V |
| `TGD-P424` / `TGD-P824` / `TGD-P848` | 早期 4/8/8 口 PoE（产品页仍在） | — |
| `[SWITCH]` | **5 口 10/100 非网管** | — |

#### B. ⭐ 决定性上下文：它的主体业务是 **IP 对讲**，不是网络
官网同目录里并列的是 `TGD-7IP24 / TGD-7IP48`（7 吋 **IP 对讲**主机）、`TGD-4K24`（IP 门面板）、`TGD-GU10 S1`（10.1 吋安防单元）、`TPS 9/x`（多开关）、`TGR/TPB`（电视/卫星分配）。
→ **这些 TGD PoE 交换机是给「Villa IP Kapı Paneli + 24 V 对讲」做配套供电的**，所以：
- **24 V 被动 PoE 是它的刚需**（对讲主机普遍 24 V 被动）；
- 它的交换机**全是低端非网管**，没有"网管 / 云 / 远程重启"这一层；
- 它自述 **「Üretim tasarım uygulama %100 yerli」**（生产设计 100% 本土）→ **对"这是谁做的"很敏感**，谈 OEM 要先谈"贴 TGD 牌、你方负责本地化文档与保修"。

#### C. ⭐ 与我方的**一对一对位（本轮最干净的一次）**
| 它的型号 | 我方对位 | 为什么是我方最强一刀 |
|---|---|---|
| `TGD-P4/24`（4 口 **24 V 被动**） | ⭐ **`EW-EPIS3910-8GE`**（**1–2 口 DIP 选 12V/24V 被动 PoE**、3–6 口 48V 30 W、7–8 口 48V 60 W、**云管理**、**单端口远程重启**） | **一台同时覆盖 24 V 被动 + 48 V 标准 + 云**，它要用三台机才凑得齐 |
| `TGD-P8S/24` | 同上 | 同上 |
| `TGD-P8/48`（8 口 48 V） | `EW-S1710FG-AP`（8 GE PoE + 2 SFP） | 加 **300 m 长距 + Watchdog** |
| `TGD-P16S/48` | `EW-S1616CGU` / `EW-PIS3620M-16GE`（工业 16 口） | 可上工业宽温 |
| `TGD-P24S/48` | `EW-S1927CG-AP` / `EW-S2926GM-AP`（网管） | 网管 + bt |
| `[SWITCH]` 5 口非网管 | `EW-S1805` 系 | — |

**⭐ 一句话卖点（对讲场景专用）**：**"对讲主机死机时不用上门——云平台点一下重启那个口。"** 这是它现在整条 TGD 交换机线**完全没有**的能力，而对讲/门禁是最需要远程重启的场景。

**首封主题**：`TGD 24V pasif PoE switch hattı: tek cihazda 12/24V pasif + 48V + uzaktan port reset`
**必问三句**：① 24 V 对讲那条线一年多少台？② 交换机是自产还是外协？③ 要不要把"远程重启"作成 TGD 的卖点？

### 证据等级（r52）
- 已核实：**8 个 TGD PoE 型号名与电压制式**（`en.tekniksatgroup.com.tr/kategori/poe-switch` + 产品页）、**IP 对讲生态型号（`TGD-7IP24/7IP48`、`TGD-4K24`、`TGD-GU10 S1`）**、**"100% yerli" 自述**。
- 仍空白：**TGD 交换机是自产还是外购贴牌**（关键）、年量、是否已有网管型号。
"""
