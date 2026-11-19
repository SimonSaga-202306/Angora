# r112 · Angora 历史认证、问题页和公开示例配置

## 范围与日期

本轮重点是 Angora 本体的历史 802.1X 支持、厂商问题记录及其公开示例配置；辅以 Packet Broker 通用说明和培训活动索引。会话给定 **2026-10-26 UTC**，环境墙钟显示 **2026-11-19 UTC**，冲突未独立校准，不能把目录名或墙钟倒填为旧网页真实采集日。归档时间是 Wayback 捕获字段，不是首次发表或本轮真实日历采集日。

## 新的逐源记录

[完整来源目录](source-catalog.csv)逐条记录路径、字节、SHA-256、来源类型和边界；[43 个本地原文锚](evidence-traceability.csv)、[18 条声明边界](claim-boundaries.csv)、[11 项具名增补／限定](issues-and-corrections.csv)均不替代正文。

| 编号 | 单独产物 | bytes | 可使用的范围 |
|---|---|---:|---|
| AR01 | [2022 归档：802.1X / FreeRADIUS](archive-replay/support.angoranetworks.com/ht_kb/802-1x-port-based-authentication-using-freeradius/20220118064213/index.visible.md) | 9,637 | 历史厂商指南自述 Verge 5.0 及以上；示例 PEAP，目录服务集成不在范围内。不是现场测试或当前全系列规格。 |
| AR02 | [2021 归档：SSH 卡顿](archive-replay/support.angoranetworks.com/ht_kb/ssh-baglantilarinda-donma/20210227205239/index.visible.md) | 4,402 | 历史页面列两个版本族、当时待解决及计划版本；不证明当前状态。 |
| AR03 | [2021 归档：SCP 文件传输](archive-replay/support.angoranetworks.com/ht_kb/scp-kullaniminda-hata-olusmasi/20210227215720/index.visible.md) | 4,193 | 历史厂商描述特定传输导致错误重启、当时待解决；没有操作设备。 |
| AR04 | [2021 归档：蓝色工作指示灯](archive-replay/support.angoranetworks.com/ht_kb/guc-isiginin-yanmamasi/20210227223458/index.visible.md) | 3,694 | 记载 `5.5.1.13` 及以前，状态写已解决，但字段仍叫计划修复版本；未独立验证版本发布。 |
| X06 | [厂商 Packet Broker 通用文章](external-visible/www.angoranetworks.com/gorunurluk-guvenlik-maliyet-packet-broker/index.visible.md) | 16,203 | 说明过滤与部署概念；场景流量、零损耗和投资回报表述不是具体 SKU 实测或保证。 |
| X07 | [厂商培训目录](external-visible/www.angoranetworks.com/events/category/egitim/index.visible.md) | 855 | 页面本身是动态摘要，仅显示两个条目；不是完整活动史或实到证据，与 r111 的活动页不是独立事件。 |
| X01／X02 | [访谈失败](fetch-failures/X01.visible.md)／[视频分块漂移](fetch-failures/X02.visible.md) | 1,288／1,438 | 两次都没有取得可用全文；局部块隔离，不用于结论。 |
| X03–X05 | [802.1X 直连错误](fetch-failures/X03.visible.md) · [SSH 直连错误](fetch-failures/X04.visible.md) · [快速指南直连错误](fetch-failures/X05.visible.md) | 1,186／1,186／1,187 | 页面本身是 Cloudflare 522，不是目标正文；不证明永久不可达。 |

六份成功页面／回放共 **8/8 工具块、38,984 bytes**；X06 和 AR01 各两块，其他四份各一块。X06／AR01 的同源分块另存并按断点组装，分块不是额外来源；块级清单在首块显示后建立，分块先读后纳入汇总，已披露。工具可见 Markdown 由人工转存，未自动与工具响应逐字比较；无原 HTML、图像、固件或独立设备测试。

## 公开 GitHub 示例：逐文件原路径和原始字节

