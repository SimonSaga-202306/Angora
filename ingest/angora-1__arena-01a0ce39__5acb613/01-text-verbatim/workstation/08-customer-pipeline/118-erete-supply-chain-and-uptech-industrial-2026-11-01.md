# 118 · ErETE 供应链定性收口 + upTech 工业线补正（r49 · 2026-11-01 深夜）

> **本轮只解决上一轮留下的三个未决问题**，不新增客户：
> ① `117` §五 的阻塞项「Angora 与 Edgecore 是什么关系 / ErETE 到底是客户还是对手」→ **已收口，结论见 §一**；
> ② r48 说 upTech「无工业宽温」→ **错，已证伪，见 §二**；
> ③ `Cifocs` 是自有商标还是第三方 → **证据权重下调，见 §四**。
>
> 逐家档案同步更新：`A/052`、`A/053`、`B/010`、`B/062` 各新增 **「附：r49 复查收口（2026-11-01 深夜）」**。

---

## 一、⭐ ErETE：两条证据同时到手，阻塞项解除

### 证据 A（仓库内既有，翻出来就对上了）

- `06-competitors/110` §十：**PNetworks 的硬件底座 = Edgecore（Broadcom）+ SONiC + OcNOS**，依据是 **Edgecore 官方新闻稿（MWC 2024-02-29）「Edgecore × PNetworks 战略合作」**；同一份文件把 **PNetworks 定为 Angora 的土耳其本土竞对**。
- `06-competitors/110` §13：**Angora 的线 = Ewind（深圳 ODM）+ Marvell AC3/AC5**，`SAGA` 贴 TT 牌进运营商。

→ **Angora 不是 Edgecore 渠道。** 在土耳其用 Edgecore 做白牌的是 **PNetworks**。
→ 所以 `117` §五 担心的「ErETE 卖 Edgecore ⇒ 与 Angora 自有线撞货源」**不成立**。

### 证据 B（外部，决定性）

**`ipinfusion.com/partners/`** 的 **Resellers** 名单原文列出：

> **Erete** — EMEA, **Turkey**

→ **ErETE 是 IP Infusion 的土耳其授权 Reseller**。它那个孤零零的 `OcNOS 6.6` SKU，就是这条授权的落地。

### ⭐ 但由此产生一条硬约束（**推翻 r48 给 ErETE 的建议**）

OcNOS 的合格硬件**只有两家**（`ipinfusion.com/products/ocnos-systems/` 原文）：**Edgecore（PRO 线）** 与 **UfiSpace（FAST 线）**，40+ 平台，全部 Broadcom 芯片。

→ **我方 Ewind/Angora 的箱子是 Marvell AC3/AC5，不在 OcNOS 合格清单里** —— **不能**作为"更便宜的 OcNOS 硬件"卖给 ErETE。
→ r48 写的「若为自有/ODM 白盒 → 直接给硬件 BOM 价，主打 2.5G/25G/100G 价格档」**必须收窄**：

| 之前（r48） | 现在（r49 定稿） |
|---|---|
| ❌ "我们的交换机跑 OcNOS，比 Edgecore 便宜" | ✅ **"XPS 品牌的接入/园区线，与 OcNOS 数据中心线互补"** |
| ❌ 拿 100G/25G 白盒对 `AS7712-32X` / `Wedge100BF-32X` | ✅ 只有**走 ONIE/SONiC 认证**才谈数据中心白盒，且必须先报认证周期与费用 |
| ❌ 一上来谈"替换 Edgecore" | ✅ **谈 `XPS-1220-*` 这条 GE 接入 PoE 线的补位与换代** |

### ⭐ 新发现：它真正在打的自有牌是 **`XPS-1220` 线（5 款 GE 接入 PoE）**

`Yönetilebilir L2+ PoE Switchler`（分类 94）**5 个产品，全为 XPS**：

| 型号 | 端口（页面原文） | 我方对位 | 升级在哪 |
|---|---|---|---|
| **`XPS-1220-10P`** | 8×10/100/1000 PoE + 2×100/1000 SFP | `EW-S1710FG-AP` | bt / 云 / 300 m |
| **`XPS-1220-18P`** | 16×PoE + 2×SFP | `EW-S1616CGU` | 同上 |
| **`XPS-1220-26P`** | 22×PoE + 2×Gigabit Combo | `EW-S1927CG-AP` | 同上 |
| **`XPS-1220-26PH`** | 22×PoE + 2×Combo（高功率） | `EW-S1927CG-AP` / `EW-PIS3810M-8GE-BT` | **单口 60 W** |
| **`XPS-1220-52P`** | 48×PoE + 4×SFP | `EW-S1950CG-AP` | bt / 云 |

