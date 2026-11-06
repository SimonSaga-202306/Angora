# 151 · KGYS「C 型边缘交换机」= 土耳其 8 口工业 PoE 的全国性市场；以及五家新渠道线索

**日期**：2026-11-06（+0800） · **轮次**：r82（第 35 次「继续」） · **上一份**：`150-four-new-leads-and-rubisec-cert-gap-2026-11-06.md`
**一句话**：上一轮我在找「谁在卖工业交换机」；这一轮找到了**「国家为什么要买 8 口工业交换机」**——土耳其警方的城市安全系统（KGYS）在全国电线杆的现场机柜里，每一根杆子要一台 8 口工业 PoE 交换机，而规格书第 1.1.26 条要求**警察总局信息与通信部签发的「C 型边缘交换机与流量整形测试报告（结果：BAŞARILI）」**。这张纸是在位者的护城河，也是我方唯一真正的门槛。

---

## 0. 七句话

1. **KGYS 规格书原文**：现场机柜内那台设备叫「C TİPİ ETHERNET ANAHTAR」，必须是**工业级、−40~+60 ℃、无风扇、IP20、带告警继电器、支持环网冗余、8 个千兆电口 + 至少 2 个千兆光口、≥8,000 MAC、每口都要 PoE（802.3af/at）**，且**每口可做 traffic shaping**（40 Mbps 下丢包 ≤0.5%、延迟 ≤0.5 s、能吸收 ≥200 Kbit 突发）。
2. **门票是一条认证**：1.1.26 条 —— 必须持有**警察总局（EGM）信息技术与通信部**签发的、结果为 **「BAŞARILI」** 的《C-Tipi Kenar Anahtar ve Traffic Shaping Test Report》，且投标签约时必须随标提交。
3. **目前拿到这张纸的只有 4 个牌子**：**Extreme Networks、Allied Telesis、CryptoLink、D-Link**（来源：turk-iot.com 技术文，2023-12）。
4. **CryptoLink 的那台 `CRLISW-8P` 与 D-Link `DIS300`、Extreme `ISW 8GbP 4-SFP` 是同一套固件界面**（默认 `192.168.2.1`、`admin/admin`，配置步骤完全相同）⇒ **极可能同一个台湾 ODM 平台，CryptoLink 是贴牌而非自研**（**推断，非确认**）。这直接改写我们对 CryptoLink 的判断：**它是「已经有门票的二道贩子」，不是「需要门票的新人」**——它是我方进入 KGYS 最快的通道。
5. **在位价格锚**：D-Link `DIS-300G-8PSW`（6×1G + 2 SFP + 4 PoE+ / 120 W / IP30 / 16 Gbps / 8K MAC / 无风扇）零售 **$1,132 / $1,262**；Lantech 泰国代理价 `IPGS-3208GSFP-48V` **35,443 THB**、`IPGS-3408GSFP-48V` **39,278.25 THB**（≈$1,000–1,200）。⇒ **KGYS 单杆位这一档的市价就是 $1,100–1,300**，与我方 $380（DAHUA）/$500–700（目标档）之间是 **2–3 倍空间**。
6. **五家渠道线索全部落地**（含工商号/地址/电话/关键人；其中 **Areskom 是对 r37 旧档 #63 的升级，不是新入**）：**Teslakom**（Lantech 土耳其独家 10 年，A-/76）· **Proline Bilişim**（$6.645M EGM KGYS 24 个月合同，A-/75）· **Areskom**（Westermo 16 年 VAD，B+/71）· **GGS Bilişim**（6 省 KGYS，B/68）· **Ankara Netmon**（1998 Netaş 出身，126 人，Top500 ICT 第 14，B/66）；另有 OBC / 4A Elektrik / Teleteknik / TİO 四家电力与盘厂线。
7. **一条自我修正**：**İSAC 不是「纯目录商」，它的质量方针写着「目标是进入生产、建立自己的企业品牌」** ⇒ 它要的是**贴牌供应商**，不是又一个代理品牌。这条改变了给 İSAC 的话术（详见 §4）。

---

## 1. KGYS：土耳其 8 口工业 PoE 的全国性市场

### 1.1 它是什么
**KGYS = Kent Güvenlik Yönetim Sistemi（城市安全管理体系）**，民间俗称 **MOBESE**。由**安全总局（Emniyet Genel Müdürlüğü, EGM）** 主导、**ASELSAN / ASELSANNET** 承接全国 81 省 + 北塞的摄像头、车牌识别（PTS）、交通电子稽查网。执行层是一批**现场安装与集成商**（§3）。

**对我方的意义**：这套系统的物理末端就是**街道电线杆下的现场机柜**——每根杆子、每个路口，一台工业交换机，把 8 路摄像头（每路 ≤5 Mbps，合计 ≤40 Mbps）汇到光纤环网。**这是「8 口工业 PoE」这个品类在土耳其唯一一个国家级、可重复、按省份批量复制的需求源。**

### 1.2 规格书原文要点（C TİPİ ETHERNET ANAHTAR）
来源：`turk-iot.com`「Cryptolink Switch KGYS Projesi özelinde Konfigürasyonu」（2023-12），引用 EGM 技术规格书 1.1 条全文。

