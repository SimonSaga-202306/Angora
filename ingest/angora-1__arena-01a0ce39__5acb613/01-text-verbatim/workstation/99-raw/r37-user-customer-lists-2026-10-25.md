# r37 用户上传客户名单两份：全量入库 + 深挖（2026-10-25）

用户指令：「我在main上传了2个客户list 你读一下 深入挖掘一下这些客户 看看哪些能跟进啥的」
两份 list（均 origin/main 根目录）：
1. **`Turkey Client List.xlsx`**（Blob e69bb4b，c4085aa 即在库）= sheet「Turkey」**299 行×5 列**（Person / Interested in / Contact / Remark / Company）= 原始客户总名单。全量转录 = `99-raw/r37-turkey-client-list-299.tsv`（9.1KB）。
2. **`AI客户评估_TR 10.06.xlsx`**（6b28302，2026-10-25 11:36 上传，713KB）= sheet「总表」**300 行，仅 No.1-50 有双 AI 评估**（No. / Company / **AI评估结果**〔评分%+A/B/C 级+公司定性+建议动作+兴趣产品线+依据〕/ **CALUDE评估结果**〔第二 AI：评分%+等级+独立定性〕/ Country / Person / From〔渠道：迪拜展/IFSEC/IASF/谷歌/富通天下〕/ Interested in / Contact / Remark）+ No.51-300 空模板 + 明细 sheet 1-300=**空模板**（仅表头「跟进时间/跟进内容/客户回复/平台/备注」，无数据）。全量转录 = `99-raw/r37-ai-kehu-eval-master.tsv`（64KB 逐字）+ `99-raw/r37-ai-kehu-detail-sheets.tsv`（空模板记录）。
3. **`2025土耳其ISAF客户.xlsx`**（b754bd4，2026-10-25 用户上传，2MB）= ISAF 2025 展会现场接待 4 sheet（Sheet1 合并 51 条 + Evelyn 28 + Ady 29 + Simon 31；去重唯一 98 = TR 85 + 非土 13）。全量转录 = `99-raw/r37-isaf-2025-raw.tsv` + 分析 = `99-raw/r37-isaf-2025-analysis-2026-10-25.md`（A 级 12 家/非土留档 13/bypass 专项 6 条）。
※ 二进制 xlsx 不重复落仓（r27 最小占用；数据 100% 由 TSV 转录承载；原件在 origin/main）。

## 1. 交叉比对（50 家评估 vs 111/110 库）
**26 家已在库**（111 行 1-23 共 25 家：行 1 含 Telkolink+GelecekBT、行 11 含 EretEKNE+isee 两家/行 + 110 行 20 Entegron）；**24 家新** → 111 新增行 56-79（本轮）。
编号口径：**速览表 # = master 总表 No.1-50**（与 TCL 299 名单顺序不完全一致）；master 50 家中 **43 家在 TCL 299 内**（TCL #1-55 段 + #60 entegron），**7 家仅 master 有、不在 TCL**（rima #42 / radioteknoloji #43 / karer #45 / dacel #47 / fiberden #48 / cctvdepo #49 / eurocam #50）。
⭐**EuroCam = master No.50 有双评估**（AI 15B / CL「核心业务未确认，建议人工介入」），IASF 2021 面见 Gokhan DEMİR CEO，非「无评估」。
⭐**关键交叉发现：TCL #60 entegronnetwork.com = 110 行 20 LONGLINE 自有 OEM 品牌**（Claude 评估：母公司 LONGLINE Technology Ltd 2000 年成立 Bayrampaşa，Entegron=其中国 OEM 贴牌）→ 110 行 20 备注更新。
⭐**关键交叉发现：TCL #5 pavotek.com.tr = Pavo Group（= PNetworks 母集团，110 行 1）电子/嵌入式子公司确认**（pavotek.com.tr 导航全链 pavo-group.com，同批新闻 TWIF 2026-07-30 / Republikorp 2026-08-27）→ 110 行 1 备注更新。

