# 🎥 Angora 自有 YouTube 频道 & KOZ'23 峰会 · 深度情报

> **采集日期：2026-09-27**（第 9 轮深挖）
> **重大突破**：此前判定「YouTube 字幕全被 bot 墙挡死」是**错误的**。
> 换用 `fetch_page` 直接抓视频页，**Angora 自有频道的字幕全部可读**。
> 仅 ICTMEDIATV 那条 40:43 长访谈（`z0loF632E2s`）因页面被 JS 撑成 171 分块而未能取出，
> 但 2020 年那条 4:30 短访谈（`yveHNxOXD3g`）**字幕完整到手**。

---

## 一、⭐ 官方社媒矩阵（官网 JSON-LD `sameAs` 权威字段）

从 `angoranetworks.com/?lang=en` 页面源码的结构化数据中直接读出，这是**最权威**的账号清单：

| 平台 | 地址 | 状态 |
|---|---|---|
| X / Twitter | https://twitter.com/angoranetworks | ✅ 24 关注者，60 帖，2016-12 注册，最后发帖 2025-10-28 |
| **Instagram** | **https://www.instagram.com/angora_networks/** | 🆕 **此前未知**；直接抓取 403（需登录） |
| LinkedIn | https://www.linkedin.com/company/angora-networks/ | ✅ 2,110 关注者，11–50 人；员工列表页仍 403 |
| **YouTube** | **https://www.youtube.com/channel/UCCAG46dVy-wxXtO-_b7fTPA** | 🆕 **此前未知**；见下 |

> 📌 新增两个此前完全没查到的官方账号：**Instagram** 与**自家 YouTube 频道**。

---

## 二、⭐⭐ Angora 自有 YouTube 频道 · 全部 6 个视频

频道：`UCCAG46dVy-wxXtO-_b7fTPA`（@angoranetworks）

| # | 视频 ID | 标题 | 时长 | 上传 | 观看 | 主讲 |
|---|---|---|---|---|---|---|
| 1 | `mPVd05zz4VM` | Angora ThinC İnce İstemci Eğitimi Temmuz 2023 | 1:35:56 | 2023-07 | 573 | （薄客户端培训） |
| 2 | `Sh-uqJsl0JE` | **Arrow Data Diode** | 8:55 | 2023-06-05 | **323** | 英文解说 |
| 3 | `I5kDVMWC79I` | **KOZ'23 · Angora Networks Ürün Portföyü** | 17:52 | 2022-12-06 | 31 | **Can Hayat** |
| 4 | `C43VQBJtdrk` | **KOZ'23 · Angora Ürün Portföyü** | 25:09 | 2022-12-06 | 20 | **Taylan Esen** |
| 5 | `32J3cYQXCyM` | **KOZ'23 · Angora Networks Pazar Analizi** | 19:15 | 2022-12-06 | 16 | **İbrahim Balcı** |
| 6 | `jrdoTa5owZk` | **KOZ'23 · Angora Kanal Ortaklığı Programı** | 29:01 | 2022-12-03 | 32 | **Zafer Doğruel** |

> 💡 **观看量极低**（16–323），说明这些是**面向渠道伙伴的内部资料**，几乎无人研究。情报价值极高。

---

## 三、⭐⭐⭐ KOZ'23 峰会 · 完整组织架构

**KOZ'23**（Angora Kanal Ortakları Zirvesi，渠道伙伴峰会）2022-10-19 安卡拉，口号
**"Birlikte Üretelim, Birlikte Büyüyelim"（一起生产，一起成长）**。
来源：ictmedia 报道 + 官网 `/angora-kozz23/`（该页现为 **404**，已被删除 → Wayback 目标）+ 4 个 KOZ'23 视频。

### 3.1 Angora 内部人员（含新增）

