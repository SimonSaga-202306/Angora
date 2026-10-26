# 111 土耳其优质客户管线（第 19+20+21 轮深搜产出）

> **建立**：2026-10-08（第 19 轮）｜**扩展**：第 20 轮（同批扩展）｜**输入**：raw r19（用户 50 家名单）+ `99-raw/turkey-customer-list-round20-iasf2025-2026-10-08.md`（IASF 2025 展会 50 条，逐家深搜）+ `99-raw/turkey-customer-list-round21-iasf2025-full-2026-10-08.md`（IASF 2025 **完整**名单 86 条，第 21 轮新增 27 条土耳其客户逐家深搜）
> **收录标准**（用户指令）：只收**优质客户 / 对标客户**；无价值、不相关、核实为红灯绑定/无关业务的**一律不收**，理由在 raw 文件 §1.1 逐家留痕。
> **方法论**：用户提供的 URL/联系人/AI 评分列 = **参考输入，不作为证据**；每家的"交换机产品线"与"当前供应链"列 = **本轮独立官网/搜索核实**（fetch 官网 7 家 + web_search 站点索引 16 家；后段 fetch 代理故障，受影响家已标注）。
> **三件套**：本 MD + `111-turkey-customer-pipeline.csv`（同数据）+ `111-turkey-customer-pipeline.xlsx`（格式化，当前 **145 行数据**，r37 后）。
> **铁律**：不涉二极管类产品（只增不删：110 竞对表既有二极管行不动）。
> **第 23 轮复核（2026-10-21，用户「把你之前做的再过一次 / 继续挖掘 angora 相关信息」）**：本管线 2 项待核处理——#20 **Opax 待核解决**（法律主体 = Opax Mühendislik Kamera Alarm ve Güvenlik Sistemleri ... Ltd. Şti.，**Nevşehir/Opax Plaza**，+90 850 259 12 12，B2C+B2B 代理双轨；opax.pl = 另一波兰域，与土耳其主体无书面关联，\"外资主体\"假设降级）；#43 **Duzgun** 部分解决（toptansarf.com 在运营 = TOPTANSARF BİLGİSAYAR VE GÜVENLİK SİSTEMLERİ，Bahçelievler/İstanbul，10 年 B2B 批发 1000+ SKU；teksarf.com 当前 500 宕机；同一主体 = 高概率，待实联确认）。管线行数不变（51），详见 `99-raw/r23-recheck-mining-2026-10-21.md`。

---

## 一、总览

- **第 19 轮：输入 50 家 → 收录 23 家**（A 核心 5 + B+ 3 + B 12 + B- 3），合并 2 组（#10+#23 同集团、#9+#29 同集团）
- **第 20 轮（IASF 2025 展会名单）：输入 50 条 → 新增 22 行 + 并入现有行 1（#64 Snexus）+ 排除 27**；新增 = B+ 3 + B 2 + B- 17
- **第 21 轮（IASF 2025 完整名单 86 条补全版）：已分析 51 条跳过 + 非土耳其留档 8 条（不分析）+ 新土耳其 27 条深搜 → 新增 6 行（#46-51）+ 排除 21**；**管线总计 51 行**
- **重大更正 1 家**：#44 **entegronnetwork.com = LONGLINE 第二品牌**（官网自述 "Established in 2000, LONGLINE Technology Ltd"，同址 Longline Plaza No:18 Bayrampaşa）→ **从客户除名，转入 110 竞对行 20 更新**（双品牌：LNG switch 线 + Entegron PoE/FTTx 线 57 SKU）
- **排除 24 家**（详见 raw §1.1 逐家原因；第 22 轮计数复核更正：原误记 26，raw §1.1 实核 50 = 25✅〔23 行，#23 GelecekBT 并入行 1 / #29 Isee 并入行 11〕+ 24❌排除 + 1⚠️entegron→110 竞对行 20）：红灯深绑 6（mfd=西门子/areskom=Westermo+ATOP/okisan=Dahua+Tiandy/intenet=Raisecom+TETAŞ/teamon=Planet+Ruijie/bimel=Planet+Ruijie+Cisco）｜自研封闭/无关 7（gmtcontrol=本土 PLC 厂/pavotek=防务/optima=物理安全厂/technopc=封闭集成/dacelsolutions=工业自动化/fiberden=MC 线缆/metcom=switch 配菜）｜规模过小 3（egemenelektronik=小零售/lemax=微型批发 $26-129/teknolojipazar=İzmir PC 零售发不过去）｜失联/404/未证实 8（filizguvenlik/inovatech/tekmarshop/kiracbilisim/baburtech/radioteknoloji/eurocamguvenlik + cebecigrup=欧美品牌倾向）

## 二、A 核心（5 家，第一优先开发）

