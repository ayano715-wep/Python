import os
import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QInputDialog

class PlanApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.is_saved = True  # حالة الحفظ

    def initUI(self):
        # إعداد الواجهة
        self.setWindowTitle("Plan Manager")
        self.setGeometry(200, 100, 700, 500)

        self.layout = QVBoxLayout()

        self.label = QLabel("Enter your plan:")
        self.layout.addWidget(self.label)

        self.plan_input = QLineEdit(self)
        self.plan_input.setFixedSize(700, 40) 
        self.layout.addWidget(self.plan_input)

        # تكبير الأزرار
        self.add_button = QPushButton("Add Plan", self)
        self.add_button.setFixedSize(250, 40) 
        self.add_button.clicked.connect(self.add_plan)
        self.layout.addWidget(self.add_button)

        self.edit_button = QPushButton("Edit Last Plan", self)
        self.edit_button.setFixedSize(250, 40) 
        self.edit_button.clicked.connect(self.edit_plan)
        self.layout.addWidget(self.edit_button)

        self.save_button = QPushButton("Save Plans", self)
        self.save_button.setFixedSize(250, 40)  
        self.save_button.clicked.connect(self.save_plans)
        self.layout.addWidget(self.save_button)

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setFixedSize(250, 40) 
        self.exit_button.clicked.connect(self.confirm_exit)
        self.layout.addWidget(self.exit_button)

        self.plan_list = QTextEdit(self)
        self.plan_list.setReadOnly(True)
        self.layout.addWidget(self.plan_list)
        
        self.setLayout(self.layout)

        self.plans = []
        self.num = 0  # عدد الخطط المدخلة

    def add_plan(self):
        plan_text = self.plan_input.text()
        if plan_text:
            self.plans.append(plan_text)
            self.num += 1
            self.plan_list.append(f"{self.num} - {plan_text}")
            self.plan_input.clear()
            self.is_saved = False  # تغيير الحالة إلى غير محفوظ

    def edit_plan(self):
        if not self.plans:
            QMessageBox.warning(self, "Warning", "No plans to edit.")
            return

        edit_index, ok = QInputDialog.getInt(self, "Edit Plan", f"Enter the number of the plan to change (1-{len(self.plans)}):")
        
        if ok and 1 <= edit_index <= len(self.plans):
            new_plan_text, ok = QInputDialog.getText(self, "Change Plan", "Enter new plan text:")
            if ok:
                self.plans[edit_index - 1] = new_plan_text  # تعديل الفهرس لأن المستخدم يبدأ العد من 1
                self.update_plan_list()
                self.is_saved = False  # تغيير الحالة إلى غير محفوظ
        else:
            QMessageBox.warning(self, "Error", "Invalid plan number.")

    def update_plan_list(self):
        self.plan_list.clear()
        for idx, plan in enumerate(self.plans, start=1):
            self.plan_list.append(f"{idx} - {plan}")

    def save_plans(self):
        if not self.plans:
            return

        folder_name = 'plans'
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        file_name = f"plan_{date_str}.txt"
        file_path = os.path.join(folder_name, file_name)

        with open(file_path, 'w') as file:
            file.write(f"Plans on {date_str}:\n\n")
            for idx, plan in enumerate(self.plans, start=1):
                file.write(f"{idx} - {plan}\n\n")

        QMessageBox.information(self, "Success", f"Plans saved to {file_path}")
        self.is_saved = True  # تغيير الحالة إلى محفوظ

    def confirm_exit(self):
        if self.is_saved:
            self.close()  # أغلق التطبيق إذا كانت الحالة محفوظة
            return

        reply = QMessageBox.question(self, "Exit", "Do you want to save your plans before exiting?",
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        if reply == QMessageBox.Yes:
            self.save_plans()
            self.close()  # أغلق التطبيق
        elif reply == QMessageBox.No:
            self.close()  # أغلق التطبيق
        # إذا اختار المستخدم Cancel، فلا يحدث شيء

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlanApp()
    window.show()
    sys.exit(app.exec_())
