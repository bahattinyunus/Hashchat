# 🦅 Hashchat: Elit Kriptografik Komuta Merkezi

> **"Mahremiyet bir ayrıcalık değil, matematiksel bir kesinliktir."** - *Cypherpunk Manifestosu*

<div align="center">
  <img src="assets/banner.png" alt="Hashchat Elite Banner" width="100%" />
  <br/>
  <br/>
  <a href="https://github.com/bahattinyunus/Hashchat/blob/main/LICENSE"><img src="https://img.shields.io/badge/Lisans-Apache%202.0-blue.svg" alt="License"></a>
  <a href="https://github.com/bahattinyunus/Hashchat/actions"><img src="https://img.shields.io/github/actions/workflow/status/bahattinyunus/Hashchat/ci.yml?branch=main" alt="CI Status"></a>
  <a href="https://swift.org"><img src="https://img.shields.io/badge/Swift-5.9-orange.svg" alt="Swift"></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.11-yellow.svg" alt="Python"></a>
  <a href="https://developer.apple.com/documentation/security"><img src="https://img.shields.io/badge/Security-CommonCrypto-green.svg" alt="Security"></a>
  <br/>
  <br/>
</div>

## 📚 Hashchat Ansiklopedisi
Bu doküman hem bir kullanım kılavuzu hem de ileri seviye bir kriptografi ders kitabıdır. Projenin amacı, ticari uygulamaların arkasına saklanan güvenlik mekanizmalarını şeffaf bir şekilde öğretmektir.

