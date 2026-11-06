# -*- coding: utf-8 -*-
"""r80 附录数据：定价规则拆双轨（白牌 ÷2.95 vs 真实 MSRP 0.8–1.0×）+ Nokta 工商身份 + 电力段三条新线索。"""

D = {}

D['52'] = """
#### r80 补：**工商级身份补完，并推翻 r79 的「2000 年成立」**

| 字段 | 内容 |
|---|---|
| 法定全称 | **NOKTA ELEKTRONİK VE BİLİŞİM SİSTEMLERİ SANAYİ TİCARET ANONİM ŞİRKETİ** |
| **VKN（税号）** | **6310730521**（**Şişli** 税务局） |
| **MERSİS** | **0631-0730-5210-0020** |
| **商业登记号** | **555138-0**（登记号 555138） |
| **注册成立** | **2005-05-26**（原名 **… LTD. ŞTİ.**，后转 **A.Ş.**） |
| **实缴资本** | **30,000,000.00 ₺**（≈$600k） |
| NACE | **#465202**（电子器件与零件批发） |
| 地址 | **Perpa Ticaret Merkezi A Blok Kat:2 No:1**；信函址 **B Blok Kat:8 No:906**, 34384 Şişli |
| 电话 / 邮箱 | **0212 222 87 80** · `nokta@noktaelektronik.net` |
| KEP | `noktaelektronikvebilisim@hs03.kep.tr` |
| **ETBİS 登记** | **2024-05-02** |
| **商标** | **`upTech` = Nokta 注册的商标**（土耳其专利商标局） |

**🛑 修正 r79**：r79 依 SignalHire 记「成立 2000」。**工商登记实为 2005-05-26**；「2000」是公司自我表述（可能指前身或个体经营起点）。**对外一律用 2005-05-26 + VKN 6310730521。**

**⇒ 三条判读**
1. **实缴资本 3,000 万 ₺（≈$600k）** ⇒ **A 级里「中等偏上」的重资产分销商**，比 Cenova（LTD，Perpa 三层）更「公司化」。
2. **「2000 → 2005」这个差** ⇒ **它习惯把历史讲长 5 年**；**谈判中凡「我们做了 25 年」都要打折听，但不要点破。**
3. **`upTech` 是注册商标** ⇒ **它不会换牌，但可以换「牌下面的机器」** ⇒ **话术：不换 `upTech`，换里面的板子。**
**⇒ 分级 78 → 81。**
**⚠ 空白**：生产设施的具体地址仍未取（现有只是 Perpa 办公室）。
"""

