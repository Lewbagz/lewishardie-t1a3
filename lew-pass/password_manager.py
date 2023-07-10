from password_generator import generate_password
from clear import clear_terminal
import json
import os
import pyperclip
import main

## CLASS SETUP IF TIME ALLOWS, trial later

# class Website:
#     def __init__(self, username, email, password):
#         self.username = username
#         self.email = email
#         self.password = password

#     def print_info(self):
#         print(self.username, self.email, self.password)
    
#     def save_to_json(self, filename):
#         website_dict = {'username': self.username, 'email': self.email, 'password': self.password}
#         with open(filename, 'w') as file:
#             file.write(json.dumps(website_dict, indent=4))
    
#     def load_from_json(self, filename):
#         with open(filename, 'r') as file:
#             data = json.loads(file.read())
        
#         self.username = data['username']
#         self.email = data['email']
#         self.password = data['password']



# Function to load the json file
def load_accounts(user_file):
   if os.path.exists(user_file):
        with open(user_file, "r") as file:
            try:
                return json.load(file) 
            except json.decoder.JSONDecodeError:
                return{}
   else:
       return{}

# Function to save the json file
def save_accounts(accounts, user_file):
    with open(user_file, "w") as file:
        json.dump(accounts, file, indent=4)

# function to display the terminal options
def print_options():
    clear_terminal() #maybe
    print("""---------------------------------
    Account options
---------------------------------
Select from the options below, 
by inputing the revelant number.
---------------------------------
---------------------------------
    [1] List Accounts
    [2] Add Accounts
    [3] Get Password
    [4] Remove Account
    [5] Log Out
    [Enter anything else to exit..]
---------------------------------""") 

# function to display the accounts in the json file
def list_accounts(user_file):
    clear_terminal()

    print("""---------Your Accounts---------
-------------------------------
""")
              
    accounts = load_accounts(user_file)


    if len(accounts) < 1:
        print("""-------------------------------
------ Account List Empty -----
-------------------------------""")

    for website, account_info in accounts.items():
        username = account_info["Username"]
        email = account_info["Email"]
        password = account_info["Password"]
            
        print(f"""
        {website}
------------------------------
Username: {username}
Email: {email}
Password: {password}
------------------------------
""")

# function to add additional accounts to the json file
def add_accounts(user_file):
    clear_terminal()
    print("""---------------------------------
    Add Account
---------------------------------
Enter no value to retun
---------------------------------
---------------------------------""")
    
    website = input("What account is this for? ").upper()
    if (website == ""):
        return
    username = input("What is your username for the account? ")
    if (username == ""):
        return
    
    while True:
        email = input("What is the email associated with the account? ")
        if "@" in email and "." in email:
            break
        else:
            print("Invalid Email")

        # return to welcome screen with null entry
        if (email == ""):
            return

    # Run password generator
    password = generate_password()

    accounts = load_accounts(user_file)
    accounts.update({website: {"Username": username, "Email": email, "Password": password}})
    save_accounts(accounts, user_file)
    
    print("New account added")
    print(f"""
    -------- {website} --------
    Your Username is : {username}
    Your  Email   is : {email} 
    Your Password is : {password}
""")

def get_password(user_file):
    clear_terminal()

    print("----------- Get Password -----------")
    print("--------- Enter no value to return --------")

    accounts = load_accounts(user_file)

    if len(accounts) < 1:
        print("""-------------------------------
------ Empty Account List -----
-------------------------------""")
              
    for index, (website, account_info) in enumerate(accounts.items()):
        password = account_info["Password"]

        print(f"""--------------
        [{index + 1}] {website}
--------------""")

    while True:
        
        selection = input("Which account password would you like to retrieve?: ")

        if selection == "":
            print("Returning you back to the main page")
            input("press anything to continue")
            return
        
        try:
            selection = int(selection)
            if selection in range(1, len(accounts) + 1):
                accounts[website]
                pyperclip.copy(password)
                print(f"The account '{website}' password has been copied to your clipboard.")

        except ValueError:
            print("Invalid selection.")
# function to remove account from user database         
def remove_account(user_file):
    clear_terminal()

    print("----------- Remove Account -----------")

    accounts = load_accounts(user_file)

    if len(accounts) < 1:
        print("""-------------------------------
------ Empty Account List -----
-------------------------------""")

    for index, (website, account_info) in enumerate(accounts.items()):
        username = account_info["Username"]
        # password = account_info["Password"]
        email = account_info["Email"]

        print(f"""------------------------------------------------
[{index + 1}] {website}: {username}, {email}
------------------------------------------------""")

    while True:

        selection = (input("Enter the number of the account to remove: "))

        if selection == "":
            print("Returning you back to the main page")
            input("press anything to continue")
            return
        
        try:    
            selection = int(selection)
            if selection in range(1, len(accounts) + 1):
                website = list(accounts.keys())[selection - 1]
                del accounts[website]
                save_accounts(accounts, user_file)
                print(f"The account '{website}' has been removed.")
        
        except ValueError:
            print("invalid")

def log_out():
    clear_terminal()
    print("--------- Log out of account --------")
    while True:
        try:
            option = input("Are you sure you want to log out?[y/n]: ")

        except ValueError:
            break

        match option:
            case "y":
                import main
                main.start_main()
                return
            case _:
                print("returning you page")
                input("press anything to continue")
                return

def start_password_management(username, user_file):

    while True:
        print_options()

        try:
            option = int(input("Enter your selection: "))
        except ValueError:
            break

        match option:
            case 1:
                list_accounts(user_file)
            case 2:
                add_accounts(user_file)
            case 3:
                get_password(user_file)
            case 4:
                remove_account(user_file)
            case 5:
                log_out()
            case _:
                break

    input("press enter to continue...")

print("Application closed")