**全线共性**：**GE 接入 + 1G SFP 上联**，**无 2.5G、无 bt（最高 at/高功率 at）、无 10G 上联、无云管理**。
→ **这就是我方唯一能正面对打的一段**，而且话术干净：*"XPS-1220 hattınız GE + 1G uplink'te kalıyor; aynı form-factorde 2.5G ve 802.3bt (60W/port) verebiliyoruz — kendi markanızla."*

### Edgecore 在它产品树里的真实权重（逐类点算）

| 分类 | 产品数 | 品牌构成 |
|---|---|---|
| OMURGA（33） | 8 | Edgecore ECS **5** + 自有 `XPS-1320-36F` 1 + 其他 |
| **Kenar Switchler（34）** | ⚠ **0（空分类）** | 导航里有入口，**里面没有产品** |
| **Yönetilebilir L3（69）** | **6**（首页展示 4） | **全部 Edgecore**：`ECS4610-26T`、`ECS4610-50T`、`ECS4620-28T`、`ECS4620-52T` |
| **L2+ PoE（94）** | 5 | **全部自有 XPS-1220** |
| **OPEN NETWORKING（102）** | 7 | **全部 Edgecore**（含 `Wedge100BF-32X`、`ASXvOLT16`） |
| NOS（107） | 1 | `OcNOS 6.6` |

→ **它是一台「西边 Edgecore 打 DC/骨干/L3、东边 XPS 打接入/工业」的双轨机器。**
→ **我方只在「东边」有意义；西边被 OcNOS 合格清单锁死，碰不得。**

**首封主题（r49 定稿）**：`XPS-1220 hattı için 2.5G + 802.3bt yedek kaynak (kendi markanızla, OcNOS'a dokunmadan)`
**必问三句**：① **"XPS-1220'i kim ürettiriyor, Çin'de mi?"** ② **"IP Infusion reseller'lığınız münhasır mı?"** ③ **"2.5G erişim talebi geliyor mu?"**
**⚠ 纪律**：**绝不提"替代 Edgecore"**、**绝不提"我们的箱子跑 OcNOS"**（一查合格清单就露），**只谈接入段 + 自有品牌贴牌**。

---

## 二、⚠ upTech：**有完整工业线 `ISW` 系列**（r48 的"无工业宽温"是错的）

r48 只点了交换机三类（非管理/L2+/L3）就下了"无工业"的结论 —— 工业线在**另一个分类** `Endüstriyel Ethernet`（**50 个产品**，3 页，r49 读了第 1 页）。

### upTech 工业型号（已见 6 款，多款标 `Yeni`）

| 型号 | 形态 | 我方对位 |
|---|---|---|
| `ISW2420-GGS` | L2 网管 4×GE + 2×GE SFP | `EW-PIS1805-4GE` |
| **`ISW2420-GGSP`** | L2 网管 4×GE **PoE**(af/at) + 2 SFP | `EW-PIS1805-4GE` / `EW-EPIS3910-8GE` |
| `ISW2820-GGS` | L2 网管 8×GE + 2 SFP（IP40，−40 °C） | `EW-PIS1810-8GE` |
| **`ISW2820-GGSPV`** | L2 网管 8×GE **PoE** + 2 SFP | `EW-PIS1810-8GE` / `EW-EPIS3910-8GE` |
| `ISW1820-FGSP` | **非管理 8×百兆** PoE + 2×GE SFP | `EW-PIS1802-1GE` 系 |
| `ISW21240-GGS` | L2 网管 12×GE + 4×GE SFP | `EW-PIS3620M-16GE` |

**工业段的真实差距**：upTech 工业线**全部 GE + 1G SFP**，**无 2.5G / 无 10G 上联 / 无 bt**，且**非管理款仍是百兆**。
→ 我方三张牌：**① 10G 上联（`EW-PIS5712M-8GE` 4×10G SFP+）② 12/24 V 被动 PoE + 云（`EW-EPIS3910-8GE`）③ bt 60 W（`EW-PIS3810M-8GE-BT`）**。

### ⚠ 但同分类里它还卖这些（我方话术必须避开两处）

