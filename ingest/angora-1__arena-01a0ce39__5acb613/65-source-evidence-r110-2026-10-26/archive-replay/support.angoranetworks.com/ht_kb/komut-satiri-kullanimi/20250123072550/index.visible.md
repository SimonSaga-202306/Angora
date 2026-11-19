[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")

[5 captures](https://web.archive.org/web/*/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "See a list of every capture for this URL")

28 Nov 2021 - 23 Jan 2025

|     |     |     |
| --- | --- | --- |
| [Jun](https://web.archive.org/web/20240623114636/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "11:46:36 Jun 23, 2024") | JAN | Feb |
| [11:46:36 Jun 23, 2024](https://web.archive.org/web/20240623114636/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "11:46:36 Jun 23, 2024") | 23 |  |
| [2022](https://web.archive.org/web/20220630225257/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "22:52:57 Jun 30, 2022") | 2025 | 2026 |

success

fail
[Share via My Web Archive](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi# "Share via My Web Archive") [Sign In](https://archive.org/account/login.php "Sign In")[Get some help using the Wayback Machine](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine")[Close the toolbar](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi#close "Close the toolbar")

[screenshot](https://web.archive.org/web/20250123072550/http://web.archive.org/screenshot/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "screenshot")[video](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi# "video")[Share on Facebook](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi# "Share on Facebook")[Share on Twitter](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi# "Share on Twitter")

[About this capture](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi#expand)

TIMESTAMPS

![loading](https://web-static.archive.org/_static/images/loading.gif)

The Wayback Machine - https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht\_kb=komut-satiri-kullanimi

# Knowledge Base

Search ForSearch

1. [Home](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/ "Home")
2. [Knowledge Base](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?post_type=ht_kb "Knowledge Base")
3. [How To Guides](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb_category=how-to-guides "View all posts in How To Guides")
4. [Komut Satırı kullanımı](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "Komut Satırı kullanımı")

Bu belge, komut satırı üzerinden, anahtar fonksiyonlarının nasıl yapılandırılacağını anlatmaktadır. Farklı fonksiyonlar ile ilgili detaylı yapılandırmalara geçmeden önce, komut satırı arayüzünün nasıl kullanılabileceğini anlamak daha uygun olacaktır.

## Kullanıcı yetki seviyeleri

Anahtarı işletmeye
yetkili kullanıcılar aşağıdaki yetki seviyelerinde yaratılabilir.

- **Seviye 1:** Bu kullanıcı seviyesi, sadece monitör yetkilerine sahiptir. Bu seviyedeki kullanıcı grafik arayüzüne giriş yapamaz ve yapılandırma üzerinde değişiklik yapamaz.
- **Seviye 15:** Bu kullanıcı seviyesi tüm komutları çalıştırabilir, grafik arayüzüne ulaşabilir ve istediği yapılandırma değişikliklerini yapabilir.

Bir kullanıcının
Seviye 15 yetkilerini kullanabilmesi için, özel yönetim alanına (privileged
mode) geçmesi gerekir. Bu geçiş için aşağıdaki komut kullanılır:

```
switch#enable
```

Bu komut girildiğinde, bir parola sorulur. Doğru parola sağlanırsa yetki alanı değişimi sağlanır. Bu parola, yapılandırma alanında, aşağıdaki komut ile tanımlanır.

`switch<conf>#enable password level [seviye] [parola]`

_`ÖRNEK: switch<conf>#enable password 15 seviye15parola`_

Geçilen seviye sadece mevcut oturum için geçerlidir. Yeni bir oturuma giriş yapıldığında seviyenin artırılması için yeniden ‘enable’ komutu kullanılmalıdır.

Kullanıcı Komut Alanına
dönmek için aşağıdaki komut kullanılır:

_`switch#disable`_

Kullanıcı kimlik doğrulaması RADIUS veya TACACS protokolleri kullanılarak yapılıyorsa, kullanıcının seviye 15 erişimi için gereken parola, harici bir sunucu da tanımlanmalıdır. Bu protokollerin kullanımı Kimlik Doğrulama belgelerinde anlatılmaktadır.

## Komut Satırı Alanları

Cihazları daha verimli yönetmek için, komut satırı farklı alanlara ayrılmıştır.  Her alan kendi özel komut setlerini içerir.

Alanların sıralaması ilk
erişildikleri nokta itibariyle, yetki seviyesine göre şöyledir:

1. Kullanıcı komut alanı
2. Yetkili komut alanı
3. Genel yapılandırma alanı
4. Arayüz yapılandırma alanı

### Kullanıcı Komut Alanı

Yeni bir yönetim oturumu başlatıldığında, ilk ulaşılan alan ‘Kullanıcı Komut Alanı’ dır. Bu alanda sınırlı sayıda komuta izin verilir ve sadece yapılandırma değişimi olmayan, temel monitörleme, basit testler ve sistem bilgilerine erişim gibi  görevler yerine getirilir.

Kullanıcı komut alanı, cihaz adının yanında bir büyüktür işareti ile tanınır:

_`switch>`_

Cihazların varsayılan isimi kullanılan sürüme
göre, ‘console’ ya da ‘switch’ olarak tanımlanmıştır. Bu isim Yapılandırma Alanında
aşağıdaki komut ile değiştirilir:

`switch<conf>#hostname [cihaz ismi]`

### Yetki Komut Alanı

Yetki Komut Alanı, yetkili kullanıcıların parola kullanarak geçebildikleri alandır. Bu alan, daha detaylı görüntülemeye ve yapılandırmaya izin verir. Güvenlik nedenlerinden dolayı parola girişi yapılırken, tuşlanan karakterler ekranda gözükmez.

Kullanıcı tanımı yapılırken yetki seviyesi 15
olarak tanımlanmış kullanıcılar, kimlik bilgilerini girdiklerinde doğrudan
Yetki Komut Alanı’na girerler.

Seviyeleri 1 olan kullanıcılar, Yetki Komut Alanı’na
giriş yapmak için aşağıdaki komutu kullanmalıdır:

_`switch>enable`_

Kullanıcı Komut Alanı’na dönüş için aşağıdaki komut
kullanılmalıdır:

_`switch#disable`_

### Genel Yapılandırma Alanı

Bu alanda çalıştırılan komutlar, tüm sistem üzerinde etkisi olan yapılandırmaları düzenlemek için kullanılır.

Genel Yapılandırma Alanı’na geçiş yapmak için, Yetki Komut Alanı’nda
aşağıdaki komut kullanılır:

_`switch#configure`_

Bu komut sonucunda alan değişimi sağlanır. Genel Yapılandırma
alanında, komut satırı aşağıdaki gibi gözükür:

_`switch(config)#`_

Bu alandan Yetki Komut Alanı’na geri dönmek için **_CTRL+Z_** kısayolunu ya da aşağıdaki iki komuttan birini kullanabilirsiniz:

_`switch(config)# exit`_

_`switch(config)# end`_

### Arayüz yapılandırma Alanı

Bu alandaki komutlar sadece belli arayüzler üzerindeki
yapılandırma için kullanılır.

**Erişim (Line) arayüzleri:** Yönetim bağlantılarını yapılandırmak için kullanılan komutları içerir. Bağlantı hızı, zaman aşımı ayarları gibi yapılandımalar burada ayarlanır. Genel yapılandırma Alanı’nda aşağıdaki komut kullanılarak giriş yapılır:

_`switch(config)# line [bağlantı tipi]`_

_`switch(config-line)#`_

**VLAN Veritabanı:** VLAN tanımlamaları için gereken tüm komutları içerir. Bu alana girmek için aşağıdaki komut kullanılır:

_`switch(config)# vlan database`_

_`switch(config-vlan)#`_

**Yönetim Erişim Listeleri:** Yönetim amaçlı erişim listeleri tanımlamayı sağlayan komutları içerir. Bu alana girmek için aşağıdaki komut kullanılır:

_`switch(config)# management access-list [isim]`_

_`switch(config-macl)#`_

**Port kanalları:** Birleşik portlar tanımlamayı sağlayan komutları içerir. Bu alana girmek için aşağıdaki komut kullanılır:

_`switch(config)# interface` **`port-channel`**` [sayı]`_

_`switch(config-if)#`_

**Arayüz:** Tekil arayüzler üzerindeki  tanımlamaları sağlayan komutları içerir. Bu alana girmek için aşağıdaki komut kullanılır:

_`switch(config)# interface` **`[arayüz tipi]`**` [arayüz numarası]`_

_`switch(config-if)#`_

Angora anahtarlar üzerinde farklı tiplerde arayüzler bulunmaktadır.
Aşağıda arayüz tipleri ve komut satırında kullanılan kısaltmaları
listelenmiştir:

- **GigabitEthernet arayüzleri (10/100/1000 bits)**— **GigabitEthernet** veya **gi** veya **GE.**
- **TenGigabit thernet ports (10000 bits)**— **TenGigabitEthernet** veya **te** veya **xg.**
- **LAG (Port Channel)**— **Port-Channel** veya **po.**
- **VLAN**— **VLAN**
- **Tunnel**— **tunnel** veya **tu**

Fiziksel arayüzlerin numaralandırmaları, cihaz üzerinde yazılmıştır. Yapılandırma sırasında istenilen arayüzü seçmek için,

_`[Cihaz Numarası/0/Arayüz Numarası]`_

şeklinde seçim yapılmalıdır. Cihaz bir yığın grubu içerisinde çalıştırılmıyorsa, numarası her zaman 1 (bir) olur. Eğer cihaz yığın grubu içerisinde ise, cihaz numarası önceden tanımlanan değerdir ( _unit-id_).

Genel arayüz seçimi aşağıdaki şekildedir:

_`switch(config)#`_`` _`interface[ ][<cihaz-numarası>/]<0>/<arayüz numarası>}  | {port-channel | po | ch}[ ]<port-channel numarası > | {tunnel | tu}[ ]<tunnel numarası > | vlan[ ]<vlan-id>`_

Aşağıda farklı
arayüzler için örnekler listelenmiştir:

_`switch(config)#interface GigabitEthernet 1/1/1`_

_`switch(config)#interface GE 1/1/1`_

_`switch(config)#interface gi1/1/1`_

_`switch(config)#interface FastEthernet 1/2/1`_

_`switch(config)#interface fe1/2/1`_

_`switch(config)#interface po1`_

_`switch(config)#interface vlan 1`_

### Arayüz aralığı

Birbirini takip eden arayüzler için aynı yapılandırmaya
ihtiyaç duyulduğunda, aralık seçilerek işlem yapılır. Aralık seçildikten sonra
yapılan tüm değişiklikler, tüm arayüzlere uygulanır.

Aralık seçimi
için aşağıdaki komut yapısı kullanılır:

_`switch(config)#interface` **`range`**` [ilk arayüz numarası – son arayüz numarası]`_

_`switch(config)#interface range gi1/1/1-5`_

Aralık seçimi
yapılırken aşağıdaki örnekteki gibi farklı tipte arayüzler seçilebilir:

_`switch(config)#interface range gi1/1/1-5 , vlan 1-2`_

## Komutların girilmesi

Komut satırında giriş yapılırken, ana komuta parametre olarak ilaveler yapılması gerekir. Örneğin ‘ _show_’ komutu, anahtar yapılandırması ve karakteri ile ilgili bilgilerin görüntülenmesi için kullanılır. Bu komutun arkasına ilave edilecek parametreler ile, hangi fonksiyon ile ilgili bilgilerin gösterileceği belirlenir. Genel komut yapısı ve örnekleri aşağıdaki gibidir:

_`Ana komut +`_ **_`fonksiyonel argümanlar`_** _` + parametreler`_

_`ÖR: show`_ **_`interfaces switchport`_** _`  gi 1/0/1`_

Komutların girişi sırasında yardım almak için soru işareti (?) karakteri kullanılabilinir. Komut veya parametre yerine soru işareti karakterine basıldığında, kullanılabilecek kelimeler listelenir. Eğer komut veya parametrenin bir kısmı girildikten sonra soru işaretine basılırsa, girilen karakterler ile eşleşen olası kelimeler görüntülenir.

Önceden girilen komutları tekrar yazmadan kullanabilirsiniz. Klavyenizde bulunan yukarı ve aşağı tuşlarına basarak tanımlanmış derinliğe kadar geriye gitmeniz mümkündür. Konsol bağlantıları için varsayılan derinlik 10 komuttur. Bu değer istenilirse 256’ya kadar artırılabilinir. Ayrıca ‘ _show history_’ komutu ile önceki komutların listesine ulaşabilirsiniz.

Yapılandırma sırasında
girilen bir komutun geri alınması için aynı komutun başına ‘no’ anahtar kelimesi
girilmelidir. Bazı komutlar için geri alma esnasında, parametrelerin silinmesi
gerekebilir.

Komut girilirken ‘ _TAB_’ tuşuna bastığınızda, komut satırı arayüzü, girdiğiniz karakterle uyumlu komutları gösterir. Eğer uyumlu sadece bir komut veya parametre varsa, komut veya parametre tamamlanır. Eğer uyumlu komut yoksa herhangi bir değişiklik veya gösterim olmaz.

Komut için zorunlu olan
parametreler girilmeden çalıştırmak istenirse, komut satırı arayüzü aşağıdaki
hatayı verir.

_`(config)#interface`_

_`%missing mandatory parameter`_

_`(config)#interface`_

### Klavye kısayolları

Komut satırı kullanımınız kolaylaştıracak, klavye
kısayolları aşağıda listelenmiştir:

|     |     |
| --- | --- |
| **Klavye kısayolu** | **Tanım** |
| Yukarı tuşu | Hafızadaki bir önceki komutu tekrar gösterir. Tekrar<br> basıldığında önceki komutlara doğru görüntüleme devam eder. |
| Aşağı tuşu | Hafızadaki bir sonraki komutu tekrar gösterir. Tekrar<br> basıldığında sonraki komutlara doğru görüntüleme devam eder. Son komutun<br> ardından, boş satıra döner. |
| Ctrl+A | İmleci satırın en<br> başına götürür |
| Ctrl+E | İmleci satırın en sonuna<br> götürür |
| Ctrl+Z<br> / End | Tüm alanlardan, Yetkili komut alanına dönüşü sağlar. |
| Backspace/Ctrl+H | Yazılmış olan son karakteri siler |

### Was this article helpful?

[Yes](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi#) [No](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi#)

### Related Articles

- [Software Upgrade (TFTP/USB) – Verge Switches](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge "Software Upgrade (TFTP/USB) – Verge Switches")  - 0
  - 669
- [Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)")  - 3
  - 1222
- [Sistem Bilgilerini Öğrenme](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "Sistem Bilgilerini Öğrenme")  - 1
  - 829
- [Link Katmanı Keşif Protokolü (LLDP)](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "Link Katmanı Keşif Protokolü (LLDP)")  - 0
  - 1189
- [Hızlı Başlangıç Kılavuzu](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=hizli-baslangic-kilavuzu "Hızlı Başlangıç Kılavuzu")  - 1
  - 917
- [Yazılım Güncelleme (TFTP/USB) – Verge Anahtarlar](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar "Yazılım Güncelleme (TFTP/USB) – Verge Anahtarlar")  - 3
  - 971

### Leave A Comment? [Cancel Reply](https://web.archive.org/web/20250123072550/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi\#respond)

Save my name, email, and website in this browser for the next time I comment.