| 条款 | 要求 |
|---|---|
| 1.1 定义 | 立杆现场机柜内汇聚摄像头/室外无线/网络设备的通信设备；**允许与其他交换机不同品牌** |
| 1.1.1 | 必须是**工业型**交换机 |
| 1.1.2 | 工作温度 **−40 ℃ ~ +60 ℃** |
| 1.1.3 | 湿度 **10–95%** |
| 1.1.4 | **无风扇**，不得有活动散热部件 |
| 1.1.5 | 至少 **IP20** |
| 1.1.6 | 故障告警继电器输出 |
| 1.1.7 | 环网/Mesh 冗余；光纤任一点断纤或断交换机，其余网络不中断 |
| 1.1.8 | **≥8 个千兆电口 + ≥2 个千兆光口**；SFP 可支持 70 km，LX/SX/ZX/100BASE-X；随设备带 1 个同品牌 10 km 1000Base-LX SFP |
| 1.1.9 | 每支 SFP 配 1 米光纤跳线 |
| 1.1.10 | 全端口 **non-blocking** |
| 1.1.11 | **≥8,000 个 MAC** |
| 1.1.12 | ≥4 个优先级队列 |
| 1.1.13 | RMON + **SNMP v1/v2/v3**，telnet/console/web 管理 |
| 1.1.14 | L2 ICMP + **IGMP snooping** |
| 1.1.15 | **802.1Q VLAN**、MSTP(802.1s)、x-ring 或同类、VLAN tagging/trunking |
| 1.1.16 | 802.1p 优先级 + ToS |
| 1.1.17 | MAC 地址端口安全 |
| 1.1.18 | 可导轨安装（含电源适配器） |
| 1.1.19 | **802.1x** 端口准入 |
| 1.1.20 | 端口镜像 |
| 1.1.21 | **每一个端口都要 PoE（802.3af）与 PoE+（802.3at）** |
| 1.1.22 | **LACP 802.3ad** |
| 1.1.23 | **IPv6** VLAN 接口与流量 |
| 1.1.24 | 授权随设备，不得另购 license |
| 1.1.25 | **每物理端口（含 SFP）可独立 traffic shaping**：40 Mbps 总量下丢包 ≤0.5%、整形延迟 ≤0.5 s、能吸收 ≥200 Kbit 突发（软/硬件 buffer）；**不得另配整形设备** |
| **1.1.26** | **必须持有 EGM 信息技术与通信部签发的、结果「BAŞARILI」的《C-Tipi Kenar Anahtar ve Traffic Shaping Test Report》**，随标提交；以往以「Haberleşme Daire Başkanlığı」名义签发的旧报告同样有效 |

### 1.3 谁已经有这张纸
同源（turk-iot.com）明确写出：**「Türkiye'de hali hazırda Extreme Network, Allied Telesis, Cryptolink, Dlink gibi çeşitli markalar Haberleşme Daire Başkanlığı'ndan BAŞARILI raporu almış」**——即 **Extreme Networks / Allied Telesis / CryptoLink / D-Link 四家已取得「BAŞARILI」报告**，且现场已有大量在用设备。

对应型号（同源）：
- **CryptoLink `CRLISW-8P`**
- **D-Link `DIS300`**（系列）
- **Extreme Networks `ISW 8GbP, 4-SFP`**

**⚠ 结构性观察（推断，非确认）**：文中说三家「使用相似的软件、配置相同」，并给出截图——默认 IP `192.168.2.1`、`admin/admin`、系统信息页同款布局。⇒ **三家极可能出自同一台湾 ODM 参考设计，CryptoLink 是本地贴牌商。** 若成立：
- **CryptoLink 的价值不是「新客户」，而是「已持票 + 已有配电/边境环网场景」的通道**；
- **我方的谈判筹码是「同一平台、我方报价」**，而不是「说服它换品牌」（与 r80「对 CryptoLink 谈边境/车牌环网」一致，但优先级应上调）。

### 1.4 在位价格锚（本轮新增）
| 型号 | 规格 | 价格 | 来源 | 折算 |
|---|---|---|---|---|
| **D-Link `DIS-300G-8PSW`** | 6×1G + 2 SFP + **4 PoE+** / 120 W / IP30 / 16 Gbps / 8K MAC / 无风扇 / 导轨 | **$1,132.22**（eibabo，含税口径）/ **$1,261.99**（Tradeinn，含税） | eibabo.us、tradeinn.com | **≈$1,130–1,260** |
| 同上（澳/新币） | — | AUD 2,507 / AUD 3,107 / SGD 3,142 | cplonline、megaofficesupplies、compaqs | 佐证同一价位带 |
| **Lantech `IPGS-3208GSFP-48V`** | 8×1G + 2 SFP，8 口 PoE 30 W，−20~60 ℃ | **35,443.00 THB** | businessensotech.com（泰国代理价目） | ≈**$1,090**（按 ~0.0307 USD/THB 估，⚠ 汇率假设） |
| **Lantech `IPGS-3408GSFP-48V`** | 8×1G PoE at/af 30 W + 4 SFP，−40~75 ℃ | **39,278.25 THB** | 同上 | ≈**$1,205**（同上假设） |
| **Allied Telesis `AT-GS950/10PS`** | 8 口 PoE 智能管理 | **$496.1 + KDV** | pamukteknoloji.com.tr | 佐证「非全 PoE 的 8 口」在 $500 档 |
| **Allied Telesis `AT-GS980M/52`** | 48 口管理型 | **$3,000 + KDV** | 同上 | 48 口锚点 |

