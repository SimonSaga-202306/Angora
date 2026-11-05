# -*- coding: utf-8 -*-
"""r48 补录（2026-11-01）：第二轮抓站后的修正与新证据，追加到既有 A/B 档案文末。"""

D = {}

# ---------------- A / 053 Winet：重大重构 ----------------
D['53'] = """
### ⭐ r48 重构：Winet 不是"自有品牌网络设备商"，而是 **Mikrotik / Ubiquiti 的 WISP 渠道商**（自有 WINET 只是其 one-brand）

**依据**：`wi.com.tr` 的「Brands」页逐条列出 30 个品牌及 SKU 数——
**Mikrotik 473 · WINET 426 · Ubiquiti 319 · Ruijie 40 · Mimosa 29 · Huawei 25 · WiPOINT 24 · VSOL 23 · GMT Control 23 · Mean Well 20 · RF Elements 18 · NetElastic 18 · S-Link 17 · TP-Link 16 · DeltaLink 9 · DMA-SOFT 6 · Everest 6 · Paessler 4 · RedLine 3 · Extralink 3 · Xiaomi 3 · Tenda 3 · Compex 2 · Juniper 1 · Pisces 1**（另有 Teltonika / Cambium / IgniteNet / InfiNET / Nexans 挂 0）。

**这组数字的含义（重要）**
- **Mikrotik 473 + Ubiquiti 319 = 792 个 SKU**，"无线 ISP（WISP）"才是它的主战场；**WINET 426** 是自家 house brand，覆盖天线、RF、PoE、配件与少量交换机。
- 有 **VSOL 23（GPON）** 与 **WiPOINT 24（Hotspot）** → 它做**光纤接入与热点运营**，客户是**小型 ISP / 运营商 / 酒店 / 园区**。
- 有 **GMT Control 23** → 与 `B/060 GMTCNT` 同一条线索（同一批客户群：工业与网络集成）。
- **⚠ 所以我方要卖的不是"企业 LAN 交换机"，而是「WISP / FTTx 现场那台 PoE」**。

**⭐ 商务模式（可直接抄进报价备注）**
- **全站以 USD 标价**（不是 ₺），**满 US$10,000 免运费**，**仓库支持当日自提（Same-day pickup for warehouse）**。
- → 它按**美元**做生意，**我方报 USD FOB 完全对得上**；且它**有仓库、有自提** → 能承接小批量现货。

**⭐ 新抓到的美元价格锚点（Ruijie 线，best sellers 页）**
| 型号 | 描述 | 页面价 |
|---|---|---|
| **`RG-ES08G-L`** | Ruijie **8 口千兆非管理**交换机 | **$19.50** |
| `RG-ES05G-L` | Ruijie 5 口千兆非管理 | $12.50（原价 $12.90） |
| `RG-EW300N` | 300 Mbps 无线路由 | $15.50 |
| `RG-EW1300G` | 1300M 双频千兆路由 | $45.00 |
| `RG-EW1200G` | 1200M 双频无线路由 | $55.00 |
| `RG-EST100-E` | 无线网桥套装 | $45.00（原价 $49.00） |
| **`RG-POE-AF15`** | PoE 注入器（af 15 W） | **$16.00** |
| **`RG-POE-AT30`** | PoE 注入器（at 30 W） | **$21.00** |

**→ 两个可直接用的结论**
1. **8 口千兆非管理 = US$19.50（零售/电商价）** —— 这是**土耳其市场 8 口千兆的价格地板**。任何"8 口千兆"报价必须以它为参照。
2. **WINET 自家 `OEM-8-PORT-GB-POE`（7×PoE 24/48V + 1 上行）= 2,916.76₺ + KDV**（r47 已录）。两条锚点并列 → **"非管理 8 口千兆 ≈ $19.5"** 与 **"8 口 PoE ≈ 2,917₺"** 之间的差，就是**PoE 的溢价空间**（我方报价应落在两者之间）。

### 与我方的切入点（**r48 改写，取代 r47 版本**）
| 它的场景 | 我方对位 | 为什么对 |
|---|---|---|
| **Mikrotik / Ubiquiti WISP 铁塔与 CPE 供电** | ⭐ **`EW-EPIS3910-8GE`**（云管理工业 PoE：**1–2 口 DIP 选 12V/24V 被动 PoE**、3–6 口 48V 30W、7–8 口 48V 60W） | WISP 现场大量使用 **24 V 被动 PoE**（Mikrotik 生态），**商用 af/at 机不兼容**；这台机正好兼容，且支持**单端口远程重启**（塔上设备死机的唯一解） |
| **户外/塔顶恶劣环境** | **`EW-PIS1810-8GE`**（宽温工业）/ `EW-PIS1802-1GE`（户外单口 PoE） | 宽温 + 防雷 |
| **GPON / FTTx（VSOL 线）** | **`EW-S53928QM`**（24×10G+4×100G 汇聚）/ `EW-810GS-20`、`EW-10GSFP-SR`（光模块） | 接入汇聚 + 模块打包 |
| **Hotspot / 园区（WiPOINT 线）** | **`EW-ES3028CG-AP`**（24 口云 PoE 400 W）/ `EW-ES3006CG-AP` | 云管理 + PoE |
| **8 口 PoE 现货（OEM 线）** | **`EW-S1710FG-AP`**（af/at）→ **`EW-S1810CF-AP`**（bt 60 W + 300 m + watchdog） | 对齐它自己的 `OEM-8-PORT-GB-POE` |

**打法（r48 更新）**
- 主题改为：**"WISP saha PoE: 12/24V pasif + uzaktan port reset — Mikrotik/Ubiquiti kurulumları için"**（WISP 现场 PoE：12/24V 被动 + 远程端口重启）。
- ⭐ **不要一上来卖 24 口机架式**——它的客户是铁塔/CPE，**8 口、DC 供电、能远程重启**才是痛点。
- 必问三句：**① Mikrotik 用 24V pasif PoE 的项目多吗？② Saha switch'i kaç adet/yıl? ③ USD fiyatla çalışıyorsunuz, FOB Shenzhen olur mu?**

### 证据等级（r48 增补）
- 已核实（新增）：**30 个品牌的 SKU 数**、**USD 标价 + 满 $10,000 免运费 + 当日自提**、**Ruijie 8 个 SKU 的美元价**（`wi.com.tr` 品牌页与 best-sellers 页逐条）。
- 仍空白：法定名与地址、成立年、员工数、**WINET 品牌商标归属**、WINET 交换机现工厂。
"""

