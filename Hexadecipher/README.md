# 🔐 Hex Encoder & Decoder (Python)

## 📌 Overview | نظرة عامة

**English:**
This project is a simple Python implementation of a string encoder and decoder using **hexadecimal representation**. It converts strings into hex values and restores them back to their original form.

**العربية:**
هذا المشروع عبارة عن تطبيق بسيط بلغة بايثون يقوم بتشفير النصوص إلى **النظام الست عشري (Hex)** ثم فك التشفير وإرجاعها إلى شكلها الأصلي.

---

## ⚙️ Features | الميزات

* 🔁 Encode strings to hexadecimal
* 🔓 Decode hexadecimal back to original text
* 🧠 Uses built-in Python functions (`ord`, `chr`, `hex`)
* 📦 Works on list of strings

---

## 🧪 Example | مثال

### Input:

```python
name = ["ali", "ayaz", "ahmed"]
```

### Output:

```bash
Encoded:
[['0x61', '0x6c', '0x69'], ...]

Decoded:
[['ali'], ['ayaz'], ['ahmed']]
```

---

## 🧩 Code Structure | بنية الكود

### 1. Encoding Function | دالة التشفير

```python
def string(x):
```

**English:**

* Converts each character into ASCII using `ord()`
* Converts ASCII to hex using `hex()`
* Stores results in a list

**العربية:**

* تحويل كل حرف إلى ASCII باستخدام `ord()`
* تحويله إلى Hex باستخدام `hex()`
* تخزين النتائج داخل مصفوفة

---

### 2. Decoding Function | دالة فك التشفير

```python
def chrekter(y):
```

**English:**

* Converts hex back to integer
* Uses `chr()` to restore characters
* Joins characters into full string

**العربية:**

* تحويل Hex إلى أرقام
* استخدام `chr()` لإرجاع الحروف
* دمج الحروف لتكوين النص الأصلي

---

## 🚀 How to Run | طريقة التشغيل

```bash
python he_x2.py
```

---

## 📄 License | الرخصة

MIT License

---

## 👨‍💻 Author | المطور

**Ayano**
