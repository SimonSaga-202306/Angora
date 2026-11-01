# Angora Verge **Kurumsal（企业）** 宣传册（/download/428/）—— 首次读到正文（chunk 0–2）

| field | value |
|---|---|
| URL | https://www.angoranetworks.com/download/428/ |
| 文档内自述 | "**Verge 2023** Kurumsal Ethernet Anahtarları" |
| capture | 2026-11-01T05:32–05:36Z，PDF 4 分块，本轮取 0–2（规格/RFC/MIB 主体已覆盖，chunk3 订购信息未取） |
| 与 r39 对比 | 首次入库 |

## 相对网页新增
- 端口规模原文：**"8, 24, 32 veya 48 adet sabit gigabit"** —— **32 口**这一档在网页型号表里没有对应编码（网页是 8/24/48）。→ 疑似 24×GE + 4×Combo 的整机 28/32 口口径混用，**待核**。
- L3 能力：**"Statik, RIP*, OSPF* yönlendirme"**（工业册只写 Static）→ **企业册承认 RIP/OSPF**，与 Synapse 的 L3-lite 定位衔接。
- **MAC 表 16,384**、**ARP 8,000**。
- RFC 清单（逐个列出的就有 50+ 条，含 RFC 1213/1493/1643/1757/2674/2863 等标准 MIB），**SNMP v1/v2c/v3 + USM**，RMON 4 组（历史/统计/告警/事件）。
- **sFlow 与 telemetry 应用**（原文 "Sflow desteği, RESTAPI, telemetri uygulamaları"）—— 网页只提 REST API。
- **USGv6 与 IPv6 Gold Logo 认证**（原文 "USGv6 ve IPv6 Altın Logo sertifikası"）—— 这是可核的第三方认证主张，价值高于一般营销语。
- 支持 SFP 类型：1000BaseSX/LX/ZX/T、10GBaseSR/LR/ZR/ER。
- DHCP 选项 12/66/67/82/129/150；远程端口镜像（RSPAN）；多镜像会话（双会话，8 源口 → 1 目的口）；VLAN 镜像。
- 节能细节：短于 10 m 的线缆自动降信号、可关闭端口 LED、Link-Down 断电。
- 管理/运维：双镜像、脚本化 CLI、用户分级 1–15、Xmodem 升级、线缆检测、BOOTP/SNTP、**零接触自动配置**（安全拷贝自动拉配置）。
- 同样提出 **Angora OS 自主**与**全土耳其语 GUI**。

## 与 425（工业册）的三处口径差异（必须分开引用）
| 项 | 425 工业册 | 428 企业册 |
|---|---|---|
| L3 | 仅"Statik 3. Katman*" | "Statik, RIP*, OSPF*" |
| Jumbo | 9,216 B | 9,216 B（一致） |
| 32 口 | 无 | **有（"8, 24, 32 veya 48"）** |

## 边界
- chunk 3（订购信息/型号编码表）未取；**因此本册给出的型号编码仍待补**。
