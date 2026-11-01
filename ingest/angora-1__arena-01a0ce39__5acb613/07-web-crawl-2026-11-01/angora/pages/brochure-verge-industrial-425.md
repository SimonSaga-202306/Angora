# Angora Verge **Endüstriyel** 宣传册（/download/425/）—— 首次读到正文（chunk 0–1）

| field | value |
|---|---|
| URL | https://www.angoranetworks.com/download/425/ |
| 文档内自述 | "**Verge 2023** Endüstriyel Ethernet Anahtarları" |
| capture | 2026-11-01T05:33–05:34Z，PDF 4 分块，本轮取 0–1（规格表主体已覆盖） |
| 与 r39 对比 | 首次入库 |

## ⭐ 新型号编码（官网型号表里**没有**）
规格表里唯一的型号是 **`ANW-2023-E8GT`**：
| 指标 | 值 |
|---|---|
| 转发率 | **48.1 Mpps**（64 字节包口径） |
| 交换容量 | **56 Gbps** |
| RAM / Flash | **512 MB / 128 MB** |
| 端口 | 8× 固定千兆铜 + 4× 10G 光纤上联 |
| VLAN | **4096** 并发；端口/802.1Q/MAC/管理/私有/访客/未授权 VLAN；Radius 动态 VLAN |
| 端口聚合 | 802.3ad LACP，**最多 8 组 × 每组 8 口**（宣传文中另写"32 个候选端口"） |
| Jumbo | **9,216 字节** |
| 生成树 | 802.1d / 802.1w（**8 实例**）/ 802.1s |
| 组播 | IGMP v1/v2/v3、Snooping、Querier、**1000 个组播组**、MVR |
| 三层 | 硬件全速转发、**最多 64 条静态路由**、CIDR、LAG/VLAN/loopback 三层接口、VRRP |
| 安全 | 512 条 ACL、DAI、IPSG、DHCP Snooping、IP-MAC-Port 绑定、PVE、DoS 防护、RADIUS/TACACS+ |
| 缓冲 | **12 MB** |
| 环网 | **G.8032 ERPS**、UDLD |
| 节能 | 802.3az、链路断开断电、按线长调节信号 |
| 其他 | SSHv1/v2、SSL、Web 认证、STP BPDU/Root Guard、SCT（管理通道保护） |

> 与网页 `/network-devices/` 的 `ANW-1104-* / ANW-1108-*` 命名**完全不同**。这说明 "Verge 工业 8 口" 在同一代里存在**两套型号编码**（网页用 ANW-11xx，宣传册用 ANW-2023-E8GT）。**对投标文件认型号时必须两套都查**，否则会漏报。

## 定位与卖点（原文要点）
- "**Tamamı Türkçe grafik arayüz**"（**全土耳其语图形界面**）—— 这是 Angora 最硬的本地化差异点。
- **Angora OS**：原文声明交换机操作系统与上层功能**由 Angora 自主整合/开发**，"不依赖外部资源"，补丁与功能迭代自主完成。→ 这是我们对客户讲"本地研发"的可引用原话。
- 硬件叙事：**65/40 纳米 ASIC + 低功耗 ARM CPU**。
- 三层能力在工业册里写作 "**Statik** 3. Katman*"（带星号脚注），企业册（428）写 "Statik, RIP*, OSPF*" —— **同一家族的 L3 能力，两本册子口径不同**，工业册更保守。引用时按册子分开写。
- 安全特性清单（逐条）：802.1X + Web 认证、DAI/IPSG/DHCP Snooping、IPv6 首跳安全（RA Guard、DHCPv6 Guard、ND Inspection、Neighbor Binding Integrity）、SSL、ACL（含时间 ACL）、Guest VLAN、Private VLAN、风暴抑制、RADIUS/TACACS+/本地库、DoS 防护。

## 边界
- 本轮只读 chunk 0–1（共 4）；chunk 2–3 为 RFC 清单与订购信息尾部，**未读**。
- 该册未给工作温度、功耗、MTBF 数值（网页版给了 −40…+80 °C，**册子里查不到**）。
