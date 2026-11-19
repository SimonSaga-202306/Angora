# Angora 深挖 r113：历史网络管理、语音 VLAN 与问题索引

> **结论先看**：新增九份历史厂商支持页／分类页回放。2021 与 2025 的 LLDP 文档都写出厂默认开启；2021 与 2024 的语音 VLAN 文档给出 OUI 和接口模式示例。这些都是**历史文档声明，不是当前型号实测或客户部署**。2022 问题分类页仍列出 r112 的两篇问题文章，但没有给出当时的修复状态。
>
> 会话给定日期为 **2026-10-26 UTC**，环境时钟显示 **2026-11-19 UTC**，冲突未独立校准；档案捕获日期不是本轮真实采集日。[既有日期说明](../../../69-source-evidence-r111-2026-10-26/time-and-provenance-correction.md)。

[来源目录](../../../77-source-evidence-r113-2026-10-26/source-catalog.csv) · [36 条原文锚](../../../77-source-evidence-r113-2026-10-26/evidence-traceability.csv) · [17 项边界](../../../77-source-evidence-r113-2026-10-26/claim-boundaries.csv) · [10 项具名增补／限定](../../../77-source-evidence-r113-2026-10-26/issues-and-corrections.csv) · [完整回读](../../../77-source-evidence-r113-2026-10-26/README.md) · [档案附录](../09-orders/120-angora-orders-dossier-2026-10-21.r113-appendix.md) · [映射](../09-orders/120-angora-orders-master-2026-10-21.mapping-r113.md)。

## 1. LLDP：厂商历史默认值，不是现场配置

