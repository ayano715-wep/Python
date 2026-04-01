# 🎓 Student Manager CLI (Python)

## 📌 Overview

**English:**
Student Manager is a simple command-line application written in Python that allows users to manage student records. It supports viewing, editing, and adding student information such as grades and pass/fail status.

**العربية:**
برنامج **Student Manager** هو تطبيق يعمل عبر سطر الأوامر بلغة بايثون، يتيح إدارة بيانات الطلاب مثل الدرجات وحالة النجاح أو الرسوب، مع إمكانية العرض والتعديل والإضافة.

---

## ⚙️ Features | الميزات

* 📖 View individual student information
* 📚 Display all students
* 📝 Modify student grades and status
* ➕ Add new students
* 🎨 Colored terminal output باستخدام `termcolor`

---

## 🧪 Usage | طريقة الاستخدام

### English:

1. Run the script
2. Choose an option from the menu
3. Enter student name when required
4. Perform actions like edit, add, or view

### العربية:

1. شغّل البرنامج
2. اختر رقم من القائمة
3. أدخل اسم الطالب عند الطلب
4. نفّذ العملية (عرض، تعديل، إضافة)

---

## 📁 Data Structure | بنية البيانات

```python
info = {
    "ahmed": {"degree": 50, "success": "Seccssful"},
    "ali": {"degree": 66, "success": "Failed"}
}
```

---

## 🚀 Installation & Run | التشغيل

### 1. Install dependency:

```bash
pip install termcolor
```

### 2. Run:

```bash
python main.py
```

---

## 📌 Menu Options | قائمة الأوامر

| Option | Description         |
| ------ | ------------------- |
| 1      | Show student info   |
| 2      | Show all students   |
| 3      | Change student data |
| 4      | Add student         |
| 5      | Exit                |

---

## 📄 License

MIT License

---

## 👨‍💻 Author

Ayano