| 姓名 | 职务（土耳其文） | 中文 | 峰会讲题 | 备注 |
|---|---|---|---|---|
| **Levent KILIÇ** | Yönetici Ortak | 管理合伙人 | *Angora Networks Vizyonu*（愿景） | ⭐ 创始人之一 |
| **Mehmet Taylan ESEN** | Yönetici Ortak / süreçlerden sorumlu direktör | 管理合伙人／流程总监 | *Angora Üretim Süreci*（生产流程） | ⭐ 创始人之一 |
| **Mehmet Yasin KORU** | Lider Donanım Mühendisi | 首席硬件工程师 | *Angora Ürün Geliştirme Süreci* | 硬件设计负责人 |
| **Zafer DOĞRUEL** | Kanal Yönetim Müdürü | 渠道管理经理 | *Angora Kanal Ortağı Programı* | 🆕 新增 |
| **İbrahim BALCI** | İş Geliştirme Direktörü | 业务拓展总监 | *Pazar Analizi - Yerli Network Ürünleri* | 🆕 新增 |
| **Can HAYAT** | Sistem Mühendisi | 系统工程师 | *Angora Ürün Portföyü*（产品组合） | 🆕 新增 |

### 3.2 外部关联方

| 姓名 | 单位 | 角色 |
|---|---|---|
| **Aykut DALYAN** | **ELCORE** Ülke Müdürü | ⭐ **ELCORE 是 Angora 的分销商**（新发现） |
| **Selenay ŞENOL** | ICT MEDIA Dergisi | 主持人 |
| **Kenan Nurhan ALTINSAAT** | TBD（**Türkiye Bilişim Derneği** = 土耳其信息技术协会）安卡拉分会董事会主席；**2025-04-19 当选 TBD 全国主席**（第 35 届大会；已核实：tbd.org.tr。前宪兵军官，1961 生于 Samsun/Bafra） | 网络安全圆桌嘉宾 |
| **Gökhan Osman ŞENŞÜKÜR** | **SIBEREUM** 创始合伙人 | 网络安全圆桌嘉宾；Club Angora 背书人 |
| **Prof. Dr. Levent ERASLAN** | SODİMER 主席 | 主题演讲 *Dijital Devrim; Metaverse* |
| **Murat PEHLİVAN** | ICTMEDIA | 电视访谈主持人 |

> 🆕 **新发现分销商：ELCORE**（此前仅知 Advensis）。
> 🆕 **新发现关联公司：SIBEREUM**（Gökhan Şenşükür，Managing Partner）。

---

## 四、⭐⭐⭐ 关键经营数据（Zafer Doğruel 渠道演讲原文）

> 以下均为 **2022 年 10 月** Angora 自述口径。

| 指标 | 数值 | 原文依据 |
|---|---|---|
| **交换机国产化率（2022）** | **68%** | *"switchlerimizde %68"* |
| **薄客户端国产化率（2022）** | **76%** | *"thinklightlarımızda da %76"* |
| **2023 目标国产化率** | **拉到 80%** | *"Bu rakamları %80 seviyesinde çekmek 2023 yılı içerisindeki hedeflerimiz"* |
| **在网设备数** | **2,000 台以上** | *"sahada artık 2000'in üzerinde Cihazımız var"* |
| **库存 SKU** | **100 种以上** | *"stoğumuzda 100'den fazla ürün var"* |
| **最长供货周期** | **不超过 10 周** | *"tedarik sürelerimizi de 10 haftanın üzerine çıkartmadık"* |
| **同行供货周期** | 竞品报 **450–500 天** | *"450 günlerin… 500 Günü tedarik sürelerinin verildiği"* |
| **招聘方式** | **仅靠内部推荐 + 实习生** | *"Biz personel alımlarımızı sadece referansla gerçekleştiriyoruz ve stajyer istihdamıyla…"* |
| **Intel 授权** | ⭐ 持有 **Intel developer license**（土耳其极少数） | *"bir İntel'in developer sonunda çok az sayıda firmanın sahip olduğu bir yetkinliğe sahibiz bir lisansa sahibiz"* |

> ⚠️ **战略含义**：Angora 的护城河叙事 = **国产化率 + 供货速度 + Intel 授权**。
> 我方（Simon / SmartByte）在**国产化率**上天然无法竞争（这是土耳其政府项目的准入条件），
> 但在**供货周期**上——我方 10 周 vs 竞品 450–500 天——**Angora 已把"快"当作核心卖点**，
> 这意味着我方若交期慢于 10 周将直接失分。

