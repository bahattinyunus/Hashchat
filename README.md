# 🦅 Hashchat: Elit Kriptografik Komuta Merkezi

> **"Mahremiyet bir ayrıcalık değil, matematiksel bir kesinliktir."** - *Cypherpunk Manifestosu*

<div align="center">
  <img src="assets/banner.png" alt="Hashchat Elite Banner" width="100%" style="border-radius: 10px; box-shadow: 0 0 20px rgba(0, 255, 255, 0.5);" />
  <br/>
  <br/>
  <!-- Rozetler: Projenin gücünü gösterir -->
  <a href="https://github.com/bahattinyunus/Hashchat/blob/main/LICENSE"><img src="https://img.shields.io/badge/Lisans-Apache%202.0-blue.svg?style=for-the-badge&logo=apache" alt="License"></a>
  <a href="https://github.com/bahattinyunus/Hashchat/actions"><img src="https://img.shields.io/github/actions/workflow/status/bahattinyunus/Hashchat/ci.yml?branch=main&style=for-the-badge&logo=github-actions" alt="CI Status"></a>
  <a href="https://swift.org"><img src="https://img.shields.io/badge/Swift-5.9-orange.svg?style=for-the-badge&logo=swift" alt="Swift"></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.11-yellow.svg?style=for-the-badge&logo=python" alt="Python"></a>
  <a href="https://developer.apple.com/documentation/security"><img src="https://img.shields.io/badge/Security-CommonCrypto-green.svg?style=for-the-badge&logo=apple" alt="Security"></a>
  <br/>
  <br/>
</div>

---

# 🎓 Hashchat Akademisi'ne Hoşgeldiniz
Bu doküman sadece bir "Beni Oku" dosyası değildir; burası modern siber güvenliğin kalbine açılan kapıdır. **Hashchat**, ticari mesajlaşma uygulamalarının (WhatsApp, Signal) arkasındaki "sihri" bozar ve size **saf matematiği** gösterir.

