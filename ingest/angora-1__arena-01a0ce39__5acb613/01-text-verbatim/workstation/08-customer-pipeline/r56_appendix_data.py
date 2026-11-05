# -*- coding: utf-8 -*-
"""r56 补录（2026-11-01）：Koza 关格（TRENDnet 5 款）+ FS Grup 身份 + MOQ/交期武器。"""

D = {}

# ---------------- B / 015 Koza ----------------
D['15'] = """
### ⭐⭐ r56：Koza 关格 —— **它卖 TRENDnet，5 个型号，全部百兆**

前两轮（r47 / r54）只确认了「有 PoE Switchler 类目」但取不到型号。本轮改用**站内搜索**（OpenCart 路由）拿到全表：

`kozaguvenlik.com.tr/index.php?route=product/search&search=poe+switch&limit=50` → **共 5 个型号，全部 `TRENDnet TN-*`**

| 型号 | 端口 | PoE 预算 | 交换容量 |
|---|---|---|---|
| `TN-P08G` | **8×10/100 PoE** + 2×GE 上联 | **120 W** | 1.8 Gbps |
| `TN-P08FG` | 8×10/100 PoE + 1×GE + 1×SFP | — | — |
| **`TN-P16M`** | **16×10/100 PoE** + 2×GE | **360 W** | 8.8 Gbps |
| `TN-P16MG` | 16×10/100 PoE + 2×GE + 2×SFP | — | — |
| **`TN-P24MG`** | **24×10/100 PoE** + 2×GE + 2×SFP | — | — |

#### 结论（三条）
1. **Koza 无自有品牌** —— 它的 PoE 线是 **TRENDnet**（美国品牌，中国代工），**不是贴 Koza 牌**。
2. **全线 100M、全线非管理、af/at 30 W、无 2.5G、无 bt、无云。**
3. ⭐ **最干净的一刀**：**24 口那台 `TN-P24MG` 仍是百兆** ⇒ **`EW-S1927CG-AP`（24 口 GE PoE + 300 m + Watchdog）一对一换**。

#### 场景判断
它做 **Teletek（防盗/消防报警）+ AJAX + Kodicom（摄像/NVR）**，PoE 只用于**给摄像头与 AP 供电**，**不需要 2.5G**。
→ **首封只讲 GE + 300 m + Watchdog**；**不要一上来讲 2.5G**（会把话题带到它不关心的方向）。

**首封**：`TN-P24MG (100M) yerine 24 port Gigabit PoE — aynı fiyat bandında`
**必问**：① TRENDnet 是独家吗？② 每年 24 口走多少台？③ 要不要网管版做项目？

### 证据等级（r56）
- 已核实：**5 个型号与端口/预算**（站内搜索结果页原文）。
- 仍空白：`TN-P24MG` 的 PoE 预算与实价、TRENDnet 代理层级。
"""

# ---------------- B / 062 Cebeci（品牌方落地主体查清） ----------------
D['62'] = """
### ⭐ r56：它的品牌方在土耳其的落地主体查清了 —— **FS Grup Bilişim（2017 年成立，安卡拉）**

| 项 | 证据 |
|---|---|
| 主体 | **FS GRUP BİLİŞİM LİMİTED ŞİRKETİ** |
| 成立 | **2017 年**（`fsgrup.com.tr/about-us` 原文：「şirketimiz 2017 yılında kurulmuş olup lider markalar ile anlaşmalar sağlamıştır」） |
| 地址 | **Cevizlidere Mah. 1243. Sokak No:6/4 Öveçler / ANKARA** |
| DMO 目录 | **FOREDGE (12) 个条目**（含 `S5700-24GP-4TFR`、`S5700-48GP-4TFR`、`SF412A-LC-10KM` SFP）+ MILESIGHT (1) |
| 性质 | **经销商/集成商**，**不是 FOREDGE 的分公司或子公司** |

#### 意义（对 r54/r55 的「300 渠道」说法降温）
- FOREDGE 官网自述 **「300+ yurtiçi kanal ortağı」** 是**品牌方口径**；
- **在土耳其能查到它进货的唯一主体只有 FS Grup**，办公地址是**安卡拉 Öveçler 的一间办公室**，DMO 只有 **12 个 SKU**；
- ⇒ **它是「一个能进 DMO 的安卡拉伙伴」，不是全国性组织。**
- ⇒ **我方的现实路径**：**找 FS Grup 的同类（能进 DMO 的安卡拉/伊斯坦布尔 IT 经销商）合作**，而不是幻想直接铺 300 家终端。

#### 对 Cebeci 的话术（r55 已改写，本轮补一句）
**首封第三句加**：`FS Grup / Foredge kanalını biliyoruz — sizin için daha düşük MOQ ve daha hızlı sevkiyatla aynı DMO uyumunu kurabiliriz.`

### 证据等级（r56）
- 已核实：**FS Grup 成立年份、地址、DMO 12 个 FOREDGE 条目**（`fsgrup.com.tr` + `dmo.gov.tr` 原文）。
- 仍空白：FS Grup 与 FOREDGE 的**代理协议性质**（独家/非独家）、FOREDGE 土耳其**是否有第二个进货主体**。
"""
