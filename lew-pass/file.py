### FILE HANDLING

## DOES FILE EXIST

import os # detects operating system

# file_path = "topic.txt" # checks for the file in the os

# print("file exists or not", os.path.exists(file_path)) # checks to see if file exists, return bool value

## READ, WRITE and APPEND

password_file_path = "passwords.txt"

def file_exists(file_path):
    if os.path.exists(file_path):
        # perform reading operations
        return True
    else:
        raise Exception(f"{file_path} does not exist")

#READ
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

#WRITE
def write_file(file_path):
    with open(file_path, 'w') as file:
        file.write("Hello from VSC")

#APPEND
def append_file(file_path):
    with open(file_path, 'a') as file:
        file.write("\nAppending, Hello from the app")

try:
    # DOES FILE EXIST
    file_exists(password_file_path)
    #READ
    password_content = read_file(password_file_path)
    print(password_content)
    #WRITE
    write_file(password_file_path)
    #APPEND
    append_file(password_file_path)
except Exception as err:
    print(str(err))
    # create new file if it doesnt exsist home work

## Use case, a player saving game graphic settings. When the player clicks save, the program will check for the file "graphics.txt", read that file, write / append the text within that file to mirror that of what the player has set.