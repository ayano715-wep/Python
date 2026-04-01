# 🔍 Python Port Scanner

## 📌 Overview

**English:**
This project is a simple TCP port scanner built using Python. It scans a target IP address and detects open ports within a specified range.

**العربية:**
هذا المشروع عبارة عن أداة بسيطة لفحص المنافذ (Port Scanner) باستخدام بايثون، تقوم بفحص عنوان IP واكتشاف المنافذ المفتوحة ضمن نطاق محدد.

---

## ⚙️ Features | الميزات

* 🔎 Scan TCP ports
* 🌐 Accept user input for target IP
* 📡 Detect open ports
* ⚡ Simple and lightweight implementation

---

## 🧪 How It Works | آلية العمل

### English:

* The script iterates over a range of ports
* Attempts to connect using TCP socket
* If connection succeeds → port is open
* Stores results in a list

### العربية:

* يقوم البرنامج بالمرور على مجموعة من المنافذ
* يحاول الاتصال بكل منفذ باستخدام TCP
* إذا نجح الاتصال → المنفذ مفتوح
* يتم حفظ النتائج في قائمة

---

## 🚀 Usage | طريقة التشغيل

```bash
python main.py
```

ثم أدخل:

```bash
Enter the ip for scan port : 192.168.1.1
```

---

## 📌 Example Output

```bash
Open ports on 192.168.1.1: [22, 80, 443]
```
---

## 📄 License

MIT License

---

## 👨‍💻 Author

Ayano
