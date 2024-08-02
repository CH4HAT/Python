'''# importing a file from another file
import lib
lib.test()
lib.again()

# importing random
import random
num =  random.randint(1,10) #will return numnber betwwn 0,10 inclusive
print(num)

"""conditional if statements"""
choice = input("please enter a number between 1 and 10: ")

# string.isdigit() returns True/False if string is converted to a number 
if choice.isdigit():
    choice = int(choice)
    if choice < 1 and choice > 10:
        print("print avalid number between 1 and 10")

x = 10        
if x == 10:
    print("x is equal to ten")
    # pass #the pass keyword can be used when you temporirily enpty the block 
else:
    # pass
    print("x is not equal to ten")


    """
    Rules of if statement:
    A section of if statements has to start with single mandatory ifs
    -followed by multiple elif statements 
    -follwed by single optional else statement

    if:
    else:
    

    if:
    elif:
    elif:
    elif:
    
    """"""
    Comparison operators
    >, >=, <, <=, ==,!=

    logical operators
    and
    or
    not

    """
    """
    True and True is True, otherwise false
    False and False is False otherwise True
    """

    """
    ternary if statements

    """
    age = 16
    candrive = "yes" if age>=16 else"No"
# using multiple conditions in single statements 
    halicence = True
    hasbuspass = True
    Bustrike = False
    if ((age >= 16 and halicence) or hasbuspass) and not Bustrike:
        print("you can get to school")
'''
"""
loops

""""""
while True:
    # infinte loop unless you break 
    print("inside the while loop")
    break

counter = 0 
while counter <=10:
    counter+=1
    if counter == 5:
        continue #send the script back on the top
    print(counter)

""""""
For loops
"""
numbers = [1,2,3,4,5,6,7,8,]

for numbers in numbers:
    #number is a loop variable we declare and it can be named whatever you like 
    print(numbers)

r = range(1,10) #will generate number between 1-9  (1>= range <10)
r = range(0,10,2) #will give with an increment of 2 1,3,5,7,9

for i in range (1,10):
    print (i)
print(r)


schools = ["bcit", "sfu", "ubc"]

for i in range(1,3):
    print(schools[i]) #will give bcit and sfu

for i in range(3):  #it means 0,1,2
    print(schools[i])

for i in range(len(schools)):
    print(schools[i])



"""
 enumerate()  it will tale a list and it will give us back tuples, the tuples ill contain a) and value of b) index
 """   

cities = ["urrey", "vancouver","richmond"]

for index, value in enumerate(cities):
    print(f"{index+1}.{value}")
   


