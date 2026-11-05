# 121 · 「自有品牌」大清算：谁真的是自有品牌（r52 · 2026-11-01）

> **这一轮把过去 40 多轮一直在用的一个词彻底拆了**：土耳其客户嘴里的「自有品牌」，到底是指**自己注册的商标**，还是**自己在独家分销的深圳品牌**。
>
> 结论：**四家里三家不是自有商标。** 而且这个错误会直接影响谈法——**对"代理"谈 OEM 是错的方向**（它有上游、能换供应商），**对"自有商标"谈 OEM 才对**（它要的是产品，不是品牌授权）。

---

## 一、⭐⭐ Telkolink / GelecekBT：**它是我方在土耳其最强的对手，不是最好的客户**

### 1. 目录规模（`gelecekbt.com/anahtarlar` facet 原文）

| 分类 | SKU | 分类 | SKU |
|---|---|---|---|
| Ethernet Switch | **122** | Ethernet POE Switch | **126** |
| Endüstriyel Switch | **73** | Endüstriyel POE Switch | **60** |
| Endüstriyel Omurga | **10** | Omurga Fiber Switch | **57** |
| 10Gigabit Switch | **104** | **Multirate（1G/2.5G/10G）** | **15** |
| SFP Modül | **112** | **POE Switch AI** | **22** |
| PD POE Switch | 7 | | |

→ **交换机 ≈ 291 SKU**，**25 个品牌**，其中 **`CLR Networks` 193 个**。
代理品牌（facet 原文）：CLR Networks · **D-Link · Huawei · HP/Aruba · Netgear · Fortinet · Zyxel · Cisco · TG-NET · Repotec · Planet · Moxa · Advantech · 3Onedata · Kyland · Hirschmann · Harting · Siemens · Schneider · Allied Telesis · Axis · Ruijie**。

### 2. ⭐ 品牌真相：CLR 不是它的自有商标

- 它自家幻灯片原文：**「CLR Networks Türkiye dağıtıcısı GelecekBT'dir」**；
- `guvenlikonline.com` 企业页：**「CLR Networks、ONET、Telkolink、Netkablo gibi markaların Türkiye dağıtıcısıdır」**。

→ **CLR = 深圳品牌，GelecekBT 是土耳其分销商。** 本档旧记「自有品牌 CLR」应改为 **「独家/代理分销的深圳品牌」**。

### 3. 🛑 三项自我证伪（推翻 `116` 的三行）

| 原判断 | 实测 | 结论 |
|---|---|---|
| **2.5G：11 家 0 家** | ❌ **整条 2.5G 线**：`CLR-MRS-8106N`(5×2.5G+1×10G)、`-8106P`(4×2.5G PoE+1+1)、`-8109N`(8×2.5G+1×10G)、`-8109P`(8×2.5G **PoE** 100 W)、`-8218N`(16×2.5G+2×10G Web 管理)、`-8226N`(**24×2.5G**+2×10G)、`-8312N/P`(8×2.5G + **2×10G RJ45 + 2×10G SFP+ L3**)、`-8330N/P`(**24×2.5G PoE + 6×10G SFP L3**)、`CLR-SWT-80F`(8×1.25/2.5/10G SFP+)；**另有 `CLR-DCS-2110N/P` = 24×2.5G + 100G 上联 L3** | 2.5G **已被它做满** |
| **bt：只有 1–4 口** | ❌ facet：`Tip3 60W` **3** · `Tip4 90W` **1** · `802.3bt` **6**；`CLR-SWF-9006BT` **96 W** | bt 已到 **90 W 单口** |
| **云管理：0 家** | ❌ facet `Cloud` **15** · `Yapay Zeka` **12**；`CLR-SWT-5736F/3754F` 标 **L3 Cloud** | 云已在线 |
| **40/100G：0 家** | ❌ 100G 上联 **6** · 100G 交换机 **9** · 400G **1**；`CLR-DCS-6332F/6432F` = **32×40/100G QSFP28** | 已在卖 100G/400G |

→ **`116` 的六行缺口矩阵对 Telkolink 完全不成立。** 它是全名单技术水位最高的一家，**也是我方最直接的对手**（同为深圳 ODM、同一客群、同一货架）。

### 🛑 r53 修正（取代本节第 4 点里的两处）

r53 拿到 `CLR-MRS-8330P` **完整技术表**，推翻 r52 的两条：

| r52 原文 | r53 实测 | 判定 |
|---|---|---|
| 「**没有一款 2.5G SKU 标 802.3bt**」「`-8330P` 功率未知」 | **`24×2.5G PoE（1–4 口 bt 90 W）+ 6×10G SFP+`**，**总 PoE 400 W**，整机 max 52 W | ❌ **推翻** |
| 「2.5G PoE 只有 100 W」 | 100 W 是 8 口 `-8109P`；24 口那台 **400 W** | ❌ 口径错 |

