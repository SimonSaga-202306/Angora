# 121 · Angora 全量重头分析（统一时间线 + 27 轮信息整合 + 2.5 年关系全画像）

- 日期：2026-10-21（第 28 轮）
- 触发：用户「基本上所有关于 Angora 的信息都给你了（wechat Talk、订单、相关文件）。你再看看时间戳，应该是从 2024 年开始沟通的。统一理解一下这些信息，然后再重头分析一下 Angora」
- 本轮执行：① Drive WeChat Talk 26 张长截图**逐张视觉核对**（顶/尾裁剪识别）② 各信源时间戳锚点核对 ③ 全库信息统一 ④ 重头分析
- 信源全集：微信语料 2,601 轮（2024-05-02 16:36→2026-10-03 00:40）/ Gmail 159 封（2024-09-18→2025-08-29）/ Drive 订单链 9+1 单（r27 120 号档案）/ 官网镜像 / 社媒 10+ 平台 / 进口数据 45+21 票 / TT 关系档案 / 投标档案 / 竞对 110 三件套 / 客户管线 111 三件套 / 27 轮全部 raw

> **⚠️ r30 状态更新（2026-10-21，只增不删）**：① **88 台（第 10 笔）= 已终止**（2026-10-08 13:03 Levent 原话：partner 因交期改主意、转投土耳其本地现货 cryptoink.com.tr）——本文「在手 88 台 104,720 RMB」「风险 #1 88 台未落纸面」「机会 O1 88 台 10 月内关单」等表述以本注为准（详情见 `123-angora-88-dead-levent-tt-background-2026-10-21.md`）② 新增语料 63 轮（10/8 段，语料 2,601→2,664）③ Levent TT 背景考证 = Cisco 的 Turk Telekom 战略客户经理 15 年+（非 TT 员工）。

---

## §1 ⭐ 时间戳统一核对（用户指令第 1 项）

| 信源 | 起点 | 终点 | 证据 |
|---|---|---|---|
| **微信（Levent KILIÇ 会话）** | **2024-05-02 16:36** | 2026-10-03 00:40 | 本轮截图 #1 首行 =「**2024-5-2 16:36 You have added Levent KILIÇ as your Weixin contact. Start chatting!**」→「hi, Levent, How are you?」→ Levent 16:45「Hi Simon, great.. Thanks. Here may be much quicker to chat for small stuff.」 |
| Gmail | 2024-09-18 | 2025-08-29 | gmail-threads.json 159 封 min/max |
| 订单（STSC 合同） | 2024-05-08（1st 首单） | 2025-07-11（7th）+ **2026-10-02（88 台预期单）** | 120 号档案 |
| 商业登记 | 2024-03-11（TICARET SICIL） | — | 根夹 PDF（2024-03-09 股东大会：Hakan Oztuna 新主席，地址迁 Camlıca） |
| 公司成立 | **2016** | — | 40-angora-company-full-history |

**结论（对用户问题的直接回答）**：✅ 与 Angora/Saga 的商业沟通**始于 2024-05-02 16:36**（微信加好友当天首条消息），6 天后（2024-05-08）即下首单。**2.5 年关系，微信 = 日常沟通主通道（Levent 原话：「Here may be much quicker to chat for small stuff」）**。

### 1.1 WeChat Talk 26 张截图核对结果（本轮）
- 25 张（摄于 2026-09-23 22:34:55→22:52:51）= **同一会话（Levent KILIÇ）的完整长截图平铺**：第 1 张起点 = 会话最顶部（2024-5-2 16:36），第 25 张终点 = 会话最底部（**8/30 Sunday 21:03**「understood」+ 输入框可见），中间 23 张逐张首尾相接（已抽验 9 张顶部：5-2 / 5-27 / 8-6 / 9-17 / 10-22 / 10-30 / 11-8 / 11-27 / 2025-1-8，跳跃均 < 窗口长度 = 有重叠）
- 1 张（摄于 2026-10-06 17:25:57）= **88 台订单段**（10/2 19:56→10/3 00:40）
- **与现有语料对平：26/26 张 = 0 条新消息**。88 台段已在库（r13 第 26 张图「877 图」OCR，`wechat-conversation-aligned.md` L10300-10326）；25 张覆盖区间 = 语料全区间（2,601 轮）的视觉副本
- 副产物：25 张长截图（合计 58MB）已核验后**删除**（最小存储原则），转录证据 = 本文 §1 + 120 号档案 §7.6 注

