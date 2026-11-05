# -*- coding: utf-8 -*-
"""r49 补录（2026-11-01 深夜）：ErETE 供应链定性收口 + upTech 工业线（r48 漏项）+ Winet/Cifocs 复核。"""

D = {}

# ---------------- B / 010 ErETE ----------------
D['10'] = """
### ⭐⭐ r49 收口：ErETE 是 **IP Infusion 官方 Reseller（EMEA / Turkey）** —— 附件的答案在这

r48 留下的悬案「它是不是 IP Infusion 独家 / 我方会不会与它撞货源」，这一轮两头都拿到了证据。

**证据一（我方内部，仓库内既有）**
- `06-competitors/110` §十：**PNetworks 的硬件底座 = Edgecore（Broadcom 芯片）+ SONiC + OcNOS**，依据是 **Edgecore 官方新闻稿（MWC 2024-02-29）**「Edgecore × PNetworks 战略合作」；同处写明 **PNetworks 是 Angora 的土耳其本土竞对**。
- 同处 §13：**Angora 线 = Ewind（深圳 ODM）+ Marvell AC3/AC5**，`SAGA` 贴 TT 牌。
- → ⭐ **结论：Angora 不是 Edgecore 渠道；Edgecore 在土耳其的白牌玩法是 PNetworks 在做。** 所以 ErETE 卖 Edgecore **不构成与 Angora 自有线的货源冲突**，而是**指向「ErETE 的上游可能与 PNetworks 同池」**。

**证据二（外部，决定性）**
- **`ipinfusion.com/partners/`** 的 **Resellers** 名单里明确列出 **`Erete` · EMEA, Turkey**。
- → **ErETE 是 IP Infusion 的土耳其授权 Reseller**，不是"随便卖卖 NOS"。它的 `OcNOS 6.6` 单一 SKU 就是这条授权的落地。

**⭐ 但由此得出一条硬约束（推翻 r48 建议的一部分）**
- OcNOS 的**硬件合格清单只有 Edgecore 与 UfiSpace**（`OcNOS Systems`：PRO = Edgecore，FAST = UfiSpace；40+ 平台，Broadcom 芯片）。
- → **我方 Ewind/Angora 的箱子（Marvell AC3/AC5）不在 OcNOS 合格清单里，无法作为「更便宜的 OcNOS 硬件」卖给 ErETE。**
- → **正确打法**（r49 改写）：
  | 不要做的事 | 该做的事 |
  |---|---|
  | ❌ 说"我们的交换机跑 OcNOS，比 Edgecore 便宜" | ✅ 说 **"XPS 品牌的接入/园区线，与 OcNOS 数据中心线互补，不抢它的 ONIE 生意"** |
  | ❌ 拿 100G/25G 白盒去对 `AS7712-32X`/`Wedge100BF-32X` | ✅ 只有**做 ONIE/SONiC 认证**这一条路才谈数据中心白盒（且要报认证周期） |
  | ❌ 一上来谈"替换 Edgecore" | ✅ 谈 **`XPS-1220-*` 这条 GE 接入 PoE 线的补位与换代**（见下） |

### ⭐ r49 新发现：它真正的「自有品牌」是 **XPS-1220 线**（5 款，GE 接入 PoE）

`Yönetilebilir L2+ PoE Switchler`（分类 94）**5 个产品，全部 XPS**：

| 型号 | 端口（页面原文） |
|---|---|
| **`XPS-1220-10P`** | 8×10/100/1000 PoE + 2×100/1000 SFP |
| **`XPS-1220-18P`** | 16×10/100/1000 PoE + 2×100/1000 SFP |
| **`XPS-1220-26P`** | 22×PoE + 2×Gigabit Combo + … |
| **`XPS-1220-26PH`** | 22×PoE + 2×Gigabit Combo + …（H = 高功率版） |
| **`XPS-1220-52P`** | 48×PoE + 4×100/1000 SFP |

**⭐ 这才是与我方正面重合的一段**：全是 **GE 接入 + 1G SFP 上联**，**没有 2.5G、没有 bt（最高到 at/PoH）、没有 10G 上联、没有云管理**。
- 我方对位：`XPS-1220-10P` → **`EW-S1710FG-AP`**（8×PoE + 2 SFP，af/at）；`XPS-1220-18P` → **`EW-S1616CGU`**；`XPS-1220-26P/26PH` → **`EW-S1927CG-AP`**；`XPS-1220-52P` → **`EW-S1950CG-AP`**（48 口）。
- **升级点**：**bt 60 W/口（`EW-S1810CF-AP`/`EW-PIS3810M-8GE-BT`）+ 300 m 长距拨码 + 云管理（`EW-ES3006CG-AP`）**。
- **话术**：*"XPS-1220 hattınız GE + 1G uplink'te kalıyor; biz aynı form-factorde 2.5G ve 802.3bt (60W/port) verebiliyoruz — kendi markanızla."*

### 补充：Edgecore 在它产品树里的真实权重（r49 逐类点算）

| 分类 | 产品数 | 品牌构成 |
|---|---|---|
| **OMURGA（33）** | 8 | Edgecore ECS **5** + 自有 `XPS-1320-36F` **1** + … |
| **Kenar Switchler（34）** | ⚠ **0（空分类）** | 导航里有、**里面没有产品** |
| **Yönetilebilir L3（69）** | **6**（首页显示 4） | **全部 Edgecore**：`ECS4610-26T`、`ECS4610-50T`、`ECS4620-28T`、`ECS4620-52T` |
| **Yönetilebilir L2+ PoE（94）** | 5 | **全部自有 XPS-1220** |
| **OPEN NETWORKING（102）** | 7 | **全部 Edgecore**（含 Wedge100BF-32X / ASXvOLT16） |
| **NOS（107）** | 1 | `OcNOS 6.6` |

→ **Edgecore 占它「数据中心 + 骨干 + L3」三块，XPS 占「接入 PoE + 工业」两块**。它是一台**「西边 Edgecore 打 DC、东边 XPS 打接入」的双轨机器**。
→ ⭐ **我方只在「东边」有意义**（接入/工业 PoE + 2.5G），**西边碰不得**（OcNOS 合格清单锁死）。

### 证据等级（r49 增补）
- 已核实（新增）：**IP Infusion 官网 Reseller 名单含 Erete（EMEA, Turkey）**、**OcNOS Systems 硬件仅 Edgecore(PRO)/UfiSpace(FAST)**、**XPS-1220 五款型号与端口**、**L3 分类 6 款全 Edgecore**、**Kenar 分类为空**。
- 仍空白：**Angora 与 PNetworks 是否有过接触**（内部问）；ErETE 的 Edgecore 是直进还是经分销商；IP Infusion 授权是否**独家**（官网名单只写国别，不写独家）。
"""