### İçindekiler
1. [Giriş ve Felsefe](#-giriş-ve-felsefe)
2. [Hashchat Nedir?](#-hashchat-nedir)
3. [🛠️ Teknoloji Yığını (Derinlemesine Analiz)](#-teknoloji-yığını-derinlemesine-analiz)
    - [Frontend Mimarisi (Swift/iOS)](#frontend-mimarisi-swiftios)
    - [Backend Mimarisi (Python/FastAPI)](#backend-mimarisi-pythonfastapi)
4. [🔐 Kriptografi Motoru](#-kriptografi-motoru)
    - [Simetrik Şifreleme (AES & DES - Matematiksel Temeller)](#simetrik-şifreleme-aes--des)
    - [Asimetrik Şifreleme (RSA - Anahtar Teorisi)](#asimetrik-şifreleme-rsa)
5. [🏗️ Mimari 2.0: Sistem Tasarımı](#-mimari-20-sistem-tasarımı)
    - [Ironclad Persistence (Kalıcı Hafıza)](#ironclad-persistence-sqlite)
    - [Elite Intelligence (İstihbarat ve Loglama)](#elite-intelligence-loguru)
6. [Kurulum ve Operasyon](#-kurulum-ve-operasyon)
7. [Katkıda Bulunma](#-katkıda-bulunma)

---

## 🚀 Giriş ve Felsefe

**Hashchat**, modern internetin güvenliğini sağlayan matematiksel motorları görselleştirmek ve denemek için tasarlanmış bir **Dijital Laboratuvardır**.

Çoğu mesajlaşma uygulaması (WhatsApp, Signal) güvenlidir, ancak "kara kutu" gibidirler. Nasıl çalıştıklarını göremezsiniz. Hashchat ise "cam kutu" (glass-box) yaklaşımını benimser. Şifreleme anahtarlarının nasıl üretildiğini, AES baytlarının nasıl karıştırıldığını ve bir mesajın ağ üzerinde nasıl seyahat ettiğini size gösterir.

## 📱 Hashchat Nedir?

Hashchat, güvenli bir WebSocket rölesi üzerinden iletişim kuran çift katmanlı bir sistemdir.
- **Uçtan Uca Şifreleme (E2EE)**: Mesajlar cihazınızdan çıkmadan önce şifrelenir.
- **Sıfır Bilgi (Zero-Knowledge)**: Sunucu, mesajların içeriğini asla bilemez. Sadece şifreli veri paketlerini (ciphertext) taşır.
- **Güvenli Taşıma**: Tüm trafik WSS (WebSocket Secure) protokolü ile korunur.

---

## 🛠️ Teknoloji Yığını (Derinlemesine Analiz)

### Frontend Mimarisi (Swift/iOS)
iOS uygulaması, **Clean Architecture** prensipleri ve **MVVM** (Model-View-ViewModel) deseni üzerine inşa edilmiştir.

#### 1. SwiftUI & Combine Framework
Arayüz, durum tabanlı (state-driven) bir yapı olan **SwiftUI** ile kodlanmıştır.
- **View (Görünüm)**: `ChatView` gibi yapılar, `ChatViewModel` üzerindeki değişiklikleri dinler.
- **Combine**: Asenkron veri akışlarını yönetmek için kullanılır. WebSocket üzerinden bir mesaj geldiğinde, bu veri bir `PassthroughSubject` boru hattından (pipeline) geçer ve saniyenin binde birinde ekrana yansır.

#### 2. CoreCrypto & Security Framework
Standart şifreleme işlemleri için Apple'ın C tabanlı `CommonCrypto` kütüphanesi ve `Security.framework` kullanılır.
- **Keychain (Anahtarlık)**: RSA Özel Anahtarı (Private Key) burada saklanır. Bu, donanım tabanlı bir kasadır. Telefon "jailbreak" yapılsa bile, bu anahtarların donanım seviyesinden çıkarılması matematiksel olarak imkansıza yakındır.

### Backend Mimarisi (Python/FastAPI)
Sunucu tarafı, yüksek performanslı bir mesaj rölesi olarak çalışır.

#### 1. FastAPI (ASGI)
- **AsyncIO**: Eski nesil Flask (WSGI) yerine, `Starlette` ve `Pydantic` üzerine kurulu FastAPI kullanılmıştır. Bu yapı, Python'un `async/await` sözdizimini kullanarak tek bir işlemci çekirdeğinde binlerce eşzamanlı WebSocket bağlantısını yönetebilir.
- **WebSocketEndpoint**: Kalıcı, çift yönlü bir iletişim kanalı sağlar.

#### 2. SQLAlchemy 2.0 (ORM)
- **Modern Veritabanı Yönetimi**: `DeclarativeBase` sistemi kullanılarak modern Python tip güvenliği sağlanmıştır.
- **Oturum Yönetimi (Session Scoping)**: Her istek (request) için izole bir veritabanı oturumu açılır ve işlem bitince otomatik kapatılır. Bu, "connection leak" (bağlantı sızıntısı) problemlerini %100 önler.

#### 3. Loguru (İstihbarat)
- **Felsefe**: Loglar okunabilir olmalıdır. Sistem, her olayı (kayıt, mesaj iletimi, hata) renk kodlu ve yapılandırılmış formatta kaydeder. Dosyalar her 500MB'da bir otomatik olarak arşivlenir.

---

## 🔐 Kriptografi Motoru

### Simetrik Şifreleme (AES & DES)

#### AES (Advanved Encryption Standard)
Hashchat, AES-128 algoritmasının **Saf Swift (Pure Swift)** implementasyonunu içerir. Donanım hızlandırmalı AES'ten 1000 kat daha yavaştır, ancak **eğitim** için mükemmeldir.

**AES Döngüsünün 4 Aşaması:**
1.  **SubBytes (Bayt Değiştirme)**: Her bayt, S-Box adı verilen özel bir tablo kullanılarak başka bir baytla değiştirilir. Bu, kriptografide **Konfüzyon (Karışıklık)** sağlar.
2.  **ShiftRows (Satır Kaydırma)**: Matrisin son üç satırı belirli ofsetlerle kaydırılır. Bu, **Difüzyon (Yayılma)** sağlar.
3.  **MixColumns (Sütun Karıştırma)**: Sütunlar, Galois Alanı (Galois Field) matematiği ile birbirine karıştırılır.
4.  **AddRoundKey (Anahtar Ekleme)**: O anki turun anahtarı, mevcut durum matrisi ile XOR işlemine sokulur.

#### DES (Data Encryption Standard)
AES'in atasıdır. Tarihsel önemini anlamak için Feistel ağ yapısı manuel olarak kodlanmıştır.
- **Blok Boyutu**: 64 bit.
- **Anahtar Boyutu**: 56 bit (Modern standartlara göre güvensizdir, kaba kuvvet saldırısı ile kırılabilir).

### Asimetrik Şifreleme (RSA)

#### RSA (Rivest–Shamir–Adleman)
E2EE (Uçtan Uca Şifreleme) omurgamızdır. Anahtar paylaşım problemini çözer.
- **Anahtar Üretimi**: İki devasa asal sayı ($p$ ve $q$) seçilir ve modül $n = p \times q$ hesaplanır. Hashchat'te bu $n$ sayısı 2048 bittir (yaklaşık 617 ondalık basamak).
- **Şifreleme**: $c = m^e \pmod n$.
- **Deşifreleme**: $m = c^d \pmod n$.

> **Biliyor muydunuz?**: RSA-2048'i kırmak için evrendeki atom sayısından daha fazla işlem gücü ve zaman gerekir.

---

## 🏗️ Mimari 2.0: Sistem Tasarımı

Versiyon 2.0 ile Hashchat, bir prototipten profesyonel bir platforma evrildi.

### Ironclad Persistence (SQLite) 💾
Kullanıcı kimlikleri artık kalıcıdır.
- **Teknoloji**: **SQLAlchemy** ORM + **SQLite**.
- **Fayda**: Sunucu yeniden başlatılsa bile kullanıcı hesapları ve açık anahtarlar (Public Keys) silinmez. `hashchat.db` dosyası tek gerçeklik kaynağıdır (Single Source of Truth).
- **Şema**:
    ```sql
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username VARCHAR NOT NULL UNIQUE, -- Benzersiz kullanıcı adı
        public_key VARCHAR NOT NULL       -- RSA Açık Anahtarı
    );
    ```

### Elite Intelligence (Loguru) 🧠
Sistem sizinle konuşur. Tipik bir log akışı şöyle görünür:
```
2025-12-27 14:05:22 | INFO     | user_service:register:12 - Kayıt işlemi başlatıldı: neo
2025-12-27 14:05:22 | SUCCESS  | database:add_user:28 - Kullanıcı veritabanına eklendi: neo
2025-12-27 14:05:23 | DEBUG    | websocket:connect:45 - Bağlantı kabul edildi: 127.0.0.1:56432
```

---

## 🛠️ Kurulum ve Operasyon

### Backend Kurulumu (Sinir Sistemi)
Operasyonun beyni. Python 3.11+ gerektirir.

```bash
# 1. Repoyu Klonlayın
git clone https://github.com/bahattinyunus/Hashchat.git

# 2. Sanal Ortam Oluşturun (Önerilen)
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Bağımlılıkları Yükleyin
pip install -r Hashchat/Backend/requirements.txt

# 4. Elit Sunucuyu Başlatın
cd Hashchat/Backend
uvicorn main:app --reload --host 0.0.0.0 --port 12345
```
*Veritabanının otomatik olarak oluşturulduğunu (`hashchat.db`) ve logların akmaya başladığını göreceksiniz.*

### Frontend Kurulumu (Arayüz)
Operasyonun yüzü. macOS ve Xcode gerektirir.

1. `Hashchat/Frontend/Hashchat.xcodeproj` dosyasını Xcode ile açın.
2. Paket bağımlılıklarının (Swift Package Manager) yüklenmesini bekleyin.
3. Simülatör seçin (Örn: iPhone 15 Pro).
4. **Cmd + R** tuşuna basarak derleyin ve çalıştırın.

---

## 🤝 Katkıda Bulunma

Bir miras inşa ediyoruz. Bize katılın.
- Hataları "Issues" sekmesinden bildirin.
- Yeni özellikler için "Pull Request" gönderin (Örneğin: ChaCha20 algoritması eklemek ister misiniz?).
- Katkı rehberi için [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını okuyun.

---

### 📜 Lisans
Apache 2.0 - Açık Kaynak ve Sonsuza Kadar Özgür.

> **"Karanlıktan korkmuyoruz. Biz bizzat ışığız."** - Hashchat Takımı
