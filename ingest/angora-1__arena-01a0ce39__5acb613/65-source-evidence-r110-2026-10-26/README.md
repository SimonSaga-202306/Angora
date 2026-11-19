# r110 来源、范围与可复验说明

## 一、原则和计数

本轮研究 Angora 历史软件支持、升级、堆叠与设备认证文档；不联系任何客户或第三方、不登录门户、不操作设备、不下载固件或官网 PDF，不重新开启用户已 PASS 的事项。会话指定日期为 **2026-10-26 UTC**；环境钟读到 2026-11-19，冲突未由独立时钟解决，不把任一目录标签或环境读数倒填为旧网页实际采集日。

**全量读取完成（严格限定以下本地清单）：48/48 个不同路径、258,517 bytes，均完整字节读取并记 SHA-256。** 这是一次明确范围的文件回读，不是全库、48 份原始网页、48 位证人或全部商业信息：

| 范围 | 先列范围 | 逐文件回读 | 路径 | bytes |
|---|---|---|---:|---:|
| 既存报告、映射及审计 | [范围](comparison-local-scope-before-read.csv) | [回读](comparison-local-read-inventory.csv) | 14 | 100,177 |
| 本轮保存的回放、错误页、索引与 GitHub 元数据 | [范围](source-artifact-scope-before-read.csv) | [回读](source-artifact-read-inventory.csv) | 28 | 130,178 |
| r109 五份清单，用于路径比较 | [范围](r109-inventory-comparison-scope-before-read.csv) | [回读](r109-inventory-comparison-read.csv) | 5 | 12,813 |
| 追加 CLI 回放 | [范围](supplemental-cli-scope-before-read.csv) | [回读](supplemental-cli-read-inventory.csv) | 1 | 15,349 |

本轮比较用 14 条既存路径与 r109 的 49 条路径有 **4 条重合**，其余 10 条是本轮比较范围新纳入；两轮研究主题不同，来源保存产物及入场保护核查不混算进该 14 条。见[逐路径比较](r109-r110-local-path-comparison.csv)。预列并完整回读的三份旧报告含历史订单／已停事项概述，选择范围过宽已[单独披露](local-scope-deviation-D05.md)；未重新打开其底层文书，也未根据停项产生新结论或跟进。r109 当轮目标全文取得为零；r110 的新增是以下**历史归档**，不是追溯改写 r109 当时是否抓到，也不是现行站点完全恢复。

## 二、搜索、直连、索引和回放

- [Q01–Q08](discovery-plan-before-search.csv)、[Q09–Q11](upgrade-discovery-plan-before-search.csv)、[Q12–Q14](archive-discovery-plan-before-search.csv) 共 14 次预列搜索；手工元数据分别为 [32](discovery-metadata.csv)、[7](upgrade-discovery-metadata.csv)、[7](archive-discovery-metadata.csv) 行。**查询归属、排序及零结果标记未经可靠核实**，46 行仅为待核查发现线索，不据此断言某查询的结果或零命中；三个表逐行添加警示，并各自保留原字节副本，见 [C12 修正记录](discovery-attribution-correction.md)。不以搜索片段冒充全文。
- [五个直连目标](external-fetch-plan-before-fetch.csv)的工具状态虽显示 `success`，返回内容却均为 Cloudflare **522** 错误而不是目标知识库正文；[尝试表](external-fetch-attempts.csv)和每 URL 的[独立错误转存](quarantine/522/)保留，错误页中的 IP 为工具/代理响应中显示的值，不是用户地址。单次返回不能证明网站永久离线或全球不可访问。
- 档案馆 CDX 按各 URL [先列](archive-fetch-plan-before-fetch.csv)及[扩展先列](archive-index-extension-plan-before-fetch.csv)、分别保存 9 个响应：筛选到 **35 条经 `200`、`text/html` 及 digest 折叠后的索引记录**。这不是所有捕获次数或正文；记录中的 `length` 是 CDX 字段，不是本地转存字节数，`200` 亦不保证页面身份。见[第一批索引回读](archive-index-read-inventory.csv)、[第二批回读](archive-index-extension-read-inventory.csv)和[总目录](source-catalog.csv)。
- [第一批](archive-replay-plan-before-fetch.csv)、[第二批](archive-replay-extension-plan-before-fetch.csv)及[补充 CLI](archive-replay-cli-plan-before-fetch.csv)共预列并请求 11 个归档回放，累计取得 **20/20 工具可见分块**，但能否取得目标正文另作身份检查。七个目标正文按捕获各自人工转存；另两个完整工具回放用较早文本和已观察差异重建，等级更低；两个目标未得到可用正文而隔离。完整状态和每文件字节、SHA-256 见[回放结果](archive-replay-results.csv)。
- 四次[预列 GitHub 代码检索](github-discovery-plan-before-search.csv)均返回 `total_count=0`，响应各自保存；只说明此次索引无命中，不证明全网不存在镜像。受沙箱外连限制，shell 对档案馆 HTTPS 的一次仅头部诊断返回 SSL 连接错误；没有 shell 直接下载原始 HTML。

### 可用于分析的七个独立保存产物

