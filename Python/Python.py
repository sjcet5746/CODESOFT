#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.A To-Do List application is a useful project that helps users manage
#and organize their tasks efficiently. This project aims to create a
#command-line or GUI-based application using Python, allowing
#users to create, update, and track their to-do lists
import json

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks):
    task = input("Enter task description: ")
    tasks.append({"id": len(tasks) + 1, "task": task, "status": "Pending"})
    print("Task added!")

def update_task(tasks):
    task_id = int(input("Enter task ID to update: "))
    for task in tasks:
        if task['id'] == task_id:
            task['task'] = input("Enter new task description: ")
            task['status'] = input("Enter new status (Pending/Completed): ")
            print("Task updated!")
            return
    print("Task not found!")

def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))
    tasks[:] = [task for task in tasks if task['id'] != task_id]
    print("Task deleted!")

def view_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Status: {task['status']}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. Update Task\n3. Delete Task\n4. View Tasks\n5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            update_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()


# In[2]:


#1.A To-Do List application is a useful project that helps users manage
#and organize their tasks efficiently. This project aims to create a
#command-line or GUI-based application using Python, allowing
#users to create, update, and track their to-do lists
import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(root)
        self.task_entry.pack()
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        self.tasks_listbox = tk.Listbox(root)
        self.tasks_listbox.pack()
        
        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.pack()
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")
    
    def update_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_index[0]] = new_task
                self.update_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Task cannot be empty")
        else:
            messagebox.showwarning("Warning", "No task selected")
    
    def delete_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            del self.tasks[selected_index[0]]
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "No task selected")
    
    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()


# In[ ]:


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


# In[4]:


#2.Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numerical values.")
            return
        
        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
    else:
        print("Invalid choice. Please choose a valid operation.")

if __name__ == "__main__":
    calculator()


# In[5]:


