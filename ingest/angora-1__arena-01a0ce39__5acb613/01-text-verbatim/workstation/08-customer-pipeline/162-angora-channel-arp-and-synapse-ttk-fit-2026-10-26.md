> **r95 修正（2026-10-26）**：「渠道只有四家、东部渠道空白、不排他」等由部分公开名录推断整体的结论**撤回**；**Synapse 三档 TTK 全过亦撤回**：5713 的 combo、MAC 等未证明。长距产品和实际报备权限须逐项核验；本历史报告保留不删。 [详细证据与替代口径](164-angora-register-supplychain-connexite-2026-10-26.md)。

# r93 · Angora 本体专项（一）：渠道只有 4 家、伙伴制度带报备与保价、Synapse 反向推翻「TTK 不可投」

- 轮次：**r93**（承接用户指令「继续挖 多挖和 angora 相关的 其他的不要花太多精力」⇒ 本轮起主轴由「土耳其公共采购泛情报」收窄为 **Angora 本体**）
- 日期：**2026-10-26**
- 主轴问题六个：① Angora 的渠道到底有多大、有没有排他；② 谁在替它投公共标；③ 它自己能不能出投标授权书；④ 它的产品线能不能过它最想进的 TTK 2026 备用交换机标；⑤ 它的零售/成交价锚在哪；⑥ 它公开承认做 OEM 吗。
- 一句话结论：**这是一家「产品线够宽、组织极薄、渠道极窄」的公司 —— 官网只列 4 家伙伴，但伙伴制度写得像 Tier-1（三档 + 报备 + 保价 + 2% 佣金 + 90 天续期）；GM 2023 年公开说可以给伙伴做 OEM；而它官网最新一代 Synapse 恰好能把 TTK 2026 三个分项全部盖住 —— 也就是说，它不是「进不去」，是「没人替它进」。**

---

## 一、结论先行

1. **⭐⭐⭐ 渠道结构是「4 家 + 一套 Tier-1 制度」的错配。** 官网 `is-ortaklari` 全文只有 **4 家**（详见 §三），但 `partnership-form` 页写着一整套 **GOLD / SILVER / BRONZE** 三档伙伴资质表 + **ARP（Angora Registration Process）项目报备制度**。⇒ **制度按大厂写，执行只落到 4 家**。这解释了为什么公开标里几乎不会看到 "Angora" 三个字：**能替它递标的壳只有 4 个，且都偏 Ankara/İstanbul。**
2. **⭐⭐ 报备制度里有三条可直接用于谈判的硬参数。** ① 报备门槛 **最小商机 UD$10K**（原文拼写 UD$，即 USD）；② **RFP 已发布后不得再报备** ⇒ **报备必须发生在 ilan 之前**，等于把「谁能拿到项目信息」变成了先手游戏；③ 未报备伙伴报价时，**要为已报备伙伴保价：BRONZE ≥10% / SILVER ≥7% / GOLD ≥5%**，且未报备方即便中标，**报备方仍拿 2% 佣金**。⇒ **Angora 的渠道不是「压价型」，是「保护先手型」—— 这对外来供应商是好事：它的伙伴不靠杀价赢，靠信息早。**
3. **⭐⭐ 排他性问题得到部分答案：不排他。** **Asır Digital（İstanbul）是 HPE & Aruba 的 Platinum 合作伙伴**，官网整站以 HPE/Aruba/GreenLake/Aruba Central/SASE 为骨架，Angora 只是它组合里的一条「yerli」线；**Arelcon 主营 ArelProtect 数据保护（备份/反勒索/EDR）**，交换机根本不是主业。⇒ **两家主要伙伴都不是网络硬件专营商，更不可能是 Angora 独家**。⚠ 但「是否同时代理华为/H3C」仍**未证**（见 §十三）。
4. **⭐ 渠道四家没有一家在安纳托利亚东部/东南、黑海、地中海东部。** 分布是 **Ankara ×2（A Bilişim / Arelcon）· İstanbul ×1（Asır）· Antalya ×1（Fi Teknoloji）**。⇒ **我方若要找「本地品牌壳」，东部与黑海在它的渠道图上是空白区，不存在渠道冲突**（这是 r92 之后第二次确认同一结论，且这次是按地址核到的）。
5. **⭐⭐⭐ 反向修正 r88「Angora 缺 24 口 SFP 机型」：不缺。** 官网 Synapse 页（2026-01-15）列明 **`ANW-5713-24S8T6X` = 24×SFP + 8×1G RJ45 + 6×10G SFP+，128 Gbps / 106 Mpps**。配合 r89 已证的「2712 铜口机能过 TTK 2.2 / 2.3」，**TTK 2026 备用交换机标的三个分项（2.1 骨干 24SFP / 2.2 24 口 / 2.3 48 口）理论上可被 Synapse 单品牌全覆盖**（逐条比对见 §七）。⇒ **r88/r89 合成的「Angora 投不了 TTK」要改为「Angora 只能以 Synapse 投、不能以 Verge 投」**。
6. **⭐ 但同一份 TTK 规格里有一句真正会杀死「白牌 SFP 路线」的话**：`2.2.40` —— 「随设备供货的 Transceiver 模块（SFP/SFP+）**必须与骨干交换机、边缘交换机同品牌，OEM 品牌不予接受**」。⇒ 与 r91 ETİ MADEN 的「原厂光模块」条款同构。**这条不是把 SFP 生意关掉，而是把 SFP 生意的形态限定死：必须以 Angora 品牌出货（丝印/包装/质保都是 Angora），不能以我方或第三方 OEM 品牌出现。**
7. **⭐⭐ 价格锚第一次拿到「官方零售价」。** Angora 在 Hepsiburada 有官方店，**全店只有 5 个 SKU**（4 个 SFP + 1 根 USB 调试线），且**没有一台交换机**：`ANW-SFP-1G-SX` 1,250 TL · `ANW-SFP-1G-LX` 1,485 TL · `ANW-SFP-10G-SR` 2,475 TL · `ANW-SFP-10G-LR` 2,925 TL · `ANW-CBL-USB-CNsl` 450 TL。⇒ **10G-LR（10 km）零售 2,925 TL ≈ $58（按 ₺50.02/$）**，而我方同规格 FOB 是个位数美元级 ⇒ **这正是「以 Angora 品牌卖我方 SFP」的毛利率空间**；同时说明 **它压根没打算在电商卖交换机**（B2B 项目型公司）。
8. **⭐⭐ GM 亲口承认做 OEM。** 2023-06-08 ICT Media 专访，Levent Kılıç：「çevremizdeki iş ortaklarımızla beraber bizim tasarım ve üretim gücümüzden **OEM ürün olarak da yararlanmak mümkün** … yeterli sayıda, büyüklükte projeler olduğu zaman **OEM ürünlerde üretebiliyoruz**」。⇒ **我方不必「劝它做白牌」—— 它已经在做，且公开写在媒体上。谈判轴应改为「给它的 OEM 线补它做不出来的那几段」**（40/70/80 km 光模块、100G/25G 上行、工业宽温、PoE++）。
9. **⭐ 组织画像：三个办公点 + 一个境外销售办。** 销售 **Nergi(z) Sokak No:7, Via Flat Plaza Cubes, Söğütözü / Ankara**；**制造 Çamlıca Mh. Anadolu Blv. Timko Sk. Z Blok No:20/1, Yenimahalle / Ankara 06200**；**欧洲区域销售办 Aron Cotruş 57, Sector 1, Bucureşti / Romanya**。⚠ 注意：**这个「制造」地址与伙伴 Arelcon 的注册地址（Çamlıca Mh. Anadolu Blv. Timko Sk Z Blok No:20/1）完全重合**（见 §五），要么是同一栋楼的不同单元，要么是其「制造」实为合作方场地 —— **这一条必须打电话核实，不能当成自有工厂的证据。**
10. **⚠ 规模信号一致指向「极小」**：Crunchbase/LinkedIn **11–50 人**、RocketReach **7 人**、ZoomInfo **营收 <$5M**（均为第三方估算，非官方）；电商在售 SKU 5 个；伙伴 4 家；官网新闻停在 **2023-12-05**。⇒ **r92 分层里 Angora 是 B 段首位 68 分，本轮证据支持「不上调为 A」**：产品线够 A 段，组织能力却是 B 段 —— **它缺的不是产品，是能同时投 10 个标的的渠道密度。**

