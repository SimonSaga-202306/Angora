# 土耳其锚点战略备忘录：Marvell/Prestera 对标 Mikrotik 路线（2026-10-06，第 13 轮）

> 任务来源：用户第 13 轮指令③「我之前是考虑以 Angora 这个公司为土耳其市场的锚点，但他们下单确实少且慢，还有必要继续把希望放在他们身上吗？我还有其他的公司作为选择吗？要注意：我们走的是 Marvell 路线，Marvell Prestera 系列的芯片和产品规格，对标 Mikrotik。挖掘分析一下咋搞。」
> 依据：20 号（进口记录）、96 号（客户指纹）+ 第 1–12 轮全部档案 + 本轮新挖掘（ELCORE/Poyraz/PNetworks/工商变更）。

---

## 一、Angora 锚点记分卡

**利好（资产）**
1. 公共部门牌照：**EGM/KGYS 认证工业 8 口 L2+**（2019–20）+ 11 个公共/防务客户 logo（EGM/Havelsan/TCDD/TSK/MSB/Aselsan/Türksat/KGM/卫生部/Turkcell KKTC/安纳托利亚大学）
2. "yerli" 国产品牌身份 + Teknokent + 81 省经销商网络（自称）+ ELCORE 全国分销 + Club Angora 经销商运营
3. 对我方技术路线的真实认可（第 3 单 RFP 回复原话：*"It is Marvell Based IC and we develop our own software(codes). For most peer suppliers, they do Realtek, Vitesse or Broadcom"*——他们的市场叙事本身就是"Marvell+自研软件 vs Realtek 系"，与我方打法同构）
4. 安全生态：TGSK 成员、Sibereum/SyberTÜRK 真实合作、Data Diode（Arrow）+ ModBUS/OPC 产品线
5. 对接顺畅：Levent 一线决策（单独代表权至 2027-03），报价/改配置响应快

**利空（风险/事实）**
1. **15.4 个月零落单**（2025-06-19 第 6 单 6 台 → 2026-10-02 仍在谈 88 台）；期间持续询价/问项目
2. 订单规模小：样品单 ×4 + 176 台 ×1 + 6 台 ×1；在谈 88 台（¥99K ≈ $14K 量级）
3. 公司极小：~10 人（RocketReach 7–10 人），年进口 $45–70K（进口盘子里我方占有限份额）
4. **最大外部供应商是 Ewind**（竞对 HITIT 的白牌厂）——他们多源采购、不锁定，随时可被竞对体系分走份额
5. 治理变化：2024-03 起 Taylan Esen、Uğur Han Kurt 退出董事会，新主席 Hakan Oztuna（布尔萨背景）——决策圈收缩
6. 其 My Angora 门户 deal 登记门槛 ≥$10K + 强制填竞争厂商——说明其正式订单流程本就偏小偏慢

**结论（数据支撑，不替用户拍板）**：Angora 是**"公共部门 niche + 品牌叙事价值"**资产，不是**量**资产。继续做（工业口 EGM 认证单、88 台这类单成本已消化），但量级希望应转移。

## 二、替代/并行锚点候选（Marvell/Prestera 对标 Mikrotik）

