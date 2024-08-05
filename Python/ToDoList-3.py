#1.A To-Do List application is a useful project that helps users manage
#and organize their tasks efficiently. This project aims to create a
#command-line or GUI-based application using Python, allowing
#users to create, update, and track their to-do lists
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QHBoxLayout, QMessageBox
import sys

class TodoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To-Do List Application")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.task_entry = QLineEdit()
        self.task_entry.setPlaceholderText("Enter a task")
        self.layout.addWidget(self.task_entry)

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.layout.addWidget(self.add_button)

        self.tasks_list = QListWidget()
        self.layout.addWidget(self.tasks_list)

        self.button_layout = QHBoxLayout()
        
        self.update_button = QPushButton("Update Task")
        self.update_button.clicked.connect(self.update_task)
        self.button_layout.addWidget(self.update_button)

        self.delete_button = QPushButton("Delete Task")
        self.delete_button.clicked.connect(self.delete_task)
        self.button_layout.addWidget(self.delete_button)

        self.layout.addLayout(self.button_layout)
        self.central_widget.setLayout(self.layout)

    def add_task(self):
        task = self.task_entry.text()
        if task:
            self.tasks_list.addItem(task)
            self.task_entry.clear()
        else:
            self.show_message("Warning", "Task cannot be empty")

    def update_task(self):
        selected_items = self.tasks_list.selectedItems()
        if selected_items:
            item = selected_items[0]
            new_task, ok = QInputDialog.getText(self, "Update Task", "New task description:", text=item.text())
            if ok and new_task:
                item.setText(new_task)
        else:
            self.show_message("Warning", "No task selected")

    def delete_task(self):
        selected_items = self.tasks_list.selectedItems()
        if selected_items:
            item = selected_items[0]
            self.tasks_list.takeItem(self.tasks_list.row(item))
        else:
            self.show_message("Warning", "No task selected")

    def show_message(self, title, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(text)
        msg.setWindowTitle(title)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())