AR01 的正文链接 [公开示例仓库](https://github.com/anwHub/3rdPartyConfigs/tree/7876ce42bafac38ada3c5ccca7df861ed33b63e9/freeRadiusConfigs)。先取得完整目录清单，再逐项以 GitHub blob API 获取 **7/7 文件、91,709 bytes**，各保留原相对路径与原文件名，没有合并。解码后大小与目录字段和 Git blob SHA-1 全部一致，另逐项记 SHA-256；与网页的手工转存不是同一种证据形态。[事前文件清单](github-files-scope-before-fetch.csv) · [回读清单](github-files-read-inventory.csv) · [固定提交比较](github-pinning-comparison.json)。

| 原文件 | bytes | 已保存原始路径 |
|---|---:|---|
| `README.md` | 280 | [原文件](github-raw/github.com/anwHub/3rdPartyConfigs/freeRadiusConfigs/README.md) |
| `clients.conf` | 7,678 | [原文件](github-raw/github.com/anwHub/3rdPartyConfigs/freeRadiusConfigs/clients.conf) |
| `eap` | 27,771 | [原文件](github-raw/github.com/anwHub/3rdPartyConfigs/freeRadiusConfigs/eap) |
| `freeRadius_AccessAccept_Succesfull_log.txt` | 14,833 | [原文件](github-raw/github.com/anwHub/3rdPartyConfigs/freeRadiusConfigs/freeRadius_AccessAccept_Succesfull_log.txt) |
| `mschap` | 6,973 | [原文件](github-raw/github.com/anwHub/3rdPartyConfigs/freeRadiusConfigs/mschap) |
| `radiusd.conf` | 27,091 | [原文件](github-raw/github.com/anwHub/3rdPartyConfigs/freeRadiusConfigs/radiusd.conf) |
| `users` | 7,083 | [原文件](github-raw/github.com/anwHub/3rdPartyConfigs/freeRadiusConfigs/users) |

以上是公开**样例**，可能含示例账号、IP、共享密钥或旧预览链接；原字节完整保留以便审计，报告不复制这些值、不使用它们、不连接任何服务。七文件完整解码并逐行扫描；README 的公开旧预览链接曾在工具回读中显示但未访问，报告不摘录示例值；不是人工逐行安全审计。当前仓库 ref 指向 `7876ce42bafac38ada3c5ccca7df861ed33b63e9`，API 的提交日期字段为 2020-01-16；当前固定提交与本轮目录 7/7 路径／大小／blob 一致，**不证明该 ref 在 2022 归档时的状态或生产部署**。G06 在本次 API 响应中只列出一个公开仓库；不据此推断私有或删除的仓库。

**增补 r110 GH03**：旧轮对支持域名的 GitHub 代码搜索保存为零结果，本轮沿归档文档链接直接定位到这个公开 README，文件中确实含同一支持域名。旧轮本就说零结果不能证明不存在；本次发现不证明旧查询当时返回错误，也不推测搜索索引原因。

## 全量读取完成（限定清单）

**58/58 个不同路径、355,715 bytes**。其中四个隔离视频局部块只做完整字节／UTF-8 扫描与哈希，不作语义结论；四个成功页辅助块与完整页重复；七个 GitHub 原文件完整解码逐行扫描，报告不摘录样例值；README 的公开旧预览链接曾在工具回读中显示但未访问。因此 58 是**路径数，不是 58 个独立原始来源或 58 份人工语义审核**。

| 分组／逐路径清单 | 文件数 | bytes |
|---|---:|---:|
| [r110／r111 比较资料](prior-round-read-inventory.csv) | 9 | 60,019 |
| [旧来源对照](comparison-source-read-inventory.csv) | 6 | 53,706 |
| [r104 来源形态元数据](prior-provenance-read-inventory.csv) | 3 | 16,355 |
| [r110 GH03 查询及响应](prior-gh-read-inventory.csv) | 2 | 667 |
| [首批 CDX 回读](archive-index-read-inventory.csv) | 4 | 470 |
| [补充 CDX 回读](archive-index-extension-read-inventory.csv) | 2 | 418 |
| [GitHub API G01–G05](github-api-read-inventory.csv) | 5 | 22,444 |
| [GitHub API G06](github-org-read-inventory.csv) | 1 | 5,332 |
| [GitHub 逐文件原始字节](github-files-read-inventory.csv) | 7 | 91,709 |
| [本轮成功页面／回放](new-source-read-inventory.csv) | 6 | 38,984 |
| [失败／隔离诊断](diagnostic-read-inventory.csv) | 9 | 39,771 |
| [同源成功分块](successful-chunk-read-inventory.csv) | 4 | 25,840 |

另做安全复验：三份入场元数据 **3/3、621,041 bytes** 完整解析；32 份已有保护副本 **32/32、17,473,261 bytes** 仅做字节哈希、不解释内容。868 个入场 stash 对象和远端原位／既有保护副本 blob／mode 逐项核对；本地 stash 不保证跨环境持久。上述 58、3、32 三组共 **93 个不同路径、18,450,017 bytes**，其中保护副本及隔离块不是正文语义研究。[安全复验](safety-recheck-summary.json)。

## 检索、偏差和与上轮的差异

22 次预列搜索逐条执行，保存 **67 条非空结果元数据**、3 次无可见结果；重复／无关项不是独立事实。六个 CDX 索引按状态／MIME／摘要及 `to=20261026` 过滤后共 4 条记录，另两项为空；索引 200 不证明页面身份，空结果不证明没有其他档案。

相对 r111，本轮新增历史认证、问题和 GitHub 样例；相对 r110 是**增补**而非把 TACACS 与 802.1X 的不同版本门槛合并。旧 r109 V01 的视频仍因分块漂移无法验证，E03 动态培训索引则本轮可见。对旧网页 P01 的范围选取过宽、两个视频不完整、人工转存更正、API 和分块先后顺序等均见[偏差记录](scope-and-sequence-deviations.md)，已向用户说明。未主动下载官网 PDF、未操作设备或联系主体，未重新开启 PASS 事项。

同一宿主机单调钟在整理中测得 **2,689.667 秒**，含研究、整理与思考，不证明持续键盘操作；未用睡眠凑数。[计时](timing-check.json)。本轮未取得独立兼容性测试、现场部署、发布公告、工商原件或客服支持承诺，不宣称穷尽。

[主报告](../01-text-verbatim/workstation/08-customer-pipeline/181-angora-nac-support-bug-evidence-r112-2026-10-26.md) · [独立档案附录](../01-text-verbatim/workstation/09-orders/120-angora-orders-dossier-2026-10-21.r112-appendix.md) · [字段映射](../01-text-verbatim/workstation/09-orders/120-angora-orders-master-2026-10-21.mapping-r112.md) · [审计](../75-audit-r112-2026-10-26.md)。
