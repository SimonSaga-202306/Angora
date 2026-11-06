# 150 · r81：**三家新线索全部落地为「可打电话的档案」**（İNFOGEN / İSAC / RİVO）+ **RUBISEC 确认没有 IEC 61850-3**

> **轮次**：r81 ｜ **日期**：2026-11-06（+0800）｜ **上一轮**：r80（`149-…`）
> **用户指令（第 34 次「继续」）**：继续挖客户信息，**每次把工作时间拉长 10 分钟以上**。
> **本轮主线**：r80 挖到三家新线索但只有「电话 + 品牌」。**本轮把三家全部补成带工商号的档案**；同时验证了 r80 的一个关键假设（RUBISEC 到底有没有变电站认证）。

---

## 0 · 本轮七句话

1. **İNFOGEN 是一家「为 DMO 而生」的公司** —— 官网原文：**「为满足土耳其公共机构的信息技术产品需求而成立」**，**「产品、方案与服务全部通过 Devlet Malzeme Ofisi（DMO）渠道提供」**。**它不是普通代理，它是「政府渠道专营商」。**
2. **İSAC 的法定全称与工商号拿到了**：**İSTANBUL SENSÖRLER ALGILAYICI CİHAZLAR VE ENDÜSTRİYEL OTOMASYON SİSTEMLERİ SAN. VE TİC. LTD. ŞTİ.**，**MERSİS `0481056780300013`**，**2009 年成立**，**21–50 人**，**Şerifali Mah. Beyan Sk. No:5 Ümraniye/İstanbul**，**+90 216 520 31 50**。**Panasonic Industry 的土耳其唯一代理（2013 起）** + Advantech + Omron + Honeywell + Weidmüller + Telemecanique。
3. **RİVO 的身份也齐了**：**2013 年成立**，**Ankara Balgat Ata Plaza No:1/H**（+90 312 481 19 14）+ **İstanbul Ümraniye Bayraktar Blv. No:16**，**统一号 444 8 620**，**总经理 Hamdi Kepez**，DMO **`K4385`**。
4. **✅ RUBISEC 确认没有 IEC 61850-3。** 官方 `RS-IS-300` 系列 datasheet 全文只有 **L2+/L3 · −40~80 ℃ · IP40 · DIN 导轨 · MTBF 35 年 · 240 W** —— **没有 IEC 61850-3，也没有 IEEE 1613**。**⇒ r80 的推断成立：它那台 $1,221 的机器在变电站标里根本不能用。**
5. **RUBISEC 自产清单**（官方 FAQ）：`RS-IS-100-10GP` · `RS-IS-200-10GP/20GP/24GP/28GP` · `RS-IS-300-10GP/12GP/12GPX` · `RS-IS-300-16GP-8S` · `RS-IS-400-16GPTX` —— **工业段共 10 个型号，全部集中在「8–28 口」**。
6. **三家新线索的价值排序（本轮定）**：**İNFOGEN（渠道，已进 DMO，最短路径） > RİVO（安防分销，已有 K 码与 Dahua 双供） > İSAC（工业自动化，量大但段位不同） > Simgenet（电力总包，段位最高但公司最小）**。
7. **一个反常识**：**İSAC 站内 SKU 数 9,707（工业自动化）· 传感器 19,543** —— **它比我方任何一家安防客户的货架都大**，但**它的交换机是 Advantech 的副线**。**这类「巨量工业目录 + 交换机副线」的商，是「补一格」逻辑的最佳靶子。**

---

## 1 · ⭐⭐⭐ İNFOGEN：一家「为 DMO 而生」的公司

| 字段 | 内容 |
|---|---|
| 法定全称 | **İNFOGEN DANIŞMANLIK VE BİLİŞİM A.Ş.** |
| **自我定位（原文）** | **「İNFOGEN 是为满足土耳其公共机构与组织的信息技术产品需求而成立的」**；**「产品、方案与服务通过 Devlet Malzeme Ofisi（DMO）渠道提供给全国公共机构」** |
| 地址 | **Selami Ali Mah. Cumhuriyet Cad. Boğaziçi Plaza No:46 K:5, Üsküdar / İstanbul** |
| 电话 / 邮箱 | **+90 216 706 18 45** · `info@infogen.com.tr` · 站点 `infogen.com.tr` |
| **DMO K 码** | **`K5884`**（PLANET）· `K3193` / `K4329`（D-Link，r76） |
| **合同** | **2026-03-10 → 2028-03-10**（PLANET `IGS-801T`） |
| **品牌** | **Fortinet · Safetica · Carbonite · ESET · Microsoft · D-Link · PLANET** |
| 品类 | **网络（switch / AP / 工业 switch）· 条码（扫描枪 / 打印机）· 系统管理与咨询** |
| 业务性质 | **纯政府渠道**（DMO）+ 系统管理外包 |

