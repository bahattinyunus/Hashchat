<div align="center">
  <img src="assets/banner.png" alt="Hashchat Elite Banner" width="100%" style="border-radius: 10px; box-shadow: 0 0 40px rgba(0, 255, 255, 0.4);" />
  
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
  <h3><i>"Mahremiyet bir ayrıcalık değil, matematiksel bir kesinliktir."</i></h3>
  <p><b>Versiyon:</b> 2.0 (Elite Edition) | <b>Mimari:</b> Zero-Knowledge Relay | <b>Lisans:</b> Apache 2.0</p>
</div>

---

### 📟 SİSTEM GİRİŞİ BAŞLATILIYOR...

```console
root@hashchat-command-center:~$ ./initialize_protocol.sh --verbose --level=MAX
> [INIT] ÇEKİRDEK SİSTEMLER BAŞLATILIYOR... (ZAMAN: 0.003s)
> [LOAD] Kriptografik Motor (Pure Swift AES-128 Implementation)... DOĞRULANDI.
> [LOAD] Anahtar Yönetim Sistemi (RSA-2048 OAEP/SHA256)... DOĞRULANDI.
> [CNCT] Güvenli Soket Katmanı (WSS/TLS 1.3)... BAĞLANTI KURULDU @ PORT 12345.
> [DB]   Kalıcı Veri Katmanı (SQLite + SQLAlchemy ORM v2.0)... ŞEMA SENKRONİZE.
> [LOG]  İstihbarat Servisi (Loguru Sink)... AKTİF VE DİNLİYOR.
> SİSTEM HAZIR. "CAM KUTU" (GLASS-BOX) PROTOKOLÜ DEVREDE.
```

---

## 🎓 HASHCHAT AKADEMİSİ: BÜYÜK ANSİKLOPEDİ (MAGNUM OPUS)

Bu doküman, Hashchat projesinin **Nihai Kaynak Kodudur**. Bir yazılım projesinin ötesinde, bu bir **Siber Güvenlik Manifestosu** ve **Kriptografi Ders Kitabıdır**.

Buradaki her satır, ticari uygulamaların (WhatsApp, Telegram, Signal) arkasına saklanan "sihri" bozmak ve size **işin mutfağındaki saf matematiği** öğretmek için yazılmıştır.

---

