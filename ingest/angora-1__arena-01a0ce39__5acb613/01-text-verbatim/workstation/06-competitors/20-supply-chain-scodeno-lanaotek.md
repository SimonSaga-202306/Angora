# 🔗 供应链全景：Scodeno → Lanaotek → Larch → Angora

> 2026-09-23 · 信息来源：**用户直接提供**（本人亲述，Levent 亦向其确认过部分）
> 本文件修正了 `10-supplier-competitor-dossiers.md` 中对 Larch 的定位

---

## ⚠️ 重要修正

上一版我把 **Larch Networks 判断为"最危险的对手"** —— **这是错的**。

按用户提供的链条，Larch 只是**买货的一方**，它的工业交换机硬件来自 Lanaotek，
Lanaotek 背后是 Scodeno，而 **Scodeno 老板刘念 与 SmartByte 老板刘情 是亲兄弟**，
**SmartByte 正是我方的供货方（用户是贸易商，从 SmartByte 采购）**。

> **所以整条链是"自家人的货绕了一圈卖给了 Angora"。**

---

## 一、完整链条图

```
【兄弟公司 / 工厂层】
   Scodeno（刘念） ═══ 亲兄弟 ═══ SmartByte（刘情）
   en.scodeno.com                 smartbyte-switch.com
   ├─ 网管工业交换机 Series 7 / 8  ║  ├─ 我方（Saga / Simon）的供货来源
   ├─ 非网管工业交换机             ║  └─ 用户（贸易商）从这里采购
   ├─ Aestra 系列（2025-12 新）
   ├─ XBLUE 系列
   ├─ BYPASS 系列
   └─ M12 交换机系列
        │
        │  （Lanaotek 同时也卖 SmartByte 的部分产品，两兄弟的货互相串）
        ▼
【贸易层】
   Lanaotek / Lanao Communication Technology Limited（品牌 "Lanbras"）
   lanaotek.com  ·  sales@lanaotek.com  ·  +86-13631637180  ·  +86-755-8465-6994
   —— 贸易商，从多家工厂进货
        │
        ▼
【海外品牌 / 软件层】
   Larch Networks（以色列，Rosh Ha'ayin）
   —— 买入 Lanaotek 的硬件，叠加 Marvell 软件（ROS / OpenROS / SONiC）与品牌
        │
        ▼
【终端品牌】
   Angora Networks（土耳其安卡拉）
   —— 贴 ANW-xxxx 牌，卖给土耳其政府/运营商（EGM、TT、KGM…）
```

---

## 二、各环节档案

### 2.1 Scodeno（工厂 · 刘念）

| 项 | 内容 |
|---|---|
| 官网 | https://en.scodeno.com/ |
| 产品页 | https://en.scodeno.com/product_list_8.html |
| 主力 | **网管型工业交换机 Series 7 与 Series 8**，DIN 导轨与机架式两种形态 |
| 网络层次 | 覆盖 **L2 / L2+ / L3** —— 从接入、汇聚到核心的端到端组网 |
| 其他系列 | 非网管工业交换机（`product_list_5`）、**Aestra 系列**（`product_list_222`，2025-12 上新）、**XBLUE 系列**（`product_list_17`）、**BYPASS 系列**（`product_list_83`）、**M12 交换机系列**（`product_list_84`） |
| 分类 | 工业核心交换机 / 工业汇聚交换机 / 工业接入交换机 |
| 卖点 | 丰富的安全协议与稳健安全策略 |
| 网站语言 | 英文站（另有中文站） |

> **Aestra 系列 2025-12 上新** —— 时间点值得注意：Angora 在 **2026-04** 改版 VERGE，
> **2025-08/09** Larch 才把 Angora 挂上官网客户页。**节奏吻合。**

### 2.2 Lanaotek（贸易商 · 品牌 "Lanbras"）

| 项 | 内容 |
|---|---|
| 主体 | **Lanao Communication Technology Limited** |
| 官网 | https://www.lanaotek.com/ |
| 品牌 | 站内出现 "Explore **Lanbras**" —— 自有品牌名 |
| 邮箱 | sales@lanaotek.com |
| 电话 | +86-13631637180 / +86-755-8465-6994 |
| 语言站 | 英 / 法 / 西 / 俄 / 葡 / 阿 / 德 —— **7 语种，出口导向极强** |
| 社媒 | VK（vk.com/lanaotek） |
| 定位 | "leading network supplier… providing enterprise customers and end-users professional ICT products and solutions" |

**产品目录（极宽，典型贸易商结构）：**