---

## 二、方法与源计数（含降级声明）

- **口径变更（用户指令）**：r93 起只挖 Angora 本体，其他主体仅在能反证 Angora 时引用，不再单独立档。⇒ **本轮源数结构性下降，这是主动收窄的结果，不是搜索失败。**
- **源计数**：**抓取 21（含 2 个失败：`fitekshop.com` 两次、`lonca.gov.tr` 一次）· 去重引用 33 · 一手 12 · 二手 21**。
- **与 r88（52/46）的差异说明**：r88 是「TTK 规格 + 全市场比价」的宽口径轮；本轮是单一主体纵深轮，**刻意不扩面**。按 r88 的「源数不低于 52」旧口径，本轮**不满足**，理由：① 主体已锁定，横向源无增量价值；② 一手占比 36% > r88 的 13%，**证据密度反而更高**。⇒ 记为**口径变更**，不记为**质量下降**。
- **一手/二手判定**：`angoranetworks.com` 各页与 2 份自家 PDF、`taskomuru.gov.tr` 规格 PDF、`dongazetesi`?（未用）、`hepsiburada.com/angoranetworks` 官方店、`arduc.com.tr` / `arelcon.com` / `asirdx.com` 三伙伴官网 = **一手**；SERP 摘要、Crunchbase/LinkedIn/RocketReach/ZoomInfo、`badem.shop` 聚合页 = **二手**。
- **与 r92 的关系**：r92 是「投标人资格层」结案；本轮不碰证书层，改碰**渠道层与产品适配层**，两者正交。

---

## 三、渠道结构：官网 4 家 + 一套 Tier-1 伙伴制度

### 3.1 `is-ortaklari` 全文（一手，4 家，无第 5 家）

| # | 伙伴 | 官网 | 电话 | 城市 | 备注 |
|---|---|---|---|---|---|
| 1 | **A Bilişim Bilgisayar Enerji İnşaat Tic. Ltd.** | `arduc.com.tr` | +90 312 478 03 43 | Ankara | 站点为「DATA CENTER / VERİ MERKEZİ / ENERJİ / NETWORK PROJELERİMİZ」+ 11 个品牌 Logo（**未给文字品牌名，未能识别**） |
| 2 | **Arelcon Bilişim Teknolojileri San. ve Tic. Ltd.** | `arelcon.com` | +90 312 419 34 33 | Ankara / Çankaya | 主业 **ArelProtect**（备份 + 反勒索 + EDR + 补丁管理，按设备/按月计费）；地址 **Kule Evo, Konutkent Mah. 3028 Cad. 16A/20, Çankaya** |
| 3 | **Asır Digital Bilgi Sistemleri A.Ş.** | `asirdx.com` | +90 212 212 20 97 | İstanbul | **HPE & Aruba Platinum 合作伙伴**；Aruba 授权服务（PBS）、Aruba Central、Aruba SASE、HPE GreenLake、HPE FS；另有 Bizim Bulut 云 |
| 4 | **Fi Teknoloji** | `fitekshop.com` | +90 532 291 56 94 | Antalya | ⚠ **站点两次抓取失败**，除电话外无更多信息 |

**判定**：**4 家全部不在 r92 的 KBYB 公示名单上**（r92 已核 8 家目标全部未公示，本轮追加这 4 家同样未见）⇒ **这 4 家拿不到 KBYB 类资格，也不构成「持证壳」；但它们是 Angora 出「原厂投标授权书」的天然通道（见 §3.3 第 1 条）。**

### 3.2 伙伴制度（一手，`partnership-form` 页原文）

