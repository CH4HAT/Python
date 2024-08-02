def test():
    print("something")

def again():
    print("again")

def getint(prompt: str) -> int: 
 keep_playing = True
 while keep_playing:
    num_guesses = input("please enter the number of guesses: ")
    if num_guesses.isdigit():
        num_guesses = int(num_guesses)
    max_number = input("please enter maximum value to be stored: ")
    if max_number.isdigit():
        max_number = int(max_number)


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
        guesses_correctly = True
        break