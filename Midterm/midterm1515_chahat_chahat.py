"""
    In this script you will be using variables, while and for loops, tuples and lists, and conditional statements to generate a transcript of courses and grades

    The transcript will be represented by a list of tuples, each tuple containing:
        a. the name of the course
        b. the random grade for the course

    An example transcript might look like the following:
    [("ACIT 1515", 75), ("ACIT 1630", 70), ("ACIT 1420", 81), ("ACIT 1620", 83)]

    Once your transcript has been generated, you must calculate the average of all grades in the transcript.

    If the average is greater than or equal to 50, the while loop ends and a message is printed indicating to the user that they have passed, and how many attempts it took to pass.

    If the average is less than the 50, the while loop must be allowed to continue, and new transcripts are created until a passing mark is achieved.
"""

import random

# 1. Create a variable named 'passed' that stores the boolean value False
passed = False

# 2. Create a variable named attempts that stores the number zero
attempts = 0

# 3. Create a while loop that will run until the passed variable becomes True. Note: the remaining steps must be placed inside this while loop
while not passed:
    # 4. Create a variable that stores a list of four strings: "ACIT 1515", "ACIT 1630", "ACIT 1420", and "ACIT 1620"
    variable = ["ACIT 1515", "ACIT 1630", "ACIT 1420", "ACIT 1620"]
    # 5. Create a variable that stores an empty list
    var = []
    # 6. Create a for loop that loops through all the values in the list from step 4. Note: steps 7, 8, and 9 should be placed inside this for loop
    for s in variable:
        # 7. Inside the for loop, create a variable that stores a random number between 0 and 100
        random_no = random.randint(0,100)
        # 8. Next, create a variable that stores a tuple containing:
        tuple_storage = (s,random_no)
        var.append(tuple_storage)
            # a. The current string in the list from step 4
            # b. The random number from step 7

        # 9. Append the tuple to the list from step 5
        
    print(var)
    # 10. End the for loop by printing the entire list from step 5 on one line. Test your script to confirm that it contains values similar to the example at the top of the script

    # 11. Calculate the average of the numeric values stored in the tuples of the list from step 5, and store the result in a variable
    average = sum(marks[1] for marks in var)/len(var)
    # 12. Increase the value stored in the attempts variable by one
    attempts+=1
    # 13. If the number stored in the variable from step 11 is greater than or equal to 50:
        # a). Print a message congratulating the user on passing, and show them how many attempts it took to pass
        # b). Stop the while loop
    if average >=50:
        print(f"congratulation you have passed by taking {attempts} attempts")
        passed=True