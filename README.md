<div align="center">
  <img src="assets/banner.png" alt="Hashchat Elite Banner" width="100%" style="border-radius: 10px; box-shadow: 0 0 30px rgba(0, 255, 255, 0.3);" />
  
  <br />
  <br />

  <!-- SYSTEM STATUS BADGES -->
  <a href="https://github.com/bahattinyunus/Hashchat/actions">
    <img src="https://img.shields.io/github/actions/workflow/status/bahattinyunus/Hashchat/ci.yml?branch=main&style=for-the-badge&logo=github&label=SYSTEM%20STATUS&color=00ff00" alt="System Status">
  </a>
  <a href="https://swift.org">
    <img src="https://img.shields.io/badge/CORE-SWIFT_5.9-orange?style=for-the-badge&logo=swift&logoColor=white" alt="Swift Core">
  </a>
  <a href="https://python.org">
    <img src="https://img.shields.io/badge/BACKEND-PYTHON_3.11-yellow?style=for-the-badge&logo=python&logoColor=white" alt="Python Backend">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/ENCRYPTION-RSA_2048-blueviolet?style=for-the-badge&logo=lock&logoColor=white" alt="RSA Encryption">
  </a>

  <br />
  
  <h1>🦅 HASHCHAT: ENTEGRE SİBER SAVUNMA PLATFORMU</h1>
  <h3><i>"Mahremiyet bir ayrıcalık değil, matematiksel bir kesinliktir."</i></h3>
  <p><b>Versiyon:</b> 2.0 (Elite Edition) | <b>Lisans:</b> Apache 2.0 | <b>Statü:</b> Operasyonel</p>
</div>

---

### 📟 SİSTEM GİRİŞİ BAŞLATILIYOR...

```console
user@hashchat-terminal:~$ ./initialize_protocol.sh --verbose
> [INIT] ÇEKİRDEK SİSTEMLER BAŞLATILIYOR...
> [LOAD] Kriptografik Motor (Pure Swift AES-128 Implementation)... YÜKLENDİ.
> [LOAD] Anahtar Yönetim Sistemi (RSA-2048 Manual Keygen)... YÜKLENDİ.
> [CNCT] Güvenli Soket Katmanı (WSS/TLS 1.3)... BAĞLANDI.
> [DB]   Kalıcı Veri Katmanı (SQLite + SQLAlchemy)... AKTİF.
> [LOG]  İstihbarat Servisi (Loguru Sink)... DİNLİYOR.
> SİSTEM HAZIR. "CAM KUTU" (GLASS-BOX) MODU AKTİF.
```

---

## 🎓 HASHCHAT AKADEMİSİ: GİZLİLİĞİN MİMARİSİ (TAM METİN)

Bu doküman, Hashchat projesinin **Resmi Teknik El Kitabıdır**. 
Buradaki bilgiler, basit bir yazılımın ötesinde; modern kriptografinin, ağ güvenliğinin ve ileri seviye yazılım mimarisinin temellerini öğretmek amacıyla, bir üniversite ders kitabı derinliğinde hazırlanmıştır.

**Okuyucuya Not:** Bu proje, ticari uygulamaların (WhatsApp, Telegram, Signal) arkasına saklanan "sihri" bozar ve size işin **saf matematiğini** gösterir.

