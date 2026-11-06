# -*- coding: utf-8 -*-
"""r75 附录数据：白牌层（OEM）+ Perpa B K:8 名册 + İzmir 路线 + 两条品牌标签修正。"""

D = {}

D['8'] = """
#### r75 补：**名称订正 + 五个自有商标 + 它已经有两条中国线**

**🛑 修正 r73（B/008）**：档案原名写「**Hane Elektronik**」—— **法定名是 `HAN ELEKTRONİK`**（站点 `hanelektronik.com`），被推翻的写法是「Hane」。

| 项 | 内容 |
|---|---|
| 法定全称 | **HAN ELEKTRONİK Bilgisayar ve Güvenlik Sistemleri A.Ş.** |
| 成立 / 人数 | **2000** · **51–200 人** |
| 地址 | **Mehmet Akif Mah. Bahariye Cad. (Basın Ekspres Yolu) 1904 Sok. No:15/A, Küçükçekmece / İstanbul** |
| 电话 | **444 1 426** · `info@hanelektronik.com` · 支持站 `destek.hanelektronik.com` |
| **自有商标（官网「BELGELERİMİZ」逐条）** | **Han Elektronik 商标注册证** · **FOREDGE 分销证** · **VIDEOPARK** · **SPY / SPY AHD / SPY IP / SPY Mobile / SPY Alarm / SPY Network Solution** · **AVerFire / AVerGuard / AVerSound 商标** · **M-Sight（金属探测门 / X 光机）** · **ISO 9001 · ISO 10002 · TS-12540** |
| 独家代理 | **MILESIGHT（土耳其唯一授权分销 + 其土耳其办事处）**：2018「最高增值+最快成长伙伴」、**2023「最有价值伙伴」** · **UNIWIZ（唯一）** · **PANASONIC 可寻址消防** · **AXXON / Hoop Cam** · Honeywell · TNA · AlienFence · **Shelly** · GRUNDIG · Nevio · Monitoreal |
| **⭐ 中国品牌线** | **Ruijie** + **Reyee** —— 官网品牌表明列 |
| 产品 | IP/模拟相机、NVR/DVR、**PoE 交换机 25 款**（FOREDGE AI1016GC 16 口 250 W 云管理 / AI1024GC 24 口 300–360 W / AI806M；VIDEOPARK VP-24PG-2UPG-2SFP 400 W）、SFP、无线网桥 VP-2300CPE、金属探测门 / X 光机 |

⇒ **判读**：它有**两层中国供应链** —— **OEM 白牌（FOREDGE + VIDEOPARK，深圳特征）** + **品牌代理（Ruijie + Reyee）**。
⇒ **它不需要「帮它建品牌」，它需要「换掉现在那个深圳工厂」**：**同规格、更硬的价、更准的交期、能给它云管理。**
⇒ ⚠ **别跟它谈 Ruijie 授权** —— 它自己就在卖 Ruijie 和 Reyee。
"""

D['9'] = """
#### r75 补：**它其实有 BDCOM —— 这个锚价是「本地可比」，不是海外参考**

**🛑 修正 r73（B/009）**：档案把 Öncü 记成「Sec-on 自有品牌 + 工业 PoE 实锤」，**漏了它同时代理 BDCOM**。

| 在售工业交换机（官网原文） | 品牌 |
|---|---|
| `SC-E208-4FH` **8 口 PoE 受管工业** | **Sec-on（自有）** |
| `IES200-V25-4S2T8P` **8 口 100/1000M 受管 PoE 工业** | **BDCOM** |
| `IES200-V25-4S10T` **10 口受管工业** | **BDCOM** |
| `IES2000-TW8S8P` | **BDCOM** |

⇒ **影响**：**BDCOM 在土耳其已有正式代理（Öncü）** ⇒ 我们手里的 BDCOM 工业 $399 锚价**是本地可比的**，不是海外参考价。
⇒ **报价必须对着 Öncü 的 BDCOM 价打，不是对着 Moxa。**
"""

