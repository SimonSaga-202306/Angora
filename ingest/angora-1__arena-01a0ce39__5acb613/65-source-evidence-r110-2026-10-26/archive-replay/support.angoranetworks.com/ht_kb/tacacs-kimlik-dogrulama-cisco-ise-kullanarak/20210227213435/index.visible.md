[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")

[5 captures](https://web.archive.org/web/20210227213435*/https://support.angoranetworks.com/?ht_kb=tacacs-kimlik-dogrulama-cisco-ise-kullanarak "See a list of every capture for this URL")

27 Feb 2021 - 30 May 2024

|     |     |     |
| --- | --- | --- |
| Jan | FEB | Mar |
|  | 27 |  |
| 2020 | 2021 | 2022 |

success

fail
[Share via My Web Archive](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=tacacs-kimlik-dogrulama-cisco-ise-kullanarak# "Share via My Web Archive") [Sign In](https://archive.org/account/login.php "Sign In")[Get some help using the Wayback Machine](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine")[Close the toolbar](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=tacacs-kimlik-dogrulama-cisco-ise-kullanarak#close "Close the toolbar")

[screenshot](https://web.archive.org/web/20210227213435/http://web.archive.org/screenshot/https://support.angoranetworks.com/?ht_kb=tacacs-kimlik-dogrulama-cisco-ise-kullanarak "screenshot")[video](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=tacacs-kimlik-dogrulama-cisco-ise-kullanarak# "video")[Share on Facebook](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=tacacs-kimlik-dogrulama-cisco-ise-kullanarak# "Share on Facebook")[Share on Twitter](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=tacacs-kimlik-dogrulama-cisco-ise-kullanarak# "Share on Twitter")

[About this capture](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=tacacs-kimlik-dogrulama-cisco-ise-kullanarak#expand)

TIMESTAMPS

![loading](https://web-static.archive.org/_static/images/loading.gif)

The Wayback Machine - https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht\_kb=tacacs-kimlik-dogrulama-cisco-ise-kullanarak

# Knowledge Base

Search ForSearch

1. [Home](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/ "Home")
2. [Knowledge Base](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?post_type=ht_kb "Knowledge Base")
3. [How To Guides](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb_category=how-to-guides "View all posts in How To Guides")
4. [Tacacs+ Kimlik Doğrulama (Cisco ISE kullanarak) – TR](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=tacacs-kimlik-dogrulama-cisco-ise-kullanarak "Tacacs+ Kimlik Doğrulama (Cisco ISE kullanarak) – TR")

## Genel Bakış

Tacacs+, kullanıcıların ağ cihazlarını yönetmek amacıyla erişim sağlamalarında, kullanılan bir kimlik doğrulama protokolüdür. Ağ güvenliği uygulamalarında sıklıkla kullanılmaktadır. Daha detaylı bilgi için sözü protokolün ilk sahibine bırakmayı daha uygun buluyoruz. Bu [linkten detaylı bilgiye](https://web.archive.org/web/20210227213435/https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_tacacs/configuration/15-s/sec-usr-tacacs-15-s-book/sec-cfg-tacacs.html) ulaşabilirsiniz.

Bu belge, Verge ürün ailesindeki cihazlar ve Cisco ISE üzerindeki yapılandırma aşamalarını anlatmaktadır. Bu yapılandırma test amaçlı temel özellikleri içermektedir. ISE tarafındaki yapılandırmayı daha detaylı hale getirmek mümkündür, ancak detaylar bu dokuman kapsamını dışındadır.

## Yapılandırma

### Verge yapılandırması

4.0 versiyonu ve üzerini kullanantüm Angora kenar anahtarları TACACS+ desteği sunmaktadır. Aşağıdaki yapılandırma tam olarak aynı şekilde tüm donanım (yığınlanmış yapılar dahil) ve yazılım modellerinde kullanılabilinir.

TACACS+ kimlik doğrulama yapılandırması için, temel olarak bir TACACS+ sunucu (bu belge kapsamında Cisco ISE) tanımı yapılmalı ve anahtarın kullanıcı oturum isteklerini bu sunucu üzerinden yapmasını sağlamak gereklidir. İstenirse birde çok sunucu tanımlamak ve bunlar arasında önceliklendirme yapmak mümkündür. Bu belgede kolaylık açısında tek sunucu kullanılmıştır. Tüm zaman değerleri varsayılan ayarlarda bırakılmıştır. TACACS+ yapılandırmasında kullanılan komutların detayları için, [bu linkte bulunan komut satır belgesini](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=security-tacacs) okuyabilirsiniz.

> `(config)#aaa authentication login authorization default tacacs local`

```
Bu komut, anahtara, yünetimsel erişim isteklerini doğrulamak için önce bir tacacs sunucu kullanmasını söylemektedir. Eğer tacacs sunucu erişilemez (istek reddedildiğinde değil) ise, ancak o zaman cihaz üzerinde tanımlı kullanıcılar üzerinden kimlik doğrulama yapmak mümkün olacaktır.
```

> `(config)#aaa authentication enable authorization default tacacs`

```
Bu komut sadece izinli kullanıcılara "enable" komutu girerek yetki seviyelerini değiştirmelerine izin verir. Bu komut girilmezse, enable şifresini bilen herhangi bir kullanıcı yetki seviyesini yukarıya (15) taşıyabilir.
```

> `(config)#tacacs-server host 192.168.1.15 key angora`

```
Anahtar ve tacacs sunucu tarafında aynı 'key' (burada angora olarak belirlenmiştir) kullanılmalıdır.
```

> `(config)#tacacs-server host source-interface vlan 1`

```
Zorunlu olmamakla beraber, kullanıcı doğrulama isteklerinde kaynak adresi olarak kullanacak arayüzü belirleyebilirsiniz. Bunu yapmak, tacacs sunucu tarafında girilen adresle gelen isteklerin adreslerinin aynı olmasını sağlamak açısından iyi bir fikirdir.
```

Verge anahtarlar üzerinde yapmanız gerekenler bunlar. Şimdi Cisco ISE tarafına geçebilirsiniz.

### Cisco Identity Services Engine (ISE) yapılandırması

Cisco ISE kullanıcıların ve cihazların ağ kaynaklarını güvenli erişimlerini sağlamak için kullanılır. Temelde 802.1x hizmeti sağlayan bir radius sunucu olmakla beraber, profillendirme gibi daha ileri seviyede hizmetleri de sağlamaktadır. Radius desteğinin yanında, tacacs sunucu olarak da çalışarak, cihazlara güvenli yönetim erişimi sağlanmasında kullanılmaktadır.

Ürün ile ilgili daha detaylı bilgiye Cisco web sitesi üzerinden ulaşabilirsiniz.

Belgenini bu bölümü, size Cisco ISE yapılandırması konusunda rehberlik ederek Verge anahtarlar ile beraber çalışmasına yardımcı olacaktır. Bu yazıda örnek olarak kullanılan ISE cihazında, yazının yayınlanma tarihindeki en son yayınlanan, 2.6 sürümü yazılım kullanılmıştır.

Tacacs özelliğinin kullanılabilmesi için, her şeyden önce hizmetin aktif edilmiş olması gereklidir.

Tacacs servisini aktifleştirmek için, aşağıdaki menü kullanılır:

> Work Centers->Device Administration->Overview->Deployment

Tüm ISE cihazlarında veya istediğiniz bir kısmında tacacs servisini aktif hale getirebilirsiniz.

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.54.27-1024x428.png)

Tacacs servisi açıldığında, temel yapılandırmaya başlayabilirsiniz. Kalan tüm yapılandırma adımları için “Work Centers->Device Administration” menüsü kullanılacaktır.

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.19.37-1024x653.png)

#### Yeni cihaz ekleme

Öncelikle, tacacs bilgileri ile ulaşılacak cihazın tanımlanması gerekir. Yeni cihaz eklemek için ‘network resources’ menüsü kullanılır.

> Work Centers->Device Administration->Network Resources

‘Network resources’ bölümünden, önce “Network Devices” ardından “+Add” tabına tıklayın Açılan yeni sayfada cihaz bilgilerini girin

- Zorunlu alanları doldurun
- “Device Profile” değiştirmeyin (Cisco)
- “Tacacs Authentication Settings” i işaretleyin ve daha önce anahtar yapılandırmasında kullandığınız ‘key’ değerini (angora olarak tanımlanmıştı) ‘shared secret’ alanına giriniz.

Her iki taraftada aynı değeri girdiğinize emin olun. Aksi takdirde, tacacs istekleriniz reddedilecek ve cihaz komut satırına girişiniz mümkün olmayacaktır.

Örnek yapılandırma aşağıdadır:

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.33.30-1024x824.png)

Sayfanın en altında bulunan ‘Save’ butonuna tıklayarak yeni cihazı ekleme işlemini bitirin.

İşlem sonunda, cihaz aşağıdaki şekilde listelenecektir.

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.33.59-1024x264.png)

#### Tacacs profili yaratma

Yeni tacacs profili yaratmak için aşağıdaki menüden “+Add” butonuna tıklayın;

> Device Administration->Policy Elements->Results->Tacacs Profiles

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.35.03-1024x427.png)

Aşağıdaki örnekte, tüm anahtar yapılandırmasını görebilecek ve değiştirebilecek seviye 15 bir kullanıcı profili yaratılmaktadır.

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.35.58-1024x694.png)

#### Komut seti yaratma

Komut setleri, kullanıcının yetkili olduğu komutların belirlenmesini sağlar. Angora Verge anahtarları mevcut yazılımda, tacacs komut doğrulamasını desteklemediğinden, bu aşamada basit bir komut seti ile tüm komutlara izin verecek politikayı yaratabilirsiniz. Komut izinleri tacacs profillerindeki yetkilendirme seviyeleri ile ayrıştırılabilinir.

Komut seti yaratmak için, aşağıdaki meüden , “+Add” butonuna tıklayın;

> Device Administration->Policy Elements->Results->Tacacs Command Sets

Sadece uygun bir isim verip, “Permit any command that is not listed below” kutusunu işaretleyin, ve “Save” butonuna basın.

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-24-at-23.08.02-1024x474.png)

