# 115 · 土耳其 B 档深挖总表（r46 · 2026-11-01）

> **这是什么**：`TR Customers/B/` 里 **77 家 B 档客户**的**横向汇总表**。
> 逐家的详细内容（主体核实 / 品类 / 切入点 / 打法 / 证据等级）在各自的
> `TR Customers/B/<序号>-<slug>.md` 的 **「附：B 档深挖（r46）」** 小节里；**本文件只做索引与排序**，不替代原文。
>
> **本轮范围**：**只做 B 档 77 家**。
> - **A 档（33 家）本轮不重做**——A 档已经是文档最厚的一档（15 家有完整研究档案），按用户指令「A 类似乎已经挖完了」处理。
> - **C 档（36 家）本轮零投入**——按用户指令「C 类就是不跟进的了，没那么多精力」处理。**C 档没有任何 r46 新增内容**，`TR Customers/C/` 保持 r45 原样。

---

## 一、一句话结论

**B 档被严重低估了。** 77 家里：

- **11 家已经在卖交换机**（其中 6 家有**自有品牌或白牌型号**，可谈 OEM/二供）——这些不是「潜在客户」，是**已经在花钱买同类产品的公司**。
- **17 家是工业/弱电相邻品类**（布线、机柜、PLC、工业通信、车牌识别、护理呼叫）——**交换机是它们的配套缺口**。
- **22 家是工程商/集成商/小电商**——量小但真实，适合「现货 + 小批量」。
- **10 家是结构错配或资料空白**——应**移出或降档**，不要再投入销售时间。

---

## 二、🔴 已经在卖交换机 = 最优先（11 家）

> 判据：官网/电商上有**具体交换机型号**，或明确列了 switch/PoE 品类。**谈「二供 / 贴牌 / 补档」，不谈「教育」。**

