# 119 · ErETE 全站型号台账 + upTech 工业全表 + WINET 枚举硬边界（r50 · 2026-11-01）

> **本轮性质**：把 r49 的两条**过度结论**收回，并把 ErETE 的产品树**逐分类点完**。
> 一句话结论：**ErETE 是 Edgecore 主导型分销商，自有 XPS 只占接入段的一部分，而且 XPS-1320 已经有 10G 上联** —— r49 说的"XPS 无 10G""东边 XPS 打接入"两句都要改。

---

## 一、ErETE 全站型号台账（12 个分类逐个点算）

| 分类 ID | 名称 | 产品数 | 品牌构成（本轮实见） |
|---|---|---|---|
| 33 | Omurga Switchler（骨干） | **8** | Edgecore ECS **5** + 自有 `XPS-1320-36F` **1** + 其余 |
| **34** | **Kenar Switchler（边缘）** | ⚠ **0** | **空分类**（导航有入口、无产品） |
| 68 | Yönetilebilir L2（网管 L2） | **12**（首页显 7） | **全部 Edgecore**：`ECS4210-12T/28T`、`ECS4110-52T`、`ECS4510-28T/52T`、`ECS4120-28T/52T` |
| 69 | Yönetilebilir L3（网管 L3） | **6** | **全部 Edgecore**：`ECS4610-26T/50T`、`ECS4620-28T/52T` |
| 70 | WebSmart | **9** | Edgecore `ECS2100-10T/28T` + 自有 **`XPS-1110-18/26`（仅 10/100TX 百兆）** |
| **71** | **PoE Switchler** | **16** | ⚠ **全部 Edgecore**：`ECS2100-10P`(125 W)、`ECS2100-28P`、`ECS2100-28PP`(400 W)、`ECS4210-12P/28P`、`ECS4110-52P`、`ECS4620-28P/52P` … |
| 94 | L2+ PoE（网管） | **5** | **全部自有 XPS-1220**：`-10P / -18P / -26P / -26PH / -52P`（GE + 1G SFP） |
| **98** | **L2+（网管，非 PoE 类目）** | **11** | **全部自有 XPS**：`XPS-1220-10/18/26`（GE+1G）· **`XPS-1320-28P / 28PH / 36P / 36PH / 52P`（PoE + 4×10G 或 8×SFP）** · `XPS-1320-28 / 36 / 52`（非 PoE + 4×10G） |
| 102 | OPEN NETWORKING | **7** | **全部 Edgecore**（`Wedge100BF-32X`、`AS7712-32X`、`AS6712-32X`、`AS5712-54X`、`AS4610-54T/54P`、`ASXvOLT16`） |
| 107 | NOS | **1** | `OcNOS 6.6`（IP Infusion） |
| 99 | Fiber Switchler | 抓取失败 | **未取**（需重试） |
| 95 / 96 / 97 | 非管理 PoE / 非管理 / WebSmart PoE | **未取** | — |

**粗算比例**：已点到的 **Edgecore ≈ 46 款**（L2 12 + L3 6 + PoE 16 + 骨干 5 + ONIE 7），**自有 XPS ≈ 19 款**（1110×2 + 1220×5 + 1320×11 + 骨干 ×1）。
→ **Edgecore : XPS ≈ 2.4 : 1。**
→ ⚠ **r49 的「东边 XPS 打接入 / 西边 Edgecore 打 DC」这个二分法太干净了**：**PoE 主力（16 款）全部是 Edgecore**，XPS 只在**"L2+ PoE 网管"这一个细类（5 款）**和**"L2+ 网管"里带 PoE 的（5 款）**出现。
→ **正确说法**：**Edgecore 是主轴（含 PoE 与接入），XPS 是"补口的自有线"**。

---

## 二、⚠ 两处必须回收的 r49 结论

### 回收一：「XPS 全线无 10G 上联」——**错**

`XPS-1320` 系列**明确带 4×10G SFP+**（分类 98 五款 PoE 型号的页面标题原文）：`XPS-1320-28P` = **24 port GE PoE + 4 port 10G SFP+**，`XPS-1320-52P` = **48 port PoE + 4 port 10G SFP+**；`XPS-1320-36P/36PH` = 24 PoE + **8×100/1000 SFP**；`XPS-1320-28/36/52` 为非 PoE 版同样 4×10G。

→ **能说的只剩三条**：**① 无 2.5G ② 无 802.3bt（最高 at / "PH" 高功率档）③ 无云管理**。
→ **"无 10G"不能说**，一说就被 `XPS-1320` 打脸。

### 回收二：「WINET 交换机近乎孤例」——**证据不足，撤回**

- `wi.com.tr/kategori/switch-poe-switch?brand=winet` 及两个子类 **商品列表返回 `No results found`**（前端 JS 渲染，`fetch_page` 取不到条目）；
- `wi.com.tr/sitemap.xml` **只有 20 个栏目页**，**没有任何商品 URL** → 无法反查；
- facet 计数**被无关品类污染**（PoE 交换机分类里混入 Wi-Fi 6 AP 的 2.4 GHz 速率、UniFi 云管理等字段）→ **facet 不能当作 SKU 计数用**。

