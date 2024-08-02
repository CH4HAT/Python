


counter = 0
print(counter)
counter = 0+1
print(counter)
counter+=1
print(counter)
"""
Data types 
int(whole number)
float(decimal numbers)
str(string) - any sequence of character inside of single or double quotes 
bool(boolean) - True/False
None(empty)

type() - will return current datatype of the function

str.isdigit()  returns weather a value can be consisdered or converted to a numeric value 
"""

"""
strings:
(sequence types in python)
think of string as list of individual characters 
len() - used to find length of a string like we can find how many characters are in there 
lets say cource= 'ACIT 1515'
print(len(course)) and it should print 9

print(f'the length of dtring "acit 1515" if {len(course)}')

index into the string   using [] 
print(course[1])   - everything starts from zero 0 
will print C from ACIT 1515

you can also do negative indexes like print (course[-1])     -1 is last char and -1 is second last 

use the 'in' operator to check if char or strings inside of a larger string 
print("CIT" in course)    its gonna return true or false
print ("full" not in course )    it"ll print true again cos its not in course string


conversion of datatypes 
 eg
  coursenumber = 1515
  print(coursenumber, type(coursenumber))       will give 1515 <class'int'>

  coursenumberstring = str(coursenumber)
  print(coursenumberstring, type(coursenumberstring))   will give 1515 <class'string'>


  print(int(bcit))    will crash the script


"""
print("bcit".isdigit())