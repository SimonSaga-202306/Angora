# 117 · 四家客户的「产品清单取证」（r48 · 2026-11-01）

> **这是什么**：r47 的 `116` 给的是"档位级"对位（因为我们只有分类、没有型号）。
> r48 直接进四个官网把**分类逐层点到底**，拿到了**型号级清单** → 本文件是**原始清单 + 修正 + 战略含义**。
>
> 四家 = **Nokta/upTech（A/052）· Winet（A/053）· ErETE（B/010）· Cebeci/Cifocs（B/062）**。
> 这四家正好代表四种完全不同的客户类型：**自有品牌贴牌商 / WISP 渠道 / 开放网络分销商 / 电信测试+自有转换器品牌**。

---

## 〇、这轮最重要的一句话

**r47 把 Nokta 判成"最优先 OEM 目标"是对的；但 r48 发现 Winet 和 ErETE 的定性都需要改：**

- **Winet 不是"自有品牌网络设备商"** —— 它是 **Mikrotik（473 SKU）+ Ubiquiti（319 SKU）的 WISP 渠道**，自有 WINET（426 SKU）只是 house brand。**因此我方要卖的是"塔上那台 DC 供电、能远程重启的 PoE"，不是 24 口机架式。**
- **ErETE 不是普通分销商** —— 它是 **Edgecore（智邦）的分销商 + IP Infusion OcNOS 的转售方**，卖到 **Wedge100BF-32X（Tofino 可编程 100G）与 ASXvOLT16（XGS-PON OLT）**。**这直接撞上 Angora 自己的 Edgecore 线 → 必须先内部拍板再接触（见 §五）。**

---

## 一、Nokta / upTech（A/052）· 自有品牌贴牌商 —— **14 款交换机全清单**

**命名规则**：`SW` + `1/2/3`（1=非管理 / 2=L2+ / 3=L3）+ 端口数 + 代号（`G`=GE、`S`=SFP、`P`=PoE、`C`=combo、`U`=bt、`X`=10G）。

| # | 型号 | 端口 / 功率 | 我方对位 | 谁强 |
|---|---|---|---|---|
| 1 | `SW10411-GGTSP` | 4×GE PoE + 1×GE RJ45 + 1×GE SFP，75 W | `EW-PIS1805-4GE` → `EW-S1910G-DP` | 平 |
| 2 | `SW1042-GGSP` | 4×GE PoE + 2×GE SFP，75 W | `EW-PIS1805-4GE` | 平 |
| 3 | `SW1082-GGSP` | **8×GE PoE + 2×GE SFP，120 W** | ⭐ `EW-S1710FG-AP` | 平（价格战） |
| 4 | `SW1082-GGSUP` | 8×GE PoE（**1–4 口 bt**）+ 2 SFP，**300 W** | ⭐ `EW-S1810CF-AP`（**7–8 口 bt 60 W/口** + 300 m + watchdog） | **我方** |
| 5 | `SW10244-GGCP` | 24×GE PoE + 4 combo，400 W | `EW-S1927CG-AP` / `EW-S1950CG-AP` | 平（我方上联弱） |
| 6 | `SW2082-GGSP` | 8×GE PoE + 2 SFP，120 W（**L2+**） | ⚠ 我方 8 口**受管** PoE 是薄弱点 | 客户 |
| 7 | `SW2082-GGSUP` | 8×GE PoE（1–4 bt）+ 2 SFP，300 W（L2+） | `EW-PIS3810M-8GE-BT`（8 口全 bt） | **我方** |
| 8 | `SW20162-GGSP` | **16×GE PoE + 2 SFP，250 W** | `EW-S1616CGU` PoE 版 / `EW-PIS3620M-16GE` | 平 |
| 9 | `SW20162-GGCP` | 16×GE PoE + 2×1G combo，280 W | 同上 | 平 |
| 10 | `SW20244-GGCP` | 24×GE PoE + 4 combo，400 W（L2+） | ⭐ `EW-S2926GM-AP`（24 PoE + 4 combo + 2 SFP） | 平（1:1） |
| 11 | `SW20244-GGCUP` | 24×GE PoE（1–4 bt）+ 4 combo，**500 W** | ⭐ `EW-S5748GM-AP`（L3 / 48 PoE / **4×10G**）/ `EW-S5954GM-AP`（L3+ **OSPF·VRRP**） | **我方（代差）** |
| 12 | `SW20244-GGC` | L2+ 24×GE + 4 combo（非 PoE） | ⭐ `EW-S2928GM`（4×**1/2.5/10G** SFP+） | **我方** |
| 13 | `SW30244-GXS` | **L3 24×GE + 4×10G SFP+** | `EW-S5748GM-AP`（L3 且带 PoE） | 平/我方 |
| 14 | `SW30248-GSTC4X` | **L3 24×GE SFP + 8×GE RJ45（共享）+ 4×10G** | ⭐ `EW-S3936GM`（8×GE + **24×GE SFP** + 4×1/2.5/10G，**598 Gbps**，Microchip/Vitesse） | **结构同构** |

