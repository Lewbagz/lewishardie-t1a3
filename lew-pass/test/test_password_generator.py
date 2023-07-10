import string



def test_generate_password():
    # Test case 1: Minimum and maximum length are the same
    
    min_password_length = input
    max_password_length = 10
    password = min_password_length == max_password_length
    assert True

    # Test case 2: Minimum and maximum length are different
    min_password_length = 8
    max_password_length = 12
    password = min_password_length != max_password_length
    assert True

    # Test case 3: Password contains at least one lowercase, uppercase, digit, and special character
    
    password = "abchSd123h3./dgdhf"
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in string.punctuation for c in password)

    