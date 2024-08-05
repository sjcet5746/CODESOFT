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