# Gordion 数据中心线 + Ewind 海关实测数据

> 2026-09-23

---

# 一、⭐ GORDION 数据中心交换机（完整规格）

来源：https://www.angoranetworks.com/download/1053/（Gordion 宣传册 PDF，已解析）

**宣传语**：「Türkiye'nin DC Switch'i」—— 土耳其的 DC 交换机
「Yerli Akıl, Küresel Teknoloji」（本土智慧，全球技术）
「Angora 数据中心系列，性能最高达 **12.5 Tbps**，超高速度与高密度的千兆交换机家族」
「Angora 交换机支持 **VXLAN、NVGRE 及可能的 VXLAN-GPE** 功能，基于 **Marvell 架构 + Intel 支持的硬件**；
**高级三层功能、VPLS、EVPN、高级路由与 MPLS 支持**，使其成为 DC 边缘路由的绝佳选择。」

| 特性 | 2520-48SFP25G-6SFP100G | 2520-32QSFP100G | 2520-32QSFP400G |
|---|---|---|---|
| **芯片组** | **Marvell 95EX 系列** | **Marvell 95EX 或 95CX 系列** | **Marvell 95CX 系列** |
| Flash | 16 GB | 64 GB | 64 GB |
| RAM | 8 GB | 16 GB | 16 GB |
| 总带宽 | **3.2 Tbps** | **6.4 Tbps** | **12.8 Tbps** |
| 风扇 | 4+1 热插拔 | 5+1 热插拔 | 5+1 热插拔 |
| 电源 | 520W 热插拔 | 1600W 热插拔 | 1600W 热插拔 |
| 尺寸 | 440×470×44mm（19" 1U） | 440×560×44mm | 440×560×44mm |
| 1/10/25GbE 接口 | 48 | — | — |
| 40/100 GbE 接口 | 6 | 32 | — |
| 400GbE 接口 | — | — | 32 |
| 说明 | 48×25G 下行 + 6×100G 上行，**双电源、双风扇、AngoraOS** | 32×100G 口，双电源、双风扇 | 32×400G 口，双电源、双风扇 |

## 🔴 解读

1. **Marvell 95EX / 95CX 是 Marvell Prestera 高端数据中心芯片** —— 直接坐实
   **Angora 的 DC 产品线 = Marvell 高端方案**，而 **Larch Networks 是 Marvell 认证方案提供商、
   且提供 "Fastboot for Marvell Prestera Family" 服务**。
   **→ Gordion 这条线通过 Larch 的可能性极高。**

2. **型号前缀 `2520-` 与 `/network-devices/` 表里 DC/TOR 那一栏的 `2520-48`、`2520-32Q` 完全对应。**
   即 2420 / 2520 / 3224 / 3248 / 3232 / 4124X / 4148X / 4224Y / 4432Z **都是 Gordion/DC 平台的原厂编号，
   没有 ANW 前缀** → 沿用外部平台型号。

3. **`2520-48SFP25G-6SFP100G`：48×25G + 6×100G，3.2 Tbps。**
   **→ 这与仓库里的数据中心 RFP（`ANW-DC-RFP-EN.pdf`：48×25G + 6×40/100G ≥3.6 Tbps MLAG）几乎完全一致。**
   说明 **Angora 拿 Gordion 2520-48SFP25G-6SFP100G（或类似平台）去应那个 DC 标**。

4. **12.8 Tbps / 32×400G** —— Angora 的产品线上限远超我方认知。
   **这不是一家"只会做 8 口工业机"的公司。** 我方在工业 8 口的竞争，
   与 Angora 在数据中心级产品上的野心，是两条不相交的赛道。

5. **对照 Karınca NPB**：48×10/25G + 6×100G、**1.9 Tbps**、Marvell 包处理器、16GB Flash / 8GB RAM。
   **Gordion 2520-48 是 3.2 Tbps、同样 16GB Flash / 8GB RAM** ——
   **两者硬件平台高度相似（同款 Marvell + 同款存储配置），很可能同源，只是软件/用途不同
   （一个做 NPB 分流，一个做 DC 交换）。**

---

# 二、Ewind 海关实测数据（ImportGenius 印度站，**未被墙**）

## 2.1 先回答问题：ImportGenius / Panjiva 到底能不能用？

**我实测了，结论如下：**

| 平台 | 土耳其数据 | 实测结果 |
|---|---|---|
| **ImportGenius** | ❌ **没有土耳其** | 直接访问 `https://www.importgenius.com/turkey/tradebase` → **404 "This page has been lost at sea!"** |
| **Panjiva** | ❌ **没有土耳其** | 维基百科明确列出其覆盖国：US、中国、墨西哥、巴西、玻利维亚、智利、哥伦比亚、厄瓜多尔、巴拿马、巴拉圭、秘鲁、乌拉圭、委内瑞拉 —— **无土耳其** |
| **ImportGenius 印度站** | ✅ **可用，且明细不付费也能看到** | 成功抓到 Ewind 10 条完整发货记录 |

> **也就是说：要看 Angora（土耳其进口方）的海关数据，ImportGenius 与 Panjiva 在结构上就无解。**
> 可用的是：**Volza（已被反爬墙）、TurkeyTradeData、TradeInt（宣称对土耳其有"独家"数据）、
> Tendata（宣称覆盖 228 国含土耳其）、Export Genius。**

