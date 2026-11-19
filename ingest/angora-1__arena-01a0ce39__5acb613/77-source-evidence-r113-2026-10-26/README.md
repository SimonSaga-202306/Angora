# r113 · Angora 历史运维与跨快照证据

## 范围与日期

本轮围绕 Angora 历史支持文档中的 LLDP、语音 VLAN、系统信息、快速入门、MIB 索引及问题分类页；不联系客户或第三方，不登录设备、执行命令、下载官网 PDF 数据表或 MIB ZIP，不重新开启已 PASS 的事项。会话给定 **2026-10-26 UTC**，环境墙钟显示 **2026-11-19 UTC**；冲突未独立校准。档案捕获、网页显示日期和本轮真实采集日不能混为一谈。

## 逐源记录与边界

[来源目录](source-catalog.csv)逐条记录 URL／原路径、字节、SHA-256、来源等级和局限；[36 条本地文本锚](evidence-traceability.csv)、[17 项边界](claim-boundaries.csv)和[10 项具名增补／限定](issues-and-corrections.csv)不替代各自正文。

| 来源 | 捕获／本地文件 | bytes | 证据边界 |
|---|---|---:|---|
| AR01 | [2022 缺陷总分类](archive-replay/support.angoranetworks.com/ht_kb_category/bug/20220630221935/index.visible.md) | 2,709 | 页面显示分类计数和子分类；不是全部问题数据库或现行状态。 |
| AR02 | [2022 Verge 问题分类](archive-replay/support.angoranetworks.com/ht_kb_category/verge-angoraos/20220630214623/index.visible.md) | 3,051 | 列出 SSH／SCP 页面链接和关闭子分类计数，不写两项在 2022 是否已修复。 |
| AR03 | [2021 LLDP 指南](archive-replay/support.angoranetworks.com/ht_kb/link-katmani-kesif-protokolu-lldp/20211128053947/index.visible.md) | 12,115 | 厂商当时称出厂启用并可逐接口配置；不是现场测量或当前所有设备默认值。 |
| AR04 | [2025 LLDP 指南](archive-replay/support.angoranetworks.com/ht_kb/link-katmani-kesif-protokolu-lldp/20250211055347/index.visible.md) | 12,212 | 同一厂商同一文档的另一回放，不是独立实验。 |
| AR05 | [2025 系统信息指南](archive-replay/support.angoranetworks.com/ht_kb/sistem-bilgilerini-ogrenme/20250211062334/index.visible.md) | 7,619 | 厂商描述信息和 SNMP／NMS 读取；截图未保存，不是具体设备测量。 |
| AR06 | [2025 快速入门：遮盖回读视图](derived-redacted/AR06.safe-review.md) | 原转存 8,701；视图 8,761 | 历史文本含公开默认登录值；原转存在[来源目录](source-catalog.csv)中单列，视图遮盖两个位置、不作独立来源。未登录、未使用。 |
| AR07 | [2021 语音 VLAN 指南](archive-replay/support.angoranetworks.com/ht_kb/voice-video-ip-telephony/20210227210054/index.visible.md) | 8,511 | OUI、接口模式和 VLAN 为厂商示例；未执行命令或验证型号。 |
| AR08 | [2024 语音 VLAN 指南](archive-replay/support.angoranetworks.com/ht_kb/voice-video-ip-telephony/20241202222118/index.visible.md) | 8,496 | 同一文档另一捕获；不证明全部中间时间或当前固件。 |
| AR09 | [2025 MIB 链接索引](archive-replay/support.angoranetworks.com/ht_kb/snmp-mib-dosyalari/20250211052135/index.visible.md) | 4,415 | 仅显示 Verge MIB ZIP 链接；未下载，内容／OID／当前可用性未知。 |
| X01 | [2021 杂志单页误命中](external-visible/www.edergi.kobi-efor.com.tr/sayilar/2021/9/files/basic-html/page122.visible.md) | 8,046 | 可见页不含 Angora 名称，属于无关线索；不分析或跟进页内其他人物。 |

