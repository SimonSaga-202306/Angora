# 125 · 「MOQ 1 台 / 5 天」——我方唯一还成立的硬武器（r56 · 2026-11-01）

> r55 的结论是：对 FOREDGE，我方在规格上**没有一项碾压**，只剩「更低 MOQ、更快打样、更低价格」。
> r56 把这句话**变成了数字**，并且顺手关掉两个悬了三轮的空格（**Koza 的型号**、**FS Grup 的身份**）。

---

## 一、⭐⭐⭐ 本轮最重要的一条：**MOQ 1 台 vs 500 台；5–7 天 vs 42–56 天**

| 项 | Ewind（阿里店铺原文） | FOREDGE（官网原文） |
|---|---|---|
| **MOQ** | **「Min. Order: 1 piece」** | **「MOQ 500 adetten başlar」** |
| **交期** | **1–20 台 = 5 天；21–50 台 = 5 天；51–100 台 = 7 天** | **6–8 周（42–56 天）** |
| **打样** | **3–7 天**（rapid sampling） | 未承诺 |

⇒ **倍数关系：MOQ 500× 优势、交期 6–10× 优势。**
⇒ **这就是首封信的第一句**（土耳其语）：
> `Foredge 500 adet ve 6–8 hafta istiyor. Bizde MOQ 1 adet, sevkiyat 5–7 gün.`

⚠ **但要把话说准**（避免夸大）：这是我方**阿里零售挂单口径**，不等于对土耳其经销商的正式政策。**对经销商仍应按 100–200 台试单承诺**，并明确「试单后转量产」的阶梯。
⚠ **诚实边界**：如果客户要的是 **500 台以上、且能等 8 周**，**我们的 MOQ 优势归零**，只剩价格。

### 由此算出的渠道尺子（`126` 见 `07-web-crawl.../alibaba-moq-leadtime-price`）
| 我方 FOB | 土耳其零售（r54 实测） | 倍率 |
|---|---|---|
| 24 口 GE PoE **$95–106** | Besta **$208–223** / ALFA **$194** / `F2420GBL-A` **$424** | **2.0× – 4.0×** |

→ **客户报价低于 FOB×2 = 在压价；高于 ×4 = 他赚太多、我方有提价空间。** 这是本轮最实用的一把尺子。

---

## 二、⭐⭐ `FS Grup Bilişim` 身份查清：**2017 年成立的安卡拉 IT 经销商，不是 FOREDGE 分公司**

| 项 | 证据 |
|---|---|
| 主体 | **FS GRUP BİLİŞİM LİMİTED ŞİRKETİ** |
| 成立 | **2017 年**（自家 `fsgrup.com.tr/about-us` 原文：「şirketimiz 2017 yılında kurulmuş olup lider markalar ile anlaşmalar sağlamıştır」） |
| 地址 | **Cevizlidere Mah. 1243. Sokak No:6/4 Öveçler / ANKARA** |
| DMO 目录 | **FOREDGE (12) 个条目**（含 `S5700-24GP-4TFR`、`S5700-48GP-4TFR`、`SF412A-LC-10KM` SFP）+ **MILESIGHT (1)**（安防类） |
| 性质 | **经销商/集成商**，非品牌方 |

### 这对 r55 的「300 渠道」判断意味着什么（**修正语气，不是推翻事实**）
- FOREDGE 官网自述的 **「300+ yurtiçi kanal ortağı」** 是**品牌方口径**；
- 但**它在土耳其的 DMO 落地只有 FS Grup 一家**（12 个 SKU），**地址是安卡拉 Öveçler 的一间办公室**；
- ⇒ **"FOREDGE 已在土耳其布下 300 家渠道"这个印象要降温**：**它有一个能进 DMO 的安卡拉伙伴，但不是一个全国性组织**。
- ⇒ **我方的现实路径**：**找一个同样能进 DMO 的安卡拉/伊斯坦布尔伙伴**（FS Grup 的同类），而不是幻想直接铺 300 家。

---

## 三、⭐⭐ `Koza` 关格（三轮未取到，本轮用站内搜索拿到）

`kozaguvenlik.com.tr/index.php?route=product/search&search=poe+switch` → **共 5 个型号，全部 TRENDnet**：

| 型号 | 端口 | PoE 预算 | 交换容量 |
|---|---|---|---|
| `TN-P08G` | **8×10/100 PoE** + 2×GE 上联 | **120 W** | 1.8 Gbps |
| `TN-P08FG` | 8×10/100 PoE + 1×GE + 1×SFP | — | — |
| **`TN-P16M`** | **16×10/100 PoE** + 2×GE | **360 W** | 8.8 Gbps |
| `TN-P16MG` | 16×10/100 PoE + 2×GE + 2×SFP | — | — |
| **`TN-P24MG`** | **24×10/100 PoE** + 2×GE + 2×SFP | — | — |

