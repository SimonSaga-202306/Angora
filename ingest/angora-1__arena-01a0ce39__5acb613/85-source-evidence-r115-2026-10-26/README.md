# r115 来源、范围与审计入口

本目录单独保存发现计划、选择性查询元数据、按 URL／回放日期分开的工具可见文字、索引、失败和漂移记录。每个页面或分块独立文件，**不得拼接**，也不将同源页面／回放当成独立见证。由人工转存：不声称 byte-identical 原始 HTML、原工具响应或远端文件，手工转录错误可能存在；SHA-256 只证明本地文件之后未变。

## 交付与目录

- [主报告](../01-text-verbatim/workstation/08-customer-pipeline/184-angora-institutional-partnership-evidence-r115-2026-10-26.md)、[独立档案附录](../01-text-verbatim/workstation/09-orders/120-angora-orders-dossier-2026-10-21.r115-appendix.md)、[映射](../01-text-verbatim/workstation/09-orders/120-angora-orders-master-2026-10-21.mapping-r115.md)、[单主体备忘](../86-followup-angora-r115-2026-10-26/angora-networks.md)、[审计](../87-audit-r115-2026-10-26.md)。
- [基础来源块／失败／索引目录](source-catalog.csv) 25 行、[补充目录](source-catalog-extension.csv) 3 行；一行是一个保存块或状态，并非一个独立证人。[取文结果](fetch-outcomes.csv)、[补充结果](fetch-outcomes-extension.csv)分别记录完成、失败、跳转、分块、局部发现。P01 索引只抓 16 块之一，单独隔离，仅为寻找 P07 的发现过程，不用于正文事实；P07 是完整单篇工具可见块。
- [证据锚](evidence-traceability.csv) 18 项、[补充锚](evidence-traceability-extension.csv) 8 项；[选定文字对比](selected-comparison-result.json)、[伙伴方补充对比](selected-comparison-extension-result.json)均仅核本地选定句，不证原网页字节或独立性。
- e-Safe 候选 AR01 和赛后 AR02 各保存 2/2 返回块；P10 保存 2/2 块；E01 保存 2/2 发现索引块，**绝不合并或拼接**。空 CDX 仅表示该查询过滤条件未返回记录，不能证明历史上不存在。P04 404；P06 跳到通用新闻，P09 跳到另一人帖子；保留结果并禁止作原目标证据。
- [P02、P03、P10 初稿](transcription-drafts/)与各自 correction-plan／before／result 文件保留。三处人工误写分别修复一项；单次替换通过仅说明本地两版差异受控，不排除其他错漏。

## 搜索与完整读取的精确范围

先列 [Q01–Q24](search-plan-before-search.csv) 和逐批 [增补计划](search-plan-extension-before-search.csv)，再执行 Q01–Q108；[每个查询一个元数据文件](search-discovery/)，人工记录 431 条结果（含重复）及 4 个零结果。**仅保留每次查询、结果计数和少量选定 URL；全部搜索结果与摘要未完整持久化**，因此不能重演整个结果列表，计数亦为人工转记、不等于独立来源数；网页事实只从另外保存的目标页面和回放使用。

分三批先列范围后完整按字节读取：旧轮 [13/13、95,096 bytes](prior-round-read-summary.json)；本轮 [127/127、169,015 bytes](source-read-summary.json)；补充 [19/19、27,454 bytes](extension-read-summary.json)。**全量读取完成（限定本地清单）：159/159 不同路径、291,565 bytes，159/159 UTF-8。** 路径、字节和本地 SHA-256 分见三个 inventory 及 [合计](combined-read-summary.json)。它们包括搜索元数据、索引、失败、漂移、重复来源块和初稿，不表示所有网页完整或 159 个独立来源。P01 远端仅取第 1 块，已明确排除；未知工具响应的其他文本不能由摘要替代。

首次旧轮预列误写 r105 文件名，留下 12 条初稿；在旧资料读取之前另列正确 13 条，见 [纠错](prior-scope-correction.md)。用户已 PASS 的主档正文、隔离 PDF 和停止访问的关于页不在阅读清单；主档如有追加，仅核原字节前缀并加索引，不解析旧内容。

## 日期、入场安全与边界

[日期口径](date-and-session-boundaries.md)：会话给定 2026-10-26 UTC，沙箱墙钟观察到 2026-11-20 UTC 且未校准；两者分开，不能回填采集日。回放捕获时间、网页自标日期、活动日期与页面当前动态内容分别表述。10-29 结果晚于会话日，未打开或用于本轮结论。[路径核验](path-resolution-observed.json)确认两份入场计划确实在仓库路径而非 `/home/user/ingest/`。

本轮入场保护 868 个原未跟踪路径、46,015,150 bytes：836 与远端原路径、32 与远端具名保护异版匹配；选择性本地 stash 后逐项核第三父树，再 ff-only 快进。证据在 [84 入场目录](../84-entry-safety-r115-2026-10-26/)；stash 仅保证本环境，不 pop。保留所有事前清单和纠正，不 reset／clean、切分支或全量暂存。计时见 [checkpoint](timing-checkpoint.json)：同 boot 的后段超过 10 分钟，含阅读、分析与等待。

不打开官网 PDF、INFO.rar、评论验证码或隔离文件，不处理旧财务差异、未成交／未付款旧单、仓库旧 RFQ/RFP；不联系停项主体、C 档不跟进；不操作设备、不使用关闭的 Gmail／Drive。无新增 Ewind 事实。证据不能升级为认证、实测、采购、交易或履约。
