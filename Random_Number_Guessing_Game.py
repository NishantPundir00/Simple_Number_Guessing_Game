# Random Number Guessing game using python

import random

while True:
    upper_num = input("Type a number for Upper Bound to Start Game : ") # Upper Bound
    
    if upper_num.isdigit():
        print("__________________________________________________________\n")
        print("Lets Start Game")
        upper_num = int(upper_num)
        break
    else:
        print("__________________________________________________________\n")
        print("Invalid Input Try Again...")

Secret = random.randint(1,upper_num)
count = 1
guess = None

while guess != Secret:
    print("Type 0 for Exit")
    guess = input(f"Guess a Number between 1 to {upper_num} : ")

    # Check Valid Input
    if guess.isdigit():
        guess = int(guess)
        if guess <= upper_num and guess >= 0:
            pass
        else:
            print("__________________________________________________________\n")
            print("Invalid Input Try Again...")
            continue

    else:
        print("__________________________________________________________\n")
        print("Invalid Input Try Again...")
        continue
    
    # For Exit
    if guess == 0:
        break
    
    # Compare Numbers
    if guess == Secret:
        print("__________________________________________________________\n")
        print("Congratulations!! you got it")
        print("__________________________________________________________\n")
    else:
        print("__________________________________________________________\n")
        print("Try Again...")
        count+=1

# Guess Count
print(f"It took you {count} Guesses!")