### 4.1 创始叙事（Zafer 原话）
> *"2016 yılında **iki sektör emekçisi mühendis** tarafından… bir hayalin…"*
> *"**Levent Kılıç ve Taylan Esen**… o yıllar sektörün 20 yıllık deneyimini…*
> *'neden onların yaptıklarını Biz yapamıyoruz' sorgulaması ile İşe başladılar…*
> *birazcık **yel değirmenlerine karşı** mücadele ettiler."*

→ **两人创办，各带 20 年行业经验**；自比"与风车作战"（堂吉诃德）。

---

## 五、⭐⭐⭐ 市场分析（İbrahim Balcı · 与马尔马拉大学联合研究）

> 2020 年做的研究，KOZ'23 上首次公开。这是 Angora **自己的市场认知**，极有价值。

### 5.1 土耳其 IT 市场结构（数据源：TÜBİSAT / Deloitte 为 TÜBİTAK 编制）
- 2019 年市场规模约 **1.56 亿 TL**（修订后 1.53 亿）
- **以 TL 计连年增长，以美元计则不然** → 汇率压力（*"sürekli olarak artan kur baskısı"*）
- 硬件占比约 **20 亿里拉，约 13%**

### 5.2 ⭐ 国产化率（关键）
| 类别 | 国产使用率 |
|---|---|
| 服务 / 软件 | **约 70%**（有语言、成本、运输优势） |
| **硬件（IT）** | 2019 **17%** → 2020 **19%**（+2） |
| **硬件（通信技术）** | 2019 **16%** → 2020 **15%**（−1） |

→ **软件服务高度国产化，硬件严重依赖进口**；这正是 Angora 的生存空间，
也是 Levent 反复强调"国产自主"的根本原因。

### 5.3 ⭐ 研究问题与三大假设
**研究问题**：投标中国产与进口产品相遇时，**即便国产品具备同等能力，偏好仍普遍倒向进口产品**。

| # | 假设 | 内容 |
|---|---|---|
| H1 | 既往采购经验 | 以往采购中的负面经验**负面**影响新采购 |
| H2 | 民族主义情绪 | **不影响**决策（*"milliyetçi duygular… bunu etkilemez olarak belirledik"*） |
| H3 | 风险感知 | 决策者认为**采购国产风险更高** |

> 💡 **对 Simon 的直接意义**：**打"民族牌"没用**（Angora 自己研究证实）。
> 真正起作用的是 **① 既往使用体验 ② 风险感知**。
> → 我方应集中资源在**降低客户风险感知**（认证、案例、质保、样品测试通过率），而非强调身份。

### 5.4 方法论与样本
- **判断抽样（judgmental sampling）**，经 **LinkedIn** 发放
- **24 道**问题，发予 **1,000 人** → 回收 **115** → **剔除 69**（6 人无决策权、3 家外资公司决策在境外）→ **有效样本约 46**
- 受访者画像：**>90% 男性**；**80%+ 年龄 36–54**；**~90% 本科及以上学历**；**~90% 为总监及以上或企业主**
- 企业分层指标：员工数 / **AP 数** / 外资持股比例

---

## 六、⭐⭐ 产品组合（Can Hayat 系统工程师 · 逐条）

| 产品线 | 要点 |
|---|---|
| **Kenar Anahtarlar / VERGE（边缘交换机）** | 首个产品线，"ilk göz ağrımız"（初恋）；**8–48 口**全覆盖；支持堆叠、冗余电源 |
| **Endüstriyel（工业交换机）** | ⭐ 已部署于 **Eskişehir** 与 **Antalya**；**4–48 口**；**IP30**；宽温；强调"多端口数丰富度"是我方差异化点 |
| **Kaleiçi（非网管交换机）** | 面向 CCTV / 承包商，低价走量；⭐ **独家销售权归 "filteknoloji"**（新公司名） |
| **Gordion（数据中心交换机）** | ⭐ 命名取自安卡拉 Polatlı 29km 处的弗里吉亚古都 Gordion（戈尔迪乌姆之结 / 亚历山大大帝） |
| **angoraNMS（网管系统）** | ⭐ "**完全自研**"；可管理自有设备 + **监控其他品牌**；拓扑图、告警、温度/CPU、短信邮件、报表 |
| **ThinC / Thince（薄客户端）** | 基于 Asus；**野战医院**（sahra hastaneleri）场景加 4G/5G 模块；学校实验室 / 酒店前台 / 呼叫中心 |
| **Karınca（蚂蚁）Packet Broker** | 数据包分发，"智能交通警察"；数据中心流量调度 |
| **Arrow Data Diode（数据二极管）** | 单向数据传输；军工 / 工业 / 金融 / 医疗；见 §7 |
| **Arı（蜜蜂）安全硬件** | SD-WAN 安全服务设备 |

### 6.1 ⭐⭐ Gordion 命名背后的战略隐喻（Can Hayat 原话）
> *"eğer bir **devlet kurumunun omurgasında** bizim anahtarlarımız çalışırsa,*
> *Biz oradaki **düğümü keser** ve yavaş yavaş sevinçlerimizi（ürünlerimizi）oraya verebiliriz."*

→ **翻译：如果我们能打进一个政府机构的骨干网，就等于斩断了那个"结"，
之后就能逐步把其他产品铺进去。**

⚠️ **这是 Angora 对我方最直接威胁的战略表述**：
**骨干交换机 = 楔子**，先占骨干再横向扩张。这与 Türk Telekom 项目完全对应。

### 6.2 ⭐ 已确认的落地项目（Can Hayat 原话）
- **TRT（土耳其国家广播电视）安特拉 campus** —— 整个网络 + WiFi 全部换成 Angora；
  此前用其他品牌"持续出问题" → **批量替换** → 二次采购
- **Konya Plato 项目** —— 第二次采购
- **Eskişehir / Antalya** —— 工业交换机（安塔利亚多雨、雷击、夏季高温）
- **KGS（城市交通监控）** —— 持有 **"trafik şekillendirme raporu"（流量整形报告）**，凭此可参与投标

> 💡 **KGS 流量整形报告**解释了为什么 Angora 能进 EGM（警察总局）项目 —— 他们**有证**。
> 我方若想进入同类项目，必须确认是否具备对应资质文件。

---

## 七、⭐ Arrow Data Diode（英文官方视频，2023-06-05，323 次观看）

- **定位**：*"more than a security device… a data transfer platform"*（不只是安全设备，是数据传输平台）
- **架构**：2 台以上设备 + 检查 / 传输 / 报告工具集
- **端口密度**：下联支持 **1G 与 10G**；**USB** 文件传输；可选**串口与 I/O**（工业与医疗）
- **电源**：**DC / AC 双输入，支持冗余**
- **传输协议**：Web、**FTP、SMB**；USB 设备 kiosk 模式；**SCADA**、管理流量、业务控制报文
- **检查能力**：检查文件**类型 / 大小 / 扩展名**；**清除元数据**防泄露
- **集成**：**ICAP** 与 **exchange API**，可与第三方安全方案对接
- **安全**：业界标准高强度算法加密；目录服务认证；全量日志与告警
- **管理**：Web 界面、拖拽式文件传输、目录服务 + 层级权限、心跳监控
- **目标行业**：**国防（严格分级）／工业（高速无损）／金融（监管合规）／医疗（隐私完整）**

> 💡 Arrow 是 Angora 面向**军工与关键基础设施**的拳头产品，与其政府项目战略完全一致。

---

## 八、⭐ Taylan Esen 自述（KOZ'23 · 流程总监）

- 头衔自述：*"Benim adım Taylan Esen… **Angora süreçlerinden sorumlu direktörüm**"*
  （Angora 流程总监；开玩笑说连办公室水壶都归他管）