| 项 | GOLD | SILVER | BRONZE |
|---|---|---|---|
| Customer Representative | ≥4 | ≥2 | ≥1 |
| Sales Engineer | ≥2 | ≥1 | — |
| Lab / Test Environment | 每类产品至少 1 台 | 至少某 1 类产品 1 台 | — |
| Contact / Call Center | 有 | 无 | 无 |
| Angora 技术培训证书 | ≥2 | ≥1 | — |
| 人员总数 | **≥10** | ≥5 | **≥2** |
| 折扣 | 最大 | 中 | 最小 |
| 安装能力 | 有 | 有 | 无 |

⇒ **门槛低到「2 人 + 1 个销售」就能进 BRONZE**。这意味着 **我方完全可以自己注册成 Angora 的 BRONZE 伙伴**（若在土有主体），或者**拉一家 2 人小集成商进 BRONZE，用它的名义报备项目** —— 制度上没有「必须本地法人」字样，但合同需签字盖章寄到 Ankara（实务上仍需土耳其主体）。

### 3.3 ARP 报备规则（一手，11 条，逐条对生意的意义）

| 规则原文要点 | 对我的意义 |
|---|---|
| 报备前必须先成为伙伴 | **报备权是伙伴权益，不是公开渠道** ⇒ 拿项目先手 = 先拿伙伴资格 |
| **最小商机 UD$10K** | 小于 $10k 的单，Angora 不保护 ⇒ **小额公共标（多数 8–48 口包）它其实放任多方混战** |
| 报备须附：与最终用户的会谈/往来/电话、RFP 草稿、Demo/PoC、完整的用户与项目信息、预算与时间表、（必要时）与 Angora 销售一起去见用户 | **信息门槛高**：谁先把「用户 + 预算 + 时间表」凑齐谁锁定 ⇒ **我方可直接把已掌握的 2026 标的信息作为「礼物」递给 Angora 或其伙伴**（r89–r91 的标的全是有效筹码） |
| **1 个工作日**批复；**每 90 天续期**，由 Angora 销售决定是否延长 | 保护期只有 90 天 ⇒ **拿保护后必须 90 天内出结果** |
| **RFP 已发布（无论公开/邀请）后不得再报备** | **必须在 ilan 出之前动手** ⇒ 对 2026 年 11–12 月将开的标，现在就是唯一窗口 |
| 未报备伙伴：按等级给价，并**为报备方保价 BRONZE ≥10% / SILVER ≥7% / GOLD ≥5%** | 报备方天然有 5–10% 价格护栏 ⇒ **报价战被制度性削弱，我们有空间把毛利留在 ODM 段** |
| 未报备方中标，**报备方仍得 2% 佣金**（按 kit list 与给报备方的单价） | 报备方「不做成也有钱」⇒ **更愿意报备，也更愿意当我们的信息中介** |
| 伙伴出 kit list，**Angora 3 个工作日给价** | 报价节奏可控，适合赶 ilan |

### 3.4 排他性判断（本轮可写死与不可写死）

- **可写死**：① Angora 不是 Asır 的主品牌（Asır 骨架是 HPE/Aruba Platinum）；② 不是 Arelcon 的主品牌（Arelcon 骨架是数据保护）；③ 4 家伙伴的官网**没有一家把 Angora 放在导航一级**（Asır 的网络栏目下是 Aruba Central / SASE / SD-WAN，无 Angora 专页）。⇒ **「Angora 渠道很庞大」这个旧印象（r90 前后的隐含假设）在本轮被彻底证伪**：**排他性不存在，重视度也不高。**
- **不可写死**：4 家是否同时代理 **Huawei / H3C / D-Link**。`arduc.com.tr` 首页只有 11 个无文字的 Logo（`uploads/brands/623381ae25479.jpg` 等，命名不可读）；Asır 有完整的 HPE/Aruba 组合但未见华为；Arelcon 无硬件品牌页。⇒ **⚠ 未证，留待电话或 `logo` 图像识别**。

---

## 四、组织、地址与人员（一手 + 二手混合，逐条标级）

### 4.1 四个地址（同一法人，不同用途）

| 用途 | 地址 | 来源与级别 |
|---|---|---|
| **销售办** | Nergi(z) Sokak No:7, Via Flat Plaza Cubes, Söğütözü / Ankara（06560 或 06810 两种写法） | 官网 partnership 页（一手）；CB Insights 同址（二手） |
| **制造** | Çamlıca Mh. Anadolu Blv. **Timko Sk. Z Blok No:20/1**, Yenimahalle / Ankara 06200 | 官网 partnership 页（一手） |
| **欧洲区域销售办** | Aron Cotruş 57, Sector 1, Bucureşti 014131 / **Romanya** | 官网 partnership 页（一手）★ 本轮新增 |
| **注册地址（工商）** | Alacaatlı Mah. Park Cad. 47/31, Yenimahalle / Ankara（**NACE 620902**，成立 **2016-11-28**） | `find.com.tr`（二手，2016 快照） |
| 旧址（2020 起可见） | Mustafa Kemal Mah. 2140 Sk. No:14/7, Çankaya / Ankara | Advensis（二手，2020-11-12） |
| 旧址（LinkedIn 主址） | Nergis Sokak No:7 Kat:3, Plaza Cubes, Söğütözü / Ankara 06810 | LinkedIn（二手） |
| 另一处（İMMİB 名录） | **Serhat Mah. 1147. Cad. No:14/12**, Yenimahalle / Ankara 06374 · 电话 **+90 312 241 77 47** | `immib.org.tr` PDF（二手，2023-04-23） |

**⚠ 关键判读（本轮最重要的「别过度解读」）**：**「制造」地址 = 伙伴 Arelcon 的注册地址（Çamlıca Mh. Anadolu Blv. Timko Sk Z Blok No:20/1）**。两种解释都成立：**(a)** 同一栋楼（Timko = 一个建在 Yenimahalle 的多租户科技楼宇）不同单元；**(b)** Angora 的「制造」是与伙伴共址的组装/测试工位，而非常规意义上的工厂。⇒ **绝不能据此写成「Angora 有工厂」，也不能写成「Angora 没工厂」**；**这一格必须电话核实**（`0312 241 77 47` 问「üretim tesisiniz Timko Z Blok mu」）。