## 2. 双评估 50 家速览（评分=AI/Claude；全量逐字见 r37-ai-kehu-eval-master.tsv）
| # | 公司 | AI | CL | 定性要点 | 渠道/联系人 | 库状态 |
|---|------|----|----|---------|------------|--------|
| 1 | iotsistem.com | 20B | 25B | IoT 方案商，managed switch 专区（Mlis/MLB 非主流） | Bosgem / info@iotsistem.com | 111 #18 |
| 2 | filizguvenlik.com.tr | 22B | 5C | 伊兹密尔 25 年安防（报警+CCTV+火灾），纯本地服务 | **Sadik Yildiz（Ali 员工）迪拜展面见 M905337463788** | 新 |
| 3 | snexus.com.tr | 35A | **50A** | 自有品牌商业+工业 switch 打自有 logo；⚠️现宣称 **L3 硬件路由 RIP/OSPF/BGP** | 90 53340 48364 | 111 #3 |
| 4 | gmtcontrol.com | 15B | 15C | 工控分销，少量 Uotek（深圳）贴自有 logo 工业 switch | Abdullah Aydin PM | 新 |
| 5 | pavotek.com.tr | 32A | 8C | ⭐=Pavo Group 子公司（电子/嵌入式/军通网络） | Gizem KIZILTAN | 110 #1 关联 |
| 6 | cenova.com.tr | 30A | 40A | CCTV 品牌商，在售 **E-wind**（深圳）PoE/工业 switch（dl-end3308pfg 实页） | info@cenova.com.tr | 111 #4 |
| 7 | cryptolink.com.tr | 35A | 35B | 安卡拉，自有 **CRL 系**（HRUI 贴牌）：CRLISW-08/14P 工业+**24 口 L3 10G**+MC+SFP | +90 312 557 64 00 | 111 #5 |
| 8 | mfd.com.tr | 15B | 8C | ⚠️西门子授权代理（SCALANCE 红灯，深度绑定） | Mustafa Cimic PM | 新 |
| 9 | eretekne.com | 22B | 30B | 在售 ONV（深圳）+XPS/Voscom 多品牌 | info@eretekne.com | 111 #11 |
| 10 | telkolink.com | **38A** | 30B | 深度绑定中国供应链：**三旺/TG-NET/CLR**+部分贴自有 logo；外观一般=品质升级空间 | info@telkolink.com | 111 #1 |
| 11 | Optima Soft / optima-engineering.com | 28A | 5C | ⚠️实为物理安防制造商（路障/防撞柱/车牌识别/闸机，安卡拉 Sincan 厂+Perpa 销售办）；IFSEC 2023 面见 | **Furkan Kalkan 技术经理 905074630566 furkan@optima.tc（计划来深圳）** | 新 |
| 12 | urunler.teleone.com.tr | 25B | 35B | 海关数据=Utepo（深圳）进口记录实锤 | — | 111 #22 |
| 13 | cebecigrup.com | 25B | 20C | 在售 ONV 工业 switch+串口设备，备注「有国内的」 | — | 新 |
| 14 | portel.com.tr | 22B | 25B | 采购三旺 3Onedata；邮箱域名 industrialnetworkcenter.com | — | 111 #16 |
| 15 | lansan.com.tr | 18B | 30B | MC+switch 打自有 logo | — | 111 #19 |
| 16 | okisan.com | 18B | 20C | ⭐**Tiandy+Dahua 土授权分销商**（dahuasecurity 分销商页），5000+ 经销网络，$8.6M，1986 起 | 444 1 309 / okisan@okisan.com | 新 |
| 17 | nfsteknoloji.com | 22B | 35B | PoE 配件+switch 采自 Utepo（深圳），CCTV 场景 | — | 111 #14 |
| 18 | rfteknoloji.com.tr | 22B | 30B | 工业交换机采自三旺，具体工业 PoE 产品页 | — | 111 #17 |
| 19 | areskom.com.tr | 15B | 20C | 代理台湾 CTS（黄灯）多品牌 | — | 新 |
| 20 | intenet.com.tr | 18B | 15C | 工业网络方案，代理 Raisecom（中国黄灯） | — | 新 |
| 21 | teamon.com.tr | 15B | 15C | 多品牌（Planet 台湾黄灯为主） | — | 新 |
| 22 | inovatech.com.tr | 18B | 5C | 安防/光纤/网络，IP CCTV 专区 | — | 新 |
| 23 | gelecekb.com | 35A | 35B | 在售 **HRUI（洪瑞）工业 switch**+光路 MC（与 #10 Telkolink 同集团） | — | 111 #1 |
| 24 | oncuguvenlik.com.tr | 35A | 30B | 安防分销，**丰润达+Utepo 双绿灯**工业/PoE/CCTV | — | 111 #9 |
| 25 | metcom.com.tr | 18B | 20B | PoE/CCTV 配件/机架/工业 MC 品类广 | — | 新 |
| 26 | egemenelektronik.com | 20B | 10C | CCTV 为主+商业 PoE，**WhatsApp 已添加** | — | 新 |
| 27 | teknolojipazar.com | 28A | 10C | Freelink（疑自有品牌）+HRUI 商业 PoE（伊兹密尔零售） | — | 新 |
| 28 | tekmarshop.com | 15B | 5C | 电商多品牌商业 PoE（=Asya Telekom 系/TEKMAR） | — | 新 |
| 29 | isee.com.tr | 18B | （同 #9 集团） | Asya Telekom 关联（Claude：与 eretekne 同集团 30B 结论） | — | 111 #11 |
| 30 | erete.com.tr | 28A | 5C | 自有品牌 XP 用 ONV（绿灯）+Etherwan（台湾黄灯）（⚠️跳转 zkr.com.tr=Kıraç 集团） | — | 111 #10 |
| 31 | coptek.com.tr | 30A | 25B | 在售 **DCN（中国）商业/工业**+ONV 工业+SFP+MC | — | 111 #6 |
| 32 | kiracbilisim.com.tr | 15B | 5C | 澳视摄像头+天地伟业认知（⚠️跳转 zkr.com.tr=Kıraç 集团） | — | 新 |
| 33 | kozaguvenlik.com.tr | 18B | 30B | **2023 CPSE 深圳安博会参展**，Deniz Aydin（技术经理）主动赴华采购 | — | 111 #15 |
| 34 | ccsguvenlik.com.tr | 25A | 30B | 在售 **HRUI** PoE switch 产品页 | — | 111 #12 |
| 35 | baburtech.com | 18B | 5C | switch 含海思（中国品牌）（安卡拉 IT 零售） | — | 新 |
| 36 | novacom.com.tr | **40A** | 30B | 自有 **NVC/NCV/ND 31 SKU PoE 线**（在售 E-wind 替换评估）；**正积极寻找工业 switch 供应商** | — | 111 #2 |
| 37 | lemaxguvenlik.com | 22A | 10C | 自有品牌（LG 前缀）PoE 源自**新桥（绿灯）**，有 OEM/重塑经验 | — | 新 |
| 38 | konakguvenlik.com.tr | 30A | 20B | 在售 **HRUI+丰润达 双绿灯** PoE；联系人 Erkut Sevin | — | 111 #23 |
| 39 | opax.com | 30A | 40A | 自有品牌 OPAX（HRUI 贴牌）完整产品页 | — | 111 #20 |
| 40 | technopc.com.tr | 18B | 10C | 本土 PC/工控机制造商（1998，74 人，$16.4M），采购 **E-wind 工业 PoE** | Mithat Yucel GM | 新 |
| 41 | haneelektronik.com | 25A | 35B | 商业 PoE 多外壳（疑 hisource）；⭐**Milesight（中国绿灯）土耳其唯一授权分销商**（2025 新增 Grundig Security+Panasonic） | info@haneelektronik.com | 111 #8 |
| 42 | rimaelektronik.com | 18B | 20B | 在售 Antaria 工业 switch（小众）；备注「网站适合推 Marvell」 | Salih Senyurt 销售总监 | 111 #13 |
| 43 | radioteknoloji.com.tr | 12B | 未确认 | IASF 2022 展接触（页面无法验证主营） | Salih Yildirim PM | 新 |
| 44 | entegronnetwork.com | 30A | **45A** | ⭐=LONGLINE 自有 OEM 品牌：Ethernet 11/**PoE 31**/EPON ONU 9/GPON ONU 6；L2 8/16/24/28 口+10G 8G+4SFP | info@entegronnetwork.com（兴趣：PON/PoE/商业 PoE，有 E-wind） | 110 #20 |
| 45 | karerguvenlik.com | 18B | 40A | 自有 **KARER** 品牌 PoE Switch 4/8/16/24 口（深圳 OEM）+自组 NVR | **Nurbaki Karatas 老板** | 111 #7 |
| 46 | bimel.com.tr | 15B | 15C | 代理 Planet/Ruijie（黄灯）+Cisco（红灯），安卡拉 1984 | Goenuel Ilbeyli | 新 |
| 47 | dacelsolutions.com | 15B | 8C | 工业自动化（PLC/WECON），switch 极边缘 | Erkan Cirit 股东 | 新 |
| 48 | fiberden.com | 15B | 10C | 光纤 MC/光缆/SFP 为主，switch 无明确痕迹 | — | 新 |
| 49 | cctvdepo.com | 15B | 25B | 2004 起 51-200 人「土首个 B2B 安防平台」（Perpa），2025 自有品牌 **SECUZI** CES 展 | **Can Gurcan CTO / Asuman Ozuedogru** IASF 2025 | 111 #21 |
| 50 | eurocamguvenlik.com.tr | 15B | 核心业务未确认 | IASF 2021 面见；CL 建议人工介入（无法确认核心业务） | Gokhan DEMİR CEO / info@eurocamguvenlik.com.tr | 新 |

