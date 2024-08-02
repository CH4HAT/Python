import requests
import json
from pathlib import Path

"""
    NOTE:
    CoPilot/ChatGPT/etc. is not allowed for this submission.
    
    Any code that:
        a) is not related to the requirements, or
        b) was not explicitly covered in class, or
        c) is unnecessarily complex, irrelevant or nonsensical, or
        d) is identical to another student's submission
    may result in lost marks, up to and including failing the exam
"""

# TASK 1 - print your name and student number (10 marks)

print("CHAHAT_CHAHAT")
print("A01209821")


# ---------------------------------------------------------------------------------


#task2
data = {}

file_path = Path("part-one.json")
url = "https://endpoints.ch/1515/final/1"
if file_path.exists():
    with file_path.open("r") as file:
        data = json.load(file)
else:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with file_path.open("w") as file:
            json.dump(data, file)
    else:
        print(f"Failed to fetch data from URL: {url}")

"""
Using pathlib only (no os module etc.), check for the existence of a file (in the same directory as this script) named part-one.json 

If the file exists, load the JSON data from it into the data variable

If the file does not exist (and ONLY if the file does not exist):
    - Make a request to https://endpoints.ch/1515/final/1, storing the response in the data variable 
    - Create a file named part-one.json (in the same directory as this script) and dump the data into it
"""

# TASK 3 - debugging and interacting with python data structures (10 marks)
"""
Somewhere in the data you will find the following values:

    - a string <color>
    - an <integer>
    - a string <type>
    - a string <operation>

DEBUG the data to figure out how to access the values, then print (one per line)

    - the <color> and its type
    - the <integer> and its type
    - the <type> and its type
    - the <operation> and its type

Below is an example response (different from the actual response, with redacted property names) and expected output:

{
    "???": {
        "???": "red"
    },
    "???": [5],
    "???": "int",
    "???": [
        { "???": "multiply" }
    ]
}

red <class 'str'>
5 <class 'int'>
int <class 'str'>
multiply <class 'str'>
"""
print(
    data.get("the_color")[0].get("value"),type(data.get("the_color")[0].get("value"))
    ) 
print(
    data.get("a_number"),type(data.get("a_number"))
    )
print(
    data.get("the_type"),type(data.get("the_type"))
    )
print(
    data.get("operation").get("is"),type(data.get("operation").get("is"))
    )



# TASK 4 - creating a function (12 marks)
"""
Create a function named after a fruit (APPLE not allowed) that is the <color> you received, with the following requirements:

    - The function must have the number of parameters equal to the <integer> you received
    - The function must print the result of performing an operation equal to the <operation> you received on the parameters.

Below is an example function based on the values above:

def strawberry(p1, p2, p3, p4, p5):
    print(p1 * p2 * p3 * p4 * p5)
"""
def avocado(p1,p2,p3):
    print(p1+p2+p3)
avocado(1,2,3)



# TASK 5 - writing a loop, and calling a function (12 marks)
"""
Write a loop that runs as many times as the <integer> you received

In each iteration of the loop, call the function from Task 3 with the correct number and <type> of arguments. The arguments can be any values you choose.

Below is example output based on the information above, assuming the function is called with the arguments 1, 2, 3, 4, and 5:
120
120
120
120
120
"""
for i in range(0,3):
    avocado(1,2,3)


# TASK 6 - fetching data, reading/writing JSON files
"""
Using pathlib only (no os module etc.), check for the existence of a file (in the same directory as this script) named part-two.json 

If the file exists, load the JSON data from it into the data variable

If the file does not exist (and ONLY if the file does not exist):
    - Make a request to https://endpoints.ch/1515/final/2, store the response in the data variable
    - Create a file named part-two.json and dump the data into the file 

Somewhere in the data you will find the following values:

    - an initial string <value>
    - a string <result>
    - a string <instruction>
"""

