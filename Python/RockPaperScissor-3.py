#4.User Input: Prompt the user to choose rock, paper, or scissors.
#Computer Selection: Generate a random choice (rock, paper, or scissors) forthe computer.
#Game Logic: Determine the winner based on the user's choice and thecomputer's choice.
#Rock beats scissors, scissors beat paper, and paper beats rock.
#Display Result: Show the user's choice and the computer's choice.
#Display the result, whether the user wins, loses, or it's a tie.
#Score Tracking (Optional): Keep track of the user's and computer's scores formultiple rounds.
#Play Again: Ask the user if they want to play another round.
#User Interface: Design a user-friendly interface with clear instructions andfeedbackfrom PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from PySide6.QtCore import Qt
import random
import sys

class RockPaperScissorsApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rock-Paper-Scissors Game")
        self.setGeometry(100, 100, 300, 250)

        self.user_score = 0
        self.computer_score = 0

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.title_label = QLabel("Rock-Paper-Scissors Game", alignment=Qt.AlignCenter)
        self.layout.addWidget(self.title_label)

        self.button_layout = QHBoxLayout()
        self.rock_button = QPushButton("Rock")
        self.paper_button = QPushButton("Paper")
        self.scissors_button = QPushButton("Scissors")
        self.rock_button.clicked.connect(lambda: self.play("rock"))
        self.paper_button.clicked.connect(lambda: self.play("paper"))
        self.scissors_button.clicked.connect(lambda: self.play("scissors"))
        self.button_layout.addWidget(self.rock_button)
        self.button_layout.addWidget(self.paper_button)
        self.button_layout.addWidget(self.scissors_button)
        self.layout.addLayout(self.button_layout)

        self.result_label = QLabel("", alignment=Qt.AlignCenter)
        self.layout.addWidget(self.result_label)

        self.score_label = QLabel("Score - You: 0 | Computer: 0", alignment=Qt.AlignCenter)
        self.layout.addWidget(self.score_label)

        self.play_again_button = QPushButton("Play Again")
        self.play_again_button.clicked.connect(self.reset_game)
        self.layout.addWidget(self.play_again_button)

        self.central_widget.setLayout(self.layout)

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'win'
        else:
            return 'lose'

    def play(self, user_choice):
        computer_choice = self.get_computer_choice()
        result = self.determine_winner(user_choice, computer_choice)

        result_message = f"Computer chose: {computer_choice}\n"
        if result == 'win':
            result_message += "You win!"
            self.user_score += 1
        elif result == 'lose':
            result_message += "You lose!"
            self.computer_score += 1
        else:
            result_message += "It's a tie!"

        self.result_label.setText(result_message)
        self.score_label.setText(f"Score - You: {self.user_score} | Computer: {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.setText("Score - You: 0 | Computer: 0")
        self.result_label.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RockPaperScissorsApp()
    window.show()
    sys.exit(app.exec())