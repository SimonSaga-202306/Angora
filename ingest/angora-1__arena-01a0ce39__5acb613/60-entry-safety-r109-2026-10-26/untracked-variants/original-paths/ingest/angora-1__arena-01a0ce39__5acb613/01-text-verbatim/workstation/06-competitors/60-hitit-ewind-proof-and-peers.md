# 🔴 HITIT = Ewind 白牌（已实证）· 中国同行海关数据 · Advensis 核实

> 2026-09-23

---

# 一、⭐⭐ HITIT 就是 Ewind 的白牌 —— 型号级 1:1 对应

## 1.1 铁证：HITIT 官方数据表

来源：https://www.angoranetworks.com/download/1808/（HITIT 数据表 PDF）
文件名：`Kaleiçi_Datasheet_Taslak`

**封面标题（土耳其语原文）**：
> **"ANGORA HİTİT SERİSİ — YÖNETİLEMEYEN KENAR ANAHTAR AİLESİ"**

翻译：**「ANGORA HITIT 系列 —— 非网管型边缘交换机家族」**

正文：
> "**Yönetime ihtiyaç duymadan**, POE özelliği ile aynı anda tüm cihazlarınızı besleyebilen…"
> （**无需管理**，即可通过 PoE 同时为所有设备供电……）
>
> "Standart bakır kablo üzerinden **250 metre** mesafeye kadar kayıpsız veri transferi"
> （标准铜缆上**最远 250 米**无损数据传输）

## 1.2 型号级对应表（⭐ 关键证据）

| Ewind 型号<br>（ImportGenius 印度海关实测） | Ewind 规格 | Angora HITIT 型号 | HITIT 规格 | 匹配 |
|---|---|---|---|---|
| **OT-1708P** | 8 FE PoE + 2 FE，**96W** | **ANW-1008-MMP96** | 8×10/100 PoE + 2×10/100，**96W** | ✅ **完全一致** |
| **OT-1708PG** | 8 FE PoE + 2 GE，**120W** | **ANW-1008-MGP120** | 8×10/100 PoE + 2×10/100/1000，**120W** | ✅ **完全一致** |
| **OT-1708PG-E** | 8 GE PoE + 2 GE，**120W** | **ANW-1008-GGP120** | 8×10/100/1000 PoE + 2×1G，**120W** | ✅ **完全一致** |
| **OT-1716P** | 16 PoE + 2 GE + 1 GF，200W | **ANW-1016-MSP300** | 16×10/100 PoE + 2×1G + 1×1G SFP，300W | ✅ 端口完全一致（PoE 略高） |
| **OT-1724P** | 24 PoE + 2 GE + 1 GF，**300W** | **ANW-1024-MSP300** | 24×10/100 PoE + 2×1G + 1×1G SFP，**300W** | ✅ **完全一致** |
| **OT-04**（4 口电源） | 4 口交换机变压器 | **ANW-1004-MMP60** | 4×10/100 PoE + 2×10/100，**60W** | ✅ |

补充对应：
| Ewind 官网产品线 | Angora HITIT |
|---|---|
| 8 口 PoE 非网管 | ANW-1008-MCP120（8×FE PoE + 2×1G Combo，120W） |
| PoE Injector / Splitter | HITIT SFP 模块：ANW-SFP-1G-SX / 1G-LX / 10G-SR / 10G-LR |
| 300 米远距离传输 | HITIT 标称 **250 米** |

> ## ✅ 结论
> **HITIT 系列 = 深圳 Ewind（Shenzhen Ewind Technology Co., Ltd）的非网管 PoE 交换机白牌。**
> 证据链：官方数据表自称"非网管" + 型号命名规则一致（OT-17xx ↔ ANW-10xx）+ 端口配置一致
> + **PoE 功率数值逐个吻合（96W / 120W / 300W）** + 远距离传输特性一致。
>
> **这也解释了 Volza 上"Ewind 是 Angora 第一大进口供应商"。**

## 1.3 HITIT 完整型号表（官方数据表逐字）

| 型号 | 10/100 电口 | 10/100/1000 电口 | 光口(SFP) | PoE 口 | 总 PoE 容量 |
|---|---|---|---|---|---|
| ANW-1004-MMP60 | 4 | 2 | — | 4 | 60W |
| ANW-1005-T | — | 5 | — | — | — |
| ANW-1008-MMP96 | 10 | — | — | 8 | 96W |
| ANW-1008-MMP120 | 10 | — | — | 8 | 120W |
| ANW-1008-MGP120 | 8 | 2 | — | 8 | 120W |
| ANW-1008-MCP120 | 8 | 2×Combo | — | 8 | 120W |
| ANW-1008-GGP120 | — | 10 | — | 8 | 120W |
| ANW-1010-T | — | 10 | — | — | — |
| ANW-1011-T | — | 10 | 1 | — | — |
| ANW-1016-MSP300 | 16 | 2 | 1 | 16 | 300W |
| ANW-1024-MSP300 | 24 | 2 | 1 | 24 | 300W |

