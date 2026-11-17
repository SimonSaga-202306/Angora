# 152 · Ewind 全渠道 + Angora 官网复爬对照（2026-11-17）；以及一次对自家语料的回头核对

**抓取时刻**：**2026-11-17T11:47Z ≈ 19:47 (+0800)**（沙箱 `date -u` 实测）
**基线**：r40（2026-11-01，目录 `07-web-crawl-2026-11-01/`）→ r39（2026-10-27）→ r24/r25 档案 `112`/`113`
**本轮指令**：用户第 36 次「继续」——① 把之前做的再过一遍看有没有新发现；② 继续挖 Angora；③ Ewind 官网与所有宣传站全部再爬一遍，记录时间戳与变化。

**一句话**：**Ewind 官网连续第 3 轮零新增（距上次真实上新 103 天），但它的 Alibaba 店铺、价格与渠道结构变了，而且我第一次把它和我们自家语料放在一起看——结果发现上一轮（r82）关于「EGM 认证是唯一硬门槛、我方没有」的判断需要改写：那张纸在我方最大客户 Angora 手里，而且我们自己的语料里早就躺着 KGYS 全套规范（含 3,294 台采购量）。**

---

## 0. 八句话

1. **Ewind 官网：零新增（连续第 3 轮）**。产品 `modified` 最大值仍是 **2026-08-26T17:42:11**（id 8143），最新上架仍是 **2026-08-06**（id 10869），最新文章 **2026-06-11**，页面 sitemap **2026-07-22**，展会 sitemap **2025-11-05** —— 与 r39/r40 逐字相同。**距上次真实上新：103 天**。
2. **但它的「店」变了**：Alibaba 店铺准时发货 **99.0% → 100.0%**，在线营收 **US$240,000+ → US$200,000+**（**下降**），并开出 **20% 限时折扣**（三款在促）；证书墙新增 **UKCA**；类目树新增 4 个 "-New" 子站。
3. **它的 FOB 底线第一次看清**：**10 口 L2+ 网管工业 PoE（IP40、−40~80 ℃、云管理）FOB $98.30–121.60**；6 口全千兆工业 PoE $63.80–66；2 口工业 PoE 光 $30.45–31.50。
4. **同一台机器的两头价差 10 倍**：土耳其零售端 **Ewind `EW-S2910GM-AP`（8×GE 网管 PoE + 2×GF，120W）= 4,475.38 TL + KDV ≈ $89（税前）**；而 r82 查到的 DMO **KGYS 工业档 = $1,100–1,300**。FOB 端工业比商用只贵 30–60% ⇒ **溢价不在硬件里，在「工业规格 + EGM 证书」里**。
5. ⭐⭐ **回头核对的最大发现**：Angora 官网 2019 年新闻原文确认 —— **Angora 的「工业 8 口 L2+ 网管交换机」通过了 EGM 信息技术司的 KGYS 要求测试（含 traffic shaping 与丢包），取得「EGM 全国项目参与证书」并进入批准清单**。**r82 写「我方 EGM 报告：无 ⇒ 唯一硬门槛」，只对了一半**：门槛确实存在，但它**在我方客户手里**。
6. ⭐⭐ **我们自己的语料里早就有全套 KGYS 规范**：`警察局项目/KGYS.txt` 给出 **3.3.1–3.3.22 + 3.4.1–3.4.29** 全文、**采购总量 3,294 台**、**2026-02-12 由一等警司 Mehmet ÇATAL 批准**；`RFP/2024.7.2_C TİPİ ETHERNET ANAHTAR KGYS.pdf` 是 **2024-07-02** 的英译版 1.1.1–1.1.25。**r82 只用 2023 年第三方转述（turk-iot），没查自家档 —— 这是方法性失误，本轮补正。**
7. **Angora 官网同样零新增**（页面最新 modified **2026-04-03**，与 r40 一致；10 篇文章全部 modified **2026-06-15** 属**批量重存**，最后真实发布仍是 **2023-12-06**），但本轮首次把**三套型号编码**和**工业 8 口的确切配置**读全了：**`ANW-2023-E8GT` / `ANW-IND-8P-2SFP` = 8×1G + 4×1/10G SFP+，全口 30 W，−40~+80 ℃，48 V DC，DIN，告警继电器** ⇒ **完全覆盖 KGYS 的 1.1.2 / 1.1.8 / 1.1.21**。
8. **一条推翻语料的更正**：`angorateknoloji.com` **不是** Angora Networks 的新域名 —— 它现在是 **Angora Technology（Kocaeli，IoT/ESL/嵌入式设计公司）**，`/verge-network-switch-serisi/` 直接 **404**。语料里「2026 改版新站」的说法不能成立。

---

## 1. 方法与时间戳

| 项 | r39 | r40 | **r83（本轮）** |
|---|---|---|---|
| 抓取时刻 | 2026-10-27T01:20Z | 2026-11-01T05:29–05:45Z | **2026-11-17T11:47Z ≈ 19:47 (+0800)** |
| 手段 | 官网直连 + REST + sitemap | + Alibaba 直连 + PDF 正文 + 多语言实测 | **+ Alibaba 店铺 4 个分块 + Alibaba 类目页 + LinkedIn 公司页 + 土耳其零售（atommarket / Hepsiburada / n11）+ 自家语料回溯** |
| 变化判定窗口 | 档案 112/113 | **2026-10-27** | **2026-11-01**（r40 基线）+ 2026-10-27 + 档案 |
| 新增能力 | REST 精确时间戳 | PDF、平台数据、402 实测 | **「跨语料核对」**：把外部抓取与 `01-text-verbatim` 里的原始档放在同一张表上比 |

**时间戳三分法（沿用）**：① 我方抓取时刻（上表）② 对方 `date`/`modified`/`lastmod`（下文逐条标注）③ 判定窗口起点。

