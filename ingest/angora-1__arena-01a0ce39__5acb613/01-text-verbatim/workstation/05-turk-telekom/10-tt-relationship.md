# Angora Networks ↔ Türk Telekom 关系深度挖掘

> 调查日期 2026-09-23
> 背景：用户指出"他们在和我的日常对话中**时常提到 TT 公司**"，故专项调查。

---

## 🎯 核心结论（先看）

1. **TT 项目是真实、持续、长达 2 年以上的主线项目**，不是客户随口一提。时间跨度 **2024-06 → 2026-07**。
2. **我方仓库里的 `RFP/Turk_Telekom_Test_Items.xlsx`，与 Türk Telekom 官网正式招标公告《Switch Alım İhalesi》逐条对应** —— 这份测试清单就是 TT **MSY 团队**的需求分解。
3. TT 招标**只接受土耳其境内投标人**（yurtiçi istekliler）→ 这解释了为什么 **Angora（本土厂商身份）是必经通道**，也解释了为什么 Levent 反复强调"我们是 100% 本国资本的制造商"。
4. **Angora 官网的 References（客户名单）里没有 Türk Telekom** —— TT 项目**尚未成为已交付业绩**，仍在进行中。
5. TT 采购单位是 **Network Sistemleri Satınalma Müdürlüğü**（网络系统采购部），公开联系邮箱
   `satinalma.networksistemleri@turktelekom.com.tr`。

---

## 1. 【关键证据】Türk Telekom 官网正式招标公告

**页面**：https://www.turktelekom.com.tr/hakkimizda/duyurular/switch-alim-ihalesi
**标题**：Switch Alım İhalesi（交换机采购招标）

### 公告全文（土耳其语原文）

```
TÜRK TELEKOMÜNİKASYON A.Ş.'DEN

İHALE İLANI

İhalenin Konusu:
Şirketimizce Türkiye genelinde sahalarda kullanmak aşağıdaki malzemenin Tedarikçi ve Türk
Telekom arasında imzalanacak sözleşmelerle temin edilmesidir.
* * *
TT Mobil A.Ş.'nin haberleşme santrallerin de ve Mobil baz istasyonlarında bulunan cihazların
uzaktan erişim işlemleri için ihtiyaç duyulan switch alım işini kapsar.
Cihaz endüstriyel tip olmalı ve ağır çevresel şartlara karşı dayanıklı olmalıdır.
Ürün 42-60V DC gerilim aralığında çalışabilme özelliğine sahip olmalıdır ve ihtiyaç duyulan
izolasyonlar sağlanmış olmalıdır.
Cihaz en az +85ºC ve –45ºC sıcaklık aralığında sorunsuz olarak çalışabilecektir.

İhaleyi Yapan Birimin Adı ve Adresi:
Türk Telekomünikasyon A.Ş Satınalma Direktörlüğü
Network Sistemleri Satınalma Müdürlüğü
Turgut Özal Bulvarı Aydınlıkevler 06103 ANKARA

İhale Katılım Şekli:
İhaleye katılmak isteyen İsteklilerin 05.07.2023 Saat 14.00' a kadar
satinalma.networksistemleri@turktelekom.com.tr adresine mail atarak ihale dokümanları için
başvuru yapması gerekmektedir. Başvuru süreci sonrası ihaleye katılacak firmalar ayrıca
bilgilendirilecektir.

İhale Usulü: （空）
İhale Tarih ve Saati: （空）

İhaleye Katılabilecek Olanlar:
Bu ihaleye, İhale Dokümanında belirtilen şartları taşıyan **yurtiçi istekliler** katılabilir.

İhaleye Katılamayacak Olanlar:
Türk Telekom Grubunda görev yaptıkları sürece, Yönetim, İcra ve Denetim Kurulu Üyeleri ile
Türk Telekom Grubunun diğer tüm çalışanları ve ayrıca ilgili mevzuatı uyarınca kamu
İhalelerine katılmaktan yasaklı olanlar İhalelere katılamazlar. Katıldıkları takdirde
teklifleri değerlendirmeye alınmaz, sehven değerlendirmeye alınır ve İhale üzerinde kalır ise
İhale iptal edilir ve geçici veya kesin teminatı gelir kaydedilir. Türk Telekom'un zararı
bulunduğu takdirde istekliden ayrıca tahsil edilir.

Türk Telekomünikasyon A.Ş. ihale tarihini tamamen kendi takdirinde olmak üzere her hangi bir
sebep göstermeden daha sonraki bir tarihe ertelemekte; ihaleyi yapıp yapmamakta, Sözleşmenin
imzalanmasından önceki herhangi bir aşamada ihaleyi iptal etmekte serbesttir.
```

