[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")

[5 captures](https://web.archive.org/web/*/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "See a list of every capture for this URL")

28 Nov 2021 - 11 Feb 2025

|     |     |     |
| --- | --- | --- |
| Oct | NOV | [Jun](https://web.archive.org/web/20220630224645/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "22:46:45 Jun 30, 2022") |
|  | 28 | [22:46:45 Jun 30, 2022](https://web.archive.org/web/20220630224645/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "22:46:45 Jun 30, 2022") |
| 2020 | 2021 | [2024](https://web.archive.org/web/20240221051341/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "05:13:41 Feb 21, 2024") |

success

fail
[Share via My Web Archive](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp# "Share via My Web Archive") [Sign In](https://archive.org/account/login.php "Sign In")[Get some help using the Wayback Machine](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine")[Close the toolbar](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp#close "Close the toolbar")

[screenshot](https://web.archive.org/web/20211128053947/http://web.archive.org/screenshot/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "screenshot")[video](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp# "video")[Share on Facebook](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp# "Share on Facebook")[Share on Twitter](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp# "Share on Twitter")

[About this capture](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp#expand)

TIMESTAMPS

![loading](https://web-static.archive.org/_static/images/loading.gif)

The Wayback Machine - https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht\_kb=link-katmani-kesif-protokolu-lldp

# Knowledge Base

Search ForSearch

1. [Home](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/ "Home")
2. [Knowledge Base](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?post_type=ht_kb "Knowledge Base")
3. [How To Guides](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb_category=how-to-guides "View all posts in How To Guides")
4. [Link Katmanı Keşif Protokolü (LLDP)](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "Link Katmanı Keşif Protokolü (LLDP)")

LLDP protokolü birbirlerine bir kablo ile bağlanarak komşu haline gelmiş cihazların, birbirleri arasında kimlik bilgilerini değişmeleri amacıyla oluşturulmuştur. IEEE 802.1AB protokol numarası ile tanımlanmıştır. Protokol detaylarına [IEEE sayfalarından](https://web.archive.org/web/20211128053947/https://standards.ieee.org/standard/802_1AB-2016.html) ulaşabilirsiniz.

LLDP herhangi bir üreticiye ait özel bir standart değildir. Bu özelliği sayesinde farklı marka üreticilere ait cihazlar arasında çalışabilmektedir.

Yerel ağda kullanılan yedekli bağlantılar ve bunlar sonucu oluşan karmaşık topolojiler içinde, cihazların bilgilerini paylaşmasına ve yöneticiler tarafında ulaşılmasına olanak verir. LLDP yönetim sistemleri tarafından da topoloji keşfi amacıyla kullanılır.

Cisco tarafından kullanılan CDP (Cisco Discovery Protokolü) ile benzer özellikler taşımaktadır. Ancak LLDP nin farklı üreticiler tarafından desteklenen açık bir standart olması, marka bağımsız ağlarda tercih edilmesine neden olur.

LLDP ile ilgili daha detaylı bilgilere [IEEE](https://web.archive.org/web/20211128053947/https://standards.ieee.org/standard/802_1AB-2016.html) ve [Wikipedia](https://web.archive.org/web/20211128053947/https://en.wikipedia.org/wiki/Link_Layer_Discovery_Protocol) üzerinde ulaşabilirsiniz.

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

`switch#sh lldp ne