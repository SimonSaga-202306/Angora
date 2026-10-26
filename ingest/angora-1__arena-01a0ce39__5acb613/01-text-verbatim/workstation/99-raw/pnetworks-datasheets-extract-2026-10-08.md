# 99-raw · PNetworks datasheets 解析 + EKAP 中标扫描 + ensun 补全（第 15 轮，2026-10-08）

> 任务来源：用户第 15 轮指令「都搞了」= 执行第 14 轮遗留的 3 条线索：
> ① pnetworks.com.tr 官网 31 项 datasheets 清单逐份解析；② rehbersanayi.com EKAP 中标归档检索 PnetWorks/Ewind/Angora 中标记录；③ ensun.io Top 14 缺失的第 11–14 家名称补全。
> 方法：官网 PDF 链接经 fetch_page 解析（PDF→markdown，单页 datasheet 基本在 chunk 0 完整）；rehbersanayi 为 EKAP 每日结果的第三方镜像（HTML 可直接抓取，绕开了 EKAP 官方 JS 应用死角）；ensun 经 web_search 摘要恢复。
> 本文件为原始落库；结构化结论已同步进 `06-competitors/110-turkey-local-competitors-{deep-dive.md,csv,xlsx}`（规则 5）。

---

## 一、PNetworks datasheets 解析（10/31 项成功，2 项死链，其余未抓）

### 1.1 解析成功的 10 份（pnetworks.com.tr/storage/app/media/… .pdf）

| 型号 | 定位 | 端口 | 性能 | 工业/电源 | 关键特性 | 备注（原文问题） |
|---|---|---|---|---|---|---|
| PN-TMS24QSFP4QSFP+ | **DC 交换机（25G/40G）** | 24×1/10/25G SFP+ + 4×40G QSFP+ | **1.86Tbps**，8 个硬件队列，4GB RAM，128K MAC | 0/+50°C，IP53，1U，6.2kg | G.8032 环网（<50ms/25 节点）+ IEEE 1588v2/Sync-E 硬件；**L3 可选**（BGP/OSPFv3/PIM）；802.1x/RADIUS/NAC/CoA；USB3 配置/升级 | 企业/DC 混合定位 |
| PN-TMS48SFP+6QSFP+ | **DC 骨干交换机/路由**（原文自称 "backbone switch/router"） | 48×SFP+ + 6×40/100G QSFP+ | **3.6Tbps L2+L3 线速** | 2×450W 热插拔电源，0/+50°C IP20，8kg | +**TWAMP**（ISP 性能测量） | 已具备 100G 骨干能力 |
| PN-CMS8GE2CG（±PoE+ 变体） | 工业 8 口边缘 | 8×GE + 2×1G SFP/Combo | 20Gbps | **−40/+70°C IP53**，12VDC（PoE 版 48–54VDC），DIN 导轨，1040g | PoE：30W/口，**预算 240W**，可选 PoE++ 60W；IEC 61850-3 | 与 CMS8GE4SFP 同壳 |
| PN-CMS8GE4SFP | 工业 8 口边缘 | 8×GE + 4×1G SFP | 24Gbps | 同上壳型 | — | — |
| PN-CMS24GE4SFP+（±PoE 变体） | 企业/工业 24 口 | 24×GE + 4×10G SFP+ | 128Gbps，**95.24Mpps**（原文印成 "95 Mbps" = 笔误） | 1U，3kg | PoE 版预算 **500W** | **TTK 招标 spec 疑似来源**（见 1.3） |
| PN-LMS24GE4SFP+ | 同壳 L 系列 | 24×GE + 4×10G SFP+ | 同 CMS24 | 2465g | — | C/L 系列差异化不明（产品线扩张痕迹） |
| PN-CMS48GE6SFP+（PoE+） | 企业 48 口 | 48×1GE + 6×10G SFP+ | ⚠️ 原文印 52Gbps（**复制 24 口表错误**） | −40/+70°C IP53 | PoE 30W/口、预算 240W（可选 PoE++ 60W）；IEC 61850-3；TWAMP | **模板复制错误实锤**（见 1.4） |
| PN-NMS | **Web 网管系统**（©2021） | — | — | 最低要求 50GB 存储/24GB 内存/4 核 | SNMP/NETCONF/**SDN-OpenFlow**/NetFlow；LLDP 自动发现+拓扑映射；**ZTP 零接触部署**+固件集中管理；RADIUS/TACACS+；**按设备许可（per-device licensing）**；FCAPS 全模块；LDAP/AD；HTTP API | **独立软件产品 = 全栈信号** |
| PN-SFP MODULE | **自产光模块** | PN_S1…PN_S8：1G LX SMF 1310nm 20km / 1G ZX 1550nm 80km / 10G SX·LX / 1G 850nm MMF 0.5km 等 | — | — | SFF-8472 DDM 可选 | **自产 SFP = 全栈信号** |

### 1.2 死链（404，勿重试）
- `PN-AC1`（WiFi 系列 datasheet）→ 404
- `pn-cms48ge4sfp.pdf`（CMS48 非 PoE 版）→ 404（PoE+ 版可用）