#2.Design a simple calculator with basic arithmetic operations.
#Prompt the user to input two numbers and an operation choice.
#Perform the calculation and display the result.
import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Display
        self.display = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 16), bd=10, relief='ridge', justify='right')
        self.display.grid(row=0, column=0, columnspan=4)

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=('Arial', 16), bd=5, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky='nsew')

        # Adjust row and column weights
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            new_text = current_text + text
            self.result_var.set(new_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


# In[ ]:


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


# In[7]:


#3.A password generator is a useful tool that generates strong and
#random passwords for users. This project aims to create a
#password generator application using Python, allowing users to
#specify the length and complexity of the password.
#User Input: Prompt the user to specify the desired length of the
#password.
#Generate Password: Use a combination of random characters to
#generate a password of the specified length.
#Display the Password: Print the generated password on the screen.
import random
import string

def generate_password(length, include_special_chars=True):
    # Define character sets
    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += string.punctuation
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator")
    
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
    
    password = generate_password(length, include_special_chars)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()


# In[8]:


#3.A password generator is a useful tool that generates strong and
#random passwords for users. This project aims to create a
#password generator application using Python, allowing users to
#specify the length and complexity of the password.
#User Input: Prompt the user to specify the desired length of the
#password.
#Generate Password: Use a combination of random characters to
#generate a password of the specified length.
#Display the Password: Print the generated password on the screen.
import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("300x200")
        
        self.create_widgets()

    def create_widgets(self):
        self.length_label = tk.Label(self.root, text="Password Length:")
        self.length_label.pack(pady=5)

        self.length_entry = tk.Entry(self.root)
        self.length_entry.pack(pady=5)

        self.special_chars_var = tk.BooleanVar()
        self.special_chars_check = tk.Checkbutton(self.root, text="Include Special Characters", variable=self.special_chars_var)
        self.special_chars_check.pack(pady=5)

        self.generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="Generated Password:")
        self.result_label.pack(pady=5)

        self.result_text = tk.Entry(self.root, width=40)
        self.result_text.pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
        except ValueError:
            self.result_text.delete(0, tk.END)
            self.result_text.insert(0, "Invalid length")
            return

        include_special_chars = self.special_chars_var.get()
        characters = string.ascii_letters + string.digits
        if include_special_chars:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.result_text.delete(0, tk.END)
        self.result_text.insert(0, password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


# In[ ]:


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


# In[10]:


#4.User Input: Prompt the user to choose rock, paper, or scissors.
#Computer Selection: Generate a random choice (rock, paper, or scissors) forthe computer.
#Game Logic: Determine the winner based on the user's choice and thecomputer's choice.
#Rock beats scissors, scissors beat paper, and paper beats rock.
#Display Result: Show the user's choice and the computer's choice.
#Display the result, whether the user wins, loses, or it's a tie.
#Score Tracking (Optional): Keep track of the user's and computer's scores formultiple rounds.
#Play Again: Ask the user if they want to play another round.
#User Interface: Design a user-friendly interface with clear instructions andfeedback
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or          (user_choice == 'scissors' and computer_choice == 'paper') or          (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock-Paper-Scissors Game")
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        
        if result == 'win':
            print("You win!")
            user_score += 1
        elif result == 'lose':
            print("You lose!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Score - You: {user_score} | Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    play_game()


# In[11]:


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
        elif (user_choice == 'rock' and computer_choice == 'scissors') or              (user_choice == 'scissors' and computer_choice == 'paper') or              (user_choice == 'paper' and computer_choice == 'rock'):
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
    root.mainloop()


# In[ ]:


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
        elif (user_choice == 'rock' and computer_choice == 'scissors') or              (user_choice == 'scissors' and computer_choice == 'paper') or              (user_choice == 'paper' and computer_choice == 'rock'):
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


# In[2]:


#5.Contact Information: Store name, phone number, email, and address for each contact.
#Add Contact: Allow users to add new contacts with their details.
#View Contact List: Display a list of all saved contacts with names and phone numbers.
#Search Contact: Implement a search function to find contacts by name or phone number.
#Update Contact: Enable users to update contact details.
#Delete Contact: Provide an option to delete a contact.
#User Interface: Design a user-friendly interface for easy interaction.
import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x400")

        self.contacts = {}  # Dictionary to store contacts

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Contact Book", font=('Arial', 16))
        self.title_label.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(self.root, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.pack(pady=10)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter contact name:")
        if not name:
            return
        phone = simpledialog.askstring("Input", "Enter phone number:")
        email = simpledialog.askstring("Input", "Enter email address:")
        address = simpledialog.askstring("Input", "Enter address:")
        if name in self.contacts:
            messagebox.showinfo("Info", "Contact already exists.")
        else:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Info", "Contact added successfully.")

    def view_contacts(self):
        self.result_text.delete(1.0, tk.END)
        for name, info in self.contacts.items():
            contact_info = f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}\n\n"
            self.result_text.insert(tk.END, contact_info)

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter contact name or phone number:")
        if not search_term:
            return
        found_contacts = []
        for name, info in self.contacts.items():
            if search_term in name or search_term in info['phone']:
                contact_info = f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}\n\n"
                found_contacts.append(contact_info)
        if found_contacts:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, ''.join(found_contacts))
        else:
            messagebox.showinfo("Info", "No contact found.")

    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to update:")
        if name not in self.contacts:
            messagebox.showinfo("Info", "Contact not found.")
            return
        phone = simpledialog.askstring("Input", f"Enter new phone number (current: {self.contacts[name]['phone']}):")
        email = simpledialog.askstring("Input", f"Enter new email address (current: {self.contacts[name]['email']}):")
        address = simpledialog.askstring("Input", f"Enter new address (current: {self.contacts[name]['address']}):")
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Info", "Contact updated successfully.")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Info", "Contact deleted successfully.")
        else:
            messagebox.showinfo("Info", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()


# In[ ]:




