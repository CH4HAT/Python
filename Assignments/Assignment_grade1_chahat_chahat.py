import random
import sys

def generate_grade() -> int:
    """ Generate a grade (1 MARK)
    Arguments:
        None
    Returns:
        A random integer between 0 and 100
    """
    return random.randint(0, 100)

def generate_grades() -> list[int]:
    """ Generate a list of grades (3 MARKS)
    Arguments:
        None
    Returns:
        A list of 7 random grades, created by calling the generate_grade() function seven times in a loop
    """
    return [generate_grade() for _ in range(7)]

def get_menu() -> list[tuple[int, str]]:
    """ Generate a menu for the user (4 MARKS)
    Arguments:
        None
    Returns:
        An enumerated list of strings, 1-based (i.e. the op)
    """
    menu = ['List Grades', 'Check Average', 'Check Status', 'Change Grade', 'Exit']
    return list(enumerate(menu, 1))

def validate_choice(choice: int) -> int:
    """ Validate the user's choice
    Arguments:
        choice: a string representation of a number
    Returns:
        A number (between 0 and 5)
    """
    if 1 <= choice <= 5:
        return choice
    return 0

def get_average(grades: list[int]) -> int | float:
    """ Get the average of a list of grades
    Arguments:
        grades: a list of integers
    Returns:
        The mean (average) of the list
    """
    return sum(grades) / len(grades)

def get_status(grades: list[int]) -> bool:
    """ Get the passing status, based on the average of grades
    Arguments:
        grades: a list of integers
    Returns:
        True if average is greater than or equal to 50, otherwise False
    """
    average = get_average(grades)
    return average >= 50

def change_grade(grades: list[int], grade: int, new_value: int) -> list[int]:
    """ Change a grade to a new valid value
    Arguments:
        grades: a list of integers
        grade: the numeric position in the list of the grade to change
        new_value: an integer between 0 and 100
    Returns:
        The updated list of integers
    """        
    if 0 <= new_value <= 100:
        grades[grade - 1] = new_value
    return grades

if __name__ == "__main__":
    grades = generate_grades()

    while True:
        for value in get_menu():
            print(*value, sep=". ")

        choice = validate_choice(int(input('Please enter a choice: ')))

        match choice:
            case 0: # 0 must be returned by validate_choice() if the input is invalid
                print('Please choose a number between 1 and 5')
            case 1:
                print("Grades:", grades)
            case 2:
                average = get_average(grades)
                print(f"Average Grade: {average:.2f}")
            case 3:
                passing = get_status(grades)
                if passing:
                    print("Congratulations! You are passing the course.")
                else:
                    print("You are not yet passing the course.")
            case 4:
                print("Grades:")
                for idx, grade in enumerate(grades, 1):
                    print(f"{idx}. {grade}")
                grade_choice = int(input("Which grade do you want to update (1-7)? "))
                new_grade = int(input("Enter the new grade value: "))
                grades = change_grade(grades, grade_choice, new_grade)
            case 5:
                sys.exit()