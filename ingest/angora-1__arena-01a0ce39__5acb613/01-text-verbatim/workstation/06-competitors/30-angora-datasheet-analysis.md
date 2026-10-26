# Angora 官方宣传册 PDF 分析（任务 ②）

> 2026-09-23 · 来源：旧站下载直链，**PDF 已成功解析**

## 已获取

| 文件 | 直链 | 状态 |
|---|---|---|
| **工业交换机数据表** `Angora-Datasheet-Endustriyel` | https://www.angoranetworks.com/download/425/ | ✅ **已解析**，共 **4 段**，本轮读取第 1 段 |
| 8/24/48 口交换机宣传册 | https://www.angoranetworks.com/download/428/ | ⏳ 未读（下一轮） |
| 宣传册目录页 | https://www.angoranetworks.com/brosurler/ | ⏳ 未读 |

> **建议用户自行下载**：PDF 里含有**产品渲染图与规格表**，是做图片反搜 / 与 Lanaotek、Scodeno、
> Ewind 目录比对的最佳原始素材。

---

## 🔴 从工业数据表挖到的关键信息

### 1. 型号命名的真相

PDF 标题为 **"Verge 2023 Endüstriyel Ethernet Anahtarları"**（VERGE 2023 工业以太网交换机）。

> **→ 这解释了 2026 新版型号 `ANW-2023-E8GT`、`ANW-2023-8G/24G/48G` 里的 "2023"：**
> **不是"2023 年发布"，而是这一代产品家族的代号就叫 "Verge 2023"。**
> 也就是说 **VERGE 这一代在 2023 年就已定型**，2026-04 只是把它的型号从
> 我方供的 `ANW-11xx/22xx` 换成了 `ANW-2023-*` / `ANW-IND-*` / `ANW-GORDION`。

### 2. ⚠️ Angora 公开宣称"软件 100% 自研，不依赖外部来源"

PDF 原文（土耳其语）：

> **"Angora OS**
> Verge anahtarlarında çalışan işletim sistemi ve üzerindeki tüm işlemler,
> **Angora Networks tarafından birleştirilmiştir**. …
> Tüm yazılımsal geliştirmeler, **harici bir kaynağa ihtiyaç duymadan**,
> **tamamen Angora Networks imkanları ile yapılmakta** ve müşterilerin ihtiyaçlarına
> uygun zamanlarda teslim edilmektedir."

翻译：**"Verge 交换机上运行的操作系统及其上的所有操作，均由 Angora Networks 整合完成……
所有软件开发**无需任何外部来源**，**完全依靠 Angora Networks 自身能力**完成。"**

> **⚠️ 重大矛盾**：Larch Networks 把 Angora 挂在自己的 **Clients 客户页**（2025-09 上传），
> 而 Angora 对外宣称软件全自研、不依赖外部。
> **两种可能**：
> ① 这份 PDF 是 2023 年版，早于 Angora–Larch 合作（Larch 挂 Angora 是 2025-08），此时说法属实；
> ② Angora 在**对外宣传上刻意淡化 Larch**，以维持"100% 国产自主"的政府项目形象。
>
> **无论哪种，这都是一个可以利用的杠杆**：Angora 要保"国产自主"人设，
> 就意味着**它不能公开承认用 Larch/OcNOS** —— 这反过来给了**不透明的供应商（如我方）空间**。

### 3. 硬件规格线索（可用于芯片反查）

- **"65/40 纳米技术的新一代 ASIC"** + **"低功耗高性能 ARM CPU"**
- 端口：**8 个固定千兆电口 + 4 个 10G 光骨干口**
- 支持 **IEEE 802.3az** 能效以太网、Link Down 自动断电

> 65/40nm ASIC + ARM CPU 的组合，指向 **Marvell Prestera 家族**（Larch 官网恰好有
> "Fastboot for Marvell Prestera Family" 服务页）。
> **与"Larch 提供 Marvell 参考设计"的说法吻合。**

### 4. 软件功能清单（数据表宣称）

**安全**：IEEE 802.1X 端口安全 + Web 认证、动态 ARP 检测、IP 源保护、DHCP Snooping、
ND Inspection、RA Guard、DHCP6 保护、邻居绑定完整性检查、IPv6 首设备安全、
**内嵌 SSL 加密**、大容量 ACL、**访客 VLAN**、**基于时间的 ACL 与端口设置**、
基于 MAC 的移动用户安全、**私有 VLAN**、风暴抑制、
**RADIUS / TACACS+ / 本地数据库**认证、DoS 防护。

**管理**：**全土耳其语图形界面（tamamı Türkçe grafik ara yüzü）**、
CLI、智能物理接口（自动识别并配置安全/QoS）、SNMP、**REST API\***。

**三层**：**静态三层路由（Statik 3. Katman yönlendirme）\*** —— 注意带星号，
与 REST API 一样是"\*"标注项，通常表示"部分型号支持"或"后续版本支持"。

**IPv6**：支持 MacOS / Windows 8 / 10 / Linux 环境下的 IPv6 过渡。

> **含义**：Angora 数据表上**只写静态路由**，没有 OSPF/BGP/VRRP/MPLS/VRF。
> 也就是说 **VERGE 家族至今仍是 L2+ / 静态 L3** —— 与我方 8 月拒绝的动态路由 L3 不是同一档。
> **Levent 要的企业级 L3 功能，VERGE 家族给不了。**

### 5. PDF 头部出现的奇怪字样

`SECTOR HPE DURMAX` —— 出现在首页顶部，疑为**模板占位文字未清理**，
或某个行业客户的标注。**建议下载原 PDF 人工确认**（可能泄露文档来源/模板供应商）。

---

## 任务 ③：Larch 案例页 —— 没有 Angora

https://larch-networks.com/category/case-studies/ 共 **5 个案例**：

| 日期 | 案例 |
|---|---|
| 2026-02-05 | Hardware-Accelerated BFD+ for SONiC |
| 2025-08-27 | Aviation Authentication System For Aircraft Internal Network（机载内网认证） |
| 2025-07-01 | 帮助客户从单一厂商专有系统迁移到 SAI 解耦架构 |
| 2025-06-05 | 恶劣天气导致无线链路视频流中断（传输速率变化） |
| 2024-07-18 | OpenROS 用于同轴电缆通信 |

> ### 结论
> **Larch 的案例页上没有 Angora。**
> Angora 只出现在 Larch 的**首页合作墙**与 **Clients 客户页**（均为图片 logo，无文字案例）。
> **说明 Angora–Larch 的合作深度有限，或双方约定不公开。**
> 结合 Angora 数据表宣称"软件全自研不依赖外部"——**更像是刻意不公开**。

---

## 待办

| # | 动作 |
|---|---|
| 1 | 读取 PDF 剩余 3 段（含规格表与产品图） |
| 2 | 下载并解析 `download/428/`（8/24/48 口宣传册） |
| 3 | 读取 `/brosurler/` 页面，列出**全部**宣传册直链（可能还有更多 PDF） |
| 4 | 用 PDF 里的产品图做 **Google Images / TinEye 反搜**，比对我方、Lanaotek、Scodeno、Ewind 目录 |
| 5 | 人工确认 PDF 头部 "SECTOR HPE DURMAX" 含义 |
