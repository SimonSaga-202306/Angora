# r108 · KOZ 研究、商业化与证据边界

## 本地范围：完整字节读取，按来源分开

[第一批专题范围](local-scope-before-topic-read.csv)和[完整字节／哈希](local-read-inventory.csv)为 **23 个不同路径、197,292 bytes**；其中 5 项在本轮专题清单之前，已先按 [r108 安全范围](../56-entry-safety-r108-2026-10-26/README.md)列出并完整读取。其余 18 项先列专题范围再读。它们包括旧报告、上轮来源／索引、既存厂商页面、两份派生 CMS 表、修订后访谈转存；不读取已隔离的伙伴墙和禁用 PDF 抽取。

先保存 `02-social-intel` [顶层完整目录元数据](social-directory-complete-metadata.csv)（5 个条目），然后单独列出并完整读取[旧 KOZ 视频研究 `50`](social-selection-scope-before-read.csv)，见[回读哈希](social-selection-read-inventory.csv)：1 条、17,662 bytes。该文件是旧的**研究／字幕摘录**，不是视频原件；没有把其中旧姓名或过时的主动追问作为本轮跟进。

合计 **24/24 个不同路径、214,954 bytes**：5 条先在安全范围列读再纳专题，另 19 条按各自本轮范围先列后读。哈希只能标识保存字节，不能独立证明先后顺序或内容真实。与 r107 的 20 项[交集](overlap-r107-20.csv)为 9 条；范围不同，24 对 20 不是可比质量分数，也不表示已覆盖全资料库。安全核查另有 31 个保护副本、17,455,599 bytes，不计入 24 项。

一次早期探索性文件名筛选因共同路径前缀误匹配，元数据输出过多且被工具截断，包含与本轮无关旧单文件名；**未打开其正文、不计作完整目录或来源**。改用社媒目录的完整 5 条元数据后再选读一条。见[偏差 D01](exploration-deviations.csv)。

## 新 URL：按来源身份、展示层和完成状态分别记

1. [ICT Media KOZ 预告](external-visible/ictmedia.com.tr/haber/angora-networks-kanal-ortaklari-zirvede-bulusuyor/index.tr.extracted.md)：[事先范围](web-event-scope-before-fetch.csv)，2/2 工具块，14,244 bytes（含储存用末尾换行），[范围和哈希](web-event-visible-inventory.csv)／[块偏移](web-event-chunk-inventory.csv)。前瞻议程不是实际会议或签约证明。
2. [TÜBİSAD 协会页面](external-visible/www.tubisad.org.tr/tr/guncel/detay/Turkiye-bilgi-ve-iletisim-teknolojileri-sektorunun-buyuklugu-150-milyar-lirayi-asti/58/2671/0/index.tr.extracted.md)：先列[范围](web-market-scope-before-fetch.csv)，工具返回 1/1 块、420 bytes，但只有导航与 cookie 说明，**文章正文和原报告未取得**；不把搜索摘要当正文或原件。[块记录](web-association-chunk-inventory.csv)。
3. [Global Tech 2020 文章](external-visible/www.globaltechmagazine.com/2020/06/02/bilgi-ve-iletisim-teknolojileri-sektoru-2019-pazar-verileri-aciklandi/index.tr.extracted.md)：同一事先范围，3/3 工具块、23,266 bytes；是媒体对 TÜBİSAD 数字的转述，不是独立的新调查或 Angora 财报。动态页眉及推荐栏目含晚于会话日期的文本，正文日期和页面采集日期不能由这些字段推断。
4. [Angora 市场分析视频工具转写](external-visible/www.youtube.com/watch/32J3cYQXCyM/index.tr.extracted.md)：先列[范围](web-video-scope-before-fetch.csv)，3/3 工具块、17,948 bytes；是视频页面的无时间戳工具文本，不是视频原件、听音、幻灯片或经过逐字校对的字幕。[视频／媒体块范围](web-market-video-chunk-inventory.csv)，[三项回读哈希](web-market-video-visible-inventory.csv)。

以上 **4 个来源身份、9/9 工具块、55,878 bytes**；其中 3 个有本轮可分析正文／转写，协会页无正文。每个 URL 的文字单独保存，按工具返回范围不故意删段；尾部额外换行仅为存储形式。页面与视频均人工转存，未能程序化取得工具响应字节比较，**不能保证完整逐字忠实**。媒体页第二块曾独立人工重抄并与保存片段匹配，见[记录](web-manual-transcription-check.csv)；两次都人工，不排除相同漏字，且工具接口并不保证固定块长。ICT 页面边界脚本的初次错误已写[偏差 D02](exploration-deviations.csv)。