### 1.3 关键交叉发现
- **TTK 假设（待核）**：CMS24GE4SFP+ 规格表 "95.24 Mpps"（原文误印 95 Mbps）≈ TTK 2025-12-25 招标（30 台 managed switch）的规格口径 → PNetworks 产品规格疑似**按土耳其国铁招标参数定制**（或反之，招标按市场主流参数写）。方向与因果均待核，但两者数值吻合度异常高。
- **Trabzon 假设（强相关）**：Trabzon Büyükşehir 2026-08-05 İKN 2026/1272126（61saat.com）：1 台 omurga（骨干）+ 20 台 kenar（边缘）switch + **1 套 ağ yönetim yazılımı（网管软件）** + 50 AP，**yalnızca yerli istekliler（仅本土供应商可投）** → "switch + NMS 软件 + AP 打包 + 本土限定" 与 PNetworks 全栈（TMS 骨干 + CMS 边缘 + PN-NMS）+ PN-AC 无线线**完全对口**，是其理想客户画像。

### 1.4 QA 信号（可用于竞争叙事）
- CMS48GE6SFP+ PoE+ 页：转发速率 52Gbps（应为 48GE 的 96Gbps 量级）+ 端口表是 24 口版本 = **整表从 24 口 sheet 复制未改**
- 多份 datasheet 正文出现**错误型号名**（如 A 型号页写 B 型号）
- 解读：产品线 2021→2026 从 1 款扩到 31 项 datasheets，文档质量跟不上扩张速度 → 早期 OEM/白牌起家的常见痕迹，与其"PNetworks 实体仅 3 人（RocketReach）+ 集团背书"互相印证

### 1.5 实体信息修正
- PNetworks 官网 About：**成立于 2019**（Teknopark İstanbul）；RocketReach 实体员工数 **3 人**（PAVO 集团 600+）
- 与 110 档案"品牌 2021 首发"不矛盾：2019 注册 → 2021 出首发 switch。CSV 成立列保留"集团2003年；PNetworks品牌2021"，备注补 2019 注册。

### 1.6 未抓部分（本轮边界）
31 项清单中本轮成功解析 10 份 + 2 份死链；其余 ≈19 份（含 WiFi 全系列、部分企业款、optics 扩展）未逐份抓取 → 列为下轮可选线索，优先级低（核心规格轮廓已足够）。

---

## 二、rehbersanayi EKAP 中标扫描（首次打通 EKAP 数据死角）

### 2.1 数据源
- `rehbersanayi.com/veri/ihale-sonuclari`：EKAP 每日结果镜像。**2026-06-30 → 2026-10-06 共 27,412 项中标，总预算 1,118.6M TL；38% 的中标 ≤2 家投标（低竞争）**
- `rehbersanayi.com/ihale/arsiv/sektor/bilisim-ve-yazilim-teknolojileri`：IT 行业归档 **547 项 / 10 页**（每页最多 20 条 × 最多 4 chunk）

### 2.2 扫描范围与结果（如实声明边界）
- 本轮实际扫描：**IT 归档第 1–6 页 × chunk 0 ≈ 120/547 条**（按时间倒序，≈ 2026 年 9–10 月最新段）
- 检索词：PnetWorks / PNetworks / PAVO / Ewind / Angora / yerli switch
- **结果：0 命中**（无一家作为中标方出现；Ewind 作为"被采购品牌"也未在最近段出现）
- 解读：不构成"无中标"证明（仅覆盖 ≈22% 且为最新段），但结合"官网无任何参考客户 logo、L&N 渠道为主"，**PNetworks 的中标量级不大、渠道窄** 的判断与第 14 轮一致
- 下轮线索（低优先级）：抓完 10 页 × 4 chunk 做全量 547 条扫描

### 2.3 同期市场信号（本轮顺带捕获）
| 日期 | 机构 | 内容 | 金额 (TL) | 投标数 |
|---|---|---|---|---|
| 2026-09-15 | **İSTTELKOM** | 服务器 + **ağ anahtarı（交换机）** + 备份系统 | **244.6M** | **1 家** |
| 2026-09/10 | Bingöl（医院系统） | IT 设备 | 45M | — |
| 2026 近期 | Dugan（icra 执行局） | 笔记本 | 292.5M | — |
- 市场结构信号：**大额 switch 采购单一投标常态**（244.6M TL 仅 1 家投标）→ 关系型市场，品牌矩阵 ≠ 中标量，渠道人脉是变量

---

## 三、ensun Top 14 补全（部分成功）

- **第 11 位 = Provider**（Pendik，成立 2018，11–50 人）：区域科技集团，系统集成 / IoT / 大数据 / 云（另见 ensun 系统集成 Top 41 榜）
- 第 12–14 位：**无法恢复**（原页 chunk 边界截断 4 个标题，二次抓取与搜索均无果）→ 维持第 14 轮数据边界声明，不重试
- 14 家中真正"本土 switch 硬件制造商"仍 ≈ 1 家（PNetworks）+ 2 家小型集成商，第 14 轮结论不变

---

## 四、来源清单（本轮）
1. pnetworks.com.tr 官网 10 份 datasheet PDF（fetch_page 解析，2026-10-08）
2. pnetworks.com.tr About 页（成立 2019）+ RocketReach（3 人）
3. rehbersanayi.com/veri/ihale-sonuclari（市场统计页）
4. rehbersanayi.com/ihale/arsiv/sektor/bilisim-ve-yazilim-teknolojileri 第 1–6 页
5. 61saat.com（Trabzon İKN 2026/1272126，经 web_search 摘要）
6. imzagazetesi（TTK 2025-12-25 30 台 managed switch，经 web_search 摘要）
7. ensun.io Provider 条目（经 web_search 摘要）