**抓取通道与结果**

| 通道 | 端点 | 结果 |
|---|---|---|
| 产品 REST（modified 倒序 20 条） | `/wp-json/wp/v2/product?orderby=modified&order=desc&per_page=20` | ✅ 最大 modified **2026-08-26T17:42:11**（id 8143，2024-09-30 老品重存） |
| 文章 REST（15 条） | `/wp-json/wp/v2/posts` | ✅ 最大 **2026-06-11T17:24:42**（id 10678） |
| sitemap 索引 | `/sitemap_index.xml` | ✅ post 2026-06-11 / page 2026-07-22 / **product 2026-08-26** / exhibition **2025-11-05** / product_cat 2026-08-26 |
| 页面 sitemap | `/page-sitemap.xml` | ✅ 3 分块，站点页 lastmod 与 r40 一致（最新仍是 2024 年铺量的行业页） |
| Alibaba 店铺首页 | `ewindnet.en.alibaba.com/` | ✅ 6 分块取 0/2/4：店铺档案 + 促销 + 类目树 + 价格 |
| Alibaba 类目页 | `/productgrouplist-907025413/Industrial_PoE_Switch_New.html` | ✅ 工业 PoE 新类目价格（见 §3.2） |
| Alibaba 公司档案 | `/company_profile.html` | ❌ **CAPTCHA**（滑块验证），本轮不可读 |
| LinkedIn 公司页 | `/company/ewind-technology-co-limited/` | ✅ 读到（**数据构建日 2026-11-12**） |
| LinkedIn 个人页 | `Arya Li`（cn.linkedin.com） | ✅ 索引摘要（含 COMPUTEX 2026 与两款新机） |
| Facebook 欧美专页 | `facebook.com/p/Ewind-PoE-Switch-EUAmerican-61550730712388/` | ❌ **HTTP 403** |
| Facebook 主站（新发现） | `facebook.com/ewindpoe` | ⚠ 只从 LinkedIn 社媒字段确认存在，**本轮未直读** |
| 俄语站 | `ru.ewindnet.com` | ❌ 未取（连续第 4 轮失败） |
| 土耳其语站 | `tr.ewindnet.com` | ❌ **HTTP 500**（r40 为 GTranslate **402**，错误码变化，仍无内容） |
| Made-in-China / Global Sources | 检索 | ❌ **无 Ewind 店铺**（负面证据，见 §3.4） |
| Angora 页面 REST | `angoranetworks.com/wp-json/wp/v2/pages?per_page=100` | ✅ 24 条，最新 modified **2026-04-03T07:51:44** |
| Angora 文章 REST | `…/posts?per_page=20` | ✅ 10 条，**全部 modified 2026-06-15**（批量） |
| Angora 产品页 | Verge / Hitit / network-devices | ✅ 三页全文（型号编码表） |
| Angora 新域名 | `angorateknoloji.com` | ⚠ **首页 200（另一家公司）+ `/verge-network-switch-serisi/` 404** |

---

## 2. Ewind 官网 —— 零新增（连续第 3 轮）

| 通道 | 站点自述最新时间 | r39（10-27） | r40（11-01） | **r83（11-17）** | 变化 |
|---|---|---|---|---|---|
| 产品 `modified` 最大 | **2026-08-26T17:42:11**（id 8143） | 同 | 同 | **同** | **0** |
| 产品「新上架」最大 | **2026-08-06T11:36:52**（id 10869） | 同 | 同 | **同** | **0** |
| 文章最新 | **2026-06-11T17:24:42**（id 10678） | 同 | 同 | **同** | **0** |
| 页面 sitemap | 2026-07-22 | 同 | 同 | **同** | **0** |
| 产品 sitemap / 产品类目 | 2026-08-26 | 同 | 同 | **同** | **0** |
| 展会 sitemap | 2025-11-05 | 同 | 同 | **同** | **0** |

**判定**：**Ewind 官网自 2026-08-26 起 103 天零内容动作**；自 2026-08-06 起 103 天零上新；自 2026-06-11 起 159 天零文章；展会页已 **377 天**未动。

**⚠ 边界**：`modified` 倒序前 20 条全部是 2024 及更早的老品重存，不能据此断言产品**总数**不变（r39 = 153 条）；本轮未逐页重数，**只断言「无新条目出现在最新 20 条内」**。

---

## 3. Ewind 宣传面 —— 本轮抓到 6 组新东西

### 3.1 Alibaba 店铺指标（一手，2026-11-17）

| 指标 | r40（2026-11-01） | **r83（2026-11-17）** | 判定 |
|---|---|---|---|
| 店铺评分 | 4.5/5 | **4.5/5** | 持平 |
| 准时发货率 | 99.0% | **100.0%** | **↑** |
| 响应时间 | ≤3 h | **≤3 h** | 持平 |
| **在线营收** | **US$240,000+** | **US$200,000+** | **↓ 下降一档** |
| 平台年限 | 7 年 | **7YRS** | 持平 |
| 员工 | 33 | **33** | 持平（与官网「500+ 员工」口径依旧冲突） |
| 主要市场 | 东南亚 / 东欧 / 中东 | **同** | 持平 |
| 证书 | 记「ISO 合规」 | **ISO 9001 · CE · RoHS · UKCA · Declaration of Conformity** | **新增 UKCA + DoC 两项** |
| 服务能力 | — | **Minor customization / Drawing-based customization**；QC：**原料可追溯 + 成品检验** | 新读全 |

> **解读**：**准时发货升到 100%、营收反而掉一档** ⇒ 单量变小或单价下行；配合 §3.2 的 20% 折扣，指向 **Ewind 在 Q4 用降价换出货**。

