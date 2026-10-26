<!-- ============================================================ -->
<!-- FILE 297/781 -->
<!-- PATH: INFO_2025.12.17/Performance of VastLakes Platform_EN.pptx -->
<!-- SIZE: 105121 bytes -->
<!-- SHA256: 08ee6f0ea7d341efca6ecd5354f7d84f6ca4b66a17445b1f3e532fec10a3ee06 -->
<!-- EXTRACTION: python-pptx - every slide, every shape text, every table, notes -->
<!-- ============================================================ -->

Presentation: slides=9

## SLIDE 1
[shape 1 | TEXT_BOX (17) | 文本框 3]
SAGA TELECOM VASTLAKES PLATFORM PERFORMANCE
High Performance Switching Hardware Platform

[shape 2 | TEXT_BOX (17) | 文本框 6]
Platform Overview

[shape 3 | TEXT_BOX (17) | 文本框 7]
VastLakes platform is a purpose built device to address the challenge in the recent network evolution. VastLakes platform combines a feature-rich switch core and an embedded ARM A53 CPU Core running at 800MHz/1.2GHz. Platform supports a variety of port configurations, providing full-rate port capability from 100M to 100G

[shape 4 | TEXT_BOX (17) | 文本框 8]
Key Features of the VastLakes Platform

[shape 5 | TEXT_BOX (17) | 文本框 9]
Ethernet capabilities: MAC table, Vxlan, IPFIX, ACL, EVC etc.
Full set of Layer 2 and Layer 3 protocols
Rich OAM
Security feature set
Precision timing protocol

[table 6 rows=14 cols=3]
Type	Specification	Value
Ethernet Basic	　	　
Jumbo Frame	Maximum jumbo frame size	9600
Unicast MAC	MAC address capacity	Default profile: 98304
		Extended-buffer: 12288
		IPv6 profile: 98304
		Layer3 profile: 98304
	MAC learning rate(SW)	> 4000pps
	MAC learning rate(HW)	> 10Gbps
	Blackhole MAC address capacity	128
Multicast MAC	MAC address capacity	Default profile: 2048
		Extended-buffer: 1024
		IPv6 profile: 1024
		Layer3 profile: 1024

[shape 7 | TEXT_BOX (17) | 文本框 1]
Table 1: Performance of VastLakes Platform

[shape 8 | TEXT_BOX (17) | 文本框 17]
Performance of the VastLakes Platform


## SLIDE 2
[shape 1 | TEXT_BOX (17) | 文本框 1]
Table 1: Performance of VastLakes Platform(Continued)

[table 2 rows=28 cols=3]
Type	Specification	Value
Ethernet Basic	　	　
VLAN	VLAN IDs	4094
　	VLAN instances	4094
　	VLANs to enable statistics	256
VLAN Mapping	Maximum mapping table	64
　	Maximum rules number	1024
EVC	Maximum EVC number	4094
Link Aggregation(Static & LACP)	Maximum member number per group	No limitation
	Maximum Group Num	64
	Load balance key mode	Static/Dlb/RR/Resilient/Self-healing
	Convergence time	< 50ms
VLAN Classification	Maximum rule number	4096
	Maximum group number	1
	Base MAC capacity	512
	Base IPv4 capacity	448
	Base IPv6 capacity	32
	Base protocol capacity	7
Ethernet Ring Protection	　	　
STP	Convergence time	< 30s
RSTP	Convergence time	< 1s
MSTP	Instance number	64
	Convergence time	< 1s
ERPS	Domain number	16
	Ring number	1 Primary ring/domain
		2 Sub ring/domain
	Protection instance number per Ring	64
	Switchover time	< 50 ms


## SLIDE 3
[shape 1 | TEXT_BOX (17) | 文本框 1]
Table 1: Performance of VastLakes Platform(Continued)

