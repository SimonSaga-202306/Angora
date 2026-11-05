# -*- coding: utf-8 -*-
"""B 档深挖数据 · 第 2 批（111 序号 31–130）。内容来自 2026-11-01 的公开检索。"""

D = {}

D['31'] = """
### 一句话
**F.A.S.T. 是土耳其"工厂自动化系统集成"的老牌 A.Ş.**（**1994** 成立，Ataşehir，约 **32 人**），做的是**工业以太网 / 现场总线 / SCADA / 防爆**，客户是**工厂与流程工业**。**这是 B 档里"工业 PoE 最对口"的一家**——它卖的不是安防，是车间网络。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **Fabrika Aygıtları Sistem Teknolojisi A.Ş.**（F.A.S.T.） |
| 成立 | **1994** |
| 规模 | 约 **32 人**（第三方） |
| 地址 | **Ataşehir / İstanbul** |
| 域名 | **`fasttr.com`**（+ `fast.com.tr`） |
| 总经理 | **Şener Üstbaş** |
| 邮件 | `first@fasttr.com`（域名习惯；另有具名邮箱） |

### 它在做什么
- 自述三个方向：**工业以太网 / 现场总线网络、控制系统集成、软件与 SCADA**。
- 自述资质：**防爆（Ex-proof）/ 危险区域（tehlikeli bölge）项目经验**、TÜV/功能安全相关表述。
- ⚠ 它**不是安防商**：摄像机不在它的语汇里，**工业交换机在**。

### 与我方的切入点
1. **工业交换机是它的日常品类** → 它已有固定供应源（多为德国/台湾品牌）→ 我方定位是**"降本二供"**，不是开荒。
2. **防爆/危险区域** → 需要**宽温（−40~75 °C）、IP40+、DC 宽压、DIN 导rail、无风扇** → 我方 `EW-S1710FG-AP` / `DL-END3308PFG` 类可直接报。
3. **SCADA / 组播** → 需要 **IGMP Snooping + QoS + 802.1Q VLAN + SNMP**（它做环网），**环网协议（RSTP/MSTP、ERPS）要写清楚**。

### 打法
- 首封 **土耳其语**，给 `first@fasttr.com` 并 **抄 Şener Üstbaş**；主题 **"Endüstriyel switch — ikinci kaynak（Ex-proof projeleri için）"**。
- 附：**宽温 + DC 宽压 + 防雷 + 环网** 四行参数 + **一份 ERPS/RSTP 自愈时间**（工业客户只看这个）。
- 问：**"Ring topolojilerinde kendini toparlama süreniz kaç ms?"** —— 一问就知道它是不是真懂，也会让它认真回。

### 证据等级与空白
- 已核实：法定名、1994、约 32 人、Ataşehir、GM 姓名、业务方向（官网 + 展会名录 + 第三方三处一致）。
- 空白：营收、现交换机品牌、采购负责人。
"""

D['32'] = """
### 一句话
**Fiberix 是加济安泰普（Gaziantep）的"光纤互联网服务商（ISP）"，不是设备分销商**——它有自己的 **ASN 185.207.56.0/22**。⚠ **它买的是局端/骨干设备，不是我方 8/24 口 PoE。按名称打进去基本无效，按"它的客户"打才有意义。**

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **FİBERİX İLETİŞİM HİZMETLERİ LTD. ŞTİ.** |
| 地址 | **Gaziantep**, Zübeyde Hanım Blv. No:74/A |
| 电话 | **0850 333 2700** |
| 关键证据 | ⭐ **ASN 185.207.56.0/22**（自有 IP 段）→ **ISP 身份确定** |
| 规模 | ⚠ 第三方数据冲突：51–200 人 / $13.4M **vs** 1–20 人 / $1–9M（**不可信，按"中小"处理**） |

### 为什么它会被列进 B 档（以及为什么这是错的）
- 名字里有 "Fiber" → 被当成"光纤设备商"录进来了。
- 实际业务是**向终端用户/企业卖宽带**（GPON / 城域光纤）。
- ⚠ 与 #102 是**同一家**（跨批次重复）。

### 与我方的真实关系（三条，按价值排序）
1. ⚠ **直接卖交换机：机会极低**。ISP 采购走集采，且以 OLT / 汇聚 / 核心为主。
2. ✅ **它的"企业客户侧"（kurumsal müşteri）** 才是战场：企业专线开通时**客户侧 CPE/接入交换机**常由 ISP 配套。→ **可谈"CPE 配套"**，量稳定但单价低。
3. ✅ **它的工程队**（做 FTTH 施工）会用到**户外 PoE / 工业交换机**（杆上、楼道）→ **小批量、防雷、宽温**。

### 打法
- **不要首封卖产品**。首封问一句：**"Kurumsal müşteri tarafında CPE/switch tedarikini siz mi yapıyorsunuz?"**（企业侧 CPE/交换机是你们配吗？）
- 若答"是" → 走 CPE 配套；若答"否" → **本档归档**，不投入。
- 地址与电话走官网/`0850 333 2700`。

### 证据等级与空白
- 已核实：法定名、Gaziantep 地址、电话、**ASN 185.207.56.0/22**（BGP 注册数据）。
- 空白：真实规模（两套第三方数据互斥）、是否自建 CPE 供应链、决策人。
"""

D['33'] = """
### 一句话
**HCS 是"结构化布线批发商"**（`hcs.com.tr`，**2000-11-22** 注册的 **A.Ş.**，**İkitelli OSB / Başakşehir**），主业是**铜缆/光纤连接件 + 机柜**——**和 Lansan 同一生态位，但更老、公司化更彻底**。⚠ 网络上有名录把它的地址错写成 **Kayseri**，那是错的。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **HCS Kablolama Sistemleri Sanayi ve Ticaret A.Ş.** |
| 成立 | ⭐ **2000-11-22** |
| 地址 | **Boypas No:3A, İkitelli OSB, 8. Cadde, Başakşehir / İstanbul 34490**（⚠ 部分名录误记为 Kayseri） |
| 电话 | **+90 212 438 25 75** |
| 域名 | `hcs.com.tr` / `hescs.com` |

### 业务结构
- 品类：**Cat5e/Cat6/Cat6A 铜缆、光纤（OM3/OM4）、patch panel、keystone、配线架、机柜、线槽**。
- 客户：**项目型（企业、政府、医院、学校）+ 经销商**。
- 它有 **A.Ş. + 20+ 年** → **有正规财务与合规能力**（能开信用证、能进口）。

### 与我方的切入点
1. **"Switch 与 Aktif Ürünler" 是它的空白**（和 Lansan 一模一样：强在无源，弱在有源）。
2. **它做项目 → 需要"整套弱电包"**：布线 + 机柜 + **交换机**。我方补上交换机，它就能**一个报价单打完一个项目**（这是它最想要的）。
3. **A.Ş. + 2000 年成立** → **可谈年度框架 + 贴牌**（HCS 牌交换机），比年轻公司靠谱。

### 打法
- 首封给 `info@hcs.com.tr`，主题 **"Proje bazlı switch tedariki — HCS markasıyla"**（项目型 + 贴 HCS 牌）。
- 一句话：**"你们报布线，我们补有源，同一张 teklif（报价单）。"**
- 问：**"Projelerde switch'i siz mi veriyorsunuz yoksa müşteri mi alıyor?"**

### 证据等级与空白
- 已核实：法定名、**2000-11-22 成立**、A.Ş. 类型、İkitelli OSB 地址、电话、品类（企业登记站 + 官网 + 电话查询站三处一致）。
- 空白：员工数、营收、是否已在做贴牌。
"""

D['34'] = """
### 一句话
⚠ **Stasanet d.o.o. 不是土耳其公司，是塞尔维亚（贝尔格莱德）公司**——`Vojvode Hrvoja 28, Beograd`，2013/14 成立，2–10 人，由捷克背景的集团设立，是 **Jablotron（捷克报警系统）的官方进口商**，2025 年前后新签 **Cathexis** 分销。**它被误录进土耳其名单。**

### 主体（已核实）
| 项 | 内容 |
|---|---|
| 法定名 | **Stasanet d.o.o.**（**d.o.o. = 塞尔维亚/克罗地亚的有限责任公司**，不是土耳其的 Ltd. Şti.） |
| 地址 | **Vojvode Hrvoja 28, Beograd, Sırbistan（塞尔维亚）** |
| 成立 | 2013 / 2014（两处来源略有出入） |
| 规模 | **2–10 人**（小） |
| 背景 | 捷克创始人/集团背景（`stasanet.rs` 有捷克语关联） |
| 代理 | ⭐ **Jablotron 官方进口商（捷克报警系统）**；2025 年新增 **Cathexis**（VMS）分销 |
| 业绩自述 | **每年 200+ 合作伙伴** |

### 处理建议
1. ⚠ **从"土耳其客户"池里移出**，改标 **"Balkan / Serbia"** 或直接降 C。它不是土耳其市场。
2. 若我方要进**巴尔干**，它是一个**真实可用的进口商**（有代理经验、有品牌关系、人少决策快）→ **但要走"出口到塞尔维亚"的流程**（CE + 塞尔维亚本地认证），与土耳其完全不同。
3. **不要**把它和土耳其的 `033-hcs` / `019-lansan` 混为一类。

### 证据等级与空白
- 已核实：d.o.o. 主体、贝尔格莱德地址、Jablotron 官方进口商身份、Cathexis 分销、2–10 人、200+ 伙伴自述（官网 + LinkedIn + Jablotron 渠道页）。
- 空白：真实年采购额、是否愿意做交换机品类。
"""

D['35'] = """
### 一句话
**Antalya Turkuaz 是安塔利亚的区域分销商，而且它已经在卖 TP-Link 的 Omada / VIGI**——**我方与它是"同一条货架上的替代品"关系，不是补充关系。** 另外它代理 **Teknim（土耳其本土消防/安防）** 与 **Dahua**。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 名称 | **Antalya Turkuaz Bilişim Teknolojileri** |
| 地址 | **Muratpaşa / Antalya** |
| 电话 / 邮箱 | **0242 345 36 91** / `turkuaz@antalyaturkuaz.com` |
| 定位 | **区域分销商（bölge distribütörü）**，覆盖安塔利亚及周边省份 |

### ⭐ 代理矩阵（决定谈法）
| 品牌 | 品类 | 对我方的含义 |
|---|---|---|
| **TP-Link / Omada / VIGI** | 交换机 + AP + 摄像机 | ⚠ **正面撞我方交换机** → 谈"平替/降本"或"Omada 兼容" |
| **Dahua** | 摄像机 / NVR | PoE 需求的源头 |
| **Teknim** | 土耳其本土消防/报警 | 本土品牌关系强 → 说明它**愿意做土耳其本土品牌**（我方贴牌可走这条路） |

### 与我方的切入点
1. **它卖 Omada** → Omada 的核心卖点是**云管理**。我方若**不能提供云管理**，正面打必输。
   → **正确切法**：**"非管理/轻管理 PoE 批量替代"**（酒店、宿舍、小区这类"装完不管"的场景），**不打它 Omada 的客户端**。
2. **Teknim 关系说明它有本土品牌运营能力** → 可谈 **"Antalya Turkuaz 牌"或"Turkuaz"贴牌 PoE**。
3. **安塔利亚 = 旅游/酒店集中地** → **酒店弱电是最大场景**（客房 AP + 走廊摄像机 + 前台），**16/24 口 PoE + 长距**是主力。

### 打法
- 首封给 `turkuaz@antalyaturkuaz.com`，主题 **"Otel projeleri için ekonomik PoE switch（Omada alternatifi değil, tamamlayıcı）"**。
- **明确说"我们不来抢 Omada"**——这句话能决定它是否回你。
- 问：**"Otellerde 24 port PoE tarafında fiyat baskısı var mı?"**

### 证据等级与空白
- 已核实：地址、电话、邮箱、**TP-Link/Omada/VIGI + Dahua + Teknim 代理**（官网品牌页）。
- 空白：法定名、成立年、员工数、营收、现 PoE 供应商结构。
"""