### 中文要点

| 项 | 内容 |
|---|---|
| 采购方 | Türk Telekomünikasyon A.Ş.（土耳其电信） |
| 需求方 | **TT Mobil A.Ş.**（TT 移动子公司） |
| 用途 | 通信局站与**移动基站**内设备的**远程接入**用交换机 |
| 设备类型 | **必须为工业级**，抗恶劣环境 |
| 供电 | **42–60V DC** 工作范围，并需具备所需隔离 |
| 工作温度 | **至少 −45°C ~ +85°C** |
| 采购单位 | Satınalma Direktörlüğü / **Network Sistemleri Satınalma Müdürlüğü** |
| 地址 | Turgut Özal Bulvarı, Aydınlıkevler, 06103 Ankara |
| 报名邮箱 | **satinalma.networksistemleri@turktelekom.com.tr** |
| 首轮报名截止 | 2023-07-05 14:00 |
| 投标资格 | **仅土耳其境内投标人（yurtiçi istekliler）** |
| 备注 | TT 保留延期/取消招标的全部裁量权（**"ihaleyi yapıp yapmamakta serbesttir"**＝可完全不招标） |

---

## 2. 【关键证据】TT 招标公告 ↔ 仓库测试清单 逐条对应

仓库文件：`RFP/Turk_Telekom_Test_Items.xlsx` → 第二张表 **"TÜRK TELEKOM MSY TEAM QUESTIONS"**

| TT 官方招标要求 | 仓库测试清单条目 | 匹配 |
|---|---|---|
| Cihaz **endüstriyel tip**，ağır çevresel şartlara dayanıklı | —（整体前提） | ✅ |
| **42-60V DC** 工作范围 + 隔离 | 第 1 条：**Power 42-60 V** | ✅ **完全一致** |
| **+85ºC ~ –45ºC** | 第 2 条：Temperature **+75 -40** | ✅ 对应（测试清单略宽松） |
| 远程接入用交换机（8 口级别） | 第 3 条：**8 Portu 10/100/1k Copper** | ✅ |
| — | 第 4 条：Min 2 port 1/2.5G SFP Fiber | ✅ |
| — | 第 5 条：1-4096 Vlan |
| — | 第 6 条：1GB İlave ayrı SFP sunulmalı（须另提供 1G SFP） |
| — | 第 7 条：**Factory Reset PIN** |
| — | 第 8 条：**8 K MAC** |
| — | 第 9 条：**512 Mb Ram - 32 MB Flash** |
| — | 第 10 条：**IP40** |
| — | 第 12 条：Ring - **20 ms** |
| — | 第 13 条：Jumbo Frame **9K** |
| — | 第 14 条：Dynamic ARP Protection, DHCP Snooping |
| — | 第 15 条：Management ACL, L2/L3/L4 ACL, IP Source Guard |
| — | 第 16 条：**SNMP v3, HTTPS, SSHv2 ve sFTP, SFLOW** |
| — | 第 17 条：Port Mirroring |
| — | 第 18 条：Port Forwarding（备注：L3 Port Forwarding） |
| — | 第 19 条：HTTPS Web User Konfig |
| — | 第 20 条：**Firmware SFTP Upgrade** |
| — | 第 21 条：SNMP Trap, Syslog, SFlow |
| — | 第 22 条：SSHv2 |
| — | 第 23 条：TACACS or Radius |
| — | 第 24 条：Management Platform |
| — | 第 25 条：PoE |
| — | 第 26 条：Switch+Router（备注：L3 Routing） |
| — | 第 27 条：**NAT / Port Forwarding**（备注：L3 Routing） |

第一张表 **"TEST ITEMS"** 为 TT 日常通用功能清单（1.1~1.29），包含 Basic VLAN / Trunking /
VLAN translation / IGMP VLAN tag / Loop detection / Link Aggregation / DHCP Snooping /
Rate Limiting / Bandwidth Control / Port Security / Config&Firmware backup restore /
Trusted Host / Syslog / PoE / Port Mirror / IP-MAC-PORT Binding / Spanning tree / IPv6 /
QinQ / **Dynamic Routing Support** / MAC Limitation / **Switch L3 Interface** / **Stacking** /
ME Tests / AC&DC Energy Tests / 802.1P / **VRRP Redundancy** / NTP / Radius-TACACS。

> **⚠ 战略含义**：TT 的通用清单里包含 **Dynamic Routing、Switch L3 Interface、Stacking、VRRP**
> —— 这四项正是 Levent 在 2026-07-31《SAGA Enterprise L3 Recommendation Report》里向我方索要的功能。
> **即：Levent 要 L3，不是为了泛泛的"企业级市场"，而是 TT 这条具体产品线的准入要求。**