# ---------------- A / 052 Nokta：upTech 交换机全表 ----------------
D['52'] = """
### ⭐ r48 增补：upTech 交换机产品线**全表**（官网逐型号抓取）

**命名规则（看懂就能自己推规格）**：`SW` + **1/2/3**（1=非管理 / 2=L2+ 管理 / 3=L3 管理）+ 端口数 + 代号（`G`=GE、`S`=SFP、`P`=PoE、`C`=combo、`U`=bt/大功率、`X`=10G）。

#### A. 非管理 PoE（`SW1xxxx`）
| 型号 | 规格 | 我方对位 | 差在哪 |
|---|---|---|---|
| `SW10411-GGTSP` | 4×GE PoE + 1×GE RJ45 + **1×GE SFP**，**75 W** | `EW-PIS1805-4GE`（4×GE PoE + 1 SFP）/ `EW-S1910G-DP` | 同档 |
| `SW1042-GGSP` | 4×GE PoE + 2×GE SFP，75 W | `EW-PIS1805-4GE` | 同档 |
| `SW1082-GGSP` | **8×GE PoE + 2×GE SFP，120 W** | ⭐ **`EW-S1710FG-AP`**（8×GE PoE + 2 SFP） | 同档 → **价格战** |
| `SW1082-GGSUP` | 8×GE PoE（**1–4 口 802.3bt**）+ 2 SFP，**300 W** | ⭐ **`EW-S1810CF-AP`**（**7–8 口 bt 60 W/口** + 300 m + watchdog） | ⭐ **它只有 1–4 口 bt，我方 7–8 口全 bt** → 真差异 |
| `SW10244-GGCP` | 24×GE PoE + 4×GE combo SFP，400 W | `EW-S1927CG-AP`（24 GE PoE + 2 RJ45 + 1 SFP）/ `EW-S1950CG-AP`（48 口） | 我方 24 口上联只有 1 SFP → **要补 combo 版** |

#### B. L2+ 管理 PoE（`SW2xxxx`）
| 型号 | 规格 | 我方对位 | 差在哪 |
|---|---|---|---|
| `SW2082-GGSP` | 8×GE PoE + 2 SFP，120 W | `EW-S1710FG-AP` 的受管对应（`EW-S2926GM-AP` 的 8 口版） | 我方**8 口受管 PoE 是产品线薄弱点** ⚠ |
| `SW2082-GGSUP` | 8×GE PoE（1–4 bt）+ 2 SFP，**300 W** | `EW-PIS3810M-8GE-BT`（8 口 af/at/**bt** + 2 SFP） | ⭐ 我方 **8 口全 bt** |
| `SW20162-GGSP` | **16×GE PoE + 2 SFP，250 W** | `EW-S1616CGU`（16 GE，PoE 版）/ `EW-PIS3620M-16GE`（16 PoE + 4 SFP，工业） | 同档 |
| `SW20162-GGCP` | 16×GE PoE + 2×1G combo，280 W | 同上 | — |
| `SW20244-GGCP` | 24×GE PoE + 4 combo SFP，400 W | `EW-S2926GM-AP`（24×GE PoE + 4 combo + 2 SFP，**L2+ 受管**） | ⭐ **1:1 对位** |
| `SW20244-GGCUP` | 24×GE PoE（1–4 bt）+ 4 combo，**500 W** | ⭐ **`EW-S5748GM-AP`**（L3 48 PoE + 4×10G）/ **`EW-S5954GM-AP`**（L3+ OSPF/VRRP） | ⭐ 我方是 **L3 + 10G 上联**，它只有 1G combo → **换代差** |
| `SW20244-GGC` | L2+ 24×GE + 4 GE combo SFP（非 PoE） | `EW-S2928GM`（24×GE + 4×1/2.5/10G SFP+） | ⭐ 我方上联是 **10G** |

#### C. L3 管理（`SW3xxxx`）
| 型号 | 规格 | 我方对位 | 差在哪 |
|---|---|---|---|
| `SW30244-GXS` | L3 **24×GE + 4×10G SFP+** | `EW-S2928GM`（L2+）/ **`EW-S5748GM-AP`**（L3 + 4×10G，含 PoE） | 我方 L3 版本**自带 PoE** |
| `SW30248-GSTC4X` | L3 **24×GE SFP + 8×GE RJ45（共享）+ 4×10G SFP+** | ⭐ **`EW-S3936GM`**（8×GE RJ45 + **24×GE SFP** + 4×1/2.5/10G SFP+） | ⭐ **结构几乎同构**（都是"少量电口 + 大量光口 + 4×10G"）；我方芯片 = **Microchip/Vitesse，598 Gbps** |

#### **upTech 全线合计：约 14 个交换机型号**（非管理 PoE 5 + L2+ 管理 7 + L3 管理 2）

**⭐ 从这张全表能得出的三个硬结论**
1. **它完全没有 2.5G**（全表 0 个 2.5G 型号）→ 我方 `EW-S6826`（24×2.5G+2×10G）、`EW-S6818`、`EW-S6809`、`W-S2910SM-DP` 是**整条新增产品线**，不是替换。
2. **它的 802.3bt 只在"1–4 口"，总功率 300 W / 500 W** → 我方 `EW-S1810CF-AP`（7–8 口 60 W）、`EW-PIS5728GM-AP-BT`（24 口 bt / **800 W**）是**功率维度碾压**。
3. **它的 L3 最高只有 4×10G，没有 25G/100G，也没有工业宽温** → 我方 `EW-S53928QM`（24×10G+4×100G）、`EW-S57948QM`（48×2.5G+4×100G）、`EW-PIS*` 工业线全部是空白补给。

**这把"给它报价"变成了三道非常具体的题**（建议邮件就这么写）：
> *"upTech 交换机线共约 14 款，全部为 GE + 最高 4×10G。我们看到的三个空缺：(1) 2.5G 全线没有；(2) 802.3bt 只在 1–4 口；(3) 工业宽温与 100G 完全没有。这三档我们可以直接贴 upTech 牌供货。"*

### 证据等级（r48 增补）
- 已核实（新增）：**14 个交换机型号的完整名称与端口/功率规格**（`noktaelektronik.net` 的 L2/L2+、L3、10G、PoE 管理/非管理各分类页逐条）、**upTech 六大类目结构**（Audio/Video 423、RF 267、Computer 197、Passive Network 158、Power 140、**Active Network 81**、Test 17、CCTV 11 …）、**B2B 下单平台 = `noktaelektronik.com.tr`**。
- 仍空白：upTech 交换机的**现工厂**、年采购量、采购负责人姓名。
"""

