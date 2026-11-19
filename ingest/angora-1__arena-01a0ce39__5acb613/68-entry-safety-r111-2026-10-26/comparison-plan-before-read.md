# r111 入场保护：比较与后续计划（读取文件字节之前）

1. `incoming-scope-before-read.csv` 已先列出入场时 868 条原相对路径、状态与字节大小。本轮新增的本目录不属于这 868 条，不加入待 stash 路径。
2. 仅读取预列文件的完整字节以计算 SHA-256 与 Git blob SHA-1，不展示、不解释其中的商业或已 PASS 内容；将每条结果与 `FETCH_HEAD` 的同路径 Git tree 元数据比较。
3. 对每个不同或远端不存在的文件，先核对远端 r109 `60-entry-safety-r109-2026-10-26/untracked-variants/original-paths/` 下对应的受保护副本的 Git blob；若不一致或没有对应副本，先以原相对路径在本目录的 `untracked-variants/original-paths/` 下单独复制并逐字节核验，绝不合并或覆盖。
4. 在逐项保护完成、写出指定路径的 stash 计划后，才可对**这 868 条精确路径**执行一次包含未跟踪文件的本地 stash；比较 stash 第三父树与入场 Git blob。stash 是本地备份，不保证跨环境或远端保留，不 pop。确认已安全保护后当前分支仅快进到已抓取的远端 HEAD。
5. 安全检查和散列不代表研究、重新跟进或重新解释已 PASS 的底层资料。环境 UTC 与给定会话日期冲突，只记录观察；本轮耗时另用同一宿主机 monotonic 估计。
