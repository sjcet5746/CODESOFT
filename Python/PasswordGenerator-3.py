#3.A password generator is a useful tool that generates strong and
#random passwords for users. This project aims to create a
#password generator application using Python, allowing users to
#specify the length and complexity of the password.
#User Input: Prompt the user to specify the desired length of the
#password.
#Generate Password: Use a combination of random characters to
#generate a password of the specified length.
#Display the Password: Print the generated password on the screen.
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QCheckBox
import sys
import random
import string

class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.create_widgets()

        self.central_widget.setLayout(self.layout)

    def create_widgets(self):
        self.length_label = QLabel("Password Length:")
        self.layout.addWidget(self.length_label)

        self.length_entry = QLineEdit()
        self.layout.addWidget(self.length_entry)

        self.special_chars_check = QCheckBox("Include Special Characters")
        self.layout.addWidget(self.special_chars_check)

        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)
        self.layout.addWidget(self.generate_button)

        self.result_label = QLabel("Generated Password:")
        self.layout.addWidget(self.result_label)

        self.result_text = QLineEdit()
        self.result_text.setReadOnly(True)
        self.layout.addWidget(self.result_text)

    def generate_password(self):
        try:
            length = int(self.length_entry.text())
        except ValueError:
            self.result_text.setText("Invalid length")
            return

        include_special_chars = self.special_chars_check.isChecked()
        characters = string.ascii_letters + string.digits
        if include_special_chars:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.result_text.setText(password)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())