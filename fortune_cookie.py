#Fortune_Cookie

#program plan 1/10/17
#import
#generate the random number between one and five and store it into a variable
#write the five unique fortunes
#write the if else if logic matching random numbers to the fortunes
#press enter to continue

import random

the_number = random.randint(1, 5)
print(the_number)

if the_number == 1:
    print("You really should roll again.")
elif the_number == 2:
    print("Why are you looking for a computer to tell you your future?")
elif the_number == 3:
    print("Go pound sand.")
elif the_number == 4:
    print("Have a glass of water.")
elif the_number == 5:
    print("You will be happy if you so choose to be.")

input("\n\n Press the enter key to exit.")
    