| # | 公司 | 核实核心 | 我方评估 | 切入动作 |
|---|---|---|---|---|
| 1 | **Telkolink + GelecekBT**（同集团） | 官网自证同集团（"Telkolink, GelecekBT'ye aittir"）；**Perpa 批发中心**分部；多品牌**土耳其分销+进口商**；**CLR（深圳）品牌** + 四站矩阵；GelecekBT 品类树 = Switch（PoE/工业/2.5G multirate/10G/AI/PD PoE）+ SFP（100M-800G 全族）+ MC 全族 → **与我司逐线对应** | **88** | 发完整 model list + OEM 贴 CLR 方案；Yusuf Olcer/Furkan Aydin/satis@ |
| 2 | **NOVA Group（Novacom）** | **PoE Switch 类目 31 SKU 全自有品牌**（NVC/NCV/ND 系列，含 ND-920 光纤 switch，全 In stock） | **86** | **工业级扩展 OEM**（商业级已有供应商，工业级寻源中）；Ali Pekyurek；用户侧 = CEO 到访+主动问 OEM |
| 3 | **Snexus Networks** | **全 ladder 自有线**：P&P PoE → Managed G → **Managed 10G L3（SN-XGS5300 $1,130-2,750）** → **Fiber Omurga（$400-1,650）** + 工业 + 模块；自述 L3 = RIP/OSPF/BGP 硬件路由 | **85** | OEM 合作开发信（贴 SN- 标 + Marvell Prestera L3 叙事）；FB 电话（用户侧） |
| 4 | **Cenova** | CCTV 品牌（CN- 相机矩阵）+ **自有 PoE 交换机线 8 款**（SWP-POE33016PFU-AT 16 口 G 400W / SWP-POE31024PFM 24 口 440W / DL-3808PFG 受管…） | **82** | OEM 贴 Cenova（CCTV PoE 场景 + 相机-交换机捆绑）；Rifat Baydemir |
| 5 | **CryptoLink**（Ankara） | **CRL 自有品牌 7 份 datasheet**：24 口 L3 10G / CRL-SW-2402 / CRL-MC02 / CRL-SFP-10G / CRLISW-08/14P（工业）；**公共机构客户**（边境安全/网络/车牌/信号屏蔽） | **80** | **轨道 A（公共 niche）**：CRL 贴牌供货；公共机构群 = EGM 认证线可触达；敏感域只走产品供货 |

## 三、B+ / B（15 家，第二梯队跟进）

| # | 公司 | 核实核心 | 评估 | 切入 |
|---|---|---|---|---|
| 6 | Coptek（Balmumcu） | DCN（中国）omurga L2/L3 + ONV 工业（18 口 L2+ 受管 PoE/10G uplink 16 口 L2+）+ Antaira + DONGWE 光转 + SFP 全族 | 78 | 全替换方案（5 年保修对位） |
| 7 | Karer（Pendik） | **KARER 自有 PoE 6 款**：8 口 G PoE $60-150，**库存 1000+ 级**（批发走量） | 76 | OEM 贴 KARER（8/16 口 PoE 直接对位） |
| 8 | Hane Elektronik | **FOREDGE + VIDEOPARK 双白牌 PoE 25 款**（云管理 250-400W）+ FOREdge SFP 模块 | 74 | 贴牌替换 + 云 NMS 组合卖点 |
| 9 | Öncü Güvenlik A.Ş. | **Sec-on 自有工业 PoE**（SC-E204-H 4 口 G PoE -40/+75°C 等 3 款）+ Hik/BDCOM | 72 | Sec-on 贴牌工业 PoE（STI 8 口对位） |
| 10 | ErETE | **XPS（ONV 贴牌）工业线**（受管/受管 PoE/非管理 5 系列）+ **EdgeCore ECS4660-28F L2/L3/L4 metro 在售** | 71 | XPS 贴牌替换 + EdgeCore 底座情报 |
| 11 | Eretekne（+Isee 集团） | XPS 工业（XPS-I7120-14P 10 口 8PoE L2+）+ **EtherWAN 品牌页**（16 口 PoE L2+ 等）+ ONV | 70 | 三源（XPS/EtherWAN/ONV）任一侧替换切入 |
| 12 | CCS Güvenlik | **BC-ODS 自有白牌 PoE**（16 口 250m extend/8 口 G 工业/32 口 L2 受管）+ Reyee（$911 24SFP L2）/Dahua/Hik | 69 | BC-ODS 贴牌替换（长距 PoE 卖点） |
| 13 | Rima Elektronik（Ankara） | **Antaira（黄灯全球品牌）工业 switch**，switch 类目**库存 103 项**；【r33 重验】安防/IT 集成商，自有 **Digifort** AI 视频分析 VMS（人脸 99.87%），品牌矩阵 Axis/FLIR/Milestone/Dahua/Hikvision/D-Link/Broadcom；Levent 2025-03-07「We have not done business before」= 非 Angora 客户 | 68 | 第二供应源提案（LNX-1002C 对位）+ 相机+交换机捆绑项目渠道 |
| 14 | NFS Teknoloji | **Surenix/Oinone PoE 现货**（4 口工业 + 24 口 L2 受管 PoE G） | 67 | 替换/补充（SRX 系列对位） |
| 15 | Koza Güvenlik（GreenTech 集团） | 2005 成立 11-50 人（LinkedIn），自有注册商标 + 分销双轨，CPSE 2023 参展 | 66 | 技术经理切入（先探自有品牌 switch 线） |
| 16 | Portel（industrialnetworkcenter） | **3OneData 工业**（IES6312 12 口 L2 受管 PoE 240W 等，EUR 计价） | 65 | 3OneData 同源替换 + ERPS 环网差异化 |
| 17 | RF Teknoloji | **3Onedata 独家代理**（PoE 工业 13 SKU + IES7110 + 串口/Modbus）+ RF 数传主业 | 64 | 3Onedata 同源替换（RF 户外场景） |
| 18 | iotsistem | **MLB 工业受管线**（14/28 口受管/5 口 PoE -40~75°C）+ USR IoT 分销 | 63 | **暖线索（联系人已有回复）**：工业受管 PoE 报价 |
| 19 | Lansan（Ankara） | **LNS 自有**（8 口 PoE $1,000 标价/24 口 PoE/6 口 PoE/SFP omurga $1,755） | 62 | LNS 贴牌（标价异常偏高 = 升级替换空间） |
| 20 | Opax（opax.com） | **OPAX 自有 PoE**（8 口 $31.50-35/16 口 300W rack，250m extend）+ 全国 Bayi 网络 | 61 | OPAX 贴牌（**r23 主体核实完成** = Opax Mühendislik ... Ltd. Şti.，Nevşehir/Opax Plaza，+90 850 259 12 12，B2C+B2B 代理双轨；opax.pl 与土耳其主体无关联） |
| 21 | CCTV Depo | **SECUZI 自有**（8+2 口 305 米 Gbit PoE）+ **Bayi B2B 系统**；2004 起 51-200 人 | 60 | SECUZI 贴牌（305m 长距对位）+ 平台批量 |