**结论**：KGYS 现场这一档（8×1G + 2~4 SFP + PoE + 环网 + 整形）**在位成交带 = $1,100–1,300**，与 r80 的 RUBISEC `IS-300-12GPX` **$1,221** 完全重合 ⇒ **不是巧合，是这一档的国际市价**。我方 $380（DAHUA 8 口 PoE）/ $500–700 目标档在其下方 **2–3 倍**。
**⚠ 注意**：`DIS-300G-8PSW` 只有 4 个 PoE 口，不满足 1.1.21「每口 PoE」⇒ KGYS 用的应是该系列**全 PoE 变体**，我方引用时不得把 8PSW 当成 KGYS 中标型号。

---

## 2. 五家新线索（按优先级）

### 2.1 ⭐⭐⭐ Teslakom — 「只有一个硬件品牌」的独家代理（**A- / 76，优先级①**）
| 项 | 内容 |
|---|---|
| 法定名 | **TESLAKOM BİLİŞİM VE TELEKOMÜNİKASYON A.Ş.** |
| 成立 | **2013**（创始团队自称「15 年行业经验」）；**2019** 在安卡拉 Bilkent CyberPark 设 **AR-GE 办公室** |
| 人数 | **11–50**（LinkedIn / Lusha 一致） |
| 伊斯坦布尔 | **Demirkol Plaza C Blok Kat:2 No:54, Bağcılar / İstanbul** · **0212 356 46 46** · faks 0212 216 10 58 |
| 安卡拉 | **1606. Cad. No:4/A, Cyberpark Cyberplaza A Blok 2.Kat No:A207, 06800 Bilkent / Ankara** · **0312 472 99 67** |
| 邮箱 | `iletisim@teslakom.com` |
| 品牌 | **LANTECH（台湾，工业交换机/路由器/AP）** · NIAGARA NETWORKS · FUDO · VIPRINET · SYCOPE · CELERWAY · WANTASTIC · AUKUA · PORTNOX NAC |
| 独家 | **「TESLAKOM 自 2016 年初起担任 Lantech 在土耳其的唯一授权经销商」**（官网原文） |
| Lantech 产品线 | 工业无线 · **EN50155** · **Layer 3** · **IEC 61850-3** · **PoE** · **10G** · **E-Mark** · **DNV-Tip** · **KGYS 现场交换机（C 型）** · 串口设备 · SFP |
| KGYS 型号 | **`IPGS-3408GSFP-48V-E`**：8×10/100/1000T + 4×1000M SFP L2 · PoE at/af · **G.8032 环网** · **16K MAC** · 8 个优先级队列 · **−40~75 ℃** · 24 Gbps non-blocking · **硬件集成 traffic shaping** · **「通过 EGM 相关测试」** |

**为什么它是第一优先**：8 个品牌里**只有 1 个是硬件网络**（其余是 SD-WAN / PAM / 抓包 / 测试仪）。它的整条硬件收入压在一个台湾品牌上，且官网明写 R&D 目标是**「把土耳其工程师的经验与本土/民族生产能力结合」**——**它想要自己的产品**。这是「贴牌 + 二供」的双重入口，比 İNFOGEN 的「补一格」更硬。
**切入点**：不谈替换 Lantech（它会失去 10 年独家身份），只谈**「你给 KGYS 报价时，Lantech 之外的第二条成本线」**；顺带问它 **EGM 报告能否挂在我方型号上**（若 Lantech 已持票，它知道流程）。

### 2.2 ⭐⭐⭐ Proline Bilişim — 手上正握着一张 $6.645M 的 KGYS 合同（**A- / 75，优先级②**）
| 项 | 内容 |
|---|---|
| 法定名 | **PROLINE BİLİŞİM SİSTEMLERİ VE TİCARET A.Ş.** |
| 成立 | **2003**（Bloomberg / PitchBook） |
| 人数 | **≈105**（PitchBook） |
| 地址 | **Şerifali Mah. Beyan Sokak No:66, Ümraniye / İstanbul**（⚠ 与 İSAC 的 Beyan Sk. No:5 同一条街） |
| 电话/邮箱 | **+90 216 528 62 00 / 62 04** · `info@pro-line.com.tr` |
| 关键人 | **Serdal KARAKAŞ（CEO）**（Austurkiye 会员资料）；D&B 列 Alparslan Cemail Batuk |
| 归属 | **Pasifik Teknoloji A.Ş. 的子公司**（PATEK，BIST 上市），PitchBook 记母公司为 Pacific Hardware and Software Information Technologies |
| 能力 | 系统集成 + **工业与科技部认证的 AR-GE 中心**；自研城市安全智能软件、GIS、指纹/静脉/人脸识别；做过 **e-Pasaport**、e-Kimlik 试点、SGK 生物识别（BioPOS） |
| **在手的钱** | **2026-09-23/24 KAP 公告**：EGM「**土耳其全国 KGYS 现代化与改进项目**」联合体框架内签下 **KGYS + 车牌识别（PTS）基础设施安装与承包合同，$6,645,000 + KDV，24 个月内完成** |

**为什么它是第二优先**：这不是「潜在需求」，是**已签、24 个月、按月要发货**的现场设备清单。$6.645M 里现场交换机是必配项（按 §1.2 每杆一台）。**它比任何 DMO 目录商都更急需第二供应商**。
**切入点**：**「你的 KGYS 现代化包里，现场 C 型交换机现在挂谁的牌？我方能给到 $500–700 档，且愿意配合做 EGM 测试。」** 只谈二供/降本，不谈替换（它会怕影响已批的技术文件）。

