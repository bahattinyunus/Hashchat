# 🦅 Hashchat: The Elite Cryptographic Command Center

> **"Privacy is not a privilege, it is a mathematical certainty."** - *Cypherpunk Manifesto*

<div align="center">
  <img src="assets/banner.png" alt="Hashchat Elite Banner" width="100%" />
  <br/>
  <br/>
  <a href="https://github.com/bahattinyunus/Hashchat/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License"></a>
  <a href="https://github.com/bahattinyunus/Hashchat/actions"><img src="https://img.shields.io/github/actions/workflow/status/bahattinyunus/Hashchat/ci.yml?branch=main" alt="CI Status"></a>
  <a href="https://swift.org"><img src="https://img.shields.io/badge/Swift-5.9-orange.svg" alt="Swift"></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.11-yellow.svg" alt="Python"></a>
  <a href="https://developer.apple.com/documentation/security"><img src="https://img.shields.io/badge/Security-CommonCrypto-green.svg" alt="Security"></a>
  <br/>
  <br/>
</div>

## 📚 Encyclopedia of Hashchat
This document serves as both a user manual and a technical textbook.

1. [Introduction](#-introduction)
2. [What is Hashchat?](#-what-is-hashchat)
3. [🛠️ The Technology Stack](#-the-technology-stack-deep-dive)
    - [Frontend Anatomy (Swift/iOS)](#frontend-anatomy-swiftios)
    - [Backend Anatomy (Python/FastAPI)](#backend-anatomy-pythonfastapi)
4. [🔐 The Cryptographic Engine](#-the-cryptographic-engine)
    - [Symmetric Ciphers (AES & DES)]( #symmetric-ciphers-the-math)
    - [Asymmetric Ciphers (RSA)]( #asymmetric-ciphers-the-keys)
5. [🏗️ Architecture 2.0](#-architecture-20-system-design)
    - [Ironclad Persistence](#ironclad-persistence)
    - [Elite Intelligence](#elite-intelligence)
6. [Installation](#-installation--deployment)
7. [Contributing](#-contributing)

---

## 🚀 Introduction

**Hashchat** is an educational open-source project designed to demystify the complex world of cryptography. Unlike commercial apps that hide their security mechanisms, Hashchat exposes them. It is a "glass-box" implementation of a secure messenger, allowing students and developers to inspect the gears of privacy.

## 📱 What is Hashchat?

Hashchat connects users via a secure WebSocket relay.
- **Payloads** are encrypted on the device (Edge Encryption).
- **Keys** never leave the device (Zero-Knowledge Architecture).
- **Transport** is secured via WSS (WebSocket Secure).

---

## 🛠️ The Technology Stack (Deep Dive)

### Frontend Anatomy (Swift/iOS)
The iOS app is built on the principles of **Clean Architecture** and **MVVM** (Model-View-ViewModel).

#### 1. SwiftUI & Combine
We use **SwiftUI** for a declarative UI that builds itself based on state.
- **View**: Structs like `ChatView` observe the `ChatViewModel`.
- **ViewModel**: `ObservableObject` classes that hold application state.
- **Combine**: Used for handling asynchronous data streams. When a WebSocket message arrives, it flows through a `PassthroughSubject` pipeline, triggering UI updates instantly.

#### 2. CoreCrypto & Security Framework
For standard implementations, we bridge to Apple's `CommonCrypto` (C-library) and `Security.framework`.
- **Keychain**: Used to store the RSA Private Key. This is a hardware-backed vault. Even if the phone is jailbroken, extracting these keys is mathematically infeasible.

### Backend Anatomy (Python/FastAPI)
The server is a high-performance relay station.

#### 1. FastAPI (ASGI)
- **AsyncIO**: Unlike Flask (WSGI), FastAPI is built on Starlette and Pydantic. It handles thousands of concurrent WebSocket connections using Python's `async/await` syntax.
- **WebSocketEndpoint**: Defines a persistent bidirectional channel.

#### 2. SQLAlchemy 2.0 (ORM)
- **Declaration**: We use the new `DeclarativeBase` system.
- **Session Management**: Each request gets a scoped session that is automatically closed after usage, preventing connection leaks.

#### 3. Loguru (Observability)
- **Philosophy**: Logging should be fun. We use a structured sink that rotates files automatically (500MB limit) and color-codes output for rapid visual debugging.

---

## 🔐 The Cryptographic Engine

### Symmetric Ciphers (The Math)

#### AES (Advanced Encryption Standard)
Hashchat contains a **Pure Swift** implementation of AES-128. This is 1000x slower than hardware AES but perfect for learning.

**The 4 Stages of an AES Round:**
1.  **SubBytes**: A non-linear substitution step where each byte is replaced with another according to a lookup table (S-Box). This provides **Confusion**.
2.  **ShiftRows**: A transposition step where the last three rows of the state are shifted cyclically. This provides **Diffusion**.
3.  **MixColumns**: A mixing operation which operates on the columns of the state, combining the four bytes in each column.
4.  **AddRoundKey**: The subkey is combined with the state.

#### DES (Data Encryption Standard)
The ancestor of AES. We implemented the Feistel network manually.
- **Block Size**: 64 bits.
- **Key Size**: 56 bits (unsafe by modern standards, but historically significant).

### Asymmetric Ciphers (The Keys)

#### RSA (Rivest–Shamir–Adleman)
The backbone of our E2EE (End-to-End Encryption).
- **Key Generation**: We generate a 2048-bit modulus $n = p \times q$.
- **Encryption**: $c = m^e \pmod n$.
- **Decryption**: $m = c^d \pmod n$.

> **Fun Fact**: Breaking RSA-2048 requires factoring a number with 617 decimal digits.

---

## 🏗️ Architecture 2.0: System Design

With Version 2.0, Hashchat evolved from a prototype into a robust platform.

### Ironclad Persistence
We replaced the mock dictionary storage with a **SQLite** database.
- **Why SQLite?**: Serverless, zero-configuration, and transactional.
- **Schema**:
    ```sql
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username VARCHAR NOT NULL UNIQUE,
        public_key VARCHAR NOT NULL
    );
    ```

### Elite Intelligence
The system now speaks to you. A typical log stream looks like this:
```
2025-12-27 14:05:22 | INFO     | user_service:register:12 - Attempting registration for: neo
2025-12-27 14:05:22 | SUCCESS  | database:add_user:28 - User added: neo
2025-12-27 14:05:23 | DEBUG    | websocket:connect:45 - Connection accepted: 127.0.0.1:56432
```

---

## 🛠️ Installation & Deployment

### Backend Setup
```bash
# 1. Clone
git clone https://github.com/bahattinyunus/Hashchat.git

# 2. Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate

# 3. Install
pip install -r Hashchat/Backend/requirements.txt

# 4. Run
cd Hashchat/Backend
uvicorn main:app --reload --host 0.0.0.0 --port 12345
```

### Frontend Setup (macOS)
1. Open `Hashchat/Frontend/Hashchat.xcodeproj`.
2. Trust the package dependencies (SPM).
3. Build & Run (Cmd+R).

---

## 🤝 Contributing

We are building a legacy. Join us.
- Report bugs via Issues.
- Submit PRs for new features.
- Read [CONTRIBUTING.md](CONTRIBUTING.md) for style guides.

---

### 📜 License
Apache 2.0 - Open Source and Free Forever.

> **"We do not fear the dark. We are the light."**