## 2.2 Ewind 印度发货明细（ImportGenius 实测，共 35 票）

供应商：`EWIND TECHNOLOGY CO., LTD.`
数据区间：2007-01-02 ~ 2024-02-18
买家（3 家）：**DISCREET SOLUTIONS PRIVATE LIMITED**（Pune/Maharashtra）、KIAAN INTERNATIONAL、HASTI IMPEX

| # | 产品 | 型号 | 数量 | 到货日 |
|---|---|---|---|---|
| 1 | POE SWITCH 8FE PoE + 2GE 非网管 (120W) | **OT-1708PG** | **500 NOS** | 2023-12-29 |
| 2 | POE SWITCH 8FE PoE + 2FE 非网管 (96W) | **OT-1708P** | **1373 NOS** | 2023-12-29 |
| 3 | POE SWITCH 8GE PoE + 2GE 非网管 (120W) | **OT-1708PG-E** | 300 NOS | 2023-12-29 |
| 4 | 4 口交换机用变压器（配件） | OT-04 | 1320 NOS | 2023-12-29 |
| 5 | POE SWITCH 16GE PoE+2GE+1GF 非网管 (200W) | **OT-1716P** | 250 NOS | 2023-06-24 |
| 6 | POE SWITCH 24GE PoE+2GE+1GF 非网管 (300W) | **OT-1724P** | 200 NOS | 2023-05-13 |
| 7 | POE SWITCH 16GE PoE+2GE+1GF 非网管 (200W) | OT-1716P | 250 NOS | 2023-05-13 |
| 8 | POE SWITCH 8FE PoE+2FE 非网管 (96W) | OT-1708P | **1500 NOS** | 2023-04-25 |
| 9 | POE SWITCH 8FE PoE+2GE 非网管 (120W) | OT-1708PG | 300 NOS | 2023-04-25 |
| 10 | POE SWITCH 8GE PoE+2GE 非网管 (120W) | OT-1708PG-E | 300 NOS | 2023-04-25 |

HS Code：**85176290**
买家地址示例：DISCREET SOLUTIONS PRIVATE LIMITED, PLOT NO. 24, GATE NO. 25/26 PRADHAN PARK, LONAVALA PUNE/MAH

## 2.3 🔴 Ewind 的商业本质（重要）

**Ewind 走的是「大批量、非网管、PoE、CCTV/安防」路线：**
- 单票 1,373 台、1,500 台、500 台 —— **这是走量的生意**
- **全部是非网管（Unmanaged）PoE 交换机**
- 型号体系 `OT-17xxP/G`、`OT-04` —— 与 Saga 的 `STI-xxx`/`STC-xxx`、SmartByte 的 `IDSL3M-xxx` 完全不同
- 客户是印度的**分销商/进口商**（Discreet Solutions、Kiaan International、Hasti Impex），不是最终用户

> **→ Ewind 的强项是「低成本海量非网管 PoE」，不是「工业级网管 L2+/L3」。**
> 虽然它官网上列了 L3 网管 PoE、IP66/68、M12、Bypass 等，**但从真实海关出货看，
> 它实际大量交付的是非网管 PoE**。
>
> **→ 我方（Saga）的定位是「工业级网管 L2+/L3 + 宽温 + 定制（OEM/ODM）」，
> 与 Ewind 的主战场（走量非网管 PoE）并不完全重合。**
> 但 **Angora 的 HITIT 系列（ANW-10xx，入门级 PoE 边缘）恰恰落在 Ewind 的主战区** ——
> **HITIT 很可能就是 Ewind 供的。这是一个可验证的假设。**

## 2.4 关于"Ewind 与 Angora 的合作时间"

用户判断「Ewind 应该是 2024 年之前就合作了」，**证据支持这一判断**：

| 证据 | 说明 |
|---|---|
| Volza 样本提单 | 日期 **2023-11-08**，1 PCS，来自中国 |
| TurkeyTradeData | 统计窗口 **2023-08-01 ~ 2024-07-31**，21 票全部来自中国 |
| 我方订单 | 该窗口内我方只有 **STSC20240508007（2024-05-08，$1,265）** 一单 |
| 反推 | 该窗口内 Angora 的 21 票进口**基本不是我方**，主要来自 Ewind 等 |

> **→ Ewind 与 Angora 的合作，大概率在我方 2024-05 开始合作之前就已存在。**
> 用户的直觉是对的。

---

# 三、下一步（优先级）

| # | 动作 | 为什么 |
|---|---|---|
| 1 | 去 **TradeInt** 或 **Tendata** 试土耳其数据（宣称有土耳其"独家"数据） | 唯一可能绕开 Volza 反爬的路径 |
| 2 | 抓 **Gordion 宣传册** 剩余内容 + **Synapse 宣传册（download/1797/）** | 补齐 DC 与企业级规格 |
| 3 | 抓 **HITIT 页面（旧域 `/hitit-yerli-network-switch-ailesi/`）**，与 Ewind 目录逐型号比对 | 验证"HITIT = Ewind 白牌"假设 |
| 4 | 抓 **8-24-48 口宣传册（download/428/）** | 看 ANW-11xx/22xx 是否还在册 |
| 5 | 新域名 `angorateknoloji.com` 恢复后补抓 RU 页面与博客全文 | 完成镜像 100% |