### 2.3 ⭐⭐ Areskom — **（升级既有档 #63，非新入）** 纯工业网络 VAD，Westermo 16 年（**B+ / 71，优先级③**）
> ⚠ **本条不是新线索**：Areskom 早已在 `111-turkey-customer-pipeline.csv` **第 63 行**（r37 收录，记「B- / 35 分」、「上游 = **CTS（台湾）**」「工业 MC/switch/控制设备（很多有名的牌子）」）。**r82 用一手来源把它从 B-/35 升级到 B+/71，并推翻「上游是 CTS」这一条**（见 §3.4）。

| 项 | 内容 |
|---|---|
| 法定名 | **ARESKOM İLETİŞİM SİSTEMLERİ TİC. LTD. ŞTİ.** |
| 成立 | **2004** |
| 定位 | 自称 **Value Added Distributor**（数据通信 / 工业网络 / 移动宽带 / M2M / IoT / 电信） |
| 地址 | 官网：**Altunizade Mh. Kısıklı Cd. No:35/1 Kat1, Üsküdar / İstanbul**；⚠ 行业名录仍记旧址 **Muhittin Üstündağ Cad. No:23, Koşuyolu, Kadıköy**（搬迁，两址并存） |
| 电话/邮箱 | **+90 216 428 78 78**（传真 428 76 76）· `info@areskom.com.tr` |
| 人数 | 1–10（alo118 估算，⚠ 偏小，不可作准） |
| 品牌 | **Westermo（瑞典）** · Teltonika · ETC (Etic Telecom) · Acromag · Lanner · Atop · Sena · **TEKTELIC** |
| 能力 | **Westermo 合作「超过 16 年」**（Eurasia Rail 2025 展商自述）；售前/硬件/售后全流程；site-survey、方案设计、调试 |
| 关键产品 | **Westermo Lynx 5612-F4G-T8G-LV**（**IEC 61850-3 变电站交换机**，L2/L3，8×RJ45 + 4×SFP）· **RedFox 5528**（机架型）· **Viper 220A-P8**（EN50155 车载） |

**为什么有价值**：它**已经是变电站与铁路两条线在土耳其的技术窗口**，卖的是瑞典高价货（Lynx 级）。它缺的正是**「同一个 IEC 61850-3 功能、1/3 价格的第二品牌」**——而这恰好是 r81 确认的我方**认证缺口**：**没有第三方 61850-3 报告，连它的报价单都进不去**。⇒ **Areskom 是检验「要不要去拿认证」的最好试纸**：先问它「没有 61850-3 报告，你的客户会不会接受工厂/水厂/园区场景？」。

### 2.4 ⭐⭐ GGS Bilişim — 6 省 KGYS 的现役集成商（**B / 68，优先级④**）
| 项 | 内容 |
|---|---|
| 法定名 | **GGS BİLİŞİM TEKNOLOJİLERİ A.Ş.** |
| 成立 | **2005**（LinkedIn 自述：「从安卡拉 Ostim 一间 50 m² 办公室起步」） |
| 地址 | **Batı Sitesi Mah. Gersan Sanayi Sitesi 2307/2 Sok. No:11, Batıkent, 06370 Yenimahalle / Ankara** |
| 电话/邮箱 | **+90 312 474 01 30** · `info@ggsbilisim.com` |
| 人数/营收 | ⚠ **三套口径冲突**：LinkedIn 201–500 · ZoomInfo 324 人 / 营收 $10–25M · RocketReach 3 人 ⇒ **不引具体数，可用「数百人级」** |
| 业务 | KGYS 建设/维护/项目（**安卡拉、伊斯坦布尔、伊兹密尔、特拉布宗、梅尔辛、代尼兹利**）· 车牌识别 · 红灯闯越抓拍 · 无线通信 · 交通电子稽查（TEDES）· IT-Network |
| 经验 | 自称 **20 年** |

**切入点**：它做的是**省会级整城项目**，一次采购就是数百台现场交换机；比 Proline 小但**决策链更短**（家族/创始团队）。

### 2.5 ⭐⭐ Ankara Netmon — 1998 年 Netaş 安装团队独立出来的工程公司（**B / 66，优先级⑤**）
| 项 | 内容 |
|---|---|
| 法定名 | **ANKARA NETMON İLETİŞİM SİSTEMLERİ TİCARET VE SANAYİ A.Ş.** |
| 成立 | **1998**，由 **Netaş（Nortel Netaş）安装组外包**、15 名员工创立，股份公司 |
| 人数 | **126 名专业人员**（kariyer.net 企业页）· LinkedIn 51–200 |
| 地址 | **Dumlupınar Caddesi No:28, Maliköy Anadolu OSB, Sincan / Ankara**（现址）；1999– 曾在 **Ostim 1200. Sokak No:137，1,800 m²** 厂房 |
| 电话/邮箱 | **+90 312 385 86 00** · `netmon@netmon.com.tr` |
| 排名 | LinkedIn 自述：**土耳其 ICT 500 强第 14 位** |
| 业务 | 电信安装/配置/工程/运维；**KGYS 与 PTS（车牌识别）基础设施**（SSB + ASELSAN 合同下，以安卡拉为首多省）；**5G 国产化**；**铁路信号与乘客信息系统**（Anadolu Raylı 集群成员，有自产 RF 接地汇流排）· 军用系统 |