## 四、B-（3 家，观察/补验）

| # | 公司 | 核实核心 | 评估 | 备注 |
|---|---|---|---|---|
| 22 | TeleOne | AI IP 摄像机方案商实锤；PoE Switch 类目 = AI-2 口径，search 未复现产品页（**部分验证**） | 58 | 遗留：switch 类目待 fetch 恢复补验；Utepo 海关记录（用户口径） |
| 23 | Konak Güvenlik | 品类树实锤（Ethernet → PoE 子类）；多业务混杂站点；AI-2 = 在售 OPAX 线 | 55 | 经营主体待电话核实（用户已有手机） |

> 注：第 19 轮收录合计 = 23 家（A 5 + B+ 3 + B 12 + B- 3）；第 20 轮新增 22 行（#24-45，见 §八）。

## 五、重大更正：#44 Entegron = LONGLINE（竞争者，非客户）

- 官网原文 = "**Established in 2000, LONGLINE Technology Ltd**… specializes in PoE solutions and optical fiber communication products"；地址 **Longline Plaza No:18, 34040 Bayrampaşa** = 110 行 20 同址同年
- 质量页 = "as Longline… **Longline test center**… **CE, RoHS, ISO 9001, FCC**"
- **Entegron 品牌 57 SKU**：Ethernet Switch 11 + **PoE Switch 31** + EPON ONU 9 + GPON ONU 6 + **GEPON OLT（1U 8 口/4 口 EPON）** + 10G intelligent access（8GE+4×10G SFP）+ **ENTDPS208P Reverse PoE EPON ONU MDU（FTTB）**
- **结论**：Longline = **双品牌运营商**（LNG = switch 线 / Entegron = PoE+FTTx 线）；威胁维持"高"，重叠面扩大至 PoE/FTTx/10G/工业 → **已更新 110 行 20**（CSV+XLSX+MD 三件套同步）
- 用户对该家的备注（E-wind/GXCOM 在售）**不采信为客户证据**

## 六、排除清单（24 家，逐家原因见 raw §1.1；第 22 轮计数复核更正 26→24）

| 类别 | 公司（用户#） |
|---|---|
| 红灯品牌深绑 | mfd（西门子 SCALANCE）#8、areskom（Westermo/ATOP）#19、okisan（Dahua/Tiandy 授权）#16、intenet（Raisecom+TETAŞ）#20、teamon（Planet/Ruijie）#21、bimel（Planet/Ruijie/Cisco）#46 |
| 自研封闭/无关业务 | gmtcontrol（本土 PLC 厂）#4、pavotek（防务）#5、optima（物理安全厂）#11、technopc（封闭集成）#40、dacel（工业自动化）#47、fiberden（MC/线缆）#48、metcom（switch 配菜）#25 |
| 规模过小/价值低 | egemenelektronik（小电商，WhatsApp 已通）#26、lemax（微型批发 $26-129）#37、teknolojipazar（零售，发不过去）#27 |
| 失联/404/未证实 | filizguvenlik #2、inovatech #22、tekmarshop #28、kiracbilisim #32、baburtek #35、radioteknoloji #43、eurocam #50、cebecigrup（欧美品牌倾向）#13 |

