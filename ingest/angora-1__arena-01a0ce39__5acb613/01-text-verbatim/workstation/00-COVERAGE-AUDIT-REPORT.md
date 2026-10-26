# 🔍 入库完整性审计 · 结案报告
> 审计日期：2026-09-23　·　审计脚本：`workstation/99-raw/audit_coverage.py`（可重跑）
> 审计目标：确认仓库里**每一份原始素材的内容**与**每一条研究结论**都已进入知识库，无遗漏。

---

## 0. 结论

**审计前：文件都推了，但内容大面积没入库。**
**审计后：4 类主要缺口已全部补上（新增 150 份 MD/JSON），其余经逐项验证为误报或无内容素材。**

| 方法 | 审计前 | 审计后 |
|---|---|---|
| A. 孤儿原始素材 | 6 个 | 0 个（3 个误报已排除，2 个为纯设计稿） |
| **内容级抽查（xlsx）** | **5 份关键表格内容缺失** | ✅ 已入库 |
| **内容级抽查（docx）** | **0 / 23 份入库** ❌ | ✅ **23 / 23** |
| **内容级抽查（PDF）** | **0 / 39 份入库** ❌ | ✅ **39 / 39**（含 2 份扫描件 OCR） |
| **内容级抽查（xls 商业单据）** | **0 / 75 份入库** ❌ | ✅ **75 / 75** |
| B. 关键词覆盖 | 31/31 | 31/31 |
| C. 产物一致性 | OK | OK |

---

## 1. 补入库的内容（本轮新增）

| 类别 | 数量 | 位置 | 关键收获 |
|---|---:|---|---|
| **PDF** | **39** | `01-knowledge-base/pdfs/` | SmartByte 2025 目录（46 页 / 98K 字符）、两份 ANW-VERGE-2023 TR 数据表、ANW DC RFP、TT RFP、IoT 原理图、警察局项目三个规格包 |
| **docx** | **23** | `01-knowledge-base/docx/` | ⭐ **2026-08-17 Saga 官方 L3 战略回复**、微信会议议程（2024/2025）、`加深关系绑定` 中文策略、RFP 往来、CLI/User/Web 手册 |
| **xls/xlsx 商业单据** | **75** | `01-knowledge-base/commercial-docs/` | 报价单、形式发票、装箱单、采购合同；蒸馏出**交易主体总表** |
| **结构化表格** | **8** | `01-knowledge-base/spreadsheets/` | 土耳其客户名单 60 条、Saga 7.5.x L2+ 146 项、7.3.0 功能清单 125 项、TT 测试项、PVC 库存、BOM 等 |
| **扫描件 OCR** | **2** | `01-knowledge-base/pdfs/` | 土耳其贸易登记公报（2024-03-11）、Levent 护照（PII 已标注） |
| **RAR 目录** | 1（15 条目） | `pdfs/info-rar-inventory.*` | 暴露 5 份未知 CENTEC PPTX |
| **俄文官网镜像** | 1 | `04-website-mirror/13-pages-part4-russian.md` | VERGE 规格总表、IRIS SFP 全 SKU、两篇新闻稿、客户墙 |

---

## 2. ⭐ 审计过程中挖到的新事实（此前完全不在库里）

### 2.1 官方芯片与 L3 路线（2026-08-17）
`Reply on SAGA Enterprise L3 Recommendation Report.docx`：
- **AC3 → AC5 切换已完成**，`lite-hotfix-7.3.13` 是最后一个 AC3 版本，AC5 锁定 **至少 5 年**
- 技术资源全部投向 **L2+**；对多数 L3 机型 **"let it be"（放任）态度**
- ⭐ **"Saga has already fixed its chipset solutions on Marvell L2+ and CENTEC L3, this is a strategic move"**
- **近 6 个月 RAM/DDR 与 PCB 板价格飙升**，影响经营现金流 ← 成本压力的第 4 条独立佐证
→ 印证用户口述的芯片代际真相；我的 DX1500"代际差距"警告**二次确认作废**

### 2.2 能力缺口被坐实
- `Saga Feature List_7.5.x_L2+` 的 IP Route **只有静态路由**
- `Saga Software Function List 7.3.0` **有完整** RIP / OSPFv2 / BGP4 / ECMP / VRRP
- 而 Angora 官网俄文页 **对外标称 Enterprise = L2/L2+/L3、DC/TOR = 高级 L3 路由（VRF/MPLS/BGP6/L3VPN）**
→ **对外宣传与我方实际交付之间存在明确缺口**，这是 Levent 2026-08-30 提问的真正背景

### 2.3 联系人补全
- **Taylan 全名 = Mehmet Taylan ESEN**（`tesen@angoranetworks.com`）
- Levent 两个邮箱；Angora 电话 **+90 312 241 77 47**；安卡拉收货地址
- **TRONX Bilişim** 为另一买家（Mustafa Çalık）
- 土耳其贸易登记公报：Levent Kılıç 任董事长/董事至 **2027-03-09**；**Hakan Öztuna** 董事长至 2027-03-07；**Taylan Esen 与 Uğur Han Kurt 原董事职务终止**（⚠️ 公报可见主体为 SADUN İNŞAAT / 尚勒乌尔法登记处，归属待核，已在文件中标注）