### 1.2 2024-2026 关键时间戳锚点（截图 + 语料 + 订单三方对平）
| 日期 | 事件 | 信源 |
|---|---|---|
| 2024-05-02 16:36 | 微信建立（首条消息） | 截图#1 + 语料 |
| 2024-05-08/09 | **1st 首单** 4 台样品（$1,265） | 订单 + 语料 |
| 2024-05-27 | 首个产品需求：「If **STC-424XGGM** could be an equivalent of your existing model (or even better)?」→ Levent「Absolutely👍」 | 截图#2 |
| 2024-08-06 | **首次 L3 请求**：「can you pls check if this supports **Layer 3** features? How we can verify」（3124-TX）→ Simon 列 L3 功能（ARP/ECMP/VRRP/RIP/OSPF/BGP4/IS-IS） | 截图#3 |
| 2024-09-17 | 假期期间问题处理（「You are traveling on your festival time」） | 截图#4 |
| 2024-10-22 | **2nd 单收款** + PVC 面贴/MAC/包装确认（「production will be arranged now」） | 截图#5 |
| 2024-10-23 | Levent 与 Taylan 开车去 **Saha Expo（Istanbul）** | 截图#5 |
| 2024-10-30 | **OEM 定位对话**：「we basically do neutral devices, which means we prefer to do OEM for clients」 | 截图#6 |
| 2024-11-08 | Angora 向 Simon 提供的**客户名单群发 EoY Offer**（Levent 原话） | 截图#7 |
| 2024-12-02 | **产能预警**：「There are too many orders coming in, our production dept are now evaluating leadtime for the FINALIZED and POTENTIAL bulk orders」+ **WiFi6 AP 中立/贴牌二选一**（后落 TronX 单） | 截图#8 |
| 2025-01-08 | 3rd 单物流筹备（176/8=22 cartons × 20kg = 440kg） | 截图#9 |
| 2025-02-03 | TT 测试（ANW-1108-V 样品，型号 TT-2208-TG） | RFP_2025.1.30 |
| 2025-06-13/23 | 6th 单 TT-2208-PG ×6（TT Logo）出货 | 订单 |
| 2025-07-11 | 7th 单 TT-2208-PG ×10（MAC 登记） | MAC 表 |
| 2026-02-12 | EGM 3,294 台批准（Mehmet ÇATAL） | KGYS.txt |
| 2026-07-20 | 加深关系绑定方案（Lira/伊斯坦布仓/co-branding） | 120 §7.4 |
| 2026-07-31 | **LK 发起 SAGA L3 建议报告**（TT 2026 tender 需求） | 120 §7.3 |
| 2026-08-17 | Simon 官方回复（**CENTEC L3 全有 / AC3 冻结 7.3.13**） | 01-kb/2026-08-17 |
| 2026-08-30 20:58 | Levent：「TT asks about **48-port industrial**」（语料末条 21:03） | 语料 + 截图#25 |
| **（静默 5 周）** | | |
| 2026-10-02 19:56 | Levent：「We expect an order for **88 pieces of L2+ industrial 8-port together with 48V power supply**...pricing for this in the same box」 | 截图#26 + 语料 L10300 |
| 2026-10-03 00:19 | Simon 报价：**STI-288DGGPM 875 RMB/PC + 240W Meanwell 48V 电源 250 RMB/PC**（「keep the price low, same as last order / we will handle the material costs here / same packing box」+ 寄 angora 包装箱照片） | 截图#26 + 语料 |
| 2026-10-03 00:40 | Levent：「Thanks Simon. Great.👍」（语料全库末条） | 截图#26 + 语料 |

---

## §2 统一理解：Angora 是什么（实体画像）

