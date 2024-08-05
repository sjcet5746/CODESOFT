#2.Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt
import sys

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.result_display = QLineEdit()
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setReadOnly(True)
        self.layout.addWidget(self.result_display)

        self.create_buttons()

        self.central_widget.setLayout(self.layout)

    def create_buttons(self):
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        for row in buttons:
            button_layout = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.on_button_click)
                button_layout.addWidget(button)
            self.layout.addLayout(button_layout)

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()
        
        current_text = self.result_display.text()

        if text == '=':
            try:
                result = eval(current_text)
                self.result_display.setText(str(result))
            except Exception:
                self.result_display.setText("Error")
        else:
            new_text = current_text + text
            self.result_display.setText(new_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())