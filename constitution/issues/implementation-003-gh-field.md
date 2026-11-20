# 实施问题 003：查询仓库可见性时使用了不支持的 gh 字段（重置后重建）

重置前为评估对话公开风险，尝试 `gh repo view --json nameWithOwner,visibility,isPrivate`；本机 gh 返回退出 1：`Unknown JSON field: "visibility"`，并列出可用字段。这是本地参数错误，不是认证失败。随后改用 `nameWithOwner,isPrivate,url`，返回 `SimonSaga-202306/Angora` 且 `isPrivate: false`；用户在知情后明确选择 `publish_all`。

上述为根据当前仍可见工具输出重建的情况；当时独立保存的原始 stderr／stdout 随重置消失，不得假称已恢复。后续如重新查询，其原始输出应另存为新的请求，不混同之前结果。
