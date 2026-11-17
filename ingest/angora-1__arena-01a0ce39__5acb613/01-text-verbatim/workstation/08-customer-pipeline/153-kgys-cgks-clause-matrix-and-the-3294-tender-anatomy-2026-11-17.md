# 153 · r84：把「3,294 台」拆开 —— 五包结构、**证书只卡 8 口**、24 口其实是自由市场（2026-11-17）

> 取证时刻：**2026-11-17T12:20Z / 20:20 +0800**（外部抓取）；语料回溯截至本日。
> 用户第 37 次：「继续 深度挖掘 入库」。
> 本轮不再重复 r83 的市场面，而是**回到自家语料把 2026 年 4 月那场国标招标整个拆开**，并给出**我方 8 口工业机 / 24 口室内机对三份规格书的逐条矩阵**。
> **结论先行：我上一轮（r83）说「室内 24 口是更大的那一半」，是错的；而且「EGM 证书」只卡 8 口，24 口那一包根本没有证书要求。**
> 汇率：USD/TRY **50.02**；USD/CNY **7.15**（与语料报价口径一致）。

---

## 一、结论十条

1. **⭐⭐ 3,294 台 = 一个五包国标招标的第 2 包，全部是 8 口边缘交换机**（`ihaleciler.com` 招标摘要：第 1 包 **7,888 固定摄像机 + 2,984 PTZ + 191 LPTZ + 237 NVKÜ**，第 2 包 **3,294 台 Kenar Ethernet Anahtar**，共 5 包；EKAP 发布 **2026-04-16**、投标截止 **2026-04-30**，出现在 **Hakkari** 条目下，报价区间 **43,142,132 – 323,566,103 TL**）。
2. **⭐⭐ 24 口室内那半边只有 200 台 —— 是我上一轮说反了**。Levent 2026-04-16 原话：**「The tender on the 28th is for 600 pcs 8-port and 200 pcs for 24-port / The tender on the 29th is for 3,294 pcs 8-port」** ⇒ 8 口合计 **3,894 台（95%）**，24 口 **200 台（5%）**。
3. **⭐⭐ 证书闸门只拦 8 口**：KGYS `3.4.1–3.4.44` 室内段**通篇没有 C-Tipi 报告条款**；ÇGKS `3.3.1.1–3.3.1.39` 室内段**也没有**；报告要求只出现在 **KGYS 3.3 现场段**、**EGM 3.3.2.23**、**ÇGKS 3.3.2.23**。⇒ **投 24 口那一包，白牌即可；投 3,294 台那一包，没有证就只能看着。**
4. **⭐⭐ 证书的经济学是「可复用」而不是「要重考」**：Levent 2026-03-06 —— **「we already have this certificate as Angora. We just need to make sure our software version info is the same as the version on the certificate. We can use our existing certificate」**。⇒ 真正的约束是**固件版本号必须与证书一致**，这是我方软件分支管理问题，不是 Angora 的采购问题。
5. **⭐⭐ 而且规则里有一个官方后门**：turk-iot 引用的现行条文 —— **流量整形若不能与交换机一体实现，可作为「同品牌的外置设备」单独提供**，条件是该外置方案同样持有 BAŞARILI 报告（`harici olarak da teklif edilebilecektir`）。⇒ **一条「只做 shaping 的小盒子 + 我方普通交换机」的合规路径存在，成本远低于整机重测。**
6. **⭐ 已知持证品牌清单（二手）**：**Extreme Networks、Allied Telesis、CryptoLink、D-Link**（turk-iot）＋ **Angora**（官网 + 2026-03-06 微信自述）。⇒ 全国能投 3,294 台那一包的品牌**不超过一只手**。
7. **🔥 价格三条线全部拿到了，这是本轮最硬的一组数**：
   - **D-Link 给伙伴的价：$135/台「全包」**（交换机 + 电源 + SFP + 光纤 + 短电源线，含运、含关、含分销毛利），**交期 120 天**，30/70 付款（Levent 2026-04-22 转述，Simon 当场核对「it includes the shipping… customs… distribution margin」）。
   - **我方报价：855 RMB/台 = 830（交换机）+ 25（NEM 光模块）** ≈ **$119.6**（@7.15）。
   - **我方工厂现行价（2026-09-01→12-30，未税）**：`LT-IS6310GP-2GX8GT`（8×1G PoE + 2×SFP，L3，IP40，−40~75 ℃，6 kV，G.8032）**780 RMB**；`LT-IS3210GP-2GX8T`（L2，IPv6 仅管理面）**440 RMB**。
   ⇒ **报价 830 − 工厂 780 = 50 RMB/台 = 6.0% 毛利**。**3,294 台全部拿下 = 164,700 RMB ≈ $23,000 毛利**。这就是 Levent 说「the whole tender is not commercially viable, it is just for marketing」的算术依据。