[字节检查](tool-text-byte-characteristics.csv)记录市场视频文字 1 行、隔离片段 2 行的原可见行尾空格；为不静默清理，这两个文件在 [.gitattributes](.gitattributes) 中设 `-diff`，其余证据文件不受该特殊规则影响。实际文件仍是 UTF-8 文字，逐文件及行尾字节由新 verifier 检查。

### 一条渠道视频没有取得完整文本

[原 URL](web-channel-video-scope-before-fetch.csv)的首块返回 4 块转写呈现，后续却是 5 块的推荐页面；另按[短链接](web-channel-video-alias-scope-before-fetch.csv)尝试，同一个视频的前 2/4 块可衔接，后面又变成 6 块推荐页面。按原先计划停止，不把不同呈现硬拼。[调用元数据](web-channel-video-response-metadata.csv)逐项记录；[前两块完整返回片段](quarantine/www.youtube.com/watch/jrdoTa5owZk/visible-chunks-0-1.tr.partial.md)明确标作 **不完整、隔离、不用于结论**，[哈希／偏移](web-channel-video-partial-chunk-inventory.csv)。不兼容的推荐流仅留元数据、没有另存全文，不算完整来源，见[结果](web-channel-video-incomplete-result.csv)及偏差 D03。片段中有商业措辞，但没有提取价格或设置跟进。

因此共尝试 **6 个 URL、5 个来源身份**（含同视频别名）：4 个完整工具呈现、1 个视频不完整；只把其中 3 个含正文／转写的完整来源用于分析。四个完整文件的字符数／哈希不能证明真实性或人工转存无误。

## 派生核对与来源等级

[57 条行锚](evidence-traceability.csv)绑定旧文件**追加前前缀**和新保存文本、行号及行哈希。另有 [3 个假设／演讲结果](hypothesis-versus-presented-result.csv)、[8 项条件样本账](survey-accounting.csv)、[6 个单位算式](market-unit-arithmetic.csv)、[2 个分项差](market-component-check.csv)、[2 项预告／视频时序](event-and-recording-chronology.csv)和[13 项具名纠错／限定](issues-and-corrections.csv)。所有假设方向、`milyon/milyar`、`sahada` 均保留来源语境，不把条件算术当实测；字幕错词需原音与原研究材料复核。

[四个旧文件追加计划](append-plan-before-write.csv)先与入场 Git blob 比较后形成，[追加哈希](append-log.csv)保留 132,111 bytes 原前缀、最终追加 4,196 bytes；无覆盖或合并旧源。为澄清上传／公开日期和避免夸大转存完整性，本轮修订了两处不同文件的新增后缀，先列[计划](append-revision-plan-before-write.csv)、后留[前后哈希](append-revision-log.csv)，原有前缀不变。`50` 的假设误写、单位、设备／SKU／法律泛化和 r95 的峰会计划日／实际日期差异在原文件、独立档案附录和映射中具名修正。

## 搜索与 PASS

九条查询先写[第一组](discovery-plan-before-search.csv)、[第二组](discovery-study-plan-before-search.csv)；返回 **33 条结果记录**，分别保存为[13](discovery-metadata.csv)和[20](discovery-study-metadata.csv)条发现元数据，不把重复 URL 当独立来源。Q06 虽排除 PDF，仍返回 1 条无关 PDF 的搜索片段：**未打开或主动下载、未另存片段、不用于结论；搜索服务后台是否解析 PDF 未知**。一个搜索结果日期晚于会话日期，未打开或用于结论。未接触客户、协会或讲者；未使用已隔离页面、停用主体、历史财务差异、未成交／未付款旧单、仓库 RFQ/RFP、INFO.rar、评论验证、48 口澄清、阶梯报价或主动下载官网 PDF。

会话提供日期为 `2026-10-26 UTC`，环境时钟显示 `2026-11-19 UTC`；标签、动态页眉与环境时钟不证明历史网页采集时刻。

**全量读取完成（仅本轮限定本地清单）：24/24 路径、214,954 bytes；4 个完整工具呈现各自保存 9/9 块，另一个视频仅得 2/4 转写块、隔离不用。** 不代表视频原音、报告原件、实时状态或全部商业史已核实。