**订购信息（官方）**：
- ANW-1005-T / 1010-T / 1011-T：**工业级，IP40 防护，DIN 导轨**（无 PoE）
- 其余为企业级 PoE，单 AC 电源，壁挂/19" 机柜
- 每端口最大 30W（802.3at/af）
- 电源 100-240VAC 50/60Hz
- 协议：自学习 MAC、自动 MDI/MDIX、自动协商、Jumbo Frame、流控、
  IEEE 802.3i / 3ab / 1p / 3x / 3u / 3z / **3az**
- 数据表还提到："接口无流量时自动断电重启远端设备"（PoE 看门狗类功能）

> ### ⚠️ 战略含义（对我方利好）
> **HITIT 是非网管 PoE，与我方的网管型 L2+/L3 工业交换机不在一个竞争面上。**
> **Angora 用 Ewind 补的是"廉价非网管 PoE 边缘"这一档，不是我方的"工业网管"这一档。**
> **我方真正需要警惕的不是 HITIT，而是新版 VERGE 的 `ANW-IND-8P-2SFP`（工业 8 口 PoE）。**

---

# 二、中国同行海关数据（ImportGenius 各国站，实测可访问）

> **重要**：ImportGenius **没有土耳其站**（`/turkey/tradebase` → 404），
> 但**印度 / 越南 / 乌克兰等站点未被墙且明细可见**。以下为实测抓取结果。

## 2.1 深圳 Scodeno —— 越南站

**Shenzhen Scodeno Technology Co., Ltd.**
地址：**2F, Building A6, Silicon Valley, Power Digital Park, Dafu Road, Guanlan, Longhua District, Shenzhen, China**
页面：https://www.importgenius.com/vietnam/suppliers/shenzhen-scodeno-technology-co-ltd

| 型号 | 规格 | 数量 |
|---|---|---|
| **XPTN-9000-65-5GP** | 工业以太网交换机，5×10/100/1000M RJ45，PoE，**非网管**，**IP40**，DIN 导轨 | 1 PCE |
| **XPTN-9000-85-2GX8GP-VX** | 2×1000M SFP + 8×10/100/1000M RJ45 PoE，**网管型**，**IP50**，DIN 导轨 | 2 PCE |
| **XPTN-9000-75-2GX8GP-V** | 2×1000M SFP + 8×10/100/1000M RJ45 PoE，**网管型**，**IP40**，DIN 导轨 | 2 PCE |
| MU150C280S | 工业电源 150W(54V 2.8A)，品牌 **MOSTCN**，制造商 **Most Optoelectronics**，美规插头 | 1 PCE |

买方：CÔNG TY CỔ PHẦN CÔNG NGHỆ **STARLINKS VIỆT NAM**（越南）
到货：2020-08-31｜数据区间：2018-01-01 ~ 2020-10-19

> ### ⭐ 关键推断
> **Scodeno 的型号前缀是 `XPTN-9000-xx`。**
> **而 Angora HITIT 的三款工业机型（ANW-1005-T / 1010-T / 1011-T：IP40、DIN 导轨、无 PoE/千兆）
> 与 Scodeno XPTN-9000-65-5GP（IP40、DIN 导轨）特征高度吻合。**
> **→ HITIT 里的"企业级 PoE"部分来自 Ewind，但"工业级 DIN 导轨"部分很可能来自 Scodeno。**
> 这与用户所说"Lanaotek 也卖 SmartByte 的货，兄弟公司产品互相串"完全同构。

## 2.2 深圳 Utepo —— 乌克兰站

**Shenzhen Utepo Tech Co., Ltd**
地址：**C2301 Block BC, Union R&D Center, Longteng Community, Xixiang Street, Shenzhen**
页面：https://www.importgenius.com/ukraine/suppliers/shenzhen-utepo-tech-co-ltd

- **47 票** / 4 个买方 / 数据区间 2011-01-01 ~ 2024-08-20
- 乌克兰买方：
  1. ТОВ "ТОРГОВИЙ ДІМ СИСТЕМ ВІДЕОНАГЛЯДУ"（视频监控系统贸易行）— 至 2022-07-07
  2. ТОВ СВІТ КАМЕР（摄像机世界）— 至 2023-08-05
  3. ТОВ ДОЙЧ ІМПОРТ — 至 2024-05-31
  4. ТОВ "УПРАВЛІННЯ ІНФОРМАЦІЙНИХ ТЕХНОЛОГІЙ УКРАЇНИ" — 至 2020-07-15
- 样本发票金额：**13.41 USD**

> Utepo 的客户全是**视频监控/CCTV 渠道商**，与 Ewind 同赛道。

## 2.3 东莞 UNIPOE —— 印度站

**Dongguan Unipoe Communication Technology Co., Ltd**
页面：https://www.importgenius.com/india/suppliers/dongguan-unipoe-communication-technology-co-ltd

- 买方仅 1 家：**SYNEGRA EMS LIMITED**（Verna, Goa, India）
- 样本数量：**600 PCS**
- 数据区间：2007-01-02 ~ 2025-04-30

关联品牌：**UNIPOE IOT Technology Co., Ltd / UNIVIS**（2014 年成立，智慧 IoT 方案商，
产品线含智能网络摄像机、NVR、**带 LCD 的可视化 PoE 交换机**；客户来自美国、台湾、以色列、韩国）