8. **🔥 而 24 口那一包的毛利是 8 口的 5 倍**：工厂 `LT-S8328GP-4GX24GT-S`（24×1G PoE + 4×1G/2.5G SFP，AC5，280 W）**750 RMB**；对外 $140 ≈ 1,001 RMB ⇒ **+33%**；200 台 = 50,200 RMB 毛利，**单台毛利 251 RMB vs 8 口 50 RMB**。⇒ **资源应该压在 24 口，而不是 3,294 台那一包。**
9. **⭐⭐ 结构事实：省市级 KGYS/ÇGKS 备件标，外国公司根本不能投**。2026 年多份公告原文：**「İhaleye sadece yerli istekliler katılabilecektir」**（Adana İKN 2026/1248553）；**「yerli malı teklif eden yerli istekliye %15 fiyat avantajı」**（Ordu/Ünye）。⇒ 我方唯一路径是**通过 Angora 的 Yerli Malı Belgesi 借船**，这也解释了为什么 Saga 反复强调「we support you in the dark, Saga itself will NOT enter Turkish market directly」（2026-08-26 微信）。
10. **⭐ 我方在 4 月那两场标全军覆没，而且输给了摄像头阵营**：`2026-04-28/29` 大标 —— **伙伴第 3 名**；`2026-05-21` 市级小标（36 套工业机 + 39 台 24 口非 PoE）—— **伙伴第 3 名，中标者 Dahua（摄像头 + 交换机打包）**，我方伙伴用「我方交换机 + Hikvision 摄像头」。⇒ **KGYS 的胜负手不在交换机，在「谁能把摄像头和交换机一起报」**。

---

## 二、修正 r83（三条，点名原句）

| # | r83 原句 | 应为 | 证据 |
|---|---|---|---|
| 1 | 「**3.4.1–3.4.29**」 | **3.4.1–3.4.44（共 44 条）** | `警察局项目/EGM.txt` 实到 3.4.44；我方自制模板 `Turkey_Police_RFP_Compliance_Template.xlsx` 的 `Indoor_Switch_Compliance` 表 **A1:E45 = 44 条 + 表头** |
| 2 | 「**3,294 台里室内机占相当比例**」「室内 24 口是更大的那一半」 | **3,294 台全部是 8 口**；24 口另是一包，**只有 200 台** | 2026-04-16 Levent 原文；`ihaleciler.com` 第 2 包明写「3.294 Adet **Kenar** Ethernet Anahtar」（边缘＝现场机） |
| 3 | 「EGM 证书在客户手里 ⇒ 门槛问题基本解决」 | **证书只覆盖「工业 8 口 L2+」这一族**，且**必须固件版本与证书一致**；24 口室内段与 L2+ 商用平台**不在证内，也不需要证** | 官网证书页只写「endüstriyel 8 port Layer 2+ Yönetilebilir」；Levent 2026-03-06「make sure our software version info is the same as the version on the certificate」 |

> 按 r48 规则：以上三条在 `152` 号文件与我方映射说明中同步标注为 **修正 / 取代 r83**，不静默覆盖。

---

## 三、三份规格书 × 三套编号：同一个要求有三个编号

我方与 Angora 在 2026-03-06 的对话里已经踩过这个坑 —— Simon 原话：**「eg: IPv6 VLAN interface IP addressing and traffic (CGKS 3.3.2.21, EGM 3.3.21, KGYS 3.3.2.19)」**。

| 文件 | 编号体系 | 现场 8 口段 | 室内 24 口段 | 证书条款 |
|---|---|---|---|---|
| `KGYS.txt`（2026-02-12 批准，中文摘要） | 3.3.x / 3.4.x | **3.3.1–3.3.22** | **3.4.1–3.4.44** | 3.3 段内「强制认证」；**3.4 段无** |
| `EGM.txt`（英译，Section 3.3+3.4） | 3.3.x / 3.4.x | **3.3.1–3.3.22** | **3.4.1–3.4.44** | 3.3 段；**3.4 段无** |
| `ÇGKS.txt`（2026 备件标） | 3.3.1.x / 3.3.2.x | **3.3.2.1–3.3.2.23** | **3.3.1.1–3.3.1.39** | **仅 3.3.2.23** |

**同一要求三种口径的实例**

| 要求 | KGYS | EGM | ÇGKS |
|---|---|---|---|
| IPv6 VLAN 接口 | 3.3.21 | 3.3.21 | **3.3.2.21** |
| 现场 ≥8GE+≥2SFP | 3.3.2 | 3.3.2 | 3.3.2.2 |
| **SFP 传输距离** | **10 km**（3.3.1 交付条款） | **≥1 km**（3.3.2） | **10 km**（3.3.1.1 / 3.3.2.2） |
| 现场机 SFP 数量 | ≥2 | ≥2 | ≥2；**室内 4 个** |
| 室内 PoE | 全口 af/at（3.4.3） | 同 | 全口 af/at（3.3.1.3） |
| 室内温度 | 0–45 ℃ | 同 | 同 |
| 证书 | 现场段强制 | 现场段 | **仅 3.3.2.23** |

