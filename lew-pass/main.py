# import secrets module to generate cryptographically strong random numbers
import secrets
# import string to allow use of ascii_lowercase, ascii_uppercase, digits, punctuation
import string
# import random to use randint to randomise password length
import random

# def user_name():



def generate_password():

    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    characters = letters + digits + special_characters
    
    # password length
    # Ask the user for the websites specific length requirements guidelines

    min_password_length = 10
    max_password_length = int(input("What is the maximum length of the password? "))
    
    while True:
        password_length = secrets.choice(range(min_password_length, max_password_length + 1)) #randbelow(50) + 10 # Generates a random password length between 10-60
        password = ""
        for i in range(password_length):
            password += "".join(secrets.choice(characters))
        
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password) 
                and sum(c.isdigit() for c in password)
                and any(c in special_characters for c in password)):
            break
    
    print(f"Your password is: {password}")
        

generate_password()

    #generate password

    # while True:
    #     password = ""

    #     for i in range(password_length):
    #         password += "".join(secrets.choice(characters))
    #     if (any(c.islower() for c in password)
    #             and any(c.isupper() for c in password) == 1 
    #             and any(c in special_characters for c in password) == 1
    #             and any(c.isdigit() for c in password) == 1):
    #         print(f"Your password is: {password}")
    #         break

    # while True: this checks true or false and output the password, probably most efficient
    #         password = ""
    #         has_uppercase = False
    #         has_digit = False
    #         has_special_character = False
            
    #         for i in range(password_length):
    #             char = secrets.choice(characters)
    #             password += char
                
    #             if char.isupper():
    #                 has_uppercase = True
    #             elif char.isdigit():
    #                 has_digit = True
    #             elif char in special_characters:
    #                 has_special_character = True
            
    #         if has_uppercase and has_digit and has_special_character:
    #             print(f"Your password is: {password}")
    #             break

    # while True:
    #     password = ""
    #     uppercase_count = 0
    #     digit_count = 0
    #     special_character_count = 0
        
    #     for i in range(password_length):
    #         char = secrets.choice(characters)
    #         password += char
            
    #         if char.isupper():
    #             uppercase_count += 1
    #         elif char.isdigit():
    #             digit_count += 1
    #         elif char in special_characters:
    #             special_character_count += 1
        
    #     if (
    #         uppercase_count == 1
    #         and digit_count == 1
    #         and special_character_count == 1
    #     ):
    #         print(f"Your password is: {password}")
    #         break



    # while True:  
    #     password = ""
    #     has_uppercase = False
    #     has_digit = False
    #     has_special_character = False
        
    #     for i in range(password_length):
    #         password += "".join(secrets.choice(characters))
            
    #         if password.isupper():
    #             has_uppercase = True
    #         elif password.isdigit():
    #             has_digit = True
    #         elif password in special_characters:
    #             has_special_character = True
        
    #     if has_uppercase and has_digit and has_special_character:
    #         print(f"Your password is: {password}")
    #         break



# Password manager

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