D['10'] = """
#### r75 补：**Edge-Core + EtherWan 双代理 + 台湾据点 + 自有网络学校**

| 项 | 内容 |
|---|---|
| 法定全称 | **ERETE BİLGİ SİS. DIŞ TİC. VE SAN. LTD. ŞTİ.** |
| 成立 | **2001 年 12 月** · 创始人 **Pınar Kabil · Murat Soyak · Timur Yıldız** |
| 地址 | **19 Mayıs Mah. Güven Sok. No:4/2, Şişli / İstanbul** |
| 电话 / 邮箱 | **+90 212 212 81 03** · Faks 212 82 96 · GSM 533 778 00 84 · `erete@erete.com.tr`；GM **Murat Soyak** `murat.soyak@erete.com.tr` |
| **据点** | **伊斯坦布尔 + 台湾**（自述「Tayvan'da ve İstanbul'da merkezleri bulunmaktadır」） |
| 代理 | **EDGE-CORE（Accton 集团）土耳其分销商** ← 主动作 · **ETHERWAN**（加固型交换机 + 光纤转换器）· **VOSCOM**（光纤转换器代表）· **XPCABLE**（结构化布线，**EGM 认证**）· **XPS Active System** |
| B2B 平台 | **`eretekne.com`**（= 它自己的店，**不是独立公司**） |
| 特色 | **「Erete Network Okulu」** —— 每月固定网络培训、出认证证书（土耳其首创） |
| 项目面 | 美国多州交通信号 · 土耳其多处 **MOBESE** 用 EtherWan hardened（−40~+70 ℃，洞穴/水下/军用野外）· 军工/机场/银行/高校 |
| 保修话术 | XPCable：Cat5e **15 年系统性能保证**，Cat6 **终身** |

⇒ **软肋**：**Edge-Core / EtherWan 都是台系价格**，纯价格标打不动。
⇒ **话术**：「**EtherWan 那一档我给你同防护等级、价格低一档**」；或「**XPS 那条线我给你做 OEM**（你贴 XPS，我出货）」。
⇒ ⚠ **`XPS Active System` 身份仍未定**（「自有」vs「ONV 贴牌」两说并存）—— 见主文 §14 空白。
"""

D['11'] = """
#### r75 补：**拆分 —— `Eretekne` 是 ErETE 的店，`Isee` 是 Asya Telekom 的牌**

**🛑 修正 r73（B/011）**：档案把「**Eretekne（+ Isee，同 Asya Telekom 集团）**」并列写在一条里 —— **被推翻的是「Eretekne 与 Isee 属于同一集团」这个暗示**。真相是**两家互不相干的公司，只是被同一批 B2B 目录并列展示**。

| 名称 | 真实身份 |
|---|---|
| **`eretekne.com`** | **ErETE Bilgi Sis. Dış Tic. ve San. Ltd. Şti. 的自有 B2B 下单平台**（隐私条款落款即 ErETE，地址 Şişli Güven Sok. 4/2） |
| **`ISEE`（isee.com.tr）** | **ASYA TELEKOMÜNİKASYON VE NET GÜVENLİK SİSTEMLERİ SAN. VE TİC. LTD. ŞTİ. 的自有品牌** —— 见下一节（本轮新建档） |

⚠ **两家不可合并任何字段。**
"""

D['12'] = """
#### r75 补：**注册地址沿革 + 规模第三源 + 「İzmir 最大」是自称**

| 项 | 内容 |
|---|---|
| VKN | **2030341121**（NACE **464308**） |
| **法定 İşyeri Adresi** | **HALKAPINAR MAH. 1442 SK. TESİSAT İŞMERKEZİ No:1 L, KONAK / İZMİR 35170** |
| **地址变更（VKN 记录）** | 旧 **HALKAPINAR MAH. 1443 SK. No:3 A KONAK** → 新 **1442 SK. Tesisat İşmerkezi No:1 L** |
| 对外展示地址 | **Adalet Mh. Manas Blv. Folkart Towers No:39 İç Kapı 2511, Bayraklı** |
| 第三/第四点 | **Manisa — Yunusemre 75. Yıl Mah. 5391. Sok. No:41**（0533 272 31 91）· **İstanbul 分店 2018 Q2** |
| **规模三源** | zoominfo **283 人 / $10–25M**；同站另一处 **250–499 人 / $15.6M**；rocketreach **3 人** ⇒ **区间「中型，≥50 人可信，250+ 存疑」** |
| 自述 | 「**İzmir'in en büyük dağıtıcı firması**」—— **自我宣称，无第三方印证** |

⇒ **拜访动线（一天）**：**Folkart Towers（总部/展厅）→ Halkapınar Tesisat İş Merkezi（注册地/仓库）→ 1443 Sk. 旧址一带的 Gıda Çarşısı（整片电气电子批发）→ TeleOne（Mithatpaşa No:146）**，四站互距 1.5–5 km。
"""

