# 🏛️ Angora 政府项目 · 认证资质 · 已落地案例

> **采集日期：2026-09-27**（第 9 轮深挖）
> 关联任务：第 2 轮 §3「他们目前主要是做政府类项目，挖进展、竞标、拿到的项目」、
> 第 9 轮 §4「竞标情况挖的如何，深度挖取」。

---

## 一、⭐⭐⭐ EGM / KGYS 认证 —— 警方城市安全监控系统准入

**来源**：`angoranetworks.com/angora-networks-egm-trafik-sekillendirme-gereklilik-testlerini-gecti/`

### 1.1 事实陈述
> *"Angora Networks **endüstriyel 8 port Layer 2+ Yönetilebilir Ağ Anahtarları**, testleri başarıyla geçmiş…*
> *EGM tarafından onaylanmıştır."*
> *"Angora Networks endüstriyel anahtarlar, tüm testleri başarıyla geçmiş ve **EGM'nin ülke çapındaki projelerine katılım sertifikası** almıştır."*

| 项 | 内容 |
|---|---|
| 认证机构 | **EGM  bilgi teknolojileri Dairesi**（土耳其警察总局 信息技术司） |
| 项目 | **KGYS — Kent Güvenliği Yönetim Sistemleri**（城市安全管理系统／全国安防摄像头监控网） |
| 通过产品 | ⭐ **工业级 8 口 L2+ 网管交换机** |
| 测试内容 | 物理与电气性能 + **流量整形（traffic shaping）** + **丢包率** 等功能性能 |
| 结果 | ⭐ 取得 **EGM 全国项目参与证书**（katılım sertifikası） |

### 1.2 ⚠️ 时间校正（重要）
- 该页页脚为 **"© 2019 Angora Networks"**，页面邻近文章为 2020-11-24、2021-01-01。
- 搜索引擎给出的 `pageAge 2026-06-15` **是错误的**（抓取时间≠发布时间）。
- ✅ **结论：EGM/KGYS 认证取得于 2019–2020 年间，不是 2026 年新闻。**
  （与此前档案中"EGM 2021 通过，已更正"一致。）

### 1.3 🎯 对我方的战略含义（极高价值）
> ⚠️ **Angora 的工业 8 口 L2+ 交换机已持 EGM 全国项目参与证书，且通过"流量整形 + 丢包"测试。**

- 这**正是** Simon 在争的警方项目品类（我方供货型号为 **工业 2 光 8 电**）。
- Angora **自己有持证型号**，意味着他们**不一定非要从我方采购 8 口工业交换机** ——
  他们买我方货，更多是**成本/交期**驱动，而非"没有替代品"。
- ⭐ **但反过来**：正因为他们有证，一旦我方产品**被纳入其持证型号体系**（换牌/共证），
  我方就获得了进入 EGM 全国项目的通道。这是**我方最大的谈判筹码**，也是最大的脆弱点。

---

## 二、⭐ 已落地项目清单（多源汇总）

| 客户 / 项目 | 品类 | 时间 | 来源 | 备注 |
|---|---|---|---|---|
| **TRT 安塔利亚园区** | 全网 + WiFi | 2022 前 | KOZ'23 视频（Can Hayat） | ⭐ **整网替换**：原用其他品牌"持续出问题"→批量换成 Angora → 二次采购 |
| **Konya Plato 项目** | — | 2022 前 | 同上 | TRT 之后的第二次采购 |
| **Eskişehir** | 工业交换机 | 2022 前 | 同上 | — |
| **Antalya** | 工业交换机 | 2022 前 | 同上 | ⭐ 多雨、雷击、夏季高温环境 |
| **EGM / KGYS** | 工业 8 口 L2+ | 2019–2020 | 官网 | 已取得全国项目参与证书 |
| **KGS 城市交通监控** | — | — | KOZ'23 视频 | 凭 **trafik şekillendirme raporu**（流量整形报告）可参与投标 |
| 客户墙 11 家 | 含 **TSK 武装部队**、**MSB 国防部** | — | 官网 RU 版镜像 | 军工属性 |

> 📌 已确认的**具体项目**仍偏少。土耳其公共采购平台 EKAP 未被搜索引擎索引，
> 中标记录无法通过公开检索获得 —— 这是结构性盲区，已记录为已知限制。

---

## 三、⭐ VERGE 产品线温度规格（直击 TT 温度争议）

**来源**：`angoranetworks.com/network-devices/`（页面 time 2025-06-11）

| 产品线 | 端口 | 上行 | **工作温度** | 供电 | 安装 | PoE |
|---|---|---|---|---|---|---|
| **Industrial 8 Port（工业 8 口）** | 8×1G | 2×1/10G SFP+ | ⭐ **−40°C ~ +80°C** | 48V DC | DIN 导轨 | PoE / 非 PoE |
| Enterprise 8 Port | 8×1G | 2×1/10G SFP+ | — | PoE+ 180W AC | 19" 1U | — |
| 8/24/48 Port | 8/24/48×1G | 4×1/10G SFP+ | — | PoE+ 380W AC | 19" 1U | — |
| **Data Center / TOR** | 24/48×1G/10G/25G | **4/6/8×100G QSFP28** | — | 冗余热插拔电源 | 19" 1U | — |
| — | — | — | — | — | — | **3.6 Tbps** 超低时延 |