## 七、跟进优先级（执行序）

1. **iotsistem**（Berk 已有回复 = 唯一暖线索）→ 24h 内报价
2. **NOVA**（CEO 到访+OEM 主动问 = 高意向）→ 工业 OEM 方案书
3. **Telkolink/GelecekBT**（品类全对应+进口商）→ model list + CLR 贴牌
4. **Snexus**（双 AI 最高共识）→ OEM 开发信
5. **Cenova / CryptoLink**（公共 niche 轨道 A 并行）
6. B+ 三家（Coptek/Karer/Hane）批量发牌 → B 梯队按城市打包
7. **Entegron/Longline 双品牌** = 竞对监控项（每轮 110 复核产品线变动）

## 八、第 20 轮扩展：IASF 2025 展会名单（输入 50 条 → 新增 22 行 #24-45 + Snexus 并入 + 排除 27）

> **输入**：用户 IASF 2025 展会客户名单 50 条（49 编号 + 1 无号；raw r20 §一 verbatim）。**收录标准同 r19**：只收优质/对标；用户现场记录 = 参考（联系人/需求线索写"联系人/备注"列，**不作公司证据**）；无业务面/无法核实/红灯/不相关 = 排除，逐家原因见 raw r20 §三。
> **核实方法**：本批 22 家收录 + 28 家排除判定全部经 web_search 站点索引/地图/注册库独立核实（fetch_page 仍故障，标注同 r19）。

### 8.1 B+ 新增（3 家）

| # | 公司 | 核实核心 | 评估 | 切入 |
|---|---|---|---|---|
| 24 | **SFPTURKEY**（İstanbul） | **SFP 进口-出口商**：1G/10G SFP（GENERIC/ARUBA-HP 兼容）/DAC/switch/MC/光纤网卡 + 3 年 100% 换新 + **自有品牌 GigaCom/geMaxx** + 4 域名矩阵 | 77 | SFP 全 model list（¥25 价位带）+ 10G 光 + 带 bypass switch（客户实需 2 光2 电/2 光4 电）+ OEM 贴 GigaCom/geMaxx |
| 25 | **HAFYA Technologies**（İstanbul） | 安防+弱电集成：相机 + **IT 基础设施（有源网络设备/机房）** + 门禁/turnstile + 楼宇自动化 | 75 | **防水工业交换机规格书+报价**（现场：军队项目，工业 4 光8 电 PoE 网管；轨道 A） |
| 26 | **Makros AŞ**（İstanbul） | **i-PRO（Panasonic）土耳其 Premium Distributor**（官网自证）= 高端 CCTV 授权分销 | 73 | **DDP 双清包税报价跟进**（现场已谈 $130/$150 两档，合照 = 高意向） |

### 8.2 B 新增（2 家）

| # | 公司 | 核实核心 | 评估 | 切入 |
|---|---|---|---|---|
| 27 | **ONSİS**（Ankara） | 1992 年起安防系统商（相机控制/对讲/报警/智能/卫星）；**GM Esef Taşkiran = 用户联系人 esef@ 匹配**；规模 datanyze $28.2M（存疑待电话核） | 68 | **样品跟进（关键）**：$105 bypass 报价 + L2 + 现场要样品但无现金 → 样品物流方案 |
| 28 | **Hiperonline**（Eskişehir） | **区域光纤 ISP**（81 省覆盖，自有光纤+AirFiber+企业 Metro Ethernet 10G 对称） | 66 | 多口 switch + SFP 报价（ISP 扩网持续采购） |

### 8.3 B- 新增（17 家）

