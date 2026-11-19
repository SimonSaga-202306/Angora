# r110：两份可见转存的重建计划（执行前）

`fetch_page` 对 AR02（2024 英文 TACACS）和 AR06（2025 英文堆叠）各返回两个完整工具分块；但本地 shell 无法直接接收工具返回对象。肉眼比对后，主体文字与分别对应的 AR01、AR05 可见转存一致；快照工具栏日期、链接时间戳和相关文章列表不同。为了避免手抄大量重复文字中的遗漏，将利用 AR01/AR05 的单独转存做模板，按这两次工具返回逐项替换：时间戳、日期表、AR02 多出的页面标题、相关文章列表。输出仍是每个快照一个独立文件，绝不覆盖模板。

- 输入：`archive-replay/.../tacacs-authentication-with-cisco-ise/20210227205859/index.visible.md` → `archive-replay-reconstructed/.../tacacs-authentication-with-cisco-ise/20240530151345/index.visible.md`。
- 输入：`archive-replay/.../stacking/20220118063431/index.visible.md` → `archive-replay-reconstructed/.../stacking/20250211043846/index.visible.md`。
- **等级限制**：两份输出是有明确模板来源的人工/脚本重建，不是原始 HTML，不证明与网页或工具输出逐字节一致，也不是独立证人；无法程序化比对当前工具响应对象。任何未注意到的细微差异可能被模板遮蔽。定量结论和精确引文优先依据分别直抄的 AR01/AR03/AR05/AR08/AR09/AR10，AR02/AR06 仅辅助识别页面外观和时间线，不能用于宣称跨快照逐字相同。
- 图片、CSS 和 HTML 原件没有取得；重建只含工具显示文字与链接。生成脚本逐项替换并断言模板边界，后续清单标记为 reconstructed。