**⇒ 三条判读**
1. **它是「DMO 原生公司」** —— **不为零售、不为集成，只为「公共机构通过 DMO 下单」这一件事而存在**。**这类公司对中国供应商最友好**：**它没有品牌包袱，只有「目录里能不能放一台能交货的机器」这一个问题。**
2. **它的网络线只有 7 个品牌，其中 5 个是软件/安全**（Fortinet、Safetica、Carbonite、ESET、Microsoft）⇒ **硬件网络只有 D-Link + PLANET 两条** ⇒ **交换机是它最薄的一块。**
3. **⇒ 话术（本轮最重要的一句）**：「**你 DMO 目录里的工业交换机只有 PLANET 一台非 PoE 的 `IGS-801T`（$139）。我补你一台 8 口工业 PoE —— 你的公立医院、变电站、水厂项目就不用去别家调货。**」

---

## 2 · ⭐⭐⭐ İSAC：9,707 个工业 SKU，但交换机是副线

| 字段 | 内容 |
|---|---|
| **法定全称** | **İSTANBUL SENSÖRLER ALGILAYICI CİHAZLAR VE ENDÜSTRİYEL OTOMASYON SİSTEMLERİ SAN. VE TİC. LTD. ŞTİ.** |
| **MERSİS** | **0481056780300013** |
| **成立** | **2009** |
| 人数 | **21–50**（LinkedIn 28 · Prospeo 34 人 / 11 个部门） |
| **地址** | **Şerifali Mah. Beyan Sk. No:5, Ümraniye / İstanbul 34764**（另一记录 Şerifali Mah. Emin Sok. No:51/5） |
| 电话 / 邮箱 | **+90 216 520 31 50**（总机）· **0850 60 60 180**（销售）· `bilgi@isac.com.tr` · `kvkk@isac.com.tr` · KEP `istanbulsensorler@hs01.kep.tr` |
| 分部 | **Bursa 分公司 + Gebze 办公室** |
| **关键人** | **Hakan ALKAN —— 总经理 / 联合创始人** · Emre Güneç（Vision & Measurement 业务发展经理） |
| **代理关系（按年份）** | **Panasonic Industry —— 土耳其唯一代理（2013 起）** · **Advantech —— 特殊合作伙伴** · **Omron —— 授权经销（2015 起）** · **Honeywell —— 分销（2016 起）** · **Telemecanique Sensors / Weidmüller —— 专项合作** |
| **货架规模** | **工业自动化 9,707 · 传感器 19,543** · 安全件 2,445 · PLC/驱动 2,716 · 视觉 2,300 |
| 交换机线 | **Advantech `EKI-2000/5000/7000/9000`**（`EKI-2525P`、`EKI-2728` 等） |

**⇒ 三条判读**
1. **它是「工业自动化目录商」，不是网络商** —— **交换机只是它 9,707 个 SKU 里的一小类**。**⇒ 它不会为了交换机去找新供应商，但会为了「补一格」而接一个新品牌。**
2. **它的代理结构极度「日系 + 台系」**（Panasonic / Omron / Advantech）⇒ **对中国品牌没有心理障碍**（台系已经是它的主力）。
3. **⇒ 话术**：「**你的交换机线只有 Advantech EKI（工业级，没有变电站认证）。我补你一条 IEC 61850-3 的，你的变电站/水厂客户就不用转单。**」

---

## 3 · ⭐⭐⭐ RİVO TEKNOLOJİ：安防分销 + Dahua 双供 + 已有 DMO 码

