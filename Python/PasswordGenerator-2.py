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