D['36'] = """
### 一句话
⚠ **"Go Technology" 在公开网络中查不到土耳其实体**。两轮检索只命中两家美国公司（**GO Technology Group**，伊利诺伊 Oak Brook，IT 咨询；**GO Technology Management**，2004 年，托管 IT），与 111 记录无任何交集。**本轮结论：主体无法确认，先核名。**

### 检索实况（如实记录，不猜测）
| 检索角度 | 结果 |
|---|---|
| `"Go Technology" Türkiye bilişim` | 全部命中美国 / 印度公司 |
| `GO Teknoloji` | 未见与 111 记录匹配的主体 |
| 土耳其企业名录 / LinkedIn TR | 未命中 |
| 展会名录（ISAF 等） | 未命中 |

### 处理方式
1. **不补任何公司信息**。档案以 111 现有联系人/电话为唯一锚点。
2. 下一步只能靠人：**用 111 的电话/WhatsApp 直接问公司全称与网址**。
3. 若电话失效 → **降为观察项，不投入**。

### 与我方的切入点（假设它是 IT/系统集成商）
- 若它是"IT 服务/集成"型（与同名的美国公司同类）→ **它买 PoE 是"配套客户网络"**，量小但复购稳。
- 打法：**小批量 + 快速样品 + 不要求品牌**。

### 证据等级与空白
- 已核实：**无**。
- 空白：全部（法定名、地址、业务、规模）。
"""

D['37'] = """
### 一句话
**Shnrise 是"服务型"公司，不是分销商**：2012 年起做 **CCTV 安装 / PDKS（门禁考勤）/ 车牌识别（LPR）/ 消防**的**施工与服务**。**它买单台设备，不买批量。**

### 主体与坐标
| 项 | 内容 |
|---|---|
| 名称 | **Shnrise Güvenlik Sistemleri** |
| 成立 | **2012** |
| 地址 | İstanbul |
| 电话 | **0850 840 68 01** |
| 业务 | CCTV 安装、PDKS、LPR（车牌识别）、Yangın（消防）、维护服务 |

### 与我方的关系（实话）
- **它是安装商（montajcı）**：一年几十台到几百台，**单价敏感、品牌不敏感**。
- **不是分销商**：不要给它分销价、不要谈独家、不要谈年度框架。
- ✅ **它的价值是"零散但真实的出货口"** + **它能给现场反馈（哪种机器在安塔利亚/伊斯坦布尔的夏天会死机）**。

### 打法
- **走 WhatsApp + 电话（0850 840 68 01），不要发长邮件**（安装商不看邮件）。
- 一句话：**"8/16 口 PoE，现货，坏了直接换新。"**
- 问：**"Bir ayda kaç switch takıyorsunuz?"** —— 决定是否值得给账期。

### 证据等级与空白
- 已核实：2012 成立、İstanbul、服务范围（CCTV/PDKS/LPR/消防）、电话（官网 + 服务目录）。
- 空白：法定名、员工数、年装机量、现采购渠道。
"""

D['38'] = """
### 一句话
**Fourline 是布尔萨（Bursa）的"卫星天线起家、现做弱电批发+零售"的老渠道**，**2007 年取得品牌使用权**，产品线已扩到 **CCTV / 网络 / 报警**。它有**经销商网络（bayi ağı）**，是真正的"区域批发 + 全国经销"混合体。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 名称 | **FOURLINE / Özel Elektronik**（品牌权 2007 年起） |
| 地址 | **Şükraniye Mah. Ankara Cad. No:242, Yıldırım / Bursa** |
| 电话 | **0224 364 18 88** / GSM **0555 995 54 42** |
| 模式 | **批发（toptan）+ 零售（perakende）+ 经销商网络** |

### 业务结构（从"天线 → 弱电"的演化路径很关键）
- 起点：**uydu anten sistemleri（卫星天线）** → 这是土耳其"社区/楼宇弱电"的入口生意。
- 现在：**CCTV、网络、报警、天线** 全套 → 说明它**跟着客户需求扩品类**。
- 有 **bayi（经销商）网络** → **它就是"区域小分销"**，只是没到 Okisan 那个量级。

### 与我方的切入点
1. **布尔萨 = 土耳其汽车工业中心（Tofaş/Fiat、Renault、Bosch）** → **工厂 + 工业园**是本地最大场景 → **工业 PoE（宽温/防雷）在布尔萨比商用 PoE 更好卖**。
2. **它是"天线转弱电"的渠道** → 它的 PoE 认知可能不深 → **给它"选型表 + 场景图"比给价格有用**。
3. **品牌权 2007 = 它会做品牌运营** → 可谈 **"Fourline 牌 PoE"** 贴牌。

### 打法
- 首封给 `0224 364 18 88` 转采购 + 官网表单，主题 **"Bursa sanayi tesisleri için endüstriyel PoE switch"**。
- **按"工厂场景"打（不是"安防场景"）** —— 布尔萨的差异化就在这里。
- 问：**"Bayileriniz sanayi tarafında mı yoksa konut tarafında mı çalışıyor?"**

### 证据等级与空白
- 已核实：品牌权 2007、布尔萨 Yıldırım 地址、两路电话、批发+零售+经销模式、品类演化（官网 + 企业名录）。
- 空白：法定名、成立年、员工数、营收、现 PoE 供应商。
"""

D['39'] = """
### 一句话
**MEPA 是"伊斯坦布尔 Perpa + 开塞利（Kayseri）"双点的弱电老商**（15 年，11–50 人），品类是**消防 / CCTV / 数据网络 / 对讲 / IPTV / 光纤**—— **典型的"弱电杂货铺"，什么都卖一点**。它可能是**开塞利本地最有量的弱电批发**。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **MEPA Elektronik San. ve Tic. Ltd. Şti.** |
| 网点 1 | **Perpa Ticaret Merkezi B Blok No:187, Şişli / İstanbul** |
| 网点 2（关键） | ⭐ **Kayseri**: Sahabiye Mah. Otak Sok. No:41, Kocasinan / Kayseri，**0352 220 66 78** |
| 经验 | **15 年**（第三方）；**11–50 人** |
| 合伙人 | **Eren Gül**（co-owner） |

### 与我方的切入点
1. ⭐ **开塞利（Kayseri）是土耳其家具/金属工业重镇** → 有大量**工厂**与**OSB（工业区）** → **工业 PoE 需求存在**，且**安卡拉的品牌覆盖不到**（地理空白）。
2. **它是"弱电全品类"** → **加一条交换机线不需改组织**，只需有人推。
3. **Perpa 门店 + 开塞利分部** → 两套库存，**需要"能小批量补货的工厂"**。

### 打法
- 首封给 Perpa / 官网表单，**并抄 Eren Gül**；主题 **"Kayseri OSB projeleri için PoE switch tedariki"**。
- **一定要提"开塞利"** —— 它被当成"伊斯坦布尔小商"太久了，你一提开塞利，它就认真了。
- 问：**"Kayseri'deki müşteri profili sanayi mi yoksa konut mu?"**

### 证据等级与空白
- 已核实：法定名、**Perpa + 开塞利双地址与开塞利电话**、15 年、11–50 人、合伙人 Eren Gül、六大品类（官网 + 企业名录 + 电话查询三处）。
- 空白：营收、现交换机品牌、开塞利分部的实际规模。
"""

D['40'] = """
### 一句话
⚠ **"AG Bilgisayar" 在公开网络中指向的是 "AG Bilgisayar / Aycan Çam"（同名文件 #114）**，但检索只命中 **AGR Bilişim（安卡拉）**这一家异地公司，**无法确认与 111 记录是同一主体**。本轮：**主体存疑，先核名。**

### 检索实况
| 角度 | 结果 |
|---|---|
| `AG Bilgisayar` | 命中 **AGR Bilişim（Ankara）**，地址/业务与 111 记录不符 |
| `Aycan Çam`（#114 联系人） | 未见可对应的公司页 |
| 土耳其企业名录 | 无唯一命中 |

### 处理方式
1. **不合并 #40 与 #114**（按"一定不能合并"原则，保持两个文件、互相标注）。
2. 两个文件的**联系人可能相同（Aycan Çam）**，这是唯一可用线索。
3. 下一步：**用电话/WhatsApp 问全称 + 网址**；拿到后再补。

### 与我方的切入点（假设是 IT 转售商）
- "Bilgisayar" 命名 → 大概率是 **IT 硬件转售商**（服务器/PC/网络）。
- 打法：**PoE + 机柜 + 布线组合**，走"整套报价"而不是单品。

### 证据等级与空白
- 已核实：**无**。
- 空白：全部。
"""

D['41'] = """
### 一句话
⚠ **FH Güvenlik 是"2025 年才注册的新公司"**（`fhguvenlik.com`，Perpa 片区，**0534 484 98 11**），团队自称 15+ 年经验。**新公司 = 决策快、无历史包袱、供应商完全空白** → B 档里最容易进的一家，但**单量未知**。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 名称 | **FH Güvenlik Sistemleri ve Bilişim San. Tic. Ltd. Şti.** |
| 地址 | Halil Rıfat Paşa Mah.（Perpa 片区）, **Şişli / İstanbul** |
| 电话 | **0534 484 98 11**（手机，无座机 → 小公司特征） |
| 成立 | ⭐ **2025**（新） |
| 自述 | 团队 15+ 年行业经验 |

### 与我方的切入点（新公司的三个特点）
1. **没有历史供应商** → **第一批供货方 = 长期绑定**。这是最有价值的一点。
2. **只有手机号** → 老板即决策，**谈得快、也死得快**（要账期就崩）。
3. **Perpa 片区** → 它的客户是 Perpa 的批发商与安装商 → **它需要"能拆零"的供应**。

### 打法
- **WhatsApp 0534 484 98 11** 开场（新公司老板天天看手机），土耳其语，短句。
- 第一单：**5–10 台 8 口 PoE 试单 + 先说清账期（建议前两单预付）**。
- 问：**"Kuruluşunuz yeni — ilk tedarikçilerinizi seçiyorsunuz, değil mi?"**（直说它新，反而拉近距离）

### 证据等级与空白
- 已核实：2025 注册、Perpa 片区、手机号、自称 15+ 年（域名注册 + 站点 + 企业名录）。
- 空白：法定名全称、实际资金、客户结构。
"""