#### Kullanıcı kimlik grubu yaratma

Aynı yetki seviyelerindeki kullanıcıları gruplandırmak iyi bir fikirdir.

Yeni bir grup yaratmak için aşağıdaki menüden, “+Add” butonuna tıklayın;

> Device Administration->User Identity Groups->User Identity Groups

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.40.49-1024x441.png)

Aşağıdaki örnekte, “Privilege 15 Users” isimli bir grup oluşturulmuştur:

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.41.34-1024x297.png)

#### Kullanıcı yaratma

Erişim sağlayacak kullanıcı yaratmak için , aşağıdaki menüden “+Add” butonuna tıklayın;

> Device Administration->Identities->Users

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.42.04-1024x266.png)

“Name” ve “Login Password” gibi zorunlu alanları girin ve kullanıcıyı uygun gruba ekleyin. Bu örnekte kullanıcı “Privilege 15 Users” grubuna atanmıştır.

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.43.06-1024x725.png)

“Save” butonuna basarak yeni kullanıcıyı yaratın. Aynı prosedürü tekrarlayarak istediğiniz kadar kullanıcı yaratabilirsiniz. Ayrıca farklı kullanıcı servisleri (Active Directory, LDAP vs.) kullanıcı adı parla kontrolü yapabilirsiniz, ancak bu kısım kapsamımız dışındadır.