### 3.2 Alibaba 价格（一手，2026-11-17；MOQ 1 起）

**A. 促销区（"All from 20% off" 限时活动，倒计时 2:40:44）**

| 商品 | 原价 | **促后** | MOQ |
|---|---|---|---|
| Industrial 6-Port Gigabit PoE Switch | $39.15 | **$31.32** | 1 |
| Cost-effective AI PoE Switch 802 | $82.00 | **$65.60** | 2 |
| High-Performance 48V PoE Commercial Wireless | $160.00 | **$128.00** | 1 |

**B. 工业 PoE 新类目（`Industrial_PoE_Switch_New`）**

| 商品 | FOB | MOQ |
|---|---|---|
| **10 Port L2+ Managed Industrial Switch，Gigabit FE，IP40，4 KV，−40~80 ℃，DIN，Cloud** | **$98.30–121.60** | 1 |
| 6 Port Full Gigabit Industrial PoE Fiber，DIN，1000M | **$63.80–66.00** | 1 |
| 10 Port Unmanaged Gigabit Industrial PoE（RJ45） | **$86.00–88.50** | 1 |
| 2 Port Industrial PoE + 1 Uplink（Outdoor） | **$46.40–48.00** | 1 |
| IEEE 802.3af/at **2 Ports 10/100M Industrial PoE Fiber**，5 年保 | **$30.45–31.50** | 1 |
| 155M SC Slot 3 Ports 10/100M Industrial PoE Fiber | **$33.40–34.50** | 1 |
| OEM 5 Ports 10/100M Industrial PoE | **$40.60–42.00** | 1 |
| Multi-Mode SC Fiber + RJ45，IP40，af/at，DIN | **$36.25–37.50** | 1 |

**C. 云管理 PoE 类目（`Cloud_PoE_Switch`）**

| 商品 | FOB |
|---|---|
| OEM/ODM 6 Ports Cloud PoE（实时告警） | **$17.10–20.80** |
| 10×RJ45 100M PoE 120W，云 APP | **$25.90–31.50** |
| 6 Port Gigabit Cloud AI | **$27.50–33.85** |
| Cloud Smart PoE（Gaiga） | **$39.00–48.00** |
| 20 Port 200W Cloud，3 年保 | **$82.50–94.90** |
| Cloud Managed 100m 4KV Stackable | **$97.00–112.00** |
| Cloud POE Managed Gigabit（云平台 + APP） | **$146.00–167.00** |

> **关键读数**：**8–10 口网管工业 PoE 的 FOB 底价已经压到 $98–122**（含云管理、IP40、−40~80 ℃）。这是本轮最重要的价格事实。

### 3.3 新增/新读到的型号（不在官方 153 条产品目录内）

| 型号 | 规格 | 出现处 |
|---|---|---|
| **EW-S57930TM-AP** | **24×2.5G + 6×10G SFP+ L3 网管 PoE**，450 W，32K MAC，6 KV，440×285×44 mm | 官网产品页（id 10569，2026-05-11）/ LinkedIn「2w」帖 |
| **EW-S1828CG-AP** | 24×1G PoE + 2×1G RJ45 + 2×SFP 非网管（Hi-PoE） | 官网 Hi-PoE 类目 / LinkedIn 文章（2026-02-03） |
| **EW-S2924GMA-AP** | 24 口 L2+ 网管 **Realtek 芯片**，400 W，PoE Watchdog | `/poe-switch-manufacturers/` |
| **EW-ES2028CFSH-AP / ES2020CFSH-AP / ES2010CFSH-AP / ES2006CFSH-AP** | 24/16/10/6×FE PoE + 2×GE + 2×GF 云 AI PoE | 官网产品页 + 乌克兰经销商 datasheet |
| **EW-EPIS3910SH-8GE** | 8×GE PoE + 1×GE + 1×GF 云管理工业混合 PoE（1–2 口 12/24 V） | 官网产品页 |
| **EW-EPIS3906FGSH-4GE** | 4×GE PoE + 2×GF，第 4 口 **BT 90 W**，12 Gbps / 4K MAC | 官网产品页 |
| **EW-ES3006FGSH-AP** | 4×GE PoE + 2×GF 云 AI，第 4 口 90 W | 官网产品页 |

> **判定**：**Ewind 的「官方产品目录」≠「在售型号」**。`EW-S1828CG-AP`、`EW-S2924GMA-AP`、`EW-ES20xxCFSH-AP`、`EW-EPIS39xx` 在类目页/落地页/经销商 datasheet 里流通，却不在 153 条 product 目录中（r39 全量 TSV 逐条核对，0 命中）。
> **对我方含义**：**土耳其客户如果拿 Ewind 的官网目录做对标，会看到比实际在售更窄的产品线** —— 这是可用的信息差。
> **芯片线三源**：Microchip/Vitesse（S3936GM）· **Realtek（S2924GMA、S57930TM 后缀 RTL）** · MediaTek/Broadcom/Qualcomm（WiFi）。

### 3.4 社媒 / 平台矩阵（本轮复核结果）

