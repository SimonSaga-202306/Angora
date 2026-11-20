# r114 限定来源、回读及证据说明

## 范围与日期

会话给定日期 **2026-10-26 UTC**；沙箱观察时钟为 **2026-11-20 UTC**，冲突未独立校准。文件夹日期是历史标签；归档索引的 `to=20261026` 是检索截止，不是本轮实际抓取日。已具名纠正把沙箱钟误作会话日期的连续性摘要，见[日期更正](session-clock-discrepancy-correction.md)。不将未来 `pageAge` 和动态侧栏当历史正文。每个历史捕获日期仅说明索引／回放显示的时间。

本轮聚焦 Angora 本体的 2020–2022 公开活动、2016 相关简介和 IANA 标识，作为先前工作增补。**主体未确认**。没有工商登记原件、视频原音、独立测试／证书或交付证据。网页人工转存是工具可见文字，不是原 HTML、工具响应的自动字节副本或现场测量。

## 目录与证据锚

- [初始来源目录](source-catalog.csv)、[扩展目录](source-catalog-extension.csv)、[早期归档目录](source-catalog-cutoff-archive.csv)、[2022 活动目录](source-catalog-2022-event.csv)分别保留 URL、文件、字节、SHA-256、等级和界限。目录有索引、失败、转录初稿和多块，同源块／快照不重复算独立来源。
- [初始锚](evidence-traceability.csv)、[早期归档锚](cutoff-evidence-traceability.csv)、[2022 活动锚](event-2022-evidence-traceability.csv)包含精确子串、路径、行号和本地 SHA-256。[边界](claim-boundaries.csv)和[具名增补／纠错](issues-and-corrections.csv)逐项解释可与不可推断。
- P01／AR04 是同一组织方 2020 议程不同呈现；P02／AR05 同一人物简介不同呈现；P05／AR06 同一政府报道不同呈现。媒体报道和组织方议程来自不同发布方，但可能存在信息依赖，不能当作两份独立出席见证。
- 2022 年 July AR07 和 December AR08 是同一组织方同一议程的不同快照；AR09 是同组织方的场次说明。AR08 的两块各自保留在 `archive-chunks/AR08/`，中间拆开一词，不拼接。7 月议程自身写了 2022 和 2021 两种年份，[选定子串比较](event-2022-selected-comparison.csv)不证明其他时期或原 HTML 内容未变。r111 KobiEfor 原报道保持旧路径，不重新复制。
- AR08 曾误生成并读过拼接副本，已核对哈希后仅删除该本轮生成副本；两块和原计划／结果清单保留。[执行前说明](AR08-nonmerge-and-transcription-correction-plan.md)、[移除及初稿记录](AR08-correction-intermediate.json)、[单处纠错](AR08-correction-result.json)。旧 `AR08-assembly-result.json`、`AR08-chunk-read-inventory.csv` 和 `event-2022-read-scope-before-reread.csv` 记载的是纠正前状态，不能拿来代表当前文件或最新哈希。

## 完整读取与数量核对

**全量读取完成（限定清单）：127/127 个不同路径、414,017 bytes。**此前限定清单 97/97、323,433 bytes；本续轮新列清单 30/30、90,584 bytes。以前清单中的 96 个非隔离文件在本续轮重新逐个完整字节／UTF-8 读取并与旧哈希一致，1 个曾误读的隔离页面没有再次打开，只保留此前读取记录及文件大小。新增 30 项逐个完整字节／UTF-8 读取，其中问询元数据完整解析；主要来源文本亦分别展示回读。各清单不与来源数量等同。

- [原 97 项汇总](read-summary-final.json)：[旧轮 14](prior-round-read-inventory.csv)、[旧资料 2](prior-timeline-read-inventory.csv)、[本轮基础 18](external-read-inventory.csv)、[扩展 2](extension-read-inventory.csv)、[归档对照 14](cutoff-archive-read-inventory.csv)、[Q01–Q47 47](search-discovery-read-inventory.csv)。其中旧资料 2 内有误回读的 4,899 字节隔离页，排除结论。[D01 披露](scope-and-record-corrections.md)。
- [新增 30 项事前回读范围](continuation-expanded-read-scope-before-reread.csv)及[逐项回读清单](continuation-expanded-read-inventory.csv)：Q48–Q69 共 22 项、CDX08、AR07、AR08 两分块、纠错初稿、CDX09、AR09 和 r111 旧媒体正文各一项。[总数核对](combined-read-summary.json)。
- 这不是全库或 127 个独立来源：含 69 条检索记录文件、失败、CDX、重复块、手工错误初稿和隔离材料。旧合成辅助视图与本轮删除的 AR08 合成副本均不算新证人。原 97 和新增 30 在总体列单前已有初取／读取，随后按各自限定范围重新完整回读；r111 媒体先做了字节行数扫描，后列范围再完整回读，见[顺序披露](prior-2022-media-scope-before-reread.csv)。

## 检索及禁区

Q01–Q69 按计划串行检索、按查询独立保存，总计 254 条非零搜索结果元数据及 3 个零结果查询。元数据标题可简写，不是完整搜索响应；重复、无关、同名和未来 `pageAge` 均未算证据。Q15/Q65 未来结果未打开；Q22/Q40 无关财务片段未记录数值或分析；Q55/Q67/Q69 等仍出现无关 PDF 标记，未打开或下载。

P03 与 P05 已保留错误初稿和纠正；Q42／Q53 元数据有具名纠正。AR03 回放跳到无关域名、已隔离，未访问目标。[过程偏差](scope-and-record-corrections.md)及[清单](issues-and-corrections.csv)。Q68 实为 r107 已保存的 EGM 厂商公告，[重复说明](search-corrections/Q68-existing-r107-cross-reference.md)；不重算为新证书。没有重新打开停项主体、主动下载官网 PDF、登录设备、联系机构或重开其他 PASS 事项。

[同环境续轮计时](continuation-timing-check.json)：实测超过 10 分钟，包含研究、思考和工具等待，不代表持续键盘操作，没有睡眠凑时。尚未穷尽公开商业资料。
