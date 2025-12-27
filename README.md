<div align="center">
  <img src="assets/banner.png" alt="Hashchat Elite Banner" width="100%" style="border-radius: 10px; box-shadow: 0 0 50px rgba(0, 255, 255, 0.5);" />
  
  <br />
  <br />

  <!-- SYSTEM STATUS BADGES -->
  <a href="https://github.com/bahattinyunus/Hashchat/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/bahattinyunus/Hashchat/ci.yml?branch=main&style=for-the-badge&logo=github&label=SİSTEM%20DURUMU&color=00ff00" alt="System Status">
  </a>
  <a href="https://swift.org">
    <img src="https://img.shields.io/badge/ÇEKİRDEK-SWIFT_5.9-orange?style=for-the-badge&logo=swift&logoColor=white" alt="Swift Core">
  </a>
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/SUNUCU-PYTHON_3.11-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python Backend">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/ŞİFRELEME-RSA_2048-blueviolet?style=for-the-badge&logo=lock&logoColor=white" alt="RSA Encryption">
  </a>

  <br />
  
  <h1>🦅 HASHCHAT: ENTEGRE SİBER SAVUNMA PLATFORMU</h1>
  <h3><i>"Mahremiyet bir ayrıcalık veya lütuf değil, evrensel bir matematiksel kesinliktir."</i></h3>
  <p><b>Versiyon:</b> 2.0 (Elite Edition) | <b>Mimari:</b> Zero-Knowledge Relay | <b>Lisans:</b> Apache 2.0</p>
</div>

---

### 📟 SİSTEM GİRİŞİ BAŞLATILIYOR...

```console
root@hashchat-command-center:~$ ./initialize_protocol.sh --verbose --level=MAXIMUM
> [INIT] ÇEKİRDEK SİSTEMLER BAŞLATILIYOR... (ZAMAN: 0.003s)
> [LOAD] Kriptografik Motor (Pure Swift AES-128 Implementation)... DOĞRULANDI.
> [LOAD] Anahtar Yönetim Sistemi (RSA-2048 OAEP/SHA256)... DOĞRULANDI.
> [CNCT] Güvenli Soket Katmanı (WSS/TLS 1.3)... BAĞLANTI KURULDU @ PORT 12345.
> [DB]   Kalıcı Veri Katmanı (SQLite + SQLAlchemy ORM v2.0)... ŞEMA SENKRONİZE.
> [LOG]  İstihbarat Servisi (Loguru Sink)... AKTİF VE DİNLİYOR.
> SİSTEM HAZIR. "CAM KUTU" (GLASS-BOX) PROTOKOLÜ DEVREDE.
```

> **🔴 DİKKAT:** Bu proje sadece koddan ibaret değildir. Gelecek planlarımızı ve 2030 hedeflerimizi okumak için [**VİZYON 2030 (VISION.md)**](VISION.md) belgesini inceleyiniz.

---

## 🎓 HASHCHAT AKADEMİSİ: BÜYÜK ANSİKLOPEDİ (MAGNUM OPUS EDITION)

Bu doküman, Hashchat projesinin **Nihai Teknik Referans Kaynağıdır**. Sıradan bir yazılım projesinin "Beni Oku" dosyasının çok ötesinde, bu metin modern siber güvenliğin, kriptografinin, dağıtık sistem mimarisinin ve yazılım mühendisliği felsefesinin derinlemesine incelendiği bir **Manifesto** ve **Akademik Ders Kitabıdır**.

Buradaki her paragraf, ticari mesajlaşma uygulamalarının (WhatsApp, Telegram, Signal gibi) kapalı kapılar ardında sakladığı karmaşık güvenlik mekanizmalarını şeffaflaştırmak, "sihri" bozmak ve size **işin mutfağındaki saf matematiği** en ince ayrıntısına kadar öğretmek için titizlikle kaleme alınmıştır.

---