### 📑 İÇİNDEKİLER VE MÜFREDAT
1.  **[Bölüm I: Felsefe ve Vizyon](#-bölüm-i-felsefe-ve-vizyon)**
    *   Cam Kutu Teorisi
    *   Kerckhoffs Prensibi
2.  **[Bölüm II: Sistem Mimarisi (Blueprint)](#-bölüm-ii-sistem-mimarisi-blueprint)**
    *   Frontend: Declarative UI & Reactive Streams
    *   Backend: Asenkron Röle & WSS Protokolü
3.  **[Bölüm III: Kriptografi Motoru (The Engine)](#-bölüm-iii-kriptografi-motoru-the-engine)**
    *   Simetrik: AES-128 (Matematiksel Analiz)
    *   Asimetrik: RSA-2048 (Sayılar Teorisi)
4.  **[Bölüm IV: Veri Kalıcılığı ve İstihbarat](#-bölüm-iv-veri-kalıcılığı-ve-istihbarat)**
    *   Ironclad Persistence (SQLAlchemy)
    *   Elite Intelligence (Loguru)
5.  **[Bölüm V: Operasyonel Kurulum](#-bölüm-v-operasyonel-kurulum)**

---

## 🏛️ BÖLÜM I: FELSEFE VE VİZYON

### 1.1 "Güvenlik, Bilinmezlik Değildir"
Modern dünyada güvenlik, genellikle "belirsizlik" (obscurity) arkasına saklanır. Buna **"Security by Obscurity"** denir. Firmalar, kodlarını ne kadar saklarlarsa o kadar güvenli olduklarını sanarlar. Bu büyük bir yanılgıdır.

**Hashchat'in Felsefesi (Cam Kutu Yaklaşımı):**
Bizim güvenliğimiz, kaynak kodumuzun gizliliğinden değil, kullandığımız matematiksel algoritmaların (AES, RSA) sağlamlığından gelir.
*   Bir saldırgan (Hacker) tüm kaynak kodumuza sahip olsa bile, şifreli mesajları çözemez.
*   Buna **Kerckhoffs Prensibi** denir: *"Bir kriptosistemin güvenliği, algoritmanın gizliliğine değil, anahtarın gizliliğine dayanmalıdır."*

### 1.2 Neden Bu Projeyi Yaptık?
Çoğu geliştirici şifreleme kütüphanelerini (`import crypto`) kullanır ancak arka planda ne olduğunu bilmez. Hashchat, bu kara kutuyu açar.
*   🔑 Bir anahtarın (Key) bayt bayt nasıl üretildiğini **kod satırlarında görürsünüz**.
*   🌐 Şifreli verinin ağı nasıl terk ettiğini **izlersiniz**.
*   🧮 Matematiğe (S-Box, Galois Alanı) bizzat **dokunursunuz**.

> **Hedefimiz:** 2030 yılına kadar kriptografik okuryazarlığa sahip, "dijital egemenliği" savunan 1000 elit geliştirici yetiştirmek.

---

## 🏗️ BÖLÜM II: SİSTEM MİMARİSİ (BLUEPRINT)

Hashchat, rastgele yazılmış bir kod yığını değildir. Endüstri standardı **Clean Architecture** prensipleriyle, canlı bir organizma gibi tasarlanmıştır.

### 📱 2.1 FRONTEND: iOS (Swift)
Kullanıcı arayüzü, Apple ekosisteminin en modern mimarisi üzerine kuruludur.

#### A. SwiftUI (Görsel Dil)
Klasik "Imperative" (UIKit) yapısının aksine, SwiftUI'da biz arayüzü çizmeyiz; arayüzün neye benzemesi gerektiğini **tarif ederiz**.
*   **State-Driven (Durum Güdümlü):** `ChatView` bir fonksiyon değil, `ChatViewModel` üzerindeki verinin anlık bir yansımasıdır. Veri değiştiği an, ekran otomatik olarak yeniden çizilir.

#### B. Combine Framework (Reaktif Sinir Sistemi)
Hashchat, olay güdümlü (Event-Driven) çalışır. WebSocket'ten bir veri paketi geldiğinde, bu veri bir boru hattından (Pipeline) geçer:
1.  **Publisher:** Ağ soketinden ham veri (Raw Data) gelir.
2.  **Operator:** JSON formatındaki veri, Swift nesnelerine (Model) dönüştürülür.
3.  **Scheduler:** İşlemler arka planda yapılır, sonuç ana iş parçacığına (Main Thread) gönderilir.
4.  **Subscriber:** UI güncellenir.
*   Bu akış milisaniyeler sürer ve cihazı yormaz.

#### C. Secure Enclave (Dijital Kasa)
Kritik veriler (Özel Anahtarlar), cihazın işletim sisteminde değil, **Secure Enclave** denilen, fiziksel olarak izole edilmiş donanım kasasında şifrelenerek saklanır (Keychain). Telefon hacklense bile bu anahtarlara ulaşılamaz.

### 🧠 2.2 BACKEND: Python (FastAPI)
Sunucu tarafı, "Bloklamayan" (Non-blocking) G/Ç mimarisine sahip, yüksek performanslı bir dijital röledir.

#### A. WSS Protokolü (Sürekli Bağlantı)
Klasik HTTP protokolü "Telsiz" gibidir; bas-konuş (İstek at, cevap al). WebSocket ise **"Açık Telefon Hattı"** gibidir.
*   **Tam Çift Yönlü (Full-Duplex):** Sunucu ve istemci aynı anda konuşabilir.
*   **Düşük Gecikme:** El sıkışma (Handshake) sadece bir kez yapılır, sonra hat açık kalır.

#### B. AsyncIO (Eşzamanlılık)
Python'un `async/await` yapısı sayesinde, sunucu tek bir işlemci çekirdeğinde binlerce kullanıcıyı aynı anda bekleyebilir.
*   Geleneksel sunucular (Thread based) her kullanıcı için yeni bir iş parçacığı açar ve RAM tüketir.
*   Hashchat (Event loop based) tek bir döngüde herkesi dinler. Çok daha hafiftir.

---

## 🔐 BÖLÜM III: KRİPTOGRAFİ MOTORU (THE ENGINE)

Burası projenin kalbidir. Hashchat, algoritmaları hazır kütüphanelerden çağırmakla yetinmez; onları **öğretir**.

### ⚔️ 3.1 SİMETRİK SAVAŞ SANATI: AES-128
**Advanced Encryption Standard (AES)**, ABD hükümetinin ve bankaların verilerini korumak için kullandığı standarttır. Hashchat, bu algoritmayı **MANUEL OLARAK** Swift dilinde, her bayt işlemini görebilmeniz için sıfırdan yazmıştır.

Veri 128 bitlik (4x4 Baytlık Matris) bloklar halinde 10 tur (Round) boyunca işlenir. Her turda 4 hayati operasyon gerçekleşir:

#### 1. SubBytes (Doğrusal Olmayan Değişim - Confusion) 🎭
Her bayt, `S-Box` (Substitution Box) adı verilen özel bir matematiksel tablo kullanılarak bambaşka bir baytla değiştirilir.
*   **Amaç:** Giriş verisi ile çıkış verisi arasındaki istatistiksel ilişkiyi tamamen koparmaktır. "a" harfi her zaman aynı şifreye dönüşmez, kaos yaratılır.

#### 2. ShiftRows (Satır Kaydırma - Diffusion I) 🌪️
Durum matrisinin satırları, belirli ofsetlerle sola doğru kaydırılır.
*   1. Satır: Dokunulmaz.
*   2. Satır: 1 bayt sola.
*   3. Satır: 2 bayt sola.
*   4. Satır: 3 bayt sola.
*   **Amaç:** Veriyi blok geneline yaymaktır. Bir baytın etkisi diğer sütunlara taşınır.

#### 3. MixColumns (Sütun Karıştırma - Diffusion II) 📐
Sütunlar, Galois Alanı ($GF(2^8)$) matematiği kullanılarak, özel bir polinom ile çarpılır.
*   **Büyü:** Bu işlem normal çarpma değildir; sonlu cisim aritmetiğidir.
*   **Sonuç:** Girişteki tek bir bitlik değişim, çıkışta baytların yarısını değiştirir (Çığ Etkisi - Avalanche Effect).

#### 4. AddRoundKey (Anahtar Kilitleme) 🔐
O anki turun anahtarı (Subkey) ile mevcut durum matrisi üzerinde **XOR** işlemi uygulanır. Şifrenin anahtara bağımlı olduğu yegane adım budur.

### 🛡️ 3.2 ASİMETRİK KALKAN: RSA-2048
İki yabancının (Alice ve Bob), daha önce hiç karşılaşmadan güvenli bir şifre üzerinde anlaşabilmesi mucizesidir.

#### RSA'nın Matematiksel Temeli:
RSA güvenliği, tek yönlü bir matematiksel fonksiyona dayanır: **Büyük sayıları çarpmak kolaydır, ancak çarpanlarına ayırmak evrensel ölçekte zordur.**

1.  **Anahtar Üretimi ($KeyGen$):**
    *   İki devasa asal sayı seçilir: $p$ ve $q$.
    *   Modulus hesaplanır: $n = p \times q$. (Bu $n$ sayısı 2048 bittir, yani yaklaşık 617 basamaklı ondalık bir sayıdır).
    *   $\phi(n)$ (Euler's Totient) fonksiyonu hesaplanır. Bu, $n$'den küçük ve $n$ ile aralarında asal olan sayıların adedidir.

2.  **Şifreleme ($Encrypt$):**
    *   Mesaj ($m$), sayısal formata çevrilir.
    *   Şifreli metin $c = m^e \pmod n$ formülüyle bulunur. ($e$: Public Exponent, genellikle 65537).

3.  **Deşifreleme ($Decrypt$):**
    *   Orijinal mesaj $m = c^d \pmod n$ formülüyle geri getirilir. ($d$: Private Exponent).

> **Güvenlik Kanıtı:** $n$ sayısını $p$ ve $q$ çarpanlarına ayırmadan gizli üs $d$'yi bulmak matematiksel olarak imkansızdır. Bunu yapmak için gereken enerji, dünya üzerindeki tüm okyanusları kaynatmaya yeter.

---

## 💾 BÖLÜM IV: VERİ KALICILIĞI VE İSTİHBARAT

**Hashchat V2.0** ile sistem, geçici bir prototipten ("Unutkan" Hafıza) profesyonel bir veri altyapısına ("Kalıcı" Hafıza) evrilmiştir.

### 🏛️ 4.1 IRONCLAD PERSISTENCE (SQLite + SQLAlchemy)
Eskiden sunucu yeniden başlatıldığında tüm kullanıcılar silinirdi. Artık veriler disk üzerinde atomik bir yapıda saklanır.

*   **Veritabanı Motoru:** **SQLite**. Sunucusuz, dosya tabanlı ve ACİD uyumlu bir motordur. Tüm veritabanı tek bir dosyada (`hashchat.db`) tutulur, bu da yedeklemeyi ve taşımayı inanılmaz kolaylaştırır.
*   **ORM (Object Relational Mapping):** **SQLAlchemy 2.0**.
    *   Biz ham SQL (`SELECT * FROM users`) yazmayız. Python sınıfları ile konuşuruz (`db.scalars(select(User))`).
    *   Bu yöntem, **SQL Injection** saldırılarına karşı %100 koruma sağlar.

### 📡 4.2 ELITE INTELLIGENCE (Loguru)
İyi bir komutan, savaş alanındaki her hareketi izler. Hashchat İstihbarat Modülü (Loguru), sistemdeki her dijital nefesi kaydeder.

**Örnek Log Analizi:**
```log
# Zaman Damgası       | Seviye   | Modül:Fonksiyon:Satır          | Olay Mesajı
2025-12-27 14:05:22 | SUCCESS  | database:add_user:28           | Ajan 'Neo' sisteme başarıyla kaydedildi.
2025-12-27 14:05:23 | WARNING  | auth:verify_signature:42       | Geçersiz imza denemesi tespit edildi! IP: 192.168.1.5
2025-12-27 14:05:24 | INFO     | crypto:exchange_keys:99        | RSA Handshake (Anahtar Değişimi) tamamlandı. Kanal güvenli.
```
*   **Rotasyon:** Log dosyaları 500MB'a ulaştığında otomatik olarak yeni dosya açılır.
*   **Saklama:** Eski loglar 10 gün sonra otomatik imha edilir (Güvenlik politikası).

---

## 🛠️ BÖLÜM V: OPERASYONEL KURULUM

Kendi kriptografik komuta merkezinizi kurmak için aşağıdaki talimatları adım adım uygulayın.

### 🖥️ 5.1 Backend Kurulumu (Komuta Merkezi - Terminal)

```bash
# 1. Kaynak Kodunu İndirin
git clone https://github.com/bahattinyunus/Hashchat.git

# 2. İzole Edilmiş Python Ortamı (Virtual Environment) Oluşturun
# Bu adım, sistem kütüphanelerinizle çakışmayı önler ve temiz bir sayfa açar.
cd Hashchat/Backend
python -m venv venv

# Windows Kullanıcıları için Aktivasyon:
.\venv\Scripts\activate
# Mac/Linux Kullanıcıları için Aktivasyon:
source venv/bin/activate

# 3. Mühimmat Yüklemesi (Bağımlılıklar)
# FastAPI, SQLAlchemy, Loguru, Uvicorn ve diğer savaş gereçleri yüklenir.
pip install -r requirements.txt

# 4. Motorları Ateşleyin! 🔥
# --reload: Kod değişirse sunucuyu otomatik yeniden başlatır (Geliştirici Modu).
uvicorn main:app --reload --host 0.0.0.0 --port 12345
```

### 📱 5.2 Frontend Kurulumu (Saha Ajanı - Xcode)

1.  **Xcode'u Başlatın:** `Hashchat/Frontend/Hashchat.xcodeproj` dosyasını açın.
2.  **Paket Yönetimi:** Swift Package Manager (SPM) otomatik olarak devreye girecek ve gerekli paketleri indirecektir. İnternet hızınıza bağlı olarak 1-2 dakika sürebilir.
3.  **Hedef Cihaz:** Simülatör listesinden güncel bir cihaz seçin (Örn: iPhone 15 Pro).
4.  **Derleme:** **Cmd + R** tuşlarına basarak projeyi derleyin ve çalıştırın.

---

## 🤝 KATKIDA BULUNMA
Bu proje, açık kaynak felsefesinin bir anıtıdır.
*   🐛 **Böcek Avcıları:** Hata mı buldun? -> **Issues** sekmesine raporla.
*   💡 **Mühendisler:** Yeni bir şifreleme algoritması mı (Örn: ChaCha20) eklemek istiyorsun? -> **Pull Request** gönder.
*   📜 **Kurallar:** Katkıda bulunmadan önce [CONTRIBUTING.md](CONTRIBUTING.md) ve [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) anayasalarını okuyun.

---

<div align="center">
  <h3>📜 LİSANS: APACHE 2.0</h3>
  <p>Özgür Yazılım. Sonsuza Kadar. Kısıtlama Yok.</p>
  
  <img src="https://img.shields.io/badge/GELİŞTİRİCİ-HASHCHAT_TİMİ-000000?style=for-the-badge" alt="Signature">
  <br>
  <i>"Karanlıkta çalışırız, ışığa hizmet ederiz." - Assassin's Creed / Cypherpunks</i>
</div>
