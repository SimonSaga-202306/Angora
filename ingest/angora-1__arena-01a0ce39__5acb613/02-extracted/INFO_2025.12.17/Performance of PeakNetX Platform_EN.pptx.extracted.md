<!-- ============================================================ -->
<!-- FILE 296/781 -->
<!-- PATH: INFO_2025.12.17/Performance of PeakNetX Platform_EN.pptx -->
<!-- SIZE: 97089 bytes -->
<!-- SHA256: c269792b0c21a8f3f4fbbe177adc17d132d73e1f2d6764d98ce12b017ab07237 -->
<!-- EXTRACTION: python-pptx - every slide, every shape text, every table, notes -->
<!-- ============================================================ -->

Presentation: slides=7

## SLIDE 1
[shape 1 | TEXT_BOX (17) | 文本框 3]
HOHUNET PEAKNETX PLATFORM 
PERFORMANCE(Default Profile)

[shape 2 | TEXT_BOX (17) | 文本框 4]
High Performance Switching Hardware Platform

[shape 3 | TEXT_BOX (17) | 文本框 6]
Platform Overview

[shape 4 | TEXT_BOX (17) | 文本框 7]
PeakNetX platform is a purpose-built Ethernet switching platform to address the growing demand for extreme low latency/jitter, comprehensive end-to-end tunnel network and high speed in the era of edge computing and AI. PeakNetX platform provides superb flexible I/O connectivity capability, support full-range port speeds from 10G to 100G

[shape 5 | TEXT_BOX (17) | 文本框 8]
Key Features of the PeaknetX Platform

[shape 6 | TEXT_BOX (17) | 文本框 9]
Ethernet capabilities: MAC table, Vxlan, IPFIX, ACL, EVC etc.
Full set of Layer 2 and Layer 3 protocol
Rich OAM
Security feature set
Precision timing protocol

[table 7 rows=12 cols=3]
Type	Specification	Value
Ethernet Basic	　	　
Jumbo Frame	Maximum jumbo frame size	9600
Unicast MAC	MAC address capacity	Default profile:122880
		IPv6 profile: 65536
		Layer3 profile: 65536
	MAC learning rate(SW)	> 4000pps
	MAC learning rate(HW)	> 10Gbps
	Blackhole MAC address capacity	128
Multicast MAC	MAC address capacity	Default profile: 2048
		IPv6 profile: 1024
		Layer3 profile: 1024

[shape 8 | TEXT_BOX (17) | 文本框 1]
Table 1: Performance of PeaknetX Platform

[shape 9 | TEXT_BOX (17) | 文本框 17]
Performance of the PeaknetX Platform

[shape 10 | TEXT_BOX (17) | 文本框 1]
SAGA TELECOM PEAKNETX PLATFORM PERFORMANCE
High Performance Switching Hardware Platform


## SLIDE 2
[shape 1 | TEXT_BOX (17) | 文本框 1]
Table 1: Performance of PeaknetX Platform(Continued)

[table 2 rows=28 cols=3]
Type	Specification	Value
Ethernet Basic	　	　
VLAN　 　	VLAN IDs	4094
	VLAN instances	4094
	VLANs to enable statistics	256
VLAN Mapping　	Maximum mapping table	64
	Maximum rules number	1024
EVC	Maximum EVC number	4094
Link Aggregation (Static&LACP)	Maximum member number per group	No limitation
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
Table 1: Performance of PeaknetX Platform(Continued)

[table 2 rows=36 cols=3]
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
ARP	ARP capacity	Default profile: 16384
		IPv6 profile: 8192
		Layer3 profile: 20480
IPv4	FIB	Default profile: 61440
		IPv6 profile: 32768
		Layer3 profile: 61440
ECMP	ECMP group	240(Share with IPv6)
PBR	Policy route map	64
	Policy based routing ACE	256
OSPF	Maximum static neighbors	256
	Maximum summary address	2000
IPv4 Multicast	　	　
IPMC	Multicast routing table	Default profile: 2048
		IPv6 profile: 1024
		Layer3 profile: 2048
	Multicast routing downstream interfaces	Default profile: 4096
		IPv6 profile: 2048
		Layer3 profile: 5120
IGMP Snooping	Maximum groups number	2048
	Maximum member number	N/A
MVR	Maximum group number	Default profile: 2048
		IPv6 profile: 1024
		Layer3 Profile: 2048
	Maximum member number	Default profile: 4096
		IPv6 profile: 2048
		Layer3 profile: 5120


## SLIDE 4
[shape 1 | TEXT_BOX (17) | 文本框 1]
Table 1: Performance of PeaknetX Platform(Continued)

[table 2 rows=35 cols=3]
Type	Specification	Value
IPv6 Unicast	　	　
Host Route	NDP capacity	2048
IPv6	FIBv6	4096
	ECMP group	240(share with IPv4)