| 候选 | 角色/画像 | 匹配度 | 切入话术要点 |
|---|---|---|---|
| **ELCORE**（İstanbul/Ataşehir，elcoregroup.com） | 土耳其国际化设备分销商，**11 国 VAD**；现售：**MAIPU**（中国企业网）、Sangfor、Imperum、Blackwall(BotGuard)、S3M、Supermicro、Nokia、Alcatel-Lucent、SOTI、Utimgo/Connexite 等；**同时分销 Angora**（Aykut Dalyan = Türkiye CM） | ⭐⭐⭐ 首选 | 已在土耳其分销中国网络设备（MAIPU 先例）→ 中国 Marvell 系 L2+/L3 进入组合零摩擦；多品牌共存（与 Angora 并行）不冲突；11 国分销 = 一次对接多国落地；白牌路线可完全绕开 Angora 品牌 |
| **Poyraz Network**（poyraznetwork.com） | **Mikrotik 土耳其 Master 分销商**（2015 起）+ Ubiquiti/Aqara/Mimosa/Tachyon/Cudy/**V-Sol（GPON）** 授权；另售 Cambium/Tenda/Ruijie/PN-Link/Deltalink/Wiss/Ignitenet；5000+ SKU、B2B 分销计划、当日发货、10 年+；内容营销主打酒店/宿舍"Mikrotik 性价比之王"场景 | ⭐⭐⭐ 首选 | 对标 Mikrotik 的产品就该在 Mikrotik 的量所在处卖：其渠道吃 ISP/WISP/酒店/宿舍场景（L2+/L3 edge 靶场）；已成熟销售中国系品牌（Ruijie/Tenda/V-Sol）；B2B 计划 = 分销商直接进；V-Sol 组合可做"接入交换机+GPON"整体方案 |
| **L&N Bilgisayar** | 系统集成商，与 PNetworks 签公共部门合作（2022 协议） | ⭐⭐ 补充 | 公共部门投标通道（配合 EGM 认证叙事），适合把工业口产品送进公立采购 |
| Ewind / HITIT 体系 | 竞对（其白牌）；但 Ewind 恰是 Angora 最大外部供应商 | ❌ 不做伙伴 | 竞对关系，冲突；但可作为定价参照 |
| PNetworks（PAVO 集团） | "土耳其第一台国产交换机"（2021），公共部门 | ❌ 竞对 | 同打"yerli"旗号，公共部门正面冲突；**深挖见 `110-turkey-local-competitors-deep-dive.md`**（产品线已至 100G/25G DC） |
| Keenetic Türkiye | 2026-06 新入 switch（消费/SMB 无管理为主，CEO Vefa Tarhan） | ⭐ 观察 | 短期无交集；若其向 managed 扩张再谈 |
| filteknoloji / Sonersan / Alaattin Bilişim（Angora 小经销商） | 区域小渠道 | ⭐ 备用 | 经 ELCORE/Poyraz 体系自然触达，不必单独开发 |

## 三、打法建议（双轨 + 白牌三选）

**轨道 A（保留）**：Angora = 公共部门 niche 伙伴。继续接 EGM 认证工业口小单（6/88 台这种），报价维持"成本价+材料自消化"姿态（10/3 已定 875+250），**不投销售资源等它放量**。

**轨道 B（主攻）**：Marvell 线主力渠道开发——
1. **ELCORE**（Aykut Dalyan）：带"MAIPU 先例 + Marvell Prestera 自研软件"叙事，争取进入其 11 国分销组合；
2. **Poyraz Network**：带"对标 Mikrotik hEX/Swift/CCR 场景"的产品映射表（L2+ 管理交换 / L3 edge / 工业 / PoE）+ V-Sol GPON 组合，进其 B2B 分销计划；
3. **白牌选项**（三选一，取决于用户品牌策略）：① 我方自有品牌直供 ELCORE/Poyraz；② ELCORE 系白牌（借其 11 国渠道）；③ 继续 Angora 贴牌（仅公共部门单）。
4. 辅助：L&N Bilgisayar 走公共投标（工业口 + EGM 认证背书）。

**产品弹药**（我方已有，直接可用）：
- 第 3 单 RFP 回复文档里的 Marvell 差异化三件套（自研软件 vs Realtek 被动 / 全系工业串口 / push-in 端子+EMI）
- AC3→AC5 完整（2026 回复已确认 L2+ focus、AC5 ≥5 年供货）
- 工业口 EGM/KGYS 认证型号（STI-288DGGPM 已量产供货，875 元成本价可用）
- 对标 Mikrotik 的规格映射表 = 下一步可产出的销售文档（待用户点头）

## 四、风险与未知

1. ELCORE 同时分销 Angora 与我方品牌 → 需谈**品牌边界**（建议：我方品牌 = 企业/ISP 场景，Angora = 公共"yerli"场景，避免同场竞标）
2. Poyraz 为 Mikrotik Master 分销商 → 对其主推 Mikrotik 有合同义务，我方定位必须是"补充场景/价格带"而非替换
3. 土耳其 2024–2025 通胀/汇率波动 → 报价币种与账期（30/70 T/T 老规矩）需重谈
4. ❓ 待用户确认：**郑州启扬工控**（Volza 进口行里的出口方）与我方关系（自家/上游/无关）——影响"我方在其进口盘占比"的计算