## 3. 本轮 web 深挖（直连 5 页 + 搜索 5 批）
1. **Entegron（entegronnetwork.com 直连）**：产品树=Ethernet Switch 11 / **PoE Switch 31** / EPON ONU 9 / GPON ONU 6；L2 managed 8/16/24/28 口 GbE+2SFP、10G 8G+4SFP；WP 2021-03 建站（陈旧）；YouTube「Entegron」频道（Cahit Terzioğlu=疑似 owner 关联）；Bit Assist 联系表单。
2. **Pavotek（pavotek.com.tr 直连）= Pavo Group 确认**：导航 Solutions/Media/Innovation/Careers/Partnership/Contact 全 → pavo-group.com；Media=同批集团新闻（TWIF CFO Dr. Mahmut Kayacık 2026-07-30 / Republikorp×Bilal Yıldız 2026-08-27 / Barzan Holdings CEO 会见）；业务=Avionics / **Communication, Network and Control Systems** / Power Control / IoT / Smart Energy / Testing。
3. **Snexus（snexus.com.tr 直连）**：Wix 站；PoE switch 主视觉 +「**Zengin L3 Özellikleri**」=硬件 IP 路由 **RIP/OSPF/BGP**（新宣称，r19 记录为 L2 品牌商→升级信号）；「Bize Ulaşın」联系块。
4. **NovaCom（novacom.com.tr 直连）**：PoE Switch 类目 **31 SKU** 自有 NVC-PSE0420 / NCV-HIF0420FBL-C / **NCV-HIF2421GBL-C（2026-01 上新）** / ND-1PG0421A / ND-920-8FX2TX（8G SFP+2RJ45 光纤 switch）/ NVC-HIF0820/0821/1621GBL-C 等，全部 In stock。
5. **OPAX（opax.com 直连）**：**OPAX-08120W**=8+2 口 10/100M PoE 120W（30W/口 af/at），**$35/1,750 TL+KDV，2 年质保，Stokta Var**；规格=Extend 250m 一键旋钮/PoE Watchdog/4 芯 1236 传输/-10~50℃/4KV Surge+8KV ESD/2Gbps 交换/金属壳 200×118×44mm = 典型深圳非网管 PoE（HRUI 同源型）。
6. **Optima（搜索）**：OPTİMA Mühendislik Ltd. Şti.=2000-12 起（OSTİM→Başkent OSB Sincan 厂）物理安防制造商=路障/防撞柱/胎刺/闸机/车牌识别/防弹岗亭；**Istanbul 销售办=Perpa A Blok K:8 No:701**（+90 212 210 70 00）；HQ +90 312 815 15 00；optima@optima.tc；FB 实体页 +90 507 463 05 66=TCL Furkan Kalkan 手机（口径一致）；海外=Optima Engineering INC（沙特，LPR/停车支付）。
7. **Filiz Güvenlik（搜索）**：Filiz Güvenlik Sistemleri Proje İnşaat San. Tic. Ltd. Şti.，**1994 伊兹密尔 Konak**（Mersinli 2817 Sk. 7），51-200 人；报警+CCTV（Pinetron/Bullwark，3 年保）+火灾（Mavili/Maxlogic 伊兹密尔授权服务）+车辆跟踪+可视对讲；**土首批 7/24 报警监控中心**；+90 232 441 71 74；info@；销售 Kemal Şahin。
8. **Okisan（搜索）**：OKİSAN GÜVENLİK TEKNOJİLERİ A.Ş.，**1986 起（Ekrem ÖZKARA）/2004 A.Ş.**，İstanbul Şişli Okisan Plaza；**⭐Tiandy+Dahua 土耳其授权分销商（dahuasecurity.com 分销商页实证）**+5,000+ 经销网络；$8.6M/44-50 人；Ankara+İzmir 区域办；444 1 309 / (0212) 320 28 20；okisan@okisan.com；ISAF 参展+SAHA İstanbul 会员。
9. **CryptoLink（搜索）**：cryptolink.com.tr=**自有 CRL 系全列**：CRLISW-08 / CRLISW-14P（工业 PoE）/ CRL-SW-2402 / **24 口 L3 10G datasheet** / CRL-MC02 / CRL-SFP-10G-LC / CRL-SFP-125 LC；安卡拉 Bükreş Cad. 19/1；**+90 312 557 64 00**；turk-iot.com 实证=**KGYS 项目现场在用**（VLAN/IGMP Snooping/Traffic shaping 配置文）。
10. **Cenova**：cenova.com.tr 直连代理故障（2 次）→ 采信用户评估原文（dl-end3308pfg=E-wind PoE 产品页实存）+ r19 既有档案（边界声明）。
11. **Bimel 搜索副产物**：bimel.com.tr 工业 PoE 类目页实列 **DPTEK**（中国工业品牌）= 其「有名牌子」口径补证。

