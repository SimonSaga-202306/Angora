# r111 来源、完整回读与边界

## 日期和范围

会话给定日期 **2026-10-26 UTC**；环境观察的墙钟为 **2026-11-19 UTC**，冲突未独立校准。两者都不自动等于旧资料实际采集日。本文保留目录标签、历史证据及时间字段；[具名纠正](time-and-provenance-correction.md)说明本轮误转述 r110 C04 后的更正，r110 的谨慎日期口径仍成立。

本轮主体是 Angora；不联系人、不登录、不下载官网 PDF 数据表、不解压 INFO.rar、不重开已 PASS 的事项。搜索服务意外显示停项摘要后没有打开或使用，详见 [D01](discovery-scope-deviation-D01.md)。Q26 的 `-filetype:pdf` 未完全生效，结果出现两个**无关的 TOBB PDF**的自动摘要／元数据；没有打开、下载或用于结论。没有新的 Ewind 事实，也没有更改用户给定的对手判断。

## 逐源记录（均为本地工具可见文字，不是原始 HTML）

下表的字节数是单个本地文件当前大小。完整路径、单项 SHA-256、来源日期字段、来源等级、失败／未打开状态及具体局限见 [source-catalog.csv](source-catalog.csv)。每个网站／视频独立存放，不把不同来源、客户或事件合并。

| ID | 来源和状态 | 本地字节 | 可分析边界 |
|---|---|---:|---|
| X01 | [Advensis 抓取失败记录](fetch-failures/X01.visible.md) | 458 | 工具没有给状态码、原因或正文，不证明永久不可访问。 |
| X02 | [KobiEfor 2022 活动报道](external-visible/kobi-efor.com.tr/kapak/tbdden-kamu-bib25-ve-bimy29-butunlesik-etkinligidijital-h15774/index.visible.md) | 36,335 | 5/5 可见块；媒体自称活动媒体赞助商。发表日按页面字段，不取搜索 `pageAge`。 |
| X03 | 预列的同标题 URL，**未抓取** | — | URL slug 与 X02 返回的 canonical 相同、`www` 主机不同；可能是别名但尚未核实，绝非第二证人。 |
| X04 | [2020 短访谈页面](external-visible/www.youtube.com/watch/yveHNxOXD3g/index.visible.md) | 3,874 | 上传日期是页面字段；自动字幕未经听音，海外销售不等于首次报关出口。 |
| X05 | [厂商隐私页面](external-visible/www.angoranetworks.com/privacy-policy/index.visible.md) | 13,132 | 2/2 可见块；名称是自述，同页另有名称变体及不能作为业务事实的政策语言。 |
| X06 | [2023 销售培训公告](external-visible/www.angoranetworks.com/event/angora-kanal-ortagi-satis-egitimi/index.visible.md) | 6,932 | 网页计数 45；议程及报名字段不证明课程执行、实到或成交。 |
| X07 | [第三方目录](external-visible/www.find.com.tr/Company/angoranetworksbilisimteknolojiticaretsanayianonimsirketi/index.visible.md) | 9,190 | 2/2 可见块；目录标未核验、注册号不公开；与品牌主体的法人同一性未确认。 |
| X08 | [2023 ThinCe 培训公告](external-visible/www.angoranetworks.com/event/angora-thince-ince-istemci-egitimi/index.visible.md) | 5,019 | 网页计数 58；报名截止与活动日期相隔 29 天，原因未知，不证明实际出席或演示。 |
| P01–P04 | 四份既有来源 | 合计 59,332 | 2023 访谈摘要、厂商出口帖、2022 上传视频转写、2021 培训协议；路径及哈希见各清单，仍各自独立。 |

六个新取得的成功页面／视频共 **74,482 bytes、12/12 个工具块**：X02 五块、X04 一块、X05 两块、X06 一块、X07 两块、X08 一块。X02 的 [五个块](external-chunks/X02/)另行各自保存并用于连续边界检查；合成为单一页面是对**同一网页分块的还原**，并非合并不同来源。X05／X07 的两块各自连续转存在该来源的单一文件里，未另留两份块文件。X01 失败、X03 未打开，不计为成功页面。没有保存原 HTML、图片或音频；手工转存未与工具响应自动逐字比对，本地哈希只锁定本地字节。已发现并更正两处手抄错误，见 [transcription-corrections.csv](transcription-corrections.csv)。

## 全量读取完成（限定清单）

**26/26 个不同路径，237,155 bytes**；按下列分组逐项记录路径、大小与哈希。数字是**文件路径数**，不是 26 份独立新原文；X02 五个分块与 X02 完整页重复，X01 是失败记录。

