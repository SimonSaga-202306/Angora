# 操作指南：逐条、可验证地留存

## 先读与范围

根目录 [`AGENTS.md`](../AGENTS.md) 是仓库级代理指引；六条各在 `rules/` 独立文件。只对用户可见且已授权的材料工作；系统内部信息、凭据、无权资料、已关闭应用和既有 PASS 不因“全量”而获得授权。公开仓库与用户的明确选择见 [`policies/publication-consent.md`](policies/publication-consent.md)。自动工具不能判断所有来源的授权、是否含隐私或秘密：提交前仍须人工核查，绝不上传凭据。

每条用户消息和助手消息单独保存；改动另建记录并关联旧 ID；不用一个汇总文本替代多条消息。原始用户消息保存于 `inbox/` 供阅读，对应 byte-copy 与元数据保存在 `records/messages/<id>/`。其他来源在 `records/sources/<id>/files/<原始相对路径>`，问题／变化在 `records/events/<id>/`；每次请求在单独的 `records/crawls/<id>/`。UUID 是本地记录 ID，不是平台消息 ID。相同输入会创建不同记录，不去重。

## 逐消息、逐来源和变化

以下命令各接收**一条消息或一个文件**；把示例路径换成实际路径。`--method` 应准确选择 `manual_transcription`、`platform_visible_copy`、`platform_export`、`tool_visible_transcription` 或 `supplied_file`；不把普通复制说成已核验的原始协议字节。

```sh
python3 tools/constitution_ledger.py message --file path/to/one-message.txt --role user --method platform_visible_copy --note '来源与限制'
python3 tools/constitution_ledger.py message --file path/to/one-assistant-message.txt --role assistant --method manual_transcription --note '精确发送时刻未知'
python3 tools/constitution_ledger.py source --file path/to/source.bin --original-path original/folder/source.bin --method supplied_file --note '逐字节复制提供的文件'
python3 tools/constitution_ledger.py event --file path/to/one-issue.md --event-kind issue --method supplied_file --note '一次问题，单独记录'
```

路径也可用 `--file -` 从标准输入接收**单个**输入；不能先拼接多条消息再输入。若用户主动修改一条，保留旧记录，并在新记录加 `--supersedes <旧记录ID>`；只能指向同类型、已存在的记录。每次保存复制实际输入字节并记录大小、SHA-256、方法、观察时间；若读取失败，保存可取得的部分与 `failure.txt`，并返回非零状态。

`--event-at` 只用于已知且有来源的准确事件时间，必须同时提供 `--event-time-source user|platform|tool|document`，时间必须带明确 UTC 偏移，例如 `--event-at '2026-01-01T00:00:00+08:00' --event-time-source user`。程序另外保存转换后的北京时间和未改写的来源时间；无法获得消息收发时间就省略参数，元数据为 `null`。`recorded_at_beijing_unverified` 是本机墙钟观察而非已校准真实时间，不得倒填为消息发生时间。

## 每次抓取及失败

检查用户授权、既有 PASS 和隐私限制后，才可为一次具体请求运行：

```sh
python3 tools/constitution_ledger.py fetch --url 'https://example.org/path/file.bin' --authorization-note '说明此具体请求为何获准'
```

每次 GET 新建记录；即使 HTTP 4xx/5xx、重定向或传输失败也保存已获取的数据、解析头和 `failure.txt`，返回码 2 不表示记录不存在。默认**不跟随重定向**：逐次审查并另行保存每个获准请求。正文为 HTTP 客户端交出的实体字节，不是包括分块帧的原始网络包；解析头也不是原始头字节。`Set-Cookie` 等敏感头和含疑似凭据的 Location 被遮挡，疑似凭据 URL 会被拒绝且不存 URL；此规则只覆盖常见形式，不能保证任意正文或头部不含秘密。

默认保存上限 16 MiB；`--max-bytes` 可调整至最多 64 MiB。超过时保留已读取的前缀及一字节探针、记作不完整并向用户说明。更大材料要选择已获授权、符合仓库大小及外部存储约定的方式；不要为了声称完整而突破平台或 Git 限制。`fetch_page`/搜索工具的可见文字、手工转录、二进制原件各自独立存放并说明保真度；不支持的格式不是丢弃理由。

## 交叉校验与重置

```sh
python3 tools/constitution_ledger.py snapshot
python3 tools/constitution_ledger.py verify --snapshot <snapshot-id>
python3 tools/test_constitution_ledger.py
python3 tools/constitution_ledger.py recovery-plan
```

快照**先列范围后读字节**，覆盖当时 `records/` 中的记录内容和元数据；不覆盖所有仓库文件、不自动覆盖其后新增记录。`verify` 检查每条记录的必需载荷、失败文件、字节数/哈希、意外文件及快照是否缺失或变化；新增记录另行检查并列为新文件。只靠一份可被同时改写的元数据和快照不能证明防篡改：应将快照提交并固定在可信 Git 历史或独立存储。哈希不证明网页真实性、来源独立、未见消息或绝对无遗漏。

重置先运行只读 `recovery-plan` 并观察当前分支和状态；跟踪引用可能过时，忽略文件不在默认检查。先列出所有相关路径并完整读取，比较并保护未提交数据（含不同路径同字节的副本），再获取当前分支的最新远端；必要时对明确路径选择性 stash，并逐个核第三父树 blob。stash 本身可能随重置消失，不能是唯一备份。确认基线且不会覆盖任何资料后才可 `git merge --ff-only`；分叉、不明差异、缺乏安全备份先停并问。不得盲目 `git clean`、`reset --hard`、`stash pop/drop`。提交当前分支后核 `git ls-remote`；本轮实际保护记录见 `ingest/.../96-entry-safety-privacy-reset/`。

## 人和平台仍须完成的事

代理每轮必须主动逐消息执行；这个脚本无法订阅 Arena 聊天、读取未显示的历史或获取平台原始收发时间。早期对话无法从摘要恢复，用户可以提供逐条导出以补录。复杂任务先估量和拆解，持续做实质工作、分阶段验证，不用睡眠凑时间；最终明确给出未能入库的材料和检查边界。