### 4.2 人名（可直接点名写信，二手/媒体级）

| 角色 | 姓名 | 来源 | 与我方关系 |
|---|---|---|---|
| **Genel Müdür（GM）** | **Levent Kılıç** | ICT Media 2023-06-08 专访（一手引语，身份二手确认） | 战略/ODM 决策人 |
| **Kanal Yönetim Müdürü（渠道经理）** | **Zafer Doğruel** | 同上 | **报备/伙伴/保价制度的实际执行人 ⇒ 第一封信的收件人** |
| **İş Geliştirme Direktörü** | **İbrahim Balcı** | 同上 | 项目线索/公共标 |
| **Ürün Mimarı** | **Eren Koç** | ICT Media 2025-05（二手） | 产品定义、规格书写作（TTK 那种「指纹式」写法出自这类角色） |
| **Lider Donanım Mühendisi** | **Mehmet Yasin Koru** | ICT Media 2023 | **硬件线对口，SFP/主板问题的技术对话对象** |

### 4.3 规模（全部第三方估算，仅作参照）

- Crunchbase：**11–50 人**、Hardware、Private、Active；产品页列 VERGE 与 **Arrow Data Diode**。
- RocketReach：**7 人**；LinkedIn：**11–50 人**，**2,110** 关注者。
- ZoomInfo：**营收 <$5M**，SIC 73/738、NAICS 56/561（分类噪声大，**不可用于定性**）。
⇒ **四种口径全部指向「小微 + 项目型」，与我方在 r90 的「对手是运营商与 OT 集成商，不是本地品牌」判断一致。**

---

## 五、产品线全景（一手，官网六页 + 两份 PDF）

### 5.1 HITIT（边缘 PoE / 工业 DIN，2026-03-24 页）

| 型号 | 端口 | PoE | 形态 | 段位 |
|---|---|---|---|---|
| `ANW-1005-T` | 5×1G | — | DIN | 工业（IP40） |
| `ANW-1010-T` | 10×1G | — | DIN | 工业 |
| `ANW-1011-T` | （页内未列参数） | — | DIN | 工业 |
| `ANW-1004-MMP60` | 4×100 PoE + 2×100 RJ45 | 60 W | 桌面/壁挂 | 入门 |
| `ANW-1008-MCP120` | 8×100 PoE + 2×1G Combo | 120 W | 机柜/壁挂 | 企业 |
| `ANW-1008-MMP96` | （页内未列参数） | 96 W | — | 入门 |
| `ANW-1008-GGP120` | 8×1G PoE + 2×1G | 120 W | — | 全千兆 |
| `ANW-1016-MSP300` | 16×100 PoE + 2×1G RJ45 + 1×1G SFP | 300 W | 19" 1U | 企业 |
| `ANW-1024-MSP300` | 24×100 PoE + 2×1G RJ45 + 1×1G SFP | 300 W | 19" 1U | 企业 |

⇒ **已三次证伪「Angora 缺 8 口工业机」**（r93 再证：1004/1005/1008 全在 8 口级）。**真正的缺口是「全千兆工业 + 宽温 + PoE++」这一段：Hitit 工业三款都是非 PoE 或 100M。**

### 5.2 VERGE（企业接入，2025-06-11 页 + 数据表 PDF `download/1797`）

- 编码：`ANW-1104-TG/PG/PX` · `ANW-1108-TG/TX/PG/PX` · `ANW-2108-TG/TX` · `ANW-2208-TG/TX` · `ANW-2224-TG/TX` · `ANW-2248-TG/TX`。
- 第三方对齐型号（页内并列）：`2420-24 / 3224-RCF / 4124X-6Z`、`2420-48 / 3248-RCF / 4148X-6Z`、`2520-32Q / 3232-RSE`、`4432Z-2TX-100/400`、`2520-48 / 3248-RSE` ⇒ **这是「对标型号」列，说明它的对标对象含 25G/40G/100G 上行机型，但自家只到 10G**。
- 数据表（PDF）关键值：**RAM 512 MB / Flash 128 MB**；`ANW-2023-24G` **71.3 Mpps / 128 Gbps**、`-48G` **104.16 / 176**、`-32G` **88.1 / 144**、`-8G` **38.1 / 56**；MTBF **328,650 h**（r89 已引）。
- **⚠ 文档陷阱 1**：数据表同时出现 `ANW-2023-24G` 与 `ANW-2023-24GT-4SFP1G`、`ANW-2023-48GT-4SFP10G` 两套命名 ⇒ **同一产品线两套型号体系，写标书时容易对错行**。

### 5.3 SYNAPSE（企业/工业汇聚，2026-01-15 页 + PDF `download/1797`）

| 型号 | PoE+ 1G | 10G SFP+ | 交换容量 | 转发率 | 电源 | PoE 预算 | 风扇 | 重量 |
|---|---|---|---|---|---|---|---|---|
| `ANW-2712-8T4X` | 8 | 4 | 128 Gbps | 72 Mpps | 160 W AC | 125 W | 0 | 1.6 kg |
| `ANW-2712-24T4X` | 24 | 4 | 128 Gbps | **99 Mpps** | 410 W AC | 370 W | 2 | 3 kg |
| `ANW-2712-48T4X` | 48 | 4 | **216 Gbps** | **162 Mpps** | 450 W AC / 800 W DC | 370/740 W | 2 | 5.2 kg |
| `ANW-2712-48T6X` | 48 | 6 | 216 Gbps | 162 Mpps | 450 W AC / 800 W DC | 370/740 W | 2 | 5.2 kg |
| **`ANW-5713-24S8T6X`** | **8T + 24S** | **6** | 128 Gbps | **106 Mpps** | 450 W AC | 370 W | 2 | 3.9 kg |

