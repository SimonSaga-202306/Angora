# 🔥 Larch Networks ↔ Saga（Alan Guo）邮件往来全记录

> 2026-09-23 · 来源：main 分支新上传的 5 个 Gmail PDF
> 全文已提取至 `workstation/99-raw/larch-emails/*.txt`

---

## 一、往来总表

| 日期 | 主题 | 方向 | 消息数 |
|---|---|---|---|
| 2025-05-21 | **Managed Optical Bypass Switch** | Saga(Alan) → Larch(info@) 主动推销 | 8 |
| 2025-11-27 | **Booster PoE Switch** | Saga(Alan) → Larch(Alexander) 主动推销 | 11 |
| 2026-03-30 | **Updated Ethernet Switches Links**（附 Product Link_2026Q2.pdf） | Saga(Alan) → Larch 主动推销 | 7 |
| **2026-05-22** | **Supported SONiC for Saga Ethernet Switches \| COMPUTEX** | ⭐ **Larch CEO → Saga 主动邀约** | 10 |
| **2026-07-02** | **Request for DX1518/DX1548 Chips** | ⭐ **Larch → Saga 紧急求购芯片** | 2 |

> **结论：双向都有主动接触。不是 Larch 单方面找我们，Alan 也一直在向 Larch 推销产品。**

---

## 二、Larch 侧人员名单（全部邮箱）

| 姓名 | 邮箱 | 角色 |
|---|---|---|
| **Alexander Cheskis** | alexander@larch-networks.com | **CEO**（联合创始人） |
| **Oksana Loi / Loy** | oksana@larch-networks.com | 采购/业务（发芯片求购） |
| **Alexander Gribenko** | a.gribenko@larch-networks.com | 技术/业务 |
| **Andrey Zarudniy** | azarudniy@larch-networks.com | 业务 |
| **Inna Murzina** | imurzina@larch-networks.com | 市场/业务 |
| — | sales.team@larch-networks.com / info@larch-networks.com | 通用 |

**Saga 侧**：**Alan Guo** <a.sagatelecom@gmail.com>（Saga Telecom / OEM Factory）

---

## 三、⭐ 2026-05-22 Larch CEO 主动邀约（最有价值）

> **Alexander Cheskis, CEO, Larch Networks → Alan**
>
> "I hope you are doing well. You shared your updated Ethernet switch product links with us
> earlier this year, and I wanted to reconnect ahead of COMPUTEX.
>
> **Larch Networks can help switch vendors add a commercially supported SONiC option without
> building a full in-house NOS team.** Our package is not just development work: it includes
> **Larch Hardened SONiC, platform enablement, long-term maintenance, security and bug-fix updates,
> and Tier-2/Tier-3 support under an annual license/support model.**
>
> Given **Saga's 8/24/48-port managed switch portfolio and industrial/commercial focus**,
> this could be a practical way to offer customers a more open and programmable software option.
>
> **We will be at COMPUTEX / InnoVEX, booth S0905.** Would you be open to a short meeting in Taipei
> to discuss whether SONiC could fit one of Saga's switch lines?"

### 解读

1. **Larch CEO 亲自发来合作邀约**，明确说能帮 Saga 补上 SONiC 软件能力，**不用自建 NOS 团队**。
2. **这正好解决 Levent 要的那套 L3**（SONiC 支持 BGP/OSPF/VRRP/ECMP 等）。
3. **Larch 知道 Saga 的产品线是 8/24/48 口 + 工业/商用** —— 说明他们研究过我方。
4. **商业模型：年费制授权 + 支持（annual license/support model）**。
5. 展位 **COMPUTEX / InnoVEX 2026, booth S0905**（台北，6 月 2–5 日）。
   → 与 Larch 官网 2026-04 那条"InnoVEX 2026 @ COMPUTEX TAIPEI"新闻完全对应。

---

