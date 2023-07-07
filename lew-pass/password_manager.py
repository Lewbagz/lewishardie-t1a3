from password_generator import generate_password
from clear import clear_terminal
import json
import os
import pyperclip


# Function to load the json file
def load_accounts():
   if os.path.exists("accounts.json"):
        with open ("accounts.json", "r") as file:
            try:
                return json.load(file) 
            except json.decoder.JSONDecodeError:
                return{}
   else:
       return{}

# Function to save the json file
def save_accounts(accounts):
    with open("accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)


# function to display the terminal options
def print_options():
    clear_terminal() #maybe

    print("""
    Account options

    Select from the options below, by inputing the revelant number.

    [1] List Accounts
    [2] Add Accounts
    [3] Get Password
    [4] Remove Account
    [Enter anything else to exit..]
    """) 

# function to display the accounts in the json file
def list_accounts():
    clear_terminal() #maybe


    print("""---------Your Accounts---------
-------------------------------
""")
              
    accounts = load_accounts()


    if len(accounts) < 1:
        print("""-------------------------------
------ Account List Empty -----
-------------------------------""")

    for website, account_info in accounts.items():
        username = account_info["Username"]
        password = account_info["Password"]
        email = account_info["Email"]
            
        print(f"""
        {website}
------------------------------
Username: {username}
Password: {password}
Email: {email}
------------------------------
""")
        

# function to add additional accounts to the json file
def add_accounts():
    clear_terminal()
    print("---------Add new account--------")
    website = input("What account is this for? ").upper()
    username = input("what is your username for the account? ")
    #check for @ and .com for email
    email = input("What is the email associated with the account? ")

    password = generate_password()

    # accounts[website] = {"Username": username, "Password": password, "Email": email}

    accounts = load_accounts()
    accounts.update({website: {"Username": username, "Password": password, "Email": email}})
    save_accounts(accounts)
    
    # accounts.update({website: {"Username": username, "Password": password, "Email": email}})

    print("New account added")
    print(f"""
    -------- {website} --------
    Your Username is : {username}
    Your Password is : {password}
    Your  Email   is : {email} 
""")


def get_password():
    clear_terminal()

    print("----------- Get Password -----------")

    accounts = load_accounts()

    for website, account_info in accounts.items():
        # username = account_info["Username"]
        password = account_info["Password"]
        # email = account_info["Email"]
            
        print(f"""--------------
        {website}
--------------
""")
        
    website = input("Which account password would you like to retrieve?: ").upper()
  
    if website in accounts:
        accounts[website]
        pyperclip.copy(password)
        print(f"The account '{website}' password has been copied to your clipboard.")
    else:
        print(f"The account '{website}' does not exist.")
    pass

def remove_account():
    clear_terminal()

    print("----------- Remove Account -----------")

    accounts = load_accounts()

    if len(accounts) < 1:
        print("""-------------------------------
------ Empty Account List -----
-------------------------------""")

    for index, (website, account_info) in enumerate(accounts.items()):
        username = account_info["Username"]
        # password = account_info["Password"]
        email = account_info["Email"]

        print(f"""
------------------------------------------------
[{index + 1}] {website}: {username}, {email}
------------------------------------------------""")
    while True:
        try:    
            selection = int(input("Enter the number of the account to remove: "))
            if selection in range(1, len(accounts) + 1):
                website = list(accounts.keys())[selection - 1]
                del accounts[website]
                save_accounts(accounts)
                print(f"The account '{website}' has been removed.")
            else:
                print("Invalid selection.")
        except ValueError:
            break

while True:
    print_options()
    try:
        option = int(input("Enter your selection> "))
    except ValueError:
        break

    match option:
        case 1:
            list_accounts()
        case 2:
            add_accounts()
        case 3:
            get_password()
        case 4:
            remove_account()
        case _:
            break

    input("press enter to continue...")

print("Application closed")