D['42'] = """
### 一句话
**Bilgen Elektronik 是盖布泽（Gebze / Kocaeli）的安防工程商**，LinkedIn 活跃、**转发 Teknim 与 Polimek** 的内容 → **它站队土耳其本土品牌**。**工业区（Gebze OSB）就在门口 → 工业 PoE 有真实场景。**

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **BİLGEN ELEKTRONİK GÜVENLİK SİSTEMLERİ TEKNOLOJİLERİ YAZILIM ELEKTRİK MAKİNA SAN. VE TİC. LTD. ŞTİ.**（法定名极长，说明登记范围很宽） |
| 地址 | **Osman Yılmaz Mah. 607/1. Sk. No:21, 41400 Gebze / Kocaeli** |
| 社媒信号 | LinkedIn 活跃；**转发 Teknim / Polimek** |

### 关键判断
- ⚠ **"转发 Teknim/Polimek" ≠ 代理**，但说明它**习惯用土耳其本土品牌**（价格/服务/语言优势）→ **它不是"只认国际大牌"的客户**，对贴牌/新品牌的接受度高。
- **Gebze = 土耳其最大工业区之一（OSB 密集，含 TÜBİTAK MAM、汽车零部件、化工）** → **厂区周界安防 + 车间网络**是本地主场景。

### 与我方的切入点
1. **厂区周界** → 需要 **长距 PoE（250 m）+ 防雷 + 宽温**（Gebze 冬天冷、夏天热）。
2. **它是工程商** → 买的是"项目配套"，**不做库存** → 需要"按项目交付、允许分批"。
3. **接受本土品牌** → **可以推"土耳其可注册的贴牌"**（它更愿意卖一个有本地感的牌子）。

### 打法
- 首封给官网表单 + LinkedIn 私信（它在 LinkedIn 活跃），主题 **"Gebze OSB tesisleri için endüstriyel PoE"**。
- 问：**"Teknim/Polimek kullanıyorsunuz — switch tarafını nasıl çözüyorsunuz?"**（顺着它公开的品牌偏好问）

### 证据等级与空白
- 已核实：超长法定名、Gebze 地址、LinkedIn 活跃、Teknim/Polimek 关联（LinkedIn + 企业名录）。
- 空白：成立年、员工数、营收、现交换机品牌。
"""

D['43'] = """
### 一句话
⚠ **"Düzgün Toptan Ticaret / teksarf.com" 查不到安防或网络实体**——`teksarf` 是**纺织/服饰 B2B 平台**，检索命中的全是纺织批发。**111 里这一行极可能是名单混入的错项**（与 #104 是同一行重复）。

### 检索实况
| 角度 | 结果 |
|---|---|
| `teksarf.com` | 纺织/服装 B2B（"tekstil sarf"= 纺织辅料），**与弱电无关** |
| `Düzgün Toptan Ticaret` | 通用土耳其批发商名录，无安防/网络命中 |
| 安防展会名录 | 未命中 |

### 处理建议
1. ⚠ **本档建议降 C（不跟进）**，理由：**品类不符（纺织 vs 弱电）**，不是资料不足。
2. 若用户侧坚持保留，**唯一动作**：问一句"你们是做什么品类的？"—— 一句话即可判定。
3. **与 #104 保持两个文件、互相标注**（不合并）。

### 证据等级与空白
- 已核实：`teksarf.com` 属纺织辅料 B2B（站点内容）。
- 空白：与 111 记录是否同一主体（**大概率不是**）。
"""

D['44'] = """
### 一句话
**PROVES 是伊兹密尔的大型 IT 集成商（201–500 人，A.Ş.）**，做 **服务器 / 网络安全 / 备份 / 集成** —— 客户是**企业与公共机构**。**它买的是"数据中心与安全"，不是"PoE 交换机"**，但**它做网络集成 → 有交换机采购权**。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **Proves Bilgi Teknolojileri A.Ş.** |
| 规模 | ⭐ **201–500 人**（B 档里最大的之一） |
| 地址 | **İzmir**：Buca Şirinkapı + Bornova Egemenlik Mah. 6188 Sk. No:51-2G |
| 电话 | **0232 202 42 40** |
| 创始人 | **Serdar Karasu** |
| 业务 | 服务器、网络安全、备份、系统集成、外包 IT |

### 与我方的关系（要清醒）
- ⚠ **它是"企业 IT 集成商"**，交换机采购以** Cisco / HPE / Aruba / Huawei 数据中心级**为主 → **我方现有产品线打不进它的核心**。
- ✅ 但**它有两条缝隙**：
  1. **园区/分支机构 PoE**（它的客户里有大量连锁/分支）→ **非管理 PoE 批量**。
  2. **它做备份/存储 → 有"机柜+布线+接入交换机"的配套单**。
- ⚠ 与 #100（`PROVES / proves.com.tr`）是**同一家**（跨批次重复）。

### 打法
- **不要跟它谈"数据中心交换机"**（必输）。
- 首封给 `0232 202 42 40` 转"网络解决方案部"，主题 **"Şube/kampüs PoE switch — maliyet optimizasyonu"**（分支机构/园区 PoE 降本）。
- 问：**"Şube projelerinde 8/24 port PoE için hangi markayı kullanıyorsunuz?"** —— 如果答案是"TP-Link/Zyxel"，就有戏；如果是"Cisco"，本档归档。

### 证据等级与空白
- 已核实：法定名 A.Ş.、**201–500 人**、伊兹密尔双址、电话、创始人、业务（官网 + LinkedIn + 第三方）。
- 空白：营收、现 PoE 品牌、采购归口。
"""

D['45'] = """
### 一句话
⭐ **Alamthal 是一家"利比亚背景、伊斯坦布尔设点"的通信与科技公司**（`alamthal.ly`，İncirtepe / İstanbul，11–50 人）—— **它的市场在利比亚，不在土耳其**。这意味着：**它是我方通往北非的渠道，不是土耳其本地客户。**

### 主体与坐标
| 项 | 内容 |
|---|---|
| 名称 | **Al-amthal for Communication & Technology**（`alamthal.ly`，`.ly` = **利比亚国别域**） |
| 地址 | **İncirtepe, İstanbul 34510**（土耳其办公室） |
| 规模 | **11–50 人** |
| 关键人物 | **Nayl Alielah（CTO）**、**Khalid Kraizim（General Manager）**、**Mahmoud Alghoul（销售经理，2025 年入职）** |
| 自述 | "advanced technology and telecommunication solutions" |

### 为什么这条信息很值钱
- 土耳其有大量**利比亚/叙利亚/伊拉克背景的贸易公司**，用伊斯坦布尔做**采购与转口枢纽**。
- **`.ly` 域名 + 阿语姓名 + İstanbul 办公室** → 三个信号一致：**它从土耳其采购，卖到利比亚**。
- ⭐ **利比亚正在重建（电力、通信、安防）** → **PoE / 工业交换机是刚需**，且**价格敏感、品牌要求低**（这正是我方的甜区）。

### 打法（与土耳其本地客户完全不同）
1. **先确认清关路径**：**İstanbul → Misrata/Tripoli（海运）**，问 **FOB Istanbul 还是 CIF Misrata**。
2. **产品要求**：**宽压（利比亚电网不稳）、防雷（沙漠雷暴）、耐高温（50 °C+）** → **工业线是主力，商用线是次选**。
3. **不要谈"土耳其本地售后"**（它不需要），要谈 **"备件率 + 换机承诺"**。
4. 首封 **英文**（不是土耳其语），给 CTO **Nayl Alielah** 与 GM **Khalid Kraizim**，主题 **"PoE & industrial switches for Libya projects — FOB Istanbul"**。

### 证据等级与空白
- 已核实：`.ly` 域名、İstanbul İncirtepe 办公点、11–50 人、三位具名高管、行业（通信/IT 服务）（第三方企业库 + 域名）。
- 空白：法定土耳其实体名、利比亚母公司、年采购量、清关方式。
"""

D['46'] = """
### 一句话
⚠ **TBI / Telemobil 与 A 档 `#080 Telemobil` 是同一家**（`tbi.com.tr`）。本档与 `../A/080-telemobil-tbi-com-tr.md` **同源，内容不重复**；按"不合并"原则保留两份文件。**谈的时候只谈一次，别重复发信。**

### 对接口径
- 主体、联系人、切入点**全部以 A 档档案为准**（A 档已有完整分析）。
- 本档只作为**跨批次重复的登记位**存在。
- **实际操作**：把本档标记为"see A/080"，避免两个销售同时发信给同一家公司（**这在土耳其买家眼里非常掉分**）。

### 证据等级与空白
- 已核实：与 A/080 为同一主体（域名 `tbi.com.tr` 一致）。
- 空白：同 A/080。
"""

D['47'] = """
### 一句话
**Pelikan Bilgisayar 是伊斯坦布尔 Mecidiyeköy 的 IT 转售商**（`pelikan.com.tr`），卖 **Aktif Network（路由器/交换机/防火墙/PoE/AP）+ 服务器 + ATEN + 东芝电池**。**它是"企业 IT 采购窗口"，PoE 只是其中一栏。**

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **Pelikan Bilgisayar Hizmetleri İth. İhr.**（进口+出口） |
| 地址 | **Dereboyu Cad. No:60 A.Özkök Apt. D:9-A, Mecidiyeköy / İstanbul** |
| 域名 | `pelikan.com.tr` |
| 代理/主营 | **Aktif Network**（土本土网络品牌）、服务器、**ATEN**（KVM）、Toshiba 电池 |

### 关键判断
- **"Aktif Network" 是土耳其本土品牌** → 它已经在做**本地品牌网络产品** → **对贴牌/本土化品牌零障碍**。
- **İth. İhr.（进口出口）在法定名里** → **它有进口权**，不是纯转售。
- **它卖 ATEN / 电池 / 服务器** → **不是专业网络商**，网络只是品类之一 → **决策快但专业度一般**。

### 与我方的切入点
1. **Aktif Network 的补充位**：它现有 Aktif 的 PoE，我方做**平替或补规格**（Aktif 缺的 2.5G / bt / 工业）。
2. **它的客户是企业/政府** → 需要**授权书 + CE + 土耳其语规格**。
3. **"İth. İhr."** → 可直接谈 **FOB / 信用证**，流程它懂。

### 打法
- 首封给 `info@pelikan.com.tr`，主题 **"Aktif Network tamamlayıcı: 2.5G / 802.3bt PoE"**。
- 问：**"Aktif Network dışında switch tedarik ediyor musunuz?"** —— 若"是"，我方就是第三家；若"否"，我方是第二家。

### 证据等级与空白
- 已核实：法定名（含 İth. İhr.）、Mecidiyeköy 地址、Aktif Network/ATEN/Toshiba 代理、品类（官网 + 企业名录）。
- 空白：成立年、员工数、营收、现 PoE 品牌结构。
"""

