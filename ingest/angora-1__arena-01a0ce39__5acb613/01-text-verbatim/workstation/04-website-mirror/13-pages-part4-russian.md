# Angora 官网俄文版镜像（angoranetworks.com/?lang=ru）
> 抓取日期：2026-09-23
>
> ✅ **突破**：新域名 `angorateknoloji.com` 已确认**彻底不可用**（根域 fetch 失败、`/blog/` 与子页一律 404，Cloudflare 限流）。
> 但**旧域名 `angoranetworks.com/?lang=ru` 完全可用**，俄文内容此前从未采集。本文件补上这一缺口。
> 语言切换器确认站点为 **WPML 三语**（TR / EN / RU）。

---

## 1. 首页（RU）— 客户墙与合作伙伴

### 我们的推荐 / 客户墙（Наши рекомендации）
| 标识 | 机构 |
|---|---|
| havelsan | **HAVELSAN**（国防电子） |
| Turkcell_KKTC | Turkcell 北塞浦路斯 |
| saglik_bakanligi | **卫生部** |
| aselsan | **ASELSAN**（国防电子龙头） |
| egm | **EGM 警察总局** |
| anadolu_universitesi | 安纳多卢大学 |
| **tsk** | ⭐ **TSK 土耳其武装部队** |
| **msb** | ⭐ **MSB 国防部** |
| turksat | Türksat（卫星） |
| tcdd | TCDD 国家铁路 |
| kgm | KGM 公路总局 |

> ⚠️ **TSK（武装部队）+ MSB（国防部）在客户墙上** → 与 2026-06-05 微信中的"车规军品交换机"机会直接呼应。
> 该机会已于 2026-06-17 被 Levent 明确 PASS（"1-b Military switch (we PASS this one)"）。

### 合作伙伴（Наши партнеры）
`alaattin_bilisim` · `fi_teknoloji` · `sonersan` · `intel` · `abb` · `ubuntu` · **`larch`** · **`marvell`** · `rasberrie` · `sixfab` · `samm` · `dmy` · `astesan`

> `larch` 与 `marvell` 同列合作伙伴墙 —— 这是 Angora–Larch 关系的**官网级佐证**（用户已下令停止深挖 Larch，此处仅作既存记录）。
> 另：瘦客户机业务指向 **thince.net**；支持门户 **support.angoranetworks.com**。

---

## 2. ⭐ VERGE 系列规格总表（RU 页，含 DC/TOR）
> 来源：`/verge-network-switch-family/?lang=ru`

| | 工业 8 口 | 企业 8 口 | 24 口 | 48 口 | **数据中心 / TOR 边缘路由** |
|---|---|---|---|---|---|
| 端口 | 8×1G + 4×1/10G SFP+ | 8×1G + 2×1/10G SFP+ | 24×1G + 4×1/10G SFP+ | 48×1G + 4×1/10G SFP+ | 48×1G/10G/25G + **6×100G QSFP28** |
| 吞吐 | — | — | — | — | **3.6 Tbps，超低时延** |
| 特性集 | **L2+** | L2/L2+/L3 | L2/L2+/L3 | L2/L2+/L3 | **DC/TOR 特性集 + 高级 L3 路由** |
| 场景 | 工业标准、严苛环境 | 企业级 | 企业级 | 企业级 | Multi Scope, Programmable |
| PoE | 每口最高 30W | 每口最高 30W | 每口最高 30W | 每口最高 30W | — |
| 电源/结构 | **−40℃ ~ +80℃、48V DC、DIN 导轨** | 180W AC，19" 1U | 380W AC，19" 1U | 740W AC，19" 1U | 冗余热插拔电源，19" 1U |
| 关键特性 | VLAN, QoS, MSTP, LACP, Ring, EEE, GVRP, LLDP, 802.1x, PoE+, Stacking, Alarm Relay, IPv6, Multicast, **Static Routing** | 同左 | 同左 | 同左 | **OTP, LISP, VXLAN, MC-LAG, BGP6, REST API, MPLS, Multicast RSVP, L3VPN, VRF** |

### 🔴 从这里读出的战略事实
1. **Angora 对外销售 Enterprise 机型时标称 L2/L2+/L3，DC/TOR 标称"高级 L3 路由"（含 VRF/MPLS/BGP6/L3VPN）**。
2. 但我方 `Saga Feature List_7.5.x_L2+` 的 IP Route 大类**只有 Static Route** —— **表里不一，这是当前最大的能力缺口**。
3. 这个缺口正是 `Reply on SAGA Enterprise L3 Recommendation Report`（2026-08-17）承认并用 **CENTEC L3** 填补的：
   *"Saga has already fixed its chipset solutions on Marvell L2+ and CENTEC L3, this is a strategic move."*
4. **DC/TOR 机型确实存在**（3.6 Tbps / 6×100G QSFP28）→ 与仓库中已解析的 `INFO_2025.12.17/ANW-DC-RFP-EN.pdf` 对应。
5. 工业 8 口标称 **−40℃ ~ +80℃**，比我方资料中 TT 验收口径（−40~+75）**更宽**，属营销标称值。

**下载**：工业交换机数据表 `/download/425/`；8-24-48 口数据表 `/download/428/`

**该页客户墙**：Turkcell_KKTC、KGM、**TSK**、Türksat、TCDD、**MSB**、ASELSAN、HAVELSAN、Anadolu Üniversitesi、EGM、卫生部

