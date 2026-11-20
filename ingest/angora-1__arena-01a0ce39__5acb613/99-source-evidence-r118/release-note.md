# r118 最终校验说明

- [本地限定范围重跑](local-verification-rerun-result.json)：83/83 路径、370,711 bytes、18 项结构与关联检查、89 个相对链接存在。首次检查因 README 被误改和前向链接缺目标而失败，原 stdout／stderr／退出码及错误版本均保留；正确链接修复与另版计划文件创建后重跑通过。
- [ledger 单元测试](ledger-tests.stderr.bin)：34 项通过，退出码见 [记录](ledger-tests.exit.json)。这些测试不验证外站真实性、原始 HTML 或人工转录无误。
- 最终资料入账后 [快照](../../../constitution/snapshots/70b53f356d3045649b4567ac5d7cf112/) 与 [验证输出](release-ledger-verify.stdout.bin)：188 条记录、189 载荷、377 基线文件，成功；其中 1 条先前抓取失败有日志。该快照固定至本轮提交后才具可复核 Git 锚，不覆盖其后用户/助手消息。
- 第一次提交检查点 `6a16683411eaea4a05d58fb09f16a68997b04ba9` 与当时远端一致；最终提交／推送及暂存比较另见 `final-stage-verification.json` 和 `final-push-observation.json`（后者若尚不存在则尚未记录，不能预断成功）。
- 48 次搜索有 19 次保护性删节，人工文本没有自动逐字对照原协议；四次页面请求失败，P04 页面跨块漂移，原始 HTML、协会 PDF、官方工商原证等未取得。[完整问题](issues-and-corrections.md)。