九份回放共 **14/14 工具块、67,829 bytes**。五个两块回放另保留各自块文件；它们是同一来源的辅助材料，不是额外证人。工具可见 Markdown 均人工转存，AR06 两处公开默认词为避免重复展示先占位再在本地恢复；**未自动与工具响应或原 HTML 逐字节比较**。没有取得网页图片、MIB ZIP、固件或任何设备实测。

## 跨快照：只比较本地保存文字

- [LLDP 比较](lldp-body-comparison-result.json)：2021 与 2025 两个已保存正文的指定区间，在仅替换 Wayback URL 时间戳后均为 **5,826 bytes**、归一化 SHA-256 相同；原始保存文件本身不同。该结果只针对两份手工转存的限定片段，不证明原始 HTML、工具输出、中间年份或实际设备完全相同。
- [语音 VLAN 比较](voice-body-comparison-result.json)：2021 与 2024 两个已保存正文的指定区间各 **3,696 bytes**，本地字节相同；同样不证明原网页／工具输出字节一致或中间状态连续。
- **增补 r112**：2022 Verge 分类页列出旧 SSH／SCP 文章链接并显示关闭子分类计数；分类页没有两篇问题的状态，不能把 r112 的 2021“待解决”无证据延伸为 2022 或当前状态。**增补 r110**：土文快速入门为不同 URL 的历史回放，不代表先前失败的英文页已恢复。

## 全量读取完成（限定清单）

**47/47 个不同路径、274,674 bytes**。其中 10 个为同源辅助分块、1 个为遮盖视图、1 个为无关杂志页，9 个为 CDX 元数据；这不是 47 个独立来源或全部来源的人工语义审核。AR06 完整源文件做全字节／UTF-8 扫描，完整遮盖视图另行显示，具体方法逐条记在清单中。

| 范围与回读清单 | 文件数 | bytes |
|---|---:|---:|
| [r110／r112 报告与元数据](prior-round-read-inventory.csv) | 10 | 76,661 |
| [旧支持来源](comparison-source-read-inventory.csv) | 5 | 35,169 |
| [r108 活动对照](prior-event-comparison-read-inventory.csv) | 2 | 24,055 |
| [CDX 索引](archive-index-read-inventory.csv) | 9 | 4,118 |
| [九份回放](archive-replay-read-inventory.csv) | 9 | 67,829 |
| [五组回放分块](archive-chunk-read-inventory.csv) | 10 | 50,035 |
| [AR06 遮盖视图](AR06-redacted-review-read-inventory.csv) | 1 | 8,761 |
| [无关杂志单页](external-read-inventory.csv) | 1 | 8,046 |

19 次预列搜索逐条执行，保存 **34 条非空结果元数据、6 个零可见结果**；搜索结果不是独立正文。9 个预列 CDX 查询按 200／HTML、摘要折叠与 `to=20261026` 过滤，共 **26 条索引记录**，其中两次为空；200 不保证正文身份，空结果不证明没有其他捕获。

[顺序和范围披露](scope-and-sequence-deviations.md)记录：九个归档 URL／目标路径虽在抓取前列出，部分分块已先读组装、所有九页曾为哈希先读，随后才建立汇总回读范围并再次完整回读；Q15 无关 PDF 结果未打开或下载。旧 r108 已区分 2022 预告日期与 KOZ'23 标签，本轮回读后继续保持，不把预告当已举办。

同一宿主机单调钟在整理中测得 **2,145.020 秒**，包括研究和思考，不证明持续键盘操作；未用睡眠凑时。[计时](timing-check.json)。未获得独立测试、当前固件配置、MIB ZIP、活动实际举办记录或工商原件，不宣称信息穷尽。

[主报告](../01-text-verbatim/workstation/08-customer-pipeline/182-angora-management-voice-evidence-r113-2026-10-26.md) · [档案附录](../01-text-verbatim/workstation/09-orders/120-angora-orders-dossier-2026-10-21.r113-appendix.md) · [字段映射](../01-text-verbatim/workstation/09-orders/120-angora-orders-master-2026-10-21.mapping-r113.md) · [审计](../79-audit-r113-2026-10-26.md)。
