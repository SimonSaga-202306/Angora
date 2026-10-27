# Angora **Verge** — 国产交换机主线（2026-10-27 复核）

## 页面身份（本轮发现的一个实际问题）
同一家族**两套页面**并存，内容不一致：

| 页面 | id | published | modified | 说明 |
|---|---|---|---|---|
| `/network-devices/`「Network Switch Ailesi」 | 1775 | 2025-06-11T13:12 | 2025-06-11T13:31 | 正文写 VERGE，规格表 + 型号编码全表（2025-06 版） |
| `/verge-network-switch-serisi/`「Verge Yerli Network Switch Ailesi」 | 298 | 2021-01-01T16:13 | **2026-04-03T07:51:44** | 更晚被维护，但 r39 抓取时返回的是同一套 VERGE 文案 |

⚠ **引用时写明你读的是哪一页。** 两页都挂同样的宣传册（/download/425/ 工业、/download/428/ 8-24-48 口），但 `/network-devices/` 的行文中有一句"Layer 2/2+/3 → 降至 Layer 2+"的降级表述（2026-09-23 镜像已记），page 298 上未必同步。

## 型号编码全表（2026-09-23 镜像逐字，r39 抓取一致）
| 系列 | 编码 |
|---|---|
| 工业 8 口 | ANW-1104-TG / -PG / -PX；ANW-1108-TG / -TX / -PG / -PX（7 个） |
| 企业级 8 口 | ANW-2108-TG / -TX（2 个） |
| 8/24/48 口 | ANW-2208 / 2224 / 2248 (-TG / -TX)（6 个） |
| 数据中心 / TOR | 2420-24、3224-RCF、4124X-6Z、2420-48、3248-RCF、4148X-6Z、2520-32Q、3232-RSE、4432Z-2TX-100/400、2520-48、3248-RSE、4224Y-8Z（12 个） |
| **合计** | **27 个** |

## 规格要点
- 工业 8 口：8×1G + 2/4×1/10G SFP+，DIN 导轨，**−40 … +80 °C**，48 V DC，PoE+ 全口 30 W。
- 企业 8 口：8×1G + 2×1/10G SFP+，**180 W AC**，19" 1U。
- 8/24/48 口：**380 W AC**，2/4×1/10G SFP+。
- DC/TOR：**3.6 Tbps**、6× 100G QSFP28、冗余热插拔电源。
- 特性集：VLAN/QoS/MSTP/LACP/Ring/EEE/GVRP/LLDP/802.1X/PoE+/堆叠/告警继电器/IPv6/组播/静态路由；高阶加 OTP、LISP、VXLAN、MC-LAG、BGP6、REST API、MPLS、RSVP、L3VPN、VRF。
- 管理：标准 CLI、Angora 管理平台、SNMP、REST API。

## 命名空间（可用来自动归类任何招标文件里的散型号）
- `ANW-10xx` = **Hitit**（边缘/工业）
- `ANW-11xx / 21xx / 22xx` = **Verge**
- `ANW-27xx / 57xx` = **Synapse**
- 纯数字 `2420-xx / 32xx / 41xx / 25xx / 42xx` = **DC/TOR**（Verge 表内）

三个家族、三块不重叠的号段 → 见到陌生 ANW 编号可先判家族再查档。