⚠ **SFP 距离三份文件不一致（10 km / 1 km / 10 km）** —— 报价与 BOM 必须按**最严的 10 km** 配（`DIS-S310LX` 类 10 km 模块），否则交付阶段被挑。

---

## 四、2026-04 那场国标招标的真实结构

| 项 | 内容 | 源 |
|---|---|---|
| 包数 | **5 Kısım**（5 包） | ihaleciler.com |
| **第 1 包** | **7,888 固定摄像机 + 2,984 PTZ + 191 LPTZ + 237 NVKÜ** | 同上 |
| **第 2 包** | **3,294 台 Kenar Ethernet Anahtar（边缘以太网交换机）** | 同上 |
| 发布 / 截止 | **2026-04-16 发布 / 2026-04-30 11:00** | 同上 |
| 出现在 | **Hakkari** 条目（EKAP） | 同上 |
| 报价区间 | **43,142,132 – 323,566,103 TL** | 同上 |
| 开标方式 | 先纸面审核 → **e-auction 公开压价**（「open price war」） | 2026-04-28 Taylan 微信 |
| 分包日期 | **04-28 = 600×8 口 + 200×24 口；04-29 = 3,294×8 口** | 2026-04-16 Levent 微信 |

**⇒ 结构性判断：这是一个「摄像头包」拖着「交换机包」的招标。** 第 1 包 1.1 万台摄像头决定了谁有资格谈总价，第 2 包 3,294 台交换机只是配菜 —— 这也直接解释了 2026-05-22 的败因（Dahua 用摄像头 + 交换机打包赢走 36 套 + 39 台的小标）。

---

## 五、微信复盘：从「要不要投」到「第 3 名」（2026-03-06 → 05-22）

| 日期 | 事件 | 关键原文 / 数字 |
|---|---|---|
| **2026-03-06** | Angora 把三份 PDF 给我方；Simon 判「字段/边缘机规格几乎相同，**一个型号够**」并追问 L2 还是 L2+ | 「L2 or L2+ model is a win-loss move... it tends to be L2」；Levent：「**MSTP is missing in our L2 model**... probably we need to go with **L2+**」 |
| 同日 | **证书** | Levent：「**we already have this certificate as Angora**… We can use our existing certificate」 |
| 同日 | 我方交付 **`CGKS Field_Switch_DLink_DIS300G_Compliance.xlsx`** 给客户，作为「同型产品也会被同样挑刺」的证据 | Levent 反问「**so they still won though there are many incompliances?**」 |
| **2026-04-16** | 定价谈判 + 数量揭示 | Levent 要 **825 RMB**；Simon 还 **830**；SFP 走 **NEM Engineering**（由 Saga 付款并安装，避免 Saga 付 VAT）；30/70 付款；DDP 海运 |
| **2026-04-22** | **D-Link 报价泄露** | **$135/台 全包、120 天交货、30/70**；Simon 折算 **921 RMB**，指出「our offer is 855 RMB… the price gap is around 67 RMB or 7%… this is not good enough」 |
| 同日 | 芯片成本解释 | D-Link 疑为 **Vitesse**（DRAM 128 M / Flash 16 M / 4 Mb buffer / 8K MAC），我方 **Marvell AC5**（DDR+Flash **512 MB**）⇒ 硬件成本天然更高 |
| **2026-04-28/29** | 两个分包开标 | 伙伴先交初标，等 e-auction |
| **2026-05-20** | 市级小标 | **36 套工业机 + 39 台 24 口非 PoE**，05-21 开标 |
| **2026-05-22** | 结果 | 「**our partner ended up 3rd**… **Dahua got it**… with cameras and switches；Our partner went with our switches and **Hikvision** cameras」 |
| **2026-06-05** | 新线索 | **军用 24 口车载交换机**，土方要求「Turkish brand to avoid dependency in American or other sources」，附 `24-Port Gigabit _Military_Switch_Spec_DraftC.pdf`（360.6 KB）→ 该 PDF **不在语料内**（只有微信里这条引用） |
| **2026-08-26** | 价格调整 + 战略承诺 | 「we will adjust our prices from 1st, Sept.」；**「Saga itself will NOT enter Turkish market directly」**，只通过 Angora 出面 |
| **2026-08-30** | 新需求 | Levent 问 `STI-4xxXGGPM` 是否跑 RIP/OSPF/BGP/ECMP/VRRP（答 yes）、**48 口工业 PoE+ L3** 是否可做（答「能做，但需求不大」）⇒「**we can order 48-port industrial PoE+ Layer 3 for Turk Telekom**」 |

**⇒ 一年半的线索链，最后落到两个真实需求：Turk Telekom 的 48 口工业 PoE+ L3，和军方 24 口车载机。** 3,294 台那一包在 2026 年 5 月之后已经没有下文。

---

