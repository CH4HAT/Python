# BASICS ------------------------------------------

# create a variable, store a primitive value (int, string, bool)
primitive_value = 37
string_value = "Hello, world!"
bool_value = True

# create a variable, store a list
new_list = [1, 2, 3, 4, 5]

# iterate through the list
for item in new_list:
    print(item)

# update value in the list
new_list[2] = 37

# create a variable, store a set
transcript = {1, 2, 3, 4, 5}

# iterate through the set
for i in transcript:
    print(i)

# convert a list to a set
list = [1, 2, 2, 3, 3, 3]
set = set(list)

# create a variable, store a dictionary
dictionary = {'a': 1, 'b': 2, 'c': 3}

# iterate through keys and values in the dictionary
for i, j in dictionary.items():
    print(i, j)

# update value in the dictionary
dictionary['a'] = 37

# write an if statement that prints a value
if bool_value:
    print("The boolean value is True")

# write an if statement that sets a variable conditionally
value = 50 if primitive_value > 37 else -37

# create a function that returns a value
def function():
    return "This is a returned value"

# call the function and store the returned value
returnedvalue = function()

# create a function with a parameter that alters and returns the parameter
def alterParameter(parameter):
    parameter += 37
    return parameter

# call the function and store the returned value
altered = alterParameter(primitive_value)

# COMBINATIONS -------------------------------

# create a variable, store a list with dictionaries in it
validdict = [{'name': 'John', 'age': 30}, {'name': 'Alice', 'age': 25}]

# iterate through the list, print values
for person in validdict:
    print(person['name'], person['age'])

# iterate through the list, update a value
for person in validdict:
    person['age'] += 1

# create a variable, store a list
numbers = [1, 2, 3, 4, 5]

# iterate through the list, passing each value to a function
def square_number(number):
    return number ** 2

squared_numbers = [square_number(num) for num in numbers]

# create a function that conditionally returns a True/False value
def check_even(number):
    return number % 2 == 0

# call the function and use the result in an if statement
if check_even(100):
    print("The number is even")
