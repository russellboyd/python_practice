#Guess My Number
#
#The computer picks a random number between 1 and 100
#The player tried to guess it and the computer lets
#the player know if the guess is too high, too low
#or right on the money

import random

print("\tWelcome to 'Guess My Number' !")
print("\nI'm thinking of a number nbetween 1 and 100.")
print("You have 10 tries to figure it out.\n")

#set the initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1;

#guessing loop
while tries != 11:
    if guess > the_number:
        print("Lower...")
    elif guess < the_number:
        print("Higher...")
    elif guess == the_number:
        print("You guessed it! The number was ", the_number)
        print("And it only took you", tries, "tries!")
        break
    elif tries == 10 and guess != number:
        print("This is my message chastising you for failing with what was your charge.")
        break
    
    guess = int(input("Take a guess:  "))
    tries += 1

input("\n\nPress the enter key to exit.")