## 六、我方 8 口工业机 × 三份规格书（现场段）逐条矩阵

**对标机型**：`ANW-2023-E8GT-4SFP1G-P` / `ANW-IND-8P-2SFP`（= 工厂 `LT-IS6310GP-2GX8GT` 系）
**依据**：`ANW-VERGE-2023-INDUSTRIAL-DATASHEET`（©2021，VR20210416TRA）+ 工业价目表 2026-09~12

| 条款 | 要求 | 我方 | 判定 |
|---|---|---|---|
| 3.3.1 / 3.3.2.1 | 工业型 | 工业型、DIN 导轨、无风扇 | ✅ |
| 3.3.2 / 3.3.2.2 | ≥8×GE + ≥2×SFP（10 km 模块） | **8×1G + 4×SFP（1G 或 10G 可选）**，模块随箱 | ✅ 超出 |
| 3.3.3 / 3.3.2.3 | −40 ~ +60 ℃ | **−45 ~ +85 ℃**（数据表写「-45° dan 85°C」） | ✅ 超出 |
| 3.3.4 | 10–95% RH | **0–95%** | ✅ 超出 |
| 3.3.5 / 3.3.2.5 | 无风扇 | 无风扇被动散热 | ✅ |
| 3.3.6 / 3.3.2.6 | ≥IP20 | **IP30** | ✅ 超出 |
| 3.3.7 / 3.3.2.7 | 告警继电器 | **硬件告警继电器输出** | ✅ |
| 3.3.8 / 3.3.2.8 | 每 SFP 口 1 m 跳线 | 采购件（随箱） | ✅ 交付条件 |
| 3.3.9 / 3.3.2.9 | 非阻塞 | 线速非阻塞 | ✅ |
| 3.3.10 / 3.3.2.10 | ≥8,000 MAC | **16,384** | ✅ 超出 |
| 3.3.11 / 3.3.2.11 | ≥4 队列 | 8 队列/口 | ✅ 超出 |
| 3.3.12 / 3.3.2.12 | RMON + SNMP v1/v2/v3 + Telnet/Console/Web | 全支持，Console 物理口 | ✅ |
| 3.3.13 / 3.3.2.13 | ICMP + IGMP snooping | ✅（D-Link 在这一条是 ⚠ PARTIAL） | ✅ |
| 3.3.14 / 3.3.2.14 | 802.1Q + MSTP + x-ring + trunking | **MSTP + G.8032 ERPS ≤20 ms** | ✅ |
| 3.3.15 / 3.3.2.15 | 802.1p + ToS | ✅（D-Link ⚠） | ✅ |
| 3.3.16 / 3.3.2.16 | MAC 端口安全 | ✅ | ✅ |
| 3.3.17 / 3.3.2.17 | 802.1x 端口 | ✅ + CoA + 动态 VLAN | ✅ |
| 3.3.18 / 3.3.2.18 | 端口镜像 | ✅ | ✅ |
| 3.3.19 / 3.3.2.19 | **全口 af/at** | **全铜口 30 W 同时供电**，`ANW-IND-8P-2SFP` 预算 **270 W** | ✅ 强于 D-Link（`-8PSW` 只有 4 口 PoE） |
| 3.3.20 / 3.3.2.20 | LACP | ✅ | ✅ |
| **3.3.21 / 3.3.2.21** | **IPv6 VLAN 接口 + 流量处理** | **数据表明列 IPv6 全家桶**（IPv6 VLAN 接口 IP、IPv6 QoS、IPv6 首包安全、ICMPv6 RFC 4443、USGv6/IPv6 Gold Logo） | ✅ **这是 D-Link 的硬伤（✘ NON-COMPLY），我方是硬优势** |
| 3.3.22 | 全部同品牌同型号 | 单一 SKU 可覆盖 | ✅ |
| 3.3.2.22 | DIN + 电源预装同箱 | 需指定 48 V 工业电源并做同箱包装 | ⚠ 交付工艺 |
| **3.3.2.23 / ÇGKS 3.3.2.23** | **EGM C-Tipi 报告 BAŞARILI** | **证书在 Angora 名下（工业 8 口 L2+ 族）**；我方作为制造商不出面 | ✅ **走 Angora 名义；前提：固件版本号与证书一致** |

**关键对照**：我方与 D-Link 在这 23 条上的唯一实质差距是 —— **D-Link 缺 IPv6（✘）与证书（✘）**，我方两条都不缺；我方相对 D-Link 的劣势是**价格（830 vs 921 RMB，仅 7%）**与**DRAM 用料更贵**。

---

## 七、我方 24 口室内机 × KGYS 3.4 全 44 条

**对标机型**：`ANW-2023-24GT-4SFP1G-P`（24×1G PoE + 4×1G SFP，**370 W**）= 工厂 `LT-S8328GP-4GX24GT-S`（**280 W**）或 `LT-S8328GP-4GX24GT`（440 W）

