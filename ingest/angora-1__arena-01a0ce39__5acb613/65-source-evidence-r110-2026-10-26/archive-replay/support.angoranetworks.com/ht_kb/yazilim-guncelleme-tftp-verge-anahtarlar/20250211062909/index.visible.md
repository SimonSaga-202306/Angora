[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")

[2 captures](https://web.archive.org/web/*/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar "See a list of every capture for this URL")

28 Nov 2021 - 11 Feb 2025

|     |     |     |
| --- | --- | --- |
| [Nov](https://web.archive.org/web/20211128060707/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar "06:07:07 Nov 28, 2021") | FEB | Mar |
| [06:07:07 Nov 28, 2021](https://web.archive.org/web/20211128060707/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar "06:07:07 Nov 28, 2021") | 11 |  |
| [2021](https://web.archive.org/web/20211128060707/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar "06:07:07 Nov 28, 2021") | 2025 | 2026 |

success

fail
[Share via My Web Archive](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar# "Share via My Web Archive") [Sign In](https://archive.org/account/login.php "Sign In")[Get some help using the Wayback Machine](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine")[Close the toolbar](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar#close "Close the toolbar")

[screenshot](https://web.archive.org/web/20250211062909/http://web.archive.org/screenshot/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar "screenshot")[video](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar# "video")[Share on Facebook](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar# "Share on Facebook")[Share on Twitter](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar# "Share on Twitter")

[About this capture](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar#expand)

TIMESTAMPS

![loading](https://web-static.archive.org/_static/images/loading.gif)

The Wayback Machine - https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht\_kb=yazilim-guncelleme-tftp-verge-anahtarlar

# Knowledge Base

Search ForSearch

1. [Home](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/ "Home")
2. [Knowledge Base](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?post_type=ht_kb "Knowledge Base")
3. [How To Guides](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb_category=how-to-guides "View all posts in How To Guides")
4. [Yazılım Güncelleme (TFTP/USB) – Verge Anahtarlar](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar "Yazılım Güncelleme (TFTP/USB) – Verge Anahtarlar")

Bu yazı Angora Networks kenar anahtar cihazlarının sistem yazılımının TFTP protokolü veya USB dosya transferi aracılığı ile güncellenmesi anlatmaktadır.

Angora Networks kenar anahtarlarında kullanılan AngoraOS işletim sistemi kurumsal ağlar için stabil, yenilikçi ve kritik hizmetleri devreye almakta kullanılan ağ altyapısı yazılımıdır. İhtiyaç duyulan yüzlerce özellik ve yeni talepleri desteklemek amacıyla işletim sisteminde sürekli iyileştirmeler ve geliştirmeler yapılmaktadır.

Bu geliştirmeleri, tüm fonksiyonları ile kullanmak için en güncel sürüm yazılımın anahtarlara yüklenmesi gerekmektedir.

En güncel AngoraOS yazılımlarına [Angora Servis Portalinden](https://web.archive.org/web/20250211062909/https://servis.angora.networks/) ulaşabilirsiniz.

## **Ön Hazırlık**

Cihazların yazılım güncellemelerini TFTP protokolü ile yapacaksanız, başlamadan önce, bazı yardımcı yazılımların ve gerekli bağlantıların hazır hale getirilmesi gereklidir. Gerekli hazırlık adımları şunlardır:

1. TFTP (Trivial Transfer File Protocol) uygulaması: Bir TFTP sunucusu erişilebilir olacak şekilde yapılandırılmalı.
2. En güncel AngoraOS dosyasının TFTP sunucuda erişilecek klasör dizinine yüklenmelidir.
3. Dosya aktarımı sırasında herhangi bir kesinti durumunda müdahale edebilmek için anahtarlama cihazına konsol portundan erişim sağlanmalı. (Tüm yazılım güncelleme işlemleri uzak bağlantı ile yapılabilmektedir. Olası kesinti ve hata durumlarında komut satırı erişiminin kaybolmaması için, yerel konsol bağlantısı ile işlemlerin yapılması önerilmektedir)
4. Anahtar ve TFTP sunucu ağ üzerinden birbirine erişebilir olmalıdır. (Kesinti ve gecikmelerden etkilenmemek için anahtar portlarında birine bağlanacak bir PC üzerinde TFTP sunucu çalıştırılması, en güvenilir yöntemdir)

Aşağıdaki şekilde lokal bilgisayar üzerinden güncelleme yapılabilmesi için oluşturulmuş yapı görülmektedir.

![TFTP Upgrade](https://web.archive.org/web/20250211062909im_/https://support.angoranetworks.com/wp-content/uploads/2020/09/image.png)

Şekil 1 – Lokal Cihaz ile güncelleme

* * *

Güncelleme için USB disk kullanacaksanız, dosyayı barındıran diskin FAT32 veya ExFAT biçiminde olduğuna emin olun.

## **Güncelleme adımları**

Güncellemeye başlamadan önce, mevcut aktif ve pasif yazılımların sürümlerini not almayı unutmayın. Bunun için aşağıdaki komutu kullanabilirsiniz:

_`#show version`_

Bu komut size aşağıdaki gibi bir çıktı verecektir.

![](https://web.archive.org/web/20250211062909im_/https://support.angoranetworks.com/wp-content/uploads/2020/09/image-1.png)

Şekil 2 – Aktif ve Pasif yazılım sürümleri

* * *

Bu çıktı da “Active-image” ve “Inactive-image” olarak iki adet yazılım dosyası görüntülenmektedir. Active-image, mevcut durumda çalışan yazılımı, inactive-image ihtiyaç durumunda kullanıma alınabilecek yazılımı göstermektedir.

TFTP sunucusu erişilebilir olduktan sonra, aşağıdaki komut ile yazılım güncellemesi işlemi başlatılabilir:

- `TFTP sunucu adresi: 192.168.1.11`
- `Yüklenecek yazılım dosyası: image_5.5.3.03.bin`

_`boot system tftp://192.168.1.11/image_5.5.3.03.bin`_

![](https://web.archive.org/web/20250211062909im_/https://support.angoranetworks.com/wp-content/uploads/2020/09/image-2.png)

Şekil 3 – Yazılım güncelleme süreci

* * *

Yüklemeyi USB disk üzerinden yapmak için, diski cihazın ön bölümünde bulunan yuvaya takın.

USB diskin tanınması 8-10 saniye kadar sürecektir. Bu sürede USB disk hazır olmazsa, yeniden biçimlendirmeyi deneyin.

Aşağıdaki komutu girerek USB üzerinden dosya güncellemesini başlatabilirsiniz:

_`boot system usb://image_5.5.3.03.bin`_

Yüklenen sürüm dosyası “Inactive-image” olarak kaydedilir ve sonraki başlatmada devreye alınacak şekilde tanımlanır.

![](https://web.archive.org/web/20250211062909im_/https://support.angoranetworks.com/wp-content/uploads/2020/09/image-3.png)

Şekil 4 – Yükleme sonucu yazılım durumları

* * *

Yukarıdaki çıktı görüntülendiğinde, yazılım cihaza atılmış, ve devreye alınmaya hazır hale gelmiştir.

İstendiği zaman anahtar tekrar başlatılarak, yeni yazılım aktif duruma alınabilir. Cihazı tekrar başlatmak için aşağıdaki komut girilmelidir:

_`#reload`_

Cihaz yeniden başlatılacağı için yapılandırma değişiklikleri yapıldıysa, işlem yapılmadan önce çalışan yapılandırmanın kaydı, açılış yapılandırması üzerine `“write memory”` komutu ile kaydedilmelidir.

![](https://web.archive.org/web/20250211062909im_/https://support.angoranetworks.com/wp-content/uploads/2020/09/image-4.png)

_Şekil 5 – Yeniden başlatma_

* * *

Anahtar açıldığında tekrar _`"show version"`_ komutu çalıştırılırsa, Active-image bölümünün güncellendiği ve yeni yüklenen sürümün devreye alındığı görülecektir.

![](https://web.archive.org/web/20250211062909im_/https://support.angoranetworks.com/wp-content/uploads/2020/09/image-5.png)

Şekil 6 – Yükleme sonucu

### Was this article helpful?

[Yes](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar#) [No](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar#)

### Related Articles

- [Software Upgrade (TFTP/USB) – Verge Switches](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=software-upgrade-tftp-verge "Software Upgrade (TFTP/USB) – Verge Switches")  - 0
  - 688
- [Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)")  - 3
  - 1237
- [Sistem Bilgilerini Öğrenme](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "Sistem Bilgilerini Öğrenme")  - 1
  - 843
- [Link Katmanı Keşif Protokolü (LLDP)](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "Link Katmanı Keşif Protokolü (LLDP)")  - 0
  - 1209
- [Komut Satırı kullanımı](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "Komut Satırı kullanımı")  - 0
  - 1601
- [Hızlı Başlangıç Kılavuzu](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=hizli-baslangic-kilavuzu "Hızlı Başlangıç Kılavuzu")  - 1
  - 928

### Leave A Comment? [Cancel Reply](https://web.archive.org/web/20250211062909/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar\#respond)

Save my name, email, and website in this browser for the next time I comment.