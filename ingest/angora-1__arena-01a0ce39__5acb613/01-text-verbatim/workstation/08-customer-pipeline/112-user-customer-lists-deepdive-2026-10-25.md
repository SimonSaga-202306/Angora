# 112 · 用户两份客户名单深挖与跟进优先级（2026-10-25，第 37 轮）

来源：main 根目录 `Turkey Client List.xlsx`（299 行原始名单）+ `AI客户评估_TR 10.06.xlsx`（master No.1-50 双 AI 评估，10-06 版）+ **`2025土耳其ISAF客户.xlsx`（ISAF 2025 展会现场接待，4 sheet 去重 98 条）**。
全量逐字底稿：`99-raw/r37-ai-kehu-eval-master.tsv`（64KB）/ `99-raw/r37-turkey-client-list-299.tsv` / `99-raw/r37-user-customer-lists-2026-10-25.md`（分析+深挖 11 家）。
交叉比对：50 评估家中 **26 家在库**（111 行 1-23 共 25 家 + 110 行 20 Entegron；备注增量本轮落），**24 家新入 111 行 56-79**；ISAF 2025 展会 **66 家新入 111 行 80-145**（非土 13 条留档不入场）。

## 一、跟进优先级总表（回答「哪些能跟进」）

### Tier 1 ⭐ 立即跟进（7 家，全部在库 + 本轮 web 验证）
| 客户 | 双评 | 跟进钩子（verified） | 我方打法 | 产品线 | 联系人 |
|------|------|---------------------|---------|--------|--------|
| **NovaCom**（111 #2） | 40A/30B | 31 SKU 自有 NVC/NCV/ND PoE 线在售，**NCV-HIF2421GBL-C 2026-01 上新=持续采购中**；评估明示「正积极寻找工业 switch 供应商」 | 工业线切入（商业线已有源）：工业 PoE 完整线+OEM，报价对 E-wind/新桥 | 工业 PoE 8/16 口+ERPS | 库内既有 |
| **Snexus**（111 #3） | 35A/**50A** | Wix 站新宣称 **L3 硬件路由 RIP/OSPF/BGP**（r19 时仅 L2 品牌）=产品线升级中；自有 logo 商业+工业 switch | L2+→L3 升级配套：L2+ PoE 完整 model list+L3 方案（我方 CENTEC 补 L3）+OEM 全套（logo/UI/包装） | 商业 PoE 8/16/24+L2+/L3 | **90 53340 48364**（TCL 新得）+info@snexus.com.tr |
| **OPAX**（111 #20） | 30A/40A | OPAX-08120W=8+2 口 120W **$35/1,750TL 2 年保**（HRUI 贴牌同源型）=OEM 成熟、价格锚已知 | 替换+升级：同价段多型号（100M→GbE）+GB 系列+OEM 全套；2 年保口径对齐 | 商业 PoE 8/16/24（100M+GbE）+工业 PoE | opax.com 站联 |
| **CryptoLink**（111 #5） | 35A/35B | 自有 CRL 系全列（**CRLISW-08/14P 工业 + 24 口 L3 10G + CRL-MC02 + SFP-10G-LC**）+ **KGYS 警队项目现场在用实证**（VLAN/IGMP/traffic shaping） | 工业 L3 升级：L3 10G 核心方案（我方 STH 系/Marvell NPB 带）+ERPS+工业 PoE 补型号；KGYS 口径（公安联网） | 工业 L3 10G+工业 PoE+SFP | **+90 312 557 64 00**（本轮新得）/info@cryptolink.com.tr |
| **Telkolink+GelecekBT**（111 #1） | 38A/35B | 同集团双入口：Telkolink=三旺/TG-NET/CLR 多源+贴自有 logo（外观一般=品质升级空间）；GelecekBT=HRUI 工业 | 双品牌替换：商业 PoE（对 CLR/TG-NET）+工业 PoE（对 HRUI/三旺）+OEM 全套；强调 model list 覆盖+管理界面定制 | 商业 PoE+工业 PoE+ERPS | info@telkolink.com |
| **Entegron / LONGLINE**（110 #20） | 30A/45A | ⭐双品牌同一母公司（LONGLINE 2000 起 Bayrampaşa）：Entegron 线=Ethernet 11/**PoE 31**/EPON ONU 9/GPON ONU 6；兴趣=PON switch+PoE+商业（有 E-wind） | 双入口报价：LONGLINE 渠道（商业+工业，对 E-wind）+Entegron OEM（PoE 31 型替换/扩型）+PON 邻接 | 商业/工业 PoE+L2 managed 8-28 口+（PON 留档） | info@entegronnetwork.com |
| **Cenova**（111 #4） | 30A/40A | 自有 CCTV 品牌+在售 **E-wind PoE/工业 switch 实页**（dl-end3308pfg）；CCTV 为主营 | E-wind 替换：CCTV 场景 PoE（IGMP Snooping+PoE++ 长距+稳定）+OEM 贴 Cenova | 商业 PoE 8/16/24+CCTV 专用 | info@cenova.com.tr |