[table 2 rows=39 cols=3]
Type	Specification	Value
Ethernet OAM	　	　
CFM(802.1ag)	Maximum session number	1024
	Maximum domain number	8
	CCM interval types	7
	CCM minimum interval	3.3ms
	Maximum down MEP number	1024
	Maximum up MEP number	1024
	Maximum LMEP number	1024
IPv4 Unicast	　	　
ARP	ARP capacity	Default profile: 12288
		Extended-buffer: 4096
		IPv6 profile: 6144
		Layer3 profile: 16384
IPv4	FIB	Default profile: 57344
		Extended-buffer: 28672
		IPv6 profile: 12288
		Layer3 profile: 57344
ECMP	ECMP group	240(Share with IPv6)
PBR	Policy route map	64
	Policy based routing ACE	256
OSPF	Maximum static neighbors	256
	Maximum summary address	2000
IPv4 Multicast	　	　
IPMC	Multicast routing table	Default profile: 2048
		Extended-buffer: 512
		IPv6 profile: 1024
		Layer3 profile: 2048
	Multicast routing downstream interfaces	Default profile: 4096
		Extended-buffer: 2048
		IPv6 profile: 2048
		Layer3 profile: 5120
IGMP Snooping	Maximum groups number	2048
	Maximum member number	N/A
MVR	Maximum group number	Default profile: 2048
		Extended-buffer: 2048(Share with IPv6)
		IPv6 profile: 1024
		Layer3 Profile: 2048
	Maximum member number	4096


## SLIDE 4
[shape 1 | TEXT_BOX (17) | 文本框 1]
Table 1: Performance of VastLakes Platform(Continued)

[table 2 rows=34 cols=3]
Type	Specification	Value
IPv6 Unicast	　	　
Host Route	NDP capacity	Default profile: 2048
		Extended-buffer: 1024
		IPv6 profile: 4096
		Layer3 profile: 0
IPv6	FIBv6	Default profile: 4096
		Extended-buffer: 1024
		IPv6 profile: 6144
		Layer3 profile: 0
	ECMP group	240(share with IPv4)
IPv6 Multicast	　	　
IPMC	Multicast routing table	Default profile: 256
		Extended-buffer: 256
		IPv6 profile: 512
		Layer3 profile: 0
	Number of interfaces that support	Default profile: 512
		Extended-buffer: 1536
		IPv6 profile: 1024
		Layer3 profile: 0
	Multicast routing table	Default profile: 512
		Extended-buffer: 1536
		IPv6 profile: 1024
		Layer3 profile: 0
MVR V6	Maximum entry number	Default profile: 256
		Extended-buffer: 2048(Share with IPv4)
		IPv6 profile: 512
		Layer3 profile: 0
	Maximum member number	Default profile: 512
		Extended-buffer: 4096
		IPv6 profile: 1024
		Layer3 profile: 0
IP tunnel	　	　
IP Tunnel	Tunnel peer capacity	8


## SLIDE 5
[shape 1 | TEXT_BOX (17) | 文本框 1]
Table 1: Performance of VastLakes Platform(Continued)

[table 2 rows=36 cols=3]
Type	Specification	Value
QoS	　	　
Per-port Queue Number	Unicast queue	10
	Multicast queue	10
	Monitor queue	10
Packet Buffer	System packet buffer capacity	Default profile: 4.5MByte
		Extended-buffer: 9MByte
		IPv6 profile: 4.5MByte
		Layer3 profile: 4.5MByte
Granularity	Policer granularity	0~2M: 10K
		2M~100M: 40K
		100M~1G: 80K
		1G~2G: 120K
		2G~4G: 250K
	Queue shape granularity	4G~10G: 500K
	Port shape granularity	10k
Flow Entry	Ingress port QoS ipv4 flow entries	1532
	Ingress port QoS ipv6 flow entries	1532
	Ingress port QoS flow statistics entries	511