D['48'] = """
### 一句话
**Bilge Güvenlik（bilgetech）是安卡拉/伊斯坦布尔双城的"安防 + 弱电"工程型公司**（**2004** 成立，Ataşehir），**Axis / Milestone / Hikvision 授权经销商 + Honeywell 消防/门禁/报警**。**它卖的是"项目"，不是"货"，但项目里每一路摄像机都要 PoE。**

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **Bilge Güvenlik Sistemleri ve Teknoloji A.Ş.** |
| 成立 | **2004** |
| 地址 | **Örnek Mah. Dr. Suphi Ezgi Sok. No:6, Ataşehir / İstanbul** |
| 电话 / 传真 | **+90 216 291 12 12** / 传真 216 291 12 44 |
| 域名 | `bilgetech.com` / `bilgeguvenlik.com` |
| 代理 | ⭐ **Axis（授权经销商）、Milestone（VMS）、Hikvision、Honeywell（消防/门禁/报警）** |

### 关键判断
- **既有 Axis（高端）又有 Hikvision（性价比）** → 它**按项目分层选品**，说明**它有成本意识**（不是只认高端）。
- **Milestone VMS** → 需要**稳定组播与带宽**（和 Rima 一样的技术要求）。
- **它做"project design → implementation"** → **投标级参数是刚需**。

### 与我方的切入点
1. **Hikvision 项目的 PoE**：Hikvision 自己的 PoE 交换机毛利低、型号少 → **我方是"非 Hikvision 牌"的合理替代**（很多工程商刻意避开同品牌配套）。
2. **Axis 项目** 不碰（Axis 项目通常指定 Axis/Moxa 网络）。
3. **Honeywell 消防/门禁** → **门禁控制器也是 PoE** → 一并覆盖。

### 打法
- 首封给 `info@bilgetech.com`（+ `bilgeguvenlik.com`），主题 **"Hikvision projelerinde PoE switch alternatifi"**。
- **明确说"我们不碰 Axis 项目"** —— 让它在自己的分层里给你位置，比"我们全能"有效得多。
- 问：**"Hikvision tarafında PoE switch'i siz mi veriyorsunuz?"**

### 证据等级与空白
- 已核实：法定名 A.Ş.、**2004 成立**、Ataşehir 地址、电话传真、**Axis 授权经销商 + Milestone + Hikvision + Honeywell**（官网英文页 + 品牌页 + 第三方）。
- 空白：员工数、营收、年项目量、现 PoE 品牌。
"""

D['49'] = """
### 一句话
**Zeytek 是"机柜与布线基础设施"商**（**2019** 成立，İstanbul），主品是**机柜（含户外/防弹级 saha kabini、Mobese 柜）+ 光纤配线 + 环境监控**。**它和 HCS/Lansan 是同一生态位，但更偏"户外/市政"**。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **Zeytek Bilişim ve Teknoloji Ürünleri San. Tic. Ltd. Şti.** |
| 成立 | **2019**（团队自称 15 年行业经验） |
| 地址 | İstanbul |
| 关键人 | **Mehmet Zeytinli（Genel Koordinatör / 总经理）**；此前在 Gunko Endüstriyel、Asrack Kabinet、Dat Telekom、**Legrand** |
| 域名 | `zeytek.com.tr` |

### 品类（决定切入点）
| 产品 | 说明 |
|---|---|
| Dikili / Duvar tipi / Server rack kabinet | 标准机柜 |
| ⭐ **IP Korumalı Saha Kabinleri** | **户外防护机柜** |
| ⭐ **Mobese Kabinleri** | **MOBESE = 土耳其警方城市监控系统** → 市政/警用项目 |
| Fiber optik patch panel、IP55 空调柜 | 光纤与温控 |
| **Ortam izleme cihazları** | 环境监控（温湿度/门磁/水浸） |
| **Network Cihazları** | ⭐ **"网络设备"在它的品类里** |
| Kamera direkleri | 监控杆 |

### 与我方的切入点
1. ⭐ **关键人物背景是 Legrand + Asrack（机柜）+ Dat Telekom（网络）** → **它懂网络设备，也懂机柜** → 谈"机柜里的交换机"它完全接得住。
2. **MOBESE 柜 = 警用/市政项目** → **柜内交换机必须有"项目准入"资质**（CE + 土耳其语文件 + 长期供货承诺）→ **谁供货稳，谁就绑住项目**。
3. **它有"Network Cihazları"分类但没有品牌** → **这就是我方的位置**。

### 打法
- 首封给 `info@zeytek.com.tr`，**点名 Mehmet Zeytinli**，主题 **"MOBESE / saha kabinleri içi switch tedariki"**（柜内交换机）。
- 一句话：**"你们做柜子，我们填空——柜子里的 PoE。"**
- **提 Legrand**：*"Legrand geçmişinizi gördük"* → 立刻建立专业对等感。

### 证据等级与空白
- 已核实：法定名、2019 成立、**Mehmet Zeytinli 及其履历（Legrand/Asrack/Gunko/Dat Telekom）**、品类全表含 Mobese 柜（官网 + 第三方）。
- 空白：员工数、营收、是否已卖过交换机。
"""

D['50'] = """
### 一句话
**Foline 是"数据中心 + 弱电 + 结构化布线"的工程/咨询服务商**（İstanbul Kağıthane），**合作方是 Siemens / Viko / Panduit(PAVA?) / CommScope**。**它是设计方与施工方，不是分销商** → 它影响规格，但不一定自己采购。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **FOLİNE BİLİŞİM TEKNOLOJİLERİ SAN. VE TİC. LTD. ŞTİ.** |
| 地址（销售办） | **Premier Kampüs, İmrahor Cd. No:29, B Blok Kat:3/302, Kağıthane / İstanbul** |
| 电话 / 邮箱 | **0212 535 00 33** / `info@foline.com.tr` |
| 能力 | **Veri merkezi / Konteyner veri merkezi / Zayıf akım / Yapısal kablolama** 的 **mühendislik + danışmanlık + uygulama** |
| 合作方 | **Siemens、Viko、PAVA（Panduit 系）、CommScope**（官网"çözüm ortakları"页，48 条记录） |

### 关键判断
- **它的价值链位置是"设计 + 施工"** → **它写规格书（şartname）**。
- ⭐ **能写规格书 = 能"指定品牌"** → 若我方进入它的"解决方案伙伴"名单，**它会在项目里指定我方**（这是 B 档里最高杠杆的一种关系，比卖货值钱）。
- ⚠ 但反过来：**它不会大量囤货**，单次采购量小、按项目走。

### 与我方的切入点
1. **目标不是"卖给它"，是"进它的 şartname（招标规格）"** → 谈法：给它 **土耳其语规格模板 + 兼容性声明 + 参考项目**，让它写进方案。
2. **它做 konteyner veri merkezi（集装箱数据中心）** → 里面必配**工业级/宽温交换机** → 这是最具体的抓手。
3. **它跟 Siemens/CommScope 合作** → **对品质敏感、对价格不敏感** → 报"可靠性"，不报"最低价"。

### 打法
- 首封给 `info@foline.com.tr`，主题 **"Konteyner veri merkezi için endüstriyel switch — şartname desteği"**（为集装箱 DC 提供工业交换机 + 规格支持）。
- 附一份 **土耳其语"可写入 şartname 的规格条款"** —— 这是我方能给、别人不给的东西。
- 问：**"Konteyner DC projelerinde switch'i siz mi seçiyorsunuz?"**

### 证据等级与空白
- 已核实：法定名、Kağıthane 销售办地址、电话、四项能力、四个合作方（官网多页）。
- 空白：成立年、员工数、营收、是否自行采购设备。
"""

D['51'] = """
### 一句话
⚠ **Nazemco 与 #126 是同一家**（`Nazemco İth. İhr. San. Tic. Ltd. Şti.`），本档为跨批次重复登记，**内容以 #126 为准，不重复写**。

### 已核实的少量信息
| 项 | 内容 |
|---|---|
| 法定名 | **Nazemco İthalat İhracat Sanayi Ticaret Ltd. Şti.** |
| 业务 | **进口 + 出口（İth. İhr. 在法定名里）** |
| 公开面 | 极薄：无实质官网、无 LinkedIn、无产品目录 |

### 处理建议
1. **不合并文件**（#51 与 #126 各保留一份、互相标注）。
2. **只联系一次**（避免同一家收到两封不同销售的信）。
3. 若它确实是"纯进出口商"（无技术团队）→ **它的价值是"清关与转口"**，不是"卖设备" → 适合做**利比亚/伊拉克/叙利亚方向的转口渠道**（和 #45 Alamthal 同类）。

### 证据等级与空白
- 已核实：法定名、进口出口属性、公开面极薄。
- 空白：地址、规模、实际品类、决策人（**基本全部缺失**）。
"""

D['55'] = """
### 一句话
⭐ **ULAK Haberleşme A.Ş. 是土耳其的国家级电信设备商——"土耳其第一台国产 4.5G 基站"的研制方**，由**国防工业局（SSB）持股、Aselsan 主导**，做 **4.5G/5G 基站、关键通信、公共安全网络、无人机载基站**。⚠ **它不是分销商，它是我方的"同行/上游"**——但**它是我方在土耳其最值得建立"技术关系"的一家**。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **ULAK Haberleşme A.Ş.** |
| 性质 | ⭐ **Cumhurbaşkanlığı Savunma Sanayii Başkanlığı（SSB）iştiraki**（总统府国防工业局参股）；**Aselsan 为主承包商** |
| 业务 | **国产 4.5G / 5G 基站（baz istasyonu）**、无线接入网、**kamu güvenliği（公共安全）**、关键基础设施通信、**无人机载基站（ANKA/Aksungur 集成）** |
| 合作 | **Netaş**（2025-07 签战略合作：无线接入网 + 国防通信） |
| 场景 | 灾害应急（2023 地震中 45 人团队带 4.5G 基站进场）、国防、运营商 |
| 域名 | `ulakhaberlesme.com.tr` |

### 与我方的真实关系（必须讲清楚，不能吹）
- ❌ **不要把它当"客户"去打**。它是**国家级设备商**，供应链是**国产化导向 + Aselsan 体系**，**不会买中国白牌交换机做基站**。
- ✅ **三条真实可行路径**：
  1. **配套外设**：它的基站/应急通信车需要 **工业 PoE 交换机（给摄像头/传感器/微波回传设备供电）** —— **非核心件可以外采**，这是唯一有实质可能的缝隙。
  2. **应急/灾害场景**：它的"应急通信车"是**整车集成** → **车内的网络交换**可以外购。
  3. **情报价值**：它是**土耳其国产化的风向标** → 跟踪它的动作 = 预判土耳其"进口替代"政策走向（会影响我方整条土耳其策略）。
- ⚠ **它在 B 档是合理的**（不是采购客户），但**不该占销售时间**，该占"市场情报"时间。

### 打法（若一定要接触）
- **走技术/展会路线，不走销售路线**：**SAHA EXPO（国防展）、Mobile World Congress** 是它的场子。
- 首封给 `info@ulakhaberlesme.com.tr`，**英文**，主题 **"Industrial PoE switch for emergency comms vehicles — component supply"**（明确写"部件供应"，不写"整机方案"）。
- **绝不要提"我们可以做基站"**（会立刻被归档）。

### 证据等级与空白
- 已核实：法定名 A.Ş.、**SSB 参股 + Aselsan 主承包**、**国产 4.5G 基站**、**Netaş 2025-07 战略合作**、ANKA 无人机载基站测试、2023 地震应急部署（官方站 + 国防媒体 + 航空媒体三处）。
- 空白：采购制度、是否有非国产外购比例、供应商准入流程。
"""