| # | 公司 | 它现在卖什么（证据） | 我方缺口位 | 首封主题（土耳其语） |
|---|---|---|---|---|
| 6 | **Coptek (Koptek)** | 整条网络产品线：Omurga/DC/PoE/L3/L2/工业/SFP；型号 **`S4600-28X-SI`**（24GE+4×10G）→ 疑似白牌 | **2.5G、802.3bt、工业宽温** | `S4600 / S5700 同规格第二源 + 2.5G/bt 补位` |
| 14 | **NFS Teknoloji** | ⭐ 自有/代理 **Surenix `SRX-*`** 全梯子（8→24 口、工业、**L3 + 4×10G**）+ `ONSW-IMS8PP` | 同规格平替 + 工业线 | `SRX-4GS24PP+ / SRX-10GS24PX-L3 — alternative source` |
| 18 | **iotsistem** | ⭐ 自有 **`MLB-E4xxx`** 工业线（5/10/14/**28 口**，管理/非管理，含 PoE 与光纤） | **2.5G、802.3bt、更大端口密度** | `MLB-E4xxx 同规格代工 + 2.5G/802.3bt 补位` |
| 62 | **Cebeci Grup** | ⭐ 在售 **`S5700-24G-4FR` / `S5700-24G-4TFR`**（L3 网管，24GE + 4×10G）→ 白牌，**无品牌名** | **2.5G / bt / 工业**；电商需要现货 | `S5700-24G-4TFR muadili + 2.5G/bt 补位` |
| 79 | **Eurocam Güvenlik** | ⭐ 授权分销 **Ruijie（锐捷）**；自有品牌 Eurocam/Europer/Eurolink；**500+ 经销商** | 「Ruijie 之下的经济层」+ Eurocam 贴牌 | `Ruijie yanında ekonomik katman: Eurocam markalı PoE switch` |
| 15 | **Koza Güvenlik** | 有 **PoE Switchler** 分类；★ 自设**进口部**；Greentech 做安装 | PoE 梯度太薄（只有几款） | `PoE switch 全梯度补位 + Greentech 项目配套` |
| 19 | **Lansan** | `Switch ve Aktif Ürünler`；强项是无源件，**自称配线架制造商** | 有源（交换机）整块 | `Switch & aktif ürünler — üreticiden doğrudan` |
| 33 | **HCS Kablolama** | 布线批发 A.Ş.（2000）；**无有源产品** | 交换机整块 + 项目整套报价 | `Proje bazlı switch tedariki — HCS markasıyla` |
| 10 | **ErETE** | ★ **XPS 工业交换机**，标注 **EGM 认证**；XPCABLE 布线 | 工业交换机代工 + EGM 认证协作 | `XPS industrial switch — second source + EGM-ready` |
| 35 | **Antalya Turkuaz** | ⚠ 代理 **TP-Link / Omada / VIGI** + Dahua + Teknim | **只打「非管理批量替代」**，不抢 Omada 客户 | `Otel projeleri için ekonomik PoE switch（Omada alternatifi değil）` |
| 49 | **Zeytek** | 品类里有 **Network Cihazları**（无品牌）+ **MOBESE 柜 / 户外柜** | **柜内交换机** | `MOBESE / saha kabinleri içi switch tedariki` |

> ⚠ **第 11 家是 #67 Metcom（自研 MTC-500 车牌识别）**——它不卖交换机，但**它写自己系统的 BOM**，进 BOM 比进货架值钱。归到下面「技术型」里。

---

## 三、🟠 相邻品类 / 配套缺口（17 家）

> 它们的交换机是**"客户会问但自己不做"**的缺口。

| # | 公司 | 它做什么 | 配套缺口 |
|---|---|---|---|
| 10 | ErETE | 布线 + 工业交换机 + AI 服务器 | （已列上表，双属性） |
| 31 | **F.A.S.T.** | 工厂自动化 / 工业以太网 / 防爆 / SCADA（1994，32 人） | 工业 PoE 二供（降本） |
| 50 | **Foline** | 数据中心 + 集装箱 DC + 结构化布线（Siemens/CommScope 伙伴） | ⭐ **写进它的 şartname（招标规格）** |
| 60 | **GMT Control (GMTCNT)** | ⭐ 土耳其第一家国产 PLC（2014，51–200 人）+ HMI/变频/伺服 | ⭐ **PLC 柜内 DIN 导rail 交换机**（纯互补） |
| 63 | **Areskom** | 工业通信分销（Westermo/Moxa/Belden/Tektelic 级） | **只切「边缘/分支」，不碰核心环网** |
| 64 | **İntenet** | 1993，电信基础设施，电厂/变电站通信（TEİAŞ OPGW/RTU） | **变电站站内 PoE** |
| 67 | **Metcom A.Ş.** | ⭐ 自研车牌识别 MTC-500 / 卡口 / 计数系统 | ⭐ **杆上户外 PoE（IP66/6kV/−40~75°C）进 BOM** |
| 73 | **Kiracı Bilişim / ZKR** | ⭐ 医院 IP 护理呼叫（700+ 套），Ankara | ⭐ **长距 + 无风扇 PoE**（一个 500 床医院 ≈ 1,000 口） |
| 48 | **Bilge Güvenlik** | Axis/Milestone/Hikvision + Honeywell（2004） | **Hikvision 项目的 PoE 替代**（不碰 Axis） |
| 42 | **Bilgen Elektronik** | Gebze 工程商，公开转发 Teknim/Polimek | **Gebze OSB 厂区周界**（长距+防雷+宽温） |
| 39 | **MEPA** | 弱电全品类，**Perpa + 开塞利双点** | **开塞利 OSB 工业 PoE**（地理空白） |
| 38 | **Fourline** | 布尔萨，天线起家 → CCTV/网络/报警（品牌权 2007） | **布尔萨汽车工业厂区**（按「工厂」打，不按「安防」打） |
| 29 | **Desecure** | ⭐ 1,400+ 人 / 9 据点 / 自研 **MIA-MID-MAS** 移动监控 | ⭐ **移动监控杆/车的 DC 宽压工业 PoE** |
| 45 | **Alamthal** | ⭐ **利比亚市场**（`.ly`）+ 伊斯坦布尔采购办 | ⭐ **利比亚重建：宽压/防雷/耐高温，FOB İstanbul** |
| 13 | **Rima Elektronik** | ⭐ **Digifort（VMS）土耳其** + 方案设计 | **组播/IGMP 兼容的 PoE**（给兼容性说明） |
| 12 | **CCS Güvenlik** | 伊兹密尔最大分销（自述），2016 成立，2018 进伊斯坦布尔 | **小批量快返 + 可贴 CCS 牌** |
| 11 | **Eretekne / ISEE** | ⭐ **ISEE 自有品牌** IP 摄像机，自己进口批发 | ⭐ **「ISEE 牌 PoE 交换机」纯增量** |

---

## 四、🟡 工程商 / 集成商 / 电商（22 家）——量小但真

| # | 公司 | 形态 | 打法要点 |
|---|---|---|---|
| 16 | Portel Teknoloji A.Ş. | 工业网络 + 半导体贸易 + 电商，**有 USD/EUR 账户** | 小批量 + 快样品，报价一步到位 |
| 17 | RF Teknoloji | CalAmp 代理，覆盖中东/中亚/巴尔干 | ⚠ 谈**互补**（它做无线回传），不替换 |
| 22 | TeleOne | 伊兹密尔 + **安卡拉**双点，客户是**公共机构** | 给「投标支持包 + 授权书」 |
| 27 | ONSİS | **ISAF 2025 最后一天回展台要样品** | ⭐ **不需要调研，直接进样品+报价** |
| 37 | Shnrise | 安装/服务（2012） | WhatsApp，8/16 口现货，坏了换新 |
| 47 | Pelikan Bilgisayar | IT 转售（Aktif Network/ATEN/东芝），法定名含 **İth. İhr.** | 补 Aktif 缺的 2.5G/bt/工业 |
| 65 | Teamon | 安卡拉 SI，办免费「Ağ+」培训 | ⭐ **给它培训样机与教材**（低成本长尾） |
| 66 | İnovatech | Perpa 工程商（2014-08-21），法定名含 **Dış Ticaret** | 问「自进口还是本地拿货」 |
| 69 | Teknolojipazar | 安塔利亚电商（2010，11–50 人） | 给**土耳其语详情页素材 + 现货**，只推 8/16 口 |
| 68 | Egemen Elektronik | Ümraniye 分销，**2023 营收 +201%**，仅约 10 人 | 主打现货短交期；⚠ **账期严控** |
| 41 | FH Güvenlik | **2025 年新公司**，只有手机号 | ⭐ 供应商空白=最容易进；WhatsApp，前两单预付 |
| 44 | PROVES | 伊兹密尔大 SI（**201–500 人**） | 只谈「分支机构/园区 PoE」，不碰数据中心 |
| 124 | Interland Group | 1995 贸易集团，**含中国分支** | ⚠ **先确认它到底做不做产品线**，再谈 |
| 126 | Nazemco | 纯进出口（İth. İhr.） | 当**转口渠道**（利比亚/伊拉克/叙利亚） |
| 23 | Konak Güvenlik | 伊兹密尔 Konak 区，**主体未确认** | 一次通话建档；按安装商打 |
| 40 / 114 | AG Bilgisayar | **主体未确认**（撞 AGR Bilişim） | 一次通话问全称+网址 |
| 36 | Go Technology | **主体未确认**（只撞到美国两家同名） | 一次通话问全称+网址 |
| 70 | TekmarShop / Tekmar | **主体未确认**（撞 teknomarketshop + 疑似 #38 电话） | 先问「Tekmar 与 Fourline 是不是同一家」 |
| 105 | IHM Technology | 公开面近零（只有一位员工 LinkedIn） | LinkedIn 问全称，暂不投入 |
| 101 | Necdet Şenkaçayc | **只有人名 + 电话** | WhatsApp 一次通话建档 |
| 106 | Sinerjik (Ufuk Gökalp) | **只有人名 + 品牌通用词** | 用人名搜，不用品牌名搜 |
| 123 / 128 / 130 | Sedat / Fatih A. / 90543… | **只有人名或只有号码** | WhatsApp 直连，一次通话建档 |

---

## 五、⚫ 结构错配 / 建议降档（10 家）

> **这一节是本轮最重要的"减法"。** 这些档位不是"资料不足"，是**打法不对**。

| # | 公司 | 实际是什么 | 建议 |
|---|---|---|---|
| 34 | **Stasanet d.o.o.** | ⚠ **塞尔维亚（贝尔格莱德）公司**，Jablotron 官方进口商 | **移出土耳其名单**；若要进巴尔干，走出口流程重开 |
| 28 | **Hiperonline**（.com.tr） | ⚠ **ISP**（卖无合约宽带） | **降 C**；先确认 `hiperonline.com`（Eskişehir）是不是另一家 |
| 32 / 102 | **Fiberix** | ⚠ **ISP**（自有 **ASN 185.207.56.0/22**） | **降 C**；只问「企业侧 CPE 是否你们配套」 |
| 43 / 104 | **Düzgün Toptan / teksarf** | ⚠ **纺织辅料 B2B**，与弱电无关 | **降 C（品类不符）** |
| 71 | **Baburtech** | ⚠ **笔电备件 + 主板级维修**（5,000 m²），无网络品类 | **降 C**；唯一用途：本地 RMA/翻修伙伴 |
| 30 | **ORAL** | ⚠ **KKTC / 北塞浦路斯**（不是土耳其本土） | 保留但**改标市场**；清关路径先问清 |
| 55 | **ULAK Haberleşme** | ⚠ **国家级设备商**（SSB 参股 + Aselsan 主承包） | **不是客户**，是**市场情报源**；只谈"应急通信车内的部件供应" |
| 51 / 126 | **Nazemco**（重复档） | 纯进出口、无技术面 | 转口渠道定位，不按本地分销谈账期 |
| 46 / 100 / 102 / 116 / 117 | 重复登记档 | 与 A 档或同批其他档同一家 | ⚠ **只联系一次**（两家销售同时发信会掉分） |
| 20 | Optima（有完整档案） | 价格锚 **$35/120 W** 太低 | 不做入门款；只打 **bt / 24 口 / 宽温** |

---

## 六、⚠ 需要人工拍板的三件事

1. **升 A 候选（12 家）**：`6 Coptek`、`10 ErETE`、`14 NFS`、`18 iotsistem`、`19 Lansan`、`29 Desecure`、`33 HCS`、`62 Cebeci`、`73 ZKR`、`79 Eurocam`、`31 F.A.S.T.`、`67 Metcom`。
   → 共同理由：**已在卖同类产品 / 有自有品牌 / 有明确 BOM 缺口**，商业质量高于部分 A 档。
2. **降 C 候选（6 家）**：`34 Stasanet`、`28 Hiperonline`、`32/102 Fiberix`、`43/104 Düzgün`、`71 Baburtech`、`55 ULAK`。
   → 理由见第五节，**都是"品类/地域不对"，不是"资料不足"**。
3. **改名/改市场（2 家）**：`30 ORAL → KKTC`、`45 Alamthal → 利比亚（İstanbul 采购办）`。

> ⚠ 上述三件事**本轮只提出建议，未改动任何 `层级` 字段**（`111` 是唯一权威，改档需要人工确认）。

---

## 七、本轮的方法与证据纪律

| 做法 | 说明 |
|---|---|
| 反向查「型号」而不是查「公司名」 | Coptek/Cebeci/iotsistem/NFS 的突破点全部来自**它们官网上的具体型号**（`S4600`/`S5700`/`MLB-E4xxx`/`SRX-*`） |
| BGP / ASN 判定 ISP vs 分销商 | Fiberix 的 **ASN 185.207.56.0/22** 一锤定音；Hiperonline 靠业务页定性 |
| 企业登记站（税务/注册日） | CCS **2016-03-28**、İnovatech **2014-08-21**、Lansan **2019-12-04**、HCS **2000-11-22**、Egemen **2013-07-25** |
| 域名国别判定市场 | Alamthal 的 **`.ly`** → 利比亚；Stasanet 的 **`.d.o.o.`** → 塞尔维亚 |
| 不合并、不猜测 | 10 家主体未确认的档位，**一律写「主体未确认」+ 一次通话建档**，不给假信息 |

**诚实边界**：本轮 77 家中，**约 12 家的关键事实（法定名/注册日/地址）有 2 个以上独立来源**；**约 25 家只有官网单一来源**；**约 10 家公开面为零**（`101/103/105/106/123/128/130/36/40/114`）。**营收数字全部为第三方估算（ZoomInfo/EMIS/Tracxn/RocketReach），不可当事实引用。**

---

## 八、下一步

1. 人工拍板第六节的三件事（升 A / 降 C / 改市场）。
2. 按第二节的 11 家**逐家出「型号对位表」**（这是唯一会被认真看的附件）。
3. 第三节的 17 家走**「补位」话术**（不要说"替代"，说"你们报布线/柜子，我们补有源"）。
4. 第四节只做**分批发信 + WhatsApp**，不投入调研时间。
5. `27 ONSİS` **单独一条线**：样品 + 阶梯报价，**本周内**。

---

**相关文件**
- 逐家详情：`TR Customers/B/<序号>-<slug>.md` 的「附：B 档深挖（r46 · 2026-11-01）」
- 权威源表：`…/08-customer-pipeline/111-turkey-customer-pipeline.csv`
- 生成脚本：`…/08-customer-pipeline/build_tr_customers_r44.py`（已内置 B 深挖数据注入）
- 数据模块：`…/08-customer-pipeline/b_deepdig_data_1.py`（#6–30）、`b_deepdig_data_2.py`（#31–130）

---

## 九、r47 修正与补充（2026-11-01）

> 本文件主体（§一–§八）写于 r46；r47 又抓了一轮，**有 2 处需要修正、1 处需要升级**。**不覆盖原文，只在此追加**。

### 1. ⚠ 修正：`#62 Cebeci` 的品牌归属

- r46 写的是「`S5700` 页面无品牌名 → 疑似白牌贴 Cebeci 的牌」。**r47 抓了 `cebecigrup.com` 首页后判断需修正**：
- Cebeci 的**真实品牌宇宙是电信测试与 FTTx**：代理 **Argus、Cifocs、CMG、Greenlee-Tempo、InterCoax、Micos、Trend Networks**（官网"Markalara Göre Ürün Gruplarımız"）。
- 它的工业交换机与光纤转换器线挂的是 **`Cifocs`** 品牌（官网"Endüstriyel Switchler"分类首图 = **`Cifocs CFC-4G2SFP-IPS`**）。
- → **修正后的判断**：`S5700-24G-4FR` / `-4TFR` 是它**电商挂品（大概率代发/白牌）**，**不是它的自有品牌线**；**真正该谈 OEM 的是 `Cifocs` 这条线**（若 Cifocs 为其自有商标）。
- 同一轮补齐的**新事实**：**地址 = Halil Rıfat Paşa Mah. Yüzer Havuz Sok. No:8 D:24, Okmeydanı / İstanbul 34384**；**电话 +90 212 320 08 88 / 320 08 85**；**邮箱 `iletisim@cebecigrup.com`**。

### 2. ⭐ 升级：`#10 ErETE` 应改判 **A**

- r47 抓到 `erete.com.tr` 完整产品分类，发现它**不只卖 XPS**：
  - **`OPEN NETWORKING`** 与 **`NOS（Network Operating System）`** 两个独立分类；
  - 代理 **IP Infusion**（开放网络 NOS）与 **EtherWAN**（台湾加固工业交换机）、**LANDE**（布线）；
  - 自有 **XPS** 工业线全型号：`XPS-I7120-6/-10/-14/-16/-24`（非 PoE）、**`XPS-I7120-6P/-10P/-14P/-16P`（PoE）**、**`XPS-I8120-16`（12×GE + 4×10G SFP+，L2+）**、`XPS-I8120-24F`（12×GE + 8×SFP）；
  - EtherWAN 线：`EX89000 / EX87000 / EX77000 / EX83000 / EX61000A / EX70900 / EX72000 / ECS4660-28F`、加固 PoE `ER59000 / ER58000`、`EX75000 / EX76000 / EX78000 / EX78602 / EX74000 / EX46100 / EX48000`。
- → **它已经是"开放网络 + 工业网络"的完整分销商**，与 Angora 的产品域**正面重叠**：**这是 B 档里唯一具备"白盒 + 第三方 NOS"能力的客户**。**建议直接升 A，并列为第一批要打的 3 家之一。**

### 3. 新增：`116-b-a-model-mapping-2026-11-01.md`

- r47 把 11 家 B + 8 家 A 的**在售型号逐条对位到我方型号**（含缺口矩阵、价格锚点、必问三句、以及"我方没有的档位照实写缺"）。
- **本文件仍是"分档与优先级"的总表，具体对位去打 `116`。**
