# r109 来源、范围与可复验说明

## 1. 范围与限制

本轮聚焦 Angora 产品化、验证、培训与售后叙事；不联系客户或第三方，不提交活动表单，不解析官网 PDF，不重启任何用户已 PASS 的事项。会话日期按 **2026-10-26 UTC**，沙箱钟观察为 **2026-11-19 UTC**，冲突未解；这些不是历史来源的已证采集日期。

分析使用 [source-catalog.csv](source-catalog.csv) 的 **9 个分别保留的既有产物**，按自身原路径引用，共 101,321 bytes（以本轮追加前字节为准）。它们包括媒体刊载的受访者自述、同厂商不同语言页面、机器转写及旧研究摘要，**不是九个独立证人**。`S09` 的目录哈希为追加前前缀；追加后的完整文件及前缀分别见 [append-log.csv](append-log.csv)。

- 2023 ICT Media 文章自称为节目的摘要；r106 四块人工转存，r107 只修订一个漏字点，未自动逐字对平全文。其受访者声明不是独立测试或履约证据。
- 服务／设计／培训网页为过去轮次保存的工具可见文字；无本轮新抓的原 HTML。英／土文由同一发布方提供。培训段落的差异不能区分原网页、抽取及人工转存原因。
- r108 市场视频保存的是工具可见转写而非原音，存在识别／手工转存误差；初始假设、演讲者解释和实际调查原始资料不可混同。
- 旧 `50` 为二手研究，不是目标视频全文；此前它的 2022 活动日、市场单位和假设结论已经由 r108 修正。本轮仅进一步限定 SOP、人员／视频现状、字幕覆盖、观看量推论及出口起始年。

## 2. 先列后读与计数

| 本地范围／回读 | 路径数 | bytes |
|---|---:|---:|
| [主范围](local-scope-before-read.csv) / [回读](local-read-inventory.csv) | 40 | 770,933 |
| [补充](supplemental-local-scope-before-read.csv) / [回读](supplemental-local-read-inventory.csv) | 5 | 41,724 |
| [培训](training-local-scope-before-read.csv) / [回读](training-local-read-inventory.csv) | 2 | 10,586 |
| [上轮本地清单](comparison-local-scope-before-read.csv) / [回读](comparison-local-read-inventory.csv) | 1 | 4,645 |
| [上轮另列社媒清单](comparison-social-scope-before-read.csv) / [回读](comparison-social-read-inventory.csv) | 1 | 352 |
| **去重合计** | **49** | **828,240** |

**全量读取完成（仅上述本地范围）：49/49 个不同路径，828,240 bytes 完整逐字节回读；不是全仓扫描、49 个独立来源或原 HTML。** 一份本轮自建 baseline 曾先于修正后完整范围被打开，见 [D02](local-scope-deviation-D02.md)。误打开的历史主档包含已 PASS 章节，见 [D03](local-scope-deviation-D03.md)；不使用这些章节作结论。以上两项均如实计入，哈希本身不证明访问顺序。

[与 r108 的逐路径比较](local-scope-r108-r109-comparison.csv)：r108 的主清单 23 路径另加一条社媒选择，共 24；r109 为 49；重合 10。最初比较只读了 23 行主清单，随后先列并回读另一个清单，已在最终对照中修正。

## 3. 搜索与网页访问

- 8 个搜索问题先记录于 [Q01–Q05 计划](discovery-plan-before-search.csv)和 [Q06–Q08 计划](discovery-events-plan-before-search.csv)；搜索仅用于发现路径。两份元数据表分别保留 [24](discovery-metadata.csv) 与 [12](discovery-events-metadata.csv) 条结果信息，不保存片段为全文、不用来证明课程实施或视频内容。搜索结果不是原页面，可能遗漏或排序动态变化。
- [5 个目标直接地址](external-fetch-plan-before-fetch.csv)的首块与 [3 个替代入口](external-alias-plan-before-fetch.csv)的首块均返回 `Failed to fetch page`；[直接结果](external-fetch-attempts-01.csv)、[别名结果](external-fetch-attempts-02.csv)分别记录。**0 个目标来源新全文，0 个原音／原始 HTML／测试报告。** 未拼接任何跨次、跨来源片段。
- [GitHub 首页诊断](diagnostic-result.csv)仅第一块成功、还有第二块；没有把它当 Angora 来源或完整抓取。不能将目标失败笼统称为所有网络工具故障。
- 本地 `gh search code` 子命令不受支持，[首次调用](github-cli-invocation-error.csv)未执行搜索；后改为预列的 REST API，三次代码查询 `GH01A`–`GH03A` 各返回 `total_count=0`，仓库查询 `GR01/GR02` 各为零，精确名账号 `GR03` 返回 404。响应各自保存于 `github-api-*.json`；这些是当次索引元数据，不证明不存在镜像或相关主体。类似姓名的未知主体不合并。

## 4. 索引与保护

- [44 条完整保存行及哈希](evidence-traceability.csv)；摘要用锚并不代替原来源文本。每行哈希计算 UTF-8 行文本，不含行尾换行。
- [14 项生命周期主张／边界](lifecycle-claim-boundaries.csv)、[4 项双语段落对照](training-visible-paragraph-check.csv)、[8 项具名修正／限定](issues-and-corrections.csv)。单一厂商的多语言材料不能算交叉独立证据。
- [追加前计划](append-plan-before-write.csv)、两个单独追加文本及 [追加日志](append-log.csv)记录了旧 `50` 和旧 dossier 的原始前缀、追加字节及新哈希；没有合并或改写旧正文。
- [入场安全目录](../60-entry-safety-r109-2026-10-26/)记录初始 868 个未跟踪文件：836 与远端 r108 的 Git blob 相同，32 不同；32 个原异版均单独复制，31 又与既往保护副本逐字节一致。868 个 blob 在本地 stash `e74e476b678b48c3ce060a8c01fd04dd926a99cc` 的第三父树中逐项匹配，stash 未 pop；stash 是本地引用，不声称已推到远端。工作分支已仅做 fast-forward，无 reset、清理或切分支。
- 首次矩阵生成脚本存在语法错误、在执行前退出，未写任何矩阵；修正后才成功生成。脚本成功和哈希不保证研究结论、来源真实性或人工转存准确。
- [提交前输出清单](output-manifest-before-stage.csv)记录本轮明确列出的文件、字节和 SHA-256；为避免自引用，该清单不对自身计算哈希。只按清单及清单自身显式暂存，不使用 `git add -A`。
