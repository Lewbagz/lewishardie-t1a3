import json
from clear import clear_terminal
import os
import bcrypt
import stdiomask

def test_userCreation():

    database_file = "test_database.json"
    with open(database_file, "w") as db_file:
        db_file.write("{}")
    assert database_file

    user = "testuser"
    password = "password"
    assert True

    # Add test user to the database
    data = {user: password}
    with open(database_file, "w") as db_file:
        json.dump(data, db_file)

def test_passwordHashing():
    
    password = "password"

    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    assert hashed_password.decode()

def store_user_and_password():
    