**三个空缺（就是邮件的三段正文）**
1. **2.5G：0 款。** → `EW-S6805F / S6806 / S6809 / S6818 / S6826`＋`W-S2910SM-DP` 是**整条新增产品线**。
2. **802.3bt 只在 1–4 口，总功率 300 / 500 W。** → `EW-S1810CF-AP`（7–8 口 60 W）、`EW-PIS5728GM-AP-BT`（**24 口 bt / 800 W**）。
3. **L3 最高 4×10G，无 25G/100G，无工业宽温。** → `EW-S53928QM`（24×10G+4×100G）、`EW-S57948QM`（48×2.5G+4×100G）、`EW-PIS*` 工业线。

**还抓到的结构性事实**
- upTech 共 **916 SKU**，其中 **Active Network 81 个**（交换机 + PoE + 工业 + 无线 + 转换器），其余是 A/V 423、RF 267、电脑外设 197、无源网络 158、电源 140。
- **B2B 下单在 `noktaelektronik.com.tr`**（`.net` 是展示站）→ **说明它的经销商体系是线上化、有账号的** → 我方供货后可挂到它的 B2B 目录。

---

## 二、Winet（A/053）· WISP 渠道 —— **30 个品牌 + 美元价目**

**Brands 页的 SKU 计数（原文）**：**Mikrotik 473 · WINET 426 · Ubiquiti 319 · Ruijie 40 · Mimosa 29 · Huawei 25 · WiPOINT 24 · VSOL 23 · GMT Control 23 · Mean Well 20 · RF Elements 18 · NetElastic 18 · S-Link 17 · TP-Link 16 · DeltaLink 9 · DMA-SOFT 6 · Everest 6 · Paessler 4 · RedLine 3 · Extralink 3 · Xiaomi 3 · Tenda 3 · Compex 2 · Juniper 1 · Pisces 1**（Teltonika / Cambium / IgniteNet / InfiNET / Nexans 挂 0）。

**商务模式（原文）**：**全站 USD 标价**、**满 US$10,000 免运费**、**仓库当日自提**。

**美元价目（Ruijie 线 best sellers）**
| 型号 | 描述 | 价 |
|---|---|---|
| `RG-ES08G-L` | 8 口千兆非管理 | **$19.50** |
| `RG-ES05G-L` | 5 口千兆非管理 | $12.50（原 $12.90） |
| `RG-EW300N` | 300M 无线路由 | $15.50 |
| `RG-EW1300G` | 1300M 双频千兆路由 | $45.00 |
| `RG-EW1200G` | 1200M 双频路由 | $55.00 |
| `RG-EST100-E` | 无线网桥 | $45.00（原 $49.00） |
| `RG-POE-AF15` | PoE 注入器 af 15 W | **$16.00** |
| `RG-POE-AT30` | PoE 注入器 at 30 W | **$21.00** |

**⭐ 定价含义（本轮最有商业价值的一段）**
- **8 口千兆非管理 = US$19.50**（它的电商零售价）→ **土耳其市场的 8 口千兆价格地板**。
- **WINET `OEM-8-PORT-GB-POE`（8 口千兆 PoE）= 2,916.76 ₺ + KDV** → 与上一条并列，**"PoE 溢价"就是两者之差**。
- 我方任意 8 口 PoE 报价，**必须落在 $19.5 与 2,917₺ 之间**，否则要么丢单要么损毛利。