**切入点**：它是**「现场施工队 + 工程公司」**，不是品牌商 ⇒ 对品牌无忠诚，只对**交期与现场可用性**敏感。它做铁路信号（EN50155 场景）与 KGYS（C 型场景）两条线，**正好是我方 8 口工业两档产品都能碰上的客户**。

### 2.6 电力 / 盘厂线四家（B 档，优先级⑥–⑨）

| 公司 | 法定名 | 成立 | 地址 | 电话 | 与我方的关系 |
|---|---|---|---|---|---|
| **OBC** | **OBC BİLGİSAYAR HİZMETLERİ SAN. TİC. LTD. ŞTİ.** | — | Ayşe Hatun Çeşme Sok. Onur Plaza No:3/13, Küçükbakkalköy, Ataşehir / İstanbul | 0850 885 0064 · 0216 577 54 18/19 | **能源自动化**（甩负荷/负荷分配、配电中心、控制中心、工业设施）；**方案伙伴含 SIEMENS + MOXA** ⇒ Moxa 贵，需要 $500–700 二线；IEC 61850 RTU/PMS 自研 |
| **4A Elektrik** | **4A ELEKTRİK ELEKTRONİK TEKNOLOJİ SAN. A.Ş.**（⚠ 一处名录记为 Ltd. Şti.） | **2005**（伊斯坦布尔） | Girne Mah. Irmaklar Sk. No:C-13, Küçükyalı İş Merkezi, Maltepe / İstanbul | **+90 216 366 38 28**（传真 38 29）· `info@4aelektrik.com.tr` | **60–750 kV 输电**保护与控制、**IEC 61850 全数字变电站**、自有屏柜制造、FAT/SAT、培训 ⇒ **只要变电站标，就必须要 61850-3 报告** |
| **Teleteknik** | **TELETEKNİK KONTROL VE GÜÇ SİSTEMLERİ SAN. TİC. LTD. ŞTİ.** | — | Yenişehir Mh. Millet Cd. Sümbül Sk. Sweet Life Center No:6 A79, 34912 Pendik / İstanbul | **+90 216 482 92 47** · 0555 534 36 94 · `info@teleteknik.com.tr` | **RTU/遥测屏、计量屏**制造（TAIS T800 等）、Siemens 生态、Socomec/Frer ⇒ **屏内要 4–8 口非 PoE/低 PoE 交换机，正好是我方 4–8 口那一端** |
| **TİO Otomasyon** | **TİO OTOMASYON SANAYİ VE TİCARİ LİMİTED ŞİRKETİ** | — | Erenler Mah. 1234. Sk. No:17, Erenler / **SAKARYA** | **0264 666 17 71** · WhatsApp 0532 171 17 72 · `info@` / `satis@tiootomasyon.com` | **LS Electric 萨卡里亚授权经销商**（LS 官网列名）· 品牌 LS/Pilz/**Moxa**/Autonics/SMC/TE ⇒ 区域经销商，量小，**C+ / 55** |

**四家的共同结论**：**电力线与 KGYS 线是两种门票**——
- **电力/变电站线**：门票 = **IEC 61850-3 / IEEE 1613 第三方报告**（我方没有，Areskom/4A/OBC 全部卡在这里）；
- **KGYS/现场线**：门票 = **EGM C-Tipi 测试报告**（我方也没有，但在位的 4 个品牌里**有 2 个（CryptoLink、D-Link）是我方能触达的贴牌商**）。

---

## 3. 修正与更新（对 r81 / r80 的显式改写）

### 3.1 ⚠ **修正 r81：İSAC 的 SKU 计数与办公室城市**
- r81 记「工业自动化 **9,707** · 传感器 **19,543**」。**r82（2026-11-06）首页实时计数器为**：**SENSÖR 19,452** · **ENDÜSTRİYEL OTOMASYON 9,725** · KONTROL-PANO 4,781 · SAFETY 2,457 · PLC-HAREKET 2,734 · KABLO-KONNEKTÖR 1,984 · ELEKTRİKMEKANİK 1,889 · HİDROLİK 840 · BAĞLANTI 213 · ELEKTRONİK 69 ⇒ **合计 ≈38,144 条目录条目**。
  - **改写理由**：这些是**活的计数器**，按天变化。**今后引用必须带日期**，且不得把「9,725 条目录条目」说成「9,725 个 SKU 现货」。
  - 首页另有**另一套口径**：「**代理之外我们供应的 26 个品牌**」「**3,503 个产品**」「**28,646 件库存**」—— ⚠ **这是不同区块的计数，不可与分类计数相加或混用**（r81 未区分，**此处更正**）。
- **办公室**：r81 依 `yenibiris.com` 记「**布尔萨分公司 + 盖布泽办公室**」；**官网首页写「İstanbul、Bursa、İzmir 三地办公室」** ⇒ **补 İzmir，盖布泽降级为「招聘信息口径，未在官网确认」**。

