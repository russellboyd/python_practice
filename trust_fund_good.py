#Trust Fund Buddy - Good
#Demonstrates type conversion
print(
    """
         Trust Fund Buddy - Totals your month spending so that your trust fund doesn't run out (and you're forced to get a real job).

         Please enter the requested, monthly costs. Since you're rich, ignore pennies and use only dollar amounts.

"""
    )

car = input("Lambo Tune-Ups: ")
car = int(car)
rent = int(input("Manhattan Apartment: "))
jet = int(input("Private Jet Rental: "))
gifts = int(input("Gifts: "))
food = int(input("Dining Out: "))
staff = int(input("Staff(butlers, chef, driver, assistant): "))
guru = int(input("Personal guru and coach: "))
games = int(input("Computer games: "))

total = car + rent + jet + gifts + food + staff + guru + games

print("\nGrand Total: ", total)

input("\n\nPress the enter key to exit.")

                 