## 4. 跟进建议（详见 112 号档案）
- **Tier 1（立即跟进，双 A/暖线）**：NovaCom（40A，主动寻工业供应商）/ Snexus（35A/50A，L3 升级）/ OPAX（30A/40A，HRUI 替换+OEM）/ CryptoLink（35A/35B，CRL 系 L3 10G）/ Telkolink+GelecekBT（38A/35B，三旺/CLR/HRUI 替换）/ Entegron-LONGLINE（30A/45A，双品牌双入口）/ Cenova（30A/40A，E-wind 替换）。
- **Tier 2（暖渠道）**：Optima（IFSEC 面见+计划访深，LPR/停车 PoE）/ Filiz（迪拜面见+25 年监控中心，CCTV PoE）/ Okisan（5000 经销网络，丰润达 PoE 替换）/ Karer（老板直联，KARER OEM）/ CCTV Depo（SECUZI 自有品牌+IASF 面见）。
- **Tier 3（监控/低优先）**：MFD（Siemens 红灯）/ Bimel（Planet/Ruijie 黄灯）/ Areskom（CTS）/ Teamon（Planet）/ İntenet（Raisecom）/ Dacel / Fiberden / BaburTech / TekmarShop / İnovatech / Kiracı-ZKR / RadioTeknoloji / Egemenelektronik / Metcom / TeknolojiPazar / GMT（Uotek）/ Cebeci（ONV）/ EuroCam（CL 未确认）。
- **战略留档**：PavoTek=Pavo Group 子公司（110 行 1 监控线，非客户）。

## 5. 边界/死档
cenova.com.tr 直连代理故障（2 次，采信用户评估）/ filizguvenlik 直连改搜索成功 / okisan 直连改搜索成功 / 评估表行 51-300=空模板（无数据）/ 明细 sheet 1-300=空模板 / 299 名单中 249 家（50 评估之外）=后续批次池（本轮不逐家深挖，边界声明）。