### 3.2 ⭐ **新增（r81 未发现）：İSAC 的质量方针里有「做自己的品牌」**
`isac.com.tr/kalite-politikasi/` 原文要点：「**在生产中创造我们自己的企业品牌是我们的目标。为此，ISAC 的目标包括进入生产并最正确地管理制造过程。**」
⇒ **İSAC 要的不是第 N 个代理品牌，而是 OEM/贴牌供应商。** 这**取代** r81 对 İSAC 的「补一格（目录里缺 8 口工业 PoE）」话术——**升级为「帮你把自有品牌的第一台交换机做出来」**。同时它首页有独立的 **Industrial Ethernet Switch** 子分类（在 9,725 条之内），说明**这条线存在但没有品牌纵深**。

### 3.3 ⭐ **改写 r80：CryptoLink 的定位从「客户」升级为「持票通道」**
r80 的结论「对 CryptoLink 谈边境/车牌环网」**依然成立**，但 r82 证据显示它**已持有 EGM「BAŞARILI」报告**（`CRLISW-8P`），且**与 D-Link/Extreme 同固件**。⇒ **它不是需要说服的新人，它是能替我方把产品带进 KGYS 标书的现成通道**。优先级应**从「B 档跟进」上调**。

### 3.4 ⚠ **修正 r37：Areskom 的上游不是「CTS（台湾）」**
- **被推翻的说法**：`111-turkey-customer-pipeline.csv` 第 63 行（r37 收录）记 Areskom 的供应链为 **「CTS（台湾，黄灯）等」**，评级 **B- / 35 分**。
- **r82 一手证据**：Areskom 官网 `/kurumsal/hakkimizda/` 与首页自述代理 **Westermo（瑞典）· Teltonika · ETC (Etic Telecom) · Acromag · Lanner · Atop · Sena · TEKTELIC**；`eurasiarail.eu` 2025 展商页自述「**与 WESTERMO 合作超过 16 年**」；其官网设有 **Westermo IEC 61850-3 变电站交换机专页**（`Lynx 5612-F4G-T8G-LV` / `RedFox 5528` / `Viper 220A-P8`）。
- **⇒ 结论**：**Areskom 是 Westermo 在土耳其的长期工业网络渠道（VAD），不是 CTS 系**。评级由 **B- / 35 → B+ / 71**。
- **⚠ 未处理的遗留**：**CSV 第 63 行文本本身未改**（本轮维持「146 份客户档不动、CSV 自 ingest 后未改」的既有约定）。**下一轮若要刷新 CSV 评级列，需一并把第 63 行的「CTS」改为「Westermo 等多品牌代理」，这是唯一一处已知的旧错误记录。**

---

## 4. 渠道地图：三类买家、三张门票、三句话术

| 类型 | 代表 | 他们要什么 | 门票 | 我方话术（一句话） | 价格档 |
|---|---|---|---|---|---|
| **A. DMO 目录商 / 目录+副线** | İNFOGEN · İSAC · RİVO | 目录里能交货的一格 | 无（只需 K 码 + 发票能力） | 「补你目录里缺的那一格」/「帮你做自有品牌第一台」 | $139–700 |
| **B. 项目集成商（KGYS/城市安全）** | **Proline · GGS · Netmon · CryptoLink · Teslakom** | 按杆位批量、交期、标书合规 | **EGM C-Tipi 测试报告** | 「你 KGYS 包里现场机台现在挂谁的牌？我给你第二条成本线」 | **$500–700（对标 $1,100–1,300）** |
| **C. 工业网络 VAD / 电力 EPC** | Areskom · OBC · 4A · Teleteknik · GSL · ErETE · Simgenet | 技术合规 + 品牌背书 | **IEC 61850-3 / IEEE 1613 报告** | 「无 61850 的工厂/水厂/园区场景，我给你 1/3 价」 | $380–700 |

**这一张表把前三轮的所有线索归了位**：门票决定话术，话术决定价格档，价格档决定先打谁。**没有门票就不要去打变电站和 KGYS 主标**，只打「无认证要求的场景 + 二供」。

---

## 5. 我方产品 vs KGYS 规格 逐条对照（自评，供工厂确认）

| 规格条 | 要求 | 我方现状 | 判断 |
|---|---|---|---|
| 1.1.1–1.1.5 | 工业型 · −40~60 ℃ · 无风扇 · IP20 | 我方工业 8 口为宽温无风扇机型 | ✅ 大概率满足，**需 datasheet 逐条核** |
| 1.1.6 | 告警继电器 | 需确认 | ⚠ |
| 1.1.7 / 1.1.15 | 环网冗余 / x-ring / MSTP | 支持 ERPS/G.8032 类 | ✅（若为 G.8032 需说明「或同类」） |
| **1.1.8** | **≥8 千兆电口 + ≥2 千兆光口** | 须确认是否有 **8×1G + 2×SFP** 的 PoE 型号 | ⚠ **关键**：若只有 8 电口无光口则直接不合格 |
| 1.1.11 | ≥8,000 MAC | 通常 8K | ✅ |
| 1.1.13 | SNMP v1/v2/v3 + RMON | 通常满足 | ✅ |
| 1.1.21 | **每口 PoE af/at** | 需确认是否全口 PoE+ | ⚠ |
| **1.1.25** | **每口可整形、40 Mbps 丢包 ≤0.5%、延迟 ≤0.5 s、≥200 Kbit 突发** | 需固件实测 | ⚠ **这是 EGM 报告的核心测试项** |
| **1.1.26** | **EGM C-Tipi 测试报告 BAŞARILI** | **无** | ❌ **唯一硬门槛** |