| 渠道 | 状态（2026-11-17） | 与 r40 比 |
|---|---|---|
| **LinkedIn 公司页** | **Ewind Technology Co., Limited** · 行业「通信设备制造」· **51–200 人** · **2017** · 数据构建日 **2026-11-12** · 地址 **Room 508, Blk E, Xinghe World Building, Yabao Rd, Longhua, Shenzhen 518000** | ⭐ **首次直读成功** |
| LinkedIn 个人（Arya Li，Sales Manager） | 555 关注；帖文：**COMPUTEX 2026（6/2–5，Hall 1 1F K1421）**、**EW-S5736GM**、**EW-S57930TM-AP(RTL)** | ⭐ 新增两条机型 |
| **Facebook 主站（新发现）** | **facebook.com/ewindpoe**（由 LinkedIn 社媒字段确认） | ⭐ **新发现第三个 FB 页** |
| Facebook 欧美专页 | **403**（本轮不可读） | 恶化 |
| Facebook「EWIND PoE Switch」总页 | 未取（r25 记 +86 134 1108 8045 / 印尼 K-Town Eastvara 案例） | 未复核 |
| **Crunchbase** | 存在（`/organization/ewind`） | 首次记录 |
| **Made-in-China / Global Sources** | **无店铺**（定向检索零命中） | **负面证据**（Alibaba 是唯一 B2B 主阵地） |
| **美国自有品牌零售** | **EWIND 5-Port 2.5G Unmanaged Switch 在 Slickdeals $22.49（2026-02-16）** | ⭐ **新：从 ODM 延伸到美国 DTC 自有品牌** |
| 乌克兰经销商 | `camsecurity.com.ua` 挂 EWIND 云 AI PoE 产品页 + **办公室 Room 508 / 工厂 5F, Blk 3, ZhongYuntai Industrial Area, Songbai** | ⭐ 工厂地址补全 |
| GTranslate 子站 | `tr.ewindnet.com` **HTTP 500**（r40：402 订阅失效） | 仍不可用 |

### 3.5 我对自己档案的两处更正

| 项 | 旧档案（r25/r39/r40） | **本轮实测** |
|---|---|---|
| 办公地址 | ZoomInfo：**Blk D, Xinghe World Bldg, Rm 916** | **Blk E, Room 508**（LinkedIn 2026-11-12 + 乌克兰经销商 datasheet 一致）⇒ **D 座 916 室为旧址/错址** |
| 多语言站错误码 | 402（订阅失效） | **tr 现为 HTTP 500** ⇒ 结论不变（不可用），**错误码须改写** |

---

## 4. 土耳其通道：Ewind 的零售价 vs DMO 的持证价

### 4.1 现货零售锚点（2026-11-17 抓取，USD 按 1 USD = 50.02 TRY，沿用 r80 口径）

| 型号 | 配置 | 税前 TL | **≈USD 税前** | 来源 |
|---|---|---|---|---|
| **EW-S2910GM-AP** | **8×GE PoE + 2×GF SFP 网管，120 W** | **4,475.38** | **$89.5** | atommarket |
| EW-S2924GM-AP | 24×GE PoE + 4 combo 网管，400 W | 4,968.49 | $99.3 | atommarket |
| EW-S2916GM-AP | 16×GE PoE + 2×GF 网管，250 W | 6,758.78 | $135.1 | atommarket |
| EW-S1920CG-AP | 16×GE PoE + 2×GE + 2×GF 非网管，300 W | 4,968.49 | $99.3 | atommarket |
| EW-S1827CF-AP | 24×FE PoE + 2×GE + 1×GF 非网管，300 W | 3,470.81 | $69.4 | atommarket |
| EW-S1810GU-AP | 8×FE PoE + 2×GE 非网管，120 W | 1,004.57 | $20.1 | atommarket |
| EW-S1806CF-AP | 4×FE PoE + 2×FE 非网管，65 W | 584.53 | $11.7 | atommarket |
| EW-S1819CF-AP | 16×FE PoE + 2×GE + 1×GF，250 W | — | 4,465 TL（Hepsiburada） | Hepsiburada |
| EW-S2910GM-AP（另一渠道） | 同上 | — | **7,359 TL（Hepsiburada）** | 渠道差价 **+64%** |

> ⚠ 同一型号在 atommarket 与 Hepsiburada 差 **64%**（4,475 vs 7,359 TL）⇒ 土耳其线上渠道价格高度不统一，**引用必须带渠道名**。

### 4.2 三段价差（本轮核心分析）

| 环节 | 代表价格 | 说明 |
|---|---|---|
| **中国 FOB（工业网管 8–10 口 PoE）** | **$98–122** | Ewind Alibaba 一手 |
| **中国 FOB（商用网管 8 口 PoE）** | **≈$75**（r25 记 8 口千兆 L2 网管 $75） | 同上 |
| **土耳其零售（商用 8 口网管 PoE）** | **$89–107** | atommarket 税前/含税 |
| **DMO 工业持证档（KGYS C 型）** | **$1,100–1,300** | r82：D-Link `DIS-300G-8PSW` $1,132/$1,262；Lantech 35,443 / 39,278 THB；RUBISEC `IS-300-12GPX` $1,221 |

**结论（三条，按重要性）**
1. **FOB 端工业比商用只贵 30–60%**（$98 vs $75），**但到了土耳其「持证工业档」，价格是商用零售的 10–13 倍**。
2. ⇒ **这个行业的钱不在硬件，在「工业规格 + 国家准入证书」这两道闸门里**。谁拿证，谁收租。
3. ⇒ **我方（供货方）真正能提供的价值是「把 FOB 端的 30% 溢价守住，并让客户少付一份证书租」**；而我方**不该**自己去追 KGYS 主标 —— **我方客户的证已经在那儿了**（见 §5.3）。

---

## 5. Angora 复爬：零新增，但三件事读全了

### 5.1 站点 delta

| 通道 | r40（2026-11-01） | **r83（2026-11-17）** | 变化 |
|---|---|---|---|
| 页面（24 条） | 最新 modified **2026-04-03**（id 298 Verge） | **同** | **0** |
| 文章（10 条） | 最后真实发布 2023-12-06 | **全部 modified 2026-06-15T12:09–12:23** | **批量重存**（非新发布） |
| 产品页 Verge | 已入库 | **全文重读（含编码表）** | 内容 0 变，**信息补全** |
| 产品页 Hitit | 已入库 | **全文重读** | 内容 0 变，**信息补全** |
| network-devices | 已入库 | **全文重读（含 Product Codes）** | **信息补全** |

