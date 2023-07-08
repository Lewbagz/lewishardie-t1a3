import json
from clear import clear_terminal
import os


import bcrypt

import stdiomask


def validation(username, password, data):
    if username in data:
        hashed_password = data[username]
        if bcrypt.checkpw(password.encode(), hashed_password.encode()):
            return True
    return False

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
[3] Exit Application
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
        # Check to see if username already exists in the database
        if username_exists(username):
            print("Username already exists. Please try a different username.")
        else:
            break

    while True:
        # Get and confirm password, adding * to visual input for added security
        password = stdiomask.getpass("Create a password: ", "*")
        password1 = stdiomask.getpass("Confirm your password: ", "*")

        if len(password) < 8:
            print("Password is too short. Please try again.")
        elif password != password1:
            print("Passwords don't match. Please try again.")
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

    # Create a user-specific database for the password manager to access
    user_accounts_file = f"{username}_accounts.json"
    with open(user_accounts_file, "w") as user_file:
        json.dump({}, user_file, indent=4)

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
    password = stdiomask.getpass("Enter your password: ", '*')

    with open(DATABASE_FILE, "r") as db_file:
        data = json.load(db_file)
    
    if validation(username, password, data):
        print("Login successful")
        input("Enter any key to continue: ")
        user_file = f"{username}_accounts.json"
        import password_manager
        password_manager.start_password_management(username, user_file)
    else:
        print("Invalid username or password. Please try again.")
        input("Enter any key to continue: ")
    
    # user_database_file = f"{username}_database.json"
    # if os.path.exists(user_database_file):
    # password_manager.start_password_management(username, user_database_file)
    #     else:
    #         print("User database file not found. Please create an account or contact support.")

def main():
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w") as db_file:
            db_file.write("{}")

    while True:
        welcome_screen()

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