D['17'] = """
#### r75 补：**无线专精 —— 卖交换机给它没用，卖「无线 + 交换一体」的杆上箱方案**

| 项 | 内容 |
|---|---|
| 法定全称 | **RF Teknoloji Makine ve Otomasyon San. Tic. Ltd. Şti.** |
| 成立 | **2012**（自述「12 年以上无线通信经验」） |
| 地址 | **Tevfik Bey Mah. Şehit Adem Tamrak Sok. No:2/5, Sefaköy / Küçükçekmece / İstanbul** |
| 电话 / 邮箱 | **+90 212 210 95 65** · `info@rfteknoloji.com.tr` |
| 代理 | **CalAmp（土耳其代表 / 分销）** · **3OneData 工业线**（13 个非受管 PoE 工业 SKU） |
| 产品面 | RF 数据电台 / 无线数据机 / GSM-GPRS-3G/4G 数据机 / **CNC 控制单元** / **Smart Grid 网关** / 工业自动化 |
| 自我定位 | 「**Kablosuz Haberleşme Uzmanı**」（无线通信专家） |

⇒ **判读**：它是**无线专精 + 交换机配套**的结构。**别跟它比交换机单价**，要卖**「无线回传 + 杆上 PoE 交换」的一体箱**。
"""

D['18'] = """
#### r75 补：**`iotsistem` 与 `iosistem` 是两家不同公司 —— 绝不能合并**

**🛑 修正 r73（B/018）**：档案只记了 `iotsistem`，**没记 `iosistem.com.tr`** —— 两者名字一字母之差，**业务完全不同**。

| | **`iotsistem.com` — IoT Sistem** | **`iosistem.com.tr` — IOSistem Endüstriyel Teknolojiler** |
|---|---|---|
| 身份 | 电商 / 白牌运营 | **电力系统集成商（EPC）** |
| 自有线 | **MLB-`E4xxx`**：`4101-5 / 4102-5-F / 4103-5-P / 4105-8 / 4106-8-F / 4202-10-F / 4204-28-F`（工业受管/非受管，IP30，MTBF >25 年，双 DC 12–58 V） | 无 |
| 代理 | **USR IoT 土耳其官方分销（Bosgem）** | 无（做方案） |
| 地址 | — | **İnönü Mh. Kayışdağı Cd. No:128, Kandiş İş Mrk. K:1, Ataşehir / İstanbul** |
| 电话 | — | **+90 216 577 66 82** · `info@iosistem.com.tr` |
| 成立 / 规模 | — | **2023**（rocketreach）· **2 人** · CTO **Emre Anayurtlu** |
| 业务 | 工业交换 / 网关 / 4G 路由零售 | **SCADA · TEİAŞ RTU · EDAŞ RTU · 轨交 SDH-PDH · PAX 电话 · 数据中心能耗监测** |

⇒ **`iotsistem` 是竞品也是潜在 OEM 客户**（它已经在做我们想做的事）。
⇒ **`iosistem` 是集成商，卖方案不卖货** —— 单独建档，别串号。
"""