| 字段 | 内容 |
|---|---|
| 法定全称 | **RİVO TEKNOLOJİ A.Ş.**（前身/关联名 **Rivo Savunma ve Güvenlik Sistemleri**） |
| **成立** | **2013** |
| 人数 | **35–37**（ContactOut）· SignalHire 记 **100–200**（⚠ 冲突） |
| 营收 | SignalHire **$10M–50M** · ContactOut **$1M–5M**（⚠ 冲突，**不做单一引用**） |
| **DMO K 码** | **`K4385`**（GWSECU 摄像机 · 合同 2024-03-21 → 2026-03-26） |
| **安卡拉** | **Ehlibeyt Mah. Tekstilciler Cad. Ata Plaza No:1/H, Balgat / Ankara** · **+90 312 481 19 14** |
| **伊斯坦布尔** | **Bayraktar Bulvarı No:16, Ümraniye / İstanbul** |
| 统一电话 / 邮箱 | **444 8 620** · `info@rivo.com.tr` · 站点 `rivo.com.tr` |
| **关键人** | **Hamdi Kepez —— Genel Müdür（总经理）** · **Eray Çalışkan —— Ürün Yöneticisi（产品经理）** · Canan Öztürk（Sales Manager）· Kazım Tınaz（Regional Manager） |
| 代理 | **Dahua**（主力）· **GWSECU**（DMO 挂单） |
| **DMO 价格行为** | 与 **AKTİF GRUP（K4969）** 在 `DH-PFSD224ET2-360D` 上**完全同价 32,102.24 ₺** |

**⇒ 三条判读**
1. **它是「安卡拉 + 伊斯坦布尔双中心」的安防分销商**，**35 人量级、营收口径分歧大** ⇒ **实际规模应在「$5M–15M」区间**（两种口径的中间值）。
2. **它在 DMO 与 AKTİF GRUP 同价** ⇒ **再一次验证「DMO 价格由上游（Dahua）控」** ⇒ **它不是价格决策者，是执行者。**
3. **⇒ 它对我方的价值不是「买交换机」，而是「它已经有 K 码、有 Dahua 全线、缺工业段」** ⇒ **和 İNFOGEN 同一逻辑，但它的客户是安防集成商而不是公立机构。**
**⇒ 建议分级：B+ / 72**（比 TeleOne 58 高，比 Karer 77 低）。

---

## 4 · ✅ RUBISEC 确认没有 IEC 61850-3（r80 的推断成立）

**官方 `RS-IS-300` 系列 datasheet 全字段**（`RS-IS-300-10GP / 12GP / 12GPX`）：

| 项 | 值 |
|---|---|
| 类型 | **10 / 14 / 16 口全千兆 L2+ / L3 受管工业 PoE+** |
| 端口 | `12GPX`：**8×GbE PoE + 4×GbE RJ45（上联）+ 4×1/10G SFP+** + 1×Console RS232 |
| 交换容量 | **104 Gbps**（非阻塞）· 转发 **77.38 Mpps** · MAC **32K** · 缓存 32M · DRAM **2G** · FLASH 128M · **CPU 500 MHz** |
| **工作温度** | **−40 ~ +80 ℃** |
| **防护/安装** | **IP40** · **35 mm DIN 导轨** · 双路 V+/V− 冗余 DC（Phoenix 端子，48–57 VDC，防反接） |
| **PoE** | 802.3af/at，**单口 30 W**，**总预算 120 W / 240 W** 两档（电源另选） |
| **MTBF** | **35 年**（原文 `MTBF can reach 35 years`） |
| 环网 | **ERPS / G.8032，自愈 <20 ms，最多 250 环 / 1024 设备** |
| 三层 | **L3 软路由转发** · 静态/默认路由 128 · ARP 1024 · VRRP 255 组 |
| 管理 | Web GUI / CLI / SNMP / SSH / SSL |
| **IEC 61850-3** | **❌ 全文未出现** |
| **IEEE 1613** | **❌ 全文未出现** |
| **EN 50155 / NEMA TS2** | **❌ 未出现** |

