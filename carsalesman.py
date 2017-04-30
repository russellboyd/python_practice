#Chapter 2
#Challenge 4
#Write a Car Salesman program where the user enters the base price of a car.
#The program should add on extra fees such as tax, license, dealer prep, and destination charge.
#The other fees ahould be set values.  Display the actual price of the car once all the extras are applied.

basePrice = int(input("What is the base price of the car? "))
taxCost = basePrice * .20
licenseCost = basePrice * .02
dealerPrepCost = 1000
destinationChargeCost = 200

totalCarCost = basePrice + taxCost + licenseCost + dealerPrepCost + destinationChargeCost

print("The total cost of the car you want is ", totalCarCost)