| # | 公司 | 一句话核实 | 评估 | 切入要点 |
|---|---|---|---|---|
| 29 | DE Secure（İstanbul） | Avigilon Premium Partner + 远程监控中心（高端安防服务） | 62 | 工业 8 口 PoE 30W **含 20% 关税报价** |
| 30 | ORAL GÜVENLİK（**北塞浦路斯 Lefkoşa**） | Oral Companies 集团 2008 + Ninova 经销商 | 62 | **瑞昱方案价格**（Vitesse $90 嫌贵）+ 北塞渠道开发 |
| 31 | F.A.S.T A.Ş.（İstanbul） | 工厂设备系统技术 A.Ş.（PLC/IO 代理 + 工业 5 口 PoE） | 60 | 工业 5 口 PoE + 自动化捆绑 |
| 32 | Fiberix（Gaziantep） | 光纤 ISP（51-200 人 $13.4M）；⚠️ 已有广州合作方 | 60 | SFP+商业 switch 价格正面打（需知其现供应商） |
| 33 | HCS | 结构化布线全国品牌（Phy-FiXX/6A/机柜） | 58 | 商业 PoE L2/L3（PM 级采购） |
| 34 | STASANET（塞尔维亚） | 安防进口分销 2013 起，年 ~200 家，辐射波黑/黑山/马其顿 | 57 | PoE+光模块（前南市场入口） |
| 35 | Antalya Turkuaz | 11-50 人安防+网络集成（旅游城市） | 56 | 酒店/度假 PoE 方案 |
| 36 | Go Technology（巴勒斯坦） | 综合 IT 进口（网络/电力/太阳能/通信） | 55 | PoE 价格表（⚠️ 加沙物流风险，先核进口路径） |
| 37 | Shnrise（İstanbul 2012） | 安防全线（PDKS/相机/报警/火灾/智能家，工业设施含内） | 55 | **收发器**报价（现场主问）+ PoE 配套 |
| 38 | FOURLİNE（Bursa） | 卫星/相机/报警分销 + 经销商网络页 + 工程案例 | 54 | catalog + 相机配套 PoE |
| 39 | MEPA（Kayseri） | 11-50 人，相机+火灾+**数据网络**+音响+卫星 | 53 | 4/8/16/24 口 PoE 系列表 |
| 40 | AG Bilgisayar（Bodrum） | 10 年+ 相机+网络+门禁+停车自动化（旅游区） | 53 | **千兆 2 光8 PoE 网管 bypass**（规格明确） |
| 41 | FH Güvenlik（İstanbul/Perpa） | 2025 新设（团队 15 年+）CCTV+**网络基础设施**+工业/关键基础设施定位 | 52 | 工业交换机价格表 |
| 42 | BİLGEN（Gebze 工业区） | 电子零件供应商+安防（LTD.ŞTİ. 注册全名核实） | 52 | **2 光8 bypass**（问 PoE 功率 = 选型中） |
| 43 | Duzgun Toptan（teksarf） | 批发 IT 供应商（**r23**：toptansarf.com 在运营 = TOPTANSARF BİLGİSAYAR VE GÜVENLİK SİSTEMLERİ，Bahçelievler/İstanbul，10 年 B2B 批发 1000+ SKU；teksarf.com 当前 500 宕机；同一主体 = 高概率待实联） | 51 | 商业 PoE 批发报价 |
| 44 | PROVES（İzmir A.Ş.） | Proves Bilgi Teknolojileri A.Ş.（与 PROVEN 防务无关联证据） | 50 | 工业级报价单 + 电话核集团面 |
| 45 | Alamthal（利比亚） | 通信+IT 公司（官网 about 页核实） | 49 | 商业 PoE（⚠️ 先核支付路径） |

### 8.4 并入现有行（1）

- **#64 Snexus（info@snexus.com.tr）= 第 19 轮 A 核心 #3 同一公司** → 行 3 更新：新增联系人 **Erdem Timur Koca（90 542 552 17 79，WhatsApp，IASF 2025 现场）** + 商业级 PoE/8 光8 电兴趣 + 曾推工业级 $115 → 跟进 = 8 光8 电报价 + OEM 开发信并行。

### 8.5 排除清单（27 家，逐家原因 raw r20 §三）

| 类别 | 公司（用户#） |
|---|---|
| 无法核实（17） | LABOR #34、Arcan #42、IHM #45、Senkacayc #46、Bilimsa #48、Netmax #49、Karaal #51、Marmaris #53、Todorov #54、Sinerjik #58、Marbim #59、Dimas #60、Fadi #65、Goktork #66、Alhossan #78、3S #80、D&N #70 |
| 无法核实-分销商信号在案（1） | Ugur Imre #68（现场记录 = 分销商/不要 OEM/工业 PoE；瑞昱+DC48V 内置 $70 回复 "Not bad" → WhatsApp 跟进后再核） |
| 微型/本地服务（6） | BTM #28、Ebatek #33、Voltech #39、Cansis #52、Başaran #61、Klasnet #77（经销商咨询信号在案：问如何成为经销商） |
| 红灯深绑（2） | Acusense #37（Hikvision 授权）、ANIL #83（Dahua 主代理+Ruijie/TP-Link/Lande） |
| 业务不相关（1） | New World Polo #41（**数据冲突**：实为土耳其纺织制造商，用户列 Greece 存疑） |


> 注：无法核实 17 + 信号在案 1 + 微型 6 + 红灯 2 + 不相关 1 = **27 家**（与 50 = 22 新增 + 1 并入 + 27 排除 对平）。

### 8.6 第 20 轮跟进优先级（并入 §七 执行序）

1. **HAFYA**（军队项目通道 + 防水工业规格书需求 = 最高战略价值）→ 规格书+报价 24-48h
2. **ONSİS**（GM 级 + 样品意向，只差样品物流方案）→ 样品方案 24h
3. **SFPTURKEY**（SFP 线核心对标，OEM 双品牌）→ model list + OEM 方案
4. **Makros AŞ**（已谈价 DDP，跟进即转化）→ 正式报价单
5. **ORAL GÜVENLİK**（瑞昱方案 + 北塞新渠道）→ 瑞昱报价+价格表
6. Hiperonline / DE Secure / STASANET / Shnrise / AG Bilgisayar（规格明确的 PoE/bypass 需求）→ 批量报价
7. 其余 B- → 价格表 + WhatsApp 跟进（不谙英语者优先 WhatsApp）

