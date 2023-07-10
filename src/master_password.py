import json
from clear import clear_terminal
import os
import bcrypt
import stdiomask
import sys
import password_manager

DATABASE_FILE = "database.json"

# Function to validate if the encrypted password matches the entered password
def validation(user, password, data):
    if user in data:
        hashed_password = data[user]
        if bcrypt.checkpw(password.encode(), hashed_password.encode()):
            return True
    return False

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
    clear_terminal()
    print("""---------------------------------
    Register your Username
---------------------------------
   Pressing enter will return 
   you to the welcome screen.
---------------------------------""")
          
    while True:

        user = input("Create a User: ")
        
        if user == "":
            return

        if user == "":
            print("User name cannot be empty")
        elif user_exists(user):
            print("User already exists. Please try a different user.")
        else:
            break

    clear_terminal()
    print("""---------------------------------
    Select your Password""")
    print("""---------------------------------
Password must be 12 characters long""")
    print("""---------------------------------
    Pressing enter will return 
    you to the welcome page.
---------------------------------""")           
            
    while True:
        # Get and confirm password, adding * to visual input for added security
        password = stdiomask.getpass("Create a password: ", "*")

        if password == "":
            print("Registration canceled.")
            return  # Break out of the loop

        password1 = stdiomask.getpass("Confirm your password: ", "*")

        try:
            if len(password) < 12:
                print("Password is too short. Please try again.")
            elif password != password1:
                print("Passwords don't match. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid")

    # Hash the password
    hashed_password = hash_password(password)

    # Store the user and hashed password in the database (JSON file)
    with open(DATABASE_FILE, "r") as db_file:
        data = json.load(db_file)

    data[user] = hashed_password

    with open(DATABASE_FILE, "w") as db_file:
        json.dump(data, db_file, indent=4)

    # Create a user-specific database for the password manager to access
    user_accounts_file = f"{user}_accounts.json"
    with open(user_accounts_file, "w") as user_file:
        json.dump({}, user_file, indent=4)

    clear_terminal()
    print("You've successfully registered")
    print(f"Username: {user}")

def user_exists(user):
    with open(DATABASE_FILE, "r") as db_file:
        data = json.load(db_file)
        return user in data

def login():
    clear_terminal()
    print("""---------------------------------
            Login""")
    print("""---------------------------------
    Pressing enter will return 
    you to the welcome page.
---------------------------------""") 
    user = input("Enter the Username: ")

    if user == "":
        print("Invalid Username")
        return  # Break out of the loop
    
    password = stdiomask.getpass("Enter your password: ", '*')
    if password == "":
        print("You must enter a password")
        return  # Break out of the loop

    with open(DATABASE_FILE, "r") as db_file:
        data = json.load(db_file)

    if validation(user, password, data):
        print("Login successful")
        input("Enter any key to continue: ")
        user_file = f"{user}_accounts.json"
        # import password_manager
        # # __name__ == 
        password_manager.start_password_management(user, user_file)
    else:
        print("Invalid username or password. Please try again.")

def main():
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w") as db_file:
            db_file.write("{}")

    while True:
        welcome_screen()

        selection = input("Enter your choice: ")

        try:
            selection = int(selection)
            match selection:
                case 1:
                    register_user()
                case 2:
                    login()
                case 3:
                    sys.exit()
                case _:
                    print("INVALID SELECTION")
        except ValueError:
            print("value error")
        
        input("Press enter to continue: ")

print("Application closed")