[2021 回放](../../../77-source-evidence-r113-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/link-katmani-kesif-protokolu-lldp/20211128053947/index.visible.md#L37-L51)及[2025 回放](../../../77-source-evidence-r113-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/link-katmani-kesif-protokolu-lldp/20250211055347/index.visible.md#L37-L51)均称 LLDP 已加入 AngoraOS、**出厂设置中开启**；文本还描述邻居发现、管理平台拓扑发现及逐接口配置。例子展示的计时和邻居表是文档示例，不是本轮采集的设备状态。`LLDP-DEFAULT-21`、`LLDP-DEFAULT-25`、`LLDP-TOPOLOGY`、`LLDP-PER-INTERFACE`。

本轮分别保存两个回放；[限定正文比较](../../../77-source-evidence-r113-2026-10-26/lldp-body-comparison-result.json)只在本地手工转存中替换 Wayback URL 时间戳后比较，选定片段相同。不能由此证明原始网页字节一致、2021—2025 全时期不变、当前型号默认值或安全漏洞。**增补 r110** 的历史管理文档范围，不取代其 CLI 编号及版本适用性警示。

## 2. 语音 VLAN：示例所需条件，不能泛化为全系列规则

[2021 文档](../../../77-source-evidence-r113-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/voice-video-ip-telephony/20210227210054/index.visible.md#L39-L101)描述 IP 电话和连接其后的 PC 分离语音／数据流量；该示例使用电话厂商 OUI 表、语音 VLAN 和 **general** 接口模式，并称该场景下 access 或 trunk 不能同时承载所述电话与 PC 流量。这里是**厂商文档中的特定示例**，不是所有设备、所有语音 VLAN 实现的通用限制，也不是可直接用于生产的配置建议。`VOICE-SCOPE-21`、`VOICE-OUI`、`VOICE-MODE`、`VOICE-VLAN-EXAMPLE`。

[2024 回放](../../../77-source-evidence-r113-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/voice-video-ip-telephony/20241202222118/index.visible.md#L39-L101)的本地转存中，选定正文与 2021 转存的对应区间按字节相同；这不证明工具原响应、原 HTML 或中间版本一致，也不是两次独立测试。[比较记录](../../../77-source-evidence-r113-2026-10-26/voice-body-comparison-result.json)。

## 3. 管理接口、系统信息和 MIB：保留未验证范围

- [系统信息指南](../../../77-source-evidence-r113-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/sistem-bilgilerini-ogrenme/20250211062334/index.visible.md#L37-L79)称设备状态可由 AngoraNMS 或其他平台通过 SNMP 读取，描述模型／运行时间／温度、活动与非活动镜像、多个 CPU 平均时间窗。它提供的是厂商说明与截图链接；我们没有读取截图或设备，也不能由它推出具体 OID、SNMPv3 兼容性或唯一故障原因。`SYS-SNMP`、`SYS-IMAGE`、`SYS-CPU-INTERVALS`、`SYS-HIGH-CPU`。
- [快速入门安全回读视图](../../../77-source-evidence-r113-2026-10-26/derived-redacted/AR06.safe-review.md#L47-L53)保留原文其余内容并遮盖两处公开历史默认登录值。页面称特定位置的 `YONETIM` 管理接口“尚未启用、只用于诊断”；**型号和软件版本未明确**，不能推广到所有设备或现在。页面还写有新设备默认登录说明，但我们没有使用该值、登录设备或判断现行凭据。`QUICK-OOB`、`QUICK-DEFAULT-MENTION`。
- [MIB 索引](../../../77-source-evidence-r113-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/snmp-mib-dosyalari/20250211052135/index.visible.md#L43-L45)列出 Verge MIB 的 ZIP 链接；本轮**未下载该 ZIP**，不知道里面有哪些 OID、版本或现在是否可获取。r110 的 DHCP／TFTP ZTP 说明和 CLI 编号差异仍按原边界保留。

## 4. 2022 问题分类：出现链接不等于尚未修复

[2022 Verge 问题分类页](../../../77-source-evidence-r113-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb_category/verge-angoraos/20220630214623/index.visible.md#L37-L51)列出 SSH 和 SCP 两篇文章，并显示一个“已关闭问题”子分类计数。分类页**没有写出这两篇在 2022 年的修复状态**，也没有列清所有子分类成员；不能把 r112 的 2021“等待解决”延伸成 2022 或当前仍未解决。`CAT-SCP-LINK`、`CAT-SSH-LINK`、`CAT-CLOSED-COUNT`。旧版问题与计划修复字段仍见 [r112](181-angora-nac-support-bug-evidence-r112-2026-10-26.md)。

## 5. 业务线索、回读及空白

Q08 命中的 2021 杂志单页实际是无关任职信息，不含 Angora 名称；已完整保存并排除，不跟进页内人物。回读 [r108 KOZ 预告](../../../57-source-evidence-r108-2026-10-26/external-visible/ictmedia.com.tr/haber/angora-networks-kanal-ortaklari-zirvede-bulusuyor/index.tr.extracted.md#L9-L13)：页面显示 2022 年日期、文字使用 KOZ'23 标签和未来时；r108 已把它限定为**预告而非已举办证据**，本轮没有新证据改变该判断。

**全量读取完成（限定清单）：47/47 个不同路径、274,674 bytes**，包括九个 CDX 元数据文件、十个同源辅助分块、一个遮盖回读视图及一个无关单页，不是 47 个独立来源。[路径、字节、哈希和方法](../../../77-source-evidence-r113-2026-10-26/README.md)。九份回放的 14/14 工具块均保存为人工转存，但没有自动与工具响应或原 HTML 逐字比较。

九个归档 URL／目标路径在抓取前已列；分块计数须等首块返回，五组块先读后组装，九个本地回放在汇总范围清单前也曾为哈希读取，之后才完整回读。Q15 返回无关 PDF 搜索结果，未打开或下载；详见[顺序与范围披露](../../../77-source-evidence-r113-2026-10-26/scope-and-sequence-deviations.md)。未主动联系主体、登录或操作设备、下载官网 PDF／MIB ZIP；没有新增 Ewind 事实或改变用户已有对手分类。

同一宿主机单调钟在整理中测得 **2,145.020 秒**，含研究与思考，不证明持续键盘操作；未用睡眠凑时。[计时](../../../77-source-evidence-r113-2026-10-26/timing-check.json)。当前型号、固件、独立测试、MIB 内容、实际举办情况及工商主体仍有空白，不宣称穷尽。