### 📑 Eğitim Müfredatı (İçindekiler)
1. **[Bölüm 1: Felsefe ve Vizyon](#-bölüm-1-felsefe-ve-vizyon)** — Neden bu aracı yaptık?
2. **[Bölüm 2: Sistem Mimarisi (Blueprint)](#-bölüm-2-sistem-mimarisi-blueprint)** — SwiftUI ve FastAPI'nin dansı.
3. **[Bölüm 3: Kriptografi Motoru (The Engine)](#-bölüm-3-kriptografi-motoru-the-engine)** — AES ve RSA nasıl çalışır?
4. **[Bölüm 4: Veri Kalıcılığı ve İstihbarat](#-bölüm-4-veri-kalıcılığı-ve-istihbarat)** — SQLite ve Loguru.
5. **[Bölüm 5: Saha Operasyonu (Kurulum)](#-bölüm-5-saha-operasyonu-kurulum)** — Kendi sunucunuzu başlatın.

---

## 🏛️ Bölüm 1: Felsefe ve Vizyon

**"Cam Kutu" (Glass-Box) Teorisi**
Çoğu güvenlik uygulaması bir "Kara Kutu"dur. Güvenli olduklarını iddia ederler, ancak kanıtlayamazsınız. Hashchat şeffaftır.
*   Bir anahtarın (Key) nasıl üretildiğini **görürsünüz**.
*   Şifreli verinin (Ciphertext) ağda nasıl aktığını **izlersiniz**.
*   Matematiğe dokunursunuz.

> **Hedef**: 2030 yılına kadar siber egemenlik bilincine sahip 1000 geliştirici yetiştirmek.

---

## 🏗️ Bölüm 2: Sistem Mimarisi (Blueprint)

Bu proje, endüstri standardı **Clean Architecture** prensipleriyle tasarlanmıştır.

### 📱 Frontend: iOS (Swift)
Kullanıcı arayüzü, Apple'ın en yeni teknolojileriyle donatılmıştır.

| Teknoloji | Görevi | Neden Seçtik? |
| :--- | :--- | :--- |
| **SwiftUI** | Deklaratif UI | Animasyonlar ve durum yönetimi (State Management) için rakipsiz. |
| **Combine** reaktif Framework | Veri Akışı | WebSocket'ten gelen canlı veri paketlerini saniyenin binde birinde işlemek için. |
| **Hardware CoreCrypto** | Güvenlik | Cihazın "Secure Enclave" işlemcisini kullanarak anahtarları donanım seviyesinde korur. |

### 🧠 Backend: Python (FastAPI)
Sunucu tarafı, asenkron ve yüksek performanslı bir dijital röledir.

*   **Protokol**: `wss://` (WebSocket Secure). HTTP gibi "iste-cevap al" değildir; sürekli açık bir hattır.
*   **Hız**: `AsyncIO` sayesinde tek bir çekirdekte binlerce eşzamanlı bağlantıyı yönetir.

---

## 🔐 Bölüm 3: Kriptografi Motoru (The Engine)

Burası işin mutfağıdır. Hashchat, hem modern hem de klasik şifreleme algoritmalarını içerir.

### ⚔️ Simetrik Savaş Sanatı: AES-128
**Advanced Encryption Standard (AES)**, ABD hükümetinin gizli verilerini korumak için kullandığı standarttır. Hashchat, bu algoritmayı eğitim amacıyla **MANUEL OLARAK** (sıfırdan) Swift dilinde yazmıştır.

#### AES Nasıl Çalışır? (Adım Adım)
Veri 128 bitlik (4x4 bayt) bloklar halinde işlenir. Her blok 4 aşamadan geçer:

1.  **SubBytes (Maskeleme)**: `S-Box` tablosu kullanılarak her bayt başka bir baytla değiştirilir.
    *   *Amaç*: İstatistsel ilişkiyi bozmak (Non-linearity).
2.  **ShiftRows (Karıştırma)**: Matris satırları sola doğru kaydırılır.
    *   *Amaç*: Veriyi blok genelinde dağıtmak (Diffusion).
3.  **MixColumns (Dönüştürme)**: Sütunlar, Galois Alanı ($GF(2^8)$) matematiği ile çarpılır.
    *   *Amaç*: Tek bir bit değişirse, tüm bloğun değişmesini sağlamak.
4.  **AddRoundKey (Kilitleme)**: O turun anahtarı ile XOR işlemi yapılır.

### 🛡️ Asimetrik Kalkan: RSA-2048
İki yabancının güvenli konuşabilmesi için "Açık Anahtar" (Public Key) kriptografisi kullanılır.

**Matematiksel Kanıt:**
RSA'nın güvenliği, iki çok büyük asal sayıyı çarpmanın kolay ($p \times q = n$), ancak çarpanlarına ayırmanın ($n \rightarrow p, q$) imkansız olması ilkesine dayanır.

*   **Hashchat Parametreleri**:
    *   Modulus ($n$): 2048 bit (617 ondalık basamak).
    *   Padding: OAEP (Optimal Asymmetric Encryption Padding) - SHA256 ile.

---

## 💾 Bölüm 4: Veri Kalıcılığı ve İstihbarat

Versiyon 2.0 ile Hashchat, profesyonel bir veri altyapısına kavuştu.

### Ironclad Persistence (SQLite + SQLAlchemy)
Eskiden sunucu kapanınca veriler uçardı. Artık **Kalıcı**.
*   **ORM Yapısı**: SQL sorguları yazmak yerine Python sınıfları (Class) kullanılır.
*   **Atomik İşlemler**: Bir veri ya tam yazılır ya hiç yazılmaz. Veri bütünlüğü garantidir.

### Elite Intelligence (Loguru)
Sistem sizinle konuşur. Konsol çıktısı bir "Matrix" ekranı gibidir:

```log
2025-12-27 14:05:22 | SUCCESS  | database:add_user - Ajan 'Neo' sisteme kaydedildi.
2025-12-27 14:05:23 | WARNING  | auth:verify_signature - Geçersiz imza denemesi! IP: 192.168.1.5
2025-12-27 14:05:24 | INFO     | crypto:exchange_keys - RSA Handshake tamamlandı.
```

---

## 🛠️ Bölüm 5: Saha Operasyonu (Kurulum)

Kendi komuta merkezinizi kurmaya hazır mısınız?

### 🖥️ Backend Kurulumu (Terminal)

```bash
# 1. Repoyu Klonlayın
git clone https://github.com/bahattinyunus/Hashchat.git

# 2. Sanal Ortama Geçiş Yapın
cd Hashchat/Backend
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# 3. Mühimmatı Yükleyin (Bağımlılıklar)
pip install -r requirements.txt

# 4. Ateşleyin! 🔥
uvicorn main:app --reload --host 0.0.0.0 --port 12345
```

### 📱 Frontend Kurulumu (Xcode)
1. `Hashchat/Frontend/Hashchat.xcodeproj` dosyasını açın.
2. Paketin yüklenmesini bekleyin.
3. Hedef cihazı seçin (iPhone 15).
4. **Cmd + R** ile operasyonu başlatın.

---

## 🤝 Katkıda Bulunma
Bu proje açık kaynaktır ve topluluğun gücüyle büyür.
*   Yeni bir şifreleme algoritması mı eklemek istiyorsun? (Örn: ChaCha20)
*   Arayüzü daha da mı geliştirmek istiyorsun?

Rehberlerimizi okuyun: [CONTRIBUTING.md](CONTRIBUTING.md) ve [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

### 📜 Lisans
Bu proje **Apache 2.0 Lisansı** ile korunmaktadır. Özgürce kullanın, değiştirin, öğrenin.

> **"Karanlıkta çalışırız, ışığa hizmet ederiz."**
<div align="center">
  <sub>Hashchat Geliştirici Takımı © 2025</sub>
</div>
