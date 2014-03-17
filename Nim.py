#Olivia Millard - Homework 2
#This program will generate a game in which a human player plays against a computer user.
#The game consists of the two opponents choosing chips from two piles.
#Whoever chooses the last chip wins.

#Short welcome message.
print("Hello and welcome! \nToday you are in for a fun, engaging game playing experience.\nIt requires little to no logic, skill, or effort.\nWhoever draws the last chip(s) wins-- Good luck!")

#Whitespace.
print("\n")

"""Variable"""
## numOfChips: A prompt for the number of chips the "human player" would like to play with.
##### Function that will initialize the game based off of user input. ####
def initGame():
    numOfChips = int(input("How many chips would you like to play with today? \nPlease enter an integer greater than zero: "))
    while numOfChips <= 0:
        print("\nRe-enter your selection. Make sure it is greater than zero.\n")
        numOfChips = int(input("How many chips would you like to play with today? \nPlease enter an integer greater than zero: "))
    displayPiles(numOfChips)


"""Variables and Their Assignments"""
## Pile1, Pile2: The user-inputted value from initGame().

## intDivisionP1, intDivisionP2: The value of the integer division done on the total number of chips from Pile1 or Pile2.
    
## P1GroupedIntDiv, P2GroupedIntDiv: The chips grouped into five's based off of the quotient from intDivisionP1/intDivisionP2.
    
## remainderP1, remainderP2: The remainder from using the modulus operand on Pile1/Pile2.
    
## P1GroupedRemainder, P2GroupedRemainder: The remaining chips (the integer from remainderP1/P2, but in "chip form"). 
    
## Pile1_Grouped, Pile2_Grouped: These two variables combine the chips stored from the integer division operations and the modulus operations into a single string.