**⇒ 下轮必须向工厂问三件事**：① 有没有 **8×1G + 2×SFP 全口 PoE+** 的型号；② 固件能否做**逐口 traffic shaping + 突发缓冲**；③ 工厂是否愿意**送样到安卡拉做 EGM 测试**（费用/周期）。

---

## 6. 证据（28 源）与空白

**本轮 28 个来源**（按使用顺序）：
1. `isac.com.tr` 检索（DMO/K 码，无命中）
2. `dmo.gov.tr` 工业交换机检索（无直接命中，仅 4S/Bimel 旁证）
3. **`isac.com.tr` 首页**（计数器全套 + 三城市 + 26 品牌 + 3,503 产品 + 28,646 库存 + Industrial Ethernet Switch 子分类）
4. `gsl.com.tr/moxa-endustriyel-ethernet-switch.html`（Moxa 61850-3/EN50155/NEMA TS2 全线，r80 已录，本轮用于对照）
5. **`teslakom.com`**（品牌墙、Lantech 三条卖点）
6. **`teslakom.com/kurumsal`**（2013 成立、2019 Bilkent CyberPark AR-GE、地址电话）
7. **`teslakom.com/bize-ulasin`**（伊斯坦布尔 Demirkol Plaza 地址）
8. **`teslakom.com/markalar/lantech`**（**2016 年初起 Lantech 土耳其唯一授权经销商**、13 条产品线）
9. **`teslakom.com/altkategori/kgys-saha-switch-c-tipi`**（**`IPGS-3408GSFP-48V-E`** 全规格 + **EGM 测试通过**）
10. **`teslakom.com/altkategori/endustriyel-10g-switch`**、**`.../endustriyel-en50155-switch`**（10G / EN50155 / IP67-M12 产品线，PORTNOX NAC 品牌新增）
11. `lusha.com` Teslakom（11–50 人 · 2013）
12. `linkedin.com/company/teslakom-…`（11–50 人 · 1,404 followers）
13. `dmo.gov.tr/Arama?s=switch`（**SPA 仍不可枚举**，仅返回电刀类目）
14. `dmo.gov.tr/EMagaza/Magaza/Standart/1369`（**4S BİLİŞİM · 14 项 Cisco 交换设备 · 7,260–178,666 ₺**）
15. **`areskom.com.tr`**（2004 成立、Westermo/Teltonika/ETC/Acromag/Lanner/Atop/Sena/TEKTELIC、VAD 自述）
16. **`areskom.com.tr/kurumsal/iletisim/`**（Altunizade Kısıklı Cd. No:35/1 · 0216 428 78 78 · info@）
17. **`areskom.com.tr/markalar/westermo/…/endustriyel-iec-61850-3-switch/`**（**Lynx 5612-F4G-T8G-LV / Lynx 5612-F4G-T8G-LV L2/L3** 型号与规格）
18. `alo118.com` Areskom（旧址 **Muhittin Üstündağ Cad. No:23 Koşuyolu** · 1–10 人）
19. `endustri-dunyasi.com` Areskom（Koşuyolu 地址 + 传真 428 76 76）
20. **`eurasiarail.eu` 展商页**（**「与 WESTERMO 合作超过 16 年」**、EN 50155/EN 50121-4 铁路场景）
21. **`obc.com.tr/hizmetlerimiz/enerji-otomasyonu/dagitim-merkezleri/`**（IEC 61850 RTU/PMS、甩负荷、配电中心）
22. **`obc.com.tr/cozum-ortaklarimiz/`**（**SIEMENS + MOXA** 标志墙）
23. **`obc.com.tr/hizmetlerimiz/enerji-otomasyonu/`** + `viewlocate.com`（Onur Plaza No:3/13 · 0850 885 0064 · 0216 577 54 18）
24. **`4aelektrik.com.tr`**（**2005** 成立 · 60–750 kV · **IEC 61850 数字变电站** · FAT/SAT · 自有屏柜）
25. **`4aelektrik.com.tr/iletisim-2/`** + `alo118`（Girne Mah. Irmaklar Sk. No:C-13 Maltepe · 0216 366 38 28 · info@）
26. **`teleteknik.com.tr/iletisim/`** + `teleteknik.com.tr/rtu-ve-telemetri-cozumleri/`（Pendik Sweet Life Center A79 · 0216 482 92 47 · TAIS T800 RTU · IEC 61850 集成）
27. **`turk-iot.com/cryptolink-switch-kgys-projesi-ozelinde-…`**（**C-Tipi 全条款 1.1.1–1.1.26**、**已有 BAŞARILI 报告的四品牌**、**CRLISW-8P = DIS300 = ISW 8GbP 4-SFP 同固件 · 192.168.2.1 · admin/admin**）
28. **`austurkiye.org.tr` 会员页** + `dnb.com` + `bloomberg.com` + `pitchbook.com`（**Proline：2003 · 105 人 · Serdal KARAKAŞ · Beyan Sk. No:66 Ümraniye · 0216 528 6200 · Pasifik Teknoloji 子公司**）
29. **`rhaajans.com` / `borsatek.com` / `ekonomimanset.com`**（**KAP：Proline $6,645,000 + KDV · EGM 全国 KGYS 现代化 · 24 个月**）
30. **`linkedin.com/company/ggs-bilişim-teknolojileri`** + `zoominfo` + `rocketreach`（**GGS：2005 · Ostim 50 m² 起家 · ⚠人数三口径冲突**）
31. **`ggsbilisim.com/kgys.php`**（Ankara/İstanbul/İzmir/Trabzon/Mersin/Denizli · 20 年）
32. **`netmon.com.tr`** + `kariyer.net` + `linkedin` + `anadoluraylisistemler.org`（**Netmon：1998 Netaş 安装组外包 · 126 人 · Dumlupınar Cd. No:28 Sincan · Top500 ICT 第 14**）
33. **`eibabo.us` / `tradeinn.com` / `cplonline.com.au` / `megaofficesupplies.com.au` / `compaqs.com`**（**D-Link `DIS-300G-8PSW` $1,132–1,262 / AUD 2,507–3,107**）
34. **`businessensotech.com`**（**Lantech 泰国价目：`IPGS-3208GSFP-48V` 35,443 THB · `IPGS-3408GSFP-48V` 39,278.25 THB**）
35. **`pamukteknoloji.com.tr`**（Allied Telesis 美元价目：`AT-GS950/10PS` $496.1 · `AT-GS980M/52` $3,000）
36. **`ls-elektrik.com.tr/bayiler/`** + `tiootomasyon.com`（**TİO OTOMASYON SAN. VE TİC. LTD. ŞTİ. · Erenler 1234. Sk. No:17 Sakarya · 0264 666 17 71**）
37. `ozhat.com` / `uniletisim.com`（**Allied Telesis 在土耳其无官方总代，仅灰色渠道** ⇒ 有意义的负面证据）

