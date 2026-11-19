[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")

[6 captures](https://web.archive.org/web/*/https://support.angoranetworks.com/?ht_kb=voice-video-ip-telephony "See a list of every capture for this URL")

27 Feb 2021 - 2 Dec 2024

|     |     |     |
| --- | --- | --- |
| Jan | FEB | [Oct](https://web.archive.org/web/20211027055534/https://support.angoranetworks.com/?ht_kb=voice-video-ip-telephony "05:55:34 Oct 27, 2021") |
|  | 27 | [05:55:34 Oct 27, 2021](https://web.archive.org/web/20211027055534/https://support.angoranetworks.com/?ht_kb=voice-video-ip-telephony "05:55:34 Oct 27, 2021") |
| 2020 | 2021 | [2022](https://web.archive.org/web/20220630215258/https://support.angoranetworks.com/?ht_kb=voice-video-ip-telephony "21:52:58 Jun 30, 2022") |

success

fail
[Share via My Web Archive](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb=voice-video-ip-telephony# "Share via My Web Archive") [Sign In](https://archive.org/account/login.php "Sign In")[Get some help using the Wayback Machine](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine")[Close the toolbar](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb=voice-video-ip-telephony#close "Close the toolbar")

[screenshot](https://web.archive.org/web/20210227210054/http://web.archive.org/screenshot/https://support.angoranetworks.com/?ht_kb=voice-video-ip-telephony "screenshot")[video](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb=voice-video-ip-telephony# "video")[Share on Facebook](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb=voice-video-ip-telephony# "Share on Facebook")[Share on Twitter](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb=voice-video-ip-telephony# "Share on Twitter")

[About this capture](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb=voice-video-ip-telephony#expand)

TIMESTAMPS

![loading](https://web-static.archive.org/_static/images/loading.gif)

The Wayback Machine - https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht\_kb=voice-video-ip-telephony

# Knowledge Base

Search ForSearch

1. [Home](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/ "Home")
2. [Knowledge Base](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?post_type=ht_kb "Knowledge Base")
3. [How To Guides](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb_category=how-to-guides "View all posts in How To Guides")
4. [Voice/Video/IP Telephony](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb=voice-video-ip-telephony "Voice/Video/IP Telephony")

### Collaboration Networks Features

Verge switches are an essential part of your collaboration network. All ports on PoE enabled models, supports up to 30W of power, to feed your endpoints.

AngoraOS is capable of supporting critical voice related features, such as voice vlan and quality of services.

This document describes the configuration needed, to enable and operate voice vlan. Informations for quality of service (QoS) can be found in the technology guides sections.

### What is Voice Vlan?

A voice vlan is used to carry IP telephony endpoints generated voice traffic. Many IP phones, are equipped with two ports. One port is used to connect the voice/video capable endpoint into the network, while the other is used to connect a user device such as a personal computer, without needing additional cabling. These two ports traffic must be distinguished on VLAN level, because real time traffic needs different service levels. As a result, endpoint generated traffic is sent via a different vlan, as we call it, Voice VLAN.

### Configuration Steps

This section describes step by step configuration to enable voice vlan, and get your endpoint and its connected PC to work with your Verge Switches.

Configuration should be considered in two basic category. We should enable use of voice vlan globally, before configuring each port separately.

#### Global Configuration

To enable voice vlan, in the global configuration, it is needed to add OUI of information of IP phone vendors to be used. This OUI-Table information is used to validate the traffic from voice vlan is actually generated from the IP phone. If the OUI information is missing, the IP phone would not be activated. OUI information can be added by the following command:

voice vlan oui-table _**{add mac-address-prefix \| remove mac-address-prefix} \[text\]**_

> Example:
>
> `switch(config)# voice vlan oui-table add 00:AA:BB IPPhoneVendor`

Once the OUI table is set, the voice vlan id should be defined by entering the following command:

voice vlan id _**vlan-id**_

> Example:
>
> `switch(config)# voice vlan id 35`
>
> `For Auto Voice VLAN, changes in the voice VLAN ID, CoS/802.1p, and/or DSCP will cause the switchto advertise the administrative voice VLAN as staticvoice VLAN which has higher priority than voice VLAN learnt from external sources.Are you sure you want to continue? (Y/N)[Y] Y`

OUI table and voice vlan ID are the two essential configs to start using voice vlan. Completing these two items, it is time to enable voice vlan with the following command:

voice vlan state **_{oui-enabled \| disabled\]_**

> Example:
>
> `switchxxxxxx(config)# voice vlan state oui-enabled`

Global configuration is done. Now the ports needs to be enabled as a voice vlan member. To enable a port to be used with voice vlan, the port type should be _**‘general’**_ . _Access or trunk ports is not usable for ip telephony and pc traffic to be enabled at the same time._

Considering the voice vlan id is 35, and the PC would reside in vlan 10, following interface configuration should be entered to enable voice vlan, and ip phone:

> Example:
>
> `switchxxxxxx(config)#interface GigabitEthernet1`
>
> `switchxxxxxx(config-if)# switchport mode general`
>
> `switchxxxxxx(config-if)# switchport general allowed vlan add 35 tagged`
>
> `switchxxxxxx(config-if)# switchport general allowed vlan add 10 untagged`
>
> `switchxxxxxx(config-if)# switchport general pvid 10`
>
> `switchxxxxxx(config-if)# voice vlan enable`

This concludes the voice vlan specific configuration. With this configuration active, the IP telephony device will reside in vlan 35, where the PC connected to it, will run inside vlan 10.

### Was this article helpful?

[Yes](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb=voice-video-ip-telephony#) [No](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb=voice-video-ip-telephony#)

### Related Articles

- [Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)")  - 0
  - 67
- [Sistem Bilgilerini Öğrenme](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "Sistem Bilgilerini Öğrenme")  - 0
  - 97
- [Link Katmanı Keşif Protokolü (LLDP)](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "Link Katmanı Keşif Protokolü (LLDP)")  - 0
  - 116
- [Komut Satırı kullanımı](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "Komut Satırı kullanımı")  - -1
  - 114
- [Hızlı Başlangıç Kılavuzu](https://web.archive.org/web/20210227210054/https://support.angoranetworks.com/?ht_kb=hizli-baslangic-kilavuzu "Hızlı Başlangıç Kılavuzu")  - 0
  - 102
- [Yazılım Güncell