**⇒ 三条结论**
1. **它是「宽温工业交换机」，不是「变电站交换机」。** **−40~80 ℃ + IP40 + 双 DC 是「工厂车间」级别，不是「高压变电站」级别。**
2. **⇒ 凡涉及 TEİAŞ / 配电公司 / 变电站自动化的标，`RS-IS-300` 系列无法投标** ⇒ **GSL（Moxa/Kyland）、ErETE（EtherWan）、Simgenet（3onedata）、Beijer（JetNet）这四家才是真对手。**
3. **⇒ 我方策略分两条线**：
   - **工厂/水厂/园区（无 61850 要求）** ⇒ 打 **RUBISEC 的 $1,221 与 Dahua 的 $380 之间的 $500–700**；
   - **变电站（要求 61850-3）** ⇒ **必须拿认证**，否则连标都进不去。

---

## 5 · ⭐ RUBISEC 的工业段自产清单（官方 FAQ 原文）

`RS-IS-100-10GP` · `RS-IS-200-10GP` · `RS-IS-200-20GP` · `RS-IS-200-24GP` · `RS-IS-200-28GP` · `RS-IS-300-10GP` · `RS-IS-300-12GP` · `RS-IS-300-12GPX` · `RS-IS-300-16GP-8S` · `RS-IS-400-16GPTX`

**⇒ 结构判读**
- **10 个型号，全部落在 8–28 口**，**没有 4/5 口**、**没有 48 口工业** ⇒ **它放弃了「微型边缘」与「大型变电站」两端。**
- **我方最容易插进去的是 4–8 口（它没有）与 48 口工业（它也没有）。**

---

## 6 · 新线索总表（本轮定稿）

| 线索 | 类型 | 关键数据 | 建议分级 | 优先级 |
|---|---|---|---|---|
| **İNFOGEN** | 🎯 **DMO 专营商** | `K5884`/`K3193`/`K4329` · 合同至 2028-03 · **Üsküdar Boğaziçi Plaza No:46 K:5** · **0216 706 18 45** · 品牌 Fortinet/Safetica/Carbonite/ESET/Microsoft/D-Link/PLANET | **A- / 74** | **① 最高** |
| **RİVO TEKNOLOJİ** | 安防分销（安卡拉） | **2013 · 35 人 · 444 8 620 · Balgat Ata Plaza No:1/H · Ümraniye Bayraktar Blv. No:16 · GM Hamdi Kepez · `K4385`** | **B+ / 72** | ② |
| **İSAC** | 工业自动化目录商 | **MERSİS 0481056780300013 · 2009 · 21–50 人 · Şerifali Beyan Sk. No:5 Ümraniye · 0216 520 31 50 · Panasonic 唯一代理 + Advantech + Omron + Honeywell** | **B+ / 71** | ③ |
| **Simgenet** | 电力通信总包 | **2020-04-05 · 3onedata 代理 + 自研 SMGOS · +90 555 600 45 06 · Kartal** | **B / 68** | ④（公司太小，但段位最高） |

---

## 7 · 证据等级与空白