> 说明：上表为**去重后的来源条目**，检索与抓取共 **37 次**（≥ 上一轮 25 次的硬要求）。

**空白（不许补写）**
- **Teslakom 的 VKN / MERSİS / 成立月份**未得；`A.Ş.` 为 Lusha/LinkedIn 口径，未与 MERSİS 核对。
- **Proline 的 VKN / MERSİS** 未得；`Serdal KARAKAŞ（CEO）` 来自行业协会会员页，**未与 KAP 公告或官网核对**；D&B 另记 Alparslan Cemail Batuk，**两者职位关系不明**。
- **Areskom 现址与旧址并存未解**（官网 Üsküdar vs 名录 Kadıköy）；人数 1–10 明显低估。
- **GGS 人数 3 / 324 / 201–500 三口径冲突**，**不引具体数**。
- **Netmon 126 人**来自 kariyer.net 招聘页自述，LinkedIn 记 51–200，**以区间表述**。
- **EGM 已发报告的品牌清单**只有 turk-iot.com 一处**二手**披露（2023-12），**未从 EGM 官方或招标文件核实**；是否已新增品牌不明。
- **CryptoLink = D-Link/Extreme 同平台**是**基于固件界面与默认凭据的推断**，非拆机/商标证据。
- **KGYS 年全国采购台数**无公开数据 ⇒ **不给市场规模数字**。
- **我方是否有 8×1G+2×SFP 全口 PoE+ 型号**、**固件能否逐口整形**：**未确认**。
- **所有新电话未试拨**（Teslakom 0212 356 46 46 / 0312 472 99 67 · Proline 0216 528 62 00 · Areskom 0216 428 78 78 · GGS 0312 474 01 30 · Netmon 0312 385 86 00 · OBC 0216 577 54 18 · 4A 0216 366 38 28 · Teleteknik 0216 482 92 47 · TİO 0264 666 17 71）。

---

## 7. r83 建议（按投入产出排序）

1. 🔥 **给 CryptoLink 打电话，换话题**：不问「要不要买交换机」，问「**你的 `CRLISW-8P` 的 EGM 报告挂在哪个型号上？能不能挂在我的型号上？**」——这是**全轮最便宜的一条路径**：它已有票、已有 KGYS 场景、已是我们客户。
2. 🔥 **打 Proline（0216 528 62 00）找 Serdal KARAKAŞ**：开口就报「**我知道你 9 月签了 $6.645M 的全国 KGYS 现代化，24 个月**」，然后只问一句「现场 C 型机台现在挂谁的牌」。
3. 🔥 **打 Teslakom（0312 472 99 67，安卡拉 R&D）**：它是唯一「单硬件品牌 + 想做国产」的公司，问「**Lantech 之外，你的 KGYS 报价有没有第二条成本线**」。
4. ⭐ **向工厂发一页纸问三件事**：8×1G+2×SFP 全口 PoE+ 型号有吗？固件能否逐口整形 + 200 Kbit 突发？愿不愿送样做 EGM 测试（**周期/费用**）？—— **这一页纸决定 KGYS 这条线能不能开**。
5. ⭐ **Areskom / 4A / OBC 三家，只问一个问题**：「**没有 61850-3 第三方报告，你的客户在工厂/水厂/园区会不会接受？**」——答案就是「要不要花钱做认证」的决策依据。
6. 🕐 **补缺口**：Teslakom / Proline / Areskom 的 VKN·MERSİS；EGM 已批品牌的最新清单（试 `ihale.gov.tr` / EKAP 关键词「C Tipi Kenar Anahtar」）。
7. 🕐 **承接旧债**：`RS-IS-400-16GPTX` 是否有 61850 · PLANET `IGS-1000` 是否在册 · `G5328P-24-410W` $240 复核 · Karer/CryptoLink/Novacom 的 VKN（**四轮未命中**）。

---

*本文件为 r82 交付。所有价格均标来源与抓取日；所有推断均标「推断」；所有未核实姓名与数字均标 ⚠。*