#### 结论
1. **Koza 没有自有品牌** —— 它卖 **TRENDnet**（与 r47 判定的"PoE 梯度太薄"一致，但**数量是 5 个，不是"几款"**）。
2. **全线 100M、全线非管理、全线 af/at 30 W、无 2.5G、无 bt、无云。**
3. ⭐ **最干净的一刀**：**24 口那台还是百兆**（`TN-P24MG`）⇒ **`EW-S1927CG-AP`（24 口 GE PoE）一对一换**。
4. 场景匹配：它做 **Teletek 报警 + AJAX + Kodicom 摄像**，**PoE 是给摄像头/AP 供电**，**不需要 2.5G** → **先卖 GE + 300 m + Watchdog**，不要一上来讲 2.5G。

**首封**：`TN-P24MG (100M) yerine 24 port Gigabit PoE — aynı fiyat bandında`
**必问**：① TRENDnet 是独家吗？② 每年 24 口走多少台？③ 要不要网管版做项目？

---

## 四、DMO 里 BDCOM / 工业段的补点（`123` §四 的延伸）

DMO 目录里 **BDCOM 未见独立条目**，但土耳其渠道完备：
- **Öncü Güvenlik（oncub2b）= BDCOM 土耳其分销**：`IES2000-TU12S4T`（**12×GE SFP + 4×GE TX，256 Gbps**，AC/DC 混合供电，**IP40**，**IEEE 1588v2 PTP**）· `IES2000-TU8S8T`（8 GE + 8 SFP，**−40~85 °C**，52 Gbps，220×150×44 mm）· `IES200-V25-2S8P`（4 PoE+ + 2 SFP）· `IES200-LSTW2080P`（8 PoE + 2 SFP，48–55 V 冗余，**6 kV 防雷**）；
- **ASR Teknoloji** 也卖同系；
- **上海 Baud Data（BDCOM 原厂）阿里报价**：`IES2000-TW8S8P`（L3，8 PoE + 8 SFP）**≥5 台 $399**。

⇒ **工业段的价格锚**：**8 口 PoE + 8 SFP 的 L3 工业机，原厂 FOB ≈ $399**。
⇒ **我方 `EW-PIS3810M-8GE-BT` / `EW-EPIS3910-8GE` 的工业报价应参照 $399 上下**，而不是按整机 PoE 预算去加价。
⇒ **它没有 bt、没有云** ⇒ 工业段我方仍有 60 W + 云两张牌（与 `124` 的结论不冲突：**消费/企业段没有牌，工业段还有**）。

---

## 五、本轮新增的**销售纪律**（五条，写进所有首封信）

1. **第一句就说 MOQ 与交期**（1 台 / 5–7 天 vs 500 台 / 6–8 周）。
2. **报价用 FOB×2–4 的尺子**校验客户给的目标价。
3. **不比工厂规模与认证数量**（会输），比**打样、试单、RMA、文档转品牌**。
4. **对 Koza / 类似 TRENDnet 渠道：只讲 GE + 300 m + Watchdog**，不讲 2.5G。
5. **对工业客户：把 $399 当 FOB 锚**，主打 **60 W bt + 云 + 单口远程重启**。

---

## 六、r57 待办

1. **FS Grup 的同类**：找 **能进 DMO 的安卡拉/伊斯坦布尔 IT 经销商**（这是复制 FOREDGE 路径的唯一办法）。
2. `ewindnet.en.alibaba.com` **270+ SKU 的 MOQ / 阶梯价逐条抓取**（本轮只有索引口径）。
3. **两个阿里店铺是否同一主体**（营业执照 / 统一社会信用代码）。
4. **DMO 工业段全表**（BDCOM 为何不在册、MOXA `EDS-G512E-8PoE-4GSFP-T` 的合同价）。
5. **TÜRKPATENT 六商标**（仍 CAPTCHA，需人工）。
6. 承接：upTech `ISW` 工厂、ErETE `/99` Fiber + `/95`–`/97`、ORing–Nokta 独家、`XPS-1320-*PH` 功率、WINET SKU 数、`A/072` Lemax 决策、Technopc 未上架 SKU。

---

**相关文件**：`124`（FOREDGE 全档，本文 §二 修正其"300 渠道"语气）· `123`（价格锚点）· `07-web-crawl-2026-11-01/ewind/channels/alibaba-moq-leadtime-price-2026-11-01.md`（本文 §一 的数据来源）· `121` · `120` · `116`