---

## 3. TT 项目完整时间线（从仓库文件还原）

| 日期 | 事件 | 来源 |
|---|---|---|
| **2023-07-05** | TT 官网发布《Switch Alım İhalesi》，报名截止 | TT 官网 |
| **2024-06-14** | Levent 发来 TT RFP（土/英双语），需求 **250 台**（后可能 250+250），型号 **LT-IS6310G-2GX8GT**（8 电 + 2×2.5G 光，无 PoE 无串口）。关键需求：sFlow / ACL / SNMP MIB / **SFTP** | `Gmail - Angora Networks - 250 pieces potential order.pdf`、`RFP_2024.6.15.docx` |
| 2024-06-15 | Simon 逐条回复：7.5/7.6 光模块非自产；7.25-7.27 SFTP 不支持；土耳其语不支持；**HTTPS 不支持（Marvell 芯片只支持 HTTP）** | 同上 |
| 2024-06-18 | Taylan：若等 HTTPS 芯片，能否同时开发 SFTP？ | 同上 |
| 2024-07-10 | Taylan：与客户达成一致，**关键点是 ACL、Sflow、https、sftp**；数量 **300+** | 同上 |
| 2024-07-11 | Simon 回复：需先付定金才能排研发优先级 | `Sftp reply_2024.7.11.docx` |
| 2024-07-11 | Taylan：**SFTP 只用于软件升级**，不需要配置导入导出/syslog | 同上 |
| 2024-07-12 | Simon 报价：**交期 8~10 周**；单价 **$110/pc**，批量 **$105/pc**；不收研发费，但收 **$8,000 研发启动定金**（可抵货款）；提出方案 1（先产后升级）与方案 2（一步到位） | `R&D period&cost_2024.7.12.docx` |
| 2024-07-18 | Levent：仍在与客户争取订单 | 邮件 |
| 2024-07-23 | Taylan：客户问**能否读取交换机输入电压**（远程站点监测用），Simon 回复不可行 | 邮件 |
| 2024-09-16 | Levent：仍在讨论中 | 邮件 |
| **2024-12-10/11** | **Levent 透露重磅**：*"We are working on a project at Turk Telekom. The devices we are going to offer are the industrials you send us last time. **Our partner is very strong here, and can push the customer to publish an RFP in our favor.** I am looking for some RFP items that will point our product and eliminate other. **The order will be a big one, around 2000-3000 devices**, so i believe we can customize the product to have unique features."* | `RFP_2024.12.11.docx` |
| 2024-12 | Simon 反提议差异化卖点：Serial（串口）功能、Marvell 自研软件可快速改、**SFTP**、push-in 端子、铝面板散热 | `Reply on RFP 2024.12.10.docx` |
| **2025-01-30** | **TT 现场测试邀请**：*"We have been invited for a test on **February 3rd**."* 要求把 ANW-1108-V 样品改成 **TT-2208-TG**（TT 品牌型号 + TT logo） | `RFP_2025.1.30.docx` |
| **2025-02-05** | 提交 `Turk_Telekom_Test_Items.xlsx`，分两部分（通用功能 + MSY 团队项目专用）。客户要求先按 LT-IS6310G-2GX8GT 审核第二部分；**未测项：ACL / HTTPS / SFTP / SFLOW**；客户特别在意 **NAT 与 Port Forwarding** | `RFP_SFTP check List_2025.2.5.docx` |
| **2025-06-19** | **STSC20250619007**：向 TT 交付 **TT-2208-PG × 6**（STI-288DGGPM，工业 8 口 PoE L2+，Marvell **AC5**），WEB GUI 与标签显示 Türk Telekom 信息 | `6th order/` |
| **2025-07-11** | **STSC20250711007**：TT-2208-PG **×10**（仅在 MAC 台账中留痕，无 PI/成本表） | `mac_address&serial_number.xlsx` |
| **2026-07-31** | Levent《SAGA Enterprise L3 Recommendation Report》：**"including our current engagement in the **Turk Telekom 2026 procurement cycle**"**，并称要争取 *"multi-year framework contracts (such as the **Turk Telekom 2026 tender and its successors**)"* | `SAGA Enterprise L3 Recommendation Report.pdf` |
| 2026-08-17 | Simon 拟回复：拒绝自研 L3，推 CENTEC | `Reply on SAGA Enterprise L3...docx` |

---

## 4. 我方已交付的 TT 相关机型