IPv6 Multicast	　	　
IPMC	Multicast routing table	Default profile: 256
		IPv6 profile: 512
		Layer3 Profile: 0
	Number of interfaces that support multicast routing table	Default profile: 512
		IPv6 profile: 1024
		Layer3 Profile: 0
MVR V6	Maximum entry number	Default profile: 2048
		IPv6 Profile: 512
		Layer3 Profile: 0
	Maximum member number	Default profile: 512
		IPv6 profile: 1024
		Layer3 Profile: 0
IP tunnel	　	　
IP Tunnel	Tunnel peer capacity	8
QoS	　	　
Per-port Queue Number	Unicast queue	10
	Multicast queue	10
	Monitor queue	10
Packet Buffer	System packet buffer capacity	36MByte
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


## SLIDE 5
[shape 1 | TEXT_BOX (17) | 文本框 1]
Table 1: Performance of PeaknetX Platform(Continued)

[table 2 rows=38 cols=3]
Type	Specification	Value
ACL	　	　
MAC ACL	Ingress port ACL for MAC	Default profile: 5949
		IPv6 profile: 5949
		Layer3 profile: 5952
	Ingress VLAN ACL for MAC	Default profile: 5949
		IPv6 profile: 5949
		Layer3 profile: 5952
	Egress port ACL for MAC	Default profile: 1901
		IPv6 profile: 1904
		Layer3 profile: 1952
	Egress VLAN ACL for MAC	Default profile: 1901
		IPv6 profile: 1904
		Layer3 profile: 1952
IPv4 ACL	Ingress Port ACL for IPv4	Default profile: 5949
		IPv6 profile: 5949
		Layer3 profile: 5952
	Ingress VLAN ACL for IPv4	Default profile: 5949
		IPv6 profile: 5949
		Layer3 profile: 5952
	Egress Port ACL for IPv4	Default profile: 1901
		IPv6 profile: 1904
		Layer3 profile: 1952
	Egress VLAN ACL for IPv4	Default profile: 1901
		IPv6 profile: 1904
		Layer3 profile: 1952
IPv6 ACL	Ingress Port ACL for IPv6	Default profile: 5949
		IPv6 profile: 5949
		Layer3 profile: 5952
	Ingress VLAN ACL for IPv6	Default profile: 5949
		IPv6 profile: 5949
		Layer3 profile: 5952
	Egress Port ACL for IPv6	Default profile: 1901
		IPv6 profile: 1904
		Layer3 profile: 1952
	Egress VLAN ACL for IPv6	Default profile: 1901
		IPv6 profile: 1904
		Layer3 profile: 1952


## SLIDE 6
[shape 1 | TEXT_BOX (17) | 文本框 1]
Table 1: Performance of PeaknetX Platform(Continued)

[table 2 rows=30 cols=3]
Type	Specification	Value
ACL	　	　
ACL Flow Statistics	Ingress ACL flow statistics entries	1022
	Egress ACL flow statistics entries	511
CoPP	CoPP rules	249
	CoPP flow statistics entries	249
UDF	UDF rules	256
	UDF flow stats entries	128
Security	　	　
IP Source Guard	IPv4 maximum rules number	768
	IPv6 maximum rules number	64
802.1x Base MAC	Maximum entries	256
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
Data Center	　	　
VARP	Virtual IP number per port	15
VXLAN	VXLAN tunnel	4092
	VNI	1024
	VTEP peer	24576
	VXLAN gateway MAC for DVR	512


## SLIDE 7
[shape 1 | TEXT_BOX (17) | 文本框 1]
Product List Based on PeaknetX Platform

[table 2 rows=6 cols=3]
Series	Model	Specification
STH100G	STH-32C-HSI	32*100G QSFP28, L3 managed Ethernet switch 2*Hot-swappable 550W CRPS 4*Hot-swappable Fan Modules
	STH-24C-HSI	24*100G QSFP28, L3 managed Ethernet switch 2*Hot-swappable 550W CRPS Modules 4*Hot-swappable Fan Modules
STH25G	STH-8C48DX-HSI	48*25G SFP28, 8*100G QSFP28, L3 managed Ethernet switch 2*Hot-swappable 550W CRPS Modules 5*Hot-swappable Fan Modules
STH10G	STH-8C48XE-HSI	48*100M/1G/2.5G/5G/10G Multi-Gigabit Base-T 8*100G QSFP28 L3 managed Ethernet switch 2*Hot-swappable 550W CRPS Modules 2*Hot-swappable Fan Modules
	STH-8C48XF-SFI	48*10G SFP+, 8*100G QSFP28, L3 managed Ethernet switch 2*Fixed 200W Power Supply 4*Fixed Fans

[shape 3 | TEXT_BOX (17) | 文本框 1]
Table 2: Product List Based on PeaknetX Platform

[shape 4 | TEXT_BOX (17) | 文本框 1]
STH=Saga Telecom High-speed Series
C=100G
X=10G

D=Double
DX=25G
XE=10G Ethernet
XF=10G Fiber

HSI=Hot Swappable Input
SFI=Single Fixed Input