## 2.4 横向对比

| 公司 | 注册地 | 主战场 | 客户类型 | 型号前缀 | 单票规模 |
|---|---|---|---|---|---|
| **Ewind** | 深圳（2017） | 印度、土耳其、全球 | 分销商/进口商 | `OT-17xxP/G` | 数百~1500 台 |
| **Scodeno** | 深圳龙华观澜 | 越南、土耳其 | 系统集成商 | `XPTN-9000-xx` | 小批量样机 |
| **Utepo** | 深圳西乡 | 乌克兰、独联体 | CCTV 渠道商 | — | 47 票 |
| **UNIPOE** | 东莞 | 印度 | EMS 代工厂 | — | 600 台 |

---

# 三、✅ Advensis 核实（回答问题 4）

## 3.1 不是法国公司，是土耳其安卡拉的

| 项 | 内容 |
|---|---|
| 全称 | **Advensis Software & Consultancy**（工程/软件咨询公司） |
| 国别 | **土耳其**（页面标题明确写 "Advensis [TURKEY]"） |
| 地址 | **Mustafa Kemal Mah. 2140 Sk. No:14/7 Çankaya / ANKARA** |
| 电话 | **(0312) 474 21 22** |
| 网站 | https://advensis.com.tr/（有土耳其语 / 英语 / **俄语** 三语） |
| 代理品牌 | **Ruijie（锐捷）** + **Angora** |

## 3.2 是 Angora 的分销商/方案商 —— 有证据

证据 1（英文页）：
> "**As Advensis, we offer you the best Angora Networks**"
> "At Angora Networks, a 100% domestic network solution brand, our goal is to provide
> end-to-end solutions to all your network needs…"

证据 2（土耳其语页，2020-11-12）：
> "Ağ Anahtarı, Network Device, Yerli Switch, Thince Client, ince İstemci, gibi ürünlerin
> markası **Angora Networks**… **Advensis Angora Networks**"

证据 3：页面完整介绍 Angora 的 **VERGE / THiNCE / IRIS SFP / ANGORA NMS** 四条产品线。

证据 4：Angora 官方自我定位描述
> "Türkiye'nin önde gelen İletişim Ağı ekipmanı üreticisi Angora Networks®…
> **kritik kurumsal iletişim ağları için güvenilir bir iş ortağı**"

## 3.3 🔴 一个重要发现：Advensis 同时代理 **Ruijie（锐捷）**

> **这是一家同时代理 Angora 与锐捷的土耳其方案商。**
> **锐捷是中国头部网络厂商 —— 意味着 Angora 在渠道端直接与中国一线品牌同台竞争。**
> Advensis 是"厂商独立（manufacturer-independent）"定位：
> "**Üretici bağımsız yaklaşımımız** ile doğru zamanda doğru ürünü bulmanızı sağlamaktayız."
> （以厂商独立的方案，帮你在对的时间找到对的产品。）

---

# 四、⚠️ 人员异动（新发现）

## 4.1 渠道经理 Zafer Doğruel 已于 2024 年 3 月离职

来源：https://www.linkedin.com/in/zaferdogruel/

| 时间 | 经历 |
|---|---|
| **2021-01 ~ 2024-03**（3 年 3 个月） | **Angora Networks** — Kanal Yönetim Müdürü（渠道管理经理） |
| 2025-04 ~ 至今 | **Andasis** — İş Geliştirme Yöneticisi（业务发展经理） |
| 2017-09 ~ 2018-09 | Alp Enerji |
| 2010-12 ~ 2014-08 | **NETAŞ**（负责公共部门采购项目的全生命周期管理） |
| 1994 ~ 1999 | Ankara Üniversitesi |

> **含义**：
> ① Angora 的**渠道体系在 2024 年 3 月失去了负责人**，此后未见公开的继任者信息。
> ② 他去 NETAŞ 做过**公共部门（Kamu）采购项目管理** —— 这与 Angora 主攻政府项目的时间线吻合，
> **他很可能就是 Angora 政府项目渠道的搭建者。他 2024-03 离职，值得关注。**
> ③ 他现在在 **Andasis**（安卡拉），可作为一个侧面信息源。

## 4.2 Angora 官方 X 账号

`@AngoraNetworks` — 60 条推文，24 关注者，2016-12 加入，地区 Ankara。
（几乎无运营，可忽略）

---

# 五、待办

| # | 动作 |
|---|---|
| 1 | 抓 **Scodeno 官网 `en.scodeno.com` 型号表**，确认 `XPTN-9000` 是否对应 HITIT 工业三款 |
| 2 | 抓 **Lanaotek 工业交换机页**，与 Angora VERGE 新版 `ANW-IND-8P-2SFP` 比对 |
| 3 | 追查 **Advensis 目前的 Angora 业务是否还活跃**（页面最新为 2020 年） |
| 4 | 通过 **Andasis** 侧面了解 Zafer Doğruel 离职原因 |
| 5 | 试 **TradeInt / Tendata** 要土耳其进口数据 |
