# IETF 镜像 2021-10-20 父子比较计划

对先前 GitHub commit API `G50` 所报父 `ae9ceebec6bf7a4034e6c8d6768e13b7f4f95883`／子 `fe367b60547788ed755be66dbec17e819f63c77c` 的两份完整原文件运行 `git diff --no-index --text --unified=3`，保存完整 stdout、stderr、退出码及哈希；与 commit API 该文件的 patch 对照。核验先读的全部字节、blob、精确数字和名称行，而不是凭 API patch 单独断言。

顺便将 IETF 父文件与 rfinnie 2021-10-20 文件做完整逐字节相等比较；将 IETF 2021-10-22 与 rfinnie 2021-10-27 文件做同样比较。保留各自原路径和文件，**不合并或以相同文本声称不同数据来源独立**。时间是 Git 镜像 commit 自报时间；文件首部的 `last updated 2021-10-20` 是整个列表更新日期，不能单凭它确定具体编号的分配日或交易。
