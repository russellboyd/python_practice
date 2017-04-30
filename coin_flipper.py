#coin_flipper
#Write a program that flips a coin 100 times and then tells you the number of the heads and tails.
#Program plan 1/10/17
#import random lib
#define variables heads and tails = 0
#write for loop from 1 to 100, with rand ints being generated between 1 and 2.
#if 1 then heads, elif 2 then tails

import random

heads = 0
tails = 0
iterator = 0

while iterator != 100:
    rand_number = random.randint(1, 2)
    if rand_number == 1:
        heads += 1
    elif rand_number == 2:
        tails += 1
    iterator += 1


print("Total heads = ", heads)
print("Total tails = ", tails)