### Tier 2 ⭐ 暖渠道跟进（5 家，面见/老板级联系人）
| 客户 | 双评 | 钩子 | 打法 | 联系人（本轮新得/核验） |
|------|------|------|------|------------------------|
| **Optima / Optima Engineering**（111 #56 新） | 28A/5C | ⭐**IFSEC 2023 面见 + 计划来深圳采购 + 曾受邀参观**（最暖线）；实为物理安防制造商（安卡拉 Sincan 厂，Perpa 销售办）=LPR/停车/闸机场景 PoE 需求 | 厂访接待+LPR 场景 PoE 方案（8 口 120W 带+长距）+OEM「Optima」贴牌 | **Furkan Kalkan 技术经理 90507 463 0566 / furkan@optima.tc**；Perpa 办 +90 212 210 70 00 |
| **Filiz Güvenlik**（111 #57 新） | 22B/5C | ⭐**迪拜展面见**+25 年（1994 伊兹密尔）+51-200 人+土首批 7/24 报警监控中心（自有监控中心=switch 采购主体） | CCTV 场景 PoE+报警中心汇聚；用已有关系推进 | **Sadik Yildiz（Ali 员工）M90533 74 63788**；+90 232 441 71 74 / info@filizguvenlik.com.tr |
| **Okisan**（111 #58 新） | 18B/20C | ⭐**Tiandy+Dahua 土耳其授权分销商**（dahuasecurity 分销商页实证）+5,000+ 经销网络+$8.6M+1986 起；商业 PoE 现用丰润达（深圳） | 丰润达替换/第二供应商：商业 PoE 完整线（绑定其 Dahua/Tiandy 摄像头出货）+OEM | **444 1 309 / (0212) 320 28 20 / okisan@okisan.com**（Okisan Plaza Şişli） |
| **Karer Güvenlik**（111 #7） | 18B/40A | 自有 KARER 品牌 PoE Switch 4/8/16/24 口（深圳 OEM，自组 NVR）=品牌方直接 | KARER OEM 全套（logo/UI/包装）+NVR 配套 PoE；老板直联 | **Nurbaki Karatas（老板）** / info@karerguvenlik.com |
| **CCTV Depo**（111 #21） | 15B/25B | 2004 起 51-200 人「土首个 B2B 安防平台」（Perpa）+ **2025 自有品牌 SECUZI**（CES 展）+IASF 2025 面见 | SECUZI 品牌 PoE OEM（新品牌=无固定源）+B2B 批发价 | **Can Gurcan CTO / Asuman Ozuedogru**（IASF 面见）/ can@cctvdepo.com |