### 📑 GÖREV MÜFREDATI (BÖLÜMLER)
| Bölüm | Konu Başlığı | Akademik Odak |
| :--- | :--- | :--- |
| **01** | [Felsefe ve Vizyon](#-bölüm-1-felsefe-ve-vizyon-detaylı-analiz) | Güvenlik Paradigmaları |
| **02** | [Sistem Mimarisi](#-bölüm-2-sistem-mimarisi-blueprint-teknik-derinlik) | Clean Architecture & AsyncIO |
| **03** | [Kriptografi Motoru](#-bölüm-3-kriptografi-motoru-the-engine-matematiksel-teori) | Galois Alanları & Asal Sayılar |
| **04** | [Veri ve İstihbarat](#-bölüm-4-veri-kalıcılığı-ve-istihbarat-persistence) | ACID Prensipleri & Loglama |
| **05** | [Saha Operasyonu](#-bölüm-5-saha-operasyonu-kurulum-ve-dağıtım) | DevOps & Deployment |

---

## 🏛️ BÖLÜM 1: FELSEFE VE VİZYON (DETAYLI ANALİZ)

<details open>
<summary><b>🔍 1.1 "Cam Kutu" (Glass-Box) vs "Kara Kutu" (Black-Box) Teorisi</b></summary>
<br>

Modern dünyada güvenlik, genellikle "belirsizlik" (obscurity) arkasına saklanır. Buna **"Security by Obscurity"** denir.
*   **Kara Kutu (Black-Box):** WhatsApp veya iMessage gibi uygulamalardır. Kaynak kodları kapalıdır. Firma size "Güvenliyiz" der ve siz buna inanmak zorunda kalırsınız. Arka kapı (backdoor) olup olmadığını bilemezsiniz.
*   **Cam Kutu (Glass-Box):** Hashchat'in benimsediği felsefedir. Güvenlik, kodun gizliliğinden değil, matematiğin sağlamlığından gelir (Kerckhoffs Prensibi).

Hashchat'te:
1.  Bir anahtarın (Key) bayt bayt nasıl üretildiğini **kod satırlarında görürsünüz**.
2.  Şifreli verinin (Ciphertext) ağda nasıl aktığını **loglarda izlersiniz**.
3.  Matematiğe (S-Box, Galois Alanı) bizzat **dokunursunuz**.

**Vizyonumuz:** 2030 yılına kadar kriptografik okuryazarlığa sahip, "dijital egemenliği" savunan 1000 elit geliştirici yetiştirmektir.
</details>

---

## 🏗️ BÖLÜM 2: SİSTEM MİMARİSİ (BLUEPRINT: TEKNİK DERİNLİK)

Hashchat, rastgele yazılmış bir kod yığını değildir. Endüstri standardı **Clean Architecture** ve **SOLID** prensipleriyle tasarlanmış, yaşayan bir organizmadır.

<table width="100%">
<tr>
<td width="50%">
<h3>📱 2.1 FRONTEND: iOS (Swift)</h3>
<p>Kullanıcı arayüzü, Apple ekosisteminin en modern "State-Driven" (Durum Tabanlı) mimarisi üzerine kuruludur.</p>

<h4>A. Declarative UI (SwiftUI)</h4>
<p>Klasik "Imperative" (UIKit) yapısının aksine, SwiftUI'da biz arayüzü çizmeyiz; arayüzün neye benzemesi gerektiğini <i>tarif ederiz</i>. <code>ChatView</code> bir fonksiyon değil, bir durumun (State) yansımasıdır.</p>

<h4>B. Reactive Pipeline (Combine)</h4>
<p>Hashchat, "Event-Driven" (Olay Güdümlü) çalışır. WebSocket'ten bir veri paketi geldiğinde:</p>
<pre><code>
WebSocket -> DataStream
  -> Decode (JSONDecoder)
  -> Map (Model Dönüşümü)
  -> ReceiveOn (MainThread)
  -> Assign (UI Update)
</code></pre>
<p>Bu akış (Pipeline), <b>Combine Framework</b> ile yönetilir ve milisaniyeler içinde gerçekleşir.</p>

<h4>C. Secure Enclave Entegrasyonu</h4>
<p>Kritik veriler (Özel Anahtarlar), cihazın ana işlemcisinde değil, <b>Secure Enclave</b> denilen izole edilmiş donanım kasasında şifrelenerek saklanır (Keychain).</p>
</td>
<td width="50%">
<h3>🧠 2.2 BACKEND: Python (FastAPI)</h3>
<p>Sunucu tarafı, "Bloklamayan" (Non-blocking) G/Ç mimarisine sahip, yüksek performanslı bir dijital röledir.</p>

<h4>A. Protokol: WSS (WebSocket Secure)</h4>
<p>Klasik HTTP protokolü "Telsiz" gibidir; bas-konuş (İstek at, cevap al). WebSocket ise <b>"Açık Telefon Hattı"</b> gibidir.</p>
<ul>
<li><b>Tam Çift Yönlü (Full-Duplex):</b> Sunucu ve istemci aynı anda konuşabilir.</li>
<li><b>Düşük Gecikme (Low Latency):</b> el sıkışma (Handshake) sadece bir kez yapılır.</li>
</ul>

<h4>B. Concurrency (AsyncIO)</h4>
<p>Python'un <code>async/await</code> yapısı sayesinde, sunucu tek bir işlemci çekirdeğinde binlerce kullanıcıyı aynı anda bekleyebilir. Bir kullanıcı mesaj yazarken sunucu "donmaz", diğer kullanıcıya hizmet verir.</p>
</td>
</tr>
</table>

---

## 🔐 BÖLÜM 3: KRİPTOGRAFİ MOTORU (THE ENGINE: MATEMATİKSEL TEORİ)

Burası projenin kalbidir. Hashchat, algoritmaları hazır kütüphanelerden çağırmakla yetinmez; onları **öğretir**.

### ⚔️ 3.1 SİMETRİK SAVAŞ SANATI: AES-128 DETAYLI ANALİZ
**Advanced Encryption Standard (AES)**, dünyanın en güvenli simetrik şifreleme standardıdır. Hashchat, bu algoritmayı **MANUEL OLARAK** Swift dilinde, her bayt işlemini görebilmeniz için sıfırdan yazmıştır.

<details open>
<summary><b>🧪 AES Laboratuvarı: Döngüler ve Matrisler</b></summary>

Veri 128 bitlik (4x4 Baytlık Matris) bloklar halinde 10 tur (Round) boyunca işlenir. Her turda 4 hayati operasyon gerçekleşir:

#### 1. SubBytes (Doğrusal Olmayan Değişim - Confusion) 🎭
Her bayt, `S-Box` (Substitution Box) adı verilen özel bir matematiksel tablo kullanılarak başka bir baytla değiştirilir.
*   **Amaç:** Giriş verisi ile çıkış verisi arasındaki istatistiksel ilişkiyi tamamen koparmaktır. "a" harfi her zaman aynı şifreye dönüşmez.

#### 2. ShiftRows (Satır Kaydırma - Diffusion I) 🌪️
Durum matrisinin satırları, belirli ofsetlerle sola doğru kaydırılır.
*   1. Satır: Kaydırılmaz.
*   2. Satır: 1 bayt sola.
*   3. Satır: 2 bayt sola.
*   4. Satır: 3 bayt sola.
*   **Amaç:** Veriyi blok geneline yaymaktır.

#### 3. MixColumns (Sütun Karıştırma - Diffusion II) 📐
Sütunlar, Galois Alanı ($GF(2^8)$) matematiği kullanılarak, özel bir polinom ile çarpılır.
*   **Matematik:** Bu işlem normal çarpma değildir; sonlu cisim aritmetiğidir.
*   **Sonuç:** Girişteki tek bir bitlik değişim, çıkışta baytların yarısını değiştirir (Çığ Etkisi - Avalanche Effect).

#### 4. AddRoundKey (Anahtar Kilitleme) 🔐
O anki turun anahtarı (Subkey) ile mevcut durum matrisi üzerinde **XOR** işlemi uygulanır. Şifrenin anahtara bağımlı olduğu tek adım budur.
</details>

### 🛡️ 3.2 ASİMETRİK KALKAN: RSA-2048 TEORİSİ
İki yabancının (Alice ve Bob), daha önce hiç karşılaşmadan güvenli bir şifre üzerinde anlaşabilmesi mucizesidir.

<details>
<summary><b>📐 RSA Matematiği: İmkansız Çarpanlara Ayırma</b></summary>

RSA'nın güvenliği, tek yönlü bir matematiksel fonksiyona dayanır: **Büyük sayıları çarpmak kolaydır, ancak çarpanlarına ayırmak çok zordur.**

1.  **Anahtar Üretimi ($KeyGen$):**
    *   İki devasa asal sayı seçilir: $p$ ve $q$.
    *   Modulus hesaplanır: $n = p \times q$. (Bu $n$ sayısı 2048 bittir, yani yaklaşık 600 basamaklı bir sayıdır).
    *   $\phi(n)$ (Euler's Totient) fonksiyonu hesaplanır.

2.  **Şifreleme ($Encrypt$):**
    *   Mesaj ($m$), sayi formatına çevrilir.
    *   Şifreli metin $c = m^e \pmod n$ formülüyle bulunur. ($e$: Public Exponent).

3.  **Deşifreleme ($Decrypt$):**
    *   Orijinal mesaj $m = c^d \pmod n$ formülüyle geri getirilir. ($d$: Private Exponent).

> **Güvenlik Kanıtı:** $n$ sayısını $p$ ve $q$ çarpanlarına ayırmadan $d$ değerini bulmak matematiksel olarak imkansızdır.
</details>

---

## 💾 BÖLÜM 4: VERİ KALICILIĞI VE İSTİHBARAT (PERSISTENCE)

**Hashchat V2.0** ile sistem, geçici bir prototipten ("Unutkan" Hafıza) profesyonel bir veri altyapısına ("Kalıcı" Hafıza) evrilmiştir.

### 🏛️ 4.1 IRONCLAD PERSISTENCE (SQLite + SQLAlchemy)
Eskiden sunucu yeniden başlatıldığında tüm kullanıcılar silinirdi. Artık veriler disk üzerinde atomik bir yapıda saklanır.

*   **Technology:** **SQLite**, sunucusuz (serverless) ve dosya tabanlı bir ilişkisel veritabanıdır.
*   **ORM (Object Relational Mapping):** **SQLAlchemy**, veritabanı tablolarını Python sınıflarına (Class) dönüştürür.
    *   Biz `INSERT INTO users...` yazmayız. `db.add(new_user)` deriz.
    *   **ACID Uyumluluğu:** (Atomicity, Consistency, Isolation, Durability) prensipleri sayesinde veri bütünlüğü garanti altındadır.

### 📡 4.2 ELITE INTELLIGENCE (Loguru)
İyi bir komutan, savaş alanındaki her hareketi izler. Hashchat İstihbarat Modülü (Loguru), sistemdeki her nefesi kaydeder.

**Örnek Log Analizi:**
```log
# Zaman Damgası       | Seviye   | Modül:Fonksiyon:Satır          | Olay Mesajı
2025-12-27 14:05:22 | SUCCESS  | database:add_user:28           | Ajan 'Neo' sisteme kaydedildi.
2025-12-27 14:05:23 | WARNING  | auth:verify_signature:42       | Geçersiz imza denemesi! IP: 192.168.1.5
2025-12-27 14:05:24 | INFO     | crypto:exchange_keys:99        | RSA Handshake (Anahtar Değişimi) tamamlandı.
```

---

## 🛠️ BÖLÜM 5: SAHA OPERASYONU (KURULUM VE DAĞITIM)

Kendi kriptografik komuta merkezinizi kurmak için aşağıdaki talimatları takip edin.

<details open>
<summary><b>🖥️ Backend Kurulumu (Komuta Merkezi - Terminal)</b></summary>

```bash
# 1. Kaynak Kodunu İndirin
git clone https://github.com/bahattinyunus/Hashchat.git

# 2. İzole Edilmiş Python Ortamı (Virtual Environment)
# Bu adım, sistem kütüphanelerinizle çakışmayı önler.
cd Hashchat/Backend
python -m venv venv

# Windows Kullanıcıları için Aktivasyon:
.\venv\Scripts\activate
# Mac/Linux Kullanıcıları için Aktivasyon:
source venv/bin/activate

# 3. Mühimmat Yüklemesi (Bağımlılıklar)
# FastAPI, SQLAlchemy, Loguru, Uvicorn vb. yüklenir.
pip install -r requirements.txt

# 4. Motorları Ateşleyin! 🔥
# --reload: Kod değişirse sunucuyu otomatik yeniden başlatır (Geliştirici Modu).
uvicorn main:app --reload --host 0.0.0.0 --port 12345
```
</details>

<details>
<summary><b>📱 Frontend Kurulumu (Saha Ajanı - Xcode)</b></summary>

1.  **Xcode'u Başlatın:** `Hashchat/Frontend/Hashchat.xcodeproj` dosyasını açın.
2.  **Bağımlılıklar:** Swift Package Manager (SPM) otomatik olarak gerekli paketleri indirecektir.
3.  **Hedef Cihaz:** Simülatör listesinden güncel bir cihaz seçin (Örn: iPhone 15 Pro).
4.  **Derleme:** **Cmd + R** tuşlarına basarak projeyi derleyin ve çalıştırın.
</details>

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
  
  <img src="https://img.shields.io/badge/DEVELOPED_BY-HASHCHAT_TEAM-000000?style=for-the-badge" alt="Signature">
  <br>
  <i>"Karanlıkta çalışırız, ışığa hizmet ederiz." - Assassin's Creed / Cypherpunks</i>
</div>
