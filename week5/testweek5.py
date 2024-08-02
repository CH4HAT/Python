from getpass import getpass
# function definition
def test():
    print("inside the test function")


print("oustide of the function")

test()

def add():
    print(2+2)

add()
def add2(lhs,rhs):
    print(lhs+rhs)

add2(2000, 468732281)

lhs=10
rhs=20
def substract(lhs, rhs, *args):
    print(lhs- rhs)
    print(args)

substract(10,20,48,58,58)

def grade(course="ACIT1515", mark = 50):
    print(course, mark)
    
    


grade()
grade("Acit 1630", 30)

def f(param1, param2, **kwargs):
    print(param1, param2)
    print(kwargs)


f(param1 = 1, param2 = 2, c =3, d = 4 , e= 5)


def double(num):
    return num*2
    print("after return value?")

result = double(256)
print(result)


double(512)

def has_uppercase(password:str) -> bool:
    for character in password:
     if character.isupper():
         return True
     
    return False   


# if it has at least one uppercase character:
# return true
# else
# return False 


"""
getpass - smilar to input and hide the charater that user types in 

"""

response = getpass("enter a password")
print(response)


"""any function 




'"""

def has_uppercase(password:str) -> bool:
    return True if any(character.isupper()for character in password) else False