### Tier 3 监控/低优先（14 家，红灯黄灯绑定或规模小，本轮已入 111 留档）
MFD（Siemens SCALANCE 红灯深度绑定=**不跟进**）/ Bimel（Planet+Ruijie 黄灯+Cisco 红灯，仅 DPTEK 工业类目有缝隙）/ Areskom（CTS 黄灯）/ Teamon（Planet）/ İntenet（Raisecom）/ Dacel（自动化边缘）/ Fiberden（光纤边缘）/ BaburTech（海思零售）/ TekmarShop（多品牌电商）/ İnovatech（CCTV 服务）/ Kiracı=ZKR Kıraç 集团（跳转站，待实主体）/ RadioTeknoloji（IASF 2022 老线，页面无法验证）/ Egemenelektronik（比价电商，WhatsApp 已加=低成本推 PoE 款）/ Metcom（品类广小单）。
次级（绿灯供应商替换窗口，B 级监控）：GMT Control（Uotek 贴牌）/ Cebeci Grup（ONV，「有国内的」）/ TeknolojiPazar（Freelink 疑自有+HRUI，伊兹密尔）/ LeMax（自有 LG 前缀=新桥贴牌，OEM 经验）/ Öncü Güvenlik（111 #9，丰润达+Utepo 双绿灯，35A/30B 已有档案）/ Hane Elektronik（111 #8，Milesight 土唯一授权=绿灯，35B）。

### 战略留档（非客户）
- **Pavotek（TCL #5）= Pavo Group 电子/嵌入式子公司确认**（导航全链 pavo-group.com+同批新闻流）：军通网络/ avionics/电源/IoT；联系人 Gizem KIZILTAN。=110 行 1（PNetworks 母集团）监控线扩展，**非跟进客户**。
- **ErETE（111 #10）+ Kiracı（新）均跳转 zkr.com.tr = Kıraç 集团**（土耳其大型安防集团 ZKR）→ 两行实为同一集团双入口，后续按 Kıraç 集团统一接触。

## 二、111 管线变更（本轮，+90 行 → 总计 145 行）
- **用户名单 24 新行（56-79）**：56 Optima / 57 Filiz / 58 Okisan / 59 PavoTek（战略留档）/ 60 GMT Control / 61 MFD / 62 Cebeci Grup / 63 Areskom / 64 İntenet / 65 Teamon / 66 İnovatech / 67 Metcom / 68 Egemenelektronik / 69 TeknolojiPazar / 70 TekmarShop / 71 BaburTech / 72 LeMax / 73 Kiracı=ZKR / 74 RadioTeknoloji / 75 TechnoPC / 76 Bimel / 77 Dacel / 78 Fiberden / 79 EuroCam。
- **ISAF 2025 展会 66 新行（80-145）**：A 级 12（80 Telemobil/81 Makros/82 HAFYA/83 SFP Turkey/84 ONSIS/85 Netmax/86 bilimsat/87 UGUR IMRE/88 ORAL/89 DE secure/90 canis/91 Sami CEUIK）+ A- 8（92 Selim Kalaka/93 HCS/94 KLASNET/95 F.A.S.T/96 voltec/97 LABOR/98 MEPA/99 viva bilgisayar）+ B/C 46（100-145）。
- **既有 23 行备注增量**（111 行 1-23）+ **110 行 1（PavoTek 关联）/行 20（Entegron=LONGLINE OEM）备注**：双评估分+新联系人+新供应链实证+ISAF 面见（逐行见 CSV/XLSX 备注 [r37] 标记）。
- ⚠️ **口径说明**：56-79 的 24 家 = r19 轮「排除 24 家」同一批，用户 10.06 双评估=重新定级（r12 只增不删，r19 留痕保留）；80-145 部分 = r21「16 无法核实」ISAF 线索的现场记录补全（Sami CEUIK 500 台/Selim Kalaka 郑州换源坐实）。

