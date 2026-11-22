# 对话宪法与逐条入库

**修正／取代临时检查点说明**：六条规则、逐项记录工具及重置后的测试现已重建。检查点 `adec2a0` 的原 README 逐字节保存在 [`history/README-checkpoint-adec2a0.md`](history/README-checkpoint-adec2a0.md)，不静默丢弃旧版。

## 六条规则

1. [逐件入库，禁止擅自合并对话](rules/01-no-merging.md)
2. [用户信息、变化和北京时间](rules/02-message-time-version.md)
3. [交叉检查、抽检和其他核验](rules/03-verification.md)
4. [资料、不可读文件与问题](rules/04-sources-and-failures.md)
5. [沙箱重置与远端保护](rules/05-sandbox-recovery.md)
6. [复杂任务评估、拆解与持续工作](rules/06-complex-work.md)

## 入口

- [操作指南](OPERATING-GUIDE.md)／[仓库级代理指引](../AGENTS.md)／[现有停项与权限边界](policies/preexisting-boundaries.md)。
- [本轮用户请求](inbox/user-messages/constitution-request-0001.txt) 与 [公开选择](inbox/user-messages/privacy-answer-0002.json) 是两条独立记录；[公开仓库及用户决定](policies/publication-consent.md)。
- [各消息与版本](records/messages/)／[逐源文件](records/sources/)／[问题与变化](records/events/)／[每次抓取](records/crawls/)／[记录快照](snapshots/)。
- [最新 34 项本地测试原 stderr](audit/rebuilt-test-02.stderr.bin)／[结果](audit/rebuilt-test-02.result.json)；[此前 31 项测试](audit/rebuilt-test-01.result.json)及[符号链接缺口首次失败](audit/symlink-gap-before-fix.result.json)保留；[北京时区参考和时间分歧](issues/clock-disagreement-and-r117.md)及 [r118 新观察与承接摘要的分歧](issues/continuation-date-disagreement-r118.md)；[重置保护](../ingest/angora-1__arena-01a0ce39__5acb613/96-entry-safety-privacy-reset/)。
- [用户选择恢复研究](issues/continuation-resumes-research-r118.md)，不解除既有停项；本页变更前版本逐字节保存在 [`history/README-before-r118-7ce342a.md`](history/README-before-r118-7ce342a.md)。
- **r119 最新限定**：[时间观察和截止口径更正](issues/r119-time-observations-and-scope.md)／[应用状态与隐私范围变化](issues/r119-application-state-and-scope.md)；本页更新前逐字节版本为 [`history/README-before-r119-82891bd.md`](history/README-before-r119-82891bd.md)。

## 诚实边界

本轮请求是人工转存并在重置后根据可见调用重建的文本，不是已验证的平台传输原始字节；实际收发时间未知。更早不可见的对话无法从摘要还原，脚本也无法自动订阅未来消息。time.is 原始 HTML 未取得；重置前部分工具输出和测试进程原始日志丢失，后续观察与测试独立保存。[详细缺口](issues/unavailable-history-and-platform-limits.md)。

用户已在知情后允许逐条公开对话，但凭据、未经授权来源、关闭应用及已有 PASS 不因许可而开放；文件含敏感信息时仍须按权限处理。哈希与测试只能验证限定范围，不能证明绝对无遗漏或所有来源真实。
