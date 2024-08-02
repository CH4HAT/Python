"""
    ACIT 1515 - Lab 4

    For this version of Lab 4, you will be creating a script that prompts the user for a password using the built-in getpass function. 

    A password is considered strong if:
    1. It contains at least one uppercase letter
    2. It contains at least one lowercase letter
    3. It contains at least one number
    4. It contains at least one special character from the list ~!@#$%^&*_+-=
    5. Is at least 12 characters long
    6. Does not contain any consecutive characters

    In addition, you must use type hints in your functions to ensure that:
    a. The arguments to the function are of the correct data type
    b. The return values from the functions are of the correct data type

    Below is an example of a function that includes type hints for function arguments and return values:

    def has_uppercase(password: str) -> bool:
        pass

    For the above example, password: str indicates that the password parameter must be of type int, and 
    -> bool after the parentheses indicates that the function must return a True or False value

    To perform type checking, install mypy with:
        pip install mypy
        OR
        pip3 install mypy
    
    and check your script with:
        mypy lab4.py

    Note that the mypy command does not run the script! It only checks the script for type errors. If you 
    run mypy and see output similar to:
        Success: no issues found in 1 source file

    you can then run your file as per usual with:
        py lab4.py


    INSTRUCTIONS:
    ------------

    To implement the above functionality, you must create seven functions:

    has_uppercase()
    has_lowercase()
    has_number()
    has_special()
    has_length()
    has_consecutive_characters()
    strong_password()

    Each of the above functions must accept a single string argument named password and return a boolean value. Use type hints for both the argument and the return value.
    
    The strong_password() function, called for you in the main() function below, is responsible for calling all other functions and checking whether any of them returns False. If any of the has_ functions return false, strong_password() returns False, likewise if all the has_ functions return True, strong_password() will return True.

"""

# from getpass import getpass # optionally use this in place of input() to hide the password input

# Add your functions here
from getpass import getpass 


def has_uppercase(password :str) ->bool:
    return True if any(character.isupper() for character in password) else False

def has_lowercase(password :str) ->bool:
    return True if any(character.islower() for character in password) else False

def has_number(password :str) ->bool:
    return True if any(character.isdigit() for character in password) else False

def has_special(password :str) ->bool:
    special_characters = "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?"
    return True if any(character in special_characters for character in password) else False 
    
def has_length(password :str) ->bool:
    return True if len(password) >= 12 else False

def has_consecutive_characters(password :str) ->bool:
    return False if any(character.isspace() for character in password ) else True

def strong_password(password :str) ->bool:
    return (
        has_uppercase(password) and
        has_lowercase(password) and 
        has_length(password) and
        has_consecutive_characters(password) and 
        has_special(password) and 
        has_number(password)
    )

def main():
    password = input("Please enter your password: ")
    if strong_password(password):
        print("Strong Password")
    else:
        print("Weak Password")

if __name__ == "__main__":
    main()