# ---------------- B / 010 ErETE：Edgecore + OcNOS 实证 ----------------
D['10'] = """
### ⭐ r48 实证：ErETE 是 **Edgecore（智邦）的分销商**，NOS 卖的是 **IP Infusion OcNOS 6.6**

这一轮把它的 **OPEN NETWORKING** 与 **NOS** 两个分类逐条抓完，证据如下。

#### A. `OPEN NETWORKING`（分类下 **7 个产品**，全部为 Edgecore 白盒）
| 型号 | 类型 | 备注 |
|---|---|---|
| **`AS4610-54T`** | 1 GbE 数据中心交换机 | Edgecore 经典 48×GE + 6×10G 白盒 |
| **`AS4610-54P`** | 1 GbE 数据中心交换机（PoE 版） | 同上，PoE |
| **`AS5712-54X`** | 10 GbE 数据中心交换机 | 48×10G + 6×40G |
| **`AS6712-32X`** | **40 GbE** 数据中心交换机 | 32×40G |
| **`AS7712-32X`** | **100 GbE** 数据中心交换机 | 32×100G |
| **`Wedge100BF-32X`** | ⭐ **100 GbE（Tofino / P4 可编程）** | **这是白盒里最"硬核"的一档**，说明它做**可编程数据面**生意 |
| **`ASXvOLT16`** | ⭐ **16 端口 XGS-PON OLT** | 它不只做企业网，**还做 PON 局端** |

#### B. `NOS`（分类下 **1 个产品**）
- **`OcNOS 6.6`** —— **IP Infusion 的 Network Operating System**（数据中心版）。

#### C. `OMURGA ve KENAR SWITCHLER`（骨干与边缘）
骨干分类 8 个产品中，**5 个是 Edgecore ECS 系列**：`ECS4810-12M`（12×1000Base 光 combo，−25~+65 °C）、`ECS4620-28F`（L3 千兆堆叠 24×1000Base-X SFP）、`ECS4510-28F`（22×GE SFP + 2 combo + 2×10G）、`ECS4120-28F`（20×GE SFP + 4CG + 4×10G，L2+）、`ECS4660-28F`（24×GE SFP + 2×10G XFP + 2 扩展）；
**另 1 个是自有品牌 `XPS-1320-36F`**（骨干光纤交换机：24 端口 100/1000 SFP + …）。

#### D. 完整的自有品牌 **XPS** 矩阵（工业 + 骨干）
- 工业非 PoE 管理型：`XPS-I7120-6 / -10 / -14 / -16 / -24`（4/8/10/12 口 GE + SFP）
- 工业 PoE 管理型：`XPS-I7120-6P / -10P / -14P / -16P`
- 工业 L2+：**`XPS-I8120-16`**（12×GE + **4×10G SFP+**）、`XPS-I8120-24F`（12×GE + 8×SFP）
- 骨干：**`XPS-1320-36F`**（24×100/1000 SFP）
→ **XPS 是它真正的"自有品牌"，且已覆盖工业 + 骨干光纤两段。**

#### E. 它还卖什么（决定了它是"全栈"而不是"分销"）
- **EtherWAN** 加固工业线：`EX89000 / EX87000 / EX77000 / EX83000 / EX61000A / EX70900 / EX72000`、加固 PoE `ER59000 / ER58000 / EX75000 / EX76000 / EX78000 / EX78602 / EX74000 / EX46100 / EX48000`、`ECS4660-28F`
- **SFP 全线**：1–10G、40G QSFP、100G QSFP28、**200G / 400G / 800G**、AOC、DAC
- **LANDE** 布线、机柜（600/800/1000 mm 深、服务器柜、壁挂柜、数据中心柜）、光纤配线、室内/户外转换器、转换器机箱

### ⚠ 与我方的战略冲突（必须由人拍板，不能自动决定）

| 情形 | 说明 | 建议动作 |
|---|---|---|
| **如果 Angora 代理/转售 Edgecore** | ErETE 卖的就是 **Edgecore AS/ECS/Wedge** —— **两者在同一货源上撞车** | **不要以"Edgecore 竞品"身份接触**；改为**谈 Angora 的 white-box 供货（贴 XPS 牌）**，用价格与交期打 Edgecore 的清单 |
| **如果 Angora 是自有/ODM 白盒（非 Edgecore 渠道）** | 那 ErETE 就是**最理想的白牌客户**：它已经会卖 ONIE 白盒与 OcNOS | **直接谈"XPS 白盒 + SONiC/ONIE 兼容"**，主打 **2.5G / 25G / 100G 的价格档** |
| 无论哪种 | ErETE **已经在做**开放网络，**不需要教育**；它缺的是**更便宜的硬件来源** | 首封直接给**硬件 BOM 报价**，不要给方案 PPT |

**首封主题（r48 更新）**：`XPS / ONIE white-box için alternatif donanım kaynağı（2.5G · 25G · 100G）`
**必问三句**：① **"Edgecore ürünlerini siz mi ithal ediyorsunuz, yoksa Türkiye distribütörü üzerinden mi?"** ② **"OcNOS lisansını siz mi satıyorsunuz?"** ③ **"XPS white-box için ONIE sertifikasyonu şart mı?"**
**⚠ 纪律**：**永不贬低 EtherWAN 与 Edgecore**（两者都是它的长期代理线）；只谈"**在它的品牌下、更低的硬件成本**"。

### 证据等级（r48 增补）
- 已核实（新增）：**OPEN NETWORKING 7 个型号全为 Edgecore（含 Wedge100BF-32X 与 ASXvOLT16 XGS-PON OLT）**、**NOS = OcNOS 6.6（IP Infusion）**、**骨干 5/8 为 Edgecore ECS + 1 个自有 XPS-1320-36F**、**XPS 工业线全 8 款型号**、**SFP 覆盖到 800G**（`erete.com.tr` 分类页逐条）。
- 仍空白：**Angora 与 Edgecore 的实际关系（内部待确认）**、ErETE 的 Edgecore 授权层级（直接进口 / 经土耳其分销商）、OcNOS 授权方式。
"""

