# Angora Synapse 宣传册（/download/1797/）—— 首次读到正文

| field | value |
|---|---|
| URL | https://www.angoranetworks.com/download/1797/ |
| capture | 2026-11-01T05:31Z，PDF 正文（1 分块 = 全文） |
| 与 r39 对比 | r39 只记录路径 → **首次入库** |

## 相对网页新增的能力清单（网页没有的）
- **VLAN**：4K Active VLAN、**QinQ / Selective QinQ**、GVRP、Private VLAN、Voice VLAN
- **组播**：IGMP v1/v2/v3、Snooping、Fast Leave、MVR、IGMP Filter、**256 个组播组**
- **可靠性**：LACP（8 组 × 8 成员）、接口备份、**Jumbo 13K**、EAPS + ERPS、**ISSU 不中断升级**、**堆叠最多 16 台**、VRRP、UDLD
- **安全**：1024 条 L2/L3/L4 ACL、DAI + IP Source Guard、PPPoE+、802.1X、RADIUS、**TACACS+**、MD5/SHA-256/RSA-1024/AES256
- **管理**：Console/Telnet/SSHv1-2/HTTP/HTTPS/**SNMP v1/v2/v3**/**RMON**/TFTP/FTP/SFTP/NTP/**ZTP**/SPAN/**RSPAN**/**Dying gasp**/syslog
- **QoS**：CAR、HQoS、COS/DSCP/TOS、802.1P/DSCP 重标记、SP/WRR/SP+WRR、Tail-Drop、**WRED**、流监控与限速
- **SFP 配套 SKU（新）**：ANW-SFP-1G-SX（850nm/550m）、ANW-SFP-1G-LX（1310nm/10km）、ANW-SFP-10G-SR（850nm/550m）、ANW-SFP-10G-LR（1310nm/10km）

## 🔴 宣传册"订货信息"表有 3 行文案错误（Angora 自己的错，不是我们录错）
订单表把 **ANW-2712-24T4X / 48T4X / 48T6X** 三个型号的 Description 全部写成
> "**8-Port** Gigabit RJ45 + 4-Port 10G SFP+ …"

而同一份 PDF 的规格表写的是 **24 / 48 / 48 口**。同一页自相矛盾。
→ 含义：Angora 的宣传册在做**文案复用没校对**。招标时若客户拿 Angora 的订货页来压价，可直接指出其 24/48 口型号的官方描述是 8 口 —— 这是**可以用作谈判点的事实**（不是推测）。
→ 另一处：型号名 `ANW-2712-24T4X` = 24 口 + **4**×10G；`48T6X` = 48 口 + 6×10G，与规格表一致；只有描述错。

## 定位语（原文摘要，非译文）
"From industrial edges to enterprise aggregation switches, there is a SYNAPSE switch for each application." —— 注意这句把 Synapse 也说成覆盖工业边缘，与 r39 网页的"企业级"定位**不一致**；且工作温度 −10/+60 °C 不支持工业场景。以规格表为准。