### 2.1 公司
- **Angora Networks Bilişim A.Ş.**（2016 成立；Ankara → 2024-03 迁 **Camlıca（Ankara Yenimahalle 区**，⚠️ 非伊斯坦布尔——r29 据官网 contact 页 + SICIL 登记更正**）**；Ziraat Çayyolu IBAN TR09 0001 0019 8997 0378 9850 02）
- 2024-03-09 股东大会：**Hakan Oztuna 任新主席**，Taylan Esen / Uğur Han Kurt 辞任 → 股权结构变动（2024-03-11 SICIL 登记）
- 定位：**"yerli"（本土）品牌** = 中国 ODM（我方/Ewind/Larch/NEM 等）贴 Angora 标 + 本土 GUI/多语言/本地服务（国产化率自述 68%/76%，KOZ'23）
- 规模：100+ SKU（自有目录）/ 2,000+ 在网设备（KOZ'23 口径）/ 6 人核心团队可见（KOZ'23 组织架构 6 名字）+ **GM Levent Kilic（LK = 我方全部对接人）**
- 产品线：商用 L2/L3（ANW-3xxx 系）+ 工业（ANW-2xxx/TT-2xxx 系）+ **IoT 模块（SC0012，Drive IoT Board 夹）** + 软件（GUI 多语言、ZTP、sFlow 等）
- 渠道/客户：TT（运营商贴牌）/ **EGM 警察局（3,294 台）** / TronX（姊妹公司）/ ELCORE 分销 / filteknoloji 独家（某线）/ 55+ 土耳其 prospects（Client List 2026-07-25）/ 自有 My Angora 伙伴门户（商机登记 ≥$10K 门槛）
- 展会：Saha Expo（2024-10，Istanbul）/ IASF / KOZ 峰会（2023）

### 2.2 人（关系结构）
| 人 | 角色 | 与我们的关系 |
|---|---|---|
| **Levent Kilic（LK）** | Angora GM | ⭐ 唯一直接对接人（微信 2,601 轮）；2026-07-31 主动发起 L3 报告 = 战略级参与；护照在我方（PII，仅索引） |
| Taylan Esen | 前董事（2024-03 辞任）→ Saha Expo 随行 | 次级联系人（无微信账号，2024-10-30 确认） |
| Hakan Oztuna | 新主席（2024-03 起） | 决策层（未见直接互动） |
| Karen LEE | NEM Engine（光模块）关联 | 工业模块温度测试（-40/+75°C 照） |
| Mustafa Calik | **TronX**（姊妹公司） | Unpaid-1 单 $1,480（未付款 PASSED） |
| Mehmet ÇATAL | EGM | 3,294 台批准人 |
| Simon Cheng / Peter Hu | 我方 | Simon = 商务全权；Peter = 上级（SmartByte） |

---

## §3 关系全史：2024-05 → 2026-10（重头梳理）

### 3.1 四阶段
1. **样板期（2024-05~10）**：5-2 加微信 → 5-8 首单 4 台样品（$1,265，含 L3 3424/3448）→ 5-27 STC-424XGGM 需求确认 → 8-6 首次 L3 验证请求 → 10-22 2nd 单收款（8×2116-PG+2×1108-V，$2,345）→ 10-30 **OEM 中立定位确立**（「we prefer to do OEM for clients」）。特征：小单快反，验证互信；微信 = 日常通道。
2. **放量期（2024-11~2025-03）**：11-8 Angora 反向运营（向我们的客户名单群发 EoY offer = 把我们也当渠道用）→ 12-2 产能预警（「too many orders coming in」）+ AP 中立/贴牌（→ TronX $1,480 单）→ **2025-01-17 3rd 单 178 台（$47,174，最大单：5% 折扣 / RMA 2% / 30-20-50 付款 / 4 周生产 / 包装定制 / ANW-PWR-48-240 定制电源）**→ 2025-03-02 出货（440kg/22 箱）。特征：从样品到量产主渠道。
3. **通道期（2025-04~2025-12）**：4th-pre（9,110 RMB 未出货）/ 4th 样品 3+3 台（2025-05-07）/ 5th 13 台 **Angora+TronX 双品牌**（2025-05-28）/ **6th TT-2208-PG ×6（Turk Telekom Logo，2025-06-23）= 白牌进运营商体系** / 7th TT ×10（2025-07-11，MAC 池 A5:00:00~A5:05:FF 预留 2,048）/ INFO_2025.12.17 = **CENTEC L3 方案包已备好**（VastLakes/PeakNetX/STH 系）。特征：产品贴牌化 + 运营商通道打开 + L3 技术储备。
4. **战略期（2026-01~10）**：EGM 3,294 台批准（02-12）/ RAM+PCB 涨价压现金流（08-17 自述）/ **07-31 LK 主动发起 SAGA L3 建议报告**（TT 2026 tender：stacking/USB/OOB/dual-PSU/OSPF/BGP/VRF；市场价 $1,000-2,500 vs 我方街价 $340/530）→ **08-17 官方回复：AC3 冻结（7.3.13 末版）+ 「Saga 锁定 Marvell L2+ + CENTEC L3」**/ 07-20 加深关系绑定方案（Lira 付款 / 伊斯坦布 office+仓 / VMI / co-branding「Saga Telecom & Angora Networks」）/ 08-30 TT 问 48 口工业 → **（静默 5 周）→ 10-02 88 台 L2+ 工业 8 口 + 48V 电源预期单**（875+250 RMB，「same as last order」= 承接 2024-11 TronX 单 STI-288DGGPM 价位 $125 ≈ 890 RMB，我方吸收材料涨价）。特征：关系从贸易升级**共创**（路线图 / business plan / 战略绑定）。

