# RFP/Saga Software Function List-release 7.3.0.xlsx

> 原始文件：`RFP/Saga Software Function List-release 7.3.0.xlsx`

## 原文表格

```

--- sheet: Saga software function ---
Switch Specification | Marvell 
AlleyCat 3 series | Marvell 
AlleyCat 5 series | Remark
Ethernet interface | Port features | Support IEEE 802.3x Flow Control | P | P
Support Interface Counters | P | P
SupportJumbo Frame, maxium:10222bytes | P | P
Port aggregation | Support GE Port Aggregaiton | P | P
Support 10GE Port Aggregation | P | P
Support Static Aggregation | P | P
Support LACP Dynamic Aggragation | P | P
Aggregation Groups creation supported number | 64 | 64
Number of Each Aggregation Group Members | 8 | 8
Switching features | VLAN | IEEE 802.1Q Tagged VLAN | P | P
MAC-based VLAN | P | P
IP-based VLAN | P | P
Protocol-based VLAN | P | P
VLAN Range | 1-4094 | 1-4094
Mac- address Table | Support Static Mac-address Management | P | P
Support Dynamic Mac-address Management | P | P
Support Filtering Mac-address | P | P
Support Mac-address Limit based on port and VLAN | P | P
Support Mac-address Flapping based on Port or VLAN | P | P
Mac-address Table Size | 16k | 16k
GVRP | Normal Mode | P | P
Fixed Mode | P | P
Forbidden Mode | P | P
QinQ | Support Port-based QinQ | P | P
Support VLAN-based QinQ | P | P
Support VLAN-Mapping | P | P
Support Flow-based QinQ | P | P
MSTP | Support 802.1D STP | P | P
Support 802.1W RSTP | P | P
Support 802.1S MSTP | P | P
Support BPDU Guard | P | P
Number of Single Ring Device Connections* Suggested | 20 | 20
ERPS（G.8032) | Support Major Ring | P | P
Support linking the Sub Ring and other Rings | P | P
Recovery Time | 20ms | 20ms
Number of Single Ring Device Connections* Suggested | 20 | 20
Storm Suppression | Speed Limited basing on port bandwidth percentage | P | P
Support broadcast storm suppression(broadcast; unknown multicast; unknown unicast) | P | P
SPAN | Supported Number of Sessions | 7 | 7
Support Many-to-One Mode | P | P
RSPAN | Remote Port mirroring(Remote Switch Port Analyzer) | P | P
LLDP | Link Layer Discovery Protocol | P | P
Port isolation | Isolate Groups supported number | 1 | 1
IP Routing | Static Routing | Support VLAN Interface（SVI） and Route Port | P | P
Support IPv4 Static Routing Table Entry Configuration | P | P
Support ARP Dynamic Learning and Static Configuration | P | P
Support IPv6 Static Routing Table Entry Configuration | P | P
Support IPv6 Neighbor Discovery and Static Configuration | P | P
Routing Prefix Table Size For IPv4, for IPv6 Divide by 4 | 256 | 768
RIP | Routing Information Protocol | P | P | L3 only
OSPFv2 | Open Shortest Path First | P | P | L3 only
IS-IS | Intermediate System-to-Intermediate System | P | P | L3 only
BGP4 | Border Gateway Protocol V4 | P | P | L3 only
ECMP | Equal Cost Multi Path | P | P | L3 only
DHCP | DHCPv4 Client | Dynamic Host Configuration Protocol, For IPv4 | P | P
DHCPv6 Client | Dynamic Host Configuration Protocol For IPv6 | P | P
DHCPv4 Snooping | Support DHCP Snooping Trust Port | P | P
Support DHCP Snooping Option-82 | P | P
Support DHCP Snooping Circuit-id and Remote-id Customized | P | P
DHCPv4 Server | DHCP Server,  For IPv4 | P | P
Quality of Service | QoS | Support QoS Class, Remarking | P | P
Support SP, WRR Queue Scheduling | P | P
Ingress Port-based Rate-limit | P | P
Egress Port-based Rate-limit | P | P
Policy-based QoS | P | P
Port Queue Numbers | 8 | 8
Multicast | IGMP Snooping | Internet Group Management Protocol Snooping | P | P
Multicast Table Size | 1k | 1k
Security functions | ACL | Support IP Standard ACL | P | P
Support IP Extended ACL | P | P
Support Mac ACL | P | P
Support IPv6 ACL | P | P
Supporting ACL  application on VLAN | P | P
Maximum number of ACL Entrys, Include Input and Output | 240 | 480
Port Security | Support Port Security | P | P
IP Source Gurad | Support IP Source Guard, Port-based IP/Mac Binding Access | P | P
ARP Check | ARP Check(ARP packet filtering) | P | P
Ddos | Ddos Attack Protection | P | P
Dot1x | Port Access Control | P | P
Mac-address Access Control | P | P
RADIUS Server | P | P
AAA | RADIUS Authentication Access Switch | P | P
TACACS Authentication Access Switch | P | P
Authorization | P | P
reliability | Loop Detect | Based on Port or VLAN | P | P
VRRP | Virtual Router Redundancy Protocol | P | P | L3 only
Management &
Monitoring | Dual Stack | IPv4 and IPv6 Dual Stack Management | P | P
Syslog Management | Syslog Level 7 to 0, Corresponding Debug, Info, Notice, Warning, Err, Critical, Alert | P | P
Supports Connecting up to 3 Servers | P | P
For IPv4 and IPv6 | P | P
User management | Support Authentication by Password Protection | P | P
Support Local Management of User Privilege | P | P
Remote Authorization by RADIUS or TARCAS | P | P
Support User Privilege Level 0 to 15 | P | P
Login Service Management | Up to 8 Users Online Simultaneously by vty | P | P
Access Control Based on IPv4 or IPv6 ACL | P | P
Device firmware management | Support Firmware Upgrade by WEB | P | P
Support Firmware Upgrade by CLI | P | P
Support Dual Partition | P | P
Web Management | Web Management | P | P
Support HTTP V1.1 | P | P
Support HTTPS | O | P
For IPv4 and IPv6 | P | P
failure detection | Ping and Tracerout, For IPv4 and IPv6 | P | P
Support Dying-gasp | P | P
Support Optical-DDM | P | P
Support One Click Fault Information Collection | P | P
Support Cable Detect | P | P
NTP | For IPv4 and IPv6 | P | P
Configuration import/export | Remote Configuration import/export by FTP/TFTP) | P | P
Local Configuration Import/export by USB | P | P
sFLOW | Sampled Flow | P | P
SNMP | Supporting Version(SNMP V2C/V3) | P | P
RMON | RMON | P | P
Application Protocol
 Features | PoE | Support PD Alive Detect | P | P
Support PoE Port Power Feeding Priority management | P | P
Support PoE Port Power Limit | P | P
Support PoE Power Alarm threshold settings | P | P
Support PoE Reseve Power settings | P | P
Support PoE Legacy Mode | P | P
IEEE 802.3af, IEEE 802.3at, IEEE 802.3bt | P | P
Telnet Server | Support Telnet Server, For IPv4 and IPv6 | P | P
Telnet Client | Support Telnet Client, For IPv4 and IPv6 | P | P
SSH Server | Support SSH2 , for IPv4 and IPv6 | P | P
```