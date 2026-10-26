<!-- ============================================================ -->
<!-- FILE 305/781 -->
<!-- PATH: INFO_2025.12.17/Saga Software Function List_EN.pptx -->
<!-- SIZE: 154107 bytes -->
<!-- SHA256: 3caa5c7de784d52e470ed7266e511c817f3fe0c66f3b194260263f8c47984ec6 -->
<!-- EXTRACTION: python-pptx - every slide, every shape text, every table, notes -->
<!-- ============================================================ -->

Presentation: slides=17

## SLIDE 1
[table 1 rows=6 cols=8]
Type	Sub Type	Feature	Description	EB	MS	MA	Remark
Ethernet basic features	Ethernet	Interface	Ethernet interface operating modes(full duplex, half duplex, and auto-negotiation)	◯	◯	◯	
			Ethernet interface operating rates	◯	◯	◯	
			Jumbo Frame	◯	◯	◯	
			port-xconnect	◯	◯	◯	
		Flow-control	Flow-control tx/rx	◯	◯	◯	

[shape 2 | AUTO_SHAPE (1) | AutoShape 2]
STOS (SAGA TELECOM OPERATING SYSTEM) UNIFIED SWTICH SOFTWARE FUNCTION LIST

[shape 3 | AUTO_SHAPE (1) | AutoShape 3]
Overview

[shape 4 | AUTO_SHAPE (1) | AutoShape 4]
STOS, launched by Saga Telecom, is a switch operating system, which is also an unified software platform used by all switches. STOS has experienced through commercial application test over 10 years. Its advanced modular flexible architecture offers good hardware decoupling capability. Saga Telecom constantly iterates and releases an updated versions every quarter to fix bugs or update features, ensuring better adaptation to an ever-changing network environment.

[shape 5 | AUTO_SHAPE (1) | AutoShape 5]
keywords

[shape 6 | AUTO_SHAPE (1) | AutoShape 6]
Accumulating and iterating over a span of 10 years.
An unified Software Platform.
Being verified in the extensive commercial network environment.
The features are modularized, which allows for pruning, and the code can be easily ported for the same reason.

[shape 7 | AUTO_SHAPE (1) | AutoShape 9]
Version: V2.4（STOS Firmware Version: V3.0.22）Release Date: 2025/12/12

[shape 8 | AUTO_SHAPE (1) | AutoShape 10]
Features List table

[shape 9 | AUTO_SHAPE (1) | AutoShape 12]
Tips for reading：  EB-Basic license     MS-Advanced license    MA-Metropolitan Area Network License    
ST-Stacking license      ◯-support     X-non-support