### 3.2 沟通机制
- 微信 = 日常（2,601 轮，左 Levent / 右 Simon，25/25 张归因一致）；Gmail = 正式单据（159 封）；WeChat meeting = 定期议程（2024.10.31 + 2025 两份 agenda docx）；决策闭环快（Levent 21:03 问 → 00:19 答 → 00:40 确认）

---

## §4 经济账（统一后全口径）

| 项 | 数字 |
|---|---|
| 已成交 6 单收款 | **57,194 USD**（成本 338,314.62 RMB → 414,103.74 RMB） |
| 已成交利润 | **75,789.12 RMB（加权 18.3%）** |
| 最大单 | 3rd 178 台 $47,174（15.9%，大单折扣+UPS 空运） |
| 未了结 1 | 4th-pre 9,110 RMB 未出货单 |
| 未了结 2 | TronX $1,480 未付款（PASSED，仅登记） |
| **在手 88 台（2026-10-02 报价）** | 88 × (875 + 250) = **104,720 RMB ≈ $14,646**（若按 TT 通道 30% 运费加收 + 5% 折扣外，毛利预期 18-25%）= **单笔已超 4th/5th/6th 之和** |
| MAC 池 | A5 段 2,048 地址（已用 41，余 2,000+ = TT 通道放量信号） |
| 定价行为 | STI-288DGGPM 875 RMB（2024-11 价位 $125）2026-10 不变 + 电源 250 = **我方吸收 RAM/PCB 涨价**（「we will handle the material costs here」）= 以价换量换绑定 |
| 付款行为 | 6/6 单按期（30-20-50 实际 30/70）；唯一坏账 = TronX $1,480（姊妹公司，2024-11 至今） |

**重头结论**：Angora 已从「小单客户」变成**我方土耳其市场最大单一收入来源 + 唯一运营商/政府贴牌通道**。88 台若落地 = 2026 年首单且体量接近 6th+7th 之和。

---

## §5 产品与技术线（统一理解）

1. **L2+ 是基本盘**（AC3 Marvell，7.3.13 冻结）：ANW-2116-PG（178 台主力）/ 2224/2248-PX（AC5 防爆）/ TT-2208-PG（TT 通道）/ STI-288DGGPM（工业 8 口，TronX→88 台）
2. **L3 需求线 = 2024-08 起持续 2 年**：2024-08-06 首次验证请求 → 3rd 单 L2+（TT 当时只要 L2+）→ 2026-07-31 L3 报告（TT 2026 tender 要 L3 全套）→ 08-17 回复 = **CENTEC L3（STH1G/STH25G，功能全有）= 我方 L3 唯一路线**；L3 市场价 $1,000-2,500 vs 我方 L2+ 街价 $340/530 = **2-5 倍溢价空间**
3. **工业线扩张中**：8/30「TT asks about 48-port industrial」+ 10-02 88×8 口 L2+ 工业 + 48V 系统（TT-2208-PG 也是 DC44-57V = **48V 电信级供电体系 = TT 机房/局端特征**）→ 工业 8 口→48 口产品线是下一个放量点
4. **EGM 3,294 台规格 vs 现有产品**：野外 8GE+2SFP 70km -40~60°C IP20 DIN 全口 PoE ≈ **STI/TT-2208 平台改型**（70km = 光口 10G-LR 级）；室内 24GE+4SFP 56Gbps ≈ 2224-PX 平台；**C-Type 测试报告 = 强制门槛**（Karen 的 -40/+75°C 测试照 = 测试进行中侧证）
5. **TT-2116-PG.zip（3rd 单夹）**= 16 口 PoE 贴 TT 标预研 → TT 通道从 8 口向 16 口扩
6. **软件**：7.3.0 清单（MAC 16k/ERPS 20ms/静态 256-768/ACL 240-480/sFlow）+ ZTP（Angora 自有）+ 多语言 GUI = 「Marvell 无同行全线」护城河（2026-07-20 绑定文档原话）

