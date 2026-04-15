# 🛡️ Hybrid Honeypot System (SSH + Web)

## 📌 Project Overview

This project demonstrates a **multi-layer honeypot system** designed to detect and analyze cyber attacks.

It combines:

* 🔐 **SSH Honeypot** using Cowrie
* 🌐 **Web Honeypot** using Flask

The system captures attacker behavior such as login attempts, credentials, and commands in a controlled environment.

---

## 🏗️ Project Structure

honeypot-project/
├── cowrie/

├── web-honeypot/

│   ├── app.py

│   ├── requirements.txt

│   ├── templates/

│   │   └── login.html

│   └── web_logs.txt

├── screenshots/

└── README.md

---

## 🚀 Features

### 🌐 Web Honeypot

* Fake admin login page
* Captures:

  * Username
  * Password
  * IP address
* Logs stored in `web_logs.txt`

---

### 🔐 SSH Honeypot (Cowrie)

* Simulates a real Linux server
* Runs on port **2222**
* Captures:

  * Login attempts
  * Commands executed
* Provides fake terminal access

---

## 🛠️ Technologies Used

* Python
* Flask
* Cowrie Honeypot
* Linux (WSL Ubuntu)
* Git & GitHub

---

## ⚙️ Setup Instructions

### 🔹 1. Clone Repository

```
git clone https://github.com/your-username/honeypot-project.git
cd honeypot-project
```
# 🛡️ Cowrie Honeypot — Working Commands (WSL Ubuntu)

```bash
wsl
cd ~
git clone https://github.com/cowrie/cowrie.git
cd cowrie

python3 -m venv cowrie-env
source cowrie-env/bin/activate

python3 -m pip install --upgrade pip
pip install -r requirements.txt

pip install -e .
# If blocked:
pip install -e . --break-system-packages

cowrie start

# If cowrie command not found:
twistd -n cowrie

# Test SSH honeypot (new terminal)
ssh root@localhost -p 2222

# View logs
tail -f ~/cowrie/var/log/cowrie/cowrie.log

# Stop Cowrie
CTRL + C
kill -9 $(cat var/run/cowrie.pid)
```
---

### 🔹 2. Setup and Run Web Honeypot

```
cd web-honeypot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

👉 Open in browser:
http://localhost:5000

---

### 🔹 3. Setup and Run SSH Honeypot (Cowrie)

```
cd cowrie
source cowrie-env/bin/activate
cowrie start
```

---

## 🧪 Attack Simulation

### 🌐 Web Attack

* Enter any username and password in the login page
* Credentials will be captured and stored

---

### 🔐 SSH Attack

```
ssh root@localhost -p 2222
```

* Enter any password
* Fake shell will be displayed
* Commands will be logged

---

## 📊 Logs

### Web Logs

```
web-honeypot/web_logs.txt
```

### SSH Logs

```
cowrie/var/log/cowrie/cowrie.log
```

---

## 📸 Screenshots

**🌐 Web Honeypot using Flask**
*LOGIN PAGE
<img width="1898" height="1010" alt="Screenshot 2026-04-15 172821" src="https://github.com/user-attachments/assets/038db5ef-39b1-4089-bfd8-b2aca5efdeab" />

<img width="1202" height="607" alt="Screenshot 2026-04-15 172833" src="https://github.com/user-attachments/assets/a005faf0-ac9b-4384-840c-0562ad1c1139" />

*WEB LOGS
<img width="1691" height="907" alt="Screenshot 2026-04-15 173136" src="https://github.com/user-attachments/assets/55884183-db08-4899-8cc4-30810131a225" />

**SSH Honeypot using Cowrie**
Cowrie Logs
  
<img width="1920" height="1080" alt="Screenshot 2026-04-15 105415" src="https://github.com/user-attachments/assets/47adb458-4657-4d0f-81ad-1862a237f1eb" />

<img width="1920" height="1080" alt="Screenshot 2026-04-15 105334" src="https://github.com/user-attachments/assets/be6faa45-e3c5-4f72-b560-58c2f8156b5d" />



---

## 🎯 Learning Outcomes

* Understanding honeypot systems
* Capturing attacker behavior
* Working with real cybersecurity tools
* Implementing multi-layer security

---

## ⚠️ Disclaimer

This project is developed for **educational purposes only**.
Do not deploy publicly without proper security configurations.

---

## 🙌 Author

**Dhanalakshmi M**