- 提到 **Mehmet**（即 Mehmet Yasin Koru）负责设计细节：*"o kavramsal analizleri yapıyoruz… donanımını falan"*
- 提到 **İbrahim**（即 İbrahim Balcı）负责市场分析
- ⭐ **六段式管理流程**：
  1. **设计**（概念分析 + 市场分析 + 硬件设计）
  2. **原型**（硬件与软件**并行**开发——*"önce yazılım yapayım donanımı uydururum olmuyor"*）
  3. **集成测试**（反复："onunla çalıştım bununla çalıştım, müşteriye gönderiyoruz, bununla çalışmıyor diyor"）
  4. **产出**
  5. **培训与文档**（视频是他们的短板，*"videolar bunlardan bir tanesi ama farkındayız"*）
  6. **服务**（含可维修性：螺丝是否可重复获取、软件安全等）
- 办公室 **3 层**
- ⚠️ **自认短板**：视频内容制作不足

---

## 九、📺 ICTMEDIATV 访谈（外部媒体）

### 9.1 `yveHNxOXD3g` · 2020-10-12 · 4:30 · ⭐ 字幕完整到手
**Levent Kılıç 原话（土耳其语，译）**：
> *"Angora Network 2016 年成立，从事设计、生产、销售与营销的科技公司。*
> *我们工作在**网络技术**领域，**生产、设计、销售交换机和路由器**及类似技术设备。"*

> ⭐ ***"2021 年我们的目标：把今年开始的**出口销售**做大，用更多的对外贸易为经济做贡献。"***

> *"数字化……即使开一家最简单的店，不建立 IT 基础设施什么都做不了。"*
> *"**公共部门必须发挥领导作用**（kamunun liderliği），数字化越快，适应就越快。"*
> *"要发展国产产品，我们具备一切潜力，但需要建立**生态系统**——激励、财政支持、税收支持、配套产业技术能力。*
> *环境对了，我国的潜力绰绰有余。"*

→ **2020 年即开始出口**，且 Levent 高度依赖"政府主导 + 生态扶持"叙事。

### 9.2 `z0loF632E2s` · 2023-05-24 · 40:43 · 138 观看
- 节目 *Açık Açık*，主持人 Murat PEHLİVAN，嘉宾 **Angora Networks Genel Müdürü Levent KILIÇ**
- 主题：国产技术网络设备、交换机、国产设备在土耳其市场的地位
- 标签：`#AngoraNetworks #Switch #Network #Broker #Ağ #Teknoloji #SFP #SDWAN #NMS #ictmedia`
- ❌ **字幕未能取出**：页面被 JS 撑成 171 分块，有效内容被淹没
  → 与自有频道不同，此条**仍需本地浏览器 + 手动复制**。

---

## 十、🎯 对我方（Simon / SmartByte）的行动含义

| 发现 | 含义 | 建议动作 |
|---|---|---|
| **"民族牌无效"**（Angora 自研结论） | 不要再靠"支持国产"打动客户 | 转向**降低风险感知**：认证、案例、质保、样品测试 |
| **Angora 主打"10 周交期"** | 交期是他们的核心卖点 | 我方交期必须 ≤10 周，否则直接失分 |
| **Gordion 的"斩结"战略** | 对方想用骨干交换机楔入政府客户再横向扩张 | 在 TT 项目上必须守住**骨干位** |
| **国产化率 68%→80%** | 政府项目的硬门槛在提高 | 我方作为外国供应商，需靠**与 Angora 绑定**间接满足 |
| **KGS 流量整形报告** | 有证才能投标 | 确认我方是否需提供对应资质文件 |
| **100+ SKU 库存 / 2000+ 在网设备** | 对方规模并不小 | 报价策略不可按"小厂"对待 |
| **仅靠推荐招聘** | 组织封闭、人员稳定 | 挖人难度高；关系维护集中在 Levent/Taylan 两人 |
| **Intel developer license** | 技术背书 | 我方可用 Marvell 对标叙事 |
| **Arrow 面向军工/关键基础设施** | Angora 在向高毛利安全产品延伸 | 关注其对交换机业务的资源挤压 |

---

## 十一、📌 待办 / 死胡同更新