**⚠ 定性修正（取代 r47）**
- r47 写它是"自有品牌网络设备商"。**r48 修正：它是 WISP / FTTx 渠道商**（Mikrotik + Ubiquiti + VSOL GPON + WiPOINT 热点），自有 WINET 是 house brand（426 SKU，含天线/射频/PoE/配件/少量交换机）。
- **→ 谈法要变**：
  | r47 的错误谈法 | r48 的正确谈法 |
  |---|---|
  | 推 24 口机架式 PoE | ⭐ **推 8 口、DC 12/24 V 输入、能远程端口重启的现场机** |
  | 讲"企业 LAN 方案" | 讲 **塔上/CPE/户外柜** |
  | 忽略 PoE 制式 | ⭐ **Mikrotik 生态大量用 24 V 被动 PoE** → 我方 **`EW-EPIS3910-8GE`**（1–2 口 DIP 选 **12V/24V 被动**、3–6 口 48V 30W、7–8 口 48V 60W、**云管理 + 单端口重启**）**是全场最精准的一台机器** |
- 另有 **GMT Control 23 SKU** → 与 `B/060 GMTCNT` 交叉（同一客户群：工业 + 网络集成）。

---

## 三、ErETE（B/010）· 开放网络分销商 —— **Edgecore + OcNOS 实证**

### A. OPEN NETWORKING（**7 个产品，全部 Edgecore**）
| 型号 | 类型 |
|---|---|
| `AS4610-54T` / `AS4610-54P` | 1 GbE 数据中心（P = PoE） |
| `AS5712-54X` | 10 GbE 数据中心 |
| `AS6712-32X` | **40 GbE** 数据中心 |
| `AS7712-32X` | **100 GbE** 数据中心 |
| **`Wedge100BF-32X`** | ⭐ **100 GbE，Tofino / P4 可编程** |
| **`ASXvOLT16`** | ⭐ **16 端口 XGS-PON OLT**（PON 局端） |

### B. NOS（1 个产品）
- **`OcNOS 6.6`** —— **IP Infusion** 的数据中心 NOS。

### C. 骨干/边缘（8 个产品）
- **Edgecore 5 款**：`ECS4810-12M`（12×1000Base 光 combo，**−25~+65 °C**）、`ECS4620-28F`（L3 堆叠 24×1000Base-X）、`ECS4510-28F`、`ECS4120-28F`、`ECS4660-28F`
- **自有 1 款**：**`XPS-1320-36F`**（24×100/1000 SFP 骨干光纤）

### D. 自有品牌 XPS 全矩阵（8 款）
`XPS-I7120-6 / -10 / -14 / -16 / -24`（非 PoE 工业）· `XPS-I7120-6P / -10P / -14P / -16P`（PoE 工业）· **`XPS-I8120-16`（12×GE + 4×10G）** · `XPS-I8120-24F`（12×GE + 8 SFP）· `XPS-1320-36F`（骨干）

### E. 其他
- **EtherWAN** 加固线（`EX89000→EX72000` + `ER59000/ER58000` + `EX75000/76000/78000/78602/74000/46100/48000`）
- **SFP 到 800G**：1–10G / 40G QSFP / 100G QSFP28 / **200G·400G·800G** / AOC / DAC
- **LANDE** 布线 + 全套机柜（600/800/1000 mm 深、服务器柜、壁挂、数据中心柜）

---

## 四、Cebeci / Cifocs（B/062）· 电信测试 + 自有转换器品牌

**Cifocs 产品线（13 款）**
| 系列 | 型号 |
|---|---|
| 光纤以太网转换器 | `CFC-1100`、`CFC-1100S25`、`CFC-1200S20`、`CFC-2200`、`CFC-2200S20`、**`CFC-3200S20`（BiDi 单纤 1310/1550, 20 km）** |
| ⭐ 工业交换机 | **`CFC-4G2SFP-IPS`**（4×GE + 2×SFP） |
| 光纤模拟电话（PSTN over fiber） | `CFC-T/R2PSTN`、`CFC-T/R2PSTN1F`、`CFC-T/R4PSTN`、`CFC-T/R4PSTN1F`、`CFC-T/R8PSTN`、`CFC-T/R8PSTN2F` |
| **内部产品码** | ⭐ **`OPT-008`、`OPT-013-A/B`、`RSC-049`、`RSC-049ETH`** |

