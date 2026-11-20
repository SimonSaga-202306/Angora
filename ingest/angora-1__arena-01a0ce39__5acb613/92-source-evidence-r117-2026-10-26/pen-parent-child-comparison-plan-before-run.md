# 2021 PEN 镜像父子比较计划

镜像 commit `0829494816a42c337fe42e869ee9114b816a96ee` 的 API 指明父 commit `c99419cac238e3960c1942506514dd2f87df202b`；两次完整文件均已另存并与 Contents API 的 Git blob 和大小核对。先对这两个独立原文件执行 `git diff --no-index --text --unified=3`，完整 stdout、stderr、退出码和 SHA 单独保存；退出码 1 表示两文件不同，并非命令失败。对比 GitHub commit JSON 中同一路径的 API patch；若父子 blob、父 commit 或目标行不匹配，则停止相关结论。

只对所保存的两版字节、Git commit 元数据与文件首部的 `last updated` 字段陈述；不将镜像更新时刻或整份文件 last-updated 日期当作 IANA 对某个编号的精确分配时间。IETF 镜像与 rfinnie 镜像都可能源自同一 IANA 清单，不计成两个独立分配机构。PEN 不等于 MAC／设备实测／工商／交易。