| ID | 历史捕获（UTC）与页面 | 工具块 | 保存文件 | 证据级别与边界 |
|---|---|---:|---|---|
| AR01 | 2021-02-27 20:58:59，英文 TACACS/ISE | 2 | [可见文字](archive-replay/support.angoranetworks.com/ht_kb/tacacs-authentication-with-cisco-ise/20210227205859/index.visible.md) | 厂商指导；其说过测试不等于我们取得测试报告 |
| AR03 | 2021-02-27 21:34:35，土文 TACACS/ISE | 3 | [可见文字](archive-replay/support.angoranetworks.com/ht_kb/tacacs-kimlik-dogrulama-cisco-ise-kullanarak/20210227213435/index.visible.md) | 同一发布方的另一语言；不是独立测试 |
| AR05 | 2022-01-18 06:34:31，英文堆叠 | 2 | [可见文字](archive-replay/support.angoranetworks.com/ht_kb/stacking/20220118063431/index.visible.md) | 页面的一般描述；无型号兼容表或现场测试 |
| AR08 | 2025-02-11 05:19:45，英文软件升级 | 2 | [可见文字](archive-replay/support.angoranetworks.com/ht_kb/software-upgrade-tftp-verge/20250211051945/index.visible.md) | 版本文件名是示例；未获取镜像或图片 |
| AR09 | 2025-02-11 06:29:09，土文软件升级 | 2 | [可见文字](archive-replay/support.angoranetworks.com/ht_kb/yazilim-guncelleme-tftp-verge-anahtarlar/20250211062909/index.visible.md) | 同厂商；门户链接为历史说明，不验证现行可访问 |
| AR10 | 2025-01-23 06:08:22，土文 ZTP | 1 | [可见文字](archive-replay/support.angoranetworks.com/ht_kb/sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp/20250123060822/index.visible.md) | 厂商对 DHCP/TFTP 的描述，不是部署记录 |
| AR11 | 2025-01-23 07:25:50，土文 CLI | 2 | [可见文字](archive-replay/support.angoranetworks.com/ht_kb/komut-satiri-kullanimi/20250123072550/index.visible.md) | 模板和示例的接口中间段不一致；未实测 |

上述路径包含每个来源工具返回的首尾及分块内容拼接成各自一个产物；**只在同一回放内部衔接分块，不合并不同来源**。均为人工转存的工具可见 Markdown（包括 Wayback 工具栏），并非原 HTML／图片／固件；没有与工具响应自动逐字节比对，可能有转存误差。AR09 一处相关文章链接 title 曾手抄漏字，在提交前对照工具结果改正，见 [C07](issues-and-corrections.csv)；其余全文仍未自动逐字核验。

### 特别处理：重建、缺正文及污染

- AR02（2024 英文 TACACS）及 AR06（2025-02 堆叠）各有两个完整工具可见块，但本地无法直接从工具响应对象自动落盘；根据[执行前重建说明](transcription-reconstruction-plan.md)和[重建脚本](../../../tools/reconstruct_r110_replays.py)，分别从 AR01／AR05 模板替换各自捕获时间、工具栏、相关列表及页面标题，另存 [AR02](archive-replay-reconstructed/support.angoranetworks.com/ht_kb/tacacs-authentication-with-cisco-ise/20240530151345/index.visible.md) / [AR06](archive-replay-reconstructed/support.angoranetworks.com/ht_kb/stacking/20250211043846/index.visible.md)。**这是标明模板来源的重建，不可宣称与当次工具输出逐字相同，也不能以此声称跨时间全文未变。** 45 个事实锚全部取自上表七份直接转存，不以重建稿当独立证人。
- [AR04](quarantine/archive-replay/support.angoranetworks.com/ht_kb/tacacs-kimlik-dogrulama-cisco-ise-kullanarak/20240530160504/index.visible.md) 只显示档案工具栏及标题，正文未取得。不能因为 CDX 列 200 便认定正文可用。
- [AR07](quarantine/archive-replay/support.angoranetworks.com/ht_kb/stacking/20250805064927/index.visible.md) 回放显示的是无关汽车配件网页，不是 Angora 堆叠文章；仅保存作为身份检查和污染证据，**不用于 Angora 事实或联系**。不推断原因、域名控制权或网站遭入侵。
- 部分直接转存引用了多个示意图／截图，但没有获取这些图像文件，亦未执行原文命令。转存文件的 SHA-256 只锁定本地保存文字，不证明网页原件、历史采集时序、产品能力、证书、实际交付或售后履约。

## 三、索引、差异与局限

[45 条原文行范围及哈希](evidence-traceability.csv)只定位七篇直接转存；[19 项主张边界](claim-boundaries.csv)、[四组双语差异](cross-language-comparison.csv)、[十二项具名补充／限定](issues-and-corrections.csv)不是新证人或原文替代品。五个错误页、九个 CDX 索引及 AR09 的一次局部查看先于汇总文件范围，已[逐项披露并在后续完整回读](local-scope-deviation-D04.md)。技术名词和示例地址属于历史文档内容，不构成实际设备配置建议。

时间差异应由可信来源独立校准。r105–r109 已记载会话日和环境钟冲突；本轮复核发现它们写的会话指定日与本会话指定值相符，故不能仅凭环境读数改称其会话日期全部有误。过去的真实访问和采集日仍未知；r106 对晚于所给会话日期的推荐栏所作的未来判断，应理解为相对于该给定日期的条件判断，不是独立的发布日期核验。

[提交前输出范围](output-scope-before-hash.csv)及[范围扩展](output-scope-extension-before-hash.csv)先列共 103 条路径，再生成[逐路径大小与 SHA-256](output-manifest-before-stage.csv)；其中 102 个非清单自身文件有字节数与哈希，清单自身为避免自引用记作 `SELF`。只按该范围显式暂存，不全量 `git add -A`。
