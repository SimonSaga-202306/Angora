# EW-S57948QM 数据表（PDF 正文，r39 只有路径）

| field | value |
|---|---|
| URL | https://www.ewindnet.com/wp-content/uploads/file/20260511/1778492053344125.pdf |
| 上传目录日期 | 20260511（与产品 id 10573 的发布日 2026-05-11 一致） |
| capture | 2026-11-01T05:31Z，PDF 正文（1 个分块，完整） |
| 与 r39 对比 | r39 只记录了路径未下载 → **本轮首次入库**；正文与产品页规格表**大部分一致，但有 3 处新信息 + 1 处硬冲突** |

## 首页原文（逐字关键句）
> "**EW-S57948QM 48 Ports 5G L3 Managed Switch with 100G SFP**"
> "**48*2.5/5GE + 4*100G SFP Ports**"
> "48*2500/5000M RJ45 + 4*40G/100G SFP++ slot Managed Ethernet Switch"
> "Support QOS, STP/RSTP, IGMP, DHCP, SNMP, WEB, VLAN, ERPS etc.;"
> "**3 years warranty.**"　"RoHS FCC"（CE 字样排版粘连为 "FCCE"）

产品介绍段：
> "…supporting **48 port 5GE access ports and 25GE/100GE high-speed uplink ports**."

## 规格表（逐字）
| 项 | 值 |
|---|---|
| Fixed Port | 48×2500/5000 Base-T + **4×4000/10000 Base-X** |
| Console / MGMT | 1 / 1 |
| Switching capacity | 1280 Gbps |
| Forwarding rate | 952 Mpps |
| 工作温度 / 存储 | 0–40 °C / −40–70 °C |
| 工作湿度 / 存储 | 10–90 % RH（非凝露）/ 5–90 % RH |
| 尺寸 | 440×300×44 mm |
| 电源 | AC 100–240 V, 50/60 Hz |
| 功耗 / 重量 | 150 W / 7 kg |
| 防雷 | 6 KV |
| MAC 表 | 112 K |
| Jumbo | 12 K |
| 转发模式 | Store-and-forward |
| 路由 | Inter-VLAN、多 IP、默认路由、静态、RIPv1/v2、OSPF、**BGP** |
| IPv6 | Ping / Tracert / Telnet / TFTP / ICMP |
| 组播 | IGMP v1/v2、Snooping v1/v2、**IGMP Proxy** |
| DHCP | Server / Client / Relay / Snooping |
| 安全 | 802.1X（本地+远程）、Portal、Radius、MAC 过滤、环路检测、端口隔离、ARP 绑定/代理、**anti-DDoS / SYN Flood / UDP Flood** |
| 管理 | CLI(Console/Telnet/SSHv1-2)、Web HTTP/HTTPS、SNMP v1/v2、LLDP、NTP v1/2、Syslog、FTP/TFTP 升级 |
| 包装清单 | 主机 ×1、挂耳 ×1 对、用户手册 ×1、保修卡 ×1 |

## 🔴 硬冲突：标题说 100G，规格表写 10G
- 标题 / 首屏 / 介绍段：**4×100G SFP**、25GE/100GE 上联、"SFP++ slot"。
- 规格表 "Fixed Port" 行：**4×4000/10000 Base-X**（即 4×10G）。
- 同一份 PDF 内部自相矛盾。**采购判断**：以规格表为准（10G），标题的 100G 是复用兄弟型号（10564 = 48×10G+4×100G、10557 = 24×10G+4×100G）文案时没改干净。
- 旁证：1280 Gbps / 952 Mpps 与"48×2.5G + 4×10G"完全吻合（48×2.5×2 + 4×10×2 = 240+80 → 但按 5G 口算 48×5×2+4×100×2=1280 也对得上）—— **两条算术都能凑出 1280，因此产能数字无法用来判定**。⚠ 这点必须写清楚，不能拿交换容量当证据。

## 相对产品页（r39）新增的三条
1. **3 年质保**写进数据表（网页未提）。
2. **IPv6 只列 5 条基础命令**（Ping/Tracert/Telnet/TFTP/ICMP），**没有 IPv6 路由协议**（无 OSPFv3/RIPng）—— 与 Angora Synapse 的 IPv6 全栈形成明显差距。
3. SNMP 只到 **v1/v2**（无 v3）、无 RMON、无 TACACS+、无 ISSU/堆叠 —— 对标 Angora Synapse 的 SNMPv3/RMON/TACACS+/16 台堆叠，**Ewind 的"L3"是轻量 L3**。