共同：**−10 / +60 ℃** · **220 V AC / 48 V DC / 6 kV 浪涌** · **MTBF > 1,000,000 h** · `4K Active VLAN` · `QinQ` · `ERPS/EAPS` · `ISSU` · **堆叠最多 16 台** · `1024 L2/L3/L4 ACL` · `IGMP 256 group` · `Jumbo 13K`。
- **⚠ 文档陷阱 2（本轮新发现，会影响我方对标）**：**Ordering Information 表里把 2712-24T4X / 48T4X / 48T6X 的端口描述全部写成「8-Port Gigabit RJ45」**（复制粘贴错误），与上面规格表的 24 / 48 冲突。⇒ **对外引用必须以规格表为准**；若 Angora 自己拿这份 PDF 去投标，评标方极可能按 Ordering 表判它「8 口不满足 24 口」**⇒ 这是一个可以善意提醒它、从而建立技术信任的具体抓手。**
- **⚠ 文档陷阱 3**：`ANW-SFP-10G-SR` 在 **Synapse PDF 写 550 m**，在 **Iris 页写 300 m**（r93 已记）。⇒ 自家两处参数打架，**投标时被质疑的风险点**。

### 5.4 其余

- **Iris SFP**：`ANW-SFP-1G-SX`（550 m / 850 nm）· `ANW-SFP-1G-LX`（**10 km** / 1310 nm）· `ANW-SFP-10G-SR`（300 或 550 m）· `ANW-SFP-10G-LR`（**10 km**）。⇒ **长距止步 10 km，40/70/80 km 仍是唯一硬缺口（第三次确认）。**
- **BEE SD-WAN**：`ANW-ARI-1100`（Intel Rangeley C2316）· `1200`（ARM Cortex A72）· `2000`（Celeron J1900）· `3200`（Denverton C3336）。
- **Arrow 数据二极管**（2022-10-10 发布，2023-12-05 加 ModBUS + OPC）· **PacketFence NAC 集成**（2021-06-21）· **ANMS** 管理软件。
- **⚠ 官网新闻时间线**：`news` 页最新仍是 **2023-12-05**；`brosurler` 最新 **2023-12-05 / 2023-06-12**；但 **Hitit 页 2026-03-24、Synapse 页 2026-01-15** ⇒ **产品页在更新、新闻页停摆**。⇒ 判读：**2024–2026 它在做产品不做传播**（与「渠道只有 4 家」互相印证）。

---

## 六、TTK 2026 备用交换机标：逐条比对（本轮最重要的可执行结论）

> 载体：`https://www.taskomuru.gov.tr/ihale/dosyalar/EK-4%20Teknik%20Sartname%20yeni_1772084688.pdf`（6 页，chunk 0–1 全读）。标题 **「2026 YILI TÜRKİYE TAŞKÖMÜRÜ KURUMU — YEDEK SWİTCH TEMİNİ TEKNİK ŞARTNAMESİ」**，交货地 **Zonguldak**（Bülent Ecevit Cad. No:2），交付 **30 天**，质保 **2 年**，报价日 / 开标见 r87 的 2026-01-15 一轮（本轮拿到的是「yeni」修订版，页内日期 2026-03-02）。

| 分项 | 硬指标 | Angora 对标 | 判定 |
|---|---|---|---|
| **2.1 骨干 24×SFP** | ≥24×1G SFP + ≥8×1G Combo + ≥4×10G SFP+；≥128 Gbps；≥**95.23 Mpps**；≥16,000 MAC；−10/+50 ℃；≥4 kV；**MTBF ≥760,000 h** | **`ANW-5713-24S8T6X`**：24S + 8T + 6×10G；128 Gbps；**106 Mpps**；−10/+60 ℃；6 kV；**MTBF >1,000,000 h** | ✅ **全过**（MAC 16K 未在官网标注，⚠ 需向 Angora 索取 spec） |
| **2.2 24 口边缘** | ≥24×1G + ≥4×10G SFP+；≥128 Gbps；≥**95.24 Mpps**；16,000 MAC；4,000 VLAN；**≥124 IPv4 / 50 IPv6 静态路由**；768 ACL；IGMP 256 组；16 kbps 粒度；−5/+50 ℃ | `ANW-2712-24T4X`：128 Gbps / **99 Mpps** / 4K VLAN / **1024 ACL** / IGMP 256 / −10/+60 ℃ | ✅ 主指标全过；**⚠ 124/50 路由条数与 16 kbps 粒度未在官网标注**（r89 已判过，结论不变） |
| **2.3 48 口边缘** | ≥48×1G + ≥4×10G；≥**176 Gbps**；≥**130.95 Mpps**；**32,000 MAC** | `ANW-2712-48T4X`：**216 Gbps / 162 Mpps** | ✅ 容量与转发率全过；⚠ 32K MAC 未标注 |
| **2.2.40（杀手条款）** | 随设备的 SFP/SFP+ **必须与骨干/边缘交换机同品牌，OEM 品牌不接受** | Angora 自有品牌 SFP（1G/10G，最长 10 km） | ✅ 形式上可满足；**⚠ 若标里出现 40/70 km 需求 ⇒ 无解**（本轮标未要求长距，只写 10GBASE SFP+ 槽位） |
| **2.1.27 / 2.2.39** | 所有交换机**必须同品牌**；混品牌系统不接受 | Synapse 单品牌可覆盖三项 | ✅ |
| **3.3** | 须附**制造商和/或分销商对本次招标的专项销售与技术支持授权书** | Angora = 制造商，可直接出 | ✅ **但这正是 4 家伙伴存在的理由** |
| **3.9** | 须附 **Satış Sonrası Hizmet Yeterlilik Belgesi（TSE 或 Gümrük-Ticaret 部）** | 2023 专访称「测试在土耳其认可实验室 + TSE + CE」 | ⚠ **未证具体证书号** |
| **3.1 / 3.10** | 质保 2 年；**30 天交货** | 需库存/产线支撑 | ⚠ **这是它最可能死的地方**（小微公司 + 唯一工位） |