# ---------------- A / 052 upTech ----------------
D['52'] = """
### ⭐ r49 重要补正：**upTech 有完整的工业线 `ISW` 系列**（r48 写"无工业宽温"是错的）

r48 只点了交换机（非管理/L2+/L3）就被 `noktaelektronik.net` 的分类数骗了 —— 工业线在**另一个分类**（`Endüstriyel Ethernet`，**50 个产品**），r49 已抓到。

#### A. upTech 工业型号（已见 5 款，多款标 `Yeni`）
| 型号 | 形态 | 我方对位 |
|---|---|---|
| **`ISW2420-GGS`** | L2 网管 4×GE + 2×GE SFP（DIN 轨） | `EW-PIS1805-4GE` / `EW-EPIS3910-8GE` |
| **`ISW2420-GGSP`** | L2 网管 4×GE **PoE** + 2×GE SFP（af/at） | ⭐ `EW-PIS1805-4GE` |
| **`ISW2820-GGS`** | L2 网管 8×GE + 2×GE SFP（IP40，−40 °C） | `EW-PIS1810-8GE` |
| **`ISW2820-GGSPV`** | L2 网管 8×GE **PoE** + 2×GE SFP（af/at） | ⭐ `EW-PIS1810-8GE` / `EW-EPIS3910-8GE` |
| **`ISW1820-FGSP`** | **非管理** 8×**10/100M** PoE + 2×GE SFP（DIN，−40~+75，IP30） | `EW-PIS1802-1GE` 系 / `EW-S1910G-DP` |
| **`ISW21240-GGS`** | L2 网管 12×GE + 4×GE SFP | `EW-PIS3620M-16GE` |

**→ 与我方的真实差距（工业段）**：upTech 工业线**全部停在 GE + 1G SFP**，**没有 2.5G、没有 10G 上联、没有 bt（最高 af/at）**；且**非管理款还是百兆**（`ISW1820-FGSP`）。
→ 我方在工业段的三张牌：**① 10G 上联工业款（`EW-PIS5712M-8GE` 4×10G SFP+）② 12/24 V 被动 PoE + 云（`EW-EPIS3910-8GE`）③ bt 60 W（`EW-PIS3810M-8GE-BT`）**。

#### B. ⚠ 同分类里它还卖这些（决定我方"不比品牌比档位"）
`Endüstriyel Ethernet` 50 个产品里品牌混编：**Edge-Core**（`ECIS4500-4P4T`、`ECIS4500-8P4F`，4×/8× PoE+ 30W + 4×SFP）、**Planet**（`BSP-300` 太阳能 PoE、`IGS-801T`、`ISW-1022MT`、`WGS-804HP`、`IGS-5225-16T4S`）、**ORing**（`RGPS-R9244GP+-P` **24×PoE+ 带 4×10G SFP+** 机架工业、`IGPS-1042GPA`、`IGPS-9084GP-LA`、`IGPS-7084GP`、`IGS-3032GC`、`IGS-3044GC`）、**Dahua**（`PFS3106-4ET-60`、`PFS4207-4GT-DP` 4 口 **bt 90 W**）、**Harting**（`20 77 208 4009` mCon M12）。
- ⚠ **注意 `RGPS-R9244GP+-P`：ORing 的工业机架 24×PoE+ + 4×10G** → 我方"工业没有 10G 上联"这句话在**客户在售清单里已被 ORing 填上**，**不能用**。要用的是「**工业 + 10G + 2.5G + bt 同时具备**」。
- ⚠ `PFS4207-4GT-DP` 标 **802.3bt / 单口 90 W / 总 120 W**（页面原文）→ **Nokta 体系里已有 90 W 单口**，我方 bt 话术要盯"**全口 60 W + 总 800 W**"，不是"单口功率最高"。

### 证据等级（r49 增补）
- 已核实（新增）：**upTech 工业 ISW 系列 6 款**、**工业分类 50 个产品的品牌混编（Edge-Core/Planet/ORing/Dahua/Harting）**、**ORing 工业 24 口 PoE+ 带 4×10G**、**Dahua 4 口 bt 90 W**。
- 仍空白：**ISW 系列的现工厂**、工业线年量、`ISW21240` 之后是否还有更大端口款（分类共 3 页，r49 只读了第 1 页 20 个）。
"""