Cihazlar ve kullanıcılar yaratıldığına göre, tacacs isteklerini karşılayacak politika setlerini yaratabilirsiniz.

#### Politika setleri yaratma

Cisco ISE önceden tanımlı bir politika seti ile gelmektedir. Bu seti kontrol etmek ve yeni kurallar eklemek için aşağıdaki menüyü kullanabilrsiniz:

> Device Administration->Device Admin Policy Sets

“Default” satırının sonundaki çark simgesine tıklayarak yeni satır (“new row above”) ekleyebilirsiniz

Politika setinin adının adını değiştirin ve “Conditions” sütünundaki “+” simgesine tıklayın.

Temel fonksiyonlar için, daha önce yaratılan tüm cihazlarla eşleşen bir koşul kullanabilirsiniz. , Sağ taraftaki “Editor” bölümünden, “DEVICE:Device Type” “Equals” “All Device Types” seçin.

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-24-at-22.55.07-1024x228.png)

“Save” butonuna tıklayarak bu koşulu kütüphaneye kaydedin. Ardından “Use” butonuna tıklayarak bu koşulu politika setine ekleyin.

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-23-at-20.44.16-1024x284.png)

Yeni politika seti tanımlandıktan sonra, “>” (ok) simgesine basarak politika detayları sayfasını açın.

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-24-at-23.01.52-1024x405.png)

