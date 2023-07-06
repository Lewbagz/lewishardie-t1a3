from password_generator import generate_password
from clear import clear_terminal

# class Password_Manager:
#     def __init__ (self):
#         self.key = None
#         self.password_file = None
#         self.password_dict = {}

#     def create password file

#     def load password file

#     def add password

#     def get password

# def main():

# password = {
#     "email": "example",
#     "facebook": "facebookpassword",
#     "youtube": "youtubepassword",
#     "forum" : "forumpassword",
# }

    # Enter options from the list below

    # [1] List all task
    # [2] Add new task
    # [3] Remove task
    # [4] Mark task as completed
    # [Enter anything else to exit..]
    # """) 
    

accounts = {

}

# functions
def print_options():
    clear_terminal()

    print("""
    Account options

    Enter options from the list below

    [1] List Accounts
    [2] Add Accounts
    [3] Get Password
    [Enter anything else to exit..]
    """) 

def list_accounts():
    clear_terminal()

    # for k,v in tasks.items(): # k,v stands for key and value. a way to extract those from the list
    #     print(k,v)

    print("""---------Your Accounts---------
-------------------------------
    """)

    if len(accounts.keys()) < 1:
        print("-------------XXXXXX------------")
        print("-------Empty Account List------")
        print("-------------XXXXXX------------")
    
    for website, account_info in accounts.items():
        username = account_info["Username"]
        password = account_info["Password"]
        email = account_info["Email"]
        print(f"""{website}
Username: {username}
Password: {password}
Email: {email}
------------------------------
""")

#     for website, username in accounts.items():
#         print(f"""
#     -------- {website} --------
#     {username} 
# """)
#         print("----------------------------")

def add_accounts():
    clear_terminal()
    print("---------Add new account--------")
    website = input("What account is this for? ")
    username = input("what is your username for the account? ")
    email = input("What is the email associated with the account? ")
    password = generate_password()
    accounts[website] = {"Username": username, "Password": password, "Email": email}
    print("New website added")
    print(f"""
    -------- {website} --------
    Your Username is : {username}
    Your  Email   is : {email} 
    Your Password is : {password}
""")


# master_password = ""
# master_password = (input("What is the master password? "))



# def check_password():

#     if master_password == "test":
#         print("Right password")
#     else:
#         print("Wrong password")

# def save_password():

# run our application
while True:
    print_options()

    option = int(input("Enter your selection> "))

    match option:
        case 1:
            list_accounts()
        case 2:
            add_accounts()
        case _:
            break

    input("press enter to continue...")

print("Application closed")


 Password manager

# password_list = []

# password_length = 12-64 characters long




# Generate a random password

# User Input 

#     User Account

#     User Email


# Output

#     Generate Random Password

#     password length 10-20

#     Random password to contain specific special characters ( 1 upper, 1 lower, 1 number, 1 punctuation)





# Password manager

# Create a file on computer

#     Account Name
#     Email
#     Password