ACL		
MAC ACL	Ingress port ACL for MAC	Default profile: 2926
		Extended-buffer: 2926
		IPv6 profile: 2926
		Layer3 profile: 2976
	Ingress VLAN ACL for MAC	Default profile: 2926
		Extended-buffer: 2926
		IPv6 profile: 2926
		Layer3 profile: 2976
	Egress port ACL for MAC	Default profile: 878
		Extended-buffer: 878
		IPv6 profile: 878
		Layer3 profile: 928
	Egress VLAN ACL for MAC	Default profile: 878
		Extended-buffer: 878
		IPv6 profile: 878
		Layer3 profile: 928


## SLIDE 6
[shape 1 | TEXT_BOX (17) | 文本框 1]
Table 1: Performance of VastLakes Platform(Continued)

[table 2 rows=40 cols=3]
Type	Specification	Value
ACL		
IPv4 ACL	Ingress Port ACL for IPv4	Default profile: 2926
		Extended-buffer: 2926
		IPv6 profile: 2926
		Layer3 profile: 2976
	Ingress VLAN ACL for IPv4	Default profile: 2926
		Extended-buffer: 2926
		IPv6 profile: 2926
		Layer3 profile: 2976
	Egress Port ACL for IPv4	Default profile: 878
		Extended-buffer: 878
		IPv6 profile: 878
		Layer3 profile: 928
	Egress VLAN ACL for IPv4	Default profile: 878
		Extended-buffer: 878
		IPv6 profile: 878
		Layer3 profile: 928
IPv6 ACL	Ingress Port ACL for IPv6	Default profile: 2926
		Extended-buffer: 2926
		IPv6 profile: 2926
		Layer3 profile: 2976
	Ingress VLAN ACL for IPv6	Default profile: 2926
		Extended-buffer: 2926
		IPv6 profile: 2926
		Layer3 profile: 2976
	Egress Port ACL for IPv6	Default profile: 878
		Extended-buffer: 878
		IPv6 profile: 878
		Layer3 profile: 928
	Egress VLAN ACL for IPv6	Default profile: 878
		Extended-buffer: 878
		IPv6 profile: 878
		Layer3 profile: 928
ACL Flow Statistics	Ingress ACL flow statistics entries	1022
	Egress ACL flow statistics entries	511
CoPP	CoPP rules	249
	CoPP flow statistics entries	249
UDF	UDF rules	256
	UDF flow stats entries	128


## SLIDE 7
[shape 1 | TEXT_BOX (17) | 文本框 1]
Table 1: Performance of VastLakes Platform(Continued)

[table 2 rows=20 cols=3]
Type	Specification	Value
Security	　	　
IP Source Guard	IPv4 maximum rules number	768
	IPv6 maximum rules number	64
802.1x Base MAC	Maximum entries	Default profile: 512
		Extended-buffer: 256
		IPv6 profile: 256
		Layer3 profile: 256
DHCP Snooping	Maximum bound entry	4096
IPFIX	　	　
IPFIX	IPFIX member	4096
Reliability	　	　
BFD	Maximum session number	Share 128
S-BFD	Maximum session number	Share 128
VRRP	Maximum group number	63
Smart Link	Maximum group number	16
	Maximum instance number	64
	Switchover time	<50ms
Monitor Link	Maximum group number	16
	Maximum up-link number per group	16


## SLIDE 8
[shape 1 | TEXT_BOX (17) | 文本框 4]
Version Information

[shape 2 | TEXT_BOX (17) | 文本框 1]
Product List Based on VastLakes Platform