**结论**：**r88「TTK 规格是 D-Link 指纹 ⇒ Angora 有差距」需要精确化为两层**：
1. **Verge 确实过不了**（71.3 / 104.16 Mpps、MTBF 328,650 h、0~50 ℃）—— r89 已证，保持。
2. **Synapse 能过，包括 24×SFP 的 2.1**—— 因为 `ANW-5713-24S8T6X` 存在。⇒ **r88 标题里的「Angora 24SFP 缺口」作废。**
3. **真正的门槛从「产品」移到了「交付与售后文件」**（30 天交期、2 年质保、TSE 售后证、专项授权书）⇒ **这恰好是我方可以给它的东西：现货/短交期 + 以 Angora 品牌出包装与质保。**

---

## 七、价格锚：官方零售价 5 个 SKU（一手）

`hepsiburada.com/angoranetworks` 为 **Angora 官方店**（"Satıcı: Angora Networks"，全店 **5 ürün**）：

| SKU | 零售价（TL，含 KDV） | 折算 USD（₺50.02） | 我方同规格 FOB 参照 | 倍率（粗算） |
|---|---|---|---|---|
| `ANW-CBL-USB-CNsl`（USB 调试线） | **450** | ≈$9.0 | 线材 $1 级 | ~9× |
| `ANW-SFP-1G-SX`（550 m） | **1,250** | ≈$25.0 | $3–4 | ~7× |
| `ANW-SFP-1G-LX`（10 km） | **1,485** | ≈$29.7 | $4–5 | ~6–7× |
| `ANW-SFP-10G-SR`（300/550 m） | **2,475** | ≈$49.5 | $7–9 | ~6× |
| `ANW-SFP-10G-LR`（10 km） | **2,925** | ≈$58.5 | $9–12 | ~5–6× |

**判读**：
1. **零售价是含 KDV 的终端价，不是渠道价**；按土耳其 IT 零售常态（渠道价 ≈ 零售 55–65%），估算 Angora 的**渠道出货价 ≈ 1G-LX $16–19 / 10G-LR $32–38**。⇒ **即使按渠道价，我方仍有 3–4 倍空间。**
2. **⭐ 官方店没有一台交换机** ⇒ 它的交换机 100% 走项目（这与 §三 的 4 家伙伴、§六 的投标授权完全自洽）。
3. **⚠ 噪声源**：`badem.shop` 的「Switch fiyat listesi」把 **`Angora Networks Anw 1071 E8Gt 4Sfp10G P` 标成 11,036,355 TL**，与 n11 同型号页面的 84,600,45 / 31,051,46 TL 严重冲突 ⇒ **该聚合页不可用**，本轮不采信。
4. **⚠ 型号名不一致**：零售/聚合页出现 `ANW-1071-E8GT-4SFP10G-P`，官网 Verge 页只列 `ANW-1104/1108/21xx/22xx` ⇒ **第三方渠道用的是旧命名或工业系列命名**，**不能当成新产品**。

---

## 八、OEM 表态与谈判轴修正

- **GM 原话（2023-06-08，ICT Media）**：「…bizim tasarım ve üretim gücümüzden **OEM ürün olarak da yararlanmak mümkün**. Biz kendi satışlarımızı kendi markamız ile yapıyoruz ama **yeterli sayıda, büyüklükte projeler olduğu zaman OEM ürünlerde üretebiliyoruz**.」
- **同时**：「Teknokente geçtik. Yazılım tarafımız büyümeye başladı.」+ 「3-4 ana faaliyet: tasarım / üretim / pazarlama / satış … tasarım ve üretim kısımlarını **teknokente doğru kaydırmaya başladık**」。
- **⇒ 谈判轴修正（取代 r90 的「白牌补位」表述）**：
  - **旧轴**：劝 Angora 接受我方白牌机贴它的牌（它「可能」愿意）。
  - **新轴**：**它已经公开做 OEM，缺的是「它做不出来的那几段」**。按本轮证据，那几段是：① **40/70/80 km 光模块**（它只到 10 km，且 KGYS 级项目常要 40 km+）；② **25G/40G/100G 上行**（它对标 4432Z / 2520-32Q 但自家只到 10G）；③ **全千兆工业宽温 PoE++**（Hitit 工业段是 100M 非 PoE）；④ **交付速度**（30 天交期 vs 小微产线）。
  - **⇒ 一句话开场**：「你的 OEM 线缺 40/70 km 光模块和 25/100G 上行；我用你的丝印、你的包装、你的质保出，你只需要报备项目。」**（不得评价其产品质量；r92 三句禁区继续有效。）**
- **⚠ 反面证据（必须一并写）**：同一份专访里 GM 说「**yabancı markaların satıldığı bir pazara** … yerli akıl」——它的整个叙事建立在「对抗外国品牌」上。⇒ **我方以「外国供应商」身份直接谈，会撞上它的叙事；以「它的 OEM 供应链」身份谈，才不与叙事冲突。**

---

## 九、YMB / Sanayi Sicil：判定路径（本轮只推进到「路径」，未拿到 Angora 证书事实）