#### This function will group the piles into groups of 5 and display them to the screen. ####
def displayPiles(numOfChips):
    O = ("O")
    Pile1 = int(numOfChips)
    Pile2 = int(numOfChips)
    intDivisionP1 = (Pile1 // 5)
    P1GroupedIntDiv = (((O * 5) + " ") * (intDivisionP1))
    remainderP1 = (Pile1 % 5)
    P1GroupedRemainder = (O * remainderP1)
    intDivisionP2 = (Pile2 // 5)
    P2GroupedIntDiv = (((O * 5) + " ") * (intDivisionP2))
    remainderP2 = (Pile2 % 5)
    P2GroupedRemainder = (O * remainderP2)
    Pile1_Grouped = str(P1GroupedIntDiv) + str(P1GroupedRemainder)
    Pile2_Grouped = str(P2GroupedIntDiv) + str(P2GroupedRemainder)
    print("\nYou will go first. \nYour piles are shown below. \n")
    print("Pile 1: " + str(Pile1_Grouped))
    print("Pile 2: " + str(Pile2_Grouped))
    getHumanMove(Pile1, Pile2)


"""Variables and Their Assignments"""
## PileChoice: A prompt for the "human player's" choice of pile they want chips to be taken from.

## HumanMoveChips: A prompt for the "human player" to choose how many chips they want to take from PileChoice.

#### This function will ask for the human player's first move (which pile they want to take from and how many chips they want to take). ####
def getHumanMove(Pile1, Pile2):
    PileChoice = str(input("\nWhich pile would you like to remove chips from?\nEnter 1 for Pile One or 2 for Pile Two: "))
    if PileChoice == ("1"):
        PileChoice == Pile1
    elif PileChoice == ("2"):
        PileChoice == Pile2
    else:
        print("Please enter 1 or 2.")
        PileChoice = str(input("\nWhich pile would you like to remove chips from?\nEnter 1 for Pile One or 2 for Pile Two: "))
    HumanMoveChips = int(input("How many chips would you like to remove from Pile " +str(PileChoice)+ "? \nPlease choose an integer greater than zero: "))
    if HumanMoveChips <= 0:
        print("\nPlease choose a different move. Your choice must be greater than zero.\n")
        int(input("How many chips would you like to remove from Pile " +str(PileChoice)+ "? \nPlease choose an integer greater than zero: "))
    if HumanMoveChips >= Pile1 or HumanMoveChips >= Pile2:
        print("\nPlease choose an integer that is LESS than the total number of chips in Pile " +str(PileChoice)+ "!\n")
        int(input("How many chips would you like to remove from Pile " +str(PileChoice)+ "? \nPlease choose an integer greater than zero. \nMake sure that it is less than " +str(Pile1)+ ": "))
    computerMove(PileChoice, HumanMoveChips)
    updatePiles(Pile1, Pile2, PileChoice, HumanMoveChips)

"""Variables and Their Assignments"""
## computerPileChoice: This is the pile the "human player" didn't choose.
## ComputerMoveChips: This value is equal to the amount of chips the player chose in getHumanMove().

#### This function will state the computer's move. ####
def computerMove(PileChoice, HumanMoveChips):
    print("Hmm... interesting choices...")
    print("\nIt is now my turn.")
    if PileChoice == ("1"):
        computerPileChoice = ("2")
    elif PileChoice == ("2"):
        computerPileChoice = ("1")
    ComputerMoveChips = HumanMoveChips
    print("I will take " +str(ComputerMoveChips)+ " chips from Pile " +str(computerPileChoice)+ ".\n")
    
"""Variables and Their Assignments"""
## new_Pile1, new_Pile2: The updated piles with values that are the difference between the original Pile1/Pile2 values and the HumanMoveChips value.
## All other variables are from the displayPiles() function.

#### This function will update the piles based off of the user-inputs from getHumanMove(). ####
def updatePiles(Pile1, Pile2, PileChoice, HumanMoveChips):
    O = "O"
    new_Pile1 = Pile1
    new_Pile2 = Pile2 
    ComputerMoveChips = HumanMoveChips
    if PileChoice == ("1"):
        new_Pile1 = new_Pile1 - HumanMoveChips
        new_Pile2 = new_Pile2 - ComputerMoveChips
        intDivisionP1 = (new_Pile1 // 5)
        P1GroupedIntDiv = (((O * 5) + " ") * (intDivisionP1))
        remainderP1 = (new_Pile1 % 5)
        P1GroupedRemainder = (O * remainderP1)
        Pile1_Grouped = str(P1GroupedIntDiv) + str(P1GroupedRemainder)
        intDivisionP2 = (new_Pile2 // 5)
        P2GroupedIntDiv = (((O * 5) + " ") * (intDivisionP2))
        remainderP2 = (new_Pile2 % 5)
        P2GroupedRemainder = (O * remainderP2)
        Pile2_Grouped = str(P2GroupedIntDiv) + str(P2GroupedRemainder)
        print("\nThese are what the piles now look like:")
        print("Pile 1: " + str(Pile1_Grouped))
        print("Pile 2: " + str(Pile2_Grouped))
    if PileChoice == ("2"):
        new_Pile2 = new_Pile2 - HumanMoveChips
        new_Pile1 = new_Pile1 - ComputerMoveChips
        intDivisionP1 = (new_Pile1 // 5)
        P1GroupedIntDiv = (((O * 5) + " ") * (intDivisionP1))
        remainderP1 = (new_Pile1 % 5)
        P1GroupedRemainder = (O * remainderP1)
        Pile1_Grouped = str(P1GroupedIntDiv) + str(P1GroupedRemainder)
        intDivisionP2 = (new_Pile2 // 5)
        P2GroupedIntDiv = (((O * 5) + " ") * (intDivisionP2))
        remainderP2 = (new_Pile2 % 5)
        P2GroupedRemainder = (O * remainderP2)
        Pile2_Grouped = str(P2GroupedIntDiv) + str(P2GroupedRemainder)
        print("\nThese are what the piles now look like:")
        print("Pile 1: " + str(Pile1_Grouped))
        print("Pile 2: " + str(Pile2_Grouped))
    updatePiles_after_RoundOne(new_Pile1, new_Pile2, PileChoice, HumanMoveChips)

#### This function is a combination of getHumanMove(), computerMove(), and updatePiles(). ####
#### It runs until there are zero chips left (or while there are more than 0 chips in play). # 
def updatePiles_after_RoundOne(new_Pile1, new_Pile2, PileChoice, HumanMoveChips):
    while new_Pile1 > 0 and new_Pile2 > 0:
        O = "O"
        PileChoice = str(input("Which pile would you like to choose from now? \nEnter 1 for Pile One, 2 for Pile Two: "))
        HumanMoveChips = int(input("How many chips would you like to remove now? \nSame rules as before ( >0 ): "))
        print("\nIt is now my turn.")
        if PileChoice == ("1"):
            computerPileChoice = ("2")
        elif PileChoice == ("2"):
            computerPileChoice = ("1")
        ComputerMoveChips = HumanMoveChips
        print("I will take " +str(ComputerMoveChips)+ " chips from Pile " +str(computerPileChoice)+ ".\n")
        if PileChoice == ("1"):
            new_Pile1 = new_Pile1 - HumanMoveChips
            new_Pile2 = new_Pile2 - ComputerMoveChips
            intDivisionP1 = (new_Pile1 // 5)
            P1GroupedIntDiv = (((O * 5) + " ") * (intDivisionP1))
            remainderP1 = (new_Pile1 % 5)
            P1GroupedRemainder = (O * remainderP1)
            Pile1_Grouped = str(P1GroupedIntDiv) + str(P1GroupedRemainder)
            intDivisionP2 = (new_Pile2 // 5)
            P2GroupedIntDiv = (((O * 5) + " ") * (intDivisionP2))
            remainderP2 = (new_Pile2 % 5)
            P2GroupedRemainder = (O * remainderP2)
            Pile2_Grouped = str(P2GroupedIntDiv) + str(P2GroupedRemainder)
            print("\nThese are what the piles now look like:")
            print("Pile 1: " + str(Pile1_Grouped))
            print("Pile 2: " + str(Pile2_Grouped))
        if PileChoice == ("2"):
            new_Pile2 = new_Pile2 - HumanMoveChips
            new_Pile1 = new_Pile1 - ComputerMoveChips
            intDivisionP1 = (new_Pile1 // 5)
            P1GroupedIntDiv = (((O * 5) + " ") * (intDivisionP1))
            remainderP1 = (new_Pile1 % 5)
            P1GroupedRemainder = (O * remainderP1)
            Pile1_Grouped = str(P1GroupedIntDiv) + str(P1GroupedRemainder)
            intDivisionP2 = (new_Pile2 // 5)
            P2GroupedIntDiv = (((O * 5) + " ") * (intDivisionP2))
            remainderP2 = (new_Pile2 % 5)
            P2GroupedRemainder = (O * remainderP2)
            Pile2_Grouped = str(P2GroupedIntDiv) + str(P2GroupedRemainder)
            print("\nThese are what the piles now look like:")
            print("Pile 1: " + str(Pile1_Grouped))
            print("Pile 2: " + str(Pile2_Grouped))
        if new_Pile1 == 0 and new_Pile2 == 0:
            endGame()

#### Short farewell message. ####     
def endGame():
    print("\nLooks like I win! Hope you have better luck next time!")

#### Initializing the game. ####       
initGame()