“Authorization Policy” satırını genişletin. “Default” politika satırının sonundaki çark simgesine tıklayarak, üste bir satır ekleyin (Add new row on above).

Kurala yeni bir ad verin ve “+” simgesine tıklayarak yeni koşul ekleyin.Bu koşul, kullanıcı gruplarını eşleştirmek için kullanılacaktır.

Editor bölümünden, “Identity Group:Name” “Equals” to “User Identity Groups: Privilege 15 Groups”, seçin ve “Save” butonuna basarak koşulu kütüphaneye ekleyin.

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-24-at-23.13.59-1024x234.png)

“Use” butonuna tıklayarak politika tanımlama sayfasına geri dönün.

Politika setini sonlandırmak için , komut seti ve shell profillerini aşağıda gösterildiği gibi seçin ve “Save” butonuna basarak politikayı aktif hale getirin.

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-24-at-23.15.35-1024x508.png)

Bununla birlikte, Cisco ISE tarafında gereken yapılandırma bitmiş oluyorç ISE üzerine eklediğiniz cihazlardan birisi ile yaratılan kullanıcı bilgilerini kullanarak istek gönderip deneme yapabilirsiniz.

Başarılı bir bağlantı denemesi, aşagıdaki menüden ulaşabileceğiniz canlı kayıtlardan görülebilir;

> Operations->Tacacs->Live logs

Örnek bir kayıt aşağıdaki gibidir:

![](https://web.archive.org/web/20210227213435im_/https://support.angoranetworks.com/wp-content/uploads/2019/10/Screen-Shot-2019-10-24-at-23.19.05-1024x242.png)

### Was this article helpful?

[Yes](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=tacacs-kimlik-dogrulama-cisco-ise-kullanarak#) [No](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=tacacs-kimlik-dogrulama-cisco-ise-kullanarak#)

### Related Articles

- [Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=sifir-dokunma-yapilandirmasi-zero-touch-provisioning-ztp "Sıfır Dokunma Yapılandırması (Zero Touch Provisioning – ZTP)")  - 0
  - 67
- [Sistem Bilgilerini Öğrenme](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=sistem-bilgilerini-ogrenme "Sistem Bilgilerini Öğrenme")  - 0
  - 97
- [Link Katmanı Keşif Protokolü (LLDP)](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=link-katmani-kesif-protokolu-lldp "Link Katmanı Keşif Protokolü (LLDP)")  - 0
  - 116
- [Komut Satırı kullanımı](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=komut-satiri-kullanimi "Komut Satırı kullanımı")  - -1
  - 114
- [Hızlı Başlangıç Kılavuzu](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=hizli-baslangic-kilavuzu "Hızlı Başlangıç Kılavuzu")  - 0
  - 102
- [Yazılım Güncelleme (TFTP) – Verge Anahtarlar](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=yazilim-guncelleme-tftp-verge-anahtarlar "Yazılım Güncelleme (TFTP) – Verge Anahtarlar")  - 2
  - 182

### Leave A Comment? [Cancel Reply](https://web.archive.org/web/20210227213435/https://support.angoranetworks.com/?ht_kb=tacacs-kimlik-dogrulama-cisco-ise-kullanarak\#respond)

Save my name, email, and website in this browser for the next time I comment.