| 合同号 | 日期 | 客户型号 | 工厂型号 | 数量 | 备注 |
|---|---|---|---|---|---|
| STSC20241021007 | 2024-10-21 | ANW-1108-V | LT-IS6310G-2GX8GT / STI-280DGGM | 2 | 后改为 **TT-2208-TG** 送 TT 测试 |
| STSC20250619007 | 2025-06-19 | **TT-2208-PG** | STI-288DGGPM | 6 | **Marvell AC5 芯片**；WEB GUI 与标签显示 TT 信息；MAC 98:06:37:A5:00:13~00:18 |
| STSC20250711007 | 2025-07-11 | **TT-2208-PG** | STI-288DGGPM | 10 | MAC 98:06:37:A5:00:19~00:22；**缺 PI 与成本记录** |

> 注意型号命名：**TT-** 前缀 = Türk Telekom 专属品牌化编号，与 **ANW-**（Angora）、**TRX-**（TronX）并列。

---

## 5. Türk Telekom 背景（外部）

- **Türk Telekomünikasyon A.Ş.** 是土耳其三大国家运营商之一，与政府渊源深厚。
- 集团下属 **TT Mobil A.Ş.** 为移动业务子公司（本次交换机需求方）。
- 集团下属 **Argela** 为研发子公司，参与 ULAK（国产 5G/核心网）项目、UTM（无人机追踪管理研发项目），
  由 UDHAM（交通、海事与通信研究中心）管理。→ 说明 TT 集团内部有**强烈的国产化/自主可控导向**，
  这与 Angora 的"Yerli Akıl, Küresel Teknoloji（本土智慧，全球技术）"定位高度契合。
- 采购组织：**Satınalma Direktörlüğü → Network Sistemleri Satınalma Müdürlüğü**
  地址：Turgut Özal Bulvarı, Aydınlıkevler, 06103 Ankara
  公开联系：satinalma.networksistemleri@turktelekom.com.tr

---

## 6. 待核实 / 风险提示

| # | 问题 | 重要度 |
|---|---|---|
| 1 | TT 2026 采购周期的最新招标是否已发布？规模多少台？ | 🔴 高 |
| 2 | Angora 所称 "**our partner is very strong here, and can push the customer to publish an RFP in our favor**" —— 这个"强势伙伴"是谁？（Elcore？某系统集成商？） | 🔴 高 |
| 3 | 2025-02-03 的 TT 现场测试结果如何？仓库中无测试报告 | 🔴 高 |
| 4 | STSC20250711007（10 台 TT-2208-PG）**为何无 PI、无成本表、无收款记录**？是否已收款？ | 🔴 高 |
| 5 | TT 要求 **512MB RAM / 32MB Flash**，我方 STI-288DGGPM（AC5）是否满足？ | 🟡 中 |
| 6 | TT 要求 **IP40**，我方工业机标称 IP40 是否实测通过？ | 🟡 中 |
| 7 | TT 要求 **+85°C / −45°C**，而我方标称 **−40°C ~ +75°C** —— **不满足！** 需确认是"整表要求"还是"TT 内部放宽" | 🔴 高 |
| 8 | TT 要求 **PoE**（第 25 条）与 **NAT/Port Forwarding**（第 27 条），后者我方明确不支持 | 🔴 高 |
| 9 | TT 招标**仅限土耳其境内投标人** —— Angora 是唯一通道，我方对其依赖度极高，议价权弱 | 🟡 中 |
| 10 | TT 明确保留"可完全不招标/随时取消"的权利 —— 项目流产风险始终存在 | 🟡 中 |

---

## 7. 建议动作

1. **向 Angora 直接要 2026 TT 招标文件**（技术规格书全文），比对 `Turk_Telekom_Test_Items.xlsx` 是否有更新版本。
2. **补齐 STSC20250711007 的全部单据**（PI / 收款 / 成本），并确认 2025-07 之后是否还有更多 TT 出货。
3. **温度缺口优先解决**：TT 招标写 −45~+85°C，我方标称 −40~+75°C。要么做宽温版本，要么请 Angora 书面确认 TT 实际验收标准（仓库测试清单写的是 +75/−40，招标写 +85/−45，两者不一致，需澄清）。
4. **NAT / Port Forwarding**：客户两次点名在意（测试清单第 18、27 条），我方 Marvell 方案不支持 —— 若 CENTEC 方案支持，这正好是推 CENTEC 的最佳理由（可直接对 Levent 说："你要的 NAT/Port Forwarding/堆叠/VRRP，CENTEC 现成"）。
5. 摸清 Angora 口中的"**strong partner**"到底是谁 —— 决定这条线的可控性。