## 四、⭐ 2026-07-02 Larch 紧急求购芯片（Saga 拒绝了）

> **Oksana Loi → Alan**（抄送 Alexander Gribenko、Alexander Cheskis）
>
> "We would greatly appreciate your assistance. **We urgently need 10 pieces of DX1518/DX1548 chips
> (any variant is acceptable) for our customer.**
> Could you please let us know if you have any of these chips in stock? If so, would it be possible
> to purchase them from you?"

> **Alan 回复**：
> "But sorry to tell you that it is not available. **We do not use this chip a lot**, and as you know,
> **Marvell has a very rigorous review for chip purchases**..."

### 解读（⚠️ 高价值信号）

1. **Larch 在 2026 年 7 月出现了芯片短缺**，而且是"urgently"，**"for our customer"（为我们的客户）**。
2. **只需 10 片** —— 说明不是量产缺料，更像是**维修/样机/小批量补料**。
3. **DX1518 / DX1548** 芯片型号待确认具体厂商（Alan 的回复提到 Marvell 采购审核严格，
   推测属 Marvell 体系或同类交换芯片）。
4. **结合 Angora 是 Larch 的客户（2025-08/09 挂上官网）** ——
   **这批料的"our customer"有可能是 Angora 或与其相关的项目。这是一个可以进一步验证的线索。**
5. **我方拒绝了。** 若后续 Larch 再来问，**这是一张可以打的人情牌**。

---

## 五、Saga(Alan) 向 Larch 推销过的产品（反过来也很关键）

### 5.1 2025-05-21 Managed Optical Bypass Switch（8 封往来）

> "This is a Marvell based Managed Switch with **Optical Bypass Feature**.
> 1, Customizable Web GUI
> 2, **Optical path protection in case of power failure**
> 3, 1G/2.5G/10G fiber speed, PoE is optional"

**Larch(Alexander) 回复**：
> "Thank you for sharing this — **the Optical Bypass Switch is definitely of interest to us.**
> To evaluate further, could you kindly share more technical details?"

→ **Larch 明确表示感兴趣**，并要求更多技术细节。**这条线没断。**

### 5.2 2025-11-27 Booster PoE Switch（11 封往来 —— 最长）

> "This is about our Marvell based managed switch with **power boosting feature**.
> 1, Fiber: 4*100M/1G/2.5G/10G
> 2, Copper: 8*1G RJ45/PoE, **max 240W budget**
> 3, **DC12-54V Booster to 54V**
> 4, Support **DI/DO/RS485, USB, Alarm, fiber bypass**
> 5, Customizable Web GUI"

→ 11 封往来是所有邮件里最长的，**说明谈得最深**。

### 5.3 2026-03-30 Updated Ethernet Switches Links（2026Q2 目录）

> "We updated our product links…
> 1. **8 / 24 / 48 ports L2+ / L3 managed switches**
> 2. Commercial and Industrial Ethernet/PoE for SMBs or **CCTV** solutions
> 3. **10G / 25G / 100G aggregation and core switches**
> We also provide OEM services."

附件：**Product Link_2026Q2.pdf**

→ 这正是 Larch CEO 5 月回复时提到的"你今年早些时候分享的更新链接"。

---

## 六、🎯 战略结论

| # | 结论 |
|---|---|
| 1 | **Larch 不是敌人，是潜在的合作方/渠道。** CEO 亲自发邀约，商业模式（年费授权+支持）清晰。 |
| 2 | **我方对 Larch 有筹码**：① Larch 对 Saga 的 **Optical Bypass** 明确感兴趣；② Larch **2026-07 缺芯片且被我方拒绝**；③ Saga 有 Larch 需要的 Marvell 硬件能力。 |
| 3 | **用户决策：不主动接触 Larch，只被动回应。** ✅ 已记录，遵守。 |
| 4 | **Larch 能提供的正是 Levent 要的 L3/SONiC** —— 若 Angora 通过 Larch 拿到 SONiC，我方在 L3 上彻底出局。但**硬件仍在 Scodeno/Lanaotek/SmartByte 这一族手里**。 |
| 5 | **DX1518/DX1548 芯片求购值得追查**：只需 10 片、urgent、for our customer —— 可能是 Angora 项目的补料，可侧面验证 Angora–Larch 合作的深度与进度。 |
| 6 | **Angora 的政治顾虑已被 Levent 亲口确认**（土耳其现政府更宗教化，与以色列公司合作有政治风险）→ 这既是 Larch 的弱点，也是**我方（中国供应商）的相对优势**。 |

