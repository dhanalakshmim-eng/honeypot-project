# 🛡️ Hybrid Honeypot System (SSH + Web)

## 📌 Project Overview

This project demonstrates a **multi-layer honeypot system** designed to detect and analyze cyber attacks.

It combines:

* 🔐 **SSH Honeypot** using Cowrie
* 🌐 **Web Honeypot** using Flask

The system captures attacker behavior such as login attempts, credentials, and commands.

---

## 🚀 Features

### 🔹 SSH Honeypot (Cowrie)

* Simulates a fake Linux server
* Captures:

  * Login attempts
  * Commands executed
  * Attacker interaction

### 🔹 Web Honeypot (Flask)

* Fake admin login page
* Captures:

  * Username & Password
  * IP Address
* Stores logs in a file

---

## 🧠 Architecture

Attacker
↓
Web Login Page (Flask) → Logs credentials
↓
SSH Honeypot (Cowrie) → Logs commands

---

## 🛠️ Technologies Used

* Python 🐍
* Flask 🌐
* Cowrie Honeypot 🛡️
* Linux (WSL Ubuntu)

---

## ⚙️ Setup Instructions

### 🔹 1. Clone Repository

```
git clone https://github.com/your-username/honeypot-project.git
cd honeypot-project
```

---

### 🔹 2. Setup Web Honeypot

```
cd web-honeypot
python3 -m venv venv
source venv/bin/activate
pip install flask
python3 app.py
```

👉 Open in browser:

```
http://localhost:5000
```

---

### 🔹 3. Setup Cowrie Honeypot

```
cd cowrie
python3 -m venv cowrie-env
source cowrie-env/bin/activate
pip install -r requirements.txt
pip install -e .
cowrie start
```

---

### 🔹 4. Simulate Attack

#### 🌐 Web Attack:

Enter credentials in login page

#### 🔐 SSH Attack:

```
ssh root@localhost -p 2222
```

---

## 📊 Logs

### Web Logs:

```
web-hoeypot/web_logs.txt
```

### SSH Logs:

```
cowrie/var/log/cowrie/cowrie.log
```

---

## 📸 Screenshots

*Add screenshots here for better understanding*
<img width="1920" height="1080" alt="Screenshot 2026-04-15 105415" src="https://github.com/user-attachments/assets/47adb458-4657-4d0f-81ad-1862a237f1eb" />
<img width="1920" height="1080" alt="Screenshot 2026-04-15 105334" src="https://github.com/user-attachments/assets/be6faa45-e3c5-4f72-b560-58c2f8156b5d" />



---

## 🎯 Learning Outcomes

* Understanding honeypot concepts
* Capturing attacker behavior
* Working with real cybersecurity tools
* Building secure and deceptive systems

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
Do not deploy publicly without proper security configurations.

---

## 🙌 Author

Dhana Lakshmi M
