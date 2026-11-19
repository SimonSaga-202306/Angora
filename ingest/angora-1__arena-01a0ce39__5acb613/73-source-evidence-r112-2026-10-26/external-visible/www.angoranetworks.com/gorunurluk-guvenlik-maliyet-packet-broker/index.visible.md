[3](https://www.angoranetworks.com/gorunurluk-guvenlik-maliyet-packet-broker/#)

Geleneksel ve eski teknlojilerin kullanıldığı ağ güvenliği yapılarında temel olarak bir güvenlik duvarı ve üzerindeki portlara bağlı alanlar bulunmaktaydı. Yeni bir alan ihtiyacı olduğunda, yeni bir arayüz kullanılır, böylelikle farklı ihtiyaç ve güvenlik seviyeleri tanımlanırdı. Bu güvenlik seviyeleri arasındaki geçiş ve politikalar da uygun kurallar tanımlanarak oluşturulurdu. Bu yapılar genelde bir iç ağ ve bir dış ağdan oluşur, ihtiyaç olması durumunda sunucuların bulunacağı bir alan daha yaratılırdı. Bu 3 ağlı yapıda iç ağ, tüm kullanıcıların bulunduğu ve her koşulda güvenli kabul edilirken, dış ağ ise, internet gibi harici bağlantılara sahip ve tümüyle güvenilmez kabul edilmekteydi. Arada kalan sunucu segmenti ise, iç ağdan güvensiz, dış ağdan güvenli varsayılmaktaydı. Böylelikle herhangi bir ağ segmentine sızıldığında, o segment içinde hareketi kontrol eden herhangi bir politika olmadığından, ataklar ve sorunlar oluşması daha kolay hale geliyordu.

Teknolojinin ihtiyaçlara göre değişmesi ve ihtiyaçların teknolojinin sunduklarına göre evirilmesi sonucunda, faklı saldırı yöntemleri ortaya çıktı. Çok detaylı teknik saldırılardan, sosyal mühendislik saldırılarına kadar çeşitli yöntemler ile bilgi hırsızlığı yapmak veya servis kesintileri oluşturmak mümkün hale geldi. Dolayısıyla geleneksel erişim kuralları bazlı güvenlik yaklaşımı, modern zamanlarda kullanışlı olmaktan çıktı. Daha küçük parçalı ağlara ve uygulama ve cihazlara özgü güvenlik politikalarına ihtiyaç duyulur hale gelindi. Böylelikle tek bir kural bazlı güvenlik duvarı cihazı yerine, farklı görevlerin birleştiği birden çok cihazdan oluşan büyük bir güvenlik mimarisi kullanımı mecburiyet haline geldi.

Öte yandan, daha önce tek bir segment olarak düşünülen dahili ağlar, çok parçaya bölünerek, hem yönetimsel olarak kolay idare edilebilir hale getirildi, hem de olası atakların etki alanları daraltılmış oldu. Böylece servis kesintileri ve etkilenmeler daha sınırlı bir kaynak grubuyla sınırlandırılmış oldu.

Bir atağa karşı korunma sağlamak kadar, atak sırasında etkinin en alt seviyede tutulması ve sonrası zararın hızlı tespiti ve onarımı da en az korunma kadar kritik olarak değerlendirilmeye başlandı.

Günümüzde uygulamaların da gelişmesi ve daha yoğun kullanılır hale gelmesi sonucunda, sunucu kaynaklarının daha verimli yönetilmesi de zorunluluk haline gelmiştir. Aynı fiziksel sunucu üzerinde, birçok uygulamanın çalışması artık normal operasyonun bir parçasıdır. Sunucu sanallaştırma ve micro-segmentation teknolojileri sayesinde, çok daha küçük ve işe yarar kaynak gruplamaları sağlamak mümkündür. Bir sunucu üzerinde, birbirlerinden tamamen bağımsız birden fazla şirket veya kuruma ait uygulamalar çalışabilmektedir. Bu tip yapılara multi-tenant adı verilmektedir.

![](https://www.angoranetworks.com/wp-content/uploads/2022/10/image.png)Güvenlik Mimari Modelleri

Bu yapılar, tek bir fiziksel sunucu üzerinde, sanal olarak kaynakları paylaştırarak ve erişim sağlayarak çalışmaktadır. Böyle olunca aslında tek bir fiziksel güvenlik segmenti içinde kalmalarına rağmen, farklı ihtiyaçlara sahip olduklarından, hem kendi aralarında hem de dış Dünya’ya karşı güvenliklerinin ayrı ayrı tasarlanması gerekir. Bu amaçla, sanal güvenlik çözümleri tasarlanmıştır. Fiziksel güvenlik çözümleri ile eşlenik özellikler sağlayan bu çözümler, aslında daha genel kapsamlı ‘Yazılım Tabanlı Ağ’ (Software Defined Networks) konseptinin bir parçasıdır. Bu konsept içinde üst üste binen sanal ağlar, sanallaştırma yapıları, depolama çözümleri gibi, ağ üzerinde yer alan birçok bileşen ortak bir yönetim platformu üzerinden yönetilebilmektedir.

Bu yapılar son zamanlarda sıklıkla duyduğumuz bulut servislerinin ve dolayısıyla yeni iletişim ve servis düzeninin temellerini oluşturmaktadır.

## Packet Broker nedir?

Packet Broker’lar temelde farklı cihazların yarattığı ya da farklı ağlar arasında geçiş yapan trafiğin, kurallar çerçevesinde akıllı bir şekilde seçilerek gruplanmasını ve her grubun ihtiyaçlar doğrultusunda doğru güvenlik zinciri içerisinde aktarılmasını ve/veya analiz ve monitörleme araçlarına gönderilmesini sağlayan, çok hızlı ve yüksek kapasiteli paket yönlendirmesi yapan ağ cihazlarıdır. Başlıca görevleri arasında, trafik sınıflandırma, eşleme ve filtreleme, cihazlar arasında ağ tabanlı yük dengelemesi, ağ yedekliliği, trafik optimizasyonu ve güvenlik, performans ve mönitörleme zincirleri oluşturulması vardır.

Packet Broker’lar görevlerini yerine getirmek için, ağ içinde farklı noktalara bağlantı sağlayarak, trafiğin üzerinden geçmesini sağlar. Bu noktalar duruma göre, ağa ilk giriş noktaları, veri merkezi güvenlik segmentinin girişi, internet çıkış noktaları ya da sunucu çiftliklerinin arası olabilir. Ne kadar çok trafik Packet Broker üzerinden geçerse, o kadar detaylı sınıflandırma, analiz ve filtreleme sağlamak mümkün olur.

![](https://www.angoranetworks.com/wp-content/uploads/2022/10/image-1.png)Packet Broker hizmetleri

## Görünürlük

Ağ sanallaştırması ve segmentasyonu çok çekici olmakla beraber, doğru adımlar atılamadığında, çok daha karmaşık yapıların oluşmasına ve soruları çözmektense, daha büyüklerinin ortaya çıkmasına neden olmaktadır. Doğru segmentasyon için, sanal ya da fiziksel bileşenlerin yarattığı trafiğin farkında olunmalıdır. Bunun için görünürlük çok kritiktir. Maliyeti çok artırabilecek, birçok küçük segment oluşumu ile, güvenlik zaaflarını artırabilecek az sayıda segment oluşumu arasında, titiz bir karar verilmesi gerekir. Bu da ancak ağ içinde dolaşan trafiğin akışını doğru anlayarak mümkün olabilir.

**Birbirinden farklı birçok hayvanın olduğu bir çiftlik düşünün. Bu çiftlikte her hayvana ayrı bir kafes yapmak güvenli gözükmekle beraber, çok maliyetli ve yönetimi zor bir yöntemdir. Buna karşılık tüm hayvanlar tek bir çit içine koyarsanız, farklı grupların birbirine zarar vermesi mümkün hale gelecektir. O yüzden doğru davranışları takip etmeli ve uygun olabilecek hayvan gruplarını beraber tutabileceğiniz alanlar yaratmak gereklidir. Bu analizi doğru yapmadığınız takdirde, zararların oluşması kaçınılmazdır.**

Trafik monitörleme ve analiz araçları tam da bu iş için üretilmişlerdir. Bu araçlar, trafik bilgisini derleyerek, anlamlı korelasyonlar ve raporlar oluşturarak, genel resmin ortaya çıkmasını sağlar. Ancak bu araçlar kendi başlarına trafik toplayamaz. Trafiğin ya da trafik ile ilgili özet bilgilerin kendilerine gönderilmesini beklerler. Bir yöntem bu araçlardan birçoğunu ağ içine yayarak trafiğin üstünden geçmesini sağlamaktır. Tabii bu çok fazla yönetime ve kaçınılmaz olarak da büyük bir maliyete neden olacaktır. Packet Broker cihazları, ağ üzerindeki trafiğin filtrelenerek kopyalanmasını sağlarlar. Tüm ağınızın trafiğini üstünden geçirdiğiniz bir packet broker, farklı segmentlerden gelen trafiği istediğiniz trafik raporlama çözümüne kopyalayabilir. Bunu yaparken mimari de herhangi bir değişiklik ihtiyacı olmazken, güvenlikten de taviz verilmez.

## Güvenlik zincirleri

Görünürlükle birlikte, farklı politikalarla ağ içinde gezen değişik karakterdeki trafikleri, farklı güvenlik enstrümanlarından geçirmek de gerekir. Güvenlik duvarı, SSL sonlandırıcı, IPS, APT cihazları gibi çözümler trafiği haricen işleyerek, farklı kararlar alınmasını sağlar. Her trafik akışı için farklı güvenlik ihtiyaçları oluşmaktadır. Bu yüzden sabit bir ağ akışı sağlayarak, güvenlik önlemlerini arka arkaya koymak uygulanabilir değildir. Trafiğin ihtiyaçlarına göre akıllı kararlar alınarak, istenen trafiğin sadece gerekli güvenlik cihazları tarafından kontrol edilmesi gerekir. Böyle bir yapı, yönlendirme protokolleri ile kurulmaya çalışıldığında, ortaya çok büyük bir karışıklık çıkabilir. Tabii bu operasyonel karışıklık beraberinde, yüksek bir cihaz ve altyapı faturası da getirecektir.  **Packet Broker çözümleri bu yapıların istenildiği gibi esnek şekilde kurulabilmesini sağlar. Tek bir ağ içinde, farklı güvenlik zincirleri oluşturabilmenizi ve bunu yaparken karmaşık protokollerin yapılandırması ile uğraşmamanızı sağlar.** Sadece gereken trafiğin, gerekli güvenlik çözümlerine gönderilmesi ile, operasyonel kolaylık, mimari düzen ve çok yüksek performans optimizasyonu sağlanır.

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