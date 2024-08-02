"""
Assignment 1: Grades Generator
------------------------------

Assignment 1 is designed to test your understanding of the skills practiced in weeks 1 through 4:
- creating variables using Python's built-in data types
- converting and checking data types 
- using built-in functions
- using conditional statements and loops
- writing custom functions

For assignment 1 you will be writing a script that generates random grades and allows you to:
    a). View your randomly generated grades
    b). Get the average of your randomly generated grades
    c). Report your pass/fail status (i.e. if the average is above 50, you are passing. If the average is below 50 you are not yet passing)
    d). Change a grade
    e). Quit

The script will consist of several functions, each of which has a placeholder below with instructions.

NOTE: all input (getting choices from the user) and output (printing to the console) MUST occur inside the if __name__ == '__main__' block. 

The functions (generate_grade, generate_grades, get_menu, validate_choice, get_average, get_status, and change_grade) *MUST NOT* contain any print() or input() statements
"""

import random
import sys

def generate_grade() -> int:
    """ Generate a grade (1 MARK)
    Arguments:
        None
    Returns:
        A random integer between 0 and 100
    """
    
    pass # REMOVE

def generate_grades() -> list[int]:
    """ Generate a list of grades (3 MARKS)
    Arguments:
        None
    Returns:
        A list of 7 random grades, created by calling the generate_grade() function seven times in a loop
    """
    
    pass # REMOVE

def get_menu() -> list[tuple[int, str]]:
    """ Generate a menu for the user (4 MARKS)
    Arguments:
        None
    Returns:
        An enumerated list of strings, 1-based (i.e. the op)
    """

    # create a list of 5 strings: 'List Grades', 'Check Average', 'Check Status', 'Change Grade', 'Exit'
    
    # enumerate (starting at 1) and return the list
    
    pass # REMOVE

def validate_choice(choice: int) -> int:
    """ Validate the user's choice
    Arguments:
        choice: a string representation of a number
    Returns:
        A number (between 0 and 5)
    """
    
    # if choice is between 1 and 5, return the choice, otherwise return 0
    
    pass # REMOVE

def get_average(grades: list[int]) -> int | float:
    """ Get the average of a list of grades
    Arguments:
        grades: a list of integers
    Returns:
        The mean (average) of the list
    """

    pass # REMOVE

def get_status(grades: list[int]) -> bool:
    """ Get the passing status, based on the average of grades
    Arguments:
        grades: a list of integers
    Returns:
        True if average is greater than or equal to 50, otherwise False
    """

    # call the get_average() function and check if average is greater than or equal to 50
    # if so, return True, otherwise return False
    
    pass # REMOVE
    
def change_grade(grades: list[int], grade: int, new_value: int) -> list[int]:
    """ Change a grade to a new valid value
    Arguments:
        grades: a list of integers
        grade: the numeric position in the list of the grade to change
        new_value: an integer between 0 and 100
    Returns:
        The updated list of integers
    """        
        
    # if the new value is valid, silently (no print() statements) update the grade and return the list

    # if the new grade is not valid, silently return the list without updating the grade

    pass # REMOVE     

if __name__ == "__main__":
    # call the generate_grades() function and store the result in variable

    while True:
        for value in get_menu():
            print(*value, sep=". ")

        choice = validate_choice(int(input('Please enter a choice: ')))

        match choice:
            case 0: # 0 must be returned by validate_choice() if the input is invalid
                print('Please choose a number between 1 and 5')
            case 1:
                # print the grades, all grades on one line
                pass # REMOVE
            case 2:
                # call the get_average() function and print the average, rounded to two decimal places
                pass # REMOVE
            case 3:
                # call the get_status() function and store the returned value in a variable

                # if passing, print a message to the user indicating they are passing the course
                # otherwise, print a (supportive?) message to the user indicating they are not yet passing
                
                pass # REMOVE
            case 4:
                # enumerate and print the grades list, one grade per line

                # ask the user which grade (1 through 7) they want to update and store the result in a variable

                # ask the user for a new value and store the result in a variable

                # call the change_grade() function and pass in 
                # a) the list of grades, 
                # b) the grade to change, and 
                # c) the new value
                # store the returned list back into the same variable you created above when calling generate_grades()
            
                pass # REMOVE
            case _:
                # exit
                pass # REMOVE
            
