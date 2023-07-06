from password_generator import generate_password
from clear import clear_terminal
import json
import os


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
    [3] Remove Account
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
------ Empty Account List -----
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
    website = input("What account is this for? ")
    username = input("what is your username for the account? ")
    #check for @ and .com for email
    email = input("What is the email associated with the account? ")

    password = generate_password()

    # accounts[website] = {"Username": username, "Password": password, "Email": email}

    accounts = load_accounts()
    accounts[website] = {"Username": username, "Password": password, "Email": email}
    save_accounts(accounts)
    
    print("New account added")
    print(f"""
    -------- {website} --------
    Your Username is : {username}
    Your  Email   is : {email} 
    Your Password is : {password}
""")

def get_password():
    pass

def remove_account():
    clear_terminal()

    print("-----------Remove Account-----------")
    
    website = input("Enter the account name> ")
    
    accounts = load_accounts()

    if website in accounts:
        del accounts[website]
        save_accounts(accounts)
        print(f"The account '{website}' has been removed.")
    else:
        print(f"The account '{website}' does not exist.")
   
   
    # try:
    #     del load_accounts[account]
    #     print(account, "was deleted")
    # except ValueError:
    #     print(account, "was not found")

#     list_accounts()

#     account = input("Enter your task name or sequence> ")

#     try:
#         del accounts[account]
#         print(account, "was deleted")
#     except KeyError:
#         print(account, "was not found")


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
            remove_account()
        case _:
            break

    input("press enter to continue...")

print("Application closed")
