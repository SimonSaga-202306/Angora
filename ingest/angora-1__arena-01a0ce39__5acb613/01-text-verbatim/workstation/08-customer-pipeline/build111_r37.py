# r37 111 管线全量更新：23 行备注 + 24 行 r37 新客 + 66 行 ISAF 新客
import csv, openpyxl
P='111-turkey-customer-pipeline.csv'
X='111-turkey-customer-pipeline.xlsx'
rows=list(csv.reader(open(P,encoding='utf-8-sig',newline='')))
assert len(rows)==56, len(rows)

UPD={
1:'【r37 2026-10-25】用户双评估：Telkolink 38A/30B（在用三旺/TG-NET/CLR+部分贴自有 logo，外观一般=品质升级空间）+GelecekBT 35A/35B（在售 HRUI 工业 switch+光路 MC，Furkan Aydin 销售工程师 furkan@gelecekbt.com）=双 A Tier1 立即跟进（双品牌替换）',
2:'【r37 2026-10-25】用户双评估 40A/30B（AI 最高分）+web 验证：PoE 类目 31 SKU 自有 NVC/NCV/ND 线（NCV-HIF2421GBL-C 2026-01 上新=持续采购中）；评估明示「正积极寻找工业 switch 供应商」+【r37-ISAF 2025 面见：NOVA Group（novacom/nova-grup 双域）Ali Pekyurek PM 90533 715 92 26 微信，CEO+PM 到展，商业已有源→准备扩展工业级，问能 OEM 吗】→Tier1 工业线先行+OEM 直答',
3:'【r37 2026-10-25】用户双评估 35A/50A（Claude 最高）+web 验证：Wix 站新宣称 L3 硬件路由 RIP/OSPF/BGP（r19 时仅 L2=升级信号）+新电话 90 53340 48364（TCL）+【r37-ISAF 2025 面见：Erdem Timur Koca 90542 552 17 79（Ady WA），商业 PoE 老客，问商业 8光8，推工业报 115USD，想让我们当礼物送=送样机会】→Tier1 L2+→L3 升级配套',
4:'【r37 2026-10-25】用户双评估 30A/40A+评估明示：在售 E-wind（深圳）PoE/工业 switch（cenova.com.tr/dl-end3308pfg 实页）+Rifat Baydemir GM rifat@cenova.com.tr→Tier1 E-wind 替换（cenova 直连代理故障采信用户评估）',
5:'【r37 2026-10-25】用户双评估 35A/35B+web 验证：CRL 系全列（CRLISW-08/14P 工业 PoE+CRL-SW-2402+24 口 L3 10G+CRL-MC02+CRL-SFP-10G-LC/SFP-125）+KGYS 警队项目现场在用实证（turk-iot.com）+新电话 +90 312 557 64 00→Tier1 工业 L3 10G 升级',
6:'【r37 2026-10-25】用户双评估 30A/25B（在售 DCN 中国商业/工业+ONV 绿灯工业+SFP+MC；Claude：成单的那个印尼客户）→B+ 监控（绿灯双源，第二供应商窗口）',
7:'【r37 2026-10-25】用户双评估 18B/40A+评估明示：自有 KARER 品牌 PoE Switch 4/8/16/24 口（深圳 OEM）+自组 NVR+老板 Nurbaki Karatas（+Samet Sahin 技术服务总监）→Tier2 KARER OEM 全套老板直联',
8:'【r37 2026-10-25】用户双评估 25A/35B+Claude：⭐Milesight（中国绿灯）土耳其唯一授权分销商（2025 新增 Grundig Security+Panasonic 分销权）+商业 PoE 多外壳（疑 hisource）→B+ 绿灯大客户第二源窗口（注意：ISAF 2025 HAFYA 双域名 grundig-security.tr，生态关系待核）',
9:'【r37 2026-10-25】用户双评估 35A/30B（丰润达+Utepo 双绿灯，工业/PoE/CCTV 产品线；ibrahim@oncuguvenlik.com.tr）→B+ 监控（r19 BDCOM 档案并行）',
10:'【r37 2026-10-25】用户双评估 28A/5C+Claude：⭐erete.com.tr 跳转 zkr.com.tr=Kıraç 集团（ZKR 品牌）+XP 用 ONV（绿灯）/Etherwan（黄灯），Murat Soyak→与新 111 行 73 Kiracı 合并按 Kıraç 集团统一接触',
11:'【r37 2026-10-25】用户双评估：eretekne 22B/30B（在售 ONV 深圳绿灯+XPS/Voscom 多品牌）+isee=同集团（Claude 30B 结论复用，can@asyatelekom.net）→B 监控',
12:'【r37 2026-10-25】用户双评估 25A/30B（在售 HRUI PoE switch 产品页 ods-r-8p2u）→B+ HRUI 替换窗口',
13:'【r37 2026-10-25】用户双评估 18B/20B+在售 Antaria 工业 switch（小众）+TCL 备注「网站适合推 Marvell」+联系人 Salih Senyurt 销售总监（+Toyan Karahan PM/Aycan Tuerkay GM）→B（Marvell 方案切入已指定）',
14:'【r37 2026-10-25】用户双评估 22B/35B（PoE 配件+switch 采自 Utepo 深圳，CCTV 场景；Hasan Basarir 技术负责人 hasan.basarir@nfsteknoloji.com）→B Utepo 替换',
15:'【r37 2026-10-25】用户双评估 18B/30B+⭐2023 CPSE 深圳安博会参展+Deniz Aydin（技术经理）主动赴华采购（+ayhan@kozaguvenlik.com.tr）→B+ 暖线（展会面见+来华经验）',
16:'【r37 2026-10-25】用户双评估 22B/25B（采购三旺 3Onedata，fiber networking 定位；Okay Yucedag 销售经理 okay.yucedag@portel.com.tr）→B 三旺替换',
17:'【r37 2026-10-25】用户双评估 22B/30B（工业交换机采自三旺 3Onedata，具体工业 PoE 产品页在列）→B 三旺替换',
18:'【r37 2026-10-25】用户双评估 20B/25B+TCL 新联系人 Bosgem（info@iotsistem.com；Berk 已有回复）→B IoT 方案 PoE 配套（Mlis MLB 型号为主）',
19:'【r37 2026-10-25】用户双评估 18B/30B（MC+switch 均打自有 logo，品牌名含 LAN）→B OEM 自有品牌窗口',
20:'【r37 2026-10-25】用户双评估 30A/40A+web 验证：OPAX-08120W=8+2 口 120W $35/1,750TL 2 年质保在售（Extend 250m 一键/PoE Watchdog/4 芯 1236/-10~50℃=HRUI 同源型）+Damian Brozda VP（damian@opax.pl）/Aleksandar Radonic COO→Tier1 同价段多型号替换+OEM',
21:'【r37 2026-10-25】用户双评估 15B/25B+Claude：2004 起 51-200 人「土首个 B2B 安防平台」（Perpa）+2025 自有品牌 SECUZI（CES 展）+IASF 2025 面见+CTO Can Gurcan/Asuman Ozuedogru→Tier2 SECUZI OEM 新品牌窗口',
22:'【r37 2026-10-25】用户双评估 25B/35B+⭐海关数据=Utepo（深圳）进口记录实证（实际贸易往来）→B Utepo 替换（海关证据=采购主体坐实）',
23:'【r37 2026-10-25】用户双评估 30A/20B（在售 HRUI+丰润达双绿灯 PoE）+新联系人 Erkut Sevin 90 531 563 77 21→B+ 双绿灯替换',
}
for i,t in UPD.items():
    assert rows[i][16] is not None
    rows[i][16]=rows[i][16]+t

