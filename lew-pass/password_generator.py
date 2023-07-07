# import secrets module to generate cryptographically strong random numbers
import secrets
# import string to allow use of ascii_lowercase, ascii_uppercase, digits, punctuation
import string

def generate_password():
    # setting variables for the strings that are being imported
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation
    characters = letters + digits + special_characters

    # password length
    # Ask the user for the websites specific length requirements guidelines
    # Most websites asking for a minimum of 8, so I'll set it at 10 to ensure a more secure password from the get go
    while True:
        # loop for min password length input, check correct input and error handling
        try:
            min_password_length = int(input("What is the minimum length of the password? "))
            # if password is 8 or less characters then break loop and start again
            if min_password_length >= 8:
                break
            else:
                # while min password length < 8 print error message and continue loop
                print("""
--------------------------------------------------------------
The minimum password length must be 8 or more characters long!
--------------------------------------------------------------
""")
        # value error for when a user enters a letter or non digit instead of a digit
        except ValueError:
            print("""
-----------------------------------
You must enter a number to proceed!
-----------------------------------
""")

    # Ask user for the maximum password length allowed
    while True:
         # loop for max password length input, check correct input and error handling
        try:
            max_password_length = int(input("What is the maximum length of the password? "))
            # if max password length is <= the min password length break loop and start again
            if min_password_length < max_password_length:
                break
            else:
                # while min password legnth is > then max password length print error message and continue loop
                print("""
--------------------------------------------------------------------------
The maximum password must be greater than the minimum password to proceed!
--------------------------------------------------------------------------
""")
        except ValueError:
                print("""
-----------------------------------
You must enter a number to proceed!
-----------------------------------
""")

    # password length is randomly selected through secrets module in the range from min_password_length to max_password_length
    password_length = secrets.choice(range(min_password_length, max_password_length + 1))
    # password is set to empty
    password = ""

    while True:
        # for loop to add characters to the password up to the password length
        for i in range(password_length):
            # each character added is randomised through sercrets module
            password += "".join(secrets.choice(characters))
        # check to make sure there is atleast one character of each type in the password
        if (any(c.islower for c in password)
                and any(c.isupper for c in password)
                and sum(c in digits for c in password)
                and any(c in special_characters for c in password)):
            break

    # print(password)
    return password