D['57'] = """
### B 档补充（本家已有完整深度档案）
- 完整研究见 **`../B/057-filiz-guvenlik-sistemleri-proje-ins-san-tic-ltd.md` 的「附：完整研究档案」**：`filizguvenlik.com.tr` 逐字核实、**Hikvision + Dahua 双代理**、伊斯坦布尔工程商、`info@` 与具名邮箱。
- **B 档视角补一句**：它是**双代理（Hikvision + Dahua）** → 说明它**刻意不做单品牌绑定** → **对新品牌的心理门槛低**。落 B 的原因是"没有接触记录 + 规模不明"。
- **建议**：**优先打**，切入口 = **"双代理说明你在做价格分层，那第三层（经济款）要不要？"**

### 与 #56（Optima）的分工提醒
- 同属"安防工程商"，但 **Optima 有 $35/120 W 价格锚（要求极致低价）**，**Filiz 是双代理（可谈分层）** → **两家话术不能一样**。
"""

D['60'] = """
### 一句话
⭐ **GMT Control（GMTCNT）是"土耳其第一家国产 PLC 制造商"**（**2014** 成立，Beykoz / İstanbul，**51–200 人**），自有品牌 **GMTCNT**，产品线含 **PLC / HMI / AC Drive / 伺服 / 步进 / 工业通信**。**它不是交换机买家，它是我方的"工业通信互补方"**。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **GMT Endüstriyel Elektronik Sanayi ve Ticaret A.Ş.**（品牌 **GMTCNT**） |
| 成立 | **2014**（团队 30+ 年工业控制经验） |
| 规模 | **51–200 人** |
| 地址 | **Beykoz / İstanbul** |
| 域名 | `gmtcontrol.com` / `en.gmtcontrol.com` |
| 自述 | "**Türkiye'nin ilk yerli PLC üreticisi**"（土耳其第一家国产 PLC 制造商）、**100% 本土研发** |

### 产品线（逐条）
**PLC（GLC-396R/T、GLC-496R/T 等）· HMI 操作面板 · AC 变频器 · 伺服电机与驱动器 · 步进电机与驱动器 · 电源（SMPS）· 工业通信产品（含无线 RF）**。

### 关键矛盾点（也是我方的机会）
- ⚠ **它自称"工业通信产品"里有"kablosuz RF çalışabilen ürünler"（可无线 RF 工作的产品）**，但**没有以太网交换机**。
- ⭐ **一个做 PLC/HMI/变频器的公司，客户一定会问"交换机呢？"** → **它现在大概率是"让客户自己配"或"从别处搭售"**。
- ✅ → **我方做它的"配套交换机"（配 GMTCNT 品牌的工业 PoE / DIN 导rail 交换机）= 它补完产品线，我方拿到它的渠道**。这是**最干净的互补**，不抢它任何生意。

### 与我方的切入点
1. **DIN 导rail 工业交换机（5/8 口）** 是它的天然配套（PLC 柜内）。
2. **它的客户是机器制造商（makine imalatçısı）** → 需要**同一柜内的网络**（PLC ↔ HMI ↔ 相机/扫码枪）。
3. **它强调"国产"** → ⚠ 贴牌会伤它的品牌叙事 → **谈法要避开"国产"二字，走"配套件（aksesuar/tamamlayıcı ürün）"定位**，不要说"我们的交换机可以替代你们的"。

### 打法
- 首封给 `info@gmtcontrol.com`，主题 **"PLC panoları için DIN-ray endüstriyel switch — tamamlayıcı ürün"**（补充品，不是替代品）。
- **不要说"我们更便宜"**（它卖的是"国产自主"故事，价格不是它的卖点）。
- 问：**"Panolarınızda Ethernet switch'i müşteri mi tedarik ediyor?"**

### 证据等级与空白
- 已核实：品牌/法定实体、**2014 成立**、**51–200 人**、Beykoz、**"土耳其第一家国产 PLC"自述**、完整产品线、100% 本土研发（英/土官网 + LinkedIn 三处）。
- 空白：营收、是否有交换机外购计划、决策人。
"""

D['62'] = """
### 一句话
⭐ **Cebeci Grup 自己在卖"自有型号的 L3 网管交换机"**（`cebecigrup.com` 上有 **`S5700-24G-4TFR` / `S5700-24G-4FR`** 这类产品页），法人是 **Cebeci Teleteks San. ve Tic. Ltd. Şti.**，**同时做电商（magaza.cebecigrup.com）**。**这是 B 档里"已经在卖交换机"的铁证之一。**

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **Cebeci Teleteks San. ve Tic. Ltd. Şti.**（集团名 **Cebeci Grup**） |
| 站点 | `cebecigrup.com`（企业站）+ **`magaza.cebecigrup.com`（电商）** |
| 在售交换机 | ⭐ **`S5700-24G-4FR`（24×GE + 4×GE SFP，L3 网管）**、**`S5700-24G-4TFR`（24×GE + 4×10G SFP+，L3 网管）** |
| 规格要点 | 静态/动态 MAC 表、**ACL（L2/L3/L4）**、**802.1X**、**DHCP Snooping**、**ARP 防护、DoS 防护**、**SNMP v1/v2/v3**、**RMON**、**LLDP**、**IPv6（Ping/Tracert/Telnet/SSH/SSL）**、**最多 32 个聚合组**、**QoS 重标记** |

### 为什么这条证据很硬
- **`S5700` 是"深圳通用型号族"**（多个中国厂共用），且页面 **通篇只有规格、没有品牌名** → **几乎可以确定是白牌贴 Cebeci 的牌**。
- 它同时做 **B2C 电商（magaza）** → **有零售出口，也有项目出口** → **双通道**。
- **L3 + 10G 上联** 已在其产品线 → 说明它**已经在做中高端**（不是只卖 8 口）。

### 与我方的切入点
1. ⭐ **直接对位 `S5700-24G-4TFR`（24×GE + 4×10G，L3）** —— 我方有现成对位型号，**用它自己的页面做对位表**。
2. **它的空白**：**2.5G**、**802.3bt（90 W）**、**工业宽温** —— 这三档它的 `S5700` 都没有。
3. **电商站 = 需要"现货 + 小批量"** → 我方若能给**土耳其寄售小库存**，它的电商就活了。

### 打法
- 首封给 `cebecigrup.com` 表单 + `magaza` 客服，主题 **"S5700-24G-4TFR muadili + 2.5G/bt 补位"**（同规格 + 补位）。
- **附对位表**（`S5700-24G-4FR` / `4TFR` 逐行对位）。
- 问：**"S5700 serisi sizin markanız mı, yoksa tedarikçinin mi?"** —— 定生死的一问。

### 证据等级与空白
- 已核实：法人名、**在售 S5700 系列的完整规格**、双站（企业站 + 电商）（官网产品页逐条）。
- 空白：成立年、规模、营收、S5700 的品牌归属、现工厂。
"""

D['63'] = """
### 一句话
⭐ **Areskom 是"工业通信"的专业分销商**（`areskom.com.tr`），代理/分销 **Belden、Westermo、Moxa、Advantech、Tektelic、Hirschmann** 这类工业网络品牌，做**能源/智能电网/铁路/海事/油气/数据中心**。**它是我方工业交换机在土耳其"最像对手"的一家**——也正因为如此，**它是"二供/平替"最有说服力的对话对象**。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 名称 | **Areskom İletişim Ltd.**（`areskom.com.tr`） |
| 定位 | **工业通信 / 工业 IT / 工业网络安全 的分销与集成** |
| 行业覆盖 | **能源与智能电网、工厂与过程自动化、造船与海事、油气与石化、铁路与列车自动化、电信与数据中心、摄像头/安防/智能楼宇** |
| 技术面 | **工业以太网、以太网延伸（Ethernet extender）、光纤、Westermo WeOS/WeConfig/WeConnect、LoRaWAN（Tektelic KONA）、过程自动化（Ethernet/Modbus/Profibus I/O、4–20 mA 隔离器）、M2M/远程访问** |

### 我从官网读到的最关键一句
- 它在"能源与智能电网"页把 **"Bilgi / İnternet Güvenliği (Cyber Security)"** 写成**与供电同等重要的判据**，并列了 **"Endüstriyel Siber Güvenlik / Edge Network / Etherneti Uzatma / Fiber"**。
  → ⭐ **它卖的是"关键基础设施的可靠性 + 网络安全"**，不是"便宜"。

### 与我方的真实定位（要诚实）
- ⚠ **它是 Westermo / Moxa 级别产品的分销商** → **我方在"认证、固件、环网自愈时间"上大概率不如**。
- ✅ **但有三个真实缝隙**：
  1. **价格层**：Westermo/Moxa 在土耳其很贵 → **中低端项目（园区、楼宇、小型电站）用不起** → 我方补这一层。
  2. **交期**：欧洲品牌交期动辄 8–16 周 → **我方 4 周内可交** → 抢"急单"。
  3. **Ethernet extender / 长距 PoE**：这是它的品类之一，**我方 250 m 长距 PoE 有价格优势**。
- ⚠ **绝对不要在首封说"我们可以替代 Westermo"** —— 会立刻被拉黑。

### 打法
- 首封给 `info@areskom.com.tr`，主题 **"Uygun maliyetli alternatif: edge/şube seviyesinde endüstriyel switch"**（边缘/分支层级的性价比替代）。
- 明确画边界：**"核心环网我们不做，边缘接入我们做"** —— 这句话是拿到回复的关键。
- 问：**"Müşterilerinizde fiyat baskısı olan projeler var mı?"**

### 证据等级与空白
- 已核实：定位、七大行业覆盖、**Westermo WeOS / Tektelic KONA / LoRaWAN / Modbus-Profibus I/O** 等技术栈（官网行业页与品牌页逐条）。
- 空白：法定全名与成立年、员工数、营收、具体代理权限（独家/非独家）。
"""

D['64'] = """
### 一句话
**İntenet 是 1993 年成立的电信基础设施集成商**（`intenet.com.tr`，Esenler / İstanbul），**1996 年把 TDM 引进土耳其**，做过 **VEDOP（税务所自动化）、Sütaş WAN、财政部项目**，是 **AT&T 在土耳其的方案提供方**，现在主攻 **电厂/变电站通信（TEİAŞ OPGW、PLC、RTU）**。**它是"广域网/骨干"玩家，不是"接入"玩家。**

### 主体与坐标
| 项 | 内容 |
|---|---|
| 名称 | **İntenet İnternet, Telekomünikasyon, Network ve Bilişim Sistemleri**（INTENET） |
| 成立 | **1993** |
| 地址 | **Oruç Reis Mah. Giyiknet Sitesi 2. Sok. No:56, Esenler / İstanbul** |
| 电话 / 邮箱 | **0 212 347 84 84** / `info@intenet.com.tr` |
| 里程碑 | **1996** 引进 TDM（土耳其首批）；**1997–2000** 分销 TDM；**2000 后** 转型系统集成（Cisco WAN/LAN） |
| 代表项目 | **VEDOP（税务所自动化）、Sütaş WAN、财政部项目、Şekerbank WAN（Newbridge）**；银行 WAN 市场自述 **60% 份额** |
| 合作伙伴 | **AT&T（土耳其方案提供方）、T-Systems、IBM、Koçnet、Borusan Telekom、Vodafone、Türknet** |
| 现方向 | **电厂/变电站通信**：TEİAŞ OPGW、PAX、PLC、RTU 通信、专线供货与调试 |

### 与我方的真实关系
- ⚠ **它的核心是 WAN/骨干/电力通信**，采购的是**运营商级设备**（Cisco、Newbridge、传输设备），**不是我方 8/24 口 PoE**。
- ✅ **唯一真实缝隙：变电站/电厂的"站内接入"** —— RTU、摄像头、门禁、环境监控都要 PoE，而**站内网络通常是"最后一公里"没人管**。
- ✅ 它做**交钥匙（turn-key）+ 7/24 维护 + 次日换机保证** → **它对供应链的"备件承诺"要求极高**，这正是我方可以承诺的（换机而不是维修）。

### 打法
- 首封给 `info@intenet.com.tr`，主题 **"Trafo/şalt sahası içi PoE switch — yedek parça garantisi"**（站内 PoE + 备件保证）。
- 一句话：**"骨干你们强，站内接入我们补。"**
- 问：**"Santral projelerinde saha içi network'ü kim tedarik ediyor?"**

### 证据等级与空白
- 已核实：**1993 成立**、Esenler 地址、电话、**1996 引进 TDM**、VEDOP/Sütaş/财政部/Şekerbank 项目、**AT&T 土耳其方案方**、银行 WAN 60% 自述、现方向为电力通信（官网英/土两版一致）。
- 空白：员工数、营收、现 PoE 采购情况、决策人。
"""