| 大类 | 细类 |
|---|---|
| 数据中心交换机 | **Broadcom** 数据中心交换机 / **Marvell** 数据中心交换机 / **Centec** 数据中心交换机 |
| 企业交换机 | 可堆叠网管 / 热插拔网管 / **L2+/L3 网管** |
| **工业交换机** | **DIN 导轨 L2/L3 网管** / 机架式 L2/L3 网管 / DIN 导轨非网管 / OEO 转换器 / DIN 导轨 Web Smart / 交换机电源 |
| 接入交换机 | **太阳能 PoE 交换机** / **AI PoE 交换机** / 桌面型 / 光收发器与配件 / 网管型 / **云管理** |
| 一体化网络 | IoT 智能箱 / 太阳能智能箱 / 户外 PoE 交换机箱 / IoT 网关 / 工业路由器 / IoT 智慧灯杆 |
| **光模块与线缆** | 400G/200G、100G/40G/25G/10G、6G/2.5G/1G/155M、转换模块、**DAC/AOC 线缆**、GPON STICK/PON 模块 |

**解决方案**：互联网数据中心、企业网络、5G 网络、智慧城市、可再生能源、视频监控、FTTx。

> **注意：Lanaotek 明确有「Centec 数据中心交换机」这一分类。**
> 我方在 2026-08-17 的回复中提出用 **CENTEC** 承接 L3 —— **这条货 Lanaotek 手里就有。**

### 2.3 Lanaotek 上有 SmartByte 的产品（用户提供的铁证）

用户给的链接：
https://www.lanaotek.com/products/24xge-rj45-4x10g-sfp-support-di-do-and-rs485-port-1-4-support-bt-90w/

对应型号 **IDSL3M-04X24GHP-SU-L** —— 这是 **SmartByte 的型号**。

规格（从 URL 可读出）：24×GE RJ45 + 4×10G SFP，支持 **DI/DO 与 RS485**，1-4 口支持 **BT 90W**。

> **含义**：Lanaotek 同时卖 SmartByte 与 Scodeno 的货，**兄弟俩的渠道是打通的**。
> 用户说的"比较错综复杂"即指此。

### 2.4 Larch Networks（以色列 · 品牌/软件层）

见 `10-supplier-competitor-dossiers.md` 第一节。**修正其定位：**

| 原判断 | 修正后 |
|---|---|
| ❌ Larch 是"最危险的对手" | ✅ **Larch 是硬件的下游买家 + 软件加值方**。它的工业交换机硬件购自 Lanaotek（→ Scodeno） |
| ❌ Larch 会抢我方的 L3 生意 | ✅ Larch 提供的是 **Marvell ROS / OpenROS / SONiC / IP Infusion OcNOS 软件层**，硬件不是它造的 |

> **仍然成立的判断**：Angora 要 L3，**可以绕开我方直接从 Larch 拿软件**。
> 但**硬件仍要过 Lanaotek / Scodeno 这一关** —— 而我方（SmartByte 系）在这一层**有血缘关系**。

---

## 三、🎯 战略含义（对 Saga / 用户）

1. **我方在 Angora 供应链里不是"外人"，是"同一族谱的另一支"。**
   Angora 当前买的工业交换机硬件，源头是 Scodeno；而我方从 SmartByte 拿货 —— **两家是兄弟工厂**。

2. **这意味着：我方完全有能力提供同级别、甚至同源的硬件。**
   被"替换"的原因**大概率不是技术能力不足，而是**：
   - 价格 / 账期 / 交期竞争；
   - Angora 想**分散供应链**（Volza 显示 15 家供应商，本身就在多源采购）；
   - Larch 能提供**我方拒做的 L3 软件层**。

3. **最直接的破局点**：
   - 通过 **SmartByte（刘情）** 这条血缘，摸清 **Scodeno（刘念）** 给 Lanaotek 的**具体型号与价格**；
   - 再比对 Angora 新版 VERGE / HITIT 的规格，确认**是不是同一批货**；
   - 若是同一批货 → 我方可以用**同源硬件 + 我方报价**正面竞争。

4. **Lanaotek 有 Centec 数据中心交换机** —— 我方 8 月推的 CENTEC 方案，
   **Lanaotek 手上就有货**。这是现成的对照样本。

5. **Larch 与我方（Saga）接触过** —— 用户指出见 main 分支的 Gmail 邮件。
   ⚠️ **在仓库 6 个 Gmail PDF 的文本层中没有检索到 "Larch"**，
   需用户指出具体是哪一封（或在未解压的 `INFO_2025.12.17/INFO.rar` 里）。

---

## 四、待办

| # | 动作 | 价值 |
|---|---|---|
| 1 | 请用户指出 **Larch 联系我方** 的那封邮件 | 还原 Larch 与我方的接触史 |
| 2 | 抓取 Lanaotek **DIN 导轨 L2/L3 网管交换机**全系列型号，与 Angora VERGE/HITIT 逐项比对 | 定位 Angora 硬件源头 |
| 3 | 抓取 Scodeno **Series 7/8** 型号表 | 同上 |
| 4 | 通过 SmartByte 侧面了解 Lanaotek 的出货型号 | 血缘渠道，最快 |
| 5 | 比对 Larch 工业交换机页与 Lanaotek 产品页的**规格/图片是否一致** | 证实"Larch 硬件=Lanaotek" |