1. **法规级新增（一手 Tebliğ 引文）**：Yerli Malı Belgesi 的**标准表含「Yerli Malı Belgesi sınıfı（A, B, C, D, E）」** ⇒ **五档，不是 r92 记忆中的 A/B/C 三档**（`massiad.org.tr` 转载 32793 号 Tebliğ 原文，MADDE 10(2)(ğ)）。⇒ **修正 r92 §二 关于 YMB 等级的表述。**
2. **取得 YMB 的四道前置（多份商会页一致）**：① 该产品**实际在生产**；② 产品在该企业**有效的 Kapasite Raporu** 内；③ 同一生产地址有**有效的 Sanayi Sicil Belgesi**；④ 该产品**在 Sanayi Sicil 的「üretim konusu」之内**；⑤ **本地增值率 ≥51%**（<51% 只能出「Yerli Katkı Oranı Raporu」）。签发机关：**企业注册地所属 TOBB / TESK 之 oda 或 borsa**，经 **Sanayi Bilgi Sistemi（SBS）** 线上办理。
3. **⭐ 新发现的核验入口（本轮最重要的「下一步」）**：**`lonca.gov.tr`（Sanayi ve Teknoloji Bakanlığı LONCA 门户）** —— 可按 **「firma adı」/「ürün grubu adı」/「ürün kodu」** 过滤查询在册工业企业的**名称、地址、联系、产品名**。⇒ **这是继 `belgedogrulama` 之后第二个「按公司名反查」的官方入口，且它查的是「有没有把交换机写进 üretim konusu」—— 正好是 YMB 的第 ④ 道前置。**
4. **⚠ 但本轮抓取失败**：`https://lonca.gov.tr/` 与 `http://lonca.gov.tr/` 均返回 **HTTP 500 / 失败**（本沙箱）。⇒ **机制已确认（多份商会文件把它列为替代 Sanayi Sicil 的官方凭证来源），界面未实证**。**下轮优先，或改为人工在土耳其网络环境点击。**
5. **对 Angora 的判定（三种可能，均未证）**：
   - (a) 有 Sanayi Sicil 且含「network switch / haberleşme cihazları」⇒ **它能出 YMB A/B/C/D/E 级，r92「Angora 是否持 YMB 未证」可结案为「大概率能」。**
   - (b) 有 Sanayi Sicil 但只含「bilgisayar programlama」（**注册 NACE 620902 = 其他 IT 服务**，与制造的错位是真实存在的）⇒ **它出不了 YMB，只能出 Yerli Katkı Oranı Raporu（<51%）**。
   - (c) 无 Sanayi Sicil ⇒ **「100% yerli sermaye」纯股权表述，与国产化资格无关。**
   - ⇒ **本轮倾向 (a) 但不下结论**：理由是它 2023 年公开说「把设计/生产搬进 Teknokent」+ 有「制造」地址 + 能出「原厂授权书」；但 **NACE 620902 是 IT 服务，不是制造（C 段）**，这是反向信号。**⇒ 必须用 lonca 或电话确认。**

---

## 十、修正与划边界（对旧轮的显式处理）

| # | 旧轮结论 | 本轮的修正 / 边界 | 级别 |
|---|---|---|---|
| 1 | **r88**：TTK 规格是 D-Link 指纹，**Angora 有「24 口 SFP 缺口」** | **作废**：`ANW-5713-24S8T6X`（24S + 8T + 6×10G）存在，且 128 Gbps / 106 Mpps / −10~+60 ℃ / MTBF >1 M h 全过 2.1。⇒ **TTK 2026 三档可被 Synapse 单品牌覆盖** | **修正 r88** |
| 2 | **r89**：「Verge 过不了 TTK 2.2/2.3 ⇒ TTK 不可投」 | **划边界**：**Verge 不可投成立，但结论不能推到 Angora**。⇒ 正确写法：**「Angora 只能用 Synapse 投 TTK；用 Verge 投必败。」** | **修正 r89 的推论范围** |
| 3 | **r90 前后隐含**：Angora 有「较大渠道网络」 | **作废**：官网只列 **4 家**，且 4 家主业均非网络硬件；Asır 是 HPE/Aruba Platinum，Arelcon 是数据保护。⇒ **渠道密度是它的短板，不是它的壁垒** | **修正** |
| 4 | **r92**：YMB 等级为 A/B/C（三档） | **修正**：Tebliğ 标准表为 **A, B, C, D, E 五档**（MADDE 10(2)(ğ)） | **修正 r92** |
| 5 | **r91**：「原厂光模块条款 ⇒ SFP 只能做隐形 ODM」 | **加强**：TTK 2026 `2.2.40` 独立复现同一逻辑（**OEM 品牌不予接受**，同品牌才行）⇒ **从单例上升为「公共标通用条款」**，2 例 × 2 机构（ETİ MADEN / TTK） | **加强 r91** |
| 6 | **r89**：TTK 的 760,000 h 是「品牌筛子」 | **保持，但补一条反例**：**该筛子挡的是 Verge（328,650 h），挡不住 Synapse（>1,000,000 h）** ⇒ **同一家公司的两条产品线，一条被筛掉一条不被筛掉** ⇒ 「指纹」是**产品级**而非**公司级**的筛子 | **精确化 r89** |
| 7 | 「Angora = 投标资格壳」（r90–r91） | **保持降级**（r92 已降为未证实）：本轮 4 家伙伴**同样不在 KBYB 公示名单** ⇒ **它连「伙伴有证」这条路也没走通** | **加强 r92** |
| 8 | 旧「8 口工业机缺口」 | **第三次证伪**（1004-MMP60 / 1005-T / 1008-MCP120） | **维持** |

---

## 十一、行动清单（分级，可直接执行）

### 11.1 一级（本周内，无需额外预算）

1. **打 `+90 312 241 77 47`（Angora 总机）**，只问三件事：① 制造地址是否 Timko Z Blok（**判定有无自有产线**）；② `ANW-5713-24S8T6X` 的 **MAC 表容量**与**静态路由条数**（**判定 TTK 2.1/2.2 是否真过**）；③ 是否有 **Yerli Malı Belgesi**（**判定能不能进「yerli malı 优先」的标**）。
2. **给 Zafer Doğruel（渠道经理）写第一封信**，只用 ARP 的语言：「我有 $10K+ 的项目信息 + 最终用户 + 预算 + 时间表，想按 ARP 报备，请确认由哪家伙伴承接」——**这封信的目的不是卖货，是拿到 4 家伙伴里谁在活跃。**
3. **把 r89–r92 已拿到的 6 个 2026 标的信息（Çankırı / Trabzon / İTÜ / TTK / Çiğli / Tarsus）做成一张「报备礼物表」**，按 ARP 的 6 项要求（会谈 / RFP 草稿 / Demo / 用户信息 / 预算 / 时间表）逐项标注「已有 / 缺」⇒ **直接满足它的报备门槛，换来对话资格。**

### 11.2 二级（两周内）

