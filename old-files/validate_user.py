import bcrypt
from clear import clear_terminal

DATABASE_FILE = "database.txt"

stored_username= {

}

stored_password = {
    
}

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password.decode()

def register():
    while True:
        username = input("Create a username: ")
        password = input("Create a password: ")
        password_confirmation = input("Confirm your password: ")

        if len(password) < 8:
            print("Password is too short, please try again.")
        elif password != password_confirmation:
            print("Passwords don't match, please try again.")
        else:
            # Hash the password
            hashed_password = hash_password(password)

            # Store the username and hashed password in the database
            with open(DATABASE_FILE, "a") as db:
                db.write(f"{username},{hashed_password}\n")

            clear_terminal()
            print("You've successfully registered")
            print(f"Username: {username}")
            input("Press Enter to continue")
            return

def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Read the database file and check for matching username and password
        with open(DATABASE_FILE, "r") as db:
            stored_username, stored_password = line.strip().split(",")
                if username == stored_username and bcrypt.checkpw(password.encode(), stored_password.encode()) in db:
                    print("Login successful")
                    return

        print("Invalid username or password. Please try again.")

def main():
    while True:
        choice = input("Choose an option:\n1. Register\n2. Login\n3. Quit\n")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# def validate(username, password):
#     return username == "lewis" & password == "123"

# username = input("Enter your username: ")
# password = input("Enter your password: ")

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