→ **真正的缝改写为**：**「24 口全 bt + 800 W」**（它 24 口里只有 4 口 bt、预算 400 W、均摊 ≈16.7 W/口），外加 **L3 只到静态路由（无 OSPF/VRRP）**、**工作温度仅 −10~50 °C（商用机箱）**。

→ **同时必须承认它有两档比我方齐**：**`CLR-SWT-7514C` = 12×10G RJ45 全 10G 网管**、**`CLR-IES-T120N` = 12×1G/10G SFP+ 工业骨干（240 Gbps，−40~85 °C）**。这两档不要正面比。详见 `122` §一/§二。

### 4. 它真正还缺的（我方机会，只有四条）

1. **2.5G PoE 的功率**：`-8109P` 仅 **100 W**；⚠ **r53 更正**：`-8330P` 不是「无标注」，而是 **400 W / 仅 1–4 口 bt 90 W** → 我方 **`EW-PIS5728GM-AP-BT`（24 口 bt / 800 W）** 仍是唯一一档。
2. **工业 bt 几乎空白**：73 个工业款里 `802.3bt` 只有个别、**90 W 单口只有 1 个** → `EW-PIS3810M-8GE-BT`。
3. **`POE Extend` 18 / `POE Watchdog` 14（291 个 SKU 里）** → 我方 **300 m 拨码 + Watchdog 全系标配**是"低成本高感知"差异点。
4. **SFP 112 个 SKU 是它的现金牛** → 我方 2.5G SFP / 10G SFP+ / 工业 SFP 可齐套供。

### 5. 打法定稿（彻底改写）

| 之前（错） | 现在（对） |
|---|---|
| 「它缺 2.5G/bt/云，我方去补位」 | ❌ 它全都有 → 改口 **「同档位、更低 ODM 成本 + 可贴 CLR 牌」** |
| 当纯客户 | ⚠ **一半客户、一半竞对**（同一深圳供应链）→ **不交完整 BOM 与成本结构** |
| 谈技术领先 | ✅ 谈 **交期 / MOQ / 贴牌弹性 / 2.5G+bt 组合 / SFP 齐套** |

**首封**：`CLR hattı için ikinci kaynak: 2.5G PoE + 802.3bt (60/90W) + SFP 套件`
**必问**：① CLR 是否独家？② 2.5G 线年走多少台？③ 工业 90 W bt 有没有客户在问？

---

## 二、⭐⭐ CryptoLink：`CRL` 也不是自有品牌 —— datasheet 页脚印着 **Authorized Dealer**

- 7 份 PDF **页脚全部**是：**`CryptoLINK.  Authorized Dealer | Cryptolink Elektronik Güvenlik Sistemleri San ve Tic. Ltd. Şti`**；
- `CRL-SW-2402` 页眉出现 **`Cryptol.net`** 字样 → **CRL 属于第三方（深圳 Cryptol 系），CryptoLink 是授权经销商**。

→ 本档旧记「CRL 线 … switch+SFP+MC 全自有」**改为「代理品牌」**。

### 规格（datasheet 原文）

| 型号 | 规格 |
|---|---|
| ⭐ **`CRL-SW-L3-2404-10G`** | **24×GE PoE + 8×Combo TP/SFP + 4×10G SFP+ + 1 Console**；**BCM 芯片**；**128 Gbps / 96 Mpps**；MAC 12K；**总 360 W**；**af/at 仅 30 W**；ARM Cortex-A9 / 256 MB；**静态 + RIP + OSPF + VRRP**；−20~50 °C |
| 变体 `-8C` / `-8C-POE` | 24×1000M SFP 全光版 / 24×GE PoE 版 |
| **`CRL-SW-2402`** | 24×100/1000 **PoE**（af/at 15.4/30 W）+ **2×SFP**；52 Gbps；**总 300 W**；VLAN/Trunk；1–8 口 QoS；**防雷 6 kV / 差模 4 kV / ESD 15 kV** |
| `CRLISW-08` / `CRLISW-14P` | 工业 8 口 / 8 口 PoE |
| `CRL-SFP-10G-LC` / `CRL-SFP-125 LC` / `CRL-MC02` | 10G / 1.25G 模块 / 媒体转换器 |