# ---------------- A / 053 Winet ----------------
D['53'] = """
### r49 复核：WINET 的 426 个 SKU 里，**主体是无源光器件，不是交换机**

把 `wi.com.tr` 的 **WINET 子类计数**逐个抄下来（页面原文），结构一目了然：

| 子类 | 数量 | 子类 | 数量 |
|---|---|---|---|
| Breakout SM/MM | **53** | Patchcord Duplex SM | **37** |
| PoE 注入器 & 适配器 | **22** | Patchcord Simplex SM | 19 |
| Role/SSR 触发器 | 16 | 电源适配器 & PSU | 16 |
| 室外光缆 | 16 | 内外通用光缆 | 16 |
| Patchcord Duplex OM3 | 15 | 保险/断路器 | 15 |
| 电子自动化 | 15 | LoRa 线缆/天线 | 14 |
| 安装与技术支持 | 13 | 控制卡 | 13 |
| 手工具 | 12 | PLC 分光器条 | 11 |
| **SFP+ (10G)** | **11** | 室外箱 | 11 |

**→ 三项判断**
1. **WINET = 无源光（Patchcord/Splitter/ODF/箱体/工具）+ PoE 注入器 + 电源 + LoRa** —— 是**FTTx 现场物料商**，不是交换机品牌。它的 `OEM-8-PORT-GB-POE` 在 426 SKU 里是**孤例**（已见子类里没有 ≥2 SKU 的交换机类目）。
2. **对我方的含义变了**：r48 说"8 口 PoE 在它自有品牌里是空白"→ 更准确的是 **交换机根本不是它的主品类**，它卖的是**塔上那台 PoE 注入器（22 个 SKU）**。
3. ⭐ **最锋利的一句**：它自己就有 **22 个 PoE 注入器 SKU**，`RG-POE-AT30` 卖 **$21**，WINET 8 口 PoE 卖 **2,916.76 ₺** —— **我方 `EW-EPIS3910-8GE` 用"1 台顶 4 个注入器 + 4 条线 + 4 个电源"来打**（省 4 个适配器、省 4 个插座、能远程重启）。

⚠ 口径修正：r48 写"WINET 426 是 house brand 覆盖天线/射频/PoE/配件/**少量交换机**"，**"少量交换机"应改为"交换机近乎孤例"**（已见子类中无交换机类目）。

### 证据等级（r49 增补）
- 已核实（新增）：**WINET 不少于 30 个子类的 SKU 计数**（上表逐条抄自 `wi.com.tr` 品牌筛选页）。
- 仍空白：**WINET 交换机到底几个 SKU**（子类清单在页面折叠区，r49 只读到前 60 项）→ r50 待补。
"""

# ---------------- B / 062 Cebeci ----------------
D['62'] = """
### r49 复核：`Cifocs` 在品牌墙里与 **Argus/CMG/Greenlee/InterCoax/Kingfisher/Maisvch/Micos/PatchSee/Tempo/Trend/Vesala** 并列（**13 个品牌**）

- `cebecigrup.com/markalar/` 原文品牌清单：**argus · BitStream · cifocs · cmg · greenlee · intercoax · Kingfisher · Maisvch · micos · PatchSee · tempo · trend-networks · vesala**。
- ⚠ **这条证据对"自有品牌"是不利的**：Cebeci 把 Cifocs 与 12 个**明确的外国品牌**放在同一面墙上，**没有任何"our brand / kendi markamız"标注**。
- 支持"自有/独家"的仍是：**`CFC-*` 自家编号 + 内部码 `OPT-008` / `OPT-013` / `RSC-049` / `RSC-050`**（产品页"Ürün Kodu"列，官方原文），而代理品牌用原厂型号。
- → **判定维持「推定」，且证据权重从"偏自有"下调为「五五」**。**客户可见文本一律不写"自有商标"**，首封照旧问一句。

### 证据等级（r49 增补）
- 已核实（新增）：**Cebeci 品牌墙 13 个品牌全名单**（含 BitStream / Kingfisher / Maisvch / PatchSee / Vesala 五个 r48 未记录的）。
- 仍空白：**Cifocs 商标注册人**（TÜRKPATENT 需图形验证码 / 会话，公开检索未能直连）→ **唯一未解的阻塞项**。
"""