`Endüstriyel Ethernet` 50 个产品**品牌混编**：**Edge-Core**（`ECIS4500-4P4T`、`ECIS4500-8P4F`）、**Planet**（`BSP-300` 太阳能 PoE、`IGS-801T`、`ISW-1022MT`、`WGS-804HP`、`IGS-5225-16T4S`）、**ORing**（`RGPS-R9244GP+-P`、`IGPS-1042GPA`、`IGPS-9084GP-LA`、`IGPS-7084GP`、`IGS-3032GC`、`IGS-3044GC`）、**Dahua**（`PFS3106-4ET-60`、**`PFS4207-4GT-DP`**）、**Harting**（`20 77 208 4009` mCon M12）。

- ⚠ **`RGPS-R9244GP+-P` = ORing 工业机架 24×PoE+ 带 4×10G SFP+** → **"工业没有 10G 上联"这句话在它的在售清单里已被 ORing 填上，不能用。** 要用的是「**工业 + 10G + 2.5G + bt 同时具备**」。
- ⚠ **`PFS4207-4GT-DP` = 4 口 802.3bt，单口 90 W，总 120 W**（页面原文）→ **Nokta 体系里已有 90 W 单口**。我方 bt 话术要盯「**全口 60 W + 总 800 W**」，**不要比"单口最高功率"**。

---

## 三、WINET 复核：426 个 SKU 的主体是**无源光**，交换机近乎孤例

WINET 子类计数（页面原文）：Breakout SM/MM **53** · Patchcord Duplex SM **37** · **PoE 注入器 & 适配器 22** · Patchcord Simplex SM 19 · Role/SSR 16 · 电源 & PSU 16 · 室外光缆 16 · 通用光缆 16 · OM3 15 · 保险/断路器 15 · 电子自动化 15 · LoRa 14 · 技术支持 13 · 控制卡 13 · 手工具 12 · PLC 分条 11 · **SFP+ 10G 11** · 室外箱 11 …

1. **WINET = FTTx 现场物料商**（无源光 + PoE 注入器 + 电源 + LoRa + 工具），**不是交换机品牌**。
2. r48 写的"少量交换机"应改为 **"交换机近乎孤例"**（已见子类中没有 ≥2 SKU 的交换机类目）。
3. ⭐ **最锋利的一句**：它自己就卖 **22 个 PoE 注入器 SKU**，`RG-POE-AT30` = **$21**，WINET 8 口 PoE = **2,916.76 ₺** →
   **用 `EW-EPIS3910-8GE` 打"1 台顶 4 个注入器 + 4 条线 + 4 个电源 + 能远程重启"**，而不是打"8 口更便宜"。

---

## 四、Cifocs：证据权重**下调为五五**（仍不作定论）

`cebecigrup.com/markalar/` 品牌墙原文 **13 个品牌**：
**argus · BitStream · cifocs · cmg · greenlee · intercoax · Kingfisher · Maisvch · micos · PatchSee · tempo · trend-networks · vesala**

- ⚠ **对"自有品牌"不利**：Cifocs 与 12 个**明确的外国品牌**并列，**无任何 "kendi markamız / our brand" 标注**。
- 支持"自有/独家"的仍是：**`CFC-*` 自家编号 + 官方「Ürün Kodu」内部码**（`OPT-008`、`OPT-013`、`RSC-049`、`RSC-050`），而代理品牌一律用原厂型号。
- → **判定：五五，维持"推定"。客户可见文本一律不写"自有商标"。**
- **唯一未解阻塞项**：TÜRKPATENT 公开检索需图形验证码/会话，`fetch_page` 直连失败 → 交给人手一次查询或打电话问。

---

## 五、r50 待办（ROI 排序）

1. **`noktaelektronik.com.tr/urunler/endustriyel-ethernet-3` 第 2–3 页**（50 个工业产品只读了 20 个）→ 补齐工业段全表。
2. **`erete.com.tr` 分类 68（L2）、71（PoE）、99（Fiber）、95/96/97/98** → 确认 Edgecore/XPS 的完整比例。
3. **`wi.com.tr` WINET 折叠子类补全** → 确认交换机 SKU 数（是否只有 `OEM-8-PORT-GB-POE` 一款）。
4. **`Cifocs` 商标**：TÜRKPATENT 人工检索 / 电话问 Cebeci。
5. **Perpa 三家（Nokta / Cebeci / Zeytek）地理与上下游关系图**。

---

**相关文件**：`117-customer-catalog-forensics-2026-11-01.md`（r48 型号级清单）· `116-b-a-model-mapping-2026-11-01.md`（档位级对位 + 缺口矩阵，**工业宽温行已按本文修正**）
