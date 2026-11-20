# AR03 · 归档目标身份不符，隔离

预列请求为 `https://web.archive.org/web/20220814180044/https://support.angoranetworks.com/?ht_kb=layer-2-technologies-rate-limit-and-storm-control`。CDX 对原请求给出一条 `200`／`text/html` 记录，但 `fetch_page` 的最终 URL 转到归档内另一无关域名的 `20220814173338` 回放，显示该抓取时的 HTTP 302／再跳转提示，而非目标 Angora 支持正文。工具自动返回了这份无关归档页；没有主动打开页面内跳转目标、执行程序或采用其内容。

保留独立人工转存及索引以证明目标不符，标为**隔离、非 Angora 内容、不可作为技术事实**。不得由 CDX 状态 200、搜索结果的创建日期或无关页推断 2019 文档的内容、网站被入侵或现状。人工转存未经工具响应逐字自动校验；本地 SHA 只锁保存文件。