D['65'] = """
### 一句话
**Teamon 是安卡拉的"系统集成商"**（`teamon.com.tr`，Emek / Ankara），**经销全球品牌 + 做设计安装维护**，站点还提供 **EAN 查询 / 条码查询 / 网络工具 / 免费"网络+"培训** → **它有技术内容运营的意识**，在安卡拉的中小 SI 里算"专业型"。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 名称 | **Teamon İletişim Teknolojileri** |
| 地址 | **Emek Mah. Bişkek Caddesi 8. Cadde No:32/4, Emek / Ankara** |
| 电话 / 邮箱 | **+90 312 806 35 29** / `info@teamon.com.tr` |
| 定位 | **sistem entegratörü（系统集成商）**，做"sektör bağımsız anahtar teslim çözümler"（行业无关的交钥匙方案） |
| 站点特色 | **EAN Arama、Barkod Arama、Ağ Araçları、Ağ+ Eğitimleri（免费网络培训）** |

### 与我方的切入点
1. **它在安卡拉 = 政府项目中心** → **公共采购（kamu ihalesi）**是它的主战场 → 需要**授权书 + CE + 土耳其语文件**。
2. ⭐ **它办免费"网络+培训"** → 说明它**愿意投入技术内容** → **我方可以提供"培训素材 + 认证"**，让它把我们的产品讲进课里（这是极低成本的长尾营销）。
3. **它是 SI，不是分销** → **按项目采购、不压库存** → 需要"按项目报价 + 允许分批发货"。

### 打法
- 首封给 `info@teamon.com.tr`，主题 **"Kamu projeleri için PoE switch + eğitim materyali desteği"**（项目 + 培训素材）。
- **主动提出"给你们 Ağ+ 培训提供交换机样机与教材"** —— 这个提议它几乎没有理由拒绝，而且**一次性把我方塞进它的技术体系**。
- 问：**"Kamu ihalelerinde switch tarafında hangi markayı kullanıyorsunuz?"**

### 证据等级与空白
- 已核实：地址、电话、邮箱、SI 定位、**站点四个工具/培训功能**（官网逐条）。
- 空白：法定名、成立年、员工数、营收、现交换机品牌。
"""

D['66'] = """
### 一句话
**İnovatech（İnovatech Güvenlik ve Bilgisayar Sistemleri Dış Ticaret Ltd. Şti.）是 Şişli Perpa 片区的"安防 + 网络"工程商**，**2014-08-21 注册**，做 **IP 摄像机 / 报警 / 消防 / 门禁 / PDKS / 网络与光纤** 的**勘察→设计→安装→调试**全流程。**典型的中型工程商。**

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **İnovatech Güvenlik ve Bilgisayar Sistemleri Dış Ticaret Ltd. Şti.** |
| 注册 | ⭐ **2014-08-21** |
| 地址 | **Halil Rıfat Paşa Mah. Yüzer Havuz Sok. A Blok Kat:8 No:789, Şişli / İstanbul 34379**（Perpa 片区） |
| 电话 / 邮箱 | **(0212) 220 38 34** / `info@inovatech.com.tr` |
| 行业分类 | **Security Systems Services**（EMIS） |
| 服务 | **keşif（勘察）→ projelendirme（设计）→ kurulum（安装）→ devreye alma（调试）** |

### 与我方的切入点
1. **"Dış Ticaret" 在法定名里** → **它有进出口权** → 可直接谈进口，不需要第三方。
2. **Perpa 片区 + 2014 成立** → 中型、稳定、**供应商已固化但未绑定**。
3. **它做"网络与光纤"** → **交换机是它的在售品类**（不是空白）→ 谈**二供/降本**。

### 打法
- 首封给 `info@inovatech.com.tr`，主题 **"IP kamera projeleri için PoE switch — ikinci kaynak"**。
- 问：**"PoE switch'i ithal mi ediyorsunuz yoksa yerelden mi alıyorsunuz?"** —— 有"Dış Ticaret"资质的问题，它一定会答。

### 证据等级与空白
- 已核实：法定名、**2014-08-21 注册**、Perpa 具体门牌、电话邮箱、服务流程、行业分类（官网 + EMIS 企业库）。
- 空白：员工数、营收、现 PoE 品牌。
"""

D['67'] = """
### 一句话
**Metcom Güvenlik Teknolojileri A.Ş. 是"车牌识别（LPR）与交通/卡口系统"的专业商**（`metcom.com.tr`），自研 **MTC-500 高速公路车牌识别系统**、**MTC 计数/测温/口罩检测系统**、**XVR** 等，也做 **Hytera PoC 对讲**。**它是 ISAF 展商，产品带"自有型号"——技术型公司。**

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **METCOM GÜVENLİK TEKNOLOJİLERİ A.Ş.** |
| 站点 | `metcom.com.tr` |
| 展会 | **ISAF 展商**（`isaffuari.com` 2022 展商名录有 "metcom"） |
| 自研 | ⭐ **MTC-500 高速公路车牌识别（Plaka Tanıma）**、**Kişi Sayma Sistemi（计数/测温/口罩）**、**XVR（5-in-1 HDCVI/TVI/AHD/IP/Analog）** |
| 其他 | **Araç Takip（GPS 车队管理）**、**Hytera PNC360S PoC 对讲** |

### 与我方的切入点
1. ⭐ **LPR/卡口 = 每套系统都要"户外 PoE + 防雷 + 宽温"**：卡口摄像机装在杆上，**雷击与温差是头号杀手** → **工业 PoE 是刚需，不是可选**。
2. **它自研系统** → 它**指定硬件规格**（"我们系统里配什么交换机"由它决定）→ **进它的 BOM 比进经销商货架更值钱**。
3. **它做高速公路（otoyol）** → **国家级项目** → 需要**长期供货与备件承诺**（10 年+ 项目周期）。

### 打法
- 首封给 `metcom.com.tr` 表单 + `info@`，主题 **"Otoyol/plaka tanıma sistemleri için saha PoE switch（IP66 / 6kV / −40~75°C）"**。
- 一句话：**"你的 MTC-500 装在杆上，杆上的交换机是最容易坏的那一环。"**
- 问：**"MTC-500 projelerinde saha switch'ini siz mi veriyorsunuz?"**

### 证据等级与空白
- 已核实：法定名 A.Ş.、**MTC-500 自研系统**、计数系统、XVR、Hytera PoC、ISAF 展商身份（官网 + ISAF 名录）。
- 空白：成立年、员工数、营收、现 PoE 品牌、采购归口。
"""

D['68'] = """
### 一句话
**Egemen Elektronik 是 Ümraniye 的 CCTV/报警分销商**（**2013-07-25** 注册，约 **10 人**），**2023 年营收增长 +201.3%、总资产 +218.9%**（第三方财务）—— **B 档里增速数据最猛的一家**。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **Egemen Elektronik Güvenlik Bilgisayar Sistemleri San. ve Tic. Ltd. Şti.** |
| 注册 | ⭐ **2013-07-25** |
| 地址 | **Ihlamurkuyu Mah. Malazgirt Cad. Şendal Sok. No:1, Ümraniye / İstanbul 34771** |
| 电话 / 邮箱 | **+90 216 611 61 00** / `satis@egemenelektronik.com` |
| 规模 | 约 **10 人**（EMIS 2025） |
| ⭐ 财务 | **2023 净销售 +201.3%**、**总资产 +218.91%**（EMIS） |
| 业务分类 | 电气设备/布线材料批发（DNB）；第三方归为 CCTV/报警分销商 |

### 与我方的切入点
1. ⭐ **+201% 增长 + 只有 10 人** = **极轻资产、极快周转** → 它靠"价格 + 现货"赢 → **需要能随时补货的工厂**。
2. ⚠ **10 人公司现金流脆弱** → **账期必须严控**（建议预付或小额短账期）。
3. **Ümraniye = 伊斯坦布尔安纳托利亚侧的批发带**（Dudullu/İMES 附近）→ 它的客户是**安装商与小零售商**。

### 打法
- 首封给 **`satis@egemenelektronik.com`**（销售邮箱，说明它把销售邮箱公开 → 有效），主题 **"Hızlı tedarik: 8/16/24 port PoE switch"**。
- 主打 **"现货 + 短交期"**（它增长靠这个）。
- 问：**"Aylık ortalama kaç adet PoE switch satıyorsunuz?"** —— 10 人公司也会答，且答案能直接算出年量。

### 证据等级与空白
- 已核实：法定名、**2013-07-25 注册**、Ümraniye 地址、电话与销售邮箱、**约 10 人**、**2023 财务增速（+201.3% / +218.9%）**（DNB + EMIS + Crunchbase 三处）。
- 空白：营收绝对值、现 PoE 供应商、老板姓名。
"""

D['69'] = """
### 一句话
**Teknolojipazar 是安塔利亚的"IT/办公/安全/网络"电商**（**2010**，Muratpaşa / Antalya，11–50 人），法人 **Teknolojipazar Bilişim Yazılım ve Elektronik Tic. Ltd. Şti.**。**它是 B2C/B2B 线上零售，不是项目商。**

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **Teknolojipazar Bilişim Yazılım ve Elektronik Tic. Ltd. Şti.** |
| 成立 | **2010**（创始人 **Cemile Sağlam**） |
| 地址 | **Muratpaşa / Antalya** |
| 电话 / 邮箱 | **+90 850 888 8797** / `info@teknolojipazar.com` |
| 规模 | 11–50 人 / **<$5M**（第三方） |
| 品类 | 电脑与配件、打印机、**安全（güvenlik）**、**网络（network）**、游戏 |

### 与我方的切入点
1. **电商 = 需要"现货 + 单品毛利 + 图片/参数素材"** → 我方要提供的不是"方案"，是**土耳其语详情页素材 + 稳定现货**。
2. **它在安塔利亚** → 与 #35 Antalya Turkuaz 同城 → **两家可能互相拿货**（小心：不要给两家不同价格，会被发现）。
3. ⚠ **<$5M 的电商，单品价格敏感** → **只推 8/16 口经济款**，别推工业。

### 打法
- 首封给 `info@teknolojipazar.com`，主题 **"PoE switch — stok + Türkçe ürün içeriği desteği"**（现货 + 土耳其语内容支持）。
- 提供**现成的产品图 / 参数表 / 土耳其语描述**（这是电商最缺的）。
- 问：**"PoE switch kategorisinde en çok hangi port sayısı satılıyor?"** —— 直接拿到选品答案。

### 证据等级与空白
- 已核实：法定名、**2010 成立 + 创始人**、Muratpaşa、11–50 人、电话邮箱、品类（Tracxn + Crunchbase + ZoomInfo 三处）。
- 空白：营收绝对值、现 PoE 品牌、是否愿做自有品牌。
"""

