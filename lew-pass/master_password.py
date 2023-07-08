import json
from clear import clear_terminal
import os
import bcrypt
import stdiomask


# def encoded_input(message):
#     print(message, end="", flush=True)
#     pw = ""
#     while True:
#         symbol = getch.getch()
#         if symbol == "\n" or symbol == "\r":
#             break
#         print("*", end="", flush=True)
#     print()
#     return pw

DATABASE_FILE = "database.json"

# Function to display the login screen
def welcome_screen():
    clear_terminal()

    print("""---------------------------------
             Welcome
---------------------------------
---------------------------------
Select what you would like to do:
---------------------------------
[1] Register
[2] Login
---------------------------------
"""
)

# Function to hash the password
def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password.decode()

def register_user():
    while True:
        username = input("Create a username: ")
        # Check to see if username already exsits in database
        if username_exists(username):
            print("Username already exists. Please try a different username.")
        else:
            break
    
    while True:
        # Get and confirm password, adding * to visual input for added security
        password = stdiomask.getpass("Create a password: ", '*')
        password1 = stdiomask.getpass("Confirm your password: ", '*')

        if len(password) < 8:
            print("Password is too short, please try again.")
        elif password != password1:
            print("Passwords don't match, please try again.")
        else:
            break

    # Hash the password
    hashed_password = hash_password(password)

    # Store the username and hashed password in the database (JSON file)

    with open(DATABASE_FILE, "r") as db_file:
        data = json.load(db_file)

    data[username] = hashed_password

    with open(DATABASE_FILE, "w") as db_file:
        json.dump(data, db_file, indent=4)

    clear_terminal()
    print("You've successfully registered")
    print(f"Username: {username}")
    input("Enter any key to continue: ")

def username_exists(username):
    with open(DATABASE_FILE, "r") as db_file:
        data = json.load(db_file)
        return username in data

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open(DATABASE_FILE, "r") as db_file:
        data = json.load(db_file)
    
    if username in data:
        hashed_password = data[username]
        if bcrypt.checkpw(password.encode(), hashed_password.encode()):
            print("Login successful")
        else:
            print("Invalid username or password. Please try again.")
    
    clear_terminal()
    print("You've successfully logged in")
    input("Enter any key to continue: ")

def main():
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w") as db_file:
            db_file.write("{}")

    while True:
        welcome_screen()
  
        # selection = input("Enter your choice: ")
        # if selection == "1":
        #     register_user()
        # elif selection == "2":
        #     login()
        # elif selection == "3":
        #     break

        selection = int(input("Enter your choice: "))
        
        match selection:
            case 1:
                register_user()
            case 2:
                login()
            case _:
                break

    input("press enter to continue...")

print("Application closed")

main()
