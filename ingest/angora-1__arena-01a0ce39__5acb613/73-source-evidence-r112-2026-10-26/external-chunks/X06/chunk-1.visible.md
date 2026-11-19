zi ve bunu yaparken karmaşık protokollerin yapılandırması ile uğraşmamanızı sağlar.** Sadece gereken trafiğin, gerekli güvenlik çözümlerine gönderilmesi ile, operasyonel kolaylık, mimari düzen ve çok yüksek performans optimizasyonu sağlanır.

![](https://www.angoranetworks.com/wp-content/uploads/2022/10/image-2.png)Güvenlik Zincirleri

## Optimizasyon

Performans optimizasyonu, konu güvenliğe geldiğinde çok kritiktir. Zira yönlendirme ve anahtarlama platformlarında birim veri işleme ve aktarma performansı (örneğin 1Gbps), daha hızlı ve ucuzken, güvenlik cihazlarında aynı veriyi işlemek birkaç kez daha pahalı ve gecikmelidir. Dolayısıyla titizlikle seçilmemiş bir trafik akışı, kıymetli güvenlik kaynaklarının ziyan olmasına ve bu kaynakların kullanılırken yaratılan gecikmenin daha yüksek olmasına neden olur. Packet Broker çözümleri ile, sadece ihtiyaç duyulan trafiğin aktarımı sağlanarak en yüksek verime ulaşmak mümkün hale gelir. Ayrıca bir güvenlik enstrümanının kapasite sınırlarına ulaşıldığında, o cihazın yerine daha yüksek kapasiteli bir başka cihaz almaktansa, ihtiyaç olan yeni kapasite kadar yatırım yapıp, eski kapasitenin kullanımına devam edilmesi mümkündür.

**Bu esneklik, mimari düzen ve operasyonel kolaylık sayesinde, Packet Broker çözümleri bütçelerin daha verimli kullanılmasını sağlarken, kendi yatırımını da kısa zamanda geri döndürür.**

## Paket Analizi

Tüm bu esneklik için Packet Broker cihazının paket kaybetmeyen yüksek trafik işleme kabiliyetinden faydalanılır. Tüm paket akışları düşünüldüğünde, bu trafik kimi zaman 1Tbps seviyelerine ulaşabilir.

Bu kadar büyük hacmin Packet Broker üzerinden kolayca aktarılabilecek olmasına rağmen, tasarımsal olarak hangi trafiğin nereye aktarılacağına karar vermek oldukça önemlidir. Sonuçta ortaya çıkacak sanal akışlar ile paket ve kaynak optimizasyonu amaçlanmaktadır. Bu kararları verebilmek için detaylı bilgiler kullanabiliriz. Bazı ihtiyaçlarda sadece paket içindeki hedef ve kaynak adreslerini okumak yeterken, **bazı durumlarda paketin içinde taşınan verinin (payload) bir kısmına göre karar vermek gerekebilir. Dolayısıyla Packet Broker cihazının derin detaylara göre karar verebilmesi tercih edilir. Tabii ki tüm bunları yaparken en düşük gecikme süresine ve birim trafik taşıma maliyetine sahip olmalıdır.**

Bazı ağ anahtarı üreticilerinin cihazlarından Switch Port Analyzer – SPAN adı verilen aynalama teknolojileri ile ağ içinde gezen paketlerin farklı bir çözüme doğru aktarılması sağlanmaktadır. Bu cihazlar asıl amaçları paket anahtarlama olduğundan, üzerlerinden derin analiz için gereken bilinci sağlayacak donanım/yazılım yapısı bulunmamaktadır. Bu yüzden, sağlanan aktarım sayısı ve filtreleme imkanları oldukça sınırlıdır. Günümüz güvenlik gereksinimlerinin karşılanması için çok önemli olan esneklikten uzaktır. Dolayısıyla SPAN teknolojisi çoğunlukla gereken aktarımı sağlamak için yetersiz kalmaktadır.

## Filtreleme

Filtreleme için temel olacak veriler, ihtiyaçlara göre farklılaşabilir. Bu yüzden Packet Broker’ın tüm paketin içeriğini okuyabilmesi, filtreleme alternatiflerini artırır. L2/L3 adresleri, port numaraları, protokol bilgileri, VLAN bilgileri, MPLS etiketleri, Tünel başlıkları ve hatta içerilen veri, filtreleme amacıyla kullanılabilir.

![](https://www.angoranetworks.com/wp-content/uploads/2022/10/image-3.png)Hizmetler ve Packet Broker görevleri

Filtrelerin çeşitliliği ve bunların uygulanma hızı, genel operasyonun kalitesini belirler. Kolay bir arayüz ile filtrelerin tanımlanması ve bunların portlara eşlenmesi gerekir. Bu sayede çok hızlı şekilde ihtiyaçlara cevap vermek mümkün hale gelir. Ayrıca sağlanan esneklik, paket aktarımının mimari değişikliğe veya altyapıda değişikliğe ihtiyaç kalmadan yapılmasına imkan verir. Birçok farklı trafik noktasından gelen trafiğin, ortak bir analiz platformuna aktarılması ya da güvenlik zinciri içinde aynı paketin farklı araçlar arasındaki macerasını yönlendirmeyi, mimariye sadık kalarak yapabilmek mümkün olur. Ayrıca aynı görevi icra eden, cihazlara trafiğin akıllı şekilde yönlenmesini sağlayarak, maliyetlerinizi düşürür ve yeni ihtiyaçlarınız için bütçelerinizi verimli şekilde planlama seçenekleri yaratır.

## Mimari yerleşim

Ağ içinde cihazların altyapıya entegrasyonları açısından mimari iki kullanım türü vardır. Bunların ilki inline denilen, trafiğin cihaz üzerinden geçmesini sağlayan kullanım türüdür. Diğeri ise out-of-band denen, trafik bilgisinin ya da trafiğin kopyasının, ağ içinde farklı bir noktada bulunan cihazlara aktarılması ile oluşan mimaridir. İlk tür cihazlar, çoğunlukla trafik akışı ile ilgili kararların verildiği, güvenlik duvarı, SSL sonlandırıcı, IPS, WAF gibi **aktif** cihazlardır. Aktif cihazlardan geçen trafik, cihaz üzerindeki politikalar (örneğin, bir güvenlik zafiyeti kararı verilmesi gibi) aksini söylemedikçe ağ içinde harekete devam eder. İkinci tür ise performans analizi, monitörleme ve raporlama gibi, trafik üzerinde aktif etki sağlamayan ve sadece trafik ile ilgili analiz ve sonuçlar üreten **pasif** cihazlardır.

Packet Broker cihazları üzerlerinde tanımlanan trafik filtrelerini, trafiğin geldiği ve gönderileceği arayüzleri eşleştirdikten sonra, bu eşleştirmeye uygular. Böylelikle tanımlanan filtrede, hangi paket, gönderilecek cihazın ilgisini çekiyorsa, o paketin cihaza aktarımı ve kalan paketlerin yoluna olduğu gibi devam etmesi sağlanır.

Packet broker çözümleri, yeni nesil mimarilerin, performans açısından daha etkin ve maliyetleri kontrol ederek uygulanması ve işletilmesinde önemli bir bileşendir. Mimari ve operasyonel avantajları yanında, uzun vadeli planlamaların daha esnek yapılandırılmasını sağlar.

Angora Networks Packet Broker çözümleri ile daha fazla bilgi almak için, [iletişim formunu doldurabilirsiniz](https://www.angoranetworks.com/iletisim/) veya Angora Networks iş ortakları ile iletişime geçebilirsiniz.

![Angora](https://secure.gravatar.com/avatar/92daf4c88bb5ec76b3c484850f603c8b?s=64&d=mm&r=g)

##### [Angora](https://www.angoranetworks.com/author/wwwadmin/)

Comments are closed.

[Destek](https://support.angoranetworks.com/)

[![Türkçe](https://www.angoranetworks.com/wp-content/plugins/sitepress-multilingual-cms/res/flags/tr.png)](https://www.angoranetworks.com/gorunurluk-guvenlik-maliyet-packet-broker/#)

- [Bu sayfa için çeviri yok](https://www.angoranetworks.com/gorunurluk-guvenlik-maliyet-packet-broker/#)

 [![](https://www.angoranetworks.com/wp-content/uploads/2021/09/Post_20210902_web-2-80x80.png)\\
\\
**Angora Networks ® PacketFence NAC entegrasyonu tamamladı.** 09/01/2021](https://www.angoranetworks.com/angora-networks-cisco-ise-entegrasyonu-tamamladi-2/) [![](https://www.angoranetworks.com/wp-content/uploads/2022/10/Screen-Shot-2022-10-01-at-09.24.51-80x80.png)\\
\\
**Angora Networks ® Veri Diyotu Çözümünde Ezber Bozan ModBUS ve OPC protokolü Desteğini Tanıttı** 12/06/2023](https://www.angoranetworks.com/angora-networks-veri-diyotu-cozumunde-ezber-bozan-modbus-ve-opc-protokolu-destegini-tanitti/)