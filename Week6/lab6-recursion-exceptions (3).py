"""
    ACIT 1515 - Lab 6

    For Lab 6 you will be using recursion and try/except to create a script that simulates the folding of objects, and calculating the heights of those folded objects.

    The program should prompt the user for two values, the height of the object to be folded, and the number of folds. It should then calculate the height of the object after being folded, compare that height to some pre-defined values, and print a message to the user.

    For example:

        Assume the user wants to fold a piece of paper that is 0.1mm tall, 8 times

        Your script uses recursion to calculate that a sheet of 0.1mm paper folded 8 times is 25.6mm tall

        Given an average book, with a width of 2cm (20mm), your program outputs
            "Your 0.1mm tall object, folded 5 times, is 3.2mm tall. That is taller than an average book!"
    
    Additionally, you must use try/except/else blocks to ensure that:

        1. Values entered by the user are numeric, and non-numeric (or blank) values do not crash the scripts
        2. The program ends gracefully, even when forcibly ended using ctrl-c

"""
import sys

heightsInKilometers = [
    { 'name': 'the average book', 'height': 0.00002  },
    { 'name': 'a 32 inch TV', 'height': 0.00081 },
    { 'name': 'the average person', 'height': 0.00175},
    { 'name': 'the tallest human being that ever lived', 'height': 0.00272 },
    { 'name': 'a one story building', 'height': 0.003 },
    { 'name': 'the average giraffe', 'height': 0.0048 },
    { 'name': 'a ten story office building', 'height': 0.03 },
    { 'name': 'the tallest building in vancouver', 'height': 0.201 },
    { 'name': 'the tallest building in canada', 'height': 0.553 },
    { 'name': 'the tallest building in the world', 'height': 0.828 },
    { 'name': 'the top of mount everest', 'height': 8.848 },
    { 'name': 'the maximum height a commercial plane can fly', 'height': 12.8 },
    { 'name': 'the highest a plane has ever flown', 'height': 37.64 },
    { 'name': 'the karman line - the boundary between earth and space', 'height': 100 },
    { 'name': 'the distance to the international space station', 'height': 408 },
    { 'name': 'the distance to the moon', 'height': 384400 },
    { 'name': 'the distance to the sun', 'height': 148000000 }
]

def compare(height):
    for i in range(len(heightsInKilometers) - 1):
        if height >= heightsInKilometers[i]["height"] and height <= heightsInKilometers[i+1]["height"]:
            return heightsInKilometers[i]
    
    return None

"""
   In the fold function, return the height if times == 0 (the 'base case'),
   otherwise return a recursive call to the fold function, passing in height + height and times - 1
   as the arguments 
"""
def fold(height, times):
    print(height,times)
    if times == 0:
        return height
    else:
        return fold(height + height, times-1)
    
"""
    In the main function, use try, except, and else to get two values from the user:
        h - the height of the object (float, not int!) in mm
        n - the number of folds (int)

    If an exception is thrown, print a message saying "Please enter numeric values only"

    If no exception is thrown (i.e. in the 'else' block), do the following:
        - call the fold function, divide the returned value by 1000000 (one million) to convert to km, 
            and store this value in a variable named resKm

        - call the compare function, passing in the value from the previous step, and store this value
            in a variable named tallerObject

        - if tallerObject is None, print the following string:
            f"Your {h}mm tall object folded {n} times is {resKm:.7f}km, shorter than the average book!"
          else, print the string:
            f"Your {h}mm tall object folded {n} times is {resKm:.7f}km, taller than {tallerObject['name']}!"
        
        - regardless of output, call sys.exit() to stop the script
"""
def main():
    try:
        h = float(input("Please enter the height of the object: "))
        n = int(input("Please enter number of folds: "))
    except ValueError as e:
        print("please enter numeric values: ",e )
    else:
        reskm = fold(h,n) / 1000000
        tallerobject = compare(reskm)

        if tallerobject is None:
            print(f"Your {h}mm tall object folded {n} times is {reskm:.7f}km, shorter than the average book!")
                  
        else:
          print( f"Your {h}mm tall object folded {n} times is {reskm:.7f}km, taller than {tallerobject['name']}!")
        print(tallerobject["name"])


"""
    Use try and except to prevent ctrl-c from outputting an error to the console.

    To figure out *which* exception to catch, first run the program and type ctrl-c, then examine
    the output in the terminal.

    The code inside this section should look something like:

        try:
            main()
        except ???:
            sys.exit()

    where ??? is the error type shown to you in the terminal after typing ctrl-c to prematurely stop the script
"""
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()