**判断**：代理品牌（Argus / Micos / Greenlee-Tempo / Trend / InterCoax）**全部使用原厂型号**（`MIS-900`、`801K`、`NC-500`、`TM-700`、`Argus 153/260`），而 Cifocs **使用自家编号体系** → **Cifocs 极可能为 Cebeci 自有/独家品牌（中国贴牌 + 自建产品库）**，与 upTech 的 `SW-` 体系同构。
⚠ **商标注册人未在公开面确认** → 首封必须问：**"Cifocs sizin tescilli markanız mı?"**

**切入点**：`CFC-4G2SFP-IPS` → **`EW-PIS1805-4GE`（4 口 PoE）/ `EW-PIS1810-8GE`（8 口）/ `EW-EPIS3910-8GE`（云 + 12/24V 被动）**；
转换器 `CFC-2200S20` → `EW-810GS-20`；`CFC-3200S20`（BiDi）→ `EW-810GS-20A&B`；
⚠ **光纤模拟电话我方没有 → 不要提**（这是它的护城河业务）。

---

## 五、⚠ 两个必须由人拍板的问题（本轮不给结论）

### 问题 1：**Angora 与 Edgecore 是什么关系？**（决定 ErETE 是客户还是对手）

仓库记录显示 **Angora 侧与 Edgecore / Broadcom + SONiC 相关**（`06-competitors/112` 的对比口径），而 **ErETE 明牌卖 Edgecore（AS/ECS/Wedge）+ OcNOS**。

| 如果… | 那 ErETE 是… | 应采取的动作 |
|---|---|---|
| Angora **代理/转售 Edgecore** | ⚠ **同货源对手**（它在卖 Angora 也在卖的东西） | **不要以"Edgecore 竞品"身份接触**；改谈 **Angora 自有/ODM 白盒贴 XPS 牌**，只在**价格与交期**上打 |
| Angora 是**自有/ODM 白盒**（非 Edgecore 渠道） | ⭐ **最理想的白盒客户**（已会卖 ONIE 白盒 + OcNOS，无需教育） | 直接给 **硬件 BOM 价**，主打 **2.5G / 25G / 100G 的价格档** |

**⚠ 在这条确认之前，不要给 ErETE 发任何带 Edgecore 字样的邮件。**

### 问题 2：**要不要把 upTech 当成"贴牌大客户"来谈？**

- 支持：916 SKU 自有品牌、14 款交换机全为 GE 档、**2.5G/bt 全端口/工业/100G 全空**、B2B 平台已线上化、能转口三个区域。
- 风险：它同时代理 **Edge-Core / Ruijie / Planet / ORing** → 若我们给它贴牌，**可能被它用来压这四家的价**（对我方是好事），但也**可能引起四家反弹**（对它不是好事）。
- → **建议**：**先谈"2.5G + 全端口 bt + 100G 三档"，不要一上来谈全线替换**（给它安全感，也保住它现有代理关系）。

---

## 六、下一步（r49 备选，按 ROI 排序）

1. **`wi.com.tr` 的 WINET 426 SKU 全表**（尤其 PoE 交换机与天线）→ 把"house brand 的完整缺口"补齐。
2. **`noktaelektronik.net` 的 Industrial Ethernet 子类**（upTech 工业线到底有几款；r48 只确认了 81 个 Active 总数）。
3. **ErETE 的 `Kenar Switchler` / `Yönetilebilir L2+ / L3` 分类**（确认 Edgecore 在它营收里的比重）。
4. **`Cifocs` 商标注册查询**（TÜRKPATENT 公开检索 → 一次定生死）。
5. **Perpa 三家（Nokta / Cebeci / Zeytek）的地理与关系图** —— 它们都在 Perpa / Okmeydanı 同一片区，**互为上下游或互为客户**的可能性高。

---

**相关文件**
- `116-b-a-model-mapping-2026-11-01.md`（档位级对位，r47）
- `115-turkey-b-tier-deepdig-2026-11-01.md`（B 档横向总表，r46）
- 逐家详情：`TR Customers/A/052…`、`A/053…`、`B/010-erete.md`、`B/062-cebeci-grup.md` 的 **「附：r48 抓站补录」**