D['70'] = """
### 一句话
⚠ **TekmarShop / Tekmar 在检索中撞到两个不同主体**：① **`teknomarketshop.com`**（Bahçelievler / İstanbul 的小电商，卖车载 4K 摄像头套装，WhatsApp 543 110 4043）；② 布尔萨的相机店（Yıldırım / Bursa，0224 364 18 88 —— ⚠ **这个电话是 #38 Fourline 的**）。**本档主体无法唯一确认。**

### 检索实况
| 角度 | 结果 |
|---|---|
| `Tekmar` / `TekmarShop` | 命中 `teknomarketshop.com`（Bahçelievler 小电商，与"Bursa/Yıldırım"不符） |
| 布尔萨方向 | 命中的电话 **0224 364 18 88 是 Fourline（#38）** → **可能是同一家换了招牌，也可能只是电话记错** |
| 企业名录 | 无唯一命中 |

### 处理建议
1. ⚠ **先核名**：问 "Tekmar ile Fourline aynı şirket mi?"（若同 → 合并处理但**文件仍不合并**）
2. 若确认是 `teknomarketshop.com` 这类小电商 → **降 C**（量太小、品类偏车载）
3. 若是布尔萨实体 → 按 #38 Fourline 的方式打（同一区域、同一场景）

### 证据等级与空白
- 已核实：`teknomarketshop.com` 的存在与其地址/联系方式。
- 空白：**与 111 记录的对应关系 —— 全部未知。**
"""

D['71'] = """
### 一句话
**Baburtech 是安卡拉的"笔电配件 + 深度维修"公司**（**2007** 成立，`baburtech.com`，**5,000 m² 维修车间**），卖**原厂笔电备件**并做**主板级维修**。⚠ **它与弱电/PoE 无关** → **本档大概率是名单错项，建议降 C。**

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **BABURTECH BİLİŞİM A.Ş.**（A.Ş.，税号 1280857312，Çankaya 税务局） |
| 成立 | **2007**（第三方）；约 **8 人** |
| 地址 | 总部仓：**Ziya Gökalp Cad. No:9, Kızılay / Ankara**；技术服务中心：**Necatibey Cad. No:51, Çankaya / Ankara** |
| 电话 | **0850 302 06 47** / **+90 312 230 53 05** |
| 主营 | **原厂笔电备件（orijinal laptop yedek parça）** + **主板级维修（5,000 m²）**：主板、CPU/芯片组更换、引脚修复、电源电路、进液修复 |
| 客户 | **全国经销商（bayi）** |

### 为什么它不该留在我方名单里
- 它的客户是**维修店和经销商**，产品是**笔电零件**，**没有网络/安防品类**。
- ⚠ 强行推 PoE 只会消耗双方时间 → **建议降 C（品类不符）**，并在 B 档索引里写明理由。

### 与我方的唯一交集（若有）
- 它做**技术服务中心**（5,000 m²）→ 若我方在土耳其需要**本地维修/翻新伙伴**（RMA 处理），**它是有能力的候选**（虽然品类不同，但主板级维修能力是真的）。

### 证据等级与空白
- 已核实：A.Ş.、税号、双地址、两个电话、**5,000 m² 维修车间**、原厂备件定位（官网 + RocketReach + 本地名录）。
- 空白：营收、是否曾涉足网络品类。
"""

D['73'] = """
### 一句话
**"Kiracı Bilişim" 的真实身份是 Kıraç Group 的 IT 公司（Kıraç Bilişim，2005），品牌叫 ZKR，做"医院护理呼叫系统（nurse call）"**，总部 **Çankaya / Ankara**，11–50 人。**它是我方"医院/医疗弱电"的入口**——但**它要的是"医疗级集成"，不是交换机**。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 集团 | **Kıraç Group**（**1982** 起做制造） |
| 公司 | **Kıraç Bilgi ve İletişim Teknolojileri San. ve Tic. A.Ş.**（**2005** 成立，进弱电与 IT） |
| 品牌 | ⭐ **ZKR**（**2011** 注册） |
| 地址 | **Ümit Mah. Okullar Sok. No:16, Ümitköy / Çankaya, 06810 Ankara** |
| 电话 / 传真 | **+90 312 446 03 44** / 446 03 34 |
| 邮箱 / 站点 | `info@zkr.com.tr` / `zkr.com.tr` |
| 规模 | **11–50 人** |
| 产品 | **IP 护理呼叫系统**：触摸屏房间控制器（内置 Mifare 读卡）、床旁呼叫单元、患者手柄、拉绳呼叫、门灯；**Code Blue 急救呼叫**；对讲；与 **HIS（医院信息系统）集成**、DECT/寻呼机/Android 集成 |
| 业绩 | 自述 **700+ 套系统 / 3,000 万+ 患者服务**（全球） |

### 与我方的切入点（要选对层）
- ⚠ **它的核心是"IP 护理呼叫"**，卖的是**软件 + 医疗流程**，不是网络。
- ✅ **但它每套系统都是一张"医院 IP 网络"**：**房间控制器、床旁终端、门灯全是 PoE**，**一个 500 床医院 = 上千个 PoE 口**。
- ✅ **它的痛点**：医院网络要求 **PoE 长距（走廊 >100 m）、不间断供电、静音（无风扇）** → **我方长距 PoE + 无风扇机型直接对口**。
- ✅ **它做 HIS 集成** → 对**网络稳定性**零容忍 → **返修率是唯一判据**。

### 打法
- 首封给 `info@zkr.com.tr`，主题 **"Hasta başı terminaller için uzun mesafe PoE switch（sessiz / fansız）"**（床旁终端用长距静音 PoE）。
- ⭐ **用数字开场**：**"Bir 500 yataklı hastane ≈ 1.000 PoE portu"** —— 一句话让它的销售总监抬头。
- 问：**"Hastane projelerinde switch'i siz mi veriyorsunuz?"**

### 证据等级与空白
- 已核实：集团 1982 / 公司 2005 / 品牌 ZKR 2011、**Çankaya 地址与电话传真**、**11–50 人**、IP 护理呼叫系统全部构件、**700+ 套 / 3,000 万患者**自述（官网 + MedicalExpo + LinkedIn 三处）。
- 空白：营收、现交换机品牌、是否单独采购网络设备。
"""

D['79'] = """
### 一句话
**Eurocam（Eurocam GD Güvenlik ve Elektronik Sistemleri San. Dış Tic. Ltd. Şti.）是 Perpa 的"自有品牌进口商"**——2010 年起自营进口，**自有品牌 Eurocam / Europer / Eurolink**，同时**授权分销 Dahua、Hikvision、Eleks、Teknim、Ruijie/DMTECH**，自述 **500+ 经销商**。⭐ **它代理 Ruijie（锐捷）——说明它已经在做企业网络。**

### 主体与坐标
| 项 | 内容 |
|---|---|
| 法定名 | **Eurocam GD Güvenlik ve Elektronik Sistemleri San. Dış Tic. Ltd. Şti.** |
| 地址 | **Perpa Ticaret Merkezi, Şişli / İstanbul** |
| 起业 | **2010**（自述 15+ 年） |
| 渠道 | ⭐ **500+ 经销商（bayi）**，全国 |
| 自有品牌 | **Eurocam**（摄像机）、**Europer**（人员考勤/PDKS）、**Eurolink** |
| 授权分销 | ⭐ **Dahua、Hikvision、Eleks、Teknim、Ruijie（锐捷）/ DMTECH** |
| 服务 | **直接进口（aracısız）+ CE 认证 + 7/24 技术支持 + 自有研发/软件团队**（视频分析、车牌识别、报表演算法） |

### 为什么它是我方在 B 档的"高优先"
1. ⭐ **它代理 Ruijie** → **它已经在卖企业级交换机** → **有品类、有渠道、有技术认知，只缺"更便宜的供货"**。
2. ⭐ **它做自有品牌（3 个）** → **贴牌能力已验证** → 可谈 **"Eurocam 牌 PoE 交换机"**（或 Eurolink 牌）。
3. ⭐ **500+ 经销商 + 直接进口** → **量是 B 档里最大的之一**。
4. **它有研发团队做视频分析/车牌** → **技术型采购，认参数不认话术**。

### 打法
- 首封给 `info@eurocamguvenlik.com.tr`，主题 **"Ruijie yanında ekonomik katman: Eurocam markalı PoE switch"**（Ruijie 之下的经济层 + Eurocam 牌）。
- ⚠ **不要说"我们可以替代 Ruijie"** —— 说 **"Ruijie 之上的项目用它，价格敏感的项目用我们的"**（帮它做价格分层，它一定听懂）。
- 问：**"Ruijie'yi hangi projelerde kullanıyorsunuz, hangi projelerde fiyat yetmiyor?"**

### 证据等级与空白
- 已核实：法定名、Perpa 地址、**2010 起业**、**三个自有品牌**、**五个授权代理含 Ruijie**、**500+ 经销商 + 直接进口 + 研发团队**（官网"关于我们""品牌""服务"三页逐条）。
- 空白：员工数、营收、现 PoE 年采购量、采购负责人。
"""

D['100'] = """
### 重复登记说明
⚠ **本档 = #44 `PROVES`（Proves Bilgi Teknolojileri A.Ş.）**，跨批次重复。**内容以 `044-proves-proves-bilgi-teknolojileri-san-tic-a-s.md` 为准**（201–500 人、伊兹密尔双址、创始人 Serdar Karasu、切入点为"分支机构/园区 PoE"）。

### 操作要点
- **只联系一次**（避免同一家收到两封不同销售的信）。
- 按"不合并"原则保留两份文件、互相标注。
"""

D['101'] = """
### 一句话
⚠ **本档只有"人名 + 电话"（Necdet Şenkaçayc），公开网络无对应实体**。检索 `Necdet Şenkaçayc` 未见公司页、LinkedIn 公司页或展会记录。**本轮结论：主体无法确认，属"个人联系人"类记录。**

### 处理方式（按"不猜"原则）
1. **不补公司名、不补地址**。以电话/WhatsApp 为唯一锚点。
2. 这类记录的正确用法：**直接打电话问"公司全称 + 你们做什么"**，一次通话即可建档。
3. 若电话不通 → **归入观察项**，不投入。

### 与我方的切入点（假设是中小工程商/贸易商）
- 土耳其以个人名义登记的联系人，多数是**小工程商老板或贸易商**：**单量小、决策快、现金交易为主**。
- 打法：**WhatsApp + 短句 + 8 口 PoE 单价**，不谈方案。

### 证据等级与空白
- 已核实：**无**。
- 空白：全部。
"""

D['102'] = """
### 重复登记说明
⚠ **本档 = #32 `Fiberix`（FİBERİX İLETİŞİM HİZMETLERİ LTD. ŞTİ.）**，跨批次重复。**内容以 `032-fiberix.md` 为准**。

### 一句话提醒（最重要的一条）
**Fiberix 是 ISP（ASN 185.207.56.0/22），不是设备分销商。** 处理方式见 #32：**只问"企业侧 CPE 是否你们配套"，不首封卖货**。
"""

