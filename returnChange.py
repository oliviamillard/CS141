#Olivia Millard - Lab 3b
#This program will tell a user how many quarters, dimes, nickels, and/or pennies to give out when giving change.

#This function will ask for a user-inputted integer that correlates to how much change they need to give.
#It will then calculate the amount of quarters, dimes, nickels, and/or pennies they need to return.
"""Variables"""
#totalChange = the amount of change the user has.
#remainingChange = the change remaining after the modulus operand is used on the total change.
#print**coin** = the number of an individual coin needed in string format.


def giveChange():
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    totalChange = int(input("How much change do you have to give? (in cents): "))
    if totalChange >= 25:
        quarters = totalChange // 25
        remainingChange = totalChange % 25
    if totalChange < 25 and totalChange >= 10:
        dimes = totalChange // 10
        remainingChange = totalChange % 10
    elif totalChange >= 10 and remainingChange < 25:
        dimes = remainingChange // 10
        remainingChange = remainingChange % 10
    if totalChange < 10 and totalChange >= 5:
        nickels = totalChange // 5
        remainingChange = totalChange % 5
    elif totalChange >= 5 and remainingChange < 10:
        nickels = remainingChange // 5
        remainingChange = remainingChange % 5
    if totalChange < 5 and totalChange >= 1:
        pennies = totalChange // 1
        remainingChange = totalChange % 1
    elif totalChange >= 1 and remainingChange < 5:
        pennies = remainingChange // 1
        remainingChange = totalChange % 1
    printQuarters = (str(quarters) + " quarter(s) ")
    if printQuarters == ("0" + " quarter(s) "):
        printQuarters = ("")
    printDimes = (str(dimes) + " dime(s) ")
    if printDimes == ("0" + " dime(s) "):
        printDimes = ("")
    printNickels = (str(nickels) + " nickel(s) ")
    if printNickels == ("0" + " nickel(s) "):
        printNickels = ("")
    printPennies = (str(pennies) + " pennies/penny ")
    if printPennies == ("0" + " pennies/penny "):
        printPennies = ("")
    print("You should give: " +printQuarters+printDimes+printNickels+printPennies)
giveChange()