D['62'] = """
#### r80 总览：**定价规则拆双轨 + 三条电力段新线索 + Nokta 工商身份**

**① 🛑 修正 r79：「÷2.95」不是通用规律，是「白牌挂牌虚高」的特例**
| 类型 | 案例 | 挂牌 | DMO 净价 | 倍率 |
|---|---|---|---|---|
| **白牌（挂牌是锚）** | RUBISEC `RS-ES-200-28PS` | $1,200 | **$406** | **2.96×** |
| | RUBISEC `RS-IS-300-12GPX` | $3,600 | **$1,221** | **2.95×** |
| **真实 MSRP 品牌** | **PLANET `IGS-801T`** | **US MSRP $172**（Newegg $179） | **$139** | **0.81×** |
**⇒ 新规则（三句）**：① **有公开 MSRP / 全球零售可比的品牌（PLANET / Moxa / Cisco / HPE）⇒ DMO ≈ 0.8–1.0× MSRP**，直接引用；② **只有「官网自己挂一张价、无第三方可比」的白牌 ⇒ ÷2.3–3.0**；③ **探针：去 Newegg / planetechusa / DigiKey 搜同型号 —— 搜得到走①，搜不到走②。**
**⇒ 实际影响**：**Moxa / Planet / Cisco 的历史价格锚不需要重算**，省掉一整轮返工。

**② ⭐⭐ 新 K 码 `K5884` = İNFOGEN DANIŞMANLIK VE BİLİŞİM A.Ş.**
- 挂 **PLANET `IGS-801T`**（8 口工业千兆**非** PoE，**−40~75 ℃**，IP30，16 Gbps）：**6,955.49 ₺ 未税 / 8,346.59 ₺ 含税 ≈ $139 / $167**，产品码 **131798**。
- **合同 2026-03-10 → 2028-03-10（刚续两年）** · 电话 **0216 706 1845** · 另有 `K3193` / `K4329`（r76）。
- **它同时是 D-Link 与 PLANET 的 DMO 挂单方** ⇒ **「中低端进口网络设备」在政府渠道的实际操盘手** —— **客户表里没有的一类角色**。
- **PLANET 的 8 口工业 PoE 不在 DMO** ⇒ **这一格在 İNFOGEN 这里也是空的。**
**⇒ 打法：不替代 PLANET，补它缺的那一格。**

**③ ⭐⭐⭐ 三条新线索，全在电力/工业自动化段（与现有 146 家客户零重叠）**
| 线索 | 身份 | 关键数据 |
|---|---|---|
| **İNFOGEN** | 渠道（D-Link + PLANET） | **`K5884` · 合同至 2028-03 · 0216 706 1845** |
| **SİMGENET MÜHENDİSLİK ENERJİ SAN. VE TİC. LTD. ŞTİ.** | **3onedata 土耳其代理 + 自研 SMGOS + TEİAŞ OPGW** | **2020-04-05 · Orhantepe Mah. Girne Sk. No:25A Kartal/İstanbul（迁 Tomurcuk Sok. 4B）· +90 555 600 45 06 · info@simgenet.net**；代理 `MES5400`（30 口模块化 L3，**IEC 61850-3**，HSR/PRP，1588v2）· `MES5300-28GS` · `MES5300-24GT4GS` · `MES5200` · `MES6400PHR-8GT4XS` · `ICS5400TSN`；自研 `Simgenet Teleprotection Unit V2` |
| **İSAC** | **Advantech 工业以太网交换机授权伙伴** | **0850 60 60 180 · bilgi@isac.com.tr**；`EKI-2000/5000/7000/9000` 全线（`EKI-2525P`、`EKI-2728`）；自我定位「工业传感器 + 自动化供应商」 |

**④ ⭐⭐ 电力段（IEC 61850-3）代理地图 —— 这一格已被 6 家分完**
| 品牌 | 土耳其代理 | 认证强项 |
|---|---|---|
| **Moxa** | **GSL Mühendislik** | **IEC 61850-3 · EN 50155 · NEMA TS2 · IEC 62443** |
| **Kyland** | **GSL Mühendislik** | **IEC 61850-3 · EN 50155** |
| **EtherWan** | **ErETE**（`EX47000` / `EX47080-00B`） | **IEC 61850 / IEEE 1613**，−40~75 ℃ |
| **3onedata** | **Simgenet** | **IEC 61850-3 · HSR/PRP · 1588v2** |
| **JetNet（Korenix）** | **Beijer Electronics Türkiye** | **IEC 61850-3 · DNV · eMark · ITxPT · EN 50155** |
| **Advantech** | **İSAC** | CE/FCC/UL（**工业级，非变电站认证**） |
| **RUBISEC** | Birkil Savunma（`RS-IS-300-12GPX`） | ⚠ **未见 IEC 61850-3 声明** |
**⇒ 我方进这一段的唯一路线：做「第二源」而不是「第三品牌」** —— 找**已有电力客户但品牌单一**的 Simgenet / ErETE / İSAC，给一个**同规格、能并行投标**的备份。

**⑤ ⭐⭐ DMO「工业 8 口」两轴定稿**
| 轴 | 型号 | 净价 | ≈USD | 供应商 |
|---|---|---|---|---|
| 非 PoE | **PLANET `IGS-801T`**（−40~75 ℃，16 Gbps） | **6,955.49 ₺** | **$139** | **İNFOGEN `K5884`** |
| PoE 白牌 | **DAHUA `DH-PFSC28GT1-120D`**（120 W，−30~65 ℃） | 18,993.83 ₺ | $380 | `55483` |
| PoE 12 口 | **RUBISEC `RS-IS-300-12GP`**（**暂时无货**） | 29,204.18 ₺ | $584 | Birkil `K4525` |
| PoE 8 口 | RUBISEC `RS-IS-200-10GP` | 33,405–38,522 ₺ | $668–770 | `K4525` |
| PoE+10G+宽温 | **RUBISEC `RS-IS-300-12GPX`**（−40~80 ℃，240 W） | 61,075.68 ₺ | $1,221 | `K4525` |
| 工业 12 口 | ALCATEL `OS6465T-P12` | 65,342–66,451 ₺ | $1,306–1,328 | — |
| PoE+ 天花板 | **CISCO `IE-3300-8P2S-E`** | 115,787.25 ₺ | **$2,315** | 4S `K4427` |
**⇒ 我方 $500–700 现在有三条支撑**：Dahua $380 = **非受管 + 120 W + −30 ℃**；RUBISEC $584–770 = **无货 / 非宽温 / 资料不全**；Cisco $2,315 = 天花板。⇒ **「受管 + 240 W + 整机 −40~75 ℃ + 有货」在 $500–700 = 唯一解。**

**⑥ ⭐ Nokta 工商身份（详见本节另一段）**：**VKN 6310730521 · MERSİS 0631-0730-5210-0020 · 登记 555138-0 · 成立 2005-05-26 · 实缴 30,000,000 ₺ · `upTech` 注册商标** ⇒ **推翻 r79「2000 年成立」**，分级 78 → **81**。

**证据等级**：**`www.dmo.gov.tr/Katalog/Urun/Detay/6254602_1277284`**（PLANET `IGS-801T` 6,955.49 / 8,346.59 ₺ · 131798-K5884 · İNFOGEN · 0216 7061845 · 合同 2026-03-10→2028-03-10）· `planet.neteon.net`（**US MSRP $172**）· `newegg.com`（$179）· `planetechusa.com`（$172 / `IGS-800T` $177.53）· `dmo.tr/Katalog/Arama?...p=17` 与 `dmo.gov.tr/Arama?...p=14`（PLANET 26 SKU · `GSD-1002M` 9,951.70 · MAIPU 28 · LANDE 5 · PEPLINK 4）· `eticaret.gov.tr`（Nokta MERSİS）· `noktaelektronik.net/tr/yasal-bilgiler`（**VKN / MERSİS / Sicil / Şişli VD**）· `noktaelektronik.com.tr/yasal-bilgiler`（B Blok K:8 No:906）· `b2bhint.com`（**2005-05-26 · 30,000,000 ₺ · NACE 465202 · 原名 LTD**）· `noktaelektronik.net/en/hakkimizda`（**upTech 注册商标**）· `simgenet.net` + `/urunler.php` + `/photel-sdh`（3onedata 全线 · SMGOS · TEİAŞ OPGW · PLC · RTU）· `tikla.com.tr` + `firmadan.com` + `yandex.com.tr/maps`（Simgenet 地址/成立/迁址）· `isac.com.tr` ×3（Advantech 授权 · 0850 60 60 180）· `erete.com.tr`（EtherWan `EX47000` IEC 61850 / IEEE 1613）· `gsl.com.tr/moxa-endustriyel-ethernet-switch.html`（Moxa/Kyland 认证矩阵）· `beijerelektronik.com.tr`（JetNet 认证矩阵）—— **共 24 个来源**。

**空白**：İNFOGEN 的工商身份（只有电话 + K 码）· Simgenet 员工数/营收/VKN（2020 年成立、手机号做总机 ⇒ 疑 ≤10 人，**未证实**）· İSAC 法定全称/地址/VKN · **Karer / CryptoLink / Novacom 的 VKN（b2bhint 与 eticaret 均未命中）** · PLANET 的 8 口工业 PoE 是否在 DMO · **RUBISEC 是否有 IEC 61850-3 声明** · **所有电话未试拨**（新增 İNFOGEN 0216 706 1845 · Simgenet +90 555 600 45 06 · İSAC 0850 60 60 180）。
"""
