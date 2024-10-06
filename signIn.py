import msvcrt
import json

def load_user_database():
    try:
        with open('user_database.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_database(user_database):
    with open('user_database.json', 'w') as file:
        json.dump(user_database, file)

def getpass_with_mask(prompt=""):
    password = ""
    print(prompt, end='', flush=True)
    while True:
        char = msvcrt.getch().decode('utf-8')
        if char == '\r':
            print()  # Move to the next line after password entry
            break
        elif char == '\x08':  # Backspace
            if password:
                password = password[:-1]
                print('\x08 \x08', end='', flush=True)  # Move back, overwrite '*', move back
        else:
            password += char
            print('*', end='', flush=True)  # Print '*' for masking
    return password

def login(username, password, user_database):
    if username in user_database:
        stored_password = user_database[username]
        if stored_password == password:
            print("Login successful.")
            return True
        else:
            print("Incorrect password. Please try again.")
            return False
    else:
        print("Username not found. Please register.")
        return False

# Example usage:
user_database = load_user_database()
login_ = False



while (not login_):
    username_input = input("Enter your username: ")
    password_input = getpass_with_mask("Enter your password: ")
    if (login(username_input, password_input, user_database)):
        for key in user_database.keys():
            if (key == username_input):
                print("Welcome " + str(key) + "!")
                login_ = True
                break