## 三、ISAF 2025 展会线（第三份名单，2026-10-25 用户上传）
现场接待 3 人（Evelyn/Ady/Simon）+ 合并表；去重唯一 98=TR 85+非土 13。逐家全量见 `99-raw/r37-isaf-2025-analysis-2026-10-25.md`。
### 3.1 立即跟进（A 级 12，已入 111 行 80-91）
1. **Telemobil**（行 80）：现场记录「可重点跟进，有具体项目」—2光2电 PoE 询价+问交期 → 发价格+交期
2. **Makros/DEMIREL**（81）：130/150USD 已报，要 DDP 双清包税
3. **HAFYA**（82）：⭐**军项目+防水 4光8电 PoE+grundig-security.tr 双域名**（与 111 行 8 Hane=Grundig 分销生态待核）
4. **SFP Turkey**（83）：Evelyn 既有客户，修图级深度服务+10G 光+bypass
5. **ONSIS**（84）：2光8 PoE 网管 bypass 105USD，**要样品**
6. **Netmax**（85）：2光8 PoE 管理 bypass 120USD
7. **bilimsat/KILIC**（86）：8光8电 PoE 110USD，「最近在找这种产品」
8. **UGUR IMRE**（87）：分销商（不需要 OEM），2光8 瑞昱 PoE+DC48V 70USD，回「Not bad」
9. **ORAL GUVENLIK**（88）：150/90USD 已报，**嫌贵**→替代档/折扣
10. **DE secure**（89）：工业 8 口 30W，要含 20% 关税报价
11. **canis/AHMET CAN**（90）：12光12电 PoE 150USD
12. **Sami CEUIK**（91）：⭐政府项目，**500 台**量 2光8 PoE 已报 80-90USD（r21 头号信号坐实）
### 3.2 A- 级（行 92-99）
⭐**92 Selim Kalaka**：郑州供应商拟在土耳其开厂→**找新供应商=换源窗口**（r21 信号坐实，最高优先）/ 93 HCS（问 L2/L3）/ 94 KLASNET（**问怎么成为分销商**）/ 95 F.A.S.T（工业 5 口+PLC/IO 代理）/ 96 voltec（工业 PoE 网管）/ 97 LABOR（要价格表）/ 98 MEPA（4/8/16/24 口全线）/ 99 viva bilgisayar（Hatay 老板直联）。
### 3.3 bypass 产品线专项（ISAF 最强产品信号，8 条明确需求）
IHM（独立式+2光8，SC 口不网管）/ Aycan CAM（2光8 PoE 管理 bypass 无 10G）/ BİLGEN（2光8 bypass+PoE 功率）/ ONSIS/Netmax/ORAL/Serkan/SFP Turkey → **下轮出 bypass 专刊+样品策略（STC-424DGGPM 系）**。
### 3.4 非土留档（13，r21 只留档）
Serbia×2/Bulgaria/Libya×3/Greece/Palestine×2/Ukraine/Tunisia/Kosovo/Iran + 0770 Syria；**eu.equinix.com=r22 不跟进**；Vatankhah=Tiandy 员工（关联 111 行 58）；Maipu 迈普=中国参展商（ONV 80USD 对位价情）。

## 四、299 名单后续
50 评估之外 **249 家**=后续批次池（在 `r37-turkey-client-list-299.tsv`）；建议按「有 Person+Contact 字段」优先（暖线信号），下一轮继续双评估或按 Tier 规则直接分池。本轮不逐家深挖（边界声明，宪法第十条数据已 100% 落库）。

## 五、边界
cenova.com.tr 直连代理故障 2 次（采信用户评估+r19 档案）/ 评估表行 51-300 与明细 sheet 1-300=空模板 / MFD=Siemens 红灯不跟进 / Bimel 工业页 DPTEK=搜索副产物（未深抓）/ 249 家后续池未评估。
ISAF xlsx 原始列错位（缺 Name/Position 行左移）已按邮箱锚定修复 / Sheet1 缺号=合并表删行 / 无邮箱行以微信/手机为唯一键 / HAFYA×Grundig 生态关系待核 / 「Alisa 客户」Alisa 身份未记录 / 非土 13 条不入场（r21）。