---

## 七、待办

| # | 动作 |
|---|---|
| 1 | 读完全部 5 封的完整正文（已存 `99-raw/larch-emails/`），提取报价、型号、技术细节 |
| 2 | 确认 **DX1518/DX1548** 是哪家芯片（Marvell? Centec?），以及"our customer"是谁 |
| 3 | 确认 Alan 是否参加了 2026-06 台北 COMPUTEX 的 Larch 展位会面（booth S0905） |
| 4 | 评估：若 Larch 再次联系，**被动回应的底线与话术** |
| 5 | 交叉：Larch 求购芯片的时间（2026-07-02）与 Angora 2026 年项目节奏（TT 2026 采购周期、EGM 3,294 台）是否吻合 |

---

## 八、📌 增补（第 32 轮，2026-10-21）：Larch×Angora 合作时间线 + 官网取证

> 用户本轮显式要求挖掘「Larch 官网挂着 Angora logo，两家何时开始合作」+ 微信提过 Levent → **专项档案：`41-larch-angora-partnership-timeline-2026-10-21.md`（全量证据与 Larch 公司档案见该文件）**。本节仅存关键结论与交叉索引（只增不删）。

1. **合作起点 = 2023 年**：TTD 进口窗口下限 **2023-08**（Larch = Angora 进口前三 #2，以色列 7 票 15.56%）+ **Larch 官网 Angora logo 首现 = 2023-11**（Wayback 二分：2023-09-26 旧墙无 → 2023-11-14 新 24-logo 墙 `angora.webp` uploads/2023/11 已在线）→ 至 2026-06 Levent「a good partner」现行时确认。
2. **双向 logo 互挂**：Larch 首页墙 + /business/clients/ 页（24 客户，angora-300x150.webp）⇄ Angora 官网「Teknoloji Ortaklarımız / Наши партнеры」墙（larch 与 marvell 同列，见 `04-website-mirror/13-pages-part4-russian.md`）。
3. **Larch 公司档案（本轮官网直连）**：2009 创立（Marvell 战略合作）/ 2010 基辅办公室 / 2016 OpenROS / 2018 首推 BC3 SONiC SAI + PB 方案 / 2020 首发 400G Falcon（哈客户）/ 2021 48×25G+8×100G 2Tbps TOR（= Angora OM1/OM2 同构）/ 2022 MCLAG+PTP1588 / 2025 Ironman 模块 + FastBoot<10s；Marvell Certified SP；现推 Hardened SONiC + Dorado AI Fabric（OCP 2026-10）。
4. **微信 Larch 提及线（语料 MD 行号）**：L9347（2026-06-08 Simon 首提，Levent「Yes we know them」）/ **L9449（2026-06-11 Simon 因见 logo 而提 + Levent「a good partner」+ ⭐以色列政治问题 verbatim）** / L9555（2026-06-12 可求助选项）/ L10096+L10118（2026-08-10 SONiC 讨论，Levent 要 Sonic 样机硬件）—— 与 §六 战略结论第 4/6 条互证。
5. **产业链链位（2026-09-23 修正，未变）**：Scodeno(刘念)/SmartByte(刘情) → Larch(以色列, Marvell 硬件+软件层) → Angora(ANW)；Larch = 下游买家/伙伴，非竞对。