D['103'] = """
### 一句话
⚠ **"AcuSense" 是 Hikvision 的技术商标（AI 人车分类），不是土耳其公司名。** `acusenseteknoloji / Ümit Çelik` 这条记录大概率是**某个以 "AcuSense" 命名的极小公司/个体**（或干脆是把产品词当公司名录进来了）。**检索未见任何土耳其实体。**

### 检索实况
| 角度 | 结果 |
|---|---|
| `AcuSense` | **全部命中 Hikvision 的产品技术页**（AcuSense = Hikvision 的 AI 分类商标） |
| `Acusense Teknoloji` / `Ümit Çelik` | 无公司页、无 LinkedIn 公司页、无名录命中 |

### 处理建议
1. **不开档、不投入**；保留原始记录即可（用户侧联系人可能是真的，但**公司名是产品词**）。
2. 若用户侧确认此人仍在做安防 → **按"个人安装商"打**（WhatsApp + 8 口 PoE 单价）。
3. ⚠ **不要在任何对外文件里把 "AcuSense" 当我方客户名写**（那是 Hikvision 的商标，写出去显得不专业）。

### 证据等级与空白
- 已核实：**AcuSense 是 Hikvision 商标**（Hikvision 官方土耳其站）。
- 空白：该联系人所属实体（可能不存在）。
"""

D['104'] = """
### 重复登记说明
⚠ **本档 = #43 `Düzgün Toptan Ticaret / teksarf.com`**，跨批次重复。**两档结论一致：查不到安防/网络实体，`teksarf` 是纺织辅料 B2B，建议降 C（品类不符）。**

### 操作要点
- 若用户侧坚持保留，**唯一动作**：一句话问"你们做什么品类"。
- 与 #43 保持两份文件、互相标注（不合并）。
"""

D['105'] = """
### 一句话
⚠ **IHM Technology 公开面几乎为零**：检索只命中一位员工的 LinkedIn（Mehmet Kocabıyık，马尔马拉大学）。**无官网、无企业名录、无产品目录。**

### 处理方式
1. **不猜公司性质**（可能是集成商、也可能是贸易商）。
2. 通过那位员工（LinkedIn）**问公司全称与业务**，比猜更快。
3. 若 LinkedIn 联系不上 → **本档暂不投入**。

### 与我方的切入点（假设是中小集成商）
- 土耳其的 "Technology" 命名小公司，多数做 **IT 集成 / 安防 / 网络转售**。
- 打法：**一次电话 + 8/16 口 PoE 报价表**，看反应再决定投入。

### 证据等级与空白
- 已核实：**仅一位员工的存在**（LinkedIn）。
- 空白：法定名、地址、业务、规模 —— 全部。
"""

D['106'] = """
### 一句话
⚠ **本档只有"人名（Ufuk Gökalp）+ 品牌名 Sinerjik"，公开网络无对应实体。** 检索 `Sinerjik` 命中的是**通用词（synergy 的土耳其语拼法）**，无公司页命中。

### 处理方式
1. **不开档、不投入**；以 111 记录的联系方式为唯一锚点。
2. 若联系上 → **一次通话建档**（公司全称 / 做什么 / 一年多少台）。
3. ⚠ **"Sinerjik" 是通用词**，不要用它做搜索关键词（噪声太大），用**人名**搜。

### 证据等级与空白
- 已核实：**无**。
- 空白：全部。
"""

D['107'] = """
### 一句话
⚠ **`marbim.com.tr` 对应的是马尔丁（Mardin）的一家极小 IT 店**：**Marbim Bilişim Sistemleri**（Kızıltepe / Mardin），业务为**摄像机与报警、电话交换机、广播、电脑销售与维修、布线施工**——**典型的东南部小城 IT 店**。

### 已核实的少量信息
| 项 | 内容 |
|---|---|
| 名称 | **Marbim Bilişim Sistemleri** |
| 地点 | **Kızıltepe / Mardin**（东南安纳托利亚） |
| 业务 | 摄像机与报警系统、**电话总机（telefon santralı）**、广播系统、电脑销售与维修、布线施工 |
| 渠道 | Facebook 页为主（`facebook.com/www.marbim.com.tr`） |

### 与我方的真实关系
- ⚠ **单量极小**（一个县城的 IT 店，一年可能十几台）。
- ⚠ **物流远**（Mardin 距伊斯坦布尔 1,300 km，运费占比高）。
- ✅ **唯一价值**：**东南部/边境市场（Mardin 靠近叙利亚/伊拉克）** 可能做**转口**，若确认走转口则重新评估。

### 打法（要不要投入）
- **不建议排进优先名单**。若要触达，**最低成本方式**：Facebook 私信 + 8 口 PoE 单价（它会自己算运费）。
- 问：**"Sınır ticareti (Irak/Suriye) yapıyor musunuz?"** —— 若是，则价值完全不同。

### 证据等级与空白
- 已核实：名称、Kızıltepe / Mardin、业务范围（Facebook 页 + 本地名录）。
- 空白：法定名、规模、是否做转口。
"""

D['114'] = """
### 重复登记说明
⚠ **本档 = #40 `AG Bilgisayar`**，跨批次重复（联系人同为 **Aycan Çam**）。**两档结论一致：主体无法确认**（检索只命中安格的 AGR Bilişim，不匹配）。

### 操作要点
- **只联系一次**；用电话/WhatsApp 问 **"公司全称 + 网址"**。
- 与 #40 保持两份文件、互相标注（不合并）。
"""

D['116'] = """
### 重复登记说明
⚠ **本档 = #41 `FH Güvenlik`**（`fhguvenlik.com`，2025 年注册，Perpa 片区，0534 484 98 11）。**内容以 `041-fh-guvenlik-sistemleri-ve-bilisim-san-tic-ltd-st.md` 为准。**

### 一句话提醒
**它是 2025 年新公司 = 供应商完全空白 = 我方最容易进的一家**；但**只有手机号 → 账期必须严控**。走 **WhatsApp**，不要发长邮件。
"""

D['117'] = """
### 重复登记说明
⚠ **本档 = #42 `Bilgen Elektronik`**（Gebze / Kocaeli）。**内容以 `042-bilgen-elektronik-guvenlik-sistemleri-ltd-sti.md` 为准。**

### 一句话提醒
它**公开转发 Teknim / Polimek** → **站队土耳其本土品牌** → **对新品牌的接受度高于"只认国际大牌"的工程商**；切入口是 **Gebze OSB 的厂区周界 PoE（长距 + 防雷 + 宽温）**。
"""

D['123'] = """
### 一句话
⚠ **本档只有人名（Sedat），无公司名、无域名、无电话线索可检索。** 公开网络无从下手。

### 处理方式
1. **不猜**。以 111 记录的联系方式为唯一锚点。
2. 一次通话建档：**公司全称 / 业务 / 一年多少台 / 谁采购**。
3. 若联系不上 → 观察项。

### 证据等级与空白
- 已核实：**无**。
- 空白：全部。
"""

D['124'] = """
### 一句话
⚠ **Interland Group 不是"网络/安防"公司**：它是 **1995 年成立的国际贸易集团**（İstanbul Ümraniye，美国/保加利亚/中国有分支）。**`interland-network-security` 这个名字里的 "network security" 与它的实际业务（综合贸易）可能不是一回事**——需先确认它是"做网络安全"还是"名字里有 network"。

### 主体与坐标
| 项 | 内容 |
|---|---|
| 名称 | **INTERLAND GROUP** |
| 成立 | **1995** |
| 地址 | **Tatvani Mah. Estergon Cad. Suryapı Exen Sit. F Blok Kat:11 No:161, Ümraniye / İstanbul 34764** |
| 电话 / 传真 | **+90 216 70 975 34** / 传真 850 522 34 03 |
| 邮箱 | `info@interlandgroup.com` |
| 分支 | ⭐ **美国、俄罗斯、中国、保加利亚**（官网一处写美国/俄罗斯/中国，LinkedIn 写美国/保加利亚/中国） |
| 自述 | 国际贸易，"可靠性、质量、连续性" |

### 与我方的真实关系
- ⚠ **它的公开页面没有任何产品目录、没有品牌、没有技术团队描述** → **更像"综合贸易/代理"而不是"技术分销"**。
- ✅ **但它有"中国分支"** → **它熟悉中国采购** → 若它确实做设备贸易，**它不需要教育，只需要报价**。
- ⚠ **必须先确认**：它的"network security"是**真业务**还是**域名/名字巧合**。

### 打法（先确认，再谈）
- 首封给 `info@interlandgroup.com`，**只问不卖**：*"Ürün kataloğunuz var mı? Network/security tarafında hangi markalarla çalışıyorsunuz?"*
- 若答"有产品线" → 按分销商谈；若答"综合贸易" → **本档归档**。

### 证据等级与空白
- 已核实：1995 成立、Ümraniye 地址、电话传真、**四国分支**、贸易定位（官网 + LinkedIn）。
- 空白：**实际产品线与品类（最大未知）**、规模、营收。
"""

D['126'] = """
### 一句话
⚠ **Nazemco 与 #51 同一家**（`Nazemco İth. İhr. San. Tic. Ltd. Şti.`）。**两档公开面同样极薄**：无实质官网、无产品目录、无 LinkedIn。本档为主档，内容与 #51 一致、不重复。

### 处理建议
1. **不合并文件**；**只联系一次**。
2. 它的价值判断：法定名含 **İth. İhr.（进口出口）** 但**无技术面** → **更像"转口贸易商"**，适合做**利比亚/伊拉克/叙利亚方向的清关与转口渠道**（与 #45 Alamthal 同类）。
3. 若确认是纯贸易 → **按"转口渠道"谈 FOB 伊斯坦布尔**，不按"本地分销"谈账期。

### 证据等级与空白
- 已核实：法定名、进口出口属性。
- 空白：地址、规模、品类、决策人 —— 几乎全部。
"""

D['128'] = """
### 一句话
⚠ **本档只有"Fatih A."（人名缩写），无公司实体可检索。** 这类记录在名单里通常是**个人安装商/自由项目经理**。

### 处理方式
1. **不猜**。以电话为唯一锚点，一次通话建档。
2. 个人安装商的特征：**单次 1–5 台、现金/即时付款、品牌零忠诚** → 打法 = **WhatsApp + 单价 + 现货**。

### 证据等级与空白
- 已核实：**无**。
- 空白：全部。
"""

D['130'] = """
### 一句话
⚠ **本档只有电话号码（+90 543 780 22 23），无公司名。** 543 = 土耳其移动号段（Vodafone）。**无法做任何网络检索。**

### 处理方式
1. **不猜**。WhatsApp 直连是唯一路径（土耳其手机号绝大多数注册了 WhatsApp）。
2. 首句模板：*"Merhaba, ... firmasından ... — hangi firmadasınız ve ağ/switch tarafında çalışıyor musunuz?"*
3. 若对方是做工程/贸易的 → 建档；若是私人号 → **归入观察项**。

### 与我方的切入点（假设是中小工程商）
- 手机号登记 = **个人老板**，决策 100% 在他手上 → **报价要一次到位**。

### 证据等级与空白
- 已核实：**仅号码本身**。
- 空白：全部。
"""