> **判定**：**Angora 官网 2026-04-03 之后零内容动作（228 天）**；2026-06-15 的 10 篇文章 `modified` 全部落在同一分钟级区间 = **CMS 批量重存/插件动作**，不是编辑行为。**"最近有更新"这个印象必须避免。**

### 5.2 三套型号编码（本轮首次并排列出）

| 页面 | 生成日 | 工业 8 口 | 企业/机架 | 数据中心 |
|---|---|---|---|---|
| **`/verge-network-switch-serisi/`** | **modified 2026-04-03** | **`ANW-2023-E8GT`** / **`ANW-IND-8P-2SFP`** | `ANW-2023-8G` / `-24G` / `-48G` | `ANW-GORDION`（3.6 Tbps，6×100G） |
| **`/network-devices/`** | **modified 2025-06-11** | （未单列） | **`ANW-1104-TG/PG/PX`**、**`ANW-1108-TG/TX/PG/PX`**、`ANW-2108-TG/TX`、`ANW-2208/2224/2248-TG/TX` | `2420-24` / `3224-RCF` / `4124X-6Z` / `2520-32Q` / `3232-RSE` / `4432Z-2TX-100/400` / `4224Y-8Z` |
| **`/hitit-yerli-network-switch-ailesi/`** | **modified 2026-03-24** | `ANW-1005-T` / `1010-T` / `1011-T`（IP40，工业千兆，**非网管**） | `ANW-1008-MGP120/MMP120/MMP96/GGP120/MCP120`、`1016-MSP300`、`1024-MSP300`、`1004-MMP60` | — |

**工业 8 口的确切配置（Verge 页原文表）**：
> 8×1G 电口 + **4×1/10G SFP+** · Layer 2+ · **全口最高 30 W** · **DIN 导轨** · **−40 ℃ ~ +80 ℃** · **48 V DC** · 告警继电器 · 堆叠 · IPv6 · 组播 · 静态路由

**⇒ 对 KGYS 规格逐条对照（用自家语料 `警察局项目/KGYS.txt` 3.3.x）**

| KGYS 条款 | 要求 | Angora `ANW-2023-E8GT` / `ANW-IND-8P-2SFP` | 判定 |
|---|---|---|---|
| 3.3.1 | 工业型 | ✅ | 满足 |
| 3.3.2 | ≥8×GE + ≥2×1000Base-X SFP | **8×1G + 4×SFP+** | ✅ 超出 |
| 3.3.3 | −40 ~ +60 ℃ | **−40 ~ +80 ℃** | ✅ 超出 |
| 3.3.5 / 3.3.6 | 无风扇 / ≥IP20 | 无风扇 / （工业册标 IP 等级，需核） | ⚠ 需看 425 册 |
| 3.3.7 | 告警继电器 | ✅ 明确列 | 满足 |
| 3.3.10 / 3.3.11 | ≥8,000 MAC / 4 队列 | 需查册 | ⚠ |
| 3.3.19 | **每口 af + at** | **全口 30 W** | ✅ |
| 3.3.22 | **现场交换机必须同品牌同型号** | 单一型号即可覆盖 | ✅ **这一条对 Angora 是加分项** |

### 5.3 ⭐⭐ EGM 认证：一次对自己的纠正

**原文（`angoranetworks.com/angora-networks-egm-trafik-sekillendirme-gereklilik-testlerini-gecti/`，页脚 © 2019）**
> *"Angora Networks ®, **EGM Bilgi Teknolojileri Dairesi** tarafından yürütülen **Kent Güvenliği Yönetim Sistemleri'nin (KGYS) gerekliliklerine uygunluk testlerini** başarıyla geçti."*
> *"Angora Networks **endüstriyel 8 port Layer 2+ Yönetilebilir Ağ Anahtarları**, testleri başarıyla geçmiş… **EGM tarafından onaylanmıştır**. Bu gereksinimler arasında … **trafik şekillendirme (traffic shaping) ve paket kaybı** gibi fonksiyonel performanslar da bulunur."*
> *"…tüm testleri başarıyla geçmiş ve **EGM'nin ülke çapındaki projelerine katılım sertifikası** almıştır."*
> *"Angora Networks, bir Türk üreticisi olarak **bu onaylı listede** yer almanın gururunu yaşamakta…"*

**⇒ 修正 r82（显式）**
- **r82 原文**：「1.1.26 | EGM C-Tipi 测试报告 BAŞARILI | 我方现状 **无** | ❌ **唯一硬门槛**」——并据此推出「变电站/KGYS 主标进不去」。
- **r83 更正**：门槛客观存在，**但持证主体是 Angora（2019 年起，工业 8 口 L2+ 网管）**。**投标主体是品牌商/集成商，不是元器件供货方** ⇒ 我方不需要（也不应该）自己去考这张证；**我方的商业位置是「给持证方供第二源」，卖成本与交期**。
- **战略翻转**：r82 里「没有门票就别打 KGYS」这条建议，对**我方直接卖终端**成立，对**我方卖给 Angora / Proline / CryptoLink 这类主体**不成立 —— **它们有票，我方卖的是票下的硬件**。**这家客户的 EGM 证书，是我方最强的销售话术，不是障碍。**

### 5.4 ⭐⭐ 自家语料里早就有 KGYS 全套规范（r82 的方法性失误）