| 项 | 状态 |
|---|---|
| YouTube 字幕"全被墙" | ❌ **结论错误，已推翻**。自有频道 6 个视频字幕全部可读 |
| `z0loF632E2s`（40:43 长访谈）字幕 | ⏳ **仍未取出**，需本地浏览器手动复制 |
| Instagram `angora_networks` | 🆕 已定位账号，直接抓取 **403**，需登录 |
| 官网 `/angora-kozz23/` | ❌ **已 404 删除** → 建议 Wayback Machine 取历史快照 |
| `angora.club`（Club Angora） | 🆕 已定位，抓取失败（多次）；待重试或用 Wayback |
| **filteknoloji**（Kaleiçi 独家销售） | 🆕 新公司名，待查 |
| **ELCORE**（分销商） | 🆕 待深挖合作范围 |
| **SIBEREUM**（关联公司） | 🆕 待深挖 |
| ThinC 培训视频 `mPVd05zz4VM`（1:35:56） | ⏳ 未取字幕，待办 |


---

## r108 具名勘误：假设、调查结果和单位不可混用

- **修正／取代本档“民族牌没用、Angora 自己研究证实”**：市场视频工具返回转写把“不影响”列为初始假设，但演讲者最终称其有作用，并说约半数回应支持本土产品。该判断抽样不是全国概率样本、真实采购或因果证明；也不推断“必然有效”。对负面购买经验的假设，演讲者说本研究未能证明，不等于永远无影响。
- 本档 `20 亿 TL` 的硬件数字与视频转写 `20 milyar` 单位不符：后者字面为 **200 亿 TL**。转写 `156/153 milyon` 总盘与硬件／13% 也不自洽，未听原音不能定因。2020 媒体转述的 2019 TÜBİSAD 行业总盘 `152.7 milyar`、IT 硬件 `20.4 milyar` 另列，不冒充演讲原话或 Angora 财务。
- `115−69=46` 是基于含糊转写的条件算术，排除原因和总体代表性未核。`sahada` 不等于在线，超过 100 产品不等于 100 SKU；历史本土率／目标不证明任何政府项目的普遍准入义务，**撤回本档该推广**。旧 Intel 开发授权名称、范围和期限未得原件确认。
- 预告的 `2022-10-19` 是计划日期，后续视频上传不独立证明当天如期召开；保留对将这则预告直接定为 2023-10-19 的撤回。渠道视频另外一次抓取的前两块因分块漂移隔离不用。

详见 [r108 主报告](../08-customer-pipeline/177-angora-koz-survey-channel-evidence-r108-2026-10-26.md)与[档案附录](../09-orders/120-angora-orders-dossier-2026-10-21.r108-appendix.md)；旧文字及前缀均保留。


---

## r109 具名限定：六步流程、视频覆盖与观看量推论

- **限定本档 §8 的“六段式管理流程”**：本轮目标视频 `C43VQBJtdrk` 及别名未能获取全文，未听音或看幻灯片；这仍是旧二手摘要，不能推为正式 SOP、所有型号的强制顺序或实际执行。仅有名字的人物对应、具体内部职责和视频制作短板亦无法据本轮资料确定为现行事实。
- **限定本档开头及 §11 的“全部字幕可读”**：同档把薄客户端培训视频列为字幕未取，本轮两个目标视频的直接页及别名均失败；不能说全部已取得，也不能由本轮失败推断当时必然不可读。
- **修正并取代本档 §2 由低观看量推断“内部资料、几乎无人研究”**：有限观看数不能证明私有性、保密性或研究者人数；2022 预告的拟定受众不证明活动实际举办或资料是私有。
- **限定本档 §9 将 2020 年视为已证首次出口年**：对应短访谈本轮未取到；2023 访谈有已经向国外发货的管理层自述，但没有独立给出首次出口年。不否认出口陈述。

详见 [r109 主报告](../08-customer-pipeline/178-angora-product-lifecycle-evidence-r109-2026-10-26.md)、[档案附录](../09-orders/120-angora-orders-dossier-2026-10-21.r109-appendix.md)及[字段映射](../09-orders/120-angora-orders-master-2026-10-21.mapping-r109.md)。原前缀保留；本轮不联系任何人或重启已 PASS 事项。