→ **r49 的"交换机近乎孤例"没有证据支撑，撤回**。正确表述：**WINET 自有交换机的数量在公开面无法枚举**（唯一确证的是 `OEM-8-PORT-GB-POE`），**且 facet 里出现过 48 口 PoE / 10G SFP+ / 云管理 / 370 W 这类字段，说明它至少不止 8 口一档**。
→ **WINET 一条改为"公开面不可枚举 = 硬边界"**，不再作为"空白机会"论据。

---

## 三、upTech 工业线全表（50 个产品读完 3 页，upTech 仅 8 款）

| 型号 | 形态 | 我方对位 |
|---|---|---|
| `ISW2420-GGS` | L2 网管 4×GE + 2×GE SFP | `EW-PIS1805-4GE` |
| `ISW2420-GGSP` | L2 网管 4×GE **PoE**(af/at) + 2 SFP | `EW-PIS1805-4GE` / `EW-EPIS3910-8GE` |
| `ISW2820-GGS` | L2 网管 8×GE + 2 SFP（IP40，−40 °C） | `EW-PIS1810-8GE` |
| `ISW2820-GGSPV` | L2 网管 8×GE **PoE** + 2 SFP | `EW-PIS1810-8GE` |
| **`ISW2840-GGSP`** | L2 网管 8×GE **PoE** + **4×GE SFP** | `EW-PIS1810-8GE`（升级：4 SFP） |
| `ISW21240-GGS` | L2 网管 12×GE + 4×GE SFP | `EW-PIS3620M-16GE` |
| `ISW1820-FGSP` | **非管理 8×百兆** PoE + 2×GE SFP | `EW-PIS1802-1GE` 系 |
| **`ISW1811-FGSP`** | **非管理 8×百兆** PoE + 1×GE RJ45 + 1×GE SFP | 同上 |

**⭐ 结构性判断（比"某型号对位"重要得多）**
- Nokta 的 `Endüstriyel Ethernet` **50 款里 upTech 只有 8 款**，其余是 **ORing（约 20 款）、Planet（约 12 款）、Dahua（6 款）、Harting（2 款）、Edge-Core（2 款）**。
- → **工业段的"主供"是 ORing，不是 upTech**。upTech 的工业线是**"补位产品"**（型号新、标 `Yeni`、覆盖 4/8/12 口）。
- → ⭐ **我方要争的是"upTech 这块补位"，不是"ORing 那块主供"**：ORing 是客户长期工业主供，动不了；upTech 是新铺的自有牌，**最容易接受新 ODM**。
- 工业段我方三张牌不变：**10G 上联（`EW-PIS5712M-8GE`）、12/24 V 被动 PoE + 云（`EW-EPIS3910-8GE`）、bt 60 W（`EW-PIS3810M-8GE-BT`）** —— upTech 8 款**一款都没有**这三样。

---

## 四、⚠ 全局修正：「云管理」不再是差异化

**原 `116` 缺口矩阵第 4 行写"云管理 / AI PoE：客户侧 0 家"。本轮必须改弱。**

- 事实：**Winet 在卖 Ruijie**（40 SKU，其中 PoE 交换机 11 个），Ruijie 自有 **Reyee / 云平台**；**Nokta 在卖 Dahua / Planet / ORing**，Dahua 有 **DoLynk** 云；`wi.com.tr` 的 PoE 交换机 facet 里就出现了 **"UniFi Cloud Yönetimli: Var"** 与 **"Cloud Mobil Yönetim Var"** 字段。
- → **云管理在土耳其渠道里已经是"配置项"，不是"卖点"**。
- → 我方云管理（`EW-ES*` / `EW-EPIS*`）**不能再作为独立差异化**，只能作为**"同价位附带"**；真正的差异化仍回到 **2.5G / 全口 bt / 300 m 长距 / 12–24 V 被动 PoE** 这四条**硬规格**。

---

## 五、r51 待办（重新排 ROI）

1. `erete.com.tr` **分类 99（Fiber Switchler）** —— 本次 fetch 失败，需重取；95/96/97 同样。
2. **ORing 与 Nokta 的关系**（是否独家代理、有无本地库存）—— 决定"我方能不能挤进工业段"。
3. **upTech 工业线的现工厂** —— 8 款 ISW 全是 `Yeni`，说明**刚上新供应商**，这是最容易切入的窗口（**优先于一切**）。
4. `wi.com.tr` 商品枚举：改走 **Google/Bing 站内索引** 或 **商家后台/API**（站内分类页与 sitemap 都不可用，已封）。
5. Cifocs 商标（TÜRKPATENT 人工）。

---

**相关文件**：`118`（r49 ErETE 供应链收口，**§一 的 10G 与比例两处按本文回收**）· `117`（r48 型号级清单）· `116`（缺口矩阵，**云管理行按本文改弱**）