D['19'] = """
#### r75 补：**它就是 Perpa B K:8 No:989 —— 同一层里的自有品牌，8 口 PoE 标价 $1,000**

| 项 | 内容 |
|---|---|
| 法定全称 | **LANSAN TEKNOLOJİ A.Ş.**（招牌 **LANSAN Network Bağlantı Ekipmanları**） |
| 成立 | **2019-12-04** |
| 工商地址 | **Halil Rıfat Paşa Mah. Yüzer Havuz Sok. Perpa Ticaret Merkezi B Blok No:1/1 İç Kapı No:989, Şişli / İstanbul 34384** |
| 另一地址 | Kayabaşı Mah. Ulubatlı Hasan Cad. Work Plaza No:2H D:43 D Blok, Başakşehir（未验证） |
| 电话 | **0212 955 02 30 / 0312 955 02 00 / 0312 955 01 02**（安卡拉号段为主，疑为客服中心） |
| 自有线 | **LNS-** 全档：SFP/QSFP/DAC/AOC · 交换机 · 媒体转换器 · PoE · 网卡 · 延长器 · 光纤配件 · 结构化布线 |
| **官网标价（未税）** | `LNS-1310P` **8 口 PoE = $1,000** · `LNS-1324P` **24 口 PoE = $1,427** · `LNS-1306-P` 6 口 PoE **$242** · `LNS-1308` **8 口 SFP 骨干 = $1,755** · `LNS-3713-02` 10G 网卡 **119,259 TL** |

⇒ **$1,000 一台 8 口 PoE 不是定价，是「只做工程配套」的信号**：客户是布线和工程包，交换机搭着卖。
⇒ **它同时是「价格伞证据」**：本地白牌都能把 8 口 PoE 卖到 $1,000 ⇒ 市场对工程级 PoE 的容忍度极高。
⇒ **也是最容易被我们打穿的一家**：同规格整机成本远低于它售价的 1/10。
⇒ ⚠ **数据陷阱**：`find.com.tr` 上它的 **MERSİS `1234567890123456` / E-tebligat `12345-67890-12345` 都是占位假号** ⇒ 该页不能作工商依据。
"""

D['22'] = """
#### r75 补：**DMO 前三大供应商 —— 且法定主体与「1999」要对齐**

**🛑 修正 r74（B/022）**：① 被推翻的说法「**TeleOne 成立于 1999**」—— **1999 是品牌/项目史，法人成立于 2003-10-06**；② 被推翻的说法「**品牌名单未公开**」—— **名单已拿到**。

| 项 | 内容 |
|---|---|
| 法定全称 | **TELEONE BİLGİ VE İLETİŞİM HİZMETLERİ SANAYİ VE TİCARET LİMİTED ŞİRKETİ** |
| **VKN** | **8370410675** |
| 工商地址 | **YEŞİLTEPE MH. M.PAŞA CD. No:146, KONAK / İZMİR** |
| 成立 / 税务开始 | **成立 2003-10-06**；税务登记（işe başlama）**2009-01-22** |
| 地址（对外） | Mithatpaşa Cad. Zafet Apt. No:146 K:1 D:2-3, Konak 35260 |
| 电话 / 邮箱 | **0850 221 95 95**（另一处 (0232) 425 50 53）· `info@teleone.com.tr` |
| **代理品牌（补上 r74 空白）** | **Brickcom · Nuuo · Digital Watchdog**（三家土耳其分销） |
| **⭐⭐ DMO** | **2014 年起进入 Devlet Malzeme Ofisi**，自述「**DMO 本领域最大前三家供应商**」 |
| 资质 | **TSE-HYB 2008 起** · **ISO + OHSAS 2008 起** · **Bilişim 500 两次入榜** · **2016 全球最佳突破 Brickcom 分销商** |
| 业务 | Video İzleme · Video Analiz · **Networking** · 指挥控制中心 · 远程监控；**800 m² 伊兹密尔总部 + 安卡拉地区经理部**；全国各市合作伙伴服务**公共机构** |
| NACE 变更 | 「GÜVENLİK SİSTEMLERİ HİZMET FAALİYETLERİ」→「**BİLGİSAYAR PROGRAMLAMA FAALİYETLERİ**」⇒ 重心转向软件/系统 |

⇒ **它是全表里唯一「品牌代理 + DMO 前三 + 软件化」三合一**。
⇒ **谈 DMO K 码与规格书，比谈价格有用十倍。**
"""