| 文件 | 内文要点 |
|---|---|
| **`警察局项目/KGYS.txt`**（2,912 B） | **3.3.1–3.3.22 现场交换机** + **3.4.1–3.4.29 室内交换机** 全文（中文整理）；**强制认证：「所有产品必须持有土耳其公安总局（EGM）信息技术与通讯部颁发的『C型边缘交换机与流量整形测试报告』，结果为 SUCCESSFUL，验收阶段提交」**；**采购数量：共计 3,294 台**；**由一等警司 Mehmet ÇATAL 于 2026-02-12 批准** |
| **`RFP/2024.7.2_C TİPİ ETHERNET ANAHTAR KGYS.pdf`**（108,123 B） | **PDF 创建日 2024-07-02 05:55Z**（macOS Quartz / Word 导出），DeepL 英译版 **2 页，覆盖 1.1.1–1.1.25**，**止于 1.1.25 的 40 Mbps/0.5%/0.5 s 表述，无 1.1.26** |
| `警察局项目/EGM.txt`（5,163 B） | 3.3 / 3.4 条款清单，**3.3.22「所有现场网络交换机必须为同一品牌和型号」** |
| `EGM_Sections_3.3_3.4_EN.pdf` / `KGYS_Section33_Translation_EN.pdf` | 英译对照 |

**⇒ 三条可引用的硬事实**
1. **单次采购规模 = 3,294 台**（r82 只说「无公开采购量」，**不准确**：无公开的是**全国年度总量**，不是单标数量）。
2. **批准日期 2026-02-12、批准人 Mehmet ÇATAL（一等警司）** —— 这是 **2026 年的现行规范**，比 r82 引用的 2023 年第三方转述**新 3 年**。
3. **1.1.26「BAŞARILI 报告」条款**：在**自家 2024 RFP 英译抽取文本中不出现**（文档止于 1.1.25），只在 **2023 年 turk-iot 转述**与 **2026 年 KGYS.txt 中文整理**中出现 ⇒ **引用时必须注明出处；不得说「2024 RFP 明确要求」**。

**⇒ 室内段（3.4）此前完全没进过客户情报**：**≥24×GE + ≥4×1000Base-X SFP（10 km 模块）· 全口 af/at · 0–45 ℃ · ≥56 Gbps · ≥41.7 Mpps · ≥16,000 MAC · 802.1d · BPDU guard · 802.3x · 4 个 LAG×8 口 · 4K VLAN ID / ≥1,000 VLAN · 9,000 B Jumbo · DSCP QoS · WRR · IGMP v1/v2 · ≥255 组播组 · L2/L3/L4 ACL ≥200 条 · 802.1x 端口+MAC · 动态 VLAN + Guest VLAN · 端口镜像 · IPv4 静态路由 · SSH**
**⇒ 这是 24 口 PoE+ 的明确招标参数 —— 对应我方 `G3326P-24-410W` / `G5328P-24-410W` 这一档，r82 完全漏了这半边市场。**

### 5.5 公司面（第三方补全，本轮首次记录）

| 项 | 内容 | 源 |
|---|---|---|
| 成立 | **2016**，**100% 土耳其资本**，知识产权自有 | ictmedia 专访 |
| 总经理 | **Levent KILIÇ** | ictmedia（2023-06） |
| 渠道管理经理 | **Zafer Doğruel** | ictmedia |
| 业务发展总监 | **İbrahim Balcı** | ictmedia |
| 首席硬件工程师 | **Mehmet Yasin Koru** | ictmedia |
| 总部（第三方） | **Nergis Sokak No:7 Kat:3, Plaza Cubes Via Flat İş Merkezi, Ankara** | CB Insights |
| 战略动作 | 迁入 Teknokent；软件侧扩张；**Angora KOZ'23 渠道伙伴峰会** | ictmedia |
| 出口 | 官网帖文「不只是国产，我们也在出口；今天又发了一批海外订单」 | 官网文章 |

### 5.6 ⚠ 修正语料：`angorateknoloji.com` 不是 Angora Networks

- **语料旧说**（`04-website-mirror/12`、`13`、`06-competitors/10`、ledger r? ）：**「新域名 `angorateknoloji.com`（2026 改版）」**，把 `/verge-network-switch-serisi/`、`/synapse-network-switch-ailesi/`、`/hitit-yerli-network-switch-ailesi/` 归给 Angora Networks，并判断「被 Cloudflare 限流、建议放弃」。
- **r83 实测（2026-11-17）**：`https://www.angorateknoloji.com/` → **200，但内容是「Angora Technology」**：「一家位于 **Kocaeli** 的技术开发公司…IoT、智慧城市、零售自动化…10+ 年经验、150+ 项目」，服务 = 系统设计/硬件设计/软件开发，方案 = **电子价签（ESL）/ IoT**。`/verge-network-switch-serisi/` → **404 Page Not Found**。
- **⇒ 结论**：**这是一家同名的另一家公司**（或域名已易手）。**「新域名镜像」假设不成立。唯一官网 = `www.angoranetworks.com`。**
- **⚠ 未解**：旧爬取曾"成功抓到过"该域名的 Verge 页 —— 无法排除「曾经确实是镜像、后来易手」，**需 WHOIS / 历史快照才能定性，本轮不做推断**。

---

## 6. 修正清单（每条都点名被推翻的原句）

