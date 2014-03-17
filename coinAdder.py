#Olivia Millard - Lab 3a
#This program will add up a user's coins based off of their input.

#Short welcome message.
print("Hello. This program will add up all of your change!\nCool! Let's get started.\n")

"""
This function, first, take input from the user asking how many coins they have. Next, it takes input for what type of coin they have.
And last, it adds up the total coins depending on their value
### Variables ###
value = how much the individual coin is worth.
coinNumber = which coin of theirs they are inputting the type for (penny, nickel, dime, quarter).
total = the total amount of their coins added together.
dollarAmount = the quotient from doing integer division on the total.
centsAmount = the remainder from using modulus on the total.
"""
def addUpCoins():
    value = 0
    coinNumber = 1
    total = 0
    numOfCoins = int(input("How many coins do you have? "))
    while coinNumber <= numOfCoins:
        coin = str(input("What is coin #" +str(coinNumber)+ "? (q for quarter, d for dime, n for nickel, p for penny): "))
        coinNumber = coinNumber + 1
        if coin == "p":
            value = 0.01
            total = total + value
        elif coin == "n":
            value = 0.05
            total = total + value
        elif coin == "d":
            value = 0.10
            total = total + value
        elif coin == "q":
            value = 0.25
            total = total + value
    dollarAmount = total // 100
    centsAmount = total % 100
    print("\n")
    print("Whoa... you have a lot of monies!\n" +str(dollarAmount)+ " dollars and " +str(centsAmount)+ " cents if we're being exact.")
    print("Now go buy yourself something nice.")
addUpCoins()    