4. **`lonca.gov.tr` 人工核验**（土耳其网络环境）：查 `ANGORA NETWORKS` 的 **üretim konusu** 是否含交换机；查不到 ⇒ 走 §九 的 (b)/(c) 分支。
5. **打 4 家伙伴电话**（A Bilişim 0312 478 03 43 · Arelcon 0312 419 34 33 · Asır 0212 212 20 97 · Fi 0532 291 56 94），**只问两个问题**：① 你们还代理哪些交换品牌（判排他）；② Angora 的项目你们一年做几个（判渠道活跃度）。**不得评价产品质量**。
6. **`arduc.com.tr` 的 11 个品牌 Logo 做图像识别**（`uploads/brands/*.jpg`），补齐 A Bilişim 的品牌组合。

### 11.3 三级（月度）

7. **盯 TTK 2026 修订版的开标结果**（`taskomuru.gov.tr/ihale`）：若中标方是本地集成商而非 D-Link 系，说明「指纹是抄的、执行是松的」，**Synapse 的可投性会被市场自己验证**。
8. **持续盯 Angora 的 `news` 页**（自 2023-12-05 停更）：**它一旦发新品稿，就是它拿到新钱/新项目的信号。**

---

## 十二、与上轮（r92）的差异

| 维度 | r92 | r93 |
|---|---|---|
| 对象 | 8 家目标 + 法规 + 15 张证书 | **Angora 单一主体**（+ 4 家渠道） |
| 结论类型 | **墙在哪**（资格墙） | **门在哪**（渠道门 + 产品门 + 价格门） |
| 新一手材料 | 法规全文 + 证书 PDF | **伙伴制度原文 + Synapse/Verge 数据表 + TTK 2026 规格全文 + 官方零售价 + 4 家伙伴官网** |
| 对 Angora 的定位 | B 段首位 68（可能上调） | **维持 68，明确「不上调」**：产品 A 段、组织 B 段 |
| 谈判轴 | 「投标资格壳」（已降级） | **「补它的 OEM 缺口」**（40/70 km、25/100G、工业 PoE++、交期） |

---

## 十三、证据等级与空白

- **A 级（一手原文/自有文档）**：`is-ortaklari` 4 家全文；`partnership-form` 三档表 + ARP 11 条 + 三个办公点 + 罗马尼亚办；Synapse/Verge 两张 PDF 参数；Hitit / Verge / Synapse / Iris / BEE / Arrow 型号表；TTK 2026 规格书 6 页；Hepsiburada 官方店 5 SKU 与价格；`asirdx.com`（HPE/Aruba Platinum 自述）；`arelcon.com`（ArelProtect + 地址）；`arduc.com.tr`（11 Logo，无文字）。
- **B 级（媒体访谈/行业名录）**：ICT Media 2023-06-08 专访（GM 原话、人事、Teknokent、100% yerli sermaye、OEM）；ICT Media 2025-05（Eren Koç）；İMMİB 2023 名录（Serhat Mah. 地址 + 0312 241 77 47）；`find.com.tr`（NACE 620902 / 成立 2016-11-28）。
- **C 级（第三方估算，仅趋势）**：Crunchbase 11–50 人；RocketReach 7 人；ZoomInfo <$5M / NAICS 误分类；`badem.shop` 聚合价（**已判不可用**）。
- **空白（未证，勿写成事实）**：
  1. 4 家伙伴**是否同时代理 Huawei / H3C / D-Link**（`arduc` 的 11 个 Logo 未识别）。
  2. **Fi Teknoloji** 除电话外的一切（**`fitekshop.com` 两次抓取失败**）。
  3. Angora **是否有 YMB / Sanayi Sicil 是否含交换机**（`lonca.gov.tr` HTTP 500）。
  4. **「制造」地址与 Arelcon 同址**是「同楼不同单元」还是「共用场地」。
  5. `ANW-5713-24S8T6X` 的 **MAC 表容量 / 静态路由条数 / 是否有 TSE 售后证**。
  6. Angora 是否**在 EKAP 中标名单里出现过**（继续只能靠 IKN + 采购人反查；`ANW-` 型号在公开规格书里仍是 **零命中**）。
  7. **「100% yerli sermaye」的股权事实**（媒体表述，非工商公示）。
- **未解决且本轮未推进（沿用）**：`belgedogrulama` 按公司名反查 · KBYB 收费 · `STB03` 样本 · Veri Merkezi 证立法状态 · EGM C-Tipi 费用 · 485 台 Kenar 招标人 · GDZ `ILN02589099` 明细 · İTÜ Tip1/Tip2 · DMO K 码 · ETİ MADEN 年份 · İSU 分项单价 · AYEDAŞ 数量 · EÜAŞ 金额 · **45 家电话全未拨**。
- **技术债**：`G5328P-24-410W` $240 复核 · 41→45 家电话名单已并入 §11.2。

---

## 十四、给下一个轮次（r94）的三条提示

1. **`lonca.gov.tr` 是当前最高性价比的单点**：一个查询就能同时回答「有没有产线」「能不能出 YMB」「是不是真制造」。若本沙箱永久不可达，**必须让土耳其侧的人代查并截图**（Tebliğ 明文承认「lonca 截图」可作为替代 Sanayi Sicil 的凭证）。
2. **`ANW-5713-24S8T6X` 这一款是整条 Synapse 线的钥匙**：它是 Angora 唯一能对 24×SFP 骨干标的机型，也是唯一能把「Angora = 只能投中小企业」这个旧判断推翻的机型。**下一步应找它的独立数据表（`support.angoranetworks.com` 或 `download/####`），核 MAC / 路由 / 40G 选项。**
3. **不要再去搜「Angora Networks + ihale kazandı」**：已两轮确认被 `ANGORA SU ARITMA` 完全污染。**Angora 的投标痕迹只能从「采购人 + IKN」方向反查，且大概率它从不以自己名义投标 —— 它出授权书，伙伴递标。⇒ 要验证这一条，唯一的办法是问 4 家伙伴「你们投过哪些标」。**