#repeating task2 haha
file_path_2 = Path("part-two.json")
url_2 = "https://endpoints.ch/1515/final/2"
data_2 = {}
if file_path_2.exists():
    with file_path_2.open("r") as file:
        data_2 = json.load(file)
else:
    response = requests.get(url_2)
    if response.status_code == 200:
        data_2 = response.json()
        with file_path_2.open("w") as file:
            json.dump(data_2, file)
    else:
        print(f"Failed to fetch data from URL: {url_2}")


# ---------------------------------------------------------------------------------

the_value = ""
result = ""
course = ""

# TASK 7 - converting between data types, performing basic operations on data types (12 marks)
"""
Extract the string <value> you received into the the_value variable, and the <result> into the result variable

Follow the instructions in the <instruction> you received, then use an f-string to print the following sentence:
    "I {result} {course} in 2024"
"""
course=""
the_value=data_2.get("the_value_is")
result=data_2.get("result")
value_list = list(the_value)
for num in value_list:
    if int(num) % 2 != 0:
        course += num
print("I "+result+ " "+ course+" in 2024")



# TASK 8 - input/output, conditions (12 marks)
"""
Write a while loop that runs until a user enters a number less than 10, or a blank line
"""
while True:
    user_input = input("Please enter input")
    if user_input == "" or (user_input.isdigit() and int(user_input) < 10):
        print("Exiting the loop.")
        break
    else:
        print("Invalid input")


# TASK 9 - debugging (12 marks)
"""
Uncomment and modify the following code (without removing any code, and without adding try/except blocks) so that it runs without errors, and prints the expected output "Runtime errors occur...."
"""

"""
num1 = 1
num2 = num1 - num1

school = "BCIT"
course = ""

if num1/num2 % 0 == 1 and school[4] == 'T' and int(course) < 1620:
    print('Runtime errors occur when your file passes syntax checks, but the interpreter cannot succesfully run your code')
"""
num1 = 1
num2 = num1 

school = "BCIT"
course = ""

if school and school[-1] == 'T' and num2 != 0: 
    print('Runtime errors occur when your file passes syntax checks, but the interpreter cannot succesfully run your code')


# TASK 10 - refactoring (10 marks)
    """
There are two repetitive sections of code in this script (tasks 2 and 6):

    1. Given an existing file path, load json from that file and store it in a variable

    2. Given a *non-existent* file path, make a request to an endpoint, store the response in a variable, and write the response to a file

    Write a function that performs the steps in 1., and a second function that performs the steps in 2., with the following signatures: 
    
    1. Accepts a file path as a parameter and returns a dictionary
    
    2. Accepts a file path and URL as parameters, and returns a dictionary

NOTE: Simply providing the correct functions below will earn you 5/10 marks. To earn the full 10 marks, you must refactor (change) the script to use these functions instead of the existing code in tasks 2 and 6 (without breaking anything, of course).
"""


    
def fun1(file_path):

    data = {}
    file_path = Path("part-one.json")
    url = "https://endpoints.ch/1515/final/1" 
    if file_path.exists(): 
        with file_path.open("r") as file:
            data = json.load(file) 
    else:
        response = requests.get(url) 
        if response.status_code == 200: 
            data = response.json() 
            with file_path.open("w") as file:
                json.dump(data, file) 
        else: 
            print(f"Failed to fetch data from URL: {url}")



def fun2(file_path_2):

    url_2 = "https://endpoints.ch/1515/final/2" 
    data_2 = {} 
    if file_path_2.exists(): 
        with file_path_2.open("r") as file: 
            data_2 = json.load(file) 
    else: 
        response = requests.get(url_2) 
        if response.status_code == 200: 
                data_2 = response.json()
                with file_path_2.open("w") as file: 
                    json.dump(data_2, file) 
        else: 
                print(f"Failed to fetch data from URL: {url_2}")
    return data_2
            
fun2("part-two.json")            
fun1("part-one.json")

data=fun1("part-one.json")
          
data2=fun2("part-two.json")