# ---- r37 新行 56-79（24 家，master 双评估归属已逐家核验）----
R37=[
['56','A- 暖线（r37 新入）','Optima / Optima Mühendislik Ltd. Şti.','Ankara Sincan（Başkent OSB 厂）+İstanbul Perpa（销售办 A Blok K:8 No:701）','Optima（物理安防：路障/防撞柱/胎刺/闸机/车牌识别/防弹岗亭）','（无自有 switch 线；LPR/停车/闸机场景 PoE 需求）','（未披露）','物理准入控制制造商（2000-12 起；海外 Optima Engineering INC 沙特 LPR/停车）','Furkan Kalkan 技术经理 90507 463 05 66 furkan@optima.tc；Perpa 办 +90 212 210 70 00；optima@optima.tc','IFSEC 2023 面见+计划来深圳采购+曾受邀参观（TCL+FB 实体页号码一致核验）','A','B-','68','⭐最暖线：厂访接待+LPR 场景 PoE（8 口 120W 带+长距）+OEM Optima 贴牌','TCL 用户名单+optima-engineering.com/en/contact 搜索核验 2026-10-25（99-raw r37 §3.6）','2026-10-25','AI 28A/Claude 5C；master 备注「只处理 IP camera，对 POE switch 有兴趣」'],
['57','B 暖线（r37 新入）','Filiz Güvenlik Sistemleri Proje İnş. San. Tic. Ltd. Şti.','İzmir Konak（Mersinli 2817 Sk. No:7）','—','（集成商；CCTV+报警+火灾场景 PoE 需求）','Pinetron/Bullwark 相机（3 年保）+Mavili/Maxlogic 火灾授权服务（İzmir）','25 年报警+CCTV+火灾+车踪集成商（1994 起 51-200 人；土首批 7/24 报警监控中心=switch 采购主体）','Sadik Yildiz（Ali 员工）M90533 74 63 788；Kemal Şahin；+90 232 441 71 74 / info@filizguvenlik.com.tr','迪拜展面见（TCL Remark）','B','B-','58','CCTV 场景 PoE+报警中心汇聚；用已有迪拜关系推进','TCL 用户名单+filizguvenlik.com.tr 搜索核验 2026-10-25（99-raw r37 §3.7）','2026-10-25','AI 22B/Claude 5C'],
['58','A- 大型分销（r37 新入）','Okisan Güvenlik Teknolojileri A.Ş.','İstanbul Şişli Okmeydanı（Okisan Plaza）','（未见自有 switch 品牌；商业 PoE 现用丰润达深圳）','（分销线：商业 PoE+相机生态）','⭐Tiandy+Dahua 土耳其授权分销商（dahuasecurity.com 分销商页实证）','1986 起（Ekrem ÖZKARA）/2004 A.Ş.；5,000+ 经销网络；$8.6M/44-50 人；Ankara+İzmir 区域办','Gokhan Ozkara 外贸顾问 gokhan@okisan.com；444 1 309 / (0212) 320 28 20 / okisan@okisan.com','TCL（商业 PoE=丰润达）','A-','B','70','丰润达替换/第二供应商：商业 PoE 完整线+绑 Dahua/Tiandy 相机出货+OEM','TCL 用户名单+dahuasecurity.com 分销商页+RocketReach 搜索核验 2026-10-25（99-raw r37 §3.8）','2026-10-25','AI 18B/Claude 20C；ISAF 参展+SAHA İstanbul 会员；关联 ISAF 留档：Vatankhah=Tiandy 员工'],
['59','C 战略留档（r37 新入）','PavoTek（pavotek.com.tr）','（Pavo Group 见 110 行 1）','Pavo Group','（军通/avionics/IoT；无公开 switch 线）','（集团级未披露）','Pavo Group 电子/嵌入式子公司（Avionics/通信网络控制/电源电子/IoT/智能能源/测试）','Gizem KIZILTAN gizem.kiziltan@pavotek.com.tr（TCL）+Serkan Erturk PM serkan.erturk@pavotek.com.tr / hilal.kirlioglu@pavotek.com.tr（master）','（非客户；110 行 1 监控线）','C','C','10','不作客户跟进；监控 Pavo Group（110 行 1）','pavotek.com.tr 直连 2026-10-25（导航全链 pavo-group.com+同批新闻 TWIF 2026-07-30/Republikorp 2026-08-27）（99-raw r37 §3.2）','2026-10-25','⭐=PNetworks 母集团（110 行 1）子公司；AI 32A/Claude 8C（国防电子）'],
['60','B（r37 新入）','GMT Control（GMTCNT）','（İstanbul）','（少量 switch 打自有 logo）','少量工业 switch=Uotek（深圳）贴自有 logo（G-6405S/G-6408S）','Uotek（深圳，绿灯）','工业自动化制造商（PLC/HMI/伺服/AC 驱动/工业机器人；switch 为边缘配套）','Abdullah Aydin PM abdullahaydin@gmtcontrol.com / gmt@gmtcontrol.com','TCL（Uotek 产品页 uotek.com/product-73.html）','B','C','40','Uotek 工业线第二供应商报价（低优先）','TCL 用户名单（未独立核验，边界声明）','2026-10-25','AI 15B/Claude 15C'],
['61','C 不跟进（r37 新入）','MFD（mfd.com.tr）','İstanbul','—','工业以太网=Siemens SCALANCE（红灯）','⚠️Siemens 授权代理（深度绑定）','Siemens SIMATIC PLC/HMI/SCADA/工厂数字化代理','Mustafa Cimic PM / info@mfd.com.tr','TCL（谷歌渠道）','C','C-','5','不跟进（红灯深度绑定）','TCL 用户名单+Claude 评估（未独立核验）','2026-10-25','AI 15B/Claude 8C'],
['62','B（r37 新入）','Cebeci Grup','（İstanbul）','—','在售 ONV（深圳）工业 switch+工业串口设备','ONV（深圳，绿灯）','电信测试设备+工业 switch 分销（Transition/Westermo/Ideal/Micos 欧美品牌）','Mustafa Engin 销售与项目总监 mustafaengin@cebecigrup.com / iletisim@cebecigrup.com','TCL（备注「有国内的」）','B','C','45','ONV 工业线第二供应商（对中国供应链开放）','TCL 用户名单（未独立核验）','2026-10-25','AI 25B/Claude 20C'],
['63','B-（r37 新入）','Areskom','İstanbul Üsküdar','—','工业 MC/switch/控制设备（很多有名的牌子）','CTS（台湾，黄灯）等','工业网络方案商','info@areskom.com.tr','TCL','B-','C','35','监控（黄灯为主）','TCL 用户名单（未独立核验）','2026-10-25','AI 15B/Claude 20C'],
['64','B-（r37 新入）','İntenet','（İstanbul）','—','工业交换机 Solutions 页面（方案/集成定位）','Raisecom（中国，黄灯）；服务 TEIAŞ 土耳其电网','工业通信方案商','Ercan Ozturk GM-Owner ercan.ozturk@intenet.com.tr','TCL（谷歌渠道）','B-','C','35','监控（Raisecom 代理）','TCL 用户名单（未独立核验）','2026-10-25','AI 18B/Claude 15C'],
['65','B-（r37 新入）','Teamon','Ankara','—','多品牌 switch（主要是几个有名的牌子；AEM 等）','Planet（台湾，黄灯）为主','IT 设备多品牌分销商','info@teamon.com.tr','TCL','B-','C','30','监控（Planet 代理）','TCL 用户名单（未独立核验）','2026-10-25','AI 15B/Claude 15C'],
['66','B-（r37 新入）','İnovatech','İstanbul','—','IP CCTV 系统专区（CCTV+光纤为核心，网络配套）','（未确认）','安防/光纤/网络公司','info@inovatech.com.tr','TCL','B-','C-','25','监控（服务型）','TCL 用户名单（未独立核验）','2026-10-25','AI 18B/Claude 5C'],
['67','B-（r37 新入）','Metcom','Ankara+İstanbul Ümraniye','—','PoE switch/CCTV 配件/机架（16 槽）/工业 MC/VC 品类广','（多品牌）','CCTV/安防电子分销商','info@metcom.com.tr / ankara@metcom.com.tr','TCL','B-','B-','35','PoE 爆款低价推','TCL 用户名单（未独立核验）','2026-10-25','AI 18B/Claude 20B'],
['68','B-（r37 新入）','Egemenelektronik','（İstanbul）','—','CCTV 为主+商业 PoE+大量安防配件','（多品牌，未确认）','B2C/B2B 科技比价电商平台','Belkiz Cinar + Levent Pisman 共同老板 satis@egemenelektronik.com 90532 605 70 18（WhatsApp 已添加）','TCL（WhatsApp 已添加）','B-','C','30','WhatsApp 低成本推 PoE 爆款','TCL 用户名单（未独立核验）','2026-10-25','AI 20B/Claude 10C'],
['69','B（r37 新入）','TeknolojiPazar','İzmir Konak','Freelink（疑自有品牌）','商业 PoE（HRUI 绿灯源；Freelink FR-1621GS 300 16 口产品页）','HRUI（深圳，绿灯）','IT 零售（线下+线上）','info@teknolojipazar.com','TCL（Freelink 产品页）','B','C','45','Freelink 品牌底细+HRUI 替换','TCL 用户名单（未独立核验）','2026-10-25','AI 28A/Claude 10C；master 备注「发不过去」（物流问题待解）'],
['70','B-（r37 新入）','TekmarShop（TEKMAR）','İstanbul Ümraniye','TEKMAR（CCTV 品牌）','多品牌商业 PoE 电商（好几个牌子）','（多源；Asya Telekom 集团）','CCTV 品牌电商','info@tekmarshop.com','TCL','B-','C-','25','监控（Asya Telekom 集团同 111 行 11）','TCL 用户名单（未独立核验）','2026-10-25','AI 15B/Claude 5C'],
['71','B-（r37 新入）','BaburTech','Ankara','—','switch（含海思，疑中国产）','（多品牌）','IT 零售/电商（笔记本备件/二手/外设）','Ayse Narinsoez PM ayse@baburtech.com / destek@baburtech.com','TCL','B-','C-','25','监控','TCL 用户名单（未独立核验）','2026-10-25','AI 18B/Claude 5C'],
['72','A- 自有品牌（r37 新入）','LeMax Güvenlik','（İstanbul）','自有品牌（LG 前缀）PoE switch','8 口级商业 PoE（自有品牌；LG-ND1P802LF 产品页）','新桥（深圳，绿灯）','CCTV 分销商（OEM/品牌重塑经验）','satis@lemaxguvenlik.com','TCL（lemaxguvenlik 产品页）','A-','C','55','OEM 自有「LG」系列替换/扩型（有 OEM 经验）','TCL 用户名单（未独立核验）','2026-10-25','AI 22A/Claude 10C'],
['73','B（r37 新入）','Kiracı Bilişim=ZKR（Kıraç 集团）','（İstanbul）','ZKR（Kıraç 集团品牌）','（站点跳转 zkr.com.tr；产品未核）','（集团级）','安防/IT（澳视摄像头+天地伟业认知）','Shaalan alzitawi 董事会 shaalan@kiracbilisim.com.tr（备注：需要发 EMAIL 先联系）','TCL','B','C','35','与 111 行 10 ErETE 合并按 Kıraç 集团统一接触','TCL 用户名单+Claude 评估（跳转实主体判定）','2026-10-25','AI 15B/Claude 5C；⭐与行 10 同集团'],
['74','C（r37 新入）','RadioTeknoloji','（İstanbul）','—','（站点无法验证主营）','（未确认）','安防/通信技术（IASF 2022 参展）','Salih Yildirim PM salih.yildirim@radioteknoloji.com.tr；Abdurrahman Pehlivanoglu GM','IASF 2022','C','C-','15','老线复核（站点边界）','TCL 用户名单（站点验证失败）','2026-10-25','AI 12B/Claude 未确认（建议人工介入）'],
['75','A-（r37 新入）','TechnoPC','İstanbul Ataşehir','technopc®（工业 PC/医疗平板/国防计算）','（Switch/AP/Firewall=近期扩张配套品类；工业 PoE 采购 E-wind）','E-wind（深圳，绿灯）+Cisco/Aruba（红灯）集成','1998 本土 PC/工控机制造商（74 人，≈$16.4M）','Mithat Yuecel GM mithat.yucel@technopc.com.tr / Murat Yucel MP murat.yucel@technopc.com.tr','富通天下（TCL：工业 POE 买的 ewind 的）','A-','C','55','工业 PoE（E-wind 替换）+Marvell 工业线','TCL 用户名单+Claude 评估（未独立核验）','2026-10-25','AI 18B/Claude 10C'],
['76','C 低（r37 新入）','Bimel','Ankara（总部+4 分支）','—','switch=Planet/Beek 为主；工业类目页实列 DPTEK','Planet（黄灯）/Ruijie（黄灯）/Cisco（红灯）/DPTEK（中国）','1984 IT/网络分销（约 31 人）','Goenuel Ilbeyli 项目专家 / Engin Cebeci 电子技术员 bimel@bimel.com.tr','TCL','C','C-','20','监控（仅 DPTEK 工业类目有缝隙）','TCL 用户名单+bimel DPTEK 类目页搜索副产物 2026-10-25','2026-10-25','AI 15B/Claude 15C'],
['77','C（r37 新入）','Dacel Solutions','İstanbul Esenler','—','（switch 极边缘配套）','（自动化线为主）','1995 工业自动化方案商（11-50 人；PLC/WECON/消防/气体/KNX/HVAC；油气化工客户）','Erkan Cirit 股东 ecirit@dacel.com.tr / Ibrahim Gokcen 采购物流主管 / Ali Icoez 项目 VP','TCL','C','C-','15','监控（边缘品类）','TCL 用户名单（未独立核验）','2026-10-25','AI 15B/Claude 8C'],
['78','C（r37 新入）','Fiberden','İstanbul','—','（switch 无明确痕迹）','（光纤配件为主）','光纤 MC/光缆/SFP 电商（B2B 代理体系）','info@fiberden.com','TCL','C','C-','15','监控（边缘场景）','TCL 用户名单（未独立核验）','2026-10-25','AI 15B/Claude 10C'],
['79','B- 待评估（r37 新入）','EuroCam Güvenlik','（İstanbul）','EuroCam','（未确认）','（未确认）','（未确认）','Gokhan DEMİR CEO info@eurocamguvenlik.com.tr / gokhandemir@eurocamguvenlik.com.tr','IASF 2021','B-','—','30','下批评估（CL 建议人工介入；联系人+邮箱已备）','TCL 用户名单+master No.50 双评估（AI 15B/CL 核心业务未确认）','2026-10-25','master 50 家之一（不在 TCL 299 内）'],
]
for r in R37: assert len(r)==17, (r[0],len(r))
rows=rows+R37

