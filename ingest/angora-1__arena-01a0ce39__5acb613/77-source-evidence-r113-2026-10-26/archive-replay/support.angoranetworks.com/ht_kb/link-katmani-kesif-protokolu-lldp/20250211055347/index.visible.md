[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")

[5 captures](https://web.archive.org/web/*/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "See a list of every capture for this URL")

28 Nov 2021 - 11 Feb 2025

|     |     |     |
| --- | --- | --- |
| [Jun](https://web.archive.org/web/20240623113414/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "11:34:14 Jun 23, 2024") | FEB | Mar |
| [11:34:14 Jun 23, 2024](https://web.archive.org/web/20240623113414/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "11:34:14 Jun 23, 2024") | 11 |  |
| [2022](https://web.archive.org/web/20220630224645/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "22:46:45 Jun 30, 2022") | 2025 | 2026 |

success

fail
[Share via My Web Archive](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp# "Share via My Web Archive") [Sign In](https://archive.org/account/login.php "Sign In")[Get some help using the Wayback Machine](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine")[Close the toolbar](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp#close "Close the toolbar")

[screenshot](https://web.archive.org/web/20250211055347/http://web.archive.org/screenshot/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "screenshot")[video](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp# "video")[Share on Facebook](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp# "Share on Facebook")[Share on Twitter](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp# "Share on Twitter")

[About this capture](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp#expand)

TIMESTAMPS

![loading](https://web-static.archive.org/_static/images/loading.gif)

The Wayback Machine - https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht\_kb=link-katmani-kesif-protokolu-lldp

# Knowledge Base

Search ForSearch

1. [Home](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/ "Home")
2. [Knowledge Base](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?post_type=ht_kb "Knowledge Base")
3. [How To Guides](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb_category=how-to-guides "View all posts in How To Guides")
4. [Link Katmanı Keşif Protokolü (LLDP)](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "Link Katmanı Keşif Protokolü (LLDP)")

LLDP protokolü birbirlerine bir kablo ile bağlanarak komşu haline gelmiş cihazların, birbirleri arasında kimlik bilgilerini değişmeleri amacıyla oluşturulmuştur. IEEE 802.1AB protokol numarası ile tanımlanmıştır. Protokol detaylarına [IEEE sayfalarından](https://web.archive.org/web/20250211055347/https://standards.ieee.org/standard/802_1AB-2016.html) ulaşabilirsiniz.

LLDP herhangi bir üreticiye ait özel bir standart değildir. Bu özelliği sayesinde farklı marka üreticilere ait cihazlar arasında çalışabilmektedir.

Yerel ağda kullanılan yedekli bağlantılar ve bunlar sonucu oluşan karmaşık topolojiler içinde, cihazların bilgilerini paylaşmasına ve yöneticiler tarafında ulaşılmasına olanak verir. LLDP yönetim sistemleri tarafından da topoloji keşfi amacıyla kullanılır.

Cisco tarafından kullanılan CDP (Cisco Discovery Protokolü) ile benzer özellikler taşımaktadır. Ancak LLDP nin farklı üreticiler tarafından desteklenen açık bir standart olması, marka bağımsız ağlarda tercih edilmesine neden olur.

LLDP ile ilgili daha detaylı bilgilere [IEEE](https://web.archive.org/web/20250211055347/https://standards.ieee.org/standard/802_1AB-2016.html) ve [Wikipedia](https://web.archive.org/web/20250211055347/https://en.wikipedia.org/wiki/Link_Layer_Discovery_Protocol) üzerinde ulaşabilirsiniz.

## Angora uygulaması

LLDP IEEE tarafından tanımlanan haliyle AngoraOS işletim sistemlerine eklenmiştir.

LLDP AngoraOS servisleri arasında, fabrika ayarlarında aktif halde gelmektedir. Eğer LLDP devre dışı bırakılmak istenirse, Genel Yapılandırma alanında aşağıdaki komut girilmelidir:

`switch(config)#no lldp run`

Eğer LLDP kapatılmış ise, aktif hale getirmek için aşağıdaki komut girilmelidir:

_`switch(config)#lldp run`_

Cihaz üzerinde çalışan LLDP yapılandırmasını görmek için aşağıdaki komut kullanılır:

`switch#show lldp configuration`

Bu komutun çıktısı aşağıdaki gibidir. Çıktıda gösterildiği gibi LLDP aktif haldedir. Bu çıktı her port için LLDP durumunu da göstermektedir.

`LLDP state: Enabled`

`Timer: 30 Seconds`

`Hold multiplier: 4`

`Reinit delay: 2 Seconds`

`Tx delay: 2 Seconds`

`Notifications Interval: 5 Seconds`

`LLDP packets handling: Filtering`

`Chassis ID: mac-address`

` Port       State       Optional TLVs          Address       Notifications`

`--------- ----------- -------------------- ----------------- ---------------`

`gi1/0/1    Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/2    Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/3    Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/4    Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/5    Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/6    Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/7    Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/8    Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/9    Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/10   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/11   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/12   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/13   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/14   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/15   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/16   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/17   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/18   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/19   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/20   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/21   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/22   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/23   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`gi1/0/24   Rx and Tx       SN, SC, 4W          automatic         Disabled`

`te1/0/1    Rx and Tx       SN, SC, 4W          automatic         Disabled`

`te1/0/2    Rx and Tx       SN, SC, 4W          automatic         Disabled`

`te1/0/3    Rx and Tx       SN, SC, 4W          automatic         Disabled`

`te1/0/4    Rx and Tx       SN, SC, 4W          automatic         Disabled`

LLDP her arayüz için ayrı ayrı yapılandırılabilir. Anahtar bilgisinin dışarı iletilmesinin istenmediği arayüzlerde protokol kapatılabilir.

LLDP kullanarak mevcut komşulukları görmek için aşağıdaki komut kullanılır:

`switch# show lldp neighbors`

Bu komutun çıktısında, aktif olan tüm portlardan alınan komşu cihazlara ait LLDP mesajları derlenmiştir:

`switch#sh lldp neighbors`

`System capability legend:`

`B - Bridge; R - Router; W - Wlan Access Point; T - telephone;`

`D - DOCSIS Cable Device; H - Host; r - Repeater;`

`TP - Two Ports MAC Relay; S - S-VLAN; C - C-VLAN; O - Other`

`  Port        Device ID          Port ID         System Name    Capabilities  TTL`

`--------- ----------------- ----------------- ----------------- ------------ -----`

`gi1/0/23  00:ae:45:67:00:00      gi1/0/5          NEIGH1          B, R      106`

`gi1/0/24  00:ae:45:67:00:00      gi1/0/3          NEIGH1          B, R      106`

Bir arayüzün komşuluk detaylarını görmek için aşağıdaki komut kullanılır:

`switch#sh lldp neighbors [arayüz tipi][arayüz numarası]`

Bu komutun çıktısı aşağıdaki gibidir:

`switch#sh lldp neighbors GigabitEthernet 1/0/23`

`Device ID: 00:ae:45:67:00:00`

`Port ID: gi1/0/5`

`Capabilities: Bridge, Router`

`System Name: NEIGH1`

`System description:`

`Port description:`

`Management Address: 192.168.1.17`

`Management Address: fe80::2ae:45ff:fe67:0`

`Time To Live: 107`

`802.3 Power via MDI:`

` MDI Power support Port Class: PSE`

` PSE MDI Power Support: Supported`

` PSE MDI Power State: Enabled`

` PSE power pair control ability:  Not supported`

` PSE Power Pair: Spare`

` PSE Power class: 1`

` Power Type: Type 2 PSE`

` Power Source: Back-up Power Source`

` Power Priority: low`

` PSE Allocated Power Value: 13.0`

LLDP kullanımı, denetlenmesi ve yapılandırması için gereken tüm komutlar ilgili bilgiye, [LLDP komut satırı rehberinden](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=management-link-layer-discovery-protocol-lldp) ulaşabilirsiniz.

### Was this article helpful?

[Yes](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp#) [No](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp#)

### Related Articles

- [Software Upgrade (TFTP/USB) – Verge Switches](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge "Software Upgrade (TFTP/USB) – Verge Switches")  - 0
  - 688
- [Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)")  - 3
  - 1237
- [Sistem Bilgilerini Öğrenme](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "Sistem Bilgilerini Öğrenme")  - 1
  - 842
- [Komut Satırı kullanımı](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "Komut Satırı kullanımı")  - 0
  - 1601
- [Hızlı Başlangıç Kılavuzu](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=hizli-baslangic-kilavuzu "Hızlı Başlangıç Kılavuzu")  - 1
  - 927
- [Yazılım Güncelleme (TFTP/USB) – Verge Anahtarlar](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar "Yazılım Güncelleme (TFTP/USB) – Verge Anahtarlar")  - 3
  - 981

### Leave A Comment? [Cancel Reply](https://web.archive.org/web/20250211055347/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp\#respond)

Save my name, email, and website in this browser for the next time I comment.