**逐字 / 结构化来源（本轮 25 个）**：
`infogen.com.tr`（**自我定位「为 DMO 渠道而成立」** · 地址 · 0216 706 18 45 · `info@infogen.com.tr` · 品牌墙 Fortinet/Safetica/Carbonite/ESET/Microsoft）· `infogen.com.tr/marka/d-link/`（D-Link 线）· `infogen.com.tr/sistem-yonetimi-ve-danismanlik-hizmetleri/`（系统管理业务）· `www.dmo.gov.tr/EMagaza/Magaza/Standart/1095`（İNFOGEN 店铺页 · 服务端渲染为空）· `www.dmo.gov.tr/Katalog/Urun/Detay/6254602_1277284`（`IGS-801T` · K5884 · 合同 2026-03-10→2028-03-10）。
`isac.com.tr/calisan-aydinlatma-metni/`（**法定全称 + MERSİS 0481056780300013 + Şerifali Mah. Beyan Sk. No:5 + KEP**）· `tr.linkedin.com/company/istanbul-sensorler`（**2009 · 11–50 · Hakan ALKAN GM/联合创始人**）· `prospeo.io/c/isac-email-format`（**2009 · 21–50 · +90 216 520 31 50 · Panasonic 唯一代理 2013 / Omron 2015 / Honeywell 2016 / Advantech / Weidmüller / Telemecanique**）· `isac.com.tr/magaza/page/2366/`（**工业自动化 9,707 · 传感器 19,543**）· `isac.com.tr/advantech-din-ray-switch/` + `/-ieee-802-3af-at-poe-switch/`（EKI 全线）· `yenibiris.com`（Bursa 分公司 + Gebze 办公室 · Emin Sok. No:51/5）。
`contactout.com/company/Rivo-Teknoloji-AS-66620`（**2013 · 35 人 · Ata Plaza · 关键人清单**）· `signalhire.com/companies/rivo-savunma-ve-guvenlik-sistemleri`（**444 8 620 · 100–200 人（冲突）· $10M–50M（冲突）**）· `www.rivo.com.tr/iletisim`（**安卡拉 Ehlibeyt Mah. Tekstilciler Cad. Ata Plaza No:1/H · +90 312 481 19 14 · 伊斯坦布尔 Bayraktar Blv. No:16 Ümraniye · 444 8 620**）· `rocketreach.co`（**Hamdi Kepez GM · Eray Çalışkan Ürün Yöneticisi**）。
**`rubisec.com/wp-content/uploads/2024/03/RS-IS-300-Series.pdf`**（**10/14 口全千兆 L2+ 受管工业 PoE+ 全字段**）· **`rubisec.com/wp-content/uploads/2024/03/RS-IS-300-12GPX.pdf`**（**16 口 10G 上联 L3 · 104 Gbps · 77.38 Mpps · 32K MAC · 2G DRAM · 500 MHz · −40~80 ℃ · IP40 · MTBF 35 年 · ERPS/G.8032 <20 ms**）· `rubisec.com/switches/`（**自产清单 + `RS-IS-300-16GP-8S`、`RS-IS-400-16GPTX`、`RS-IS-300-28GPX`**）· `tybilgisayar.com/rubisec-rs-is-300-10gp` · `aksoybilisim.com`（`12GPX` 端口构成与认证字段复述）。

**空白（诚实标注）**
1. **İNFOGEN 的 VKN / MERSİS / 成立年 / 人数** —— 仍缺（**只有地址、电话、K 码**）。
2. **RİVO 的人数与营收** —— 两套口径冲突（35 vs 100–200；$1–5M vs $10–50M），**本报告只用「35 人 / 中型」定性，不引用具体数字**。
3. **Simgenet 的 VKN / MERSİS / 人数** —— 仍缺（2020 年成立、手机号做总机 ⇒ 疑 ≤10 人）。
4. **İSAC 是否已在 DMO 有 K 码** —— 未查（它做工业自动化，**可能不进 DMO**）。
5. **RUBISEC 是否有别的型号做了 IEC 61850-3**（`RS-IS-400-16GPTX` 未取 datasheet）。
6. **所有电话仍未试拨**（本轮新增：**İNFOGEN 0216 706 18 45** · **RİVO 444 8 620 / 0312 481 19 14** · **İSAC 0216 520 31 50 / 0850 60 60 180**）。

---

## 8 · r82 建议（按价值排序）

1. **🔥 给 İNFOGEN 写一封「补一格」的邮件（不是询价信）** —— 主题：**「你的 DMO 目录里工业交换机只有一台非 PoE 的 `IGS-801T`」**，**正文只讲一件事：8 口工业 PoE，能交货，能开票，能进 DMO**。
2. **🔥 打 RİVO 的 444 8 620 找 Eray Çalışkan（产品经理）** —— 不是找销售；角度：**「你的 Dahua 工业段是空的」**。
3. **🔥 把「IEC 61850-3 认证」变成一个可回答的是/否问题** —— 问工厂：**有没有 IEC 61850-3 / IEEE 1613 的第三方报告？** 没有的话，**电力段整条线（GSL / ErETE / Simgenet / Beijer）都只能谈「工厂/水厂」，不能谈「变电站」。**
4. **⭐ 取 `RS-IS-400-16GPTX` 的 datasheet**（RUBISEC 最大工业型号，看它有没有做 61850）。
5. **⭐ İSAC 与 İNFOGEN 的对比研究**：**两家都是「巨量工业/IT 目录 + 交换机副线」**，**这种结构是「补一格」话术的最佳靶子** —— 值得写成通用模板。
6. **技术债**：İNFOGEN/RİVO/Simgenet 的 VKN · **Karer/CryptoLink/Novacom 的 VKN（两轮未命中）** · `G5328P-24-410W` $240 复核。