## 九、第 21 轮扩展：IASF 2025 完整名单 86 条（用户补全版；新土耳其 27 条深搜 → 新增 6 行 #46-51 + 排除 21）

> **输入**：用户 2026-10-08 补全 IASF 2025 **完整名单 3 张表 86 条**（"重新梳理 刚才给你的可能有遗漏的"）。**指令**：① 同 r19 标准；② 已分析（r19 NOVA + r20 50 条 = 51 条）跳过；③ **只看土耳其客户，非土耳其只留档不分析**。
> **分类**：86 = 已分析跳过 51 + 非土耳其留档 8（Maipu 中国/Miroslav 塞尔维亚/Megatrade 乌克兰/AMZ Solutions 阿尔及利亚/0770 巴基斯坦/STORM ICT 科索沃/netpardazco 伊朗/**Equinix 全球（Ahmet Yilmaz，Istanbul DC SFP 买家；✅ 第 22 轮用户裁定：不跟进，仅留档**）+ 新土耳其 27（深搜）。

### 9.1 新增 B（3 家）

| # | 公司 | 核实核心 | 评估 | 切入 |
|---|---|---|---|---|
| 46 | **TBI - Telemobil**（İstanbul） | 2005 起，51-200 人 ~$25.6M；IT 方案+电气承包+楼宇自动化（集装箱码头/商场/酒店/大学/公共/医院） | 70 | **2 光2 电 PoE 报价 + 交期**（用户侧标"可重点跟进，有具体项目"，现场客户问交期） |
| 47 | **Pelikan Bilgisayar**（Perpa/Şişli） | **Perpa 批发区进口-出口商行**；商城实锤：工业 L2/L3 PoE + PoE MC + Injector/Splitter + SFP-LTE 路由 + 工业网关 + DIGITUS | 64 | 工业 PoE L2/L3 + MC + Splitter 对位报价（类目与我司逐线对应） |
| 48 | **Bilge Güvenlik A.Ş.**（İstanbul+Ankara+İzmir） | 2003 起 11-50 人；安防集成（视频分析/车牌识别）；**东南欧年度最佳渠道伙伴奖** | 62 | PoE 报价（现场明确要）+ 车牌/视频分析场景配套 |

### 9.2 新增 B-（3 家）

| # | 公司 | 一句话核实 | 评估 | 切入要点 |
|---|---|---|---|---|
| 49 | Zeytek（İstanbul/Sancaktepe） | 机房/弱电材料供应（政府/医院/银行/工业项目面） | 58 | 机房项目 switch+MC 配套 |
| 50 | FOLİNE（İstanbul/Kağıthane） | **数据中心+集装箱 DC+弱电**工程商（GM 级联系人） | 58 | DC 项目 omurga 方案 |
| 51 | NAZEMCO | 进口-出口有限公司 + 电子电商（4G 相机/音响），商业 PoE 需求 | 50 | 商业 PoE 报价 + 整柜/混柜试探 |

### 9.3 排除 21（逐家原因 raw r21 §三）

- **无法核实 16**（第 22 轮计数复核更正 17→16，21 = 16+1+2+1+1 对平）：selimkalaka（信号：郑州供应商拟在土建厂 = 换源窗口）/ **Sami CEUIK（强信号：500 台询价 + 已购 $100 样品 + 会来深圳安博会 → 微信跟进第一优先）** / Fatih A / Celali Ayazoglu（收发器）/ A7 仅电话（4/8/16 PoE 合影）/ TeT529（家用 2.5G 客群不符）/ Ertan Kral / Enes Talha Karaaslan / Gokhan / Sedat（工业+IO）/ Interland / Smali / 拉赫曼 Vatankhah（天地伟业员工+伊朗客户信号）/ Serkan（Alisa 客户 bypass）/ GÜNGÖR（两个同名均无交换机业务面+仅彩页）/ Holil
- **主体无法确认 1**：NORTEL（norteliletisim.com 无业务面，与 Nortel Netas 混淆；仅要 catalog）
- **微型+红灯 2**：viva bilgisayar（Hatay 1-10 人 + **Hikvision 授权**，同 r20 Acusense 口径）/ teknoktadestek（İnegöl/Bursa，**Dahua/Tiandy/Hikvision 三大授权**，network 次类目）
- **无交换机场景 1**：Interpos A.Ş.（半导体/PCB/无线模块制造商，CEO 仅名片）
- **端客户无需求信号 1**：Camsan Ordu A.Ş.（MDF/地板制造 780 人 $69M，仅彩页无交谈）

> 注：27 = 6 新增 + 21 排除；**111 管线总计 51 行**（A 5 + B+ 6 + B 18 + B- 22）。

## 十、第 36 轮更新：土耳其本土「类 PNetworks」品牌侧客户深挖（2026-10-21，只增）

用户指令：「挖一些土耳其本地的客户 公司啥的 和 saga 产品很契合的 类似 PNetworks」。

### 10.1 新增 4 行（#52-55，三件套同步）
| # | 层级 | 公司 | 定位 | 契合点 | 评分 |
|---|------|------|------|--------|------|
| 52 | A | **upTech / Nokta Elektronik**（Perpa） | 注册品牌主（marka 2008/13951，916 SKU） | PoE switch（af/at，相机/AP）+SFP+MC；自有 AR-GE claim+firmware 公开=白牌 ODM 转单窗口 | 78 |
| 53 | A- | **WINET（wi.com.tr）** | MikroTik 授权分销+PON/光纤专业商 | 自有 WINET 417 SKU（被动件+**micro OLT stick SFP 1:32**+被动 PoE 面板〔Yerli Üretim〕）；SFP+PON 邻接先行 | 64 |
| 54 | A | **TekniksatGroup（TGD）** | CATV/卫星/CCTV/光纤垂直集成商（1992 起） | ⭐自有 **TGD 48V PoE switch 线**（P4/P8/P8S/P16S/P24S）=与我方工业 48V DC 线直接契合 | 72 |
| 55 | B | **ULAK Haberleşme**（Ankara） | 军通（需求侧） | IDEF 2025 与 Netaş+Teknopark İstanbul 签 yerli 5G 战略协议；军平台 switch 标单监控 | 45 |

### 10.2 既有行增量（110 备注同步）
- **Netaş（110 行 2）**：2024 年报=与 ZTE 合作 **800GE ethernet 测试（单载波 800G 无再生 2,000 km，2026-02，世界纪录叙事）**+SAHA EXPO 2024（50 周年）+Orhanlı 生产基地+taktik saha/gemi haberleşme → 高速网络需求侧铁证（与既有「找 Moxa/Hirschmann 替代」机会并列）。
- **Longline（110 行 20）**：营销扩张实锤=NetGaste 2025-10-14 工业 switch 软广+Teknoblog 2026-02-05 2026 指南软广（Longline 线在投）。

### 10.3 留档（非目标，99-raw r36 §6）
Sekom（Turkcell MWC 2026 伙伴，网络软件）/ YONGATEK（RISC-V 芯片 ÇENTİK，TSMC）/ ElectraIC（3U VPX 机箱）/ General Mobile（5G 手机厂）/ Aselsan×TT 地方手机 / **VSOL=中国 OLT 厂商（PON 侧同层 ODM 竞情参照）** / 34Alarm(DayLine)·aktifsat=零售 / AN-EL=电气开关元件（排除）/ Teknopark 2021 PNetworks 规格原始出处 / Özbilen 2023 七条宣言。

### 10.4 边界
BİGG 项目表 PDF 未逐项解析 / 土耳其 CPSE 2025/2027 参展商名录无公开索引 / ULAK 品牌方证据缺失（仅需求侧）/ «yerli switch» 新闻=2021-2026 无新制造商（PNetworks 叙事垄断）。

## 十一、第 37 轮更新：用户两份名单 + ISAF 2025 展会全量入库（2026-10-25，只增，+90 行）

用户指令：「我在main上传了2个客户list 你读一下 深入挖掘一下这些客户 看看哪些能跟进啥的」+「2025土耳其ISAF客户.xlsx 一起处理」。
输入三件（全量逐字底稿在 `99-raw/`：`r37-ai-kehu-eval-master.tsv` 64KB / `r37-turkey-client-list-299.tsv` / `r37-isaf-2025-raw.tsv`+`r37-isaf-union.json`；分析=`r37-user-customer-lists-2026-10-25.md`+`r37-isaf-2025-analysis-2026-10-25.md`）：
1. `AI客户评估_TR 10.06.xlsx` master 总表 **No.1-50 双 AI 评估**（AI+CALUDE；51-300 空模板）
2. `Turkey Client List.xlsx` 299 家原始名单
3. `2025土耳其ISAF客户.xlsx` 展会现场接待（Sheet1 合并 51 条+Evelyn 28+Ady 29+Simon 31；去重唯一 98=TR 85+非土 13）

### 11.1 交叉比对（master 50 vs 111/110 库）
**26 家在库**（行 1-23 共 25 家：行 1=Telkolink+GelecekBT、行 11=EretEKNE+isee + 110 行 20 Entegron）/**24 家新**=**行 56-79**。
编号口径：99-raw 速览表#=master No.1-50（与 TCL 顺序不一）；master 50 中 43 家在 TCL 299 内、**7 家仅 master 有**（rima/radioteknoloji/karer/dacel/fiberden/cctvdepo/eurocam）。
⚠️ **与 r19 排除记录的关系（重要）**：行 56-79 的 24 家 = r19 轮「排除 24 家」的同一批（红灯绑定 6/自研无关 7/规模过小 3/失联未证实 8）。**用户 10.06 双评估名单=对新名单的重新定级**，本轮以用户双评估分+10-25 新核验为准重录为新行（r12 只增不删：r19 排除留痕保留在 §一，新行备注互指；非 PASSED 项复活）。r37 关键改判：Okisan=**Tiandy+Dahua 授权分销商 $8.6M 5000 经销**（r19「红灯」→Tier2 暖渠道）/ MFD=Bimel 仍红灯不跟进 / Optima=物理安防厂但 **IFSEC 面见+计划访深=最暖线** / Pavotek=**Pavo 子公司战略留档（110 行 1）**。

### 11.2 新行 56-79（24 家，用户双评估分）
Tier1 既有关联=行 2/3/4/5/7/20 备注增量（ISAF 面见 2 家见 11.3）。新行重点：**56 Optima（A- 最暖线，Furkan Kalkan 90507 463 05 66，LPR 场景 PoE+OEM）** / **58 Okisan（A- 大分销，444 1 309，丰润达替换+Dahua/Tiandy 绑货）** / 57 Filiz（迪拜面见）/ 59 PavoTek（C 战略留档）/ 60 GMT / 61 MFD（C 不跟进）/ 62 Cebeci / 63 Areskom / 64 İntenet（Ercan Ozturk GM-Owner）/ 65 Teamon / 66 İnovatech / 67 Metcom / 68 Egemenelektronik（两老板 Belkiz/Levent）/ 69 TeknolojiPazar / 70 TekmarShop / 71 BaburTech / 72 LeMax（A- OEM）/ 73 Kiracı=ZKR（与行 10 同 Kıraç 集团）/ 74 RadioTeknoloji / 75 TechnoPC（A-，E-wind 替换）/ 76 Bimel / 77 Dacel / 78 Fiberden / 79 EuroCam（IASF 2021，CL 未确认）。

### 11.3 ISAF 2025 展会新行 80-145（66 家）
**A 级 12 家（80-91）**：Telemobil（⭐现场「可重点跟进，有具体项目」2光2电 PoE 问交期）/ Makros-DEMIREL（130/150USD 已报+DDP）/ **HAFYA（军项目+防水 4光8电 PoE+grundig-security.tr 双域名，与行 8 Hane=Grundig 分销生态待核）** / SFP Turkey（既有客户，修图级深度服务）/ ONSIS（要样品 105USD）/ Netmax（120USD）/ bilimsat-KILIC（110USD）/ UGUR IMRE（分销商 70USD「Not bad」）/ ORAL（150/90USD 嫌贵）/ DE secure（含 20% 关税报价）/ canis-AHMET CAN（150USD）/ **Sami CEUIK（500 台订单级，r21「16 无法核实」头号信号坐实）**。
**A- 8 家（92-99）**：⭐**Selim Kalaka（郑州供应商拟土建仓→找新供应商=换源窗口，r21 信号坐实）** / HCS（问 L2/L3）/ KLASNET（**问怎么成为分销商**）/ F.A.S.T / voltec / LABOR / MEPA / viva bilgisayar（老板）。
**B/C 46 家（100-145）**：彩页/名片/低信号留档跟进。
**bypass 专项信号 6 条**（105 IHM/114 Aycan CAM/117 BİLGEN/127 Serkan/84 ONSIS/85 Netmax/88 ORAL/83 SFP Turkey）→ bypass 产品线=ISAF 本轮最强产品信号，下轮出 bypass 专刊+样品策略。
**非土 13 条留档**（r21 非土只留档）：RS×2/BG/LY×3/GR/PS×2/UA/TN/XK/IR + 0770 叙利亚；**eu.equinix.com=r22 不跟进**；**Vatankhah=Tiandy 员工**（关联行 58 Okisan 渠道线）；Maipu=中国参展商竞情（ONV 80USD 对位）。
⚠️ **与 r21「16 无法核实」关系**：ISAF xlsx=该批展会线索的现场记录补全（Sami CEUIK/Selim Kalaka/Fatih A/Celali/TeT529/Ertan/Enes Talha/Gokhan/Sedat/Interland/Smali/Serkan/GÜNGÖR/Holil 等），本轮以现场记录重录为 80-145 新行（r12 只增不删，r21 留痕保留）。

### 11.4 跟进分层（主交付见 112 号档案）
Tier1=7 家在库双 A（NovaCom/Snexus/OPAX/CryptoLink/Telkolink+GelecekBT/Entegron-LONGLINE/Cenova）+ ISAF A 级 12 家（80-91）+ Selim Kalaka（92）；Tier2=Optima/Filiz/Okisan/Karer/CCTV Depo+ISAF A- 8 家（93-99）；Tier3=其余监控。
**111 管线总计 145 行**（55 旧+24 用户名单+66 ISAF）。

### 11.5 边界
cenova 直连代理故障（采信用户评估）/ master 51-300 空模板 / ISAF xlsx 原始列错位已按邮箱锚定修复 / Sheet1 缺号=合并表删行 / 299 名单 249 家（50 评估之外）=后续批次池（本轮不逐家深挖）/ HAFYA×Grundig 关系待核 / Bimel DPTEK=搜索副产物 / ISAF 无邮箱行以微信/手机为唯一键。
