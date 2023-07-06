from cryptography.fernet import Fernet

class Password_Manager:

    def __init__(self):
        self.key = None
        self.password_file = None#("accounts.json")
    
    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as file:
            file.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as file:
            self.key = file.read()

    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        if initial_values is not None:
            for key, value in initial_values.items():
                pass # todo: add password function

    def load_password_file(self, path):
        self.password_file = path
        
        with open(path, 'r') as file:
            for line in file:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as file:
                encrypted = Fernet(self.key).encrypt(password.encode())
                file.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.password_dict[site]

def main():
    password = {
        "email": "1234567",
        "facebook": "myfbpassword",
        "youtube": "hellowworld123",
        "something": "myfavouritepassword",
    }

    pm = Password_Manager()

    print("""WHat do you want to do?
    (1) Create a new key
    (2) Create a new key
    (3) Create a new key
    (4) Create a new key
    (5) Create a new key
    (6) Create a new key
    """)

    done = False

    while not done:

        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter path: ")
            pm.create_key(path)
        elif choice == "2":
            path = input("Enter path: ")
            pm.load_key(path)
        elif choice == "3":
            path = input("Enter path: ")
            pm.create_password_file(path, password)
        elif choice == "4":
            path = input("Enter path: ")
            pm.load_password_file(path)
        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
        elif choice == "6":
            site = input("What site do you want: ")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif choice == "q":
            done = True
            print("Bye")
            

# pm = Password_Manager()
# pm.create_key(None)

# def check_password():
#     password = "test"

#     if password == txt.get():
#         print("Right Password")
#     else:
#         print("Wrong Password")


# # check_password()