**对位**：`CRL-SW-L3-2404-10G` → **`EW-S2926GM-AP`**（24 PoE + 4 Combo + 2 SFP）或升级 **`EW-S5748GM-AP`**（48 PoE + 4×10G）；`CRL-SW-2402` → `EW-S1927CG-AP`；`CRLISW-14P` → `EW-PIS1810-8GE` / `EW-EPIS3910-8GE`。
**它的客户是边界安全/车牌识别/政府项目** → **工业宽温、冗余电源、防雷** > 云。首封就谈这两条。

---

## 三、⭐ TekniksatGroup（TGD）：24 V 被动 PoE 的"一对一对位"

TGD PoE 线全表：`TGD-P4/24`（**4 口 24 V 被动**，`1,2+ / 3,6−`）、`TGD-P8S/24`（**8 口 24 V 被动**）、`TGD-P4/48`、`TGD-P8/48`、`TGD-P16S/48`、`TGD-P24S/48`、`TGD-P424/824/848`、`[SWITCH]` 5 口非网管。

**关键上下文**：它的主体业务是 **IP 对讲**（`TGD-7IP24 / 7IP48` 7 吋 IP 主机、`TGD-4K24` 门面板、`TGD-GU10 S1`、`TPS 9/x` 多开关）→ **TGD 交换机是给 24 V 对讲配套的**，所以：
- **24 V 被动 PoE 是刚需**；
- 全线**非网管**，**没有云 / 远程重启**；
- 自述 **「Üretim tasarım uygulama %100 yerli」** → 对"谁做的"敏感，**OEM 要先谈"贴 TGD 牌 + 你方负责本地化文档与保修"**。

### 对位（本轮最干净的一次）

| 它的型号 | 我方 | 为什么是"最强一刀" |
|---|---|---|
| `TGD-P4/24`（4 口 24 V 被动） | ⭐ **`EW-EPIS3910-8GE`** | **1–2 口 DIP 选 12/24 V 被动 + 3–6 口 48V 30W + 7–8 口 48V 60W + 云 + 单口远程重启** —— 它要用三台机才凑得齐 |
| `TGD-P8S/24` | 同上 | 同上 |
| `TGD-P8/48` | `EW-S1710FG-AP` | + 300 m 长距 + Watchdog |
| `TGD-P16S/48` | `EW-S1616CGU` / `EW-PIS3620M-16GE` | 可工业宽温 |
| `TGD-P24S/48` | `EW-S1927CG-AP` / `EW-S2926GM-AP` | 网管 + bt |

**一句话卖点（对讲专用）**：**"对讲主机死机不用上门——云平台点一下重启那个口。"** 这是它整条 TGD 线**完全没有**的能力，而对讲/门禁恰恰最需要远程重启。

---

## 四、⚠ 由此得出一条**通用判据**（写进所有 A 档判断）

| 现象 | 实际身份 | 谈法 |
|---|---|---|
| 有自己的**型号命名体系**（`NVC-`/`SWP-`/`LNG`/`TGD-`/`CRL-`/`CFC-`） | 可能是自有，也可能是代理 | **必须查商标** |
| datasheet 页脚写 **"Authorized Dealer"** | **一定是代理** | 谈"二供/替换它上游"，不谈 OEM |
| 官网写明 **"X markasının Türkiye dağıtıcısı"** | **一定是代理** | 同上 |
| 有 **TÜRKPATENT 注册号**（如 upTech **2008/13951**） | **真自有** | 谈 OEM 贴牌成立 |

**已核结论**：`upTech` = **真自有**（商标 2008/13951）· `CLR` = **代理** · `CRL` = **代理** · `Cifocs` = **五五推定（未查）** · `Dayline` = **未查** · `NVC/SWP/LNG/TGD` = **未查商标**。

→ **r53 第一件事：一次 TÜRKPATENT 查询把 `Cifocs / Dayline / TGD / NVC / SWP / LNG` 六个全查了。**

---

## 五、r53 待办

1. **TÜRKPATENT 商标**：`Cifocs`、`Dayline`、`TGD`、`NVC`、`SWP`、`LNG`（一次查六个）—— 决定哪些能谈 OEM。
2. `gelecekbt.com` 剩余 facet 与 `POE Switch AI`(22)、`PD POE`(7) 全表
3. `CRLISW-08/14P` datasheet（已有 PDF 未读）+ `CRL-MC02`
4. B 档"已在卖交换机"11 家 → 型号级（Coptek / NFS / iotsistem / Eurocam …）
5. `A/075 Technopc`（工业 PoE 采购 E-wind）→ 它给客户的整机型号

---

**相关文件**：`116`（缺口矩阵，**2.5G / bt / 云 / 100G 四行已按本文重写**）· `120`（r51 A 档四家自有线）· `119`（r50 全站点算）· `118` · `117`
