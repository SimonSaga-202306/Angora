[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")

[6 captures](https://web.archive.org/web/*/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "See a list of every capture for this URL")

27 Feb 2021 - 23 Jan 2025

|     |     |     |
| --- | --- | --- |
| [Jun](https://web.archive.org/web/20240623101933/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "10:19:33 Jun 23, 2024") | JAN | Feb |
| [10:19:33 Jun 23, 2024](https://web.archive.org/web/20240623101933/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "10:19:33 Jun 23, 2024") | 23 |  |
| [2022](https://web.archive.org/web/20220630214952/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "21:49:52 Jun 30, 2022") | 2025 | 2026 |

success

fail
[Share via My Web Archive](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp# "Share via My Web Archive") [Sign In](https://archive.org/account/login.php "Sign In")[Get some help using the Wayback Machine](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine")[Close the toolbar](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp#close "Close the toolbar")

[screenshot](https://web.archive.org/web/20250123060822/http://web.archive.org/screenshot/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "screenshot")[video](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp# "video")[Share on Facebook](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp# "Share on Facebook")[Share on Twitter](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp# "Share on Twitter")

[About this capture](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp#expand)

TIMESTAMPS

![loading](https://web-static.archive.org/_static/images/loading.gif)

The Wayback Machine - https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht\_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp

# Knowledge Base

Search ForSearch

1. [Home](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/ "Home")
2. [Knowledge Base](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?post_type=ht_kb "Knowledge Base")
3. [How To Guides](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb_category=how-to-guides "View all posts in How To Guides")
4. [Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)")

Angora kenar anahtarları ağ yöneticilerinin cihazları devreye alma süreçlerini en hızlı ve sorunsuz hale getirmeye yarayan fonksiyonlar içermektedir.

Günümüzde özellikle yazılım tabanlı geniş alan ağ ürünlerinde (Software Defined WAN ya da SD-WAN) önemli bir özellik olarak belirtilen dokunamdan devreye alma özelliği Angora kenar anahtar ürünlerinde ilk yazılım sürümünden itibaren bulunmaktadır.

Angora Networks ürün döngüsünün temel felsefesi olan marka bağımlılığı yaratmama yaklaşımı sayesinde, tamamen standart protokoller kullanarak cihazlarınızı ayağa kaldırabilirsiniz.

Bu özellik DHCP protokolü ile IP adresi edinme ve bu adresi öğrenirken alınan diğer seçenek bilgilerini kullanarak temel yapılandırma dosyalarını TFTP protokolü vasıtasıyla cihaza çekmek yöntemi ile çalışır.

Temel olarak kurulumunu yaptığınız cihazın DHCP sunucudan IP adresi alabilmesi ve DHCP sunucudan aldığı dosya ve erişim bilgileri ile TFTP sunucuya erişebilmesi yeterlidir.

Kutusundan yeni çıkardığınız bir Angora Verge kenar anahtarının temel güvenlik ve ağ yapılandırmasını bu şekilde yaparak ağınıza dahil edebilirsiniz.

Bunun için cihaz bağlantısı üzerinden gelecek DHCP isteklerine cevap alınabilmelidir. DHCP adresi alındıktan sonra yapılandırma için DHCP cevabında gelen TFTP sunucu ve dosya adı ile istek gönderilir. Bu isteğe cevaben gelen dosyada istenilen tüm yapılandırma bulunabilir. Cihaz bu dosyayı aldığında hemen çalışan yapılandırmasına ekler ve daha sonra bu yapılandırma üzerinde tanımlanan şekilde çalışmaya başlar.

DHCP sunucu üzerindeki kapsam (scope) içinde ip adresi, maskesi ve geçerli bir ağ geçidi haricinde, aşağıdaki seçenek numara ve içeriklerinin (option) tanımlanması gereklidir:

`66: TFTP Sunucu Adresi (Ip Adresi, Ör: 10.6.104.15)`

`67: Yapılandırma Dosyası (Dosya adı, Ör: yapilandirma.txt)`

Cihaz DHCP sunucusunda yukarıdaki bilgileri alabilir ve gelen seçeneklerde tanımlı TFTP sunucusundan erişebilirse, yapılandırma dosyasını alarak, dokunamadan tüm ayarlara sahip olabilir.

### Was this article helpful?

[Yes](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp#) [No](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp#)

### Related Articles

- [Software Upgrade (TFTP/USB) – Verge Switches](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge "Software Upgrade (TFTP/USB) – Verge Switches")  - 0
  - 669
- [Sistem Bilgilerini Öğrenme](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "Sistem Bilgilerini Öğrenme")  - 1
  - 829
- [Link Katmanı Keşif Protokolü (LLDP)](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "Link Katmanı Keşif Protokolü (LLDP)")  - 0
  - 1189
- [Komut Satırı kullanımı](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "Komut Satırı kullanımı")  - 0
  - 1587
- [Hızlı Başlangıç Kılavuzu](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=hizli-baslangic-kilavuzu "Hızlı Başlangıç Kılavuzu")  - 1
  - 917
- [Yazılım Güncelleme (TFTP/USB) – Verge Anahtarlar](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar "Yazılım Güncelleme (TFTP/USB) – Verge Anahtarlar")  - 3
  - 971

### Leave A Comment? [Cancel Reply](https://web.archive.org/web/20250123060822/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp\#respond)

Save my name, email, and website in this browser for the next time I comment.