| 条款 | 要求 | 我方 | 判定 |
|---|---|---|---|
| 3.4.1 | ≥24×GE + ≥4×1G SFP（含 10 km 模块） | 24 + 4 SFP | ✅ |
| 3.4.2 | 自协商 / 全半双工 | ✅ | ✅ |
| 3.4.3 | **全部 Base-TX 口 af/at** | 全口 af/at（**见 §8 预算陷阱**） | ✅ 能力 / ⚠ 满载预算 |
| 3.4.4 | 0–45 ℃ | **0–50 ℃** | ✅ |
| 3.4.5 | 10–85% RH | **10–90%** | ✅ |
| 3.4.6 | **≥56 Gbps** | 24×1G+4×1G 线速 = **56 Gbps**（4×10G 版 128 Gbps） | ✅ **刚好**（见 §8） |
| 3.4.7 | ≥41.7 Mpps | **48.1 Mpps（8 口族）/ 98.1 Mpps（24 口族）** | ✅ 超出 |
| 3.4.8 | ≥16,000 MAC | **16,384** | ✅ 刚好 |
| 3.4.9 | 802.1d STP | ✅ + RSTP/MSTP | ✅ |
| 3.4.10 | BPDU Guard | ✅ | ✅ |
| 3.4.11 | 802.3x | ✅ | ✅ |
| 3.4.12 | 802.3ad | ✅ | ✅ |
| 3.4.13 | ≥4 LAG × ≥8 口 | **8 组 LAG，每组 8 口（16 候选口）** | ✅ 超出 |
| 3.4.14 | 802.1Q + 4K VLAN ID + ≥1,000 VLAN | **4096 ID / 1,000 活动 VLAN** | ✅ |
| 3.4.15 | Jumbo ≥9,000 B | **9,216 B** | ✅ |
| 3.4.16–3.4.18 | 802.1p / L2-L3-L4 队列 / DSCP QoS | ✅ 全支持 | ✅ |
| 3.4.19 | 端口限速 | ✅（需在中文技术表上补一句明确表述） | ✅ |
| 3.4.20 | ≥4 队列 + WRR | 8 队列 + SPQ/WRR | ✅ |
| 3.4.21–3.4.22 | IGMP v1/v2，≥255 组 | IGMP v1/v2/**v3**，**1,000 组** | ✅ 超出 |
| 3.4.23 | L2/L3/L4 ACL | ✅ | ✅ |
| **3.4.24** | **≥200 条 ACL 规则** | 数据表**未标条数** | ⚠ **必须向工厂要书面数字** |
| 3.4.25–3.4.26 | 802.1x 端口+MAC；动态 VLAN + Guest VLAN | ✅（含 RADIUS 动态 VLAN 分配） | ✅ |
| 3.4.27 | 端口镜像 | ✅ | ✅ |
| 3.4.28 | IPv4 静态路由 | ✅（L2+ 平台支持 IPv4/IPv6 静态路由） | ✅ |
| 3.4.29 | SSH | ✅ | ✅ |
| 3.4.30 | SNMP v1/v2/v3 + Console + Web | ✅ | ✅ |
| 3.4.31 | RMON 4 组 | ✅ | ✅ |
| 3.4.32 | DHCP Relay / Snooping / Option 82 | ✅（数据表注明 IPv4/IPv6） | ✅ |
| 3.4.33 | 端口安全 | ✅（源 MAC 数量限制） | ✅ |
| 3.4.34 | LLDP 802.1ab | ✅ + LLDP-MED | ✅ |
| 3.4.35 | SYSLOG | ✅ | ✅ |
| 3.4.36 | IPv6 | ✅ 全族（23 处提及） | ✅ |
| 3.4.37 | Radius + TACACS+ | ✅ | ✅ |
| 3.4.38 | 最新固件 | ✅ | ✅ |
| **3.4.39** | **≥128 MB RAM + ≥16 MB Flash** | **512 MB RAM / 128 MB Flash（可选 256 MB）** | ✅ 大幅超出 |
| 3.4.40 | 多配置文件 + TFTP 升级 | ✅ | ✅ |
| 3.4.41 | 全许可 | ✅ 无 license 锁 | ✅ |
| 3.4.42 | 电源线 + 机柜件 + CAT6 线 | 商用机架式，标配 | ✅ 交付条件 |
| 3.4.43 | SNTP/NTP | ✅ | ✅ |
| 3.4.44 | 全部同品牌同型号 | 单一 SKU | ✅ |

**合计：✅ 41 条 / ⚠ 3 条（3.4.3 满载 PoE 预算、3.4.24 ACL 条数、3.4.42 随箱配件）/ ✘ 0 条。**
⚠ **前提声明**：上述逐条依据的是 **©2021 的 `ANW-VERGE-2023` 数据表**。2026 年在售平台已切到 **Marvell AC5 / AC5+**，个别条目（ACL 条数、队列数、满载 PoE 预算）**必须以工厂当期 release note 为准**，不得直接拿 2021 数据表对客户做承诺。

---

## 八、两个技术陷阱（这两条决定报价生死）

### 8.1 「56 Gbps」陷阱
`3.4.6` 要求 **≥56 Gbps**。而 **24×1G + 4×1G SFP 的线速上限恰好 = 24×2 + 4×2 = 56 Gbps**。
⇒ **刚好达标，一分余量都没有。** 任何「24 口 + 2 光」的机型（24×2+2×2 = **52 Gbps**）**直接废标**。
⇒ **对外报价 24 口，光口一律按「4 口起」配置**，这是本标最容易被对手用参数秒杀的一条。

### 8.2 「全口 af/at」的 PoE 预算陷阱
`3.4.3` 要求**全部 24 个铜口**支持 af/at：
- 24 × 15.4 W（af 满载）= **369.6 W**；24 × 30 W（at 满载）= **720 W**
- **750 RMB 的 `LT-S8328GP-4GX24GT-S` 只有 280 W** ⇒ 24 口 af 满载差 **90 W**
- 440 W 的 `LT-S8328GP-4GX24GT` 售价 **1,200 RMB**（+60%）⇒ 若按 $140 卖，**从赚 251 RMB 变成亏 199 RMB**

⇒ 结论：**24 口那一包必须先问清「PoE 是能力要求还是满载要求」**。若条款只要求「每口支持 af/at」（本标文字确实只写「支持」），280 W 机型合规；一旦现场按满载验收，必须换 440 W 机型，报价要 **$200 起**。

---

## 九、证书经济学：三条路，成本差一个数量级

| 路线 | 做法 | 成本 / 周期 | 谁承担 | 风险 |
|---|---|---|---|---|
| **A 借证（现行）** | 挂在 Angora 的 2019 年工业 8 口证书下，**固件版本号对齐** | **0 元**，1–2 周对版本 | Angora | 一旦我方固件升版，证书失效；且只覆盖 8 口族 |
| **B 外置 shaping 盒子** | 交换机本体不含 shaping，另配**同品牌**外置 traffic-shaping 设备，该设备同样持 BAŞARILI 报告 | 一台小盒子的重测费（未查到公开价） | 我方 | 需同品牌；客户要接受「两台设备」 |
| **C 整机重测** | 送 EGM Bilgi Teknolojileri ve Haberleşme Dairesi 重做 C-Tipi 报告 | **费用/周期均无公开数据**（待办 ㊶ 仍空） | 我方 | 报告中「软件版本」与量产品必须一致，任何固件改动都可能触发重测 |

⚠ **C 路线的钱与时间仍查不到**：土耳其 EGM 的实验室测试不对社会公开报价（TSE/TÜBİTAK MAM 有公开价目表，EGM 没有）。**只能通过 Angora 问 Levent 要去年那次的实际账单** —— 这是本轮回溯出的一条具体动作。
⚠ **B 路线的条文出处是二手**（turk-iot 转述现行 şartname：「流量整形解决方可作为同品牌外置设备单独报价」），**必须拿到 EGM 官方 şartname 原文再引用**。

---

## 十、结构性事实：省市级标我们根本不能投

| 事实 | 原文 | 源 |
|---|---|---|
| 仅限本国投标人 | 「İhaleye **sadece yerli istekliler** katılabilecektir」 | Adana İKN 2026/1248553（31.07.2026） |
| 本地货价格优势 | 「yerli malı teklif eden yerli istekliye ihalenin tamamında **%15** oranında fiyat avantajı」 | Ordu/Ünye KGYS Genişleme（25.08.2026） |
| 需本地资质 | İmalat Yeterlik Belgesi / Kapasite Raporu / Sanayi Sicil / **Yerli Malı Belgesi** / Yetkili Satıcı | Adana 同标 4.3.1 |
| 交付期 | Adana **100 天**；Bursa **60 天** | 两标公告 |

⇒ **我方无法直接投标，只能作为 Angora 的 ODM。** 而 Angora 的 **Yerli Malı Belgesi** 是真正稀缺的那张纸 —— 比 EGM 证书更值钱，因为它带来 **15% 价格优势** + 参与资格。

---

## 十一、2026 年 7–12 月在跑的标单（本轮外部扫描，含 IKN/日期）

| 日期 | 标的 | 关键点 | 源 |
|---|---|---|---|
| 2026-07-10 发布 / **07-31 开标** | **Adana** KGYS+PTS+**ÇGKS** 备件 **14 kalem** | İKN **2026/1248553**；**仅本地**；100 天交付；不设电子降价 | referansturk |
| 2026-07-21 发布 | **Diyarbakır** İl Emniyet **2026 ÇGKS 备件** | 省级重复性备件市场 | ihalehaberi |
| 2026-07-21 发布 / 08-25 | **Ordu/Ünye** KGYS Genişleme **9 çeşit** | **本地货 +15%** | orduolay |
| 2026-06-24 发布 / 07-08 开标 | **Bursa** KGYS+PTS **5 kalem** | 仅本地；60 天交付 | bursadabugun |
| 2026-08-10 发布 / 08-25 | **Gümüşhane** KGYS+PTS 材料（含立杆/开挖） | 土建混装 | gumuskoza |
| 2026-08-01 发布 / 08-19 | **Manisa/Şehzadeler** 网络交换机 + 无线 + 摄像头 | İKN **2026/1370159** | manisadenge |
| **2026-09-25 发布** | **Mardin** 2026 KGYS-ÇGKS 备件 | 新 | ihalehaberi |
| **2026-12-07 开标** | **Şırnak** 4 个县 KGYS 基建/安装/现代化，90 天 | 最新在跑 | sirnakhaber73 |

**中标侧（合同金额，含 KDV）**
| 项目 | 中标方 | 合同日 | 金额 | 源 |
|---|---|---|---|---|
| Eskişehir ÇGKS+KGYS 安装材料 | **LINK Bilgisayar** | 2026-06-24 | **13,621,371.60 TL**（≈$272k） | endeks24（页面已 404，取自检索摘要） |
| **EGM KGYS 扩建项目材料** | **LINK Bilgisayar** | 2026-07-07 | **24,024,650.00 TL**（≈$480k） | 同上 |
| EGM 人脸识别摄像 | **LINK Bilgisayar** | 2026-08-13 | **11,554,000 TL**（≈$231k） | 同上 |

⇒ **LINK Bilgisayar 是 2026 年下半年这个市场的实际承接者**（三个月内三个 EGM 单，合计 **49.2M TL ≈ $983k**）。它不在我方 146 家客户名单里 —— 这是本轮挖出的**新渠道线索**。

---

## 十二、Ewind 对照（本轮只做时间戳，确认零变化）

| 通道 | 本轮实测 | 与 r83（同日 11:47Z）比 |
|---|---|---|
| `product-sitemap` | **2026-08-26T09:42:11** | 不变 |
| `post-sitemap` | 2026-06-11T09:24:42 | 不变 |
| `page-sitemap` | 2026-07-22T10:04:12 | 不变 |
| `exhibition-sitemap` | 2025-11-05T07:31:43 | 不变 |
| `product_cat` / `product_tag` | 2026-08-26 / 2026-04-16 | 不变 |

**价格对照（把 r83 的 FOB 放进本轮的招标价里看）**
- Ewind 10 口 L2+ 网管工业 PoE **$98.30–121.60** FOB
- 我方 8 口工业 PoE（L3，2×SFP）工厂价 **780 RMB ≈ $109**
- D-Link 对伙伴全包价 **$135**
⇒ **三家落在同一条 30 美元的带子里**：Ewind $98–122、我方 $109、D-Link $135（全包）。
⇒ **「$98 的中国工厂」与「$135 的全包 D-Link」之间只剩 37 美元**，中间要装下：SFP 模块、电源、运关、分销、汇率、账期。**这个带子已经装不下第四个人。** 这也解释了为什么我方在 4 月只能报 855 RMB 并落到第 3 名。

---

## 十三、行动（七条，按优先级）

1. **🔥 把「24 口 = 无证书门槛」这条立刻告诉 Angora**：KGYS 3.4 / ÇGKS 3.3.1 全段无 C-Tipi 条款 ⇒ 24 口标可以**用我方白牌 + 任何本地品牌**直接投，这是最快能起量的口子，而且**单台毛利是 8 口的 5 倍**（251 vs 50 RMB）。
2. **🔥 报价前锁死两个参数**：光口 **4 口起**（否则 52 Gbps 废标）；PoE 是「能力」还是「满载」（决定 280 W 还是 440 W 机型，差 450 RMB/台）。
3. **🔥 向 Levent 要去年 C-Tipi 的实际账单与周期**（C 路线唯一的成本来源），同时索取 **EGM 官方 şartname 原文** 核实「同品牌外置 shaping」条款（B 路线）。
4. **⭐ 拿 24 口逐条矩阵去对客户的现行 şartname**（本文件 §7 已可作底稿），并把 3 处 ⚠ 一次性补死（ACL 条数 / 满载 PoE / 随箱配件）。
5. **⭐ 新渠道：LINK Bilgisayar**（三个月三个 EGM 单，$983k）—— 它现在是中标方，不是竞争者；作为「有合同、无自有硬件」的系统集成商，是比 Proline 更直接的 ODM 客户候选。
6. **⭐ 顺着 2026 年 7–12 月的省级备件标跟踪**（Adana/Diyarbakır/Mardin/Ordu/Gümüşhane/Bursa/Şırnak/Manisa）：这些标**只许本地投**，但每个都可能是 Angora 的入场券 —— 让我方按「本地合作伙伴中标 → 我方补 8 口/24 口现货」的模式准备**常备库存清单**。
7. **🕐 未结**：军方 24 口车载机 `24-Port Gigabit _Military_Switch_Spec_DraftC.pdf` **不在语料内**，需 Angora 补发；Turk Telekom 48 口工业 PoE+ L3 的正式 RFP 未到。

---

## 十四、修正清单与证据等级

### 修正（3 条，均点名 r83）
见 §2。另附一条**对语料整体的修正建议**：`01-text-verbatim/警察局项目/KGYS.txt` 的中文摘要**缺 3.4.30–3.4.44 以及 3.3 的 3.3.1 交付条款**（该文件只有 2,912 B），完整的 44 条在 `EGM.txt` 与 `Turkey_Police_RFP_Compliance_Template.xlsx` 里 —— **以后引用 3.4 必须引 `EGM.txt`，不能引 `KGYS.txt`**。

### 证据等级
**语料一手（16）**：`警察局项目/KGYS.txt` · `警察局项目/EGM.txt` · `警察局项目/ÇGKS.txt` · `RFP/2024.7.2_C TİPİ ETHERNET ANAHTAR KGYS.pdf.extracted.md` · `警察局项目/CGKS_Section_3.3_Network_Switches_EN.pdf.extracted.md` · `警察局项目/EGM_Sections_3.3_3.4_EN.pdf.extracted.md` · `警察局项目/KGYS_Section33_Translation_EN.pdf.extracted.md` · `警察局项目/Turkey_Police_RFP_Compliance_Template.xlsx.extracted.md` · `警察局项目/CGKS_Field_Switch_DLink_DIS300G_Compliance.xlsx.extracted.md` · `ANW-VERGE-2023-ENTERPRISE-DATASHEET-20210423-TR.pdf.extracted.md` · `ANW-VERGE-2023-INDUSTRIAL-DATASHEET-20210423-TR.pdf.extracted.md` · `SmartByte managed Ethernet switch pricelist 2026.09.1–2026.12.30` · `SmartByte Managed Industrial …pricelist 2026.09.1–2026.12.30` · `01-knowledge-base/wechat-2026.md`（2026-03-06 / 04-16 / 04-22 / 04-28 / 05-20 / 05-22 / 06-05 / 08-26 / 08-30）· `AI-2026-04-16 Levent / 04-22 Levent / 05-22 Levent` 三段对话 · `09-orders/120-angora-orders-dossier-2026-10-21.md` · `01-knowledge-base/commercial-docs/cgks-field-switch-dlink-dis300g-compliance-xlsx.md`。

**外部（18）**：`ihaleciler.com/tenders/search?tender_ts_meta=kamera`（五包结构，两处检索命中一致）· `referansturk.com.tr`（Adana İKN 2026/1248553，14 kalem，31.07.2026，仅本地）· `ihalehaberi.net`（Mardin 25.09.2026 / Diyarbakır 21.07.2026）· `orduolay.com`（Ordu/Ünye 25.08.2026，+15% 本地货）· `gumuskoza.com.tr`（Gümüşhane 25.08.2026）· `bursadabugun.com`（Bursa 5 kalem，60 天，仅本地）· `sirnakhaber73.com`（Şırnak 07.12.2026）· `manisadenge.com`（Manisa İKN 2026/1370159）· `endeks24.com`（LINK 三单；**页面已 404，取检索摘要**）· `turk-iot.com`（持证品牌清单 + 外置 shaping 条款 + 旧报告有效）· `guvenlik.teknolojileri.net` 2018 学校 şartname（同一「harici」条款的另一处佐证）· `ewindnet.com/sitemap_index.xml`（本轮实测，零变化）· `ictmedia.com.tr`（Angora OEM 自述）· 价格锚：`alibaba` r83 数据（复用，不重复抓）。

**共 34 个来源**（语料 16 + 外部 18）。

### 空白（诚实边界）
- **EGM C-Tipi 报告的费用与周期仍无任何公开数据**（TSE/TÜBİTAK 有公开价目表，EGM 无）⇒ 待办 ㊶ 继续挂。
- **「外置同品牌 shaping」条款只见二手转述**，未取到 EGM 官方 şartname 原件。
- **2026-04 国标招标的中标方与中标价均未查到**（EKAP 结果公告未公开索引）；只知我方伙伴第 3 名。
- **`24-Port Gigabit _Military_Switch_Spec_DraftC.pdf`（360.6 KB）不在语料内**，军用机规格完全空白。
- **`ANW-VERGE-2023` 数据表是 ©2021 版**，与 2026 年 AC5 平台的差异未逐条核对；ACL 条数、队列数、满载 PoE 预算三项**必须工厂书面确认**。
- **Adana 标「14 kalem」的明细未取**（EKAP 需登录）—— 不知道里面有没有交换机。
- **LINK Bilgisayar 的联系人与主营未挖**（只知道它连中三个 EGM 单）。
- 价格：D-Link $135 是**伙伴口述**，未见报价单原件；我方 830 RMB 是**微信议定**，未见合同。