功能：VLAN / QoS / MSTP / LACP / Ring / EEE / GVRP / LLDP / 802.1x / PoE+ / 堆叠 / 告警继电器 / IPv6 / 组播 / **静态路由**；
Data Center 档另有 **OSPF / LISP / VXLAN / MC-LAG / BGP / REST API / MPLS / RSVP / L3VPN / VRF**。

### 3.1 🎯 与 TT 温度问题的对照
| 口径 | 温度 | 出处 |
|---|---|---|
| **Angora VERGE 工业标称** | **−40 ~ +80 °C** | 官网产品页（2025-06） |
| TT 招标要求 | **−45 ~ +85 °C** | 招标文件（见 `05-turk-telekom/`） |
| 我方对 Levent 的口径 | **+75 °C（PoE 满载）** | 微信 2026 年对话 |

> ⚠️ **关键洞察**：
> 1. **Angora 自己的工业交换机也只标 +80°C，达不到 TT 的 +85°C** —— 说明 +85°C 在行业内是极苛刻要求，
>    不是我方独有短板。
> 2. 我方说 **+75°C 是在 PoE 满载**前提下；用户已明确：**常规运行可宣传 85°C 且能过测试**，
>    只是**满载**才降到 75°C。
> 3. → **建议口径**：对外提供**双规格**——常规运行 **−40~+85°C**、**PoE 满载 −40~+75°C**。
>    这既诚实，又把比较基准拉回到与 Angora 自标 +80°C 可比的区间。

---

## 四、⭐ 分销商与渠道结构（更新版）

| 渠道方 | 性质 | 证据 | 状态 |
|---|---|---|---|
| **ELCORE**（Elcore Group） | ⭐ **国际增值分销商（VAD）** | ① KOZ'23 峰会议题 *"ANGORA & ELCORE İş Birliği ve Distribütör Gücü"*；<br>② **Angora 官方 LinkedIn 更新中直接出现 `info.tr@elcoregroup.com`**；<br>③ Aykut Dalyan = **Elcore Türkiye Country Manager**（elcorecloud.com/contact/ 确认） | ✅ **已证实** |
| **filteknoloji** | **Kaleiçi 非网管系列独家销售** | KOZ'23 视频（Can Hayat）：*"bunların da tek satış yetkilisi filteknoloji"* | 🆕 待深挖 |
| **Advensis** | 分销商 | ZoomInfo 提及（"Advensis dealer"） | ⚠️ 证据较弱，待核 |
| **81 城市经销商与服务网** | 渠道网络 | 官网 / ictmedia 报道 | ✅ |
| **Club Angora**（angora.club） | 🆕 伙伴互动平台，有"Angora Card"权益 | KOZ'23 演讲提及（26:17 Club Angora）；SIBEREUM 的 Gökhan Şenşükür 背书 | 🆕 抓取失败，待重试 |

### 4.1 ELCORE 概况
- **国际 VAD**，业务覆盖 **11 个国家**（东欧、中亚、土耳其）：乌克兰、瑞士、摩尔多瓦、阿塞拜疆、蒙古、
  亚美尼亚、塔吉克斯坦、格鲁吉亚、土库曼斯坦、吉尔吉斯斯坦、哈萨克斯坦、乌兹别克斯坦、土耳其
- 土耳其公司 **2021 年成立**，三年内成为"全国最强分销商之一"
- 土耳其办公室：**Ataşehir / 伊斯坦布尔，Kardelen No:2, Halk Cd. Palladium Tower, 34746**，+90 216 687 08 82
- LinkedIn 关注者 2,177
- 代理品牌（部分）：**Forseca、Gatewatcher、Sangfor、Supermicro、Sectona**（2025-10 起）

> 💡 **战略含义**：ELCORE 是**跨国分销集团**，覆盖中亚与东欧。
> 若 Angora 借 ELCORE 出海（Levent 2020 年即说"要做大出口"），
> 我方作为其供应商有可能**间接受益于出口增量** —— 值得在对话中试探出口项目的需求。

---

## 五、📌 结构性盲区（已知限制，非遗漏）

| 项 | 原因 | 备注 |
|---|---|---|
| **EKAP（土耳其公共采购平台）** | 未被搜索引擎索引，无公开检索接口 | 中标记录无法系统获取 |
| 具体中标金额 | 土耳其不公示落标价格明细 | 与国内政府采购网不同 |
| 2025–2026 政府项目 | 无公开信源 | 仅能通过 Angora 自述与微信对话侧面推断 |
| Instagram 内容 | 抓取 403，需登录 | 已定位账号 `angora_networks` |

---

## 六、🎯 汇总：Angora 政府项目打法（可反推）

1. **持证先行** —— 先拿到 EGM/KGYS 参与证书、KGS 流量整形报告等**准入资质**
2. **国产化率** —— 交换机 68% → 目标 80%（政府项目的硬门槛）
3. **"斩结"战略** —— 用骨干交换机楔入政府机构，再横向铺开其他产品（Gordion 命名隐喻）
4. **渠道杠杆** —— 借 ELCORE 这类国际 VAD 做全国覆盖与出海
5. **伙伴生态** —— Club Angora 绑定经销商，KOZ 峰会年度化
6. **供货速度** —— 承诺 ≤10 周，对标竞品 450–500 天（这是他们最锋利的刀）

> ⚠️ 我方在这六条里**唯一能正面竞争的是"供货速度"**，其余五条都必须通过与 Angora 绑定来满足。
> 这解释了为什么 Levent 说 *"You are our strategic partner"* ——
> **他需要我方的产能与交期，正如我方需要他的资质与渠道。**