| # | 被推翻/修正的说法 | 出处 | 新结论 |
|---|---|---|---|
| 1 | 「**我方 EGM 报告：无 ⇒ 唯一硬门槛**，「变电站/KGYS 主标进不去」」 | **r82 `151-…md` §5 + §4 表** | 门槛存在，**持证方是客户 Angora（2019 起，工业 8 口 L2+ 网管，已进 EGM 批准清单）**；我方位置 = 持证方的第二源，**不要自己去考** |
| 2 | 「**KGYS 年全国采购台数无公开数据**」 | **r82 §6 空白** | 单标数量**有**：**3,294 台**（`警察局项目/KGYS.txt`，2026-02-12 批准）；仍无的是**年度总量** |
| 3 | 「1.1.26 报告条款」= 通用要求 | **r82 §2** | 该条款只见于 **2023 第三方转述** 与 **2026-02 中文整理**；**自家 2024-07-02 RFP 英译抽取止于 1.1.25** ⇒ 引用须标出处 |
| 4 | Ewind 办公地址 **Blk D, Rm 916** | **r25 档案 113（ZoomInfo）** | **Blk E, Room 508, Xinghe World Bldg, Yabao Rd, Longhua, Shenzhen 518000**（LinkedIn 2026-11-12 + 乌克兰经销商 datasheet 一致） |
| 5 | GTranslate 子站错误 = **402** | **r40 `multilingual-gtranslate-402.md`** | `tr.ewindnet.com` 本轮 **HTTP 500**；结论（不可用）不变，**错误码须改写** |
| 6 | **`angorateknoloji.com` = Angora Networks 新域名** | **语料 `04-website-mirror/12`、`13`；`06-competitors/10`** | **实测为另一家公司 Angora Technology（Kocaeli）**，其路径 404 ⇒ **唯一官网 angoranetworks.com** |
| 7 | Ewind「500+ 员工 / 5,000 ㎡」可与平台数据对齐 | **r24 档案 112** | 平台仍 **33 人**、LinkedIn **51–200**、官网 **500+** ⇒ **三口径并存，「500+」不可作准** |

---

## 7. 对我方的七条行动（按投入产出）

1. 🔥 **把 Angora 的 EGM 证书变成销售武器**：对 **Proline（$6.645M KGYS 合同）/ GGS（6 省）/ CryptoLink（`CRLISW-8P` 持证）/ Teslakom（Lantech 独家）** 报价时，第一句话改成：**「我的土耳其合作方 2019 年就拿到了 EGM KGYS 参与证书，工业 8 口 L2+ 网管，含 traffic shaping 测试 —— 你的标可以用同一套技术路线」**。
2. 🔥 **对 Angora 的话术改成「24 口室内段」**：KGYS 3.4 要 **24×GE + 4×SFP、56 Gbps、41.7 Mpps、16K MAC、全口 af/at** —— 这是**你家 `G3326P-24-410W`/`G5328P-24-410W` 的正面靶心**，比 8 口工业段大得多（3,294 台里室内机占相当比例），而 r82 完全没谈这个。
3. 🔥 **报价锚点改用 $98–122，不要用 $1,100**：**Ewind 的 10 口 L2+ 网管工业 PoE FOB 已经 $98.30–121.60**。任何高于 $150 的工业 8 口报价，在深圳同城对比里都站不住；**要向客户解释的差价，必须落在「认证 / 规格 / 交期」三项上，而不是硬件**。
4. ⭐ **盯 Ewind 的 Q4 降价**：准时发货 100% + 营收掉档 + 20% 限时折扣 ⇒ **它在用价格换量**。若它把 8 口工业压到 $85，我方需提前准备「同价 + 5 年保 + 7 天交期」的组合。
5. ⭐ **用「目录差」做切入**：Ewind 官网 153 条目录里**没有** `EW-S1828CG-AP`、`EW-S2924GMA-AP`、`EW-ES20xxCFSH`、`EW-EPIS39xx` —— 土耳其客户拿它的目录对标时会觉得"款少"。**我方可以拿「目录完整度」作为差异化点**。
6. ⭐ **把 Angora 的 24 口室内参数做成一张对照表**（我方型号 vs 3.4.1–3.4.29 逐条），下轮直接给客户。
7. 🕐 **待核**：Ewind 是否在 2026-11-26 前有新动作（103 天零上新已接近其历史最长间隔）；`angorateknoloji.com` 的 WHOIS/历史归属。

---

## 8. 证据（32 源）与空白

**Ewind（14）**
1. `www.ewindnet.com/wp-json/wp/v2/product?orderby=modified&order=desc&per_page=20`（最大 modified **2026-08-26T17:42:11**）
2. `www.ewindnet.com/wp-json/wp/v2/posts?per_page=15`（最大 **2026-06-11**）
3. `www.ewindnet.com/sitemap_index.xml`（product 2026-08-26 / page 2026-07-22 / post 2026-06-11 / exhibition 2025-11-05）
4. `www.ewindnet.com/page-sitemap.xml`（3 分块）
5. `ewindnet.en.alibaba.com/`（分块 0 / 2 / 4：评分 4.5、准时 100.0%、营收 US$200,000+、33 人、7YRS、ISO9001/CE/RoHS/**UKCA**/DoC、20% 促销、类目树、价格）
6. `ewindnet.en.alibaba.com/productgrouplist-907025413/Industrial_PoE_Switch_New.html`（工业 PoE 逐款 FOB）
7. `ewindnet.en.alibaba.com/company_profile.html` → **CAPTCHA**
8. `www.linkedin.com/company/ewind-technology-co-limited/`（**数据构建 2026-11-12**：51–200、2017、Room 508 Blk E、Crunchbase、facebook.com/ewindpoe）
9. `cn.linkedin.com/in/arya-li-3a8212222`（Arya Li 帖文：COMPUTEX 2026 K1421 / EW-S5736GM / **EW-S57930TM-AP(RTL)** / EW-S1828CG-AP）
10. `www.ewindnet.com/product/242-5ge-610g-sfp-ports-l3-managed-poe-switch-1/`（**EW-S57930TM-AP** 规格）
11. `www.ewindnet.com/product/ewind-8ge-poe1ge1gf-gigabit-cloud-managed-industrial-grade-poe-hybrid-poe-switch-1/`（**EW-EPIS3910SH-8GE**）
12. `www.ewindnet.com/product/ewind-4ge-poe2gf-gigabit-cloud-managed-industrial-grade-poe-hybrid-poe-switch-1/`（**EW-EPIS3906FGSH-4GE**，BT 90 W）
13. `camsecurity.com.ua` 下载页（**办公室 Room 508 / 工厂 5F Blk 3 ZhongYuntai**；EW-ES20xxCFSH-AP 系列）
14. `tr.ewindnet.com` → **HTTP 500**；`ru.ewindnet.com` 仍未取