### 2.4 俄文站带来的新情报
- 客户墙含 **TSK（武装部队）+ MSB（国防部）** → 与军品交换机机会同脉络
- **IRIS SFP 全 SKU**：`ANW-SFP-1G-LX` 正是 2026 招标中 Karen 报价 25 元的那款（1G LX 单模 10 km）
- **Cisco ISE 集成**（2021-06-21）：可平替 Cisco 接入层，**无需改动现有 ISE 配置**
- Data Diode 支持 ModBUS/OPC，目标行业**明列"军事行动"**
- **DC/TOR 机型**：3.6 Tbps、6×100G QSFP28

### 2.5 内部中文策略文档 `加深关系绑定.docx`
- **已申请里拉（LIRA）收款账户** ← 对应招标中的换汇痛点
- 拟在**伊斯坦布尔设 office + 小型 warehouse**，作**进军欧洲的跳板**（紧邻保加利亚）
- 原文论断：**"目前国内同行没人全线做 Marvell 芯片，独有的优势"** ← 第三次印证芯片代际真相

---

## 3. 经逐项验证**排除**的项目（不是遗漏）

| 项目 | 验证结论 |
|---|---|
| `Black/White TRONX.psd` | 纯 logo 设计稿，**无文本层、无可提取内容**；TRONX 业务信息已在 `commercial-docs/` 中充分覆盖 |
| `RFP/2024.5.27_RFP.xlsx` | ✅ 已入库 `commercial-docs/rfp-2024-5-27-rfp-xlsx.md`（审计脚本文件名匹配过弱导致误报） |
| `RFP/2024.6.15_TT-RFP-EN.pdf` | ✅ 已入库 `pdfs/rfp-2024-6-15-tt-rfp-en-pdf.md`（误报） |
| `IoT Board/SC0012-000.pdf` | ✅ 已入库 `pdfs/iot-board-sc0012-000-pdf.md` |
| `INFO_2025.12.17/ANW-DC-RFP-EN.pdf` | ✅ 已入库 `pdfs/info-2025-12-17-anw-dc-rfp-en-pdf.md` |
| `ANGORA LOGO2.ai` 等设计源文件 | 矢量 logo，无业务文本内容 |

---

## 4. ⚠️ 确认无法在本环境完成（需本地处理）

| 项目 | 原因 | 处理建议 |
|---|---|---|
| **`INFO_2025.12.17/INFO.rar`（51 MB，RAR 5.0）** | 沙箱无 root，`unrar` 二进制缺失，`unrar-cffi` 编译失败；`libarchive` / `bsdtar` / `7z` 均不可用 | 本地执行 `unrar x INFO.rar`。**目录清单已完整读取并存盘** |
| ├ `Performance of PeakNetX Platform_EN.pptx` (97 KB) | ⚠️ **CENTEC 平台** | 与 CENTEC L3 战略直接相关，建议优先 |
| ├ `Performance of VastLakes Platform_EN.pptx` (105 KB) | ⚠️ **CENTEC 平台** | 同上 |
| ├ `Saga Software Function List_EN.pptx` (154 KB) | Saga 软件功能清单（PPT 版） | |
| ├ `STH1G Series Switches Datasheet_EN.pptx` (9.0 MB) | STH1G 系列数据表 | |
| └ `STH25G Series Switches Datasheet_EN.pptx` (4.9 MB) | STH25G 系列数据表 | |
| **新域名 `angorateknoloji.com` 全站** | 根域 fetch 失败、子页一律 404（Cloudflare 限流），多路径多次尝试均失败 | **建议放弃**；已确认旧域名 RU/EN/TR 三语可用，信息等价 |
| `/download/425/`、`/428/`、`/485/`、`/488/`、`/491/` 等数据表 PDF | 需直接下载二进制，抓取工具只取文本 | 可本地下载后放入仓库再入库 |
| 官网评论区 | reCAPTCHA 阻断 | 无价值，跳过 |

---

## 5. 审计方法说明（可复现）
`workstation/99-raw/audit_coverage.py` 提供三种**互相独立**的检查：
- **A 孤儿检测**：原始素材文件名是否出现在任何 workstation `.md`（⚠️ 弱信号，会产生误报，需人工复核）
- **B 关键词覆盖**：31 个已知业务事实关键词是否在全库出现（强信号）
- **C 产物一致性**：`md` 消息条数 vs `json` 条目数、OCR 文件数 vs 源图数、2026 子集 vs 全集（强信号）

本轮另外使用了**内容级抽查**（从文件内抽取特征句，回查知识库），这是发现 docx/PDF/xls 大面积缺口的**关键方法**——
仅靠文件名匹配会全部误判为"已覆盖"。
