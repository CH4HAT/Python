"""

    ACIT 1515 - Lab 3

    For Lab 3 you will be creating a command-line guessing game where users can choose:
        a). The number of allowed guesses before the game is finished (or starts over), and
        b). A maximum value for the random number that is generated (i.e. the number to guess will be between 1 and the maximum value)
        
    The program will then generate a random number and prompt the user for guesses until:
        a). The number is guessed correctly
        b). The number of turns exceeds the number of allowed guesses

    Once a user has either guessed correctly or run out of guesses, the program should then ask the user if they want to continue.

    If the user enters the letter 'n', the program terminates - any other response will cause the program to start at the beginning, prompting the user for number of allowed guesses, maximum values, etc.

    For your submission, you must add code to this file sufficient to fulfill the following requirements:

    Part 1:
    -------
    Create the following six variables:
        keep_playing = True
        num_guesses = 0
        max_number = 0
        random_number = 0
        guess = 0
        guessed_correctly = False

    Part 2:
    -------
    Write a while loop using the value of the keep_playing variable as the condition that determines whether the loop should continue running or stop.

    Inside the while loop, prompt the user for:
        a). The number of allowed guesses (convert the result to int and store in the num_guesses variable)
        b). The maximum value allowed for the random number to be generated (convert the result to int and store in the max_number variable)

    Next, generate a random number using random.randint() function using 1 as the lower bound and max_number as the upper bound, and store the number in the random_number variable
        * Note the import statement provided for you - the random module (part of the standard Python library) is not available by default in Python scripts

    Part 3:
    -------
    Create a for loop using the range function, with 0 as the lower bound and num_guesses as the upper bound.

    Inside the for loop, prompt the user to enter a guess (converted to int and stored in the guess variable).

    Use if, elif, and else to print a message to the user indicating that their guess is either:
        a). "Too high!"
        b). "Too low!"
        c). "Correct!"

    If the user chooses the correct number, break out of the for loop, otherwise allow the loop to continue until all guesses have been used

    Part 4:
    -------
    Once the for loop has finished (either by the user guessing correctly, or by exhausting all available guesses), print two messages to the user:

        1. (Optionally) if they did not guess the correct number, print a message saying "Sorry, you have run out of guesses"
        2. Regardless of whether they guessed correctly or not, prompt the user with "Do you want to play again? " and store the result in a variable named response

        If response == "n", stop the while loop by setting the keep_playing variable to False which then allows the program to terminate. If the user enters any value other than "n", allow the while loop to continue running (which begins the game again from the start)

"""

import random

# add your code below this line

keep_playing = True
num_guesses = 0
max_number = 0
random_number = 0
guess = 0
guessed_correctly = False
import random

while keep_playing:
    num_guesses = input("please enter the number of guesses: ")
    if num_guesses.isdigit():
        num_guesses = int(num_guesses)
    max_number = input("please enter maximum value to be stored: ")
    if max_number.isdigit():
        max_number = int(max_number)
        keep_playing =False
         


    random = random.randint(1,max_number)    

        
    for i in range(num_guesses):
        guess = input('Enter a guess number:-')
        if guess.isdigit():
            guess = int(guess)
        if guess > random:
                print("too high : ")
        elif guess < random:
                print("too low ")
        else:
            print("correct ") 
            guessed_correctly = True
            break

    if guessed_correctly:
        print("good job")
        response = input ("do you wanna play again? ")  
        if response != "n":
            keep_playing = True
    else:
        print("sorry you ran out of time")
        response = input ("do you wanna play again? ")  
        if response == "n":
            keep_playing == False