| 分组及回读清单 | 文件数 | bytes | 说明 |
|---|---:|---:|---|
| [r109/r110 既存比较](prior-round-read-inventory.csv) | 6 | 62,357 | [事前范围](prior-round-scope-before-read.csv)；含综合报告，混有少量停项概述，范围过宽已披露。 |
| [既存元数据补充](prior-round-extension-read-inventory.csv) | 4 | 4,191 | [事前范围](prior-round-extension-scope-before-read.csv)，用于避免视频／活动重复计数。 |
| [四份既有来源](comparison-extension-read-inventory.csv) | 4 | 59,332 | [事前范围](comparison-extension-scope-before-read.csv)；逐源完整回读，不修改原文件。 |
| [本轮首批来源／失败记录](external-read-inventory.csv) | 6 | 69,921 | [汇总回读前列范围](external-read-scope-before-consolidated-read.csv)；X02／X07 曾先读，不能称首次读取前列全。 |
| [ThinCe 补充来源](external-extension-read-inventory.csv) | 1 | 5,019 | [读取前列范围](external-extension-read-scope-before-read.csv)。 |
| [X02 五个块辅助文件](X02-chunk-read-inventory.csv) | 5 | 36,335 | [块级计划](X02-chunk-plan-after-first-two-results.csv)在头两块出现后建立；块已先读组装，且和整页重复。 |

旧报告和元数据的范围／读取在本轮分别预列。X02／X07 的局部顺序例外、Q10 原计划被覆盖、Q09 停项摘要、两处手抄修正，以及 Q23／Q24 的 CSV 字段纠正均详见 [scope-and-record-corrections.md](scope-and-record-corrections.md)。哈希不证明抓取或访问顺序，不证明远端文字／原 HTML 与人工转存完全一致，也不证明设备功能、认证或履约。

**另行安全复验，不计入上述 26 个来源／比较路径**：[3/3 元数据清单](safety-metadata-recheck-read-inventory.csv)完整解析、609,109 bytes；[32/32 原有保护副本](protected-variants-recheck-read-inventory.csv)按事前路径列单后仅哈希字节、17,473,261 bytes，没有显示或解释内容。两份安全清单表头曾先查看，随后再建全量复验范围并完整解析，见偏差记录。三项合计为 61 个不同路径、18,319,525 bytes，但其中 32 项是字节哈希而非正文阅读，不能称作 61 个来源。868 个 stash 条目与 HEAD 中原位／保护副本的 blob 和 mode 均逐条复核。

## 检索、可追溯性和相对上轮的差异

- [Q01–Q28 每次查询的元数据](search-discovery/)逐条保存；查询分别记录在 [最初计划](discovery-plan-before-search.csv)、[补充计划](discovery-extension-plan-before-search.csv)、[活动与视频计划](discovery-video-event-plan-before-search.csv)、[登记计划](discovery-registration-plan-before-search.csv)、[组织者与登记计划](discovery-organizer-registry-plan-before-search.csv)。共有 **98 个非空结果行**、5 个查询无可见结果；结果含重复／无关／隔离项，只是手工结果元数据，不是原始搜索 JSON，也不能据零结果证明不存在。Q10 的原计划事后补记而非事前原字节副本。
- [来源目录](source-catalog.csv)含 12 个来源／状态条目（6 个本轮成功、1 个失败、1 个未取、4 个旧来源），[35 个逐字片段与本地行锚](evidence-traceability.csv)，[14 个声明边界](claim-boundaries.csv)，[10 个具名增补或纠正](issues-and-corrections.csv)。片段只在本地转存文件内准确，不证明原站字节或转写正确。
- **增补 r109**：V02 与 E01／E02 本轮重试得到文本，不追溯抹去 r109 的失败。**限定旧 `50` 和 r107**：尚不能确定首次海关出口年份，也不能给无日期出口帖赋邻帖日期。**相对 r110**：由历史软件文档转向企业公开叙述和活动页；r110 的版本、兼容性及搜索归属警示保持不变。
- [单调计时](timing-check.json)在整理中记录从入场起 1,685.799 秒；包含操作和思考，不证明连续键盘工作，未用睡眠充数。入场路径／原字节保护见 [68-entry-safety](../68-entry-safety-r111-2026-10-26/)；868 项入场范围中 836 与远端相同、32 与已有保护副本相同，本地 stash 已核但不能假设跨环境持久。

[主报告](../01-text-verbatim/workstation/08-customer-pipeline/180-angora-commercial-history-evidence-r111-2026-10-26.md) · [档案附录](../01-text-verbatim/workstation/09-orders/120-angora-orders-dossier-2026-10-21.r111-appendix.md) · [映射](../01-text-verbatim/workstation/09-orders/120-angora-orders-master-2026-10-21.mapping-r111.md) · [审计](../71-audit-r111-2026-10-26.md)。
