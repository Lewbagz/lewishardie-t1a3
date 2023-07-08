from clear import clear_terminal
import bcrypt


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
# def success():
#     clear_terminal()
#     print("You've successfully registered")
#     input("Enter any key to continue: ")


def register_user():
    db = open("data.txt", "r")

    while True:
        username = input("Create a username: ")
        # Email = input("Enter your email: ")
        # if username in db:
        #     print("username already exists")
        break
    
    while True:
        password = input("Create a password: ")
    
        if len(password) < 8:
            print("Password is too short, please try again.")
        else:
            break
    
    while True:
        password1 = input("Confirm your password: ")
        if password != password1:
            print("Passwords don't match, please try again.")
        else:
            break

        password = b""

        hahsed = bcrypt.hashpassword(password, bcrypt.gensalt())


    db = open("data.txt", "a")
    db.write(username+", "+password+"\n")


    clear_terminal()
    print("You've successfully registered")
    print(f"Username: {username}")
    print(f"Password: {password}")
    input("Enter any key to continue: ")


 # elif Username in db:
            #     print("username already exists")
            #     register()


def login():
    
    username = input("What is your username: ")
    password = input("what is your password: ").encode("utf-8")

    if bcrypt.checkpw(password, hashed):
        print("it matches")
        return # password_manager
    else:
        print("thats wrong dawg")


# select between register a username and loging in
while True:
    welcome_screen()
  
    selection = int(input(""))
    match selection:
        case 1:
            register_user()
        case 2:
            login()




# def validate(username, password):
#     return username == "lewis" & password == "123"

# username = input("Enter your username> ")
# password = input("Enter your username> ")

# print("welcome back")


# print("your details", username, password, "are", validate(username, password))



# class DBConnectionError(Exception): ...

# def validate(username, password):
#     return username == "lewis" and password == "123"
#     raise DBConnectionError("Your db can't be connected")

# username = input("Enter your username> ")
# password = input("Enter your password> ")

# try:
#     print("your details", username, password, "are", validate(username, password))
# except DBConnectionError as err:
#     print("error>>>>>>", str(err))

