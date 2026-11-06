# -*- coding: utf-8 -*-
"""r81 附录数据：三条新线索落地（İNFOGEN / İSAC / RİVO）+ RUBISEC 无 IEC 61850-3 的确认。"""

D = {}

D['62'] = """
#### r81 总览：**三条新线索全部落成「可打电话的档案」+ RUBISEC 确认没有 IEC 61850-3**

**① ⭐⭐⭐ İNFOGEN = 一家「为 DMO 而生」的公司**
- 官网原文：**「İNFOGEN 是为满足土耳其公共机构与组织的信息技术产品需求而成立的」**；**「产品、方案与服务通过 Devlet Malzeme Ofisi（DMO）渠道提供给全国公共机构」**。
- 地址 **Selami Ali Mah. Cumhuriyet Cad. Boğaziçi Plaza No:46 K:5, Üsküdar / İstanbul** · **+90 216 706 18 45** · `info@infogen.com.tr`。
- **K 码 `K5884`（PLANET，合同 2026-03-10→2028-03-10）· `K3193` / `K4329`（D-Link）**。
- 品牌：**Fortinet · Safetica · Carbonite · ESET · Microsoft · D-Link · PLANET** —— **5 个是软件/安全，硬件网络只有 D-Link + PLANET 两条**。
- ⇒ **交换机是它最薄的一块；它没有品牌包袱，只有一个问题：「目录里能不能放一台能交货的机器」。**
- ⇒ **话术**：「**你 DMO 目录里的工业交换机只有一台非 PoE 的 `IGS-801T`（$139）。我补你一台 8 口工业 PoE —— 你的公立医院、变电站、水厂项目就不用去别家调货。**」
- **建议分级 A- / 74，优先级最高。**

**② ⭐⭐⭐ İSAC = 9,707 个工业 SKU，但交换机是副线**
| 字段 | 内容 |
|---|---|
| **法定全称** | **İSTANBUL SENSÖRLER ALGILAYICI CİHAZLAR VE ENDÜSTRİYEL OTOMASYON SİSTEMLERİ SAN. VE TİC. LTD. ŞTİ.** |
| **MERSİS** | **0481056780300013** |
| **成立 / 人数** | **2009** · **21–50**（LinkedIn 28 / Prospeo 34 人 ÷ 11 部门） |
| 地址 | **Şerifali Mah. Beyan Sk. No:5, Ümraniye / İstanbul 34764**（另记 Emin Sok. No:51/5） |
| 电话 / 邮箱 | **+90 216 520 31 50** · **0850 60 60 180** · `bilgi@isac.com.tr` · KEP `istanbulsensorler@hs01.kep.tr` |
| 分部 | **Bursa 分公司 + Gebze 办公室** |
| **关键人** | **Hakan ALKAN —— 总经理 / 联合创始人** · Emre Güneç（Vision & Measurement 业务发展） |
| **代理（按年份）** | **Panasonic Industry —— 土耳其唯一代理（2013 起）** · **Advantech —— 特殊合作** · **Omron —— 授权经销（2015 起）** · **Honeywell —— 分销（2016 起）** · Telemecanique Sensors / Weidmüller |
| 货架规模 | **工业自动化 9,707 · 传感器 19,543** · 安全件 2,445 · PLC/驱动 2,716 · 视觉 2,300 |
| 交换机线 | **Advantech `EKI-2000/5000/7000/9000`** |
⇒ **代理结构极度「日系 + 台系」⇒ 对中国品牌无心理障碍；交换机只是 9,707 个 SKU 里的一小类 ⇒ 「补一格」逻辑的最佳靶子。**
⇒ **建议分级 B+ / 71。**

**③ ⭐⭐⭐ RİVO TEKNOLOJİ = 安防分销 + Dahua 双供 + 已有 DMO 码**
| 字段 | 内容 |
|---|---|
| 法定全称 | **RİVO TEKNOLOJİ A.Ş.** |
| **成立** | **2013** |
| 人数 / 营收 | **35–37 人**（ContactOut）vs **100–200**（SignalHire）⚠ · **$1–5M** vs **$10–50M** ⚠ ⇒ **只用「35 人 / 中型」定性，不引具体数** |
| **DMO K 码** | **`K4385`**（GWSECU，合同 2024-03-21→2026-03-26） |
| **安卡拉** | **Ehlibeyt Mah. Tekstilciler Cad. Ata Plaza No:1/H, Balgat / Ankara** · **+90 312 481 19 14** |
| **伊斯坦布尔** | **Bayraktar Bulvarı No:16, Ümraniye / İstanbul** |
| 统一电话 / 邮箱 | **444 8 620** · `info@rivo.com.tr` |
| **关键人** | **Hamdi Kepez —— Genel Müdür（总经理）** · **Eray Çalışkan —— Ürün Yöneticisi（产品经理）** · Canan Öztürk（Sales Manager） |
| 价格行为 | 与 **AKTİF GRUP（K4969）** 在 `DH-PFSD224ET2-360D` 上**完全同价 32,102.24 ₺** |
⇒ **它在 DMO 与 AKTİF GRUP 同价 ⇒ 价格由 Dahua（上游）控，它是执行者不是决策者** ⇒ **它对我方的价值是「已有 K 码 + Dahua 全线 + 缺工业段」。**
⇒ **建议分级 B+ / 72。打电话找 Eray Çalışkan（产品经理），不要找销售。**

**④ ✅ RUBISEC 确认没有 IEC 61850-3（r80 的推断成立）**
官方 `RS-IS-300-12GPX` datasheet 全字段：**16 口 10G 上联 L3 · 104 Gbps · 77.38 Mpps · 32K MAC · DRAM 2G · CPU 500 MHz · −40~80 ℃ · IP40 · 35 mm DIN · 双路 48–57 VDC 防反接 · PoE 单口 30 W / 总 120 W 或 240 W · MTBF 35 年 · ERPS/G.8032 自愈 <20 ms · 250 环/1024 设备**。
**⇒ `IEC 61850-3` / `IEEE 1613` / `EN 50155` / `NEMA TS2` 全文均未出现。**
**⇒ 它是「宽温工业交换机」，不是「变电站交换机」** ⇒ **凡涉及 TEİAŞ / 配电公司 / 变电站自动化的标，`RS-IS-300` 系列无法投标。**
**⇒ 我方策略分两条线**：**工厂/水厂/园区（无 61850 要求）⇒ 打 $500–700 那一档；变电站（要求 61850-3）⇒ 必须先拿认证，否则连标都进不去。**

**⑤ ⭐ RUBISEC 工业段自产清单（官方 FAQ 原文）**
`RS-IS-100-10GP` · `RS-IS-200-10GP` · `RS-IS-200-20GP` · `RS-IS-200-24GP` · `RS-IS-200-28GP` · `RS-IS-300-10GP` · `RS-IS-300-12GP` · `RS-IS-300-12GPX` · `RS-IS-300-16GP-8S` · `RS-IS-400-16GPTX`
⇒ **10 个型号全部落在 8–28 口；没有 4/5 口，也没有 48 口工业** ⇒ **我方最容易插进去的是 4–8 口与 48 口工业两端。**

**⑥ 新线索总表**
| 线索 | 类型 | 关键数据 | 分级 | 优先级 |
|---|---|---|---|---|
| **İNFOGEN** | **DMO 专营商** | `K5884`/`K3193`/`K4329` · 合同至 2028-03 · Üsküdar Boğaziçi Plaza No:46 K:5 · **0216 706 18 45** | **A- / 74** | ① |
| **RİVO** | 安防分销（安卡拉+伊斯坦布尔） | **2013 · 444 8 620 · 0312 481 19 14 · GM Hamdi Kepez · Ürün Yön. Eray Çalışkan · `K4385`** | **B+ / 72** | ② |
| **İSAC** | 工业自动化目录商 | **MERSİS 0481056780300013 · 2009 · 21–50 人 · Şerifali Beyan Sk. No:5 · 0216 520 31 50 · Panasonic 唯一代理** | **B+ / 71** | ③ |
| **Simgenet** | 电力通信总包 | **2020-04-05 · 3onedata 代理 + SMGOS · +90 555 600 45 06 · Kartal** | **B / 68** | ④ |

**证据等级**：`infogen.com.tr`（DMO 定位 · 地址 · 电话 · 品牌墙）· `infogen.com.tr/marka/d-link/` · `www.dmo.gov.tr/EMagaza/Magaza/Standart/1095` · `www.dmo.gov.tr/Katalog/Urun/Detay/6254602_1277284` · `isac.com.tr/calisan-aydinlatma-metni/`（**法定全称 + MERSİS**）· `tr.linkedin.com/company/istanbul-sensorler`（2009 · Hakan ALKAN）· `prospeo.io/c/isac-email-format`（**+90 216 520 31 50 · Panasonic 唯一代理 2013 / Omron 2015 / Honeywell 2016**）· `isac.com.tr/magaza/page/2366/`（**9,707 / 19,543**）· `yenibiris.com`（Bursa + Gebze）· `contactout.com`（Rivo 2013 · 35 人）· `signalhire.com`（444 8 620 · 口径冲突）· `www.rivo.com.tr/iletisim`（**两址 + 0312 481 19 14**）· `rocketreach.co`（Hamdi Kepez / Eray Çalışkan）· **`rubisec.com/wp-content/uploads/2024/03/RS-IS-300-12GPX.pdf`** + `RS-IS-300-Series.pdf` + `rubisec.com/switches/` · `tybilgisayar.com` · `aksoybilisim.com` —— **共 25 个来源**。

**空白**：İNFOGEN 的 VKN/MERSİS/成立年/人数（只有地址+电话+K 码）· **RİVO 人数与营收两套口径冲突（不引具体数）** · Simgenet 的 VKN/人数 · **İSAC 是否已在 DMO 有 K 码未查** · RUBISEC 是否有别的型号做了 IEC 61850-3（`RS-IS-400-16GPTX` 未取）· **所有电话未试拨**（新增 İNFOGEN 0216 706 18 45 · RİVO 444 8 620 / 0312 481 19 14 · İSAC 0216 520 31 50 / 0850 60 60 180）。
"""