---

## 3. ⭐ IRIS SFP 系列完整 SKU 表
> 来源：`/iris-sfp-family/?lang=ru`

| 型号 | 类型 | 接口 | 速率 | 介质 | 距离 |
|---|---|---|---|---|---|
| **ANW-SFP-1G-T** | 1000Base-T SFP | RJ45 | 1.25 Gbps | CAT5 及以上 UTP 铜缆 | 100 m |
| ANW-SFP-1G-SX | 1000Base-SX SFP | LC | 1.25 Gbps | 多模光纤 | 550 m |
| **ANW-SFP-1G-LX** | 1000Base-LX SFP | LC | 1.25 Gbps | 单模光纤 | **10 km** |
| ANW-SFP-10G-SR | 10G SR SFP+ | LC | 10.3125 Gbps | 多模光纤 | 300 m |
| ANW-SFP-10G-LR | 10G LR SFP+ | LC | 10.3125 Gbps | 单模光纤 | 10 km |

其他：全系 **RoHS**、**热插拔**、**全金属外壳**；产品线从 1G 铜模到 **QSFP28 100G**。
数据表下载：`/download/485/`（IRIS-10G）、`/download/488/`（IRIS-5G）、`/download/491/`（IRIS 100G）

### 🔴 与 2026 招标的直接对应
2026-04-16 Karen（NEM Engine）报价 **"1G LX 1310nm 10Km 商用 25 元"** ——
**精确对应上表的 `ANW-SFP-1G-LX`（1000Base-LX，单模，10 km）**。
→ 即 Angora 招标包里的 SFP 就是自有 IRIS 品牌的这一款；我方按 25 元供模块，Angora 贴 ANW 标。

> 官网原文自称 *"Мы производим собственные конвертеры..."*（我们自己生产转换器），
> 但又明说 *"Наши оптические и медные модули можно использовать во всех моделях Verge"* ——
> 即 IRIS 是**品牌化的外采模块**，与我们从 NEM/Karen 供货的模式一致。

---

## 4. 新闻稿一：Data Diode 支持 ModBUS / OPC（2023-12-05，安卡拉）
> `angora-networks-представляет-поддержку-протоколов`（注：URL 字面为 "представляет"，正文首句为 "объявила"）

**要点**
- Angora 将 **ModBUS 与 OPC** 协议支持集成进其 **Data Diode（数据二极管）** 方案
- Data Diode = **单向数据流**，用于**物理隔离**并保护网络基础设施
- 目标行业（原文列举）：**电力与燃气输配、制造、金融、军事行动（военные операции）** 等
- 收益：封闭工业网络的实时监视、缩短事件响应时间、实时商业智能分析
- 定位原文：*"не просто поставщик, но стратегический, долгосрочный партнер"*（不只是供应商，而是战略性长期伙伴）

> ⚠️ **"军事行动" 被明列为 Data Diode 目标行业** —— 再次印证 Angora 在国防/军用方向的既有布局，
> 与 2026-06-05 的车规军品交换机机会是同一条脉络。

---

## 5. 新闻稿二：Cisco ISE 集成完成（2021-06-21，安卡拉）
> `angora-networks-cisco-ise-завершила-интеграцию`

**要点** —— Angora 交换机完成与 **Cisco ISE（Identity Services Engine）** 的 802.1x 集成，与一家"重要客户"共同完成：
- 支持特性：**802.1x、AAA、授权变更 CoA、Profiling（画像）、Posture（态势）、动态 VLAN 下发、动态 ACL 下发、RADIUS、TACACS+** 及同类
- ⭐ 关键竞争话术（原文）：全部功能*"работать с профилями, используемыми для коммутаторов Cisco, и **не требуют внесения изменений в существующую конфигурацию ISE**"*
  → **与 Cisco 交换机所用的 profile 完全兼容，且无需改动现有 ISE 配置。**
- 战略含义：Angora 打的牌是 **"可平替 Cisco 接入层，而不动你已有的 Cisco ISE 策略体系"**。
  结合 Levent 有 **15 年 Cisco 土耳其电信客户经理**背景，这条产品线显然是他主导设计的。

---

## 6. 抓取方法备注（供复用）
- 俄文路径规律：`https://www.angoranetworks.com/<英文 slug>/?lang=ru`；也可用 `?page_id=<N>&lang=ru`
- 已知可用 page_id：**298 → VERGE 交换机系列（会 301 到 slug）**、**316 → IRIS SFP 系列**、**275 → 服务/培训**
- 每页底部有 WPML 语言切换器，可拿到 **EN / TR 对照 URL**，便于三语交叉核对
- 每个子页底部都重复出现"客户墙"与"合作伙伴墙"，是交叉验证客户名单的好来源
- ⚠️ 评论框有 reCAPTCHA，评论区不可抓；文章正文可完整抓取

---

## 7. 仍缺失
- [ ] **新域名 `angorateknoloji.com` 全站** —— 确认不可用（根域 fetch 失败 + 子页 404），建议放弃
- [ ] EN/TR 版本的部分页面（此前 `10/11/12-pages-part*.md` 已覆盖大部分）
- [ ] `/download/425/`、`/428/`、`/485/`、`/488/`、`/491/` 等数据表 PDF（需直接下载，未取）
- [ ] 评论区（reCAPTCHA 阻断）
