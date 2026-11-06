# -*- coding: utf-8 -*-
"""r82 附录数据：KGYS「C 型边缘交换机」市场 + 五家新渠道线索 + İSAC 修正。"""

D = {}

D['63'] = """
#### r82 总览：**KGYS 是 8 口工业 PoE 的全国性市场，门票是 EGM 一张测试报告；五家新渠道线索落地**

**① 🔥🔥🔥 KGYS = 土耳其 8 口工业 PoE 的国家级需求源**
- **KGYS = Kent Güvenlik Yönetimi Sistemi**（民间俗称 **MOBESE**），**EGM（警察总局）** 主导、**ASELSAN / ASELSANNET** 承接，覆盖 81 省 + 北塞。
- 物理形态：**街道立杆下面的现场机柜，每个点位一台工业交换机，汇 8 路摄像头（每路 ≤5 Mbps，合计 ≤40 Mbps）进光纤环网** ⇒ **8 口 = 这个国家的标准单元**。
- 规格书里这台设备叫 **「C TİPİ ETHERNET ANAHTAR」**，且明写「**该交换机可以与其他交换机不同品牌**」⇒ **单点替换是规则允许的**。

**② 🔥🔥🔥 规格书 1.1.26 = 唯一的硬门槛**
> 必须持有 **EGM 信息技术与通信部（Emniyet Genel Müdürlüğü Bilgi Teknolojileri ve Haberleşme Daire Başkanlığı）** 签发的、结果 **「BAŞARILI」** 的 **《C-Tipi Kenar Anahtar ve Traffic Shaping Test Report》**，随标提交；以往以「Haberleşme Daire Başkanlığı」名义签发的旧报告同样有效。

**⇒ 这是「品牌 + 型号 + 固件」三者绑定的国家级准入证。**

**③ ⭐⭐⭐ 已有这张纸的只有 4 个牌子**
| 品牌 | KGYS 型号 | 备注 |
|---|---|---|
| **Extreme Networks** | **`ISW 8GbP, 4-SFP`** | — |
| **Allied Telesis** | —（型号未披露） | **土耳其无官方总代**，仅灰色渠道（`ozhat.com` 自述「非官方分销商」） |
| **CryptoLink** | **`CRLISW-8P`** | **我们已有的客户** |
| **D-Link** | **`DIS300`** 系列 | 8PSW 只有 4 个 PoE 口，**不满足 1.1.21 每口 PoE** ⇒ KGYS 用应是该系列全 PoE 变体 |

**④ ⭐⭐⭐ 结构发现（推断，非确认）：`CRLISW-8P` ≈ D-Link `DIS300` ≈ Extreme `ISW 8GbP 4-SFP`**
- 三者**使用同一套固件界面**：默认 IP **`192.168.2.1`**、账号 **`admin/admin`**、系统信息页同款布局、配置步骤一字不差（来源：`turk-iot.com` 2023-12 技术文，含截图）。
- ⇒ **极可能同一台湾 ODM 参考设计，CryptoLink 是本地贴牌商，不是自研厂。**
- ⇒ **战略含义**：CryptoLink **不是要不要说服的新人，而是能替我方把型号带进 KGYS 标书的现成通道**（它已有票、已有场景、已是我们客户）。**r80「对 CryptoLink 谈边境/车牌环网」依然成立，但优先级上调。**

**⑤ ⭐⭐ KGYS 规格 19 条（1.1.1–1.1.26 摘要，供工厂逐条对照）**
- 工业型 · **−40~+60 ℃** · 湿度 10–95% · **无风扇** · **≥IP20** · 告警继电器 · 环网/Mesh 冗余（断纤/断机不中断）
- **≥8 个千兆电口 + ≥2 个千兆光口**（SFP 可 70 km，LX/SX/ZX/100BASE-X；随设备带 1 支同品牌 10 km 1000Base-LX SFP + 每支 SFP 配 1 m 跳线）
- 全端口 **non-blocking** · **≥8,000 MAC** · **≥4 个优先级队列** · **RMON + SNMP v1/v2/v3** · telnet/console/web
- **IGMP snooping** · **802.1Q VLAN / MSTP(802.1s) / x-ring 或同类 / VLAN trunking** · **802.1p + ToS** · MAC 端口安全 · **802.1x** · 端口镜像 · **LACP 802.3ad** · **IPv6** · 授权随设备不另购
- **1.1.21：每一个端口都要 802.3af 与 802.3at（PoE/PoE+）**
- **1.1.25：每物理端口（含 SFP）可独立 traffic shaping**——40 Mbps 总量下 **丢包 ≤0.5%**、**整形延迟 ≤0.5 s**、能吸收 **≥200 Kbit 突发**（软/硬件 buffer）；**不得另配整形设备**

**⑥ ⭐⭐ KGYS 这一档的在位价格 = $1,100–1,300（本轮新增锚点）**
| 型号 | 关键规格 | 价格 | 来源 | 折算 |
|---|---|---|---|---|
| **D-Link `DIS-300G-8PSW`** | 6×1G + 2 SFP + **4 PoE+** / 120 W / IP30 / 16 Gbps / 8K MAC / 无风扇 | **$1,132.22** · **$1,261.99** | eibabo.us · tradeinn.com | **$1,130–1,260** |
| 同上（澳/新） | — | AUD 2,507 · AUD 3,107 · SGD 3,142 | cplonline · megaofficesupplies · compaqs | 佐证同带 |
| **Lantech `IPGS-3208GSFP-48V`** | 8×1G + 2 SFP，8 口 PoE 30 W，−20~60 ℃ | **35,443.00 THB** | businessensotech.com（泰国代理价目） | **≈$1,090**（汇率假设 ⚠） |
| **Lantech `IPGS-3408GSFP-48V`** | 8×1G PoE at/af 30 W + 4 SFP，−40~75 ℃ | **39,278.25 THB** | 同上 | **≈$1,205**（同上 ⚠） |
| **Allied `AT-GS950/10PS`** | 8 口 PoE 智能管理 | **$496.1 + KDV** | pamukteknoloji.com.tr | 非全 PoE 的 8 口在 $500 档 |
| **Allied `AT-GS980M/52`** | 48 口管理型 | **$3,000 + KDV** | 同上 | 48 口锚点 |
⇒ **KGYS 现场档与 RUBISEC `IS-300-12GPX` $1,221 完全重合 ⇒ 这不是巧合，是这一档的国际市价。我方 $380（DAHUA）/ $500–700 目标档在其下方 2–3 倍。**

**⑦ 五家新渠道线索总表**
| 线索 | 类型 | 关键数据 | 分级 | 优先级 |
|---|---|---|---|---|
| **Teslakom** | **单一硬件品牌的独家代理** | **TESLAKOM BİLİŞİM VE TELEKOMÜNİKASYON A.Ş. · 2013 · 11–50 人 · 2019 年 Ankara Bilkent CyberPark AR-GE · 0212 356 46 46 · 0312 472 99 67** · **Lantech 土耳其唯一授权经销商（2016 年初起）** · 8 品牌中**只有 1 个是硬件网络** · 官网自述要把「土耳其工程师 + 本土生产能力」结合 | **A- / 76** | ① |
| **Proline Bilişim** | **正在执行 $6.645M KGYS 合同** | **PROLINE BİLİŞİM SİSTEMLERİ VE TİCARET A.Ş. · 2003 · ≈105 人 · Şerifali Mah. Beyan Sk. No:66 Ümraniye · 0216 528 62 00 · CEO Serdal KARAKAŞ ⚠** · **Pasifik Teknoloji（PATEK）子公司** · **2026-09-23 KAP：EGM 全国 KGYS 现代化 + PTS 基础设施，$6,645,000 + KDV，24 个月** | **A- / 75** | ② |
| **Areskom** | **纯工业网络 VAD** | **ARESKOM İLETİŞİM SİSTEMLERİ TİC. LTD. ŞTİ. · 2004 · Altunizade Kısıklı Cd. No:35/1 Üsküdar · 0216 428 78 78** · **Westermo 合作「超过 16 年」** · Westermo / Teltonika / ETC / Acromag / Lanner / Atop / Sena / TEKTELIC · 代理 **Lynx 5612-F4G-T8G-LV（IEC 61850-3 变电站）** | **B+ / 71** | ③ |
| **GGS Bilişim** | 省会级 KGYS 集成商 | **GGS BİLİŞİM TEKNOLOJİLERİ A.Ş. · 2005（Ostim 50 m² 起家）· Batıkent Gersan 2307/2 Sk. No:11 Ankara · 0312 474 01 30** · **6 省 KGYS**（Ankara/İstanbul/İzmir/Trabzon/Mersin/Denizli）· ⚠ 人数三口径冲突（3 / 324 / 201–500）**不引具体数** | **B / 68** | ④ |
| **Ankara Netmon** | 电信工程 + KGYS 现场施工 | **ANKARA NETMON İLETİŞİM SİSTEMLERİ TİCARET VE SANAYİ A.Ş. · 1998（Netaş 安装组外包，15 人起）· 126 人 · Dumlupınar Cd. No:28 Maliköy Anadolu OSB Sincan/Ankara · 0312 385 86 00** · **ICT 500 强第 14 位（自述）** · KGYS/PTS（SSB + ASELSAN）+ 铁路信号 + 5G 国产化 | **B / 66** | ⑤ |

**⑧ 电力 / 盘厂线四家（B 档）**
| 公司 | 法定名 | 关键数据 | 与我方关系 |
|---|---|---|---|
| **OBC** | **OBC BİLGİSAYAR HİZMETLERİ SAN. TİC. LTD. ŞTİ.** | Onur Plaza No:3/13 Küçükbakkalköy Ataşehir · 0850 885 0064 · 0216 577 54 18 | 能源自动化（甩负荷/配电中心/控制中心）· **方案伙伴 = SIEMENS + MOXA** ⇒ Moxa 太贵，需 $500–700 二线 |
| **4A Elektrik** | **4A ELEKTRİK ELEKTRONİK TEKNOLOJİ SAN. A.Ş.** ⚠ 一处名录记 Ltd. | **2005** · Girne Mah. Irmaklar Sk. No:C-13 Maltepe · **0216 366 38 28** | **60–750 kV 输电 + IEC 61850 全数字变电站** + 自有屏柜 ⇒ **没 61850-3 报告进不去** |
| **Teleteknik** | **TELETEKNİK KONTROL VE GÜÇ SİSTEMLERİ SAN. TİC. LTD. ŞTİ.** | Sweet Life Center No:6 A79 Pendik · **0216 482 92 47** | **RTU/计量屏制造**（TAIS T800）⇒ 屏内要 4–8 口交换机，**正对我方 4–8 口那一端** |
| **TİO Otomasyon** | **TİO OTOMASYON SANAYİ VE TİCARİ LİMİTED ŞİRKETİ** | Erenler 1234. Sk. No:17 **Sakarya** · **0264 666 17 71** · LS Electric 萨卡里亚授权经销 | 区域经销商（LS/Pilz/Moxa/Autonics/SMC/TE）⇒ **C+ / 55**，量小 |

**⑨ ⚠ 修正 r81：İSAC 的计数与城市**
- r81 记「工业自动化 **9,707** / 传感器 **19,543**」。**r82 首页实时计数器（2026-11-06）**：**SENSÖR 19,452 · ENDÜSTRİYEL OTOMASYON 9,725** · KONTROL-PANO 4,781 · SAFETY 2,457 · PLC 2,734 · KABLO 1,984 · ELEKTRİKMEKANİK 1,889 · HİDROLİK 840 · BAĞLANTI 213 · ELEKTRONİK 69 ⇒ **合计 ≈38,144 条目录条目**。
  - **这些计数是按天变的活计数器 ⇒ 今后引用必须带日期；且不得把「9,725 条目录条目」说成「9,725 个现货 SKU」。**
  - 首页另有一套口径：「**代理之外还供 26 个品牌**」「**3,503 个产品**」「**28,646 件库存**」—— **不同区块，不可与分类计数相加或混用（r81 未区分，此处更正）**。
- **办公室**：r81 依招聘站记「布尔萨 + 盖布泽」；**官网首页写 İstanbul / Bursa / İzmir 三地** ⇒ **补 İzmir，盖布泽降级为「招聘口径，官网未确认」**。

**⑩ ⭐ 新增（r81 未发现）：İSAC 的质量方针里写着「做自己的品牌」**
- `isac.com.tr/kalite-politikasi/` 原文要点：**「在生产中创造我们自己的企业品牌是我们的目标；为此 ISAC 的目标包括进入生产并最正确地管理制造过程。」**
- ⇒ **İSAC 要的不是第 N 个代理品牌，而是 OEM / 贴牌供应商。**
- ⇒ **取代 r81 对 İSAC 的「补一格」话术**，升级为：**「帮你把自有品牌的第一台工业交换机做出来」**。
- 旁证：首页有独立的 **Industrial Ethernet Switch** 子分类（在 9,725 条之内，归在 ENDÜSTRİYEL OTOMASYON 下），说明**这条线存在但没有品牌纵深**。

**⑪ 渠道三分法：门票决定话术，话术决定价格档**
| 类型 | 代表 | 门票 | 一句话话术 | 价格档 |
|---|---|---|---|---|
| **A. DMO 目录商 / 目录+副线** | İNFOGEN · İSAC · RİVO | 无（只要 K 码 + 开票能力） | 「补你目录里缺的那一格」/「帮你做自有品牌第一台」 | $139–700 |
| **B. KGYS / 城市安全集成商** | **Proline · GGS · Netmon · CryptoLink · Teslakom** | **EGM C-Tipi 测试报告** | 「你 KGYS 包里现场机台现在挂谁的牌？我给你第二条成本线」 | **$500–700（对标 $1,100–1,300）** |
| **C. 工业网络 VAD / 电力 EPC** | Areskom · OBC · 4A · Teleteknik · GSL · ErETE · Simgenet | **IEC 61850-3 / IEEE 1613 报告** | 「无 61850 的工厂/水厂/园区，我给你 1/3 价」 | $380–700 |
⇒ **没有门票就不要去打变电站主标和 KGYS 主标**；只打「无认证要求的场景 + 二供」。

**⑫ 我方 vs KGYS 逐条自评（须工厂确认）**
| 条款 | 我方现状 | 判断 |
|---|---|---|
| 工业型 / −40~60 ℃ / 无风扇 / IP20 | 宽温无风扇机型 | ✅ 需 datasheet 逐条核 |
| 告警继电器 | 未确认 | ⚠ |
| 环网冗余（G.8032 / x-ring） | 有 ERPS 类 | ✅ 需说明「或同类」 |
| **≥8 千兆电口 + ≥2 千兆光口** | 须确认是否有 **8×1G + 2×SFP** 的 PoE 型号 | ⚠ **关键：若只有 8 电口无光口，直接不合格** |
| ≥8,000 MAC / ≥4 队列 / SNMP v1v2v3 / RMON | 通常满足 | ✅ |
| **每口 PoE af + at** | 未确认是否全口 PoE+ | ⚠ |
| **逐口 traffic shaping（丢包 ≤0.5% / 延迟 ≤0.5 s / 200 Kbit 突发）** | 未实测 | ⚠ **EGM 报告的核心测试项** |
| **EGM C-Tipi 测试报告 BAŞARILI** | **无** | ❌ **唯一硬门槛** |

**证据等级**：`turk-iot.com/cryptolink-switch-kgys-projesi-ozelinde-konfigurasyonuvlanigmp-snooping-traffic-shaping-v-b/`（**C-Tipi 全条款 1.1.1–1.1.26 + 四品牌 BAŞARILI 报告 + 同固件证据 192.168.2.1 / admin-admin**）· `teslakom.com` 全站（`/kurumsal` `/bize-ulasin` `/markalar/lantech` `/altkategori/kgys-saha-switch-c-tipi` `/altkategori/endustriyel-10g-switch` `/altkategori/endustriyel-en50155-switch`）· `lusha.com` · `linkedin.com/company/teslakom-…` · `areskom.com.tr` + `/kurumsal/iletisim/` + `/markalar/westermo/.../endustriyel-iec-61850-3-switch/` · `alo118.com`（Areskom 旧址）· `endustri-dunyasi.com` · `eurasiarail.eu`（**Westermo 16 年**）· `obc.com.tr`（`/hizmetlerimiz/enerji-otomasyonu/*` · `/cozum-ortaklarimiz/`）· `viewlocate.com`（OBC）· `4aelektrik.com.tr` + `/iletisim-2/` + `4A-lr-111.pdf` · `teleteknik.com.tr`（`/iletisim/` · `/rtu-ve-telemetri-cozumleri/` · `/enerji-analizorleri/`）· `austurkiye.org.tr/users/uye/248` · `dnb.com` · `bloomberg.com` · `pitchbook.com`（**Proline**）· `rhaajans.com` · `borsatek.com` · `ekonomimanset.com` · `ticarihayat.com`（**KAP $6.645M**）· `ggsbilisim.com/kgys.php` · `linkedin.com/company/ggs-bilişim-teknolojileri` · `zoominfo.com` · `rocketreach.co`（GGS）· `netmon.com.tr` · `kariyer.net/firma-profil/ankara-netmon-a-s-43505-38035` · `linkedin.com/company/ankara-netmon-a-` · `anadoluraylisistemler.org`（Netmon）· `ls-elektrik.com.tr/bayiler/` · `tiootomasyon.com`（TİO）· `pamukteknoloji.com.tr/tr/allied-telesis/` · `ozhat.com`（Allied 在土无官方总代）· `eibabo.us` · `tradeinn.com` · `cplonline.com.au` · `megaofficesupplies.com.au` · `compaqs.com`（**D-Link DIS-300G-8PSW**）· `businessensotech.com`（**Lantech 泰国价目**）· `cyberworld.hk` · `lantechcom.tw`（Lantech 型号谱）· `www.dmo.gov.tr/Arama?s=switch`（仍 SPA）· `www.dmo.gov.tr/EMagaza/Magaza/Standart/1369`（4S Bilişim 14 项 Cisco）· `isac.com.tr`（首页计数器 / `kalite-politikasi`）· `gsl.com.tr/moxa-endustriyel-ethernet-switch.html`（Moxa 61850-3 对照）—— **去重后 37 个来源（≥ r81 的 25）**。

**空白**：**Teslakom / Proline / Areskom 的 VKN · MERSİS 全缺**（Proline 的 `Serdal KARAKAŞ（CEO）` 仅来自行业协会页，D&B 另记 Alparslan Cemail Batuk，**职位关系不明**）· **Areskom 现址（Üsküdar）与旧址（Koşuyolu）并存未解**，人数 1–10 明显低估 · **GGS 人数三口径冲突（3 / 324 / 201–500）不引具体数** · **Netmon 126 人来自招聘页自述**，LinkedIn 记 51–200 ⇒ 只用区间 · **EGM 已批品牌清单只有 turk-iot.com 一处二手披露（2023-12）**，未从 EGM 官方或标书核实，是否已新增品牌不明 · **`CRLISW-8P` = D-Link/Extreme 同平台是推断**（固件界面 + 默认凭据），非拆机/商标证据 · **KGYS 年全国采购台数无公开数据 ⇒ 不给市场规模数字** · **我方是否有 8×1G+2×SFP 全口 PoE+ 型号、固件能否逐口整形：未确认** · **所有新电话未试拨**（Teslakom 0212 356 46 46 / 0312 472 99 67 · Proline 0216 528 62 00 · Areskom 0216 428 78 78 · GGS 0312 474 01 30 · Netmon 0312 385 86 00 · OBC 0216 577 54 18 · 4A 0216 366 38 28 · Teleteknik 0216 482 92 47 · TİO 0264 666 17 71）。
"""
