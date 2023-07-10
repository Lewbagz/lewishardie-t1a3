 lewishardie-t1a3



# Lewis Hardie's T1A# Terminal Application - User Password Vault and Manager


## Link to Github Repository:

My github repository can be found at this [link](https://github.com/Lewbagz/lewishardie-t1a3).

`https://github.com/Lewbagz/lewishardie-t1a3`

## Link to Video Presentation:

My video presentation can found at this [link](https://youtube.com)

`youtube`

---

# Passworld Vault and Manager

## Purpose

The primary objective of my password manager is to enable individual users to access a secure database where they can store their signed-up accounts. Moreover, the application provides a random password generation feature to ensure highly secure passwords for each account.

During the registration process, users are required to create a unique username and a password for logging in. This password will serve as their single point of entry and should be as secure as possible, prioritizing strong security measures.

---

## Features
---
<br>
The terminal application I have developed incorporates a password generator powered by the secrets module, automating the process of creating secure passwords.

Within the application, a password manager is integrated, ensuring the secure storage of user-specific data in a JSON-based database.

To bolster security measures, the login and validation process has been implemented to restrict access to the password manager. This is achieved through the utilization of a hashed password mechanism using bcrypt.

In addition to these features, the application includes the following functionalities:

1. Master Password:
   - During the configuration phase, the user inputs a master password.
   - The master password is hashed and stored in a separate file from the password database, enhancing its security.

2. Adding New Accounts:
   - Users sign in with their master password.
   - They input the email, username, and website for the new account.
   - A random password generator is employed to generate a secure password for the account.

3. Random Password Generator:
   - The password generator prompts the user to specify the minimum and maximum length of the password.
   - It utilizes ASCII characters and the secrets module to randomly generate a string of characters, meeting the user's specified length.
   - The generator ensures that the generated password includes at least one uppercase letter, one lowercase letter, one digit, and one punctuation mark.

4. Retrieving Passwords for an App:
   - When requesting a password, the user selects the account for which they need the password.
   - The password is then copied to the user's clipboard, allowing for easy access to the desired application or website.

---

## Style Guide
---
<br>
I have chosen to adhere to PEP 8 guidelines when styling my Python code to prioritize consistency and readability. By following these guidelines, I maintain a uniform coding style that is familiar to other developers, facilitating their understanding and collaboration. PEP 8 covers various aspects such as indentation, naming conventions, comments, and imports, which contribute to the creation of well-organized and clean code. Consistent indentation and line length enhance code visual appeal and legibility, while adhering to naming conventions ensures clarity and self-explanatory code. Embracing PEP 8 not only promotes maintainable and comprehensible code but also fosters a professional coding standard within the Python community.

<br>

While adherence to PEP 8 is not obligatory, it is highly recommended for Python developers. By adhering to these guidelines, I contribute to a consistent and professional coding style that aligns with the fundamental principles of the Python language. Furthermore, following PEP 8 encourages effective collaboration and code sharing among developers by establishing a common framework of conventions and expectations. Overall, integrating PEP 8 guidelines ensures that my Python code meets high-quality standards and follows best practices, resulting in code that is more approachable and understandable for myself and fellow developers.

---

## Help Documentation
---
<br>

### <strong>Installing the application</strong>
<br>
The installation process for the application is straightforward.

Within the repository, you will find a file named "setup.sh" containing code that automatically sets up your system. 

In the command line terminal, when running a UNIX system, Mac, LINUX distribution system such as Ubunuto, all you need to do is navigate to the application folder and ./run.sh

This script performs the following steps:

- It checks if Python is installed and installs it if it is not detected.
- Next, it creates a virtual environment.
- Using the virtual environment, it verifies if pip is installed. If pip is not installed, it proceeds to install it.
- Once pip is installed, it proceeds to install all the necessary requirements and dependencies listed in the requirements file.

Once it is finished it'll inform you to now run `./run.sh` and this will launch the application.


### <strong>Dependencies</strong>

Python3 must be installed on the system in order for this application to run. You can pre-emptively download it from python.org. Otherwise I've included with in the `./setup.sh` the installation for Python3.

The packages that are used with this terminal are as follows;

- JSON  `pip3 install json`
    - JSON (JavaScript Object Notation) is a lightweight data interchange format that is commonly used for transmitting data between a server and a web application. 
- bcrypt `pip3 install bcrypt`
    - Acceptable password hashing for your software and your servers.
- pyperclip `pip3 install pyperclip`
    - Pyperclip is a cross-platform Python module for copy and paste clipboard functions.
- pytest `pip3 install pytest`
    - The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.
- stdiomask `pip3 install stdiomask`
    - A cross-platform Python module for entering passwords to a stdio terminal and displaying a **** mask, which getpass cannot do.


## System / Hardware requiremnets

The app is expected to preform well on practically any system, as it is extreamly light weight the requirements aren't high.


requirements

Implementation
- variables and variable scope
- loops and conditional control structures
- write and utilise simple functions
- error handling
- input and output
- importing a python package
- using functions frmo a python package

Apply Don't Repeat Yourself coding princicples

Provide 2 tests
    - cover a different section of the application
    - state what is being tested
    - provide at least TWO test cases and the expected results for each test case

Outline of the testing procedure and cases should be included with the source code of application

Utilise githup, make commits

Utilise dev to faciliate the execution of the application
- write a script which turns application into an exectuable