D['52'] = """
#### r75 补：**`upTech` 是 Nokta 自己的牌 —— 不是中系品牌**

**🛑 修正 r72（A/052）**：被推翻的说法「**upTech 是土耳其市场上的中系开关品牌之一**」。官网 JSON-LD 明确写着 `brand: upTech, manufacturer: Nokta Elektronik` ⇒ **upTech = Nokta 的自有品牌**（2008 / 商标 13951）。

| 项 | 内容 |
|---|---|
| `upTech` | **Nokta 自有品牌**（制造方 = Nokta Elektronik） |
| **它在售的 13 个品牌** | upTech · Dahua · **Oring Networking** · Amphenol · **Planet** · Gewiss · **Edge-Core** · Goldtool · ATC · **Ruijie** · Inno Instrument · Noyafa（+ 东芝/WD 硬盘） |

⇒ **它早有 Edge-Core / Planet / Oring / Ruijie 四条工业线** ⇒ **不能打「你缺工业」**。
⇒ **正确话术**：「**upTech 的工厂，换我。**」—— 同规格、更硬的价、更准的交期、能给你做定制壳。
"""

D['62'] = """
#### r75 补：**白牌层比代理层更肥 + Perpa B K:8 一层 8 家 + İzmir 一天路线（本轮要点）**

> 用户第 28 次「继续」。完整版见 `144-oem-white-label-layer-and-perpa-floor-8-route-2026-11-06.md`。

**① 两家品牌标签是错的（必须先改，否则话术打错人）**

| 被推翻的说法 | 真相 |
|---|---|
| 「**Ekosinerji = 土本地工业交换机品牌**」 | **EKOS Teknoloji ve Elektrik A.Ş.**（原 Ekosinerji，BİST：**EKOS**）—— **中压开关柜 / GIS / RMU / 箱变 / 变电站自动化 / NTP-PTP 时间服务器**；2000 成立；Balıkesir OSB + Gebze Güney Yanyol Cd. No:78 + İstinye；101–250 人；$7.6–7.8M；董事长 **Tarık Akbaş**；**土耳其 GIS 第一家也是最大一家** ⇒ **它是「ODM 客户」（要 IEC 61850-3 交换机 + PTP），不是竞品** |
| 「**Tipro = 土本地品牌**」 | **Tipro d.o.o.（斯洛文尼亚 / 卢布尔雅那）** —— 模块化工业键盘 + 触摸终端（BeFREE 20/22）；**土耳其代理 = GSL，2018 起**；**不做以太网交换机** |

**② ⭐⭐⭐ 真正难打的对手：GSL Mühendislik**

| 项 | 内容 |
|---|---|
| 全称 / 成立 | **GSL Mühendislik Sanayi ve Ticaret A.Ş.** · **1988 年 5 月，安卡拉**（38 年） |
| 地址 / 电话 | **İlkbahar Mah. 612. Cadde No:9, Çankaya / Ankara 06550** · **0312 473 3540**（Faks 3544）· `info@gsl.com.tr` |
| 办公室 / 人数 | 安卡拉 + 伊斯坦布尔 · **25–49 人** |
| 代理 | **Moxa（2003 年起，21 年+）** · **Kyland** · Robustel · Digi · **Tipro（2018 起）** · Pro Optix · RuggON · Transcend · TXOne · 历史含 EKOS |
| 线上规模 | `store.gsl.com.tr`：工业以太网 **311 SKU / 受管 119**；MOXA 363 · Kyland 27 |
| 技术动作 | **自己做 FAT**（Kyland 交换机在安卡拉办公室完成 FAT）· 办认证工业网络培训 |
| 价格伞 | Moxa `EDS-208-M-SC` RS Türkiye **13,988.58 TL 未税**（≈$280）· `EDS-208A-T` 美国挂牌 **$278.58** · `EDS-208A-MM-ST` RS Türkiye **26,091 TL 未税**（≈$521）⇒ **土耳其对「8 口工业非受管」的心理价位 $280–520** |

⇒ **它是正规军，护城河是「Moxa+Kyland 双线 + 工程服务」，不是价格。**
⇒ **唯一可行切口**：「**Moxa 的标你继续报 Moxa；报不下来的标，用我的线兜底** —— 不冲突、不抢你代理权。」

**③ ⭐⭐⭐ 白牌层：9 家自有品牌 = 9 个 OEM 客户**

| 公司 | 自有品牌 | 关键事实 |
|---|---|---|
| **Asya Telekomünikasyon / ISEE** ⭐新 | **ISEE** | **1995-12-27**；**Perpa B Blok K:7-8-9 No:908**（和我们客户同一层）；0850 433 27 92；11–50 人；**132 批进口 / 5 家供应商**；`ISS-2006P` 4 口 PoE 78 W / `ISS-1026P` 24 口 400 W / `ISS-1040` 28×SFP+4×10G；决策人 **Baysal Günel · Serkan Ur · Harun Baştürk** ⇒ **全表最像 OEM 客户的一家**（ISS 只有 3 个型号，无工业线/无 2.5G/无 bt） |
| **HAN Elektronik A.Ş.**（原名误记 Hane） | **FOREDGE · VIDEOPARK · SPY 家族 · AVer 系列 · M-Sight** | **2000**；Küçükçekmece；444 1 426；51–200 人；**Milesight 土耳其唯一授权 + 其土耳其办事处**（2023 最有价值伙伴）；**UNIWIZ 唯一**；Panasonic 消防；AXXON；**Ruijie + Reyee** ⇒ **已有两层中国供应链，要的是「换掉现在那个深圳工厂」** |
| **Lansan Teknoloji A.Ş.** | **LNS-** | **2019-12-04**；**Perpa B No:989**；8 口 PoE 标价 **$1,000** / 24 口 **$1,427** ⇒ **价格伞证据 + 最易打穿** |
| Nokta Elektronik | **upTech** | **upTech = 自有牌（非中系）**；在售 13 品牌含 Edge-Core/Planet/Oring/Ruijie |
| Öncü Güvenlik | **Sec-on** | 同时代理 **BDCOM**（`IES200-V25-4S2T8P` 等）⇒ **BDCOM $399 锚价是本地可比** |
| Karer · Snexus · Cenova · Novacom | KR-* / SN- / SWP / NVC- | 已在 r72–r73 建档 |

**④ ⭐⭐ Perpa B K:8 一条走廊 = 8 家（其中 4 家是客户）**
**B 836** CCTV Depo · **B 902-904** Cenova · **B 906-907** Nokta · **B 908** Asya Telekom/ISEE ⭐ · **B 989** Lansan ⭐ · **B 1105** Perpa Otomasyon/Sanpa · **B 1246** Perpa Kameram · **B 1276** ALM Elektronik
⇒ 电梯上 **A K:5（295 GelecekBT、419 Güvenlik Toptancım）→ A K:8（841 Nokta 二号店、808-810/940 Koza）**。**半天 8 家，4 家有档案。**

**⑤ ⭐⭐ İzmir 一天路线**
**Folkart Towers（CCS 总部）→ Halkapınar 1442 Sk. Tesisat İş Merkezi（CCS 注册地/仓库）→ 1443 Sk. Gıda Çarşısı（整片电气电子批发）→ Mithatpaşa No:146（TeleOne）**，四站互距 1.5–5 km。

**⑥ 两条工商级修正**
- **CCS**：法定 İşyeri Adresi = **Halkapınar 1442 Sk. Tesisat İş Merkezi No:1/L**（旧 1443 Sk. No:3/A）；另 **Manisa** 点；规模第三源 zoominfo **283 人 / $10–25M**；「İzmir 最大」是**自称**。
- **TeleOne**：**VKN 8370410675 · 法人成立 2003-10-06（1999 是品牌史）· 代理 Brickcom/Nuoo/Digital Watchdog · 2014 起进 DMO、自述前三**。

**证据等级**：`gsl.com.tr` / `store.gsl.com.tr` / `ekosinerji.com` / `erete.com.tr` / `hanelektronik.com` / `asyatelekom.net` / `isee.com.tr` / `perpa.com.tr` / `lansan.com.tr` / `teleone.com.tr` / `vknsorgula.net` / `rsdelivers.com` 逐字。
**空白**：**Asya Telekom 的 5 家供应商未取到** · `XPS Active System` 身份未定 · EKOS 的 IEC 61850-3 交换机来源未取到 · `Lansan` 真 VKN/MERSİS 未取到（公开页是假号）· FOREDGE 代工厂未定 · **所有电话仍未试拨** · **DMO K 码仍未反查（TeleOne 最值得查）**。
"""
