[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")

[6 captures](https://web.archive.org/web/*/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "See a list of every capture for this URL")

27 Feb 2021 - 11 Feb 2025

|     |     |     |
| --- | --- | --- |
| [Jun](https://web.archive.org/web/20240623120603/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "12:06:03 Jun 23, 2024") | FEB | Mar |
| [12:06:03 Jun 23, 2024](https://web.archive.org/web/20240623120603/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "12:06:03 Jun 23, 2024") | 11 |  |
| [2022](https://web.archive.org/web/20220630231239/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "23:12:39 Jun 30, 2022") | 2025 | 2026 |

success

fail
[Share via My Web Archive](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme# "Share via My Web Archive") [Sign In](https://archive.org/account/login.php "Sign In")[Get some help using the Wayback Machine](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine")[Close the toolbar](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme#close "Close the toolbar")

[screenshot](https://web.archive.org/web/20250211062334/http://web.archive.org/screenshot/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "screenshot")[video](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme# "video")[Share on Facebook](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme# "Share on Facebook")[Share on Twitter](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme# "Share on Twitter")

[About this capture](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme#expand)

TIMESTAMPS

![loading](https://web-static.archive.org/_static/images/loading.gif)

The Wayback Machine - https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht\_kb=sistem-bilgilerini-ogrenme

# Knowledge Base

Search ForSearch

1. [Home](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/ "Home")
2. [Knowledge Base](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?post_type=ht_kb "Knowledge Base")
3. [How To Guides](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb_category=how-to-guides "View all posts in How To Guides")
4. [Sistem Bilgilerini Öğrenme](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "Sistem Bilgilerini Öğrenme")

AngoraOS işletim sistemi ve komut satırı, kullandığınız cihazların anlık durumlarını öğrenmeniz için gereken komutları sağlamaktadır.

Bu bilgiler aynı zamanda ‘SNMP’ protokolü aracılığıyla, AngoraNMS yazılımı ve diğer yönetim platformları tarafından da okunabilmektedir.

Bu belgede operasyonel olarak ihtiyacınız olabilecek bazı komutlar anlatılmıştır. Daha detaylı komut bilgileri için [yönetim komutları bilgi sayfalarını](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb_category=management) ziyaret edebilirsiniz.

## Cihaz bilgileri

Kullandığınız cihazın seri numarası, mac adresleri ve çevresel karakteristiklerini öğrenmek için aşağıdaki komutları kullanabilirsiniz:

1. _show system_

_`SUPPORT#sh system`_

![](https://web.archive.org/web/20250211062334im_/https://support.angoranetworks.com/wp-content/uploads/2020/10/Screen-Shot-2020-10-18-at-21.21.36-1024x434.png)

Bu komut çıktısı size, cihazla ilgili temel bilgileri, modeli, ne kadar süredir açık olduğunu ve anlık iç sıcaklığını gösterir. Ayrıca cihazın tanımlı MAC adresini de görebilirsiniz.

2\. _show inventory_

_`SUPPORT#sh inventory`_

![](https://web.archive.org/web/20250211062334im_/https://support.angoranetworks.com/wp-content/uploads/2020/10/Screen-Shot-2020-10-18-at-21.26.48.png)

Bu komut çıktısı, cihaz donanımı ile ilgili bilgileri içerir.

3\. _show version_

_`SUPPORT#sh version`_

![](https://web.archive.org/web/20250211062334im_/https://support.angoranetworks.com/wp-content/uploads/2020/10/Screen-Shot-2020-10-18-at-21.28.37.png)

Bu komut çıktısı, cihazda o anda çalışan ve yedek olarak kullanılabilecek aktif olmayan yazılım dosyalarını ve sürümlerini gösterir.

Active-image olarak tanımlanan yazılım, kullanımda olan yazılımdır. Inactive-image ise kullanıma hazır yedek yazılımdır. Yedek yazılımın aktif olarak kullanılabilmesi için, seçildikten sonra, cihazın yeniden başlatılması gerekir.

4\. _show cpu utilization_

_`SUPPORT#sh cpu utilization`_

![](https://web.archive.org/web/20250211062334im_/https://support.angoranetworks.com/wp-content/uploads/2020/10/Screen-Shot-2020-10-18-at-21.34.13.png)

Bu komut, son 5 saniye, son 1 dakika ve son 5 dakikalık aralıklardaki ortalama işlemci kullanımını göstermektedir. Normal operasyonda anahtar işlemcisi, herhangi bir anahtarlama işlemine dahil olmaz. İşlemcinin görevi, yönetimsel arayüzlerin anahtar donanımı ile arasındaki bağı kurmaktır. İşlemcinin sürekli olarak yüksek seyrettiği cihazlarda, bir yapılandırma hatası ya da donanım sorunu olduğu düşünülebilir.

### Was this article helpful?

[Yes](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme#) [No](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme#)

### Related Articles

- [Software Upgrade (TFTP/USB) – Verge Switches](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge "Software Upgrade (TFTP/USB) – Verge Switches")  - 0
  - 688
- [Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)")  - 3
  - 1237
- [Link Katmanı Keşif Protokolü (LLDP)](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "Link Katmanı Keşif Protokolü (LLDP)")  - 0
  - 1209
- [Komut Satırı kullanımı](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "Komut Satırı kullanımı")  - 0
  - 1601
- [Hızlı Başlangıç Kılavuzu](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=hizli-baslangic-kilavuzu "Hızlı Başlangıç Kılavuzu")  - 1
  - 928
- [Yazılım Güncelleme (TFTP/USB) – Verge Anahtarlar](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar "Yazılım Güncelleme (TFTP/USB) – Verge Anahtarlar")  - 3
  - 981

### Leave A Comment? [Cancel Reply](https://web.archive.org/web/20250211062334/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme\#respond)

Save my name, email, and website in this browser for the next time I comment.