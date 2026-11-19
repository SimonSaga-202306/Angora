# Angora 档案附录 r113：历史管理、语音 VLAN 与问题分类

> 只增补 Angora 本体公开历史文档，不创建或合并客户，不联系主体。r111 法人同一性仍为 **主体未确认**；厂商说明、示例和目录不是现场验收。

## 1. 历史管理和语音功能

- [2021 LLDP 回放](../../../77-source-evidence-r113-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/link-katmani-kesif-protokolu-lldp/20211128053947/index.visible.md#L37-L51)与[2025 回放](../../../77-source-evidence-r113-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/link-katmani-kesif-protokolu-lldp/20250211055347/index.visible.md#L37-L51)均写出厂启用，描述邻居拓扑发现和逐接口配置。**增补 r110**，不证明现行型号／固件、现场配置或漏洞；两个回放是同一厂商同一文章，不是独立测试。
- [2021 语音 VLAN 回放](../../../77-source-evidence-r113-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/voice-video-ip-telephony/20210227210054/index.visible.md#L39-L101)描述 OUI、语音／数据 VLAN 和 `general` 接口模式，且对其电话加 PC 示例限定 access／trunk。该约束只记录为历史示例，不推广为所有平台标准或现场操作建议；没有执行命令。
- [系统信息页](../../../77-source-evidence-r113-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/sistem-bilgilerini-ogrenme/20250211062334/index.visible.md#L37-L79)称 AngoraNMS 或其他平台可通过 SNMP 读取信息，描述镜像与 CPU 时间窗；[MIB 页](../../../77-source-evidence-r113-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/snmp-mib-dosyalari/20250211052135/index.visible.md#L43-L45)只是 ZIP 链接。未下载 ZIP、未验证 OID、SNMP 版本或设备数值。
- [快速入门遮盖视图](../../../77-source-evidence-r113-2026-10-26/derived-redacted/AR06.safe-review.md#L47-L53)对公开历史默认登录值做了两处遮盖，原独立人工转存另存；页面写指定位置管理接口尚未启用、仅用于诊断，但未明确具体 SKU／版本。**增补 r110 入门资料可见性**：这是不同 URL 的土文历史页，不代表 r110 未取得的英文页或当前站点已恢复。没有使用登录值。

## 2. 问题状态与时间：具名限定

- **增补并限定 r112 SSH／SCP 问题**：[2022 分类页](../../../77-source-evidence-r113-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb_category/verge-angoraos/20220630214623/index.visible.md#L37-L51)列出两篇问题链接及一个关闭子分类计数，未显示两篇在 2022 的状态；r112 的 2021“待解决”和计划版本不得延伸为 2022／当前仍未修复，也不说明计划版本已发布。蓝灯页的 2021“已解决”不自动对应分类计数中的某一条。
- **继续保留 r110 CLI 编号差异**：新 LLDP／语音示例不消除旧通式与例子的中间段差异，不执行命令，也不推断具体设备。
- **继续限定 r108 KOZ 日期**：旧媒体预告显示 2022 日期与 KOZ'23 标签，但 r108 已指出不能证明实际举办日期；本轮没有新的独立活动证据，不将同一预告算作新证人。
- 两组跨快照比较只针对保存的局部文本：[LLDP 归一化比较](../../../77-source-evidence-r113-2026-10-26/lldp-body-comparison-result.json)／[语音页原字节比较](../../../77-source-evidence-r113-2026-10-26/voice-body-comparison-result.json)，不能证明远端原件或中间时期相同。

## 3. 完整读取与范围

**全量读取完成（限定清单）：47/47 路径、274,674 bytes**，其中包含 CDX、重复分块、遮盖视图和无关杂志单页，不是 47 个独立来源。[逐项路径、大小与哈希](../../../77-source-evidence-r113-2026-10-26/README.md) · [36 个原文锚](../../../77-source-evidence-r113-2026-10-26/evidence-traceability.csv)。

九个归档 URL／目标路径事前列出，但块级清单在首块返回后建立；本地分块及九页曾先读作组装／哈希，再列汇总范围并完整回读，已在[偏差记录](../../../77-source-evidence-r113-2026-10-26/scope-and-sequence-deviations.md)披露。工具转存不是原 HTML；Q15 无关 PDF 搜索结果未打开或下载。没有重开旧单、财务差异、RFQ/RFP、报价、官网 PDF、已停端口澄清或其他 PASS 事项。