### 📑 İÇİNDEKİLER VE MÜFREDAT
1.  **[Bölüm I: Felsefe ve Vizyon](#-bölüm-i-felsefe-ve-vizyon)**
    *   Cam Kutu Teorisi ve Tarihsel Bağlam
    *   Kerckhoffs Prensibi ve Modern Kriptografi
2.  **[Bölüm II: Sistem Mimarisi (Blueprint)](#-bölüm-ii-sistem-mimarisi-blueprint)**
    *   Frontend: Declarative UI Felsefesi & Reactive Streams Mimarisi
    *   Backend: Asenkron Röle Yapısı & WSS Protokol Derinlikleri
3.  **[Bölüm III: Kriptografi Motoru (The Engine)](#-bölüm-iii-kriptografi-motoru-the-engine)**
    *   Simetrik: AES-128 (Matematiksel Analiz ve Galois Alanları)
    *   Asimetrik: RSA-2048 (Sayılar Teorisi ve Asal Çarpanlar)
4.  **[Bölüm IV: Veri Kalıcılığı ve İstihbarat](#-bölüm-iv-veri-kalıcılığı-ve-istihbarat)**
    *   Ironclad Persistence (SQLAlchemy ORM ve ACID İlkeleri)
    *   Elite Intelligence (Loguru ve Yapılandırılmış Loglama)
5.  **[Bölüm V: Operasyonel Kurulum](#-bölüm-v-operasyonel-kurulum)**

---

## 🏛️ BÖLÜM I: FELSEFE VE VİZYON

### 1.1 "Güvenlik, Bilinmezlik (Obsecurity) Değildir"
Modern dünyada siber güvenlik, ne yazık ki genellikle "belirsizlik" (obscurity) arkasına saklanarak sağlanmaya çalışılır. Endüstride buna **"Security by Obscurity"** (Gizlilik Yoluyla Güvenlik) denir. Büyük teknoloji firmaları, kaynak kodlarını ne kadar sıkı saklarlarsa, sistemlerinin o kadar güvenli olacağı yanılgısına düşerler ve kullanıcıları da buna inandırırlar. Ancak tarih göstermiştir ki, gizlenen her sistem eninde sonunda tersine mühendislik ile çözülür.

**Hashchat'in Felsefesi (Cam Kutu / Glass-Box Yaklaşımı):**
Bizim güvenliğimiz, kaynak kodumuzun gizliliğinden, saklanmasından veya erişilemez olmasından değil; kullandığımız matematiksel algoritmaların (AES, RSA) evrensel sağlamlığından ve anahtar yönetimindeki titizliğimizden gelir.
*   Bir saldırgan (Hacker) veya meraklı bir devlet kurumu, Hashchat'in tüm kaynak kodlarına, veritabanı şemasına ve ağ yapısına sahip olsa bile, kullanıcılarımız arasındaki şifreli mesajları çözemez. Çünkü matematik yalan söylemez.
*   Bu yaklaşım, 19. yüzyılda Auguste Kerckhoffs tarafından ortaya atılan **Kerckhoffs Prensibi**'ne dayanır: *"Bir kriptosistemin güvenliği, algoritmanın gizliliğine değil, sadece ve sadece anahtarın gizliliğine dayanmalıdır."* Eğer algoritmanızın güvenliği onun bilinmemesine bağlıysa, o sistem zaten kırılmıştır.

### 1.2 Neden Bu Projeyi Yaptık?
Günümüzde çoğu yazılım geliştirici, projelerine şifreleme eklerken hazır kütüphaneleri (`import crypto` veya `import ssl`) kullanır ve geçer. Arka planda o kütüphanenin ne yaptığı, baytları nasıl karıştırdığı, güvenliği nasıl sağladığı bir muammadır. Hashchat, bu "kara kutuyu" parçalar ve içini sergiler.
*   🔑 **Anahtar Üretimi:** Bir RSA anahtarının (Public/Private Key pair) bayt bayt nasıl üretildiğini, asal sayıların nasıl seçildiğini **kod satırlarında canlı olarak görürsünüz**.
*   🌐 **Veri Akışı:** Şifreli verinin (Ciphertext) cihazdan çıkıp, sunucuya uğrayıp, karşı tarafa nasıl ulaştığını **loglarda adım adım izlersiniz**.
*   🧮 **Matematik:** Soyut matematikte kalan S-Box (Substitution Box), Galois Alanı ($GF(2^8)$) çarpımı gibi kavramlara bizzat kod yazarak **dokunursunuz**.

> **Nihai Hedefimiz:** 2030 yılına kadar sadece kod yazan değil, yazdığı kodun güvenliğini matematiksel olarak ispatlayabilen, kriptografik okuryazarlığa sahip ve "dijital egemenliği" savunan 1000 elit "Cyber-Sovereign" geliştirici yetiştirmektir.

---

## 🏗️ BÖLÜM II: SİSTEM MİMARİSİ (BLUEPRINT)

Hashchat, rastgele bir araya getirilmiş kod parçacıkları veya kopyala-yapıştır yapılmış bir yığın değildir. Endüstri standardı **Clean Architecture** (Temiz Mimari), **SOLID** prensipleri ve **Design Patterns** (Tasarım Desenleri) ile, yaşayan ve nefes alan bir organizma gibi tasarlanmıştır.

### 📱 2.1 FRONTEND: iOS (Swift)
Kullanıcı arayüzü ve istemci mantığı, Apple ekosisteminin en modern ve geleceğe dönük mimarisi üzerine inşa edilmiştir. Burada klasik yöntemler terk edilmiş, tamamen "State-Driven" (Durum Tabanlı) bir yapı benimsenmiştir.

#### A. SwiftUI (Deklaratif Görsel Dil)
Klasik "Imperative" (UIKit) yapısının aksine, SwiftUI'da biz arayüzü piksel piksel çizmeyiz veya "bu butonu şuraya koy" demeyiz. Biz arayüzün **neye benzemesi gerektiğini** tarif ederiz (Declare).
*   **State-Driven (Durum Güdümlü):** `ChatView` basit bir görsel çizim değildir; `ChatViewModel` üzerindeki verinin anlık, canlı bir yansımasıdır. Veri modeli değiştiği mikrosaniye içinde, ekran otomatik olarak ve optimum performansla yeniden çizilir. Geliştirici, "ekranı güncelle" komutu yazmaz; bu, sistemin doğasında vardır.

#### B. Combine Framework (Reaktif Sinir Sistemi)
Hashchat, olay güdümlü (Event-Driven) bir sistemdir. WebSocket üzerinden saniyede onlarca mesaj gelebilir. Bu veri trafiğini yönetmek için **Combine** kullanılır. Bu yapı, veri akışını bir su tesisatı gibi (Pipeline) yönetmemizi sağlar:
1.  **Publisher (Yayıncı):** Ağ soketinden ham veri (Raw Data) paketi gelir.
2.  **Operator (Operatör):** Bu ham veri, JSON formatından Swift nesnelerine (Model) dönüştürülür (`.decode`), hatalar filtrelenir (`.catch`) ve veri işlenir.
3.  **Scheduler (Zamanlayıcı):** Ağ işlemleri arka planda (Background Thread) yapılırken, sonuçlar kullanıcı arayüzünü kilitlememek için ana iş parçacığına (Main Thread) gönderilir (`.receive(on: RunLoop.main)`).
4.  **Subscriber (Abone):** Sonuç, arayüzdeki değişkenlere bağlanır ve kullanıcı mesajı görür.
*   Tüm bu karmaşık akış, Combine sayesinde milisaniyeler sürer ve cihazın pilini veya işlemcisini yormaz.

#### C. Secure Enclave (Dijital Kasa ve Donanım Güvenliği)
Mobil güvenlikte en büyük risk, cihazın çalınması veya işletim sisteminin hacklenmesidir. Hashchat, en kritik veriler olan **Özel Anahtarları** (Private Keys), cihazın normal dosya sisteminde veya RAM'inde saklamaz.
*   **Secure Enclave:** Apple işlemcilerinin (A-Series chipler) içinde bulunan, ana işletim sisteminden (iOS) tamamen izole edilmiş, kendi mikro çekirdeğine sahip fiziksel bir "Donanım Kasası"dır.
*   Hashchat, anahtarları `SecItemAdd` API'si ile bu kasaya (Keychain) yazar. Telefon yazılımsal olarak ele geçirilse bile, saldırgan donanım seviyesindeki bu kasaya erişemez. Bu, askeri seviye bir güvenlik standardıdır.

### 🧠 2.2 BACKEND: Python (FastAPI)
Sunucu tarafı, sadece verileri ileten basit bir script değildir. "Bloklamayan" (Non-blocking) G/Ç mimarisine sahip, binlerce eşzamanlı bağlantıyı yönetebilen yüksek performanslı bir dijital röledir.

#### A. WSS Protokolü (WebSockets & Sürekli Bağlantı)
Klasik internet protokolü olan HTTP, bir "Telsiz" gibidir; mandara basarsınız (İstek/Request), konuşursunuz, bırakırsınız ve cevap beklersiniz (Yanıt/Response). Bağlantı her seferinde kopar.
*   **WebSocket:** Hashchat'in kullandığı WebSocket protokolü ise **"Açık Telefon Hattı"** gibidir. Bağlantı bir kere kurulur (Handshake) ve sonsuza kadar (veya kopana kadar) açık kalır.
*   **Tam Çift Yönlü (Full-Duplex):** Sunucu ve istemci aynı anda konuşabilir. Sunucu, istemciden bir istek gelmesini beklemeden ona veri ("Yeni mesajın var!") gönderebilir. Bu, gerçek zamanlı sohbetin temelidir.
*   **Sıfır Gecikme:** Her mesajda yeniden bağlantı kurulmadığı için gecikme (Latency) minimumdur.

#### B. AsyncIO (Asenkron Eşzamanlılık)
Python'un modern `async/await` yapısı sayesinde, sunucumuz **Event Loop** (Olay Döngüsü) adı verilen bir mimari kullanır.
*   **Geleneksel Sunucular (Thread-based):** Her kullanıcı için işletim sisteminde yeni bir "iş parçacığı" (Thread) açar. 10.000 kullanıcı gelirse, sunucu binlerce thread açmaya çalışır ve RAM yetmezliğinden çöker (C10k Problemi).
*   **Hashchat (AsyncIO):** Tek bir iş parçacığı üzerinde çalışır. Bir kullanıcı veritabanından cevap beklerken, sunucu "beklemez"; o sırada diğer kullanıcıların işini halleder. Bu sayede tek bir CPU çekirdeği ile on binlerce kullanıcıya hizmet verebilir.

---

## 🔐 BÖLÜM III: KRİPTOGRAFİ MOTORU (THE ENGINE)

Burası projenin teknik kalbi, beyni ve ruhudur. Hashchat, kriptografik algoritmaları hazır kütüphanelerden tek satır kodla çağırmakla (`AES.encrypt()`) yetinmez; bu algoritmaları **eğitim amacıyla sıfırdan ve manuel olarak** uygular.

### ⚔️ 3.1 SİMETRİK SAVAŞ SANATI: AES-128 (DERİN ANALİZ)
**Advanced Encryption Standard (AES)**, şu an dünyadaki en güvenli simetrik şifreleme standardıdır. NSA (Ulusal Güvenlik Ajansı) tarafından "Gizli" ve "Çok Gizli" belgeleri korumak için onaylanmıştır. Hashchat, bu algoritmayı Swift dilinde, her bayt işlemini, her matris dönüşünü görebilmeniz için **saf kod** olarak yazmıştır.

Veri, 128 bitlik (4x4 Baytlık Matris) bloklar halinde alınır ve 10 tur (Round) boyunca "hırpalanır". Her turda 4 hayati operasyon gerçekleşir:

#### 1. SubBytes (Doğrusal Olmayan Değişim - Confusion) 🎭
Bu adımda, her bir bayt, `S-Box` (Substitution Box / Yerine Koyma Kutusu) adı verilen, matematiksel olarak özel tasarlanmış bir tablo kullanılarak bambaşka bir baytla değiştirilir.
*   **Matematiksel Amaç:** Giriş verisi ile çıkış verisi arasındaki istatistiksel ilişkiyi tamamen koparmaktır. "a" harfi her zaman aynı şifreye dönüşmez. Bu değişim doğrusal değildir (Non-linear), bu sayede "Linear Cryptanalysis" saldırılarına karşı direnç sağlanır.

#### 2. ShiftRows (Satır Kaydırma - Diffusion I) 🌪️
Şifreleme matrisinin satırları, belirli ofsetlerle sola doğru kaydırılır.
*   1. Satır: Dokunulmaz.
*   2. Satır: 1 bayt sola kaydırılır.
*   3. Satır: 2 bayt sola kaydırılır.
*   4. Satır: 3 bayt sola kaydırılır.
*   **Amaç:** Veriyi blok geneline yaymaktır (Diffusion). Bir sütundaki veri, diğer sütunlara taşınır. Böylece veriler birbirine karışmaya başlar.

#### 3. MixColumns (Sütun Karıştırma - Diffusion II) 📐
Bu, AES'in en karmaşık matematiksel işlemidir. Sütunlar, **Galois Alanı ($GF(2^8)$)** adı verilen sonlu cisim aritmetiği kullanılarak, özel bir polinom matrisi ile çarpılır.
*   **Büyü:** Bu işlem normal bir çarpma değildir; bayt seviyesinde yapılan karmaşık bir dönüşümdür.
*   **Sonuç:** Girişteki tek bir bitlik değişim (örneğin 'A' harfinin 'B' olması), çıkışta baytların en az yarısının tamamen değişmesine neden olur. Buna kriptografide **Çığ Etkisi (Avalanche Effect)** denir.

#### 4. AddRoundKey (Anahtar Kilitleme) 🔐
O anki turun anahtarı (Subkey) ile mevcut durum matrisi üzerinde **XOR** işlemi uygulanır.
*   **Önemi:** Şifrenin gizli anahtara bağımlı olduğu yegane adım budur. Diğer adımlar (SubBytes, ShiftRows, MixColumns) anahtarsızdır ve sadece karıştırma yapar. AddRoundKey ise kilidi vurur. Bu işlem tersine çevrilebilir (XOR'un tersi yine XOR'dur).

### 🛡️ 3.2 ASİMETRİK KALKAN: RSA-2048 (TEORİK DERİNLİK)
İki yabancının (Alice ve Bob), daha önce fiziksel olarak hiç karşılaşmadan, güvensiz bir kanal (internet) üzerinden güvenli bir şifre üzerinde anlaşabilmesi bir matematiksel mucizedir.

#### RSA'nın Matematiksel Temeli (Trapdoor Functions):
RSA güvenliği, tek yönlü bir matematiksel fonksiyona (Trapdoor / Tuzak Kapı Fonksiyonu) dayanır: **Büyük sayıları çarpmak çok kolaydır, ancak çıkan sonucu çarpanlarına ayırmak evrensel ölçekte zordur.**

1.  **Anahtar Üretimi ($KeyGen$):**
    *   İlk adımda, rastgele ve çok büyük iki **Asal Sayı** seçilir: $p$ ve $q$.
    *   Modulus hesaplanır: $n = p \times q$. (Hashchat'te bu $n$ sayısı 2048 bittir, yani yaklaşık 617 basamaklı ondalık bir sayıdır).
    *   $\phi(n)$ (Euler's Totient) fonksiyonu hesaplanır: $\phi(n) = (p-1)(q-1)$. Bu, $n$'den küçük ve $n$ ile aralarında asal olan sayıların adedidir.
    *   Bir "Public Exponent" ($e$) seçilir (genellikle 65537).
    *   Bir "Private Exponent" ($d$) hesaplanır: $d \equiv e^{-1} \pmod{\phi(n)}$.

2.  **Şifreleme ($Encrypt$):**
    *   Mesaj ($m$), sayısal formata çevrilir.
    *   Alice, Bob'un açık anahtarını ($e, n$) kullanarak şifreler: $c = m^e \pmod n$.

3.  **Deşifreleme ($Decrypt$):**
    *   Bob, kendi gizli anahtarını ($d$) kullanarak orijinal mesajı geri getirir: $m = c^d \pmod n$.

> **Güvenlik Kanıtı:** Bir saldırganın elinde $n$ ve $e$ vardır. Ancak gizli anahtar $d$'yi bulabilmesi için, $n$ sayısını $p$ ve $q$ çarpanlarına ayırması gerekir. 2048 bitlik bir sayıyı çarpanlarına ayırmak için gereken işlem gücü ve enerji, dünya üzerindeki tüm okyanusları kaynatmaya yeter. Mevcut matematik ve süper bilgisayarlarla bu imkansızdır.

---

## 💾 BÖLÜM IV: VERİ KALICILIĞI VE İSTİHBARAT (PERSISTENCE & INTELLIGENCE)

**Hashchat V2.0** (Elite Edition) ile sistem, geçici bir prototipten ("Unutkan" Hafıza) profesyonel, endüstriyel standartlarda bir veri altyapısına ("Kalıcı" Hafıza) evrilmiştir. Bu, projenin ciddiyetini gösteren en büyük adımdır.

### 🏛️ 4.1 IRONCLAD PERSISTENCE (SQLite + SQLAlchemy)
Eskiden (V1.0), sunucu yeniden başlatıldığında (veya çöktüğünde) kayıtlı tüm kullanıcılar ve anahtarlar RAM'den silinirdi. Artık veriler disk üzerinde atomik ve kalıcı bir yapıda saklanır.

*   **Veritabanı Motoru:** **SQLite**. Sunucusuz (Serverless), dosya tabanlı ve ACİD uyumlu, dünyanın en çok kullanılan veritabanı motorudur. Tüm veritabanı tek bir dosyada (`hashchat.db`) tutulur. Bu, yedeklemeyi ("Bu dosyayı kopyala") ve taşımayı inanılmaz kolaylaştırır, ayrıca harici bir veritabanı sunucusu kurulumu gerektirmez.
*   **ORM (Object Relational Mapping):** **SQLAlchemy 2.0**.
    *   Biz kod yazarken ham SQL (`SELECT * FROM users WHERE...`) yazmayız. Bu hem hataya açıktır hem de **SQL Injection** saldırılarına davetiye çıkarır.
    *   Bunun yerine ORM kullanırız. Veritabanı tabloları ile Python sınıfları (Class) arasında bir köprü kurarız. `db.scalars(select(User).where(User.username == "neo"))` gibi temiz, okunabilir ve güvenli kod yazarız.
    *   **ACID Uyumluluğu:** (Atomicity, Consistency, Isolation, Durability) prensipleri sayesinde veri bütünlüğü garanti altındadır. Bir işlem (Transaction) ya tamamen gerçekleşir ya da hiç gerçekleşmez; veritabanı asla "yarım" veya "bozuk" durumda kalmaz.

### 📡 4.2 ELITE INTELLIGENCE (Loguru ve Yapılandırılmış Loglama)
İyi bir komutan, savaş alanındaki her hareketi, her telsiz konuşmasını, her askerin durumunu izler. Hashchat İstihbarat Modülü (Loguru), sistemdeki her dijital nefesi, her veri paketini kaydeder.

**Neden `print()` kullanmıyoruz?**
Amatör projeler `print("Hata oldu")` yazar. Profesyonel sistemler **Yapılandırılmış Loglama (Structured Logging)** kullanır.
*   **Zaman Damgası:** Olay tam olarak ne zaman oldu? (Milisaniye hassasiyeti)
*   **Log Seviyesi:** Bu bir bilgi mi (INFO), bir uyarı mı (WARNING), yoksa kritik bir hata mı (ERROR)?
*   **Bağlam:** Bu olay hangi dosyanın, hangi fonksiyonunun, kaçıncı satırında oldu?

**Örnek Log Analizi:**
```log
# Zaman Damgası       | Seviye   | Modül:Fonksiyon:Satır          | Olay Mesajı
2025-12-27 14:05:22 | SUCCESS  | database:add_user:28           | Ajan 'Neo' sisteme başarıyla kaydedildi. (ID: 101)
2025-12-27 14:05:23 | WARNING  | auth:verify_signature:42       | Geçersiz imza denemesi tespit edildi! Kaynak IP: 192.168.1.5
2025-12-27 14:05:24 | INFO     | crypto:exchange_keys:99        | RSA Handshake (Anahtar Değişimi) başarıyla tamamlandı. Kanal güvenli.
```
*   **Otomatik Rotasyon:** Log dosyaları sonsuza kadar büyümez. 500MB'a ulaştığında sistem otomatik olarak dosyayı kapatır, sıkıştırır (zip) ve yeni bir dosya açar.
*   **Veri Saklama (Retention):** Eski loglar diskte yer kaplamaması için 10 gün sonra otomatik olarak imha edilir.

---

## 🛠️ BÖLÜM V: OPERASYONEL KURULUM

Kendi kriptografik komuta merkezinizi kurmak, sistemi ayağa kaldırmak ve sahadaki ajanlarınızla güvenli iletişim kurmak için aşağıdaki talimatları adım adım uygulayın.

### 🖥️ 5.1 Backend Kurulumu (Komuta Merkezi - Terminal)
Burası operasyonun beynidir. Tüm mesaj trafiği buradan akar (ancak şifreli olduğu için okunamaz).

```bash
# 1. Kaynak Kodunu İndirin
# GitHub'daki ana karargahtan en son kodları çeker.
git clone https://github.com/bahattinyunus/Hashchat.git

# 2. İzole Edilmiş Python Ortamı (Virtual Environment) Oluşturun
# Bu adım KRİTİKTİR. Sistem kütüphanelerinizle çakışmayı önler ve projeye özel, temiz bir alan açar.
cd Hashchat/Backend
python -m venv venv

# Windows Kullanıcıları için Aktivasyon:
.\venv\Scripts\activate
# Mac/Linux Kullanıcıları için Aktivasyon:
source venv/bin/activate

# 3. Mühimmat Yüklemesi (Bağımlılıklar)
# FastAPI (Web Framework), SQLAlchemy (Database), Loguru (Logging), Uvicorn (ASGI Server) kurulur.
pip install -r requirements.txt

# 4. Motorları Ateşleyin! 🔥
# --reload: Kodda bir değişiklik yaparsanız sunucuyu otomatik yeniden başlatır (Geliştirici Modu).
# --host 0.0.0.0: Sunucunun ağdaki tüm IP'lerden erişilebilir olmasını sağlar.
uvicorn main:app --reload --host 0.0.0.0 --port 12345
```

### 📱 5.2 Frontend Kurulumu (Saha Ajanı - Xcode)
Burası operasyonun yüzüdür. Son kullanıcı bu arayüzü kullanır.

1.  **Xcode'u Başlatın:** `Hashchat/Frontend/Hashchat.xcodeproj` dosyasını macOS üzerinde Xcode ile açın.
2.  **Paket Yönetimi:** Xcode, "Swift Package Manager" (SPM) aracılığıyla projenin ihtiyaç duyduğu harici kütüphaneleri (SnapKit, Alamofire vb. varsa) otomatik olarak analiz edecek ve arka planda indirecektir. Bu işlem internet hızınıza bağlı olarak 1-2 dakika sürebilir.
3.  **Hedef Cihaz:** Xcode'un üst barındaki simülatör listesinden güncel ve güçlü bir cihaz seçin (Örn: iPhone 15 Pro veya iPhone 16).
4.  **Derleme ve Çalıştırma:** Klavyenizdeki **Cmd + R** tuşlarına basın veya "Play" ikonuna tıklayın. Kod derlenecek ve sanal cihaz üzerinde uygulama açılacaktır.

---

## 🤝 KATKIDA BULUNMA
Bu proje, açık kaynak felsefesinin, bilginin özgürlüğünün ve kolektif zekanın bir anıtıdır. Siz olmadan eksiktir.
*   🐛 **Böcek Avcıları:** Kodda bir hata, bir güvenlik açığı veya performans sorunu mu buldun? -> Lütfen **Issues** sekmesine detaylı bir rapor bırakın.
*   💡 **Mühendisler:** Yeni bir şifreleme algoritması (Örn: ChaCha20-Poly1305) eklemek veya arayüzü modernize etmek mi istiyorsun? -> Kodunu çatalla (Fork), geliştir ve **Pull Request** gönder.
*   📜 **Kurallar:** Bu elit topluluğa katılmadan önce, iletişim kurallarımızı belirleyen [CONTRIBUTING.md](CONTRIBUTING.md) ve etik standartlarımızı belirleyen [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) anayasalarını dikkatlice okuyun.

---

<div align="center">
  <h3>📜 LİSANS: APACHE 2.0</h3>
  <p>Bu proje <b>Apache 2.0</b> lisansı ile lisanslanmıştır. Bu, yazılımı özgürce kullanabileceğiniz, değiştirebileceğiniz, dağıtabileceğiniz ve hatta ticari ürünlerde kullanabileceğiniz anlamına gelir. Bilgi paylaştıkça çoğalır.</p>
  
  <img src="https://img.shields.io/badge/GELİŞTİRİCİ-HASHCHAT_TİMİ-000000?style=for-the-badge" alt="Signature">
  <br>
  <i>"Karanlıkta çalışırız, ışığa hizmet ederiz." - Assassin's Creed / Cypherpunks</i>
</div>