---

## §6 竞争位势（我方视角）

- **对 Angora 自身**：我方 = 其「 yerli 叙事」的 L2+ 主力货源（Marvell AC3/AC5 独家 + 现货 + 830 RMB 级成本）；Ewind = 其另一大货源（印度海关 35 票）+ 我方直接竞对（同 Shenzhen 系、同白牌打法）；PNetworks = 其本土竞对（Edgecore 白牌，全栈但 3 人轻实体）；Longline = 零售侧（entegron 第 2 品牌）
- **对我方**：Angora 渠道价值 = ① 土耳其市场准入（yerli 身份 = 标单资格）② TT/EGM 政企通道（白牌贴牌）③ 数据回流（其 Client List 55+ 家 = 土耳其市场情报源；2024-11-08 反向群发 = 双边渠道化）
- **风险对冲**：双轨战略（97 号档案：Angora = 公共 niche 锚点 / ELCORE+Poyraz = 主力）仍有效；Angora 对我方依赖度（L2+ 全线 + 贴牌通道）> 我方对 Angora 依赖度（单一大客户），但 57k USD 年体量下仍须防集中

---

## §7 风险清单（重头评估）

| # | 风险 | 证据 | 等级 | 对策 |
|---|---|---|---|---|
| 1 | **88 台单未落纸面**（仅微信预期+报价，无 STSC 合同/PO） | 10-02/10-03 语料 | 中高 | 本周内催 PO + 定金（30% 惯例）；「same as last order」价位 10-10 前有效 |
| 2 | TronX $1,480 坏账（2024-11 起 22 个月） | Unpaid-1 夹 | 低（金额小）| 维持 PASSED：登记不催（用户指令） |
| 3 | 4th-pre 9,110 RMB 未出货单 fate 不明 | Unshipped 夹 | 低中 | 向用户确认（是否已私下处理） |
| 4 | AC3 冻结 → L2+ 新功能（如 48 口工业 L3）必须走 CENTEC = 交付周期风险 | 08-17 回复 | 中 | CENTEC STH1G 样机先行（120 §7.7 方案包已备） |
| 5 | RAM/PCB 涨价 vs 我方吸价（875 不变） | 08-17 + 10-03 | 中 | 单量补偿（88→200+）或电源/配件补差 |
| 6 | Levent 单点依赖（唯一对接人；其个人 = 关系载体） | 全语料 | 中 | 已推进 co-branding/VMI/伊斯坦布仓 = 组织化绑定（07-20 方案） |
| 7 | Angora 多头货源（Ewind/Larch/NEM）= 份额被分 | r13 进口 45 票 15 供应商 | 中 | Marvell 代差 + 现货 + 贴牌通道独占性（TT/EGM 仅我方） |
| 8 | 5 周静默（8/30→10/02）= 决策节奏不确定性 | 语料空窗 | 低 | 10-06 截图 = 用户方已掌握最新状态；保持 48h 响应惯例 |
| 9 | TT 自采可能绕过 Angora（TT 2026 tender 若直招 OEM） | L3 报告 | 中 | 加深绑定方案（co-branding = 让 Angora 成为 TT 的「yerli 集成商」而非转包商） |
| 10 | 我方产能（12-2024 已现「too many orders」预警） | 截图#8 | 低 | 88 台 + EGM 备料需提前锁 SmartByte 产能 |

---

## §8 机会清单（重头评估，按价值排序）

