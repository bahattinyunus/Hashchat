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
  
  <h1>🦅 HASHCHAT: KOMUTA MERKEZİ</h1>
  <h3><i>"Mahremiyet bir ayrıcalık değil, matematiksel bir kesinliktir."</i></h3>
</div>

---

### 📟 SİSTEM GİRİŞİ BAŞLATILIYOR...

```console
user@hashchat-terminal:~$ ./initialize_protocol.sh
> BAĞLANTI KURULUYOR... [OK]
> ŞİFRELEME MODÜLLERİ YÜKLENİYOR (AES-128, RSA-2048)... [OK]
> VERİTABANI BAĞLANTISI (SQLAlchemy)... [OK]
> SİSTEM HAZIR. "CAM KUTU" MODU AKTİF.
```

---

## 🎓 HASHCHAT AKADEMİSİ: GİZLİLİĞİN MİMARİSİ
Bu doküman klasik bir "Beni Oku" dosyası değildir. Modern siber güvenliğin kalbine inen, yaşayan bir ders kitabıdır. **Hashchat**, güvenlik mekanizmalarını saklamaz; onları **sergiler**.

### 📑 GÖREV MÜFREDATI
| Bölüm | Konu | İçerik Özeti |
| :--- | :--- | :--- |
| **01** | [Felsefe](#-bölüm-1-felsefe-ve-vizyon) | Neden "Cam Kutu" Teorisi? |
| **02** | [Mimarinin Mavi Özü](#-bölüm-2-sistem-mimarisi-blueprint) | SwiftUI ve FastAPI'nin Dansı |
| **03** | [Kriptografi Motoru](#-bölüm-3-kriptografi-motoru-the-engine) | AES ve RSA'nın Matematiği |
| **04** | [İstihbarat & Hafıza](#-bölüm-4-veri-kalıcılığı-ve-istihbarat) | SQLite, SQLAlchemy ve Loguru |
| **05** | [Operasyon](#-bölüm-5-saha-operasyonu-kurulum) | Komuta Merkezini Başlatma |

---

## 🏛️ BÖLÜM 1: FELSEFE VE VİZYON

<details>
<summary><b>🔍 "Cam Kutu" (Glass-Box) Teorisi Nedir? (Tıklayıp Genişletin)</b></summary>
<br>

> Çoğu mesajlaşma uygulaması (WhatsApp, Signal) güvenlidir, ancak birer "Kara Kutu"dur. İçini göremezsiniz.

**Hashchat farklıdır.** Biz, güvenliği matematiksel şeffaflıkla sağlıyoruz:
*   🔑 Bir anahtarın (Key) bayt bayt nasıl üretildiğini **görürsünüz**.
*   🌐 Şifreli verinin (Ciphertext) ağda nasıl aktığını **izlersiniz**.
*   🧮 Matematiğe (S-Box, Galois Alanı) dokunursunuz.

**Hedef:** 2030 yılına kadar siber egemenlik bilincine sahip 1000 "Elit" geliştirici yetiştirmek.
</details>

---

## 🏗️ BÖLÜM 2: SİSTEM MİMARİSİ (BLUEPRINT)

<table width="100%">
<tr>
<td width="50%">
<h3>📱 FRONTEND: iOS (Swift)</h3>
<p>Kullanıcı arayüzü, Apple'ın en ileri teknolojileriyle donatılmıştır.</p>
<ul>
<li><b>SwiftUI:</b> Deklaratif UI. Animasyonlar ve durum yönetimi (State) için rakipsiz.</li>
<li><b>Combine:</b> Reaktif Veri Akışı. WebSocket'ten gelen canlı veri paketlerini saniyenin binde birinde işler.</li>
<li><b>Secure Enclave:</b> Anahtarlar donanım seviyesinde (Hardware Level) korunur.</li>
</ul>
</td>
<td width="50%">
<h3>🧠 BACKEND: Python (FastAPI)</h3>
<p>Sunucu tarafı, asenkron ve yüksek performanslı bir dijital röledir.</p>
<ul>
<li><b>WSS Protokolü:</b> WebSocket Secure. Sürekli açık, şifreli hat.</li>
<li><b>AsyncIO:</b> Tek bir çekirdekte binlerce eşzamanlı bağlantıyı yöneten "Non-blocking" mimari.</li>
<li><b>Zero-Knowledge:</b> Sunucu, mesaj içeriğini ASLA bilmez. Sadece şifreli paketleri taşır.</li>
</ul>
</td>
</tr>
</table>

---

## 🔐 BÖLÜM 3: KRİPTOGRAFİ MOTORU (THE ENGINE)

Burası işin mutfağıdır. Hashchat, algoritmaları kütüphaneden çağırmaz; onları **öğretir**.

### ⚔️ SİMETRİK SAVAŞ SANATI: AES-128
**Advanced Encryption Standard**, ABD hükümetinin kullandığı standarttır. Hashchat, bu algoritmayı eğitim amacıyla **MANUEL OLARAK** (sıfırdan) kodlamıştır.

<details>
<summary><b>🧪 AES Laboratuvarı: Baytlar Nasıl Karışır? (Detaylı Analiz)</b></summary>

Veri 128 bitlik bloklar halinde 4 aşamadan geçer:

1.  **SubBytes (Maskeleme)** 🎭
    *   `S-Box` tablosu kullanılarak her bayt, doğrusal olmayan bir şekilde değiştirilir. İstatistiksel analizi imkansız kılar.
2.  **ShiftRows (Karıştırma)** 🌪️
    *   Matris satırları sola doğru kaydırılır. Veri blok geneline yayılır (Diffusion).
3.  **MixColumns (Dönüştürme)** 📐
    *   Sütunlar, Galois Alanı ($GF(2^8)$) matematiği ile çarpılır. Tek bir bit değişirse, tüm blok değişir.
4.  **AddRoundKey (Kilitleme)** 🔐
    *   O turun anahtarı ile XOR işlemi yapılır.
</details>

### 🛡️ ASİMETRİK KALKAN: RSA-2048
İki yabancının güvenli konuşabilmesi için "Açık Anahtar" (Public Key) sistemi kullanılır.

<details>
<summary><b>📐 RSA Matematiği: Neden Kırılamaz?</b></summary>

RSA'nın güvenliği, iki çok büyük asal sayıyı çarpmanın kolay ($p \times q = n$), ancak çarpanlarına ayırmanın imkansız olması ilkesine dayanır.

*   **Modulus ($n$):** 2048 bit (Tam 617 basamaklı bir sayı!).
*   **İşlem Gücü:** Şu anki süper bilgisayarlarla bu sayıyı çarpanlarına ayırmak evrenin yaşından uzun sürer.
*   **Padding:** OAEP (Optimal Asymmetric Encryption Padding) kullanılarak, aynı mesajın her seferinde farklı görünmesi sağlanır.
</details>

---

## 💾 BÖLÜM 4: VERİ KALICILIĞI VE İSTİHBARAT

**Hashchat V2.0** ile profesyonel veri altyapısına geçilmiştir.

### 🏛️ IRONCLAD PERSISTENCE (SQLite + SQLAlchemy)
Eskiden sunucu kapanınca veriler uçardı. Artık **Kalıcı**.
*   **ORM Yapısı:** SQL sorguları yerine Python sınıfları kullanılır.
*   **ACID Uyumluluğu:** Veri bütünlüğü garantidir.
*   **Tek Gerçeklik Kaynağı:** `hashchat.db`.

### 📡 ELITE INTELLIGENCE (Loguru)
Sistem sizinle konuşur. Konsol çıktısı bir "Matrix" ekranı gibidir:

```log
2025-12-27 14:05:22 | SUCCESS  | database:add_user - Ajan 'Neo' sisteme kaydedildi.
2025-12-27 14:05:23 | WARNING  | auth:verify_signature - Geçersiz imza denemesi! IP: 192.168.1.5
2025-12-27 14:05:24 | INFO     | crypto:exchange_keys - RSA Handshake tamamlandı.
```

---

## 🛠️ BÖLÜM 5: SAHA OPERASYONU (KURULUM)

Kendi komuta merkezinizi kurmaya hazır mısınız?

<details open>
<summary><b>🖥️ Backend Kurulumu (Terminal)</b></summary>

```bash
# 1. Repoyu Klonlayın
git clone https://github.com/bahattinyunus/Hashchat.git

# 2. Sanal Ortama Geçiş Yapın
cd Hashchat/Backend
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# 3. Mühimmatı Yükleyin
pip install -r requirements.txt

# 4. Ateşleyin! 🔥
uvicorn main:app --reload --host 0.0.0.0 --port 12345
```
</details>

<details>
<summary><b>📱 Frontend Kurulumu (Xcode)</b></summary>

1.  `Hashchat/Frontend/Hashchat.xcodeproj` dosyasını Xcode ile açın.
2.  Paketlerin yüklenmesini bekleyin.
3.  Hedef cihazı seçin (iPhone 15 Pro).
4.  **Cmd + R** ile operasyonu başlatın.
</details>

---

## 🤝 KATKIDA BULUNMA
Bu proje açık kaynaktır ve topluluğun gücüyle büyür.
*   🐛 Hata mı buldun? -> **Issues**
*   💡 Fikrin mi var? -> **Pull Request**
*   📜 Kurallar -> [CONTRIBUTING.md](CONTRIBUTING.md) ve [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

<div align="center">
  <h3>📜 LİSANS: APACHE 2.0</h3>
  <p>Özgür Yazılım. Sonsuza Kadar.</p>
  
  <img src="https://img.shields.io/badge/DEVELOPED_BY-HASHCHAT_TEAM-000000?style=for-the-badge" alt="Signature">
  <br>
  <i>"Karanlıkta çalışırız, ışığa hizmet ederiz."</i>
</div>
