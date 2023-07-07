import json
from clear import clear_terminal
import bcrypt
import os

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
        
        if username_exists(username):
            print("Username already exists. Please try a different username.")
        else:
            break
    
    while True:
        password = input("Create a password: ")
        password1 = input("Confirm your password: ")

        if len(password) < 8:
            print("Password is too short, please try again.")
        if password != password1:
            print("Passwords don't match, please try again.")
        else:
            break

    # Hash the password
    hashed_password = hash_password(password)

    # Store the username and hashed password in the database (JSON file)

    # if os.path.exists(DATABASE_FILE):
    #     with open(DATABASE_FILE, "r") as db_file:
    #         try:
    #             data = json.load(db_file)
    #         except json.decoder.JSONDecodeError:
    #             data = {}
    # else:
    #     data = {}
    with open(DATABASE_FILE, "r") as db_file:
        data = json.load(db_file)

    data[username] = hashed_password

    with open(DATABASE_FILE, "w") as db_file:
        json.dump(data, db_file)

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