# ---- ISAF 2025 新行 80-145（66 家）----
ISAF=[
['80','A 具体项目（ISAF25 新入）','Telemobil（tbi.com.tr）','İstanbul','—','2光2电 PoE（具体项目；现场展示 2光4电 PoE）','（未确认）','电信/网络','Kaan Kisacik 销售总监 kkisacik@tbi.com.tr 0216 547 67 00 / 0533 086 62 89','ISAF 2025 展台（Simon）','—（现场）','—（现场）','72','⭐重点跟进：发 2光2电 PoE 价格+交期（现场问了交期）','ISAF25 现场记录 2026-10-25（99-raw r37-isaf §A1）','2026-10-25','现场记录「可重点跟进，有具体项目」'],
['81','A 工程（ISAF25 新入）','Makros A.Ş.','İstanbul','—','工业交换机（工程用）','（未确认）','工程公司','Mustafa DEMIREL GM m.demirel@makrosisas.com.tr 0532 165 82 50 / 0212 272 47 92','ISAF 2025 展台（Evelyn，合照）','—（现场）','—（现场）','70','已报 2光10电 PoE 网管 130USD+12光12电网管 150USD；发 DDP 双清包税方案','ISAF25 现场记录（99-raw r37-isaf §A2）','2026-10-25','要双清包税运输方式'],
['82','A 军项目（ISAF25 新入）','HAFYA','İstanbul','（hafya.com.tr+www.grundig-security.tr 双域名，关系待核）','工业 4光8电 PoE 网管（防水）','（未确认）','军项目集成商（疑 Grundig Security 土生态）','Emre Makili 90544 163 36 73 / 0212 221 16 72（3 人面见合照）','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','70','发防水工业 4光8电 PoE 规格书+军项目口径；核 Grundig Security 关系（111 行 8 Hane=Grundig 分销）','ISAF25 现场记录（99-raw r37-isaf §A3）','2026-10-25','做军队项目，会用到防水交换机'],
['83','A 既有客户（ISAF25 新入）','SFP Turkey（sfpturkey.com.tr）','İstanbul','—','万兆光/2光2电/2光4电+带 bypass（深度服务中）','（Evelyn 既有客户）','SFP/光模块','UFUK GOREN ufuk.goren@sfpturkey.com.tr 0532 225 41 95 / 0212 270 57 37（+satis@/info@ 0555 090 87 37）','ISAF 2025 展台（Evelyn 既有客户）','—（现场）','—（现场）','68','维护+推 10G 光模块+bypass 系列；现场我们修图给客户（深度服务）','ISAF25 现场记录（99-raw r37-isaf §A4）','2026-10-25','推荐有特点产品给客户'],
['84','A 要样品（ISAF25 新入）','ONSIS ELEKTRONIK','（0232 区）','—','2光8 PoE 网管 bypass（要 L2）','（未确认）','电子','esef@onsis.com.tr onsis.com.tr（Ady WA）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','68','跟样品单（最后一天回来要样品，当时没带现金）+105USD 口径','ISAF25 现场记录（99-raw r37-isaf §A5）','2026-10-25','已报 105 美金'],
['85','A-（ISAF25 新入）','Netmax（Ugur Simsek）','İstanbul','—','2光8 PoE 带管理 bypass','（未确认）','网络','90532 571 08 85（Ady WA）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','66','已报 120USD，跟','ISAF25 现场记录（99-raw r37-isaf §A6）','2026-10-25','具体询价 bypass'],
['86','A-（ISAF25 新入）','bilimsateknoloji（Muharrem KILIC）','（İstanbul）','—','8光8电 PoE 网管','（未确认）','科技','bilimsateknoloji@gmail.com 0546 411 13 96 / 0850 577 93 03','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','66','已报 110USD，跟','ISAF25 现场记录（99-raw r37-isaf §A7）','2026-10-25','「最近在找这种产品」'],
['87','A- 分销（ISAF25 新入）','UGUR IMRE','（İstanbul）','—','2光8 瑞昱 PoE 网管+内置 DC48V 电源','（分销商，明确不需要 OEM）','分销商','90533 962 63 49（Ady WA；微信未通过）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','66','已报 70USD；客户回「Not bad」→改 WA 推','ISAF25 现场记录（99-raw r37-isaf §A8）','2026-10-25','分销商渠道线'],
['88','A- 价敏（ISAF25 新入）','ORAL GUVENLIK（oralcompanies.com）','（0392 区）','—','工业 PoE 网管+bypass（12光12电/2光8电两档）','（未确认）','安防集团','Muhammad AzeemUllah 经理 info@oralguvenlik.com 90533 887 03 00 / 0392 444 42 22','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','62','已报 150/90USD，客户嫌贵→给替代档或折扣空间','ISAF25 现场记录（99-raw r37-isaf §A9）','2026-10-25','2光8电带 PoE 管理（Vitesse 口径）报 90usd'],
['89','A-（ISAF25 新入）','DE secure（desecuretechnology.com）','İstanbul','—','工业 8 口 PoE 30W','（未确认）','安全技术','Serdar TURKER IT 经理 serdar.turker@desecure.com.tr 90505 786 29 19','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','62','发含当地 20% 关税的报价（DDP 口径）','ISAF25 现场记录（99-raw r37-isaf §A10）','2026-10-25','英文不太好，WA 为主'],
['90','A-（ISAF25 新入）','cansisteknoloji（Ahmet CAN）','（0332 区）','—','12光12电 PoE 带网管','（未确认）','科技','acan@cansisteknoloji.com / bilgi@ 0541 541 00 10 / 0332 447 42 26','ISAF 2025 展台（Simon）','—（现场）','—（现场）','62','已报 150USD，跟','ISAF25 现场记录（99-raw r37-isaf §A11）','2026-10-25','询价'],
['91','A 订单级（ISAF25 新入）','Sami CEUIK','（微信）','—','2光8 PoE 网管（500 台量）','光网视系（价格质量都满意）','政府项目','微信（Evelyn 添加）','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','70','500 台=订单级，已报 80-90USD，重点跟','ISAF25 现场记录（99-raw r37-isaf §A12）','2026-10-25','政府项目，需要质量好'],
['92','A 战略（ISAF25 新入）','Selim Kalaka（供应商侧线）','（微信，外国人中文很好）','—','工业 switch（找新供应商）','⭐郑州供应商打算在土耳其开工厂→需要新供应商','供应商切换窗口','WeChat: selimkalaka（Evelyn 添加）','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','68','最高优先：郑州系替代方案直接对口','ISAF25 现场记录（99-raw r37-isaf §A12）','2026-10-25','非传统客户=供应链机会'],
['93','A-（ISAF25 新入）','HCS（hescs.com）','（0352 Bilecik 区）','—','商业 PoE（问是否带 L2/L3）','（未确认）','—','Cihat TUNCBILEK PM ctuncbilek@hescs.com / info@ 90352 220 01 38 / 0212 438 25 75','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','62','发 L2+/L3 model list','ISAF25 现场记录（99-raw r37-isaf §A12）','2026-10-25','产品经理人'],
['94','A- 分销意向（ISAF25 新入）','KLASNET','（0501 区）','—','MC switch / patch cord','（未确认）','IT','mustafa@klasnet.com.tr 0501 333 55 27','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','62','问怎么成为分销商→发分销政策','ISAF25 现场记录（99-raw r37-isaf §A12）','2026-10-25',''],
['95','A-（ISAF25 新入）','F.A.S.T（fasttr.com）','（0216 区）','—','工业 5 口 PoE','（自己也代理 PLC/IO 模块）','科技','Ercan ERINC 高级销售工程师 ercan@fasttr.com 90216 574 94 34(113) / 90216 574 16 60','ISAF 2025 展台（Ady）','—（现场）','—（现场）','60','工业 PoE 小口+MC 捆绑','ISAF25 现场记录（99-raw r37-isaf §A12）','2026-10-25',''],
['96','A-（ISAF25 新入）','voltechelektronik','（0216 区）','—','工业 PoE 网管','（未确认）','电子','Hikmet EBICINOGLU info@voltechelektronik.com 0532 548 91 62 / 0551 375 12 25','ISAF 2025 展台（Evelyn/Simon）','—（现场）','—（现场）','58','发工业 PoE 网管线','ISAF25 现场记录（99-raw r37-isaf §A12）','2026-10-25',''],
['97','A-（ISAF25 新入）','LABOR Mühendislik（Ramazan DAS）','（Ankara 0412 区）','—','工业 PoE','（未确认）','工程','info@labormuhendislik.com.tr 0533 743 74 07 / 0412 257 63 26','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','58','要价格表，发','ISAF25 现场记录（99-raw r37-isaf §A12）','2026-10-25','不会英文，WA 为主'],
['98','A-（ISAF25 新入）','MEPA Elektronik','（İstanbul）','—','PoE 4/8/16/24 口（全口数=产品线级需求）','（未确认）','电子','Furkan 90535 875 11 29','ISAF 2025 展台（Ady）','—（现场）','—（现场）','58','发 PoE 全口数线','ISAF25 现场记录（99-raw r37-isaf §A12）','2026-10-25',''],
['99','A-（ISAF25 新入）','viva bilgisayar（ismet Yavuz 老板）','Hatay','—','工业交换机','（未确认）','IT（hisvision/hatayhost 多域名）','ismet Yavuz 老板 is_ya@hotmail.com / info@vivabilgisayar.com 90544 649 11 42','ISAF 2025 展台（Simon）','—（现场）','—（现场）','55','老板直联，发工业线','ISAF25 现场记录（99-raw r37-isaf §A12）','2026-10-25',''],
['100','B（ISAF25 新入）','PROVES（proves.com.tr）','（0232 区）','—','工业交换机（要报价单）','（未确认）','—','Serdar KARASU 董事会主席 bilgi@proves.com.tr 0542 563 30 82','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','50','发工业报价单','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['101','B（ISAF25 新入）','NECDET SENKACAYC','（İstanbul）','—','工业 PoE','（未确认）','—','Bilecik@hotmail.com 90533 247 59 78','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','48','发工业 PoE','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['102','B-（ISAF25 新入）','fiberix（fiberix.com.tr）','İstanbul','—','商业 switch+SFP（PoE 不常用）','⭐广州有合作伙伴','IT','karasu@fiberix.com.tr 0554 154 01 00','ISAF 2025 展台（Simon）','—（现场）','—（现场）','45','商业+SFP 推；广州合作伙伴=转介线','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['103','B-（ISAF25 新入）','acusenseteknoloji（Umit Celik）','（0216 区）','—','工业 PoE','（未确认）','科技','info@acusenseteknoloji.com 0542 839 68 33 / 0216 888 29 34','ISAF 2025 展台（Ady）','—（现场）','—（现场）','45','发工业 PoE','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25','不会英文，WA 为主'],
['104','B-（ISAF25 新入）','Duzgun Toptan Ticaret（teksarf.com）','（İstanbul）','—','商业 PoE','（未确认）','电商批发','duzgun.toptan.ticaret@gmail.com（Ady WA，不会英文）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','42','商业 PoE 爆款（WA 图片为主）','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['105','B bypass（ISAF25 新入）','IHM Technology','（0216 区）','—','bypass 独立式+2光8 带 bypass（要 SC 口，不带管理，不要光口）','（未确认）','科技','Mehmef 90532 668 98 92（Ady WA）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','50','⭐bypass 精准需求：推独立式 bypass+2光8（SC 口不网管版）','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25','bypass 专项信号'],
['106','B-（ISAF25 新入）','sinerjik（Ufuk GOKALP）','İstanbul','—','PoE splitter 1 进 2 出（要小体积）','（未确认）','能源科技','ufuk@sinerjik.net 0850 226 02 00 / 0533 210 07 40','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','40','已推 5 口 PoE 延长器（小）','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['107','B（ISAF25 新入）','Ecevit（marbim.com.tr）','（0242 区）','—','商业 PoE（对升压 5 口感兴趣）','（未确认）','—','90542 342 50 14（Ady WA）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','42','商业 PoE 升压 5 口','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25','最主要商业 PoE'],
['108','C（ISAF25 新入）','DIMAS TEKNOLOJI VE GUVENLIK','（0530 区）','—','收发器（switch 周边）','（未确认）','安防','Mustafa YILDIZ dimasteknoloji@gmail.com 0530 934 12 80','ISAF 2025 展台（Simon）','—（现场）','—（现场）','30','收发器价格+问当地是否有经销商','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25','不会英文'],
['109','C（ISAF25 新入）','basaranelektronik（Emrah Basaran 老板）','（0266 区）','—','（彩页未定产品）','（未确认）','电子','info@basaranelektronik.net 0266 357 12 08 / 0542 744 96 95','ISAF 2025 展台（Simon）','—（现场）','—（现场）','30','推商业/工业 model list','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['110','C（ISAF25 新入）','Fadi','（İstanbul）','—','收发器+交换机','（未确认）','—','90537 616 93 55（Ady WA）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','28','低成本推','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25','英文不太好'],
['111','C（ISAF25 新入）','Ali Goktork','（Ankara）','—','工业光猫','（未确认）','—','90543 760 61 56（Ady WA）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','28','工业光猫','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['112','C（ISAF25 新入）','D&N ELEKTRIK MUHENDISLIK','（0541 区）','—','switch（交换名片）','（未确认）','电气工程','Dogan TANRIKULU dn.elektrikmuhendislik@gmail.com / dn.yanginguvenliksistemleri@gmail.com 0541 549 04 37','ISAF 2025 展台（Simon）','—（现场）','—（现场）','25','跟 model list','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['113','C（ISAF25 新入）','fourline.com.tr','（0224 区）','—','（要 catalog）','（未确认）','—','info@fourline.com.tr 0224 364 18 88','ISAF 2025 展台（Simon）','—（现场）','—（现场）','25','catalog（WA 图片为主，不会英文）','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['114','B+ bypass（ISAF25 新入）','ag-bilgisayar（Aycan CAM）','（0252 区）','—','千兆 2光8 PoE 带管理带 bypass（不需要 10G）','（未确认）','IT','info@ag-bilgisayar.com 0252 999 12 60 / 0546 609 9906','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','52','⭐bypass：2光8 PoE 带管理 bypass（千兆无 10G）','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25','bypass 专项信号'],
['115','C+（ISAF25 新入）','3s.com.tr（SAVAS TULGAR）','（0533 区）','—','工业交换机','（未确认）','—','savas@3s.com.tr 0533 419 16 16','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','30','发工业线','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['116','B-（ISAF25 新入）','fhguvenlik（Hasti F. GOLLER）','（0535 区）','—','工业交换机','（未确认）','安防','hasti@fhguvenlik.com 0535 453 14 88','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','35','发工业线','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25','销售'],
['117','B bypass（ISAF25 新入）','BİLGEN ELEKTRONİK','（İstanbul）','—','2光8 带 bypass（问 PoE 功率）','（未确认）','电子','Ibrahim 90532 734 86 58（Ady WA）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','45','⭐bypass：2光8+PoE 功率参数','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25','bypass 专项信号'],
['118','C（ISAF25 新入）','ANIL（aniltelekom.com）','İstanbul','—','（名片，应该是老板）','（未确认）','电信','Cumhur OLMEZ cumhur@aniltelekom.com / aniltelekom@ 0555 976 98 08 / 0212 292 90 90','ISAF 2025 展台（Ady）','—（现场）','—（现场）','25','老板级跟进','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['119','C（ISAF25 新入）','BTM ELECTRONIC','（0532 区）','—','（可调查网站）','（未确认）','—','Mehmet Karakoyunlu mehmetkarakoyunlu@gmail.com 90532 352 48 95','ISAF 2025 展台（Simon）','—（现场）','—（现场）','25','先核主体（网站调查）','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['120','C（ISAF25 新入）','ebatek（BALKIS S.Coskun CEO）','İstanbul','—','（彩页，让用 WhatsApp 联系）','（未确认）','—','scbalkis@ebatek.com 0532 636 33 06 / 0342 215 13 22','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','25','WA 联系','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['121','C（ISAF25 新入）','turkuaz（antalyaturkuaz.com）','Antalya','—','（彩页）','（未确认）','旅游 IT','Gokhan naktar naktar@antalyaturkuaz.com 0242 345 36 91','ISAF 2025 展台（Ady）','—（现场）','—（现场）','25','WA 图片为主（不会英语）','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['122','C（ISAF25 新入）','GÜNGÖR ELEKTRONİK','（İstanbul）','—','（彩页）','（未确认）','电子','90534 793 18 74','ISAF 2025 展台（Ady）','—（现场）','—（现场）','22','WA 图片为主（不会英文）','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['123','B-（ISAF25 新入）','Sedat（微信）','（İstanbul）','—','5/8 口工业级不带 PoE 不网管+IO 模块','（未确认）','工业自动化','微信（Ady 添加）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','45','不网管工业 5/8 口+IO 模块电子 catalog','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['124','B-（ISAF25 新入）','Interland Network & Security','（İstanbul）','—','多口商业 switch','（未确认）','网络与安全','90533 833 8258（Ady WA）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','42','商业多口 model list','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['125','C（ISAF25 新入）','Smali（微信）','（İstanbul）','—','（catalog+公司 Profile）','（未确认）','—','微信（Ady 添加）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','22','发 catalog+Profile','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['126','B-（ISAF25 新入）','NAZEMCO（Osama）','（İstanbul）','—','商业 PoE','（未确认）','—','微信（Ady 添加）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','40','商业 PoE','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['127','C（ISAF25 新入）','Serkan（Alisa 客户）','（İstanbul）','—','bypass（最主要看）','（未确认）','—','微信（Ady 添加）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','25','bypass 跟进（Alisa 关系待确认）','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25','bypass 专项信号'],
['128','B+（ISAF25 新入）','Fatih A（微信）','（İstanbul）','—','工业级 2光8 PoE 不带网管','（未确认）','—','微信（Evelyn 添加）','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','48','发规格书+价格（不网管工业 2光8 PoE）','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['129','C（ISAF25 新入）','Celali Ayazoglu','（İstanbul）','—','收发器','（未确认）','—','90532 638 14 62（Evelyn WA）','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','22','收发器价格（不会英语）','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['130','B-（ISAF25 新入）','90543 780 22 23（合影客）','（Ankara）','—','商业 PoE 4/8/16 口','（未确认）','—','90543 780 22 23','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','35','商业 PoE 全口数','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['131','C（ISAF25 新入）','wechat:TeT529','（İstanbul）','—','2.5G 家用 switch','（未确认）','—','微信（Evelyn 添加）','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','20','2.5G 家用（非主力品类，留档）','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['132','C（ISAF25 新入）','Ertan Kral','（İstanbul）','—','商业 8 口（扁的那种）','（未确认）','—','90532 113 11 89（Evelyn WA）','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','25','商业 8 口','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['133','C（ISAF25 新入）','Enes Talha Karaaslan（微信）','（İstanbul）','—','工业交换机报价单','（未确认）','—','微信（Evelyn 添加）','ISAF 2025 展台（Evelyn）','—（现场）','—（现场）','28','发工业报价单','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['134','C（ISAF25 新入）','Gokhan（微信）','（İstanbul）','—','多口 switch（catalog+价格表）','（未确认）','—','微信（Ady 添加）','ISAF 2025 展台（Ady）','—（现场）','—（现场）','25','发 catalog+价格表','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['135','C（ISAF25 新入）','NORTEL İletişim（norteliletisim.com）','（0242 区）','—','（要 catalog）','（未确认）','通信','Bayram Tatli 项目经理 bayram@norteliletisim.com / info@ 90530 136 94 07 / 0242 237 27 27','ISAF 2025 展台（Simon）','—（现场）','—（现场）','25','发 catalog','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['136','C（ISAF25 新入）','Zeytek（zeytek.com.tr）','İstanbul','—','（名片+彩页）','（未确认）','—','Mehmet Zeytinli Director mehmet@zeytek.com.tr 90535 662 35 48 / 0216 755 72 33','ISAF 2025 展台（Simon）','—（现场）','—（现场）','25','跟 model list','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['137','C+（ISAF25 新入）','Bilge SECURITY SYSTEMS','（İstanbul）','—','PoE switch','（未确认）','安防','Kenan Akay bilge.guvenlik@hotmail.com 90532 120 29 31','ISAF 2025 展台（Simon）','—（现场）','—（现场）','30','推商业 PoE（WA 图片，不懂英文）','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['138','C（ISAF25 新入）','pelikanbilgisayar（Ahmet Karci）','（0541 区）','—','（名片）','（未确认）','IT（pelikan/pelimax/hpvar 多域名）','bilgi@pelikanbilgisayar.com 0541 764 78 63','ISAF 2025 展台（Simon）','—（现场）','—（现场）','22','跟','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['139','C（ISAF25 新入）','Interpos（inter-pos.com）','İstanbul','—','（名片）','（未确认）','POS','Hulusi Kultur CEO hkultur@inter-pos.com 0216 469 64 00(114) / 0532 264 89 90','ISAF 2025 展台（Simon）','—（现场）','—（现场）','22','CEO 级跟','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['140','C（ISAF25 新入）','camsanordu（0553 区）','（Tekirdağ 区）','—','（彩页，邮箱再确认）','（未确认）','军工','sclcule.o@camsanordu.com 90553 183 33 01','ISAF 2025 展台（Simon）','—（现场）','—（现场）','22','邮箱再确认跟','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['141','C（ISAF25 新入）','teknoktadestek.com','İstanbul','—','（彩页）','（未确认）','IT','90532 315 72 58','ISAF 2025 展台（Simon）','—（现场）','—（现场）','22','跟','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['142','C（ISAF25 新入）','FOLINE（foline.com.tr）','İstanbul','—','（名片）','（未确认）','—','Mahmut CESUR GM mahmut.cesur@foline.com.tr 0212 535 00 33 / 0507 225 27 28','ISAF 2025 展台（Simon）','—（现场）','—（现场）','25','GM 级跟','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['143','C+（ISAF25 新入）','Holil','（İstanbul）','—','PoE switch','（未确认）','—','90538 985 94 29','ISAF 2025 展台（Simon）','—（现场）','—（现场）','28','推商业 PoE','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['144','C（ISAF25 新入）','Marmaris Bilişim','Marmaris','—','PoE splitter / PON 问（拿别家公司产品册问的）','（未确认）','Bilişim','0533 358 54 80','ISAF 2025 展台（Simon）','—（现场）','—（现场）','22','WA 图片为主（不会英文）','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25',''],
['145','C（ISAF25 新入）','hiperonline.com','Eskişehir','—','多口 switch（一直在看）','（未确认）','电商','eskisehir@hiperonline.com 90506 024 59 86','ISAF 2025 展台（Ady）','—（现场）','—（现场）','25','推商业 PoE','ISAF25 现场记录（99-raw r37-isaf §B）','2026-10-25','不会英文'],
]
for r in ISAF: assert len(r)==17, (r[0],len(r))
rows=rows+ISAF

with open(P,'w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f,lineterminator='\r\n',quoting=csv.QUOTE_MINIMAL)
    w.writerows(rows)
chk=list(csv.reader(open(P,encoding='utf-8-sig',newline='')))
assert len(chk)==146, len(chk)
assert all(len(r)==17 for r in chk)
assert [r[0] for r in chk[1:]]==[str(i) for i in range(1,146)]
assert sum('r37 2026-10-25' in r[16] for r in chk[1:24])==23
assert sum('ISAF' in r[1] for r in chk[80:146])==66
print('111 CSV OK 145 行')

wb=openpyxl.load_workbook(X); ws=wb.active
assert ws.max_row==56
for i,t in UPD.items():
    c=ws.cell(row=i+1,column=17); c.value=str(c.value or '')+t
for r in R37+ISAF: ws.append(r)
wb.save(X)
wb2=openpyxl.load_workbook(X); ws2=wb2.active
assert ws2.max_row==146 and ws2.max_column==17
assert 'r37' in str(ws2.cell(row=3,column=17).value)
assert str(ws2.cell(row=57,column=3).value).startswith('Optima')
assert str(ws2.cell(row=146,column=3).value).startswith('hiperonline')
print('111 XLSX OK 146x17')
