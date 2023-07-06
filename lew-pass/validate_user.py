

def validate(username, password):
    return username == "lewis" & password == "123"

username = input("Enter your username: ")
password = input("Enter your password: ")

print("welcome back")


print("your details", username, password, "are", validate(username, password))



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