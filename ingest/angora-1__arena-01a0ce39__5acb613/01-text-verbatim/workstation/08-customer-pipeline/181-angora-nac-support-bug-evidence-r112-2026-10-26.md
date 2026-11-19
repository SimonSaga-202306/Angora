# Angora 深挖 r112：历史认证、问题记录与公开配置样例

> **结论先看**：新增四份可回放的历史厂商支持页面，并从其中一页找到七份公开 FreeRADIUS 样例原文件。2021 年问题页记录了 SSH 卡顿和特定 SCP 传输导致重启的**历史待修复状态**，但没有证据证明这些问题今天仍存在或计划版本已发布。样例日志也不是本轮设备实测。
>
> 会话给定日期 **2026-10-26 UTC**，环境时钟显示 **2026-11-19 UTC**，冲突未独立校准。归档捕获日期、Git 提交日期、会话日期和实际采集日期不可混用。[r111 日期纠正](../../../69-source-evidence-r111-2026-10-26/time-and-provenance-correction.md)。

[来源目录与证据级别](../../../73-source-evidence-r112-2026-10-26/source-catalog.csv) · [43 个原文锚](../../../73-source-evidence-r112-2026-10-26/evidence-traceability.csv) · [18 项边界](../../../73-source-evidence-r112-2026-10-26/claim-boundaries.csv) · [11 项具名增补／限定](../../../73-source-evidence-r112-2026-10-26/issues-and-corrections.csv) · [完整回读](../../../73-source-evidence-r112-2026-10-26/README.md) · [档案附录](../09-orders/120-angora-orders-dossier-2026-10-21.r112-appendix.md) · [映射](../09-orders/120-angora-orders-master-2026-10-21.mapping-r112.md)。

## 1. 802.1X：历史厂商指南与公开示例

