#4.User Input: Prompt the user to choose rock, paper, or scissors.
#Computer Selection: Generate a random choice (rock, paper, or scissors) forthe computer.
#Game Logic: Determine the winner based on the user's choice and thecomputer's choice.
#Rock beats scissors, scissors beat paper, and paper beats rock.
#Display Result: Show the user's choice and the computer's choice.
#Display the result, whether the user wins, loses, or it's a tie.
#Score Tracking (Optional): Keep track of the user's and computer's scores formultiple rounds.
#Play Again: Ask the user if they want to play another round.
#User Interface: Design a user-friendly interface with clear instructions andfeedback
import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.root.geometry("300x250")

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Rock-Paper-Scissors Game", font=('Arial', 16))
        self.title_label.pack(pady=10)

        self.choice_frame = tk.Frame(self.root)
        self.choice_frame.pack(pady=10)

        self.rock_button = tk.Button(self.choice_frame, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(side=tk.LEFT, padx=5)

        self.paper_button = tk.Button(self.choice_frame, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(side=tk.LEFT, padx=5)

        self.scissors_button = tk.Button(self.choice_frame, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(self.root, text="", font=('Arial', 14))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="Score - You: 0 | Computer: 0", font=('Arial', 12))
        self.score_label.pack(pady=10)

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=10)

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

        self.result_label.config(text=result_message)
        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score - You: 0 | Computer: 0")
        self.result_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()\