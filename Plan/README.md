# 📝 Plan Manager (PyQt5)

## 📌 Overview

**English:**
Plan Manager is a desktop application built with **PyQt5** that allows users to manage daily plans through a simple graphical interface. Users can add, edit, and save plans locally.

**العربية:**
برنامج **Plan Manager** هو تطبيق سطح مكتب مبني باستخدام PyQt5 يتيح إدارة الخطط اليومية عبر واجهة رسومية بسيطة، مع إمكانية الإضافة والتعديل والحفظ.

---

## ⚙️ Features | الميزات

* ➕ Add new plans | إضافة خطط جديدة
* ✏️ Edit existing plans | تعديل الخطط
* 💾 Save plans to local files | حفظ الخطط محليًا
* ⚠️ Exit confirmation if not saved | تنبيه قبل الخروج بدون حفظ
* 📅 Automatic file naming by date | تسمية الملفات حسب التاريخ

---

## 🧪 Usage | طريقة الاستخدام

### English:

1. Enter your plan in the input field
2. Click **Add Plan**
3. Plans will appear in the list
4. Use **Edit Last Plan** to modify a plan
5. Click **Save Plans** to store data

### العربية:

1. أدخل الخطة في الحقل
2. اضغط **Add Plan**
3. ستظهر الخطة في القائمة
4. استخدم **Edit Last Plan** للتعديل
5. اضغط **Save Plans** للحفظ

---

## 📁 Project Structure | بنية المشروع

```bash
project/
│
├── plan.py        # Main application file
└── plans/         # Folder for saved plans (auto-created)
```

---

## 🚀 Installation & Run | التثبيت والتشغيل

### 1. Install dependencies:

```bash
pip install PyQt5
```

### 2. Run the app:

```bash
python plan.py
```

---

## 💾 Output Example | مثال الحفظ

File path:

```bash
plans/plan_YYYY-MM-DD.txt
```

Example content:

```
Plans on 2026-04-02:
---

## 📄 License

MIT License

---

## 👨‍💻 Author

Ayano