## SLIDE 2
[table 1 rows=23 cols=8]
Type	Sub Type	Feature	Description	EB	MS	MA	Remark
Ethernet basic features	Ethernet	Storm-control	Port based storm-control	◯	◯	◯	
			VLAN based storm-control	◯	◯	◯	
		Port-block	Port-block(know/unknown unicast; know/unknown multicast/broadcast)	◯	◯	◯	
		Port-isolate	L2/L3/All  Port-isolate	◯	◯	◯	
			Uni-direction isolate	◯	◯	◯	
		L2 Protocol Tunnel	L2 Protocol Tunnel(support CFM/DOT1X/SLOW-PROTO/STP	◯	◯	◯	
		Forward mode	Store-and-forward	◯	◯	◯	
			Cut-through	◯	◯	◯	
	VLAN	VLAN Access mode	Access/Trunk	◯	◯	◯	
			Default VLAN	◯	◯	◯	
		VLAN Classification	VLAN Classification(port based/mac based/IP based/protocol based)	◯	◯	◯	
		QinQ	Basic QinQ	◯	◯	◯	
			Selective QinQ	◯	◯	◯	
			VLAN Mapping(1:1 VLAN Translation)	◯	◯	◯	
		VLAN Statistics	VLAN Statistics	◯	◯	◯	
		Private VLAN	Private VLAN	◯	◯	◯	
		Voice VLAN	Voice VLAN	◯	◯	◯	
		Guest VLAN	Guest VLAN	◯	◯	◯	
	MAC	MAC Address Table	Automatic learning and aging of MAC addresses	◯	◯	◯	
			Hardware Learning	◯	◯	◯	
			Static and dynamic  MAC address entries	◯	◯	◯	
			Blackhole MAC	◯	◯	◯	


## SLIDE 3
[table 1 rows=25 cols=8]
Type	Sub Type	Feature	Description	EB	MS	MA	Remark
Ethernet basic features	MAC	MAC Flapping detect	MAC Flapping detect	◯	◯	◯	
		Port Bridge	Port Bridge	◯	◯	◯	
	LAG	Link aggregation	Static-LAG & LACP	◯	◯	◯	
			LAG load balance(SLB)	◯	◯	◯	
			LAG load balance(DLB)	◯	◯	◯	
			LAG load balance(RR)	◯	◯	◯	
			LAG Self-healing	◯	◯	◯	
			Link aggregation weighting	◯	◯	◯	
Ethernet Ring protection features	xSTP	STP	Spanning-Tree Protocol	◯	◯	◯	
		RSTP	Rapid Spanning-Tree Protocol	◯	◯	◯	
		MSTP	Multi-instance Spanning-Tree Protocol	◯	◯	◯	
		Spanning-Tree Protocol Protection	BPDU Filter/Guard	◯	◯	◯	
			Root Guard	◯	◯	◯	
			Loop Guard	◯	◯	◯	
			Anti TC-BPDU attack	◯	◯	◯	
	ERPS	ERPS	Single ERPS ring	◯	◯	◯	
			tangent ERPS rings	◯	◯	◯	
			intersecting ERPS rings	◯	◯	◯	
			compatible with RRPP	◯	◯	◯	
	Loop back Detect	Loop back Detect	Loop back detection	◯	◯	◯	
Layer2 Multicast	Layer2 Multicast	IGMP Snooping	IGMPv1/v2/v3 Snooping	◯	◯	◯	
			Fast leave	◯	◯	◯	
			Static IGMP snooping group	◯	◯	◯	
		MVR	MVR(Multicast VLAN Registration)	◯	◯	◯	


## SLIDE 4
[table 1 rows=30 cols=8]
Type	Sub Type	Feature	Description	EB	MS	MA	Remark
IPv4 Forwarding	ARP	ARP	Static and dynamic ARP entries	◯	◯	◯	
			Aging of ARP entries	◯	◯	◯	
			Gratuitous ARP	◯	◯	◯	
		ARP proxy	basic ARP-Proxy	◯	◯	◯	
			local ARP-Proxy	◯	◯	◯	
	IPv4 Unicast Routing	IPv4 Static Routes	IPv4 Static Routes	◯	◯	◯	
			Black hole Routes	◯	◯	◯	
			co-work with IP SLA	◯	◯	◯	
			VRF(Virtual Routing and Forwarding)	◯	◯	◯	
			uRPF check	◯	◯	◯	
		RIP	RIPv1/v2	◯	◯	◯	
		OSPFv2	OSPFv2	X	◯	◯	
		IS-IS	IS-IS	X	◯	◯	
		BGP	IBGP	X	◯	◯	
			EBGP	X	◯	◯	
		Route policy	Route-map	◯	◯	◯	
			IPv4 prefix-list	◯	◯	◯	
		PBR	PBR(Policy-based Routing)	◯	◯	◯	
		ICMP	ICMP redirect	◯	◯	◯	
			ICMP unreachable	◯	◯	◯	
		ECMP	ECMP(SLB)	◯	◯	◯	
			ECMP(DLB)	◯	◯	◯	
			ECMP(RR)	◯	◯	◯	
			ECMP Self-healing	◯	◯	◯	
	IPv4 Multicast Routing	IGMP	IGMPv1/v2/v3	◯	◯	◯	
			IGMP-Proxy	◯	◯	◯	
			IGMP SSM Mapping	◯	◯	◯	
		PIM	PIM-SM	X	◯	◯	
			PIM-DM	X	◯	◯	


## SLIDE 5
[table 1 rows=28 cols=8]
Type	Sub Type	Feature	Description	EB	MS	MA	Remark
IPv6 Forwarding	IPv6 Basic Protocol	ICMPv6	ICMPv6	X	◯	◯	
		NDP	NDP	X	◯	◯	
	IPv6 Unicast Routing	IPv6 Static Routes	IPv6 Static Routes	X	◯	◯	
		RIPng	RIPng	X	◯	◯	
		OSPFv3	OSPFv3	X	◯	◯	
		IS-IS	IS-IS	X	◯	◯	
		BGP4+	BGP4+	X	◯	◯	
	IPv6 Multicast Routing	MLD v1/v2	MLD v1/v2	X	◯	◯	
		MLD v1/v2 Snooping	MLD v1/v2 Snooping	X	◯	◯	
		MVR6	MVR6	X	◯	◯	
		PIM-SM v6	PIM-SM v6	X	◯	◯	
	IP Tunnel	IPv6 over IPv4 Tunnel	IPv6 over IPv4 Tunnel	X	◯	◯	
		6to4 Tunnel	6to4 Tunnel	X	◯	◯	
		ISATAP Tunnel	ISATAP Tunnel	X	◯	◯	
	IPv6 Service	DHCPv6	DHCPv6 Relay	X	◯	◯	
			DHCPv6 Snooping	X	◯	◯	
		IPv6 Prefix List	IPv6 Prefix-list	X	◯	◯	
Device reliability features	BFD	BFD	BFD for Static route	X	◯	◯	
			BFD for OSPFv2	X	◯	◯	
			BFD for VRRP/Track	X	◯	◯	
			BFD for PBR	X	◯	◯	
	VRRP	VRRP	VRRP	◯	◯	◯	
			Track for VRRP	◯	◯	◯	
	Smart Link	Smart Link	multi-instance	◯	◯	◯	
			load balance	◯	◯	◯	
			Multi-Link	◯	◯	◯	
			Monitor-link	◯	◯	◯	


## SLIDE 6
[table 1 rows=24 cols=8]
Type	Sub Type	Feature	Description	EB	MS	MA	Remark
Device reliability features	MLAG	MLAG	MLAG basic	◯	◯	◯	
			MLAG orphan Port	◯	◯	◯	
	Stacking	Stacking	Maximum number of stacked devices: 8 Stack port: Any port or AGG	◯	◯	◯	*1
Ethernet OAM	EFM	EFM (802.3ah)	Auto detection	X	◯	◯	
			Network fault detection	X	◯	◯	
			Network fault handle	X	◯	◯	
			remote loop back	X	◯	◯	
	CFM	CFM (802.1ag)	Hardware CCM detect	X	◯	◯	
			MAC Ping	X	◯	◯	
			MAC Trace	X	◯	◯	
	Y.1731	Y.1731	Loss measure(LM)	X	◯	◯	*2
			Latency and Jitter measure	X	◯	◯	
PoE features	PoE	System Power management	Power supply on-spot detection	◯	◯	◯	
			Power supply capability detection	◯	◯	◯	
			Power capability auto configuration (PSE)	◯	◯	◯	
		Power Supply Management	Legacy PD detection	◯	◯	◯	
			PD max power management	◯	◯	◯	
			PD priority management	◯	◯	◯	
			Power Supply Task Plan management(Not ready)	◯	◯	◯	
			PD Mandatory power supply	◯	◯	◯	
		operations management	PSE log	◯	◯	◯	
			PSE Chipset temperature inquire	◯	◯	◯	
			PSE firmware update	◯	◯	◯	


## SLIDE 7
[table 1 rows=18 cols=8]
Type	Sub Type	Feature	Description	EB	MS	MA	Remark
QoS features	QoS	Traffic classification	Traffic classification based on COS/DSCP (simple classification)	◯	◯	◯	
			Traffic classification based on ACL ( complex classification)	◯	◯	◯	
			Traffic classification based on inner header of the tunnel packets	◯	◯	◯	
		Traffic behaviors	Queue scheduling	◯	◯	◯	
			Remark the priority fields(COS/DSCP) of the packet based on ACL	◯	◯	◯	
			Remark the priority fields(COS/DSCP) of the packet based on Table Map	◯	◯	◯	
			Flow redirection	◯	◯	◯	
			Flow mirror	◯	◯	◯	
		Traffic policing	Traffic policing based on direction(in/out)  of Port	◯	◯	◯	
			Traffic policing based on direction(in/out) of VLAN	◯	◯	◯	
			Traffic policing based on direction(in/out) of flow	◯	◯	◯	
			Traffic policing based on direction(in/out) of aggregated flow	◯	◯	◯	
		Traffic shaping	Queue based traffic shaping	◯	◯	◯	
			Port based traffic shaping	◯	◯	◯	
		Congestion management	SP(Strict Priority)scheduling	◯	◯	◯	
			WDRR(Weighted Deficit Round Robin)scheduling	◯	◯	◯	*3
			SP + WDRR mixed scheduling	◯	◯	◯	*4


## SLIDE 8
[table 1 rows=20 cols=8]
Type	Sub Type	Feature	Description	EB	MS	MA	Remark
QoS features	QoS	Congestion avoidance	TD(Tail Drop)	◯	◯	◯	
			WRED(Weighted Random Early Detection)	◯	◯	◯	
		Traffic statistics	Packet counts and bytes statistics based on traffic classification	◯	◯	◯	
			Packet counts and bytes statistics based on the color after traffic policing	◯	◯	◯	
			Forwarded and discarded packet counts and bytes statistics	◯	◯	◯	
		ECN (Explicit congestion notification)	ECN tags based on Tail Drop	◯	◯	◯	*5
			ECN tags based on WRED	◯	◯	◯	
Data Center	VARP	Virtual gateway	VARP(Virtual-ARP)	◯	◯	◯	
			VARP subnet	◯	◯	◯	
	Tunnel	VxLAN	Manual configure VxLAN tunnel	◯	◯	◯	
			VxLAN distributed gateway	◯	◯	◯	
			VxLAN active-active access	◯	◯	◯	
			Interconnect across Data Centers based on VxLAN	◯	◯	◯	
			Edit DSCP in VxLan outer header	◯	◯	◯	
			BGP EVPN	X	◯	◯	
			Support to enable/disable overlay split horizon per-VNI	◯	◯	◯	
		GRE Tunnel	GRE Tunnel	◯	◯	◯	
		NVGRE Tunnel	NVGRE Tunnel	◯	◯	◯	
		GENEVE Tunnel	GENEVE Tunnel	◯	◯	◯	


## SLIDE 9
[table 1 rows=30 cols=8]
Type	Sub Type	Feature	Description	EB	MS	MA	Remark
Data Center	DCB	DCBX	LLDP support DCBX TLV	◯	◯	◯	
		PFC	PFC	◯	◯	◯	
Metro Feature	MPLS	LDP	LDP	X	X	◯	
		MPLS Forwarding	MPLS Forwarding	X	X	◯	
		VPWS	VPWS (L2VPN)	X	X	◯	
		VPLS	VPLS (L2VPN)	X	X	◯	
		L3VPN	L3VPN	X	X	◯	
		MPLS OAM	MPLS OAM	X	X	◯	
		MPLS Stats	MPLS Stats	X	X	◯	
		ACL	ACL	X	X	◯	
		Qos	Qos	X	X	◯	
Security and management	System Security	SSH	SSHv1/v2	◯	◯	◯	
			RSA Key generation	◯	◯	◯	
		RADIUS	RADIUS	◯	◯	◯	
		TACAS+	TACAS+	◯	◯	◯	
		AAA	Authentication	◯	◯	◯	
			Authorization	◯	◯	◯	
			Accounting	◯	◯	◯	
		Dot1x	Port based dot1x	◯	◯	◯	
			MAC based dot1x	◯	◯	◯	
			Guest VLAN	◯	◯	◯	
		ACL	MAC/IP ACL	◯	◯	◯	
			Basic Mode ACL	◯	◯	◯	
			Port-group ACL	◯	◯	◯	
			VLAN-group ACL	◯	◯	◯	
			IPv6 ACL	◯	◯	◯	
			ACL UDF	◯	◯	◯	
			Time Range	◯	◯	◯	
		ARP Inspection	ARP Inspection	◯	◯	◯	


## SLIDE 10
[table 1 rows=24 cols=8]
Type	Sub Type	Feature	Description	EB	MS	MA	Remark
Security and management	System Security	IP Source Guard	IP Source Guard	◯	◯	◯	
		Port Security	Limitation on MAC address learning on interface	◯	◯	◯	
		VLAN Security	Limitation on MAC address learning on VLAN	◯	◯	◯	
		Control Plane Policy (COPP)	Black list/wihte list	◯	◯	◯	
			Rate limit	◯	◯	◯	
		CPU Traffic Limit	CPU Traffic Limit	◯	◯	◯	
		Prevent DDOS attack	Prevent DDOS attack (ICMP Flood/Smurf/Fraggle/LAND/SYN Flood)	◯	◯	◯	
		Login filter	Telnet/SSH ACL filtering	◯	◯	◯	
			Telnet/SSH IPv6 ACL filtering	◯	◯	◯	
		MAC Security	MacSec(802.1AE)	◯	◯	◯	*6
		Link-Flapping detection	Link-Flapping detection	◯	◯	◯	
	Network Management	DHCP	DHCP Server	◯	◯	◯	
			DHCP Relay	◯	◯	◯	
			DHCP Snooping	◯	◯	◯	
			DHCP Client	◯	◯	◯	
			DHCP Option82	◯	◯	◯	
			DHCP Option252	◯	◯	◯	
		RMON	RMON	◯	◯	◯	
		sFlow	sFlow v4/v5	◯	◯	◯	
		IP SLA	IP SLA	◯	◯	◯	
		IPFIX	IPFIX	◯	◯	◯	
		EFD	Elephant Flow Detection	◯	◯	◯	*7
		NTP	NTP(Network Time Protocol)	◯	◯	◯	


## SLIDE 11
[table 1 rows=19 cols=8]
Type	Sub Type	Feature	Description	EB	MS	MA	Remark
Security and management	Network Management	PTP（IEEE 1588）	TC（Support P2P/E2E、Ethernet/Udp Transport）	◯	◯	◯	
			BC/OC(Support OneStep/TwoStep、Request-response/Peer-delay Ethernet/Udp Transport)	◯	◯	◯	
		Err-disable	Err-disable detection and recovery	◯	◯	◯	
		DNS	Static DNS Client	◯	◯	◯	
		LLDP	LLDP	◯	◯	◯	
	Terminal Services	Command Line Interface	Configurations through CLI (Command Line Interface)	◯	◯	◯	
		Help information	Banner configuration	◯	◯	◯	
			Help information in English	◯	◯	◯	
		Terminal service	Vty Terminal service	◯	◯	◯	
			Console Terminal service	◯	◯	◯	
		Management interface	In-band management interface and configuration	◯	◯	◯	
			Out-band management interface and configuration	◯	◯	◯	
Configuration and maintenance	Configuration Management	SNMP	Network management based on SNMPv1/v2c/v3	◯	◯	◯	
			Public and private MIB	◯	◯	◯	
			Public and private Trap	◯	◯	◯	
		WEB	Configuration and management based on WEB UI	◯	◯	◯	
		Cloud Management	Automatic device connection management	◯	◯	◯	*8
			Zero-configuration deployment	◯	◯	◯	


## SLIDE 12
[table 1 rows=17 cols=8]
Type	Sub Type	Feature	Description	EB	MS	MA	Remark
Configuration and maintenance	Configuration Management	Cloud Management	Automatic network topology	◯	◯	◯	*8
			Network monitoring and alarm notification	◯	◯	◯	
			Configuration and one-click rollback	◯	◯	◯	
			Cross-network tunneling connection to network device(web/ssh/telnet)	◯	◯	◯	
			Scheduled tasks deployment	◯	◯	◯	
		RPC-API	Configuration and management based on RPC-API	◯	◯	◯	
		Smart Config	Smart Config(Automatically configuration when system start)	◯	◯	◯	
		system profile configuration	change the system specifications by choose different STM Profiles	◯	◯	◯	
		Restore factory default configuration	Restore factory default configuration	◯	◯	◯	
	File System	File system	File system(support directory and file management)	◯	◯	◯	
		Upload and download	Upload and download files through FTP or TFTP	◯	◯	◯	
			Upload and download files through Xmodem	◯	◯	◯	
	Debugging And Maintenance	Debug	per-module Debug features	◯	◯	◯	
			ICMP Debug	◯	◯	◯	
		BHM	Software process monitor: BHM(Beat Heart Monitor)	◯	◯	◯	
			Hardware Watch Dog	◯	◯	◯	


## SLIDE 13
[table 1 rows=22 cols=8]
Type	Sub Type	Feature	Description	EB	MS	MA	Remark
Configuration and maintenance	Debugging And Maintenance	Log & alarm	CPU usage display and  alarm	◯	◯	◯	
			Memory  usage display and  alarm	◯	◯	◯	
			Device temperature, PSU, FAN, status display and alarm	◯	◯	◯	
			User operation logs	◯	◯	◯	
			Management of logs, alarms, and debugging information	◯	◯	◯	
		VCT	VCT(Virtual Cable Test)	◯	◯	◯	
		system diagnostics	Detailed Diagnostic-information collection	◯	◯	◯	
		Reboot	Manual reboot	◯	◯	◯	
			Schedule Reboot	◯	◯	◯	
			Reboot Information logging	◯	◯	◯	
		network diagnostics	Ping	◯	◯	◯	
			IPv6 Ping	◯	◯	◯	
			Trace route	◯	◯	◯	
		mirror	Port mirror	◯	◯	◯	
			Flow mirror	◯	◯	◯	
			Remote mirror	◯	◯	◯	
			Multi-destination mirror(m:n)	◯	◯	◯	
			Use CPU as mirror source	◯	◯	◯	
			Use CPU as mirror destination and analyze packet	◯	◯	◯	
			ERSPAN	◯	◯	◯	
		CPU statistics	To CPU/From CPU packets statistics	◯	◯	◯	


## SLIDE 14
[table 1 rows=10 cols=8]
Type	Sub Type	Feature	Description	EB	MS	MA	Remark
Configuration and maintenance	Debugging And Maintenance	L2 Ping	layer2 network connectivity detection - L2Ping (MAC Ping/Trace)	◯	◯	◯	
		UDLD	UDLD(Unidirectional Link Detection)	◯	◯	◯	
		unidirectional	unidirectional forwarding of the fiber	◯	◯	◯	
		Loop back	port loop back	◯	◯	◯	
			hardware loop back(internal/external)	◯	◯	◯	
		System time	Time configuration	◯	◯	◯	
			Timezone	◯	◯	◯	
	Software	System software upgrate	Update via TFTP	◯	◯	◯	
	upgrate	Uboot upgrate	Uboot upgrate	◯	◯	◯	

[table 2 rows=9 cols=1]
Remark:
*1. Requires ST licence.
*2. Loss measure(LM) is not available on BigFlow and SerdesX Platform.
*3. WDRR(Weighted Deficit Round Robin)scheduling is not available on SerdesX platform.
*4. SP + WDRR mixed scheduling is not available on SerdesX platform.
*5. ECN tags based on Tail Drop is not available on SerdesX platform.
*6. MacSec(802.1AE) is not available on BigFlow Platform.
*7. Elephant Flow Detection is not available on BigFlow Platform.
*8. Cloud Management feature needs to be used  with the DHCS Cloud Management system. DHCS can be deployed on public clouds or in a private environment.


## SLIDE 15
[table 1 rows=31 cols=1]
Supported MIB
• RFC 1155 SMI
• RFC 1157 SNMPv1
• RFC 1212, RFC 1213, RFC 1215 MIB-II, Ethernet-Like MIB and TRAPs
• RFC 1493 Bridge MIB
• RFC 1643 Ethernet MIB
• RFC 1657 BGP-4 MIB
• RFC 1724 RIPv2 MIB
• RFC 1850 OSPFv2 MIB
• RFC 1905 RFC 1907 SNMP v2c, SMIv2 and Revised MIB-II
• RFC 2011 SNMPv2 for Internet Protocol using SMIv2
• RFC 2012 SNMPv2 for transmission control protocol using SMIv2
• RFC 2013 SNMPv2 for user datagram protocol suing SMIv2
• RFC 2096 IPv4 Forwarding Table MIB
• RFC 2287 System Application Packages MIB
• RFC 2570–2575 SNMPv3, user based security, encryption and authentication
• RFC 2576 Coexistence between SNMP Version 1, Version 2 and and Version 3
• RFC 2578 SNMP Structure of Management Information MIB
• RFC 2579 SNMP Textual Conventions for SMIv2
• RFC 2665 Ethernet-like interface MIB
• RFC 2819 RMON MIB
• RFC 2863 Interface Group MIB
• RFC 2863 Interface MIB
• RFC 3413 SNMP Application MIB
• RFC 3414 User-based Security model for SNMPv3
• RFC 3415 View-based Access Control Model for SNMP
• RFC 4188 STP and Extensions MIB
• RFC 4363 Definitions of Managed Objects for Bridges with Traffic Classes, Multicast Filtering, and VLAN extensions
• Draft – blumenthal – aes – usm - 08
• Draft – reeder - snmpv3 – usm - 3desede -00
• Draft-ietf-idmr-igmp-mib-13


## SLIDE 16
[table 1 rows=30 cols=1]
Supported RFC
• RFC 826 ARP
• RFC 854 Telnet client and server
• RFC 894 IP over Ethernet
• RFC 906 TFTP Bootstrap
• RFC 1027 Proxy ARP
• RFC 1058 RIP v1
• RFC 1112 IGMP v1
• RFC 1122 STOSt Requirements
• RFC 1195 Use of OSI IS-IS for Routing in TCP/IP and Dual Environments (TCP/IP transport only)
• RFC 1492 TACACS+RFC 1519 CIDR
• RFC 1587 OSPF NSSA Option
• RFC 1591 DNS
• RFC 1812 Requirements for IP Version 4 Routers
• RFC 2030 SNTP, Simple Network Time Protocol
• RFC 2068 HTTP server
• RFC 2080 RIPng for IPv6
• RFC 2131 BOOTP/DHCP relay agent and DHCP server
• RFC 2138 RADIUS Authentication
• RFC 2139 RADIUS Accounting
• RFC 2154 OSPF w/Digital Signatures (password, MD-5)
• RFC 2236 IGMP v2
• RFC 2267 Network Ingress Filtering
• RFC 2328 OSPF v2 (edge-mode)
• RFC 2338 VRRP
• RFC 2362 PIM-SM (edge-mode)
• RFC 2370 OSPF Opaque LSA Option
• RFC 2453 RIP v2
• RFC 2460 Internet Protocol, Version 6 (IPv6) Specification
• RFC 2461 Neighbor Discovery for IP Version 6 (IPv6)


## SLIDE 17
[table 1 rows=11 cols=1]
Supported RFC (The End)
• RFC 2463 Internet Control Message Protocol (ICMPv6) for the Internet Protocol Version 6 (IPv6) Specification
• RFC 2464 Transmission of IPv6 Packets over Ethernet Networks
• RFC 2474 DiffServ Precedence, including 12 queues/port
• RFC 2475 DiffServ Core and Edge Router Functions
• RFC 2526 Reserved IPv6 Subnet Anycast Addresses
• RFC 2597 DiffServ Assured Forwarding (AF)
• RFC 2598 DiffServ Expedited Forwarding (EF)
• RFC 2740 OSPF for IPv6
• RFC 3176 sFlow
• RFC 3376 IGMP v3

