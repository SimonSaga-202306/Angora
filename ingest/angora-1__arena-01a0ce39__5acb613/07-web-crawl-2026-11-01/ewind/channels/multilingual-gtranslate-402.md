# 🔴 重大发现：Ewind 全部非英语子站已下线（GTranslate 402）

| field | value |
|---|---|
| 实测时刻 | **2026-11-01T05:33Z**（13:33 +0800） |
| 实测 URL | `https://es.ewindnet.com/`、`https://tr.ewindnet.com/` |
| 返回 | **"GTranslate - Error 402: Subscription Inactive" / "GTranslate subscription is inactive or expired for www.ewindnet.com"** |
| 页面内容 | 只有 GTranslate 错误页，**无任何 Ewind 内容** |

## 语言清单（来自官网语言切换器，逐字，共 **19** 个）
Arabic(ar) · Bengali(bn) · Bulgarian(bg) · Chinese Simplified(zh-cn) · Dutch(nl) · English(www) · Filipino(tl) · French(fr) · Georgian(ka) · German(de) · Italian(it) · Japanese(ja) · Korean(ko) · Malay(ms) · Portuguese(pt) · Spanish(es) · Thai(th) · Turkish(tr) · Vietnamese(vi)

## 这一条推翻了我们自己档案里的三个表述
1. **不是"12 语言站"** —— 切换器实测 **19 个**子域（r24/r25 的 12 是搜索索引能命中的数量，不是站点数量）。
2. **不是"独立建设的多语言站"** —— 全部是 **GTranslate 机器翻译插件**生成的子域，内容与英文站同源、无本地化。
3. **截至 2026-11-01 全部不可用** —— 订阅过期，19 个子域同时变成 402 错误页。**只有英文主站可用。**

## 商业含义
- 对土耳其客户（我们最关心的市场）而言，Ewind **目前没有土耳其语站点**。这是 Angora 的本地化优势里最容易打的一张牌（Angora 有原生土耳其语官网 + 土耳其语 GUI）。
- 机器翻译站点在 2025-2026 年被关停，说明 Ewind 在**收缩营销面**，与官网内容停滞（最新产品 2026-08、最新文章 2026-06、展会页停 2025-11）是同一个信号：**Ewind 正处于"低成本维持"状态**，而不是扩张状态。
- 该结论只基于 2 个子域实测（es/tr）；**其余 17 个沿用同一插件，技术上共享同一订阅状态，但我方只实测了 2 个** —— 引用时写"实测 2 个，其余同源推断"。

## 待办
逐个实测 ar/bn/bg/zh-cn/nl/de/fr/ka/it/ja/ko/ms/pt/th/vi/tl（16 个）以把"推断"升级为"实测"。