1. **⭐ 88 台 L2+ 工业 8 口 + 48V 电源（在手，≈$14.6K）**：10 月内关单；48V 体系指向 TT 局端项目 → 关单时顺带确认终端 = TT/EGM（影响后续 48 口工业开发）
2. **⭐ TT 48 口工业（8/30 Levent 原话）**：TT 明确询问 = 需求真实；48 口 L2+ 工业 PoE（-40~70°C DIN）= 我方 STH/STC 平台可覆盖 → **10-15 前出规格+报价**（抢 Ewind 同型：Ewind 36 口 800W 工业已有，48 口工业位空档 = 时间窗）
3. **⭐ EGM 3,294 台（C-Type 测试门槛）**：KGYS/ÇGKS 规格原文已入库；Karen -40/+75°C 测试进行中 → **主动提供 C-Type 测试支持 + 70km 光口方案**；若中标 = 我方年出货 +3,294 台（= 3rd 单 18.5 倍）
4. **CENTEC L3（STH1G/STH25G）→ TT 2026 tender（$1,000-2,500 价区）**：08-17 已承诺「功能全有」→ **11 月前送 STH1G 样机 + L3 演示**（LK 在等结果；business plan 级对话已开）
5. **加深绑定三件套落地**（Lira 付款 / 伊斯坦布仓 / co-branding）：2026-07-20 方案已出 → 选 1 项先落地（建议伊斯坦布仓 = 缩短 TT 交付 + 库存前置）
6. **TT-2116-PG（16 口 PoE 贴 TT 标）**：3rd 单夹 zip = 预研材料已备 → 随 88 台单一起推
7. **Angora Client List 55+ 家 = 反向渠道**：2024-11-08 反向群发先例 → 约定季度联合客户开发（我们出 111 管线优质 23 家清单 × 其本地服务）

---

## §9 综合重判（从头分析结论）

1. **Angora = 我方土耳其战略锚点客户（A 级）**：2.5 年 6 单 57k USD + 在手 88 台 + TT/EGM 双政企管线 + 反向渠道价值；关系阶段已从「贸易」进入「**共创**」（LK 主动发起 L3 路线图对话、business plan 级互参、绑定方案上桌）
2. **时间轴验证**：沟通 2024-05-02 起（用户判断 ✅）；2.5 年内完成「加好友→首单→最大单→白牌通道→战略绑定」全跃迁，节奏 = **每 6-8 个月一个台阶**（2024H1 样板 / 2024Q4 放量 / 2025H1 通道 / 2026H1 战略）
3. **下一个台阶（2026Q4-2027H1）的三个可能**：① 88 台→TT 48 口工业→TT 2026 tender L3（CENTEC）= 运营商主线走通 ② EGM 3,294 台中标 = 政府主线走通 ③ co-branding/VMI 落地 = 组织化绑定完成。**三条线任一兑现 = Angora 年采购破 100 台量级向千台量级跃迁**
4. **对我方的硬约束**：AC3 冻结 + RAM/PCB 涨价 = 利润端承压（875 吸价）；CENTEC L3 交付能力 = 战略兑现的**唯一技术风险**（样品 + C-Type 测试双门槛）
5. **与双轨战略的兼容**：Angora 通道 = 公共/政企 niche（不与 ELCORE+Poyraz 主力渠道抢零售），维持 97 号档案双轨不变；Angora 的 55+ Client List = 主力渠道的土耳其本地化入口
6. **一句话重判**：**Angora 不是一个客户，是我方进入土耳其政企市场的「yerli 牌照」+「TT/EGM 白牌通道」+「2,048 地址 MAC 池预留的量产期权」——88 台是这份期权的行权第一步。**

---

## §10 边界声明

1. WeChat Talk 26 张 = 0 新消息（全量对平语料）；本档 §1.2 引文 = 本轮截图视觉转录 + 语料回验一致
2. 88 台单 = 微信预期 + 报价，**非合同**（无 STSC 号）；金额 104,720 RMB 为报价口径
3. 「TT 48 口工业」与「88 台」的终端归属（TT vs EGM vs 其他）= 推测（48V 体系 + 时序），待 88 台关单时确认
4. EGM 3,294 台 = RFP 规格 + 批准记录，**中标结果未出**；C-Type 测试进度无直接证据（Karen 照片 = 侧证）
5. 5 周静默（8/30→10/02）期间无其他渠道（Gmail/WeChat）记录 = 真实空窗
6. 本档引用 120 号档案（订单/文件索引）与 27 轮前序档案；冲突时以本档 §1 时间戳表为准（本轮实测）