[AR01：2022-01-18 的厂商知识库回放](../../../73-source-evidence-r112-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/802-1x-port-based-authentication-using-freeradius/20220118064213/index.visible.md#L39-L53) 描述通过 FreeRADIUS 进行终端网络接入认证，称 **Verge 运行 5.0 及以上**支持 802.1X，并列 PEAP、EAP-TLS、EAP-GTC 等类型。示例使用 PEAP 和认证服务器本地用户；**目录服务集成明确不在该文示例范围内**。文档还说可配置多个 RADIUS 服务器并设优先级，但所展示的基础示例只用一个。`NET-SCOPE`、`NET-EAP-CLAIM`、`NET-PEAP`、`NET-DIRECTORY`、`NET-SERVERS`。

这是历史厂商文档的文字，不是本轮对设备的测试、当前版本兼容表或证书。示例输出里的重认证状态只是**示例输出**，不能反推所有设备默认值。802.1X 主要涉及终端接入；r110 的 [TACACS 管理认证](../../../65-source-evidence-r110-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/tacacs-authentication-with-cisco-ise/20210227205859/index.visible.md#L47) 是不同功能，英文文档的“大于 4.0”和本次“5.0 及以上”**不能合并成统一版本门槛**。r110 土文版本边界差异仍保留。

## 2. 直接找到七份原始配置文件

AR01 链接的 [GitHub 示例目录](../../../73-source-evidence-r112-2026-10-26/github-files-scope-before-fetch.csv)共七个文件，逐一保存原相对路径和文件名，合计 **91,709 bytes**；逐文件验证 Git blob SHA-1 和大小，另记 SHA-256。固定提交 `7876ce42bafac38ada3c5ccca7df861ed33b63e9` 的目录与本轮读取的当前目录 7/7 路径／大小／blob 一致；Git API 给出的提交时间字段为 2020-01-16。不能据此证明 2022 年归档时该仓库分支恰好指向该提交，或证明任何实际部署。[逐文件清单](../../../73-source-evidence-r112-2026-10-26/github-files-read-inventory.csv) · [固定提交比较](../../../73-source-evidence-r112-2026-10-26/github-pinning-comparison.json)。

- [样例 README](../../../73-source-evidence-r112-2026-10-26/github-raw/github.com/anwHub/3rdPartyConfigs/freeRadiusConfigs/README.md#L1) 明称是配置样例。[`eap` 文件](../../../73-source-evidence-r112-2026-10-26/github-raw/github.com/anwHub/3rdPartyConfigs/freeRadiusConfigs/eap#L14-L27)的活动字段列外层 PEAP；[PEAP 段](../../../73-source-evidence-r112-2026-10-26/github-raw/github.com/anwHub/3rdPartyConfigs/freeRadiusConfigs/eap#L750-L769)列内层 MSCHAPv2。它们是**仓库文本**，不是经过我们运行、适用于所有版本或可直接部署的配置。`CFG-README`、`CFG-OUTER`、`CFG-PEAP-BLOCK`、`CFG-INNER`。
- [示例日志](../../../73-source-evidence-r112-2026-10-26/github-raw/github.com/anwHub/3rdPartyConfigs/freeRadiusConfigs/freeRadius_AccessAccept_Succesfull_log.txt#L252)含 `Access-Accept` 字样；来源、设备、服务器和客户环境未独立验证，不能把作者提供的日志当现场验收或安全认证。原文件按公开原字节保留，可能含示例账号／密钥及旧预览链接；报告不摘录这些值，本轮不使用、不登录、不运行。
- **增补 r110 GH03 的零结果边界**：r110 当时的 [GitHub 查询计划](../../../65-source-evidence-r110-2026-10-26/github-discovery-plan-before-search.csv)和[响应](../../../65-source-evidence-r110-2026-10-26/github-api-GH03.json)分别保存了支持域名搜索及零命中。本轮通过历史页面直接找到的 README 含同一域名，说明旧零结果**不能证明不存在相关公开材料**。这不证明当时查询返回错误，也不猜测索引原因；r110 原有限定保持。`OLD-GH03-QUERY`、`OLD-GH03-ZERO`、`NET-REPO`、`CFG-URL`。

## 3. 三项 2021 历史问题：分清状态与计划

| 历史记录及捕获时间 | 厂商当时写的现象与版本 | 页面状态 | 不能推出 |
|---|---|---|---|
| [SSH 卡顿](../../../73-source-evidence-r112-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/ssh-baglantilarinda-donma/20210227205239/index.visible.md#L38-L46)，2021-02-27 | 快速重复回车或粘贴多行时出现卡顿／延迟；页面说连接并未断开；版本族 `5.5.1.x`、`5.5.3.x`。 | 已识别、**等待解决**；字段列计划版本 `5.5.1.17`、`5.5.3.10`。 | 这些版本已发布、当前仍有问题、所有型号受影响或存在可利用漏洞。 |
| [SCP 文件传输](../../../73-source-evidence-r112-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/scp-kullaniminda-hata-olusmasi/20210227215720/index.visible.md#L38-L46)，2021-02-27 | 页面称向远端服务器通过 SCP 发送文件时可能软件报错并重启；同样列上述两个版本族。 | 已识别、**等待解决**；同样列上述计划版本。 | 本轮已复现、客户发生过重启或现在仍未修复。 |
| [蓝色工作灯](../../../73-source-evidence-r112-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/guc-isiginin-yanmamasi/20210227223458/index.visible.md#L39-L47)，2021-02-27 | 表示软件开始加载的蓝灯不亮；页面写 `5.5.1.13` 及更早。 | 状态写**已解决**；另一字段仍叫“计划修复版本”，列 `5.5.1.14`、`5.5.3.7`。 | 已独立验证对应版本发布、所有硬件都受影响，或原因一定是供电硬件。 |

两项待修复问题页面曾建议临时改用 TFTP；那是**历史厂商建议**，不是本轮对生产网络的操作建议。未评估传输安全、维护窗口、当前版本或现场风险，也未执行任何命令。r110 的[升级示例](../../../65-source-evidence-r110-2026-10-26/archive-replay/support.angoranetworks.com/ht_kb/software-upgrade-tftp-verge/20250211051945/index.visible.md#L81)包含一个镜像文件名；**限定 r110**：示例名称不是现场设备版本，不能与本轮计划修复字段相减后推断实际受影响或已修复。`SSH-*`、`SCP-*`、`LED-*`、`OLD-UP-SAMPLE`。

## 4. Packet Broker 与培训索引：只记录来源的边界

[厂商 Packet Broker 文章](../../../73-source-evidence-r112-2026-10-26/external-visible/www.angoranetworks.com/gorunurluk-guvenlik-maliyet-packet-broker/index.visible.md#L19-L65)解释了流量分类、过滤、串联和旁路监测等一般概念；文章谈到流量规模的例子、无丢包和较快回收投资，但没有给出可核验的测试方法、具体型号负载条件或客户回报数据。**不把这些通用说法当特定 SKU 实测吞吐、零丢包或 ROI 承诺**。`PB-DESCRIPTION`、`PB-EXAMPLE`、`PB-FILTER`、`PB-INLINE`、`PB-ROI`。

本轮取得的 [培训分类索引](../../../73-source-evidence-r112-2026-10-26/external-visible/www.angoranetworks.com/events/category/egitim/index.visible.md) 展示 r111 的两个 2023 年活动摘要，**增补 r109 E03 当轮失败**；动态索引原本就是摘要，不能替代 r111 两个独立活动页，也不证明活动已办、到场人数或全部历史。

## 5. 失败、范围与完整回读

[X01 访谈](../../../73-source-evidence-r112-2026-10-26/fetch-failures/X01.visible.md)出现脚本污染与 401 类页面模式漂移；[X02 视频](../../../73-source-evidence-r112-2026-10-26/fetch-failures/X02.visible.md)第三块变成无关推荐、总块数改变。均未得到完整文本，局部块隔离、**不作事实来源**，r109 对旧视频流程的谨慎边界继续有效。三个支持站直连是 522，但四个历史回放分别取得正文；不把单次错误当永久停站。

**全量读取完成（限定清单）：58/58 个不同路径、355,715 bytes**，具体路径、大小、哈希和读取方法见[来源说明](../../../73-source-evidence-r112-2026-10-26/README.md)。其中包含 API／CDX 元数据、失败记录、四个隔离视频局部块及四个同源重复分块；七份公开 GitHub 原文件完整解码逐行扫描；README 的公开旧预览链接曾在工具回读中显示但未访问，报告不摘录示例值。58 不是 58 个独立来源，也不是对每份文件进行人工安全审计。另有 3 份安全元数据全量解析和 32 份保护副本仅哈希。

本轮对照的一份 r104 网页混有已停端口相关字段和数据表链接，范围选择过宽，已披露；该页不用于本轮结论，没有打开 PDF 或追问停项。视频、手抄和 API／分块顺序的限制见[偏差记录](../../../73-source-evidence-r112-2026-10-26/scope-and-sequence-deviations.md)。未主动联系任何主体、登录会议或设备、下载官网 PDF 数据表，也没有新增 Ewind 事实或改变既有对手分类。

同一宿主机单调计时在整理中测得已过 **2,689.667 秒**，含研究、整理与思考，不证明持续键盘操作；未用睡眠凑时。[计时记录](../../../73-source-evidence-r112-2026-10-26/timing-check.json)。当前版本状态、真实缺陷修复、独立认证和客户履约仍缺证据，不宣称全量商业信息已穷尽。