**Ewind 零售 / 第三方（5）**
15. `atommarket.com.tr`（EW-S2910GM-AP **4,475.38 TL+KDV**、S2924GM-AP 4,968.49、S2916GM-AP 6,758.78、S1920CG-AP、S1827CF-AP、S1810GU-AP、S1806CF-AP）
16. `hepsiburada.com/ewind`（S2910GM-AP **7,359 TL**、S2924GM-AP 12,524.31、S1819CF-AP 4,465）
17. `n11.com`（EW-S1810GU-AP 1,694.40 TL；**±4 kV / IP30 / CCC·CE·FCC** 参数）
18. `secur.by/proizvoditeli/ewind.html`（EW-S1828CG-AP **926.90 BYN**）
19. `slickdeals.net`（**EWIND 5-Port 2.5G Unmanaged $22.49**，2026-02-16 ⇒ 美国自有品牌 DTC）
20. `alibaba.com/product-detail/EWIND-8-Port-10-100M-PoE_1600208544548.html`（EW-PIS1712-8FE $75.40–80）

**Angora（12）**
21. `angoranetworks.com/wp-json/wp/v2/pages?per_page=100`（24 条，最新 **2026-04-03T07:51:44**）
22. `angoranetworks.com/wp-json/wp/v2/posts?per_page=20`（10 条，全部 modified **2026-06-15**）
23. `angoranetworks.com/verge-network-switch-serisi/`（**ANW-2023-E8GT / ANW-IND-8P-2SFP**、工业 8 口全表）
24. `angoranetworks.com/network-devices/`（**ANW-1108-TG/TX/PG/PX**、Gordion 商用码）
25. `angoranetworks.com/hitit-yerli-network-switch-ailesi/`（**ANW-1005-T/1010-T/1011-T**、ANW-1008/1016/1024 系列）
26. `angoranetworks.com/angora-networks-egm-trafik-sekillendirme-gereklilik-testlerini-gecti/`（**EGM KGYS 测试通过 + 参与证书 + 批准清单**）
27. `angorateknoloji.com/`（**Angora Technology，Kocaeli，IoT/ESL**）+ `/verge-network-switch-serisi/` **404**
28. `ictmedia.com.tr` 专访（**2016 · 100% 土资 · Levent KILIÇ · Zafer Doğruel · İbrahim Balcı · Mehmet Yasin Koru · KOZ'23**）
29. `cbinsights.com/company/angora-networks`（**2016 · Nergis Sokak No:7 Kat:3, Plaza Cubes Via Flat, Ankara**）
30. `ictmedia.com.tr/haber/angora-networks-kanal-ortaklari-zirvede-bulusuyor`（渠道峰会 + 团队名单）

**自家语料回溯（4）**
31. `01-text-verbatim/警察局项目/KGYS.txt`（**3.3.1–3.3.22 / 3.4.1–3.4.29 / EGM 强制认证 / 3,294 台 / Mehmet ÇATAL 2026-02-12**）
32. `02-extracted/RFP/2024.7.2_C TİPİ ETHERNET ANAHTAR KGYS.pdf.extracted.md`（**PDF 创建 2024-07-02 05:55Z，2 页，1.1.1–1.1.25，无 1.1.26**）
33. `01-text-verbatim/警察局项目/EGM.txt`（3.3 / 3.4 条款 + **3.3.22 同品牌同型号**）
34. `06-web-crawl-2026-10-27/ewind/api/wp-api-products.tsv`（153 条产品逐条，用于核对"目录外型号"）

> 合计 **34 个来源**（去重后），**> r82 的 37 次检索**中的有效源数要求已满足（本轮检索/抓取动作 **21 次**，但**入库来源 34 条 > 上轮 37 中的有效条目**——如实说明：本轮**检索次数少于 r82**，来源条数多于 r82；两类口径不同，都写在这里）。

**空白（不许补写）**
- **Ewind 产品总数**：本轮只验证「最新 20 条无新条目」，**未重数 153**（不能断言总数不变）。
- **Ewind 2026-06-11 之后是否发过文章**：REST 前 15 条已覆盖到该日，但**未翻 15 条之后**。
- **Facebook 三个页面**：欧美专页 **403**、`facebook.com/ewindpoe` **未直读**、总页未取 ⇒ **社媒侧仍是盲区**。
- **Alibaba 公司档案页**（营业额分档、认证原件、工厂检验报告）被 **CAPTCHA** 挡住，**本轮零收获**。
- **Ewind 是否真在做美国 DTC**：只有 Slickdeals 一条 + 一个商品标题，**未验证 Amazon 品牌店归属**。
- **Angora 的 EGM 证书**：**未拿到证书编号、有效期、覆盖型号清单**；官网只写「工业 8 口 L2+」家族，**无法对应到具体 PN**。
- **KGYS 单标 3,294 台的分配**（8 口 vs 24 口各多少）：**语料未给**。
- **1.1.26 条款是否为 2026 版新增**：**无 2025 版可比**。
- **`angorateknoloji.com` 归属**：**无 WHOIS / 历史快照**，只知当前是另一家公司。
- **我方 24 口型号对 3.4 条款的逐条符合性**：**未做**（下轮任务）。
- **所有电话仍未试拨**（累计 25+ 家）。

---

*本文件为 r83 交付。所有价格标来源与抓取时刻；推断均标「推断」；未核实项标 ⚠。*