# ---------------- B / 062 Cebeci：Cifocs 实证 ----------------
D['62'] = """
### ⭐ r48 实证：`Cifocs` 是挂在 Cebeci 下的**自有编码品牌**（产品码 `OPT-` / `RSC-` 是内部码）

**抓到的 Cifocs 产品线**（`cebecigrup.com` 品牌页与产品页逐条）：

| 系列 | 型号 | 品类 |
|---|---|---|
| 光纤以太网转换器 | `CFC-1100`、`CFC-1100S25`、`CFC-1200S20`、`CFC-2200`、`CFC-2200S20`、**`CFC-3200S20`（BiDi 单纤，1310/1550，20 km）** | 10/100 与 10/100/1000 光转换器 |
| 工业交换机 | **`CFC-4G2SFP-IPS`**（4×GE + 2×SFP 工业型） | 工业以太网 |
| 光纤模拟电话 | `CFC-T/R2PSTN`、`CFC-T/R2PSTN1F`、`CFC-T/R4PSTN`、`CFC-T/R4PSTN1F`、`CFC-T/R8PSTN`、`CFC-T/R8PSTN2F` | 话务走光纤（运营商/园区场景） |
| **内部产品码** | ⭐ **`OPT-008`、`OPT-013-A/B`、`RSC-049`、`RSC-049ETH`** | — |

**为什么这组内部码是关键证据**
- `OPT-`（optical）/ `RSC-`（?）这种**前缀 + 序号的内部编码**，是**"自有品牌 + 自建产品库"**的典型做法（和 upTech 的 `SW-` 体系同构）。
- 而它代理的 **Argus / Micos / Greenlee-Tempo / Trend Networks** 都用**原厂型号**（Argus 153/260、Micos MIS 900（`MIS-900`）、Greenlee 801K、Trend NC-500/TM-700）。
- → ⭐ **判断：`Cifocs` 是 Cebeci 的自有/独家品牌，产品由中国厂贴牌（转换器 + 工业交换机 + 光纤电话），Cebeci 编内部码。**
- ⚠ **但商标注册人与授权层级未在公开面确认** → 首封**必须问一句**（下面已写）。

### 与我方的切入点（r48 更新，取代 r47 版本）
1. ⭐ **`CFC-4G2SFP-IPS` 的下一代**：它只有 **4×GE + 2×SFP 非 PoE**。我方对位 + 升级：**`EW-PIS1805-4GE`**（4×GE PoE + 1 SFP）、**`EW-PIS1810-8GE`**（8 口 PoE）、**`EW-EPIS3910-8GE`**（云管理工业 PoE，含 12V/24V 被动 PoE）。
   → **"4 口 → 8 口 + PoE + 云"** 是一条干净的产品升级线。
2. **转换器线**：`CFC-2200S20`（1G 单模 20 km）对位 **`EW-810GS-20`**；`CFC-3200S20`（BiDi 单纤）对位 **`EW-810GS-20A&B`** / `EW-810GS-3A/B`；**10G 档它没有** → `EW-10GSFP-SR`。
3. **光纤模拟电话（PSTN over fiber）** —— ⚠ **我方完全没有这个品类**，**不要提**（提了显得不懂它的业务边界）。
4. **`S5700` 系列仍是电商挂品**（r47 已修正）→ 只作为"它在卖 L3 交换机"的旁证，**不作为谈判主体**。

**首封主题（r48 更新）**：`Cifocs endüstriyel switch hattı: 4 port → 8 port + PoE + bulut yönetimi`
**必问三句**：① **"Cifocs sizin tescilli markanız mı, yoksa ithalatçısı mısınız?"**（决定 OEM 谈法）② **"CFC-4G2SFP-IPS yılda kaç adet satılıyor?"** ③ **"Cifocs markasıyla 8 portlu PoE switch ürettirmek ister misiniz?"**

### 证据等级（r48 增补）
- 已核实（新增）：**Cifocs 六类共 13 个型号**（转换器 6 + 工业 1 + 光纤电话 6）、**内部产品码 `OPT-###` / `RSC-###`**、**代理品牌使用原厂型号（对照证明）**、**Cebeci 地址：Halil Rıfat Paşa Mah. Yüzer Havuz Sok. No:8 D:24, Okmeydanı / İstanbul 34384，0212 320 08 88 / 320 08 85，iletisim@cebecigrup.com**。
- 仍空白：**Cifocs 商标注册人（关键）**、Cifocs 现工厂、年采购量。
"""
