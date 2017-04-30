#Chapter 2
#Challenge 3
#Write a Tipper program where the user enters a restaurant bill total.
#The program should then display two amounts : a 15 percent tip and a 20 percent tip.

billTotal = int(input("What is the restaurant bill total?: "))

fifteenPercentTip = billTotal * 0.15
twentyPercentTip = billTotal * 0.20

print("15% Tip = ", fifteenPercentTip)
print("20% Tip = ", twentyPercentTip)

input("\n\nPress the enter key to exit.")