[table 3 rows=11 cols=3]
Series	Model	Specification
STH-10G	STH-2C24XE-HSI	24*100M/1G/2.5G/5G/10G Multi-Gigabit Base-T 2*100G QSFP28 2*Hot-swappable Fan Modules and CRPS Modules
	STH-2C24XE-SFI	24*100M/1G/2.5G/5G/10G Multi-Gigabit Base-T 2*100G QSFP28 4*Fixed Fans, 1*Fixed Power Supply
	STH-2C24XP-HSI	24*100M/1G/2.5G/5G/10G Multi-Gigabit PoE++,  2*100G QSFP28 2*Hot-swappable Fan Modules and CRPS Modules
	STH-2C24XF-HSI	24*10G SFP+ 2*100G QSFP28 2*Hot-swappable Fan Modules and CRPS Modules
	STH-2C24XF-HSI	24*10G SFP+ 2*100G QSFP28 4*Fixed Fans, 1*Fixed Power Supply
	STH-8DX24XF-HSI	24*10G SFP+ 8*25G SFP28 2*Hot-swappable Fan Modules and CRPS Modules
	STH-8DX24XE-HSI	24*100M/1G/2.5G/5G/10G Multi-Gigabit Base-T 8*25G SFP28 2*Hot-swappable Fan Modules and CRPS Modules
	STH-8DX24XP-HSI	24*100M/1G/2.5G/5G/10G Multi-Gigabit PoE++,  8*25G SFP28 2*Hot-swappable Fan Modules and CRPS Modules
	STH-2QX8DX12XF8GF8GE-HSI	12*10G SFP+ 8*100M/1000M Base-T 8*1G SFP 8*25G SFP28 2*40G QSFP+ 2*Hot-swappable Fan Modules and CRPS Modules
	STH-2QX8DX12GF8GF8GE-SFI	12*10G SFP+ 8*100M/1000M Multi-Gigabit Base-T 8*1G SFP 8*25G SFP28 2*40G QSFP+ 4*Fixed Fans, 1*Fixed Power Supply

[shape 4 | TEXT_BOX (17) | 文本框 1]
Table 2: Product List Based on VastLakes Platform


## SLIDE 9
[table 1 rows=9 cols=3]
Series	Model	Specification
XLite	STH-2C6QX-HSI	6*40G QSFP+, 2*100G QSFP28 1*Hot-swappable Fan Module and CRPS Module 1*ATX(2*3pin)power connecter for redundancy 
	STH-2C6QX-SFI	6*40G QSFP+, 2*100G QSFP28 2*Fixed Fans, 1*Fixed Power Supply
	STH-2C24DX-HSI	24*10G SFP+, 2*100G QSFP28 1*Hot-swappable Fan Modules and CRPS Modules 1*ATX(2*3pin)power connecter for redundancy 
	STH-2C24DX-SFI	24*10G SFP+, 2*100G QSFP28 2*Fixed Fans, 1*Fixed Power Supply 1*ATX(2*4pin)power connecter for redundancy 
	STH-2C12XF12XE-HSI	12*10G SFP+, 12*10G Multi-Gigabit Base-T 2*100G QSFP28 1*Hot-swappable Fan Module and CRPS Module 1*ATX(2*3pin)power connecter for redundancy 
	STH-2C12XF12XE-SFI	12*10G SFP+, 12*10G Multi-Gigabit Base-T 2*100G QSFP28 3*Fixed Fans, 1*Fixed Power Supply 1*ATX(2*4pin)power connecter for redundancy 
	STH-2C24XE-HSI	24*10G Multi-Gigabit Base-T, 2*100G QSFP28 1*Hot-swappable Fan Module and CRPS Modules 1*ATX(2*3pin)power connecter for redundancy 
	STH-2C24XE-SFI	24*10G Multi-Gigabit Base-T, 2*100G QSFP28 3*Fixed Fans, 1*Fixed Power Supply 1*ATX(2*4pin)power connecter for redundancy 

[shape 2 | TEXT_BOX (17) | 文本框 1]
Table 2: Product List Based on VastLakes Platform(Continued)

[shape 3 | TEXT_BOX (17) | 文本框 1]
STH=Saga Telecom High-speed Series
C=100G
X=10G
G=1G
F=Fiber
E=Ethernet

Q=Quadruple
QX=40G
D=Double
DX=25G
XE=10G Ethernet
XF=10G Fiber
GF=1G SFP
GE = 1G Ethernet

HSI=Hot Swappable Input
SFI=Single Fixed Input

