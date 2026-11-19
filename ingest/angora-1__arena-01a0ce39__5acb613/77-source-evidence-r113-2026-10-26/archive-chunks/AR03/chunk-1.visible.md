ighbors`

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

LLDP kullanımı, denetlenmesi ve yapılandırması için gereken tüm komutlar ilgili bilgiye, [LLDP komut satırı rehberinden](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=management-link-layer-discovery-protocol-lldp) ulaşabilirsiniz.

### Was this article helpful?

[Yes](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp#) [No](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp#)

### Related Articles

- [Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)")  - 0
  - 366
- [Sistem Bilgilerini Öğrenme](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "Sistem Bilgilerini Öğrenme")  - 0
  - 381
- [Komut Satırı kullanımı](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "Komut Satırı kullanımı")  - 0
  - 496
- [Hızlı Başlangıç Kılavuzu](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=hizli-baslangic-kilavuzu "Hızlı Başlangıç Kılavuzu")  - 1
  - 382
- [Yazılım Güncelleme (TFTP/USB) – Verge Anahtarlar](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar "Yazılım Güncelleme (TFTP/USB) – Verge Anahtarlar")  - 2
  - 453
- [Stacking](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=stacking "Stacking")  - 2
  - 473

### Leave A Comment? [Cancel Reply](https://web.archive.org/web/20211128053947/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp\#respond)

Save my name, email, and website in this browser for the next time I comment.