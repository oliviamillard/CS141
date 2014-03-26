#Olivia Millard - Homework 1a
#This program will determine the legality of one's ability to drink in their state or in the entire US.

#Welcome message.
print("Hi there. \nUse this tool to find out if you can drink alcohol legally in your state.")
print("You will be asked to enter your state of residence, birth year, and birth month.")
print("If you are inquiring about another state's drinking laws, you may do so.")
print("That's enough talking for now... let's get started!\n\n")

"""Variables"""
#WA_resident = input to determine if one is a WA resident or not.
#state_name = user's state of residence or state of inquiry.
#birth_year = user's year of birth.
#birth_month = user's month of birth.

def main():
    
    ## This portion of the program collects user-input ##
    WA_resident = str(input("Are you inquiring about Washington laws? Enter YES or NO: "))

    ## Section of code to determine non-WA residents' ability to consume alcohol legally. ##
    ## Some states have exceptions to the "21 and over" law. ##
    if WA_resident == "NO":
    
        ##Getting birth year/month from the user##
        birth_year = int(input("What is your birth year? (e.g. 1975): "))
        birth_month = int(input("What is your birth month? (e.g. 4 for April): "))
        if birth_month == 0 or birth_month > 12:
            print("Please enter in a valid month. ")
            birth_month = int(input("What is your birth month? (e.g. 4 for April): "))
        
        ##California has laws that allow people <21 to drink a small amount of alcohol for religious purposes##
        california = str(input("Are you inquiring about California? Enter YES or NO: "))
        if california == "YES":
            state_name = "California"
            exception = str(input("Are you consuming alcohol for RELIGIOUS PURPOSES?\n(It must be a SMALL amount!) Enter YES or NO: "))
            if exception == "NO":
                if birth_year == 1993 and birth_month == 3 or birth_year <= 1993 and birth_month <= 3:
                    print("\nIt doesn't matter why you're consuming alcohol!\nYou can drink in the entire United States!\nCongrats!")
                if birth_year >= 1993 and birth_month > 3 or birth_year > 1993:
                    print("\nSorry, you won't be able to consume any alcohol... anywhere...")
            if exception == "YES":
                if birth_year == 1993 and birth_month == 3 or birth_year <= 1993 and birth_month <= 3:
                    print("\nIt doesn't matter why you're consuming alcohol!\nYou can drink in the entire United States!\nCongrats!")
                if birth_year >= 1993 and birth_month > 3 or birth_year > 1993:
                    print("\nYou can consume alcohol in this way in the state of California.\nJust don't do it anywhere else.\nBecause that'd be illegal...")
                
        if california == "NO":
            ##Kansas allows people <21 to drink on one's own property##
            kansas = str(input("Are you inquiring about Kansas? Enter YES or NO: "))
            if kansas == "NO":
                ##In Georgia and Wisconsin people <21 can drink if their parent(s)/legal guardian(s) or spouse is present##
                georgia_wisconsin = str(input("Are you inquiring about Georgia or Wisconsin? Enter YES or NO: "))
                if georgia_wisconsin == "YES":
                    exception_2 = str(input("Are your parents, legal guardians, and/or spouse present? Enter YES or NO: "))
                    if exception_2 == "YES":
                        state_name = "Georgia and Wisconsin"
                        if birth_year == 1993 and birth_month == 3 or birth_year <= 1993 and birth_month <= 3:
                            print("\nYou can actively enjoy your alcohol in the ENTIRE United States!")
                            print("Congrats on your accomplishment!")
                        if birth_year >= 1993 and birth_month > 3 or birth_year > 1993:
                            print("\nCool-- you can legally consume alcohol in Wisconsin and Georgia.\nBut not in any other US state.\nSorry :(")
                    if exception_2 == "NO":
                        if birth_year == 1993 and birth_month == 3 or birth_year <= 1993 and birth_month <= 3:
                            print("\nYou can actively enjoy your alcohol in the ENTIRE United States!")
                            print("Congrats on your accomplishment!")
                        if birth_year >= 1993 and birth_month > 3 or birth_year > 1993:
                            print("\nI am sorry, you cannot legally consume alcohol in " +str(state_name)+ ".")
                            print("Be patient and give it some time.")
                            print("Sorry :(")
                        
                if georgia_wisconsin == "NO":
                    ##This block of code is solely to determine the user's eligibity in remaining states##
                    state_name = str(input("What state are you inquiring about? "))
                    if birth_year == 1993 and birth_month == 3 or birth_year <= 1993 and birth_month <= 3:
                        print("\nYou can actively enjoy your alcohol in the ENTIRE United States!")
                        print("Congrats on your accomplishment!")
                    if birth_year >= 1993 and birth_month > 3 or birth_year > 1993:
                        print("\nI am sorry, you cannot legally consume alcohol in " +str(state_name)+ ".")
                        print("Be patient and give it some time.")
                        print("nSorry :(")

            if kansas == "YES":
                exception_3 = str(input("Will you be consuming alcohol on your own property? Enter YES or NO: "))
                if exception_3 == "YES":
                    if birth_year == 1993 and birth_month == 3 or birth_year <= 1993 and birth_month <= 3:
                        print("\nIt doesn't matter why you're consuming alcohol!\nYou can drink in the entire United States!\nCongrats!")
                    if birth_year >= 1993 and birth_month > 3 or birth_year > 1993:
                        print("\nYou can drink alcohol as long as it's on your personal property.\nBut only in Kansas, it's illegal for you in all other states.")
                    
    ## This portion of the program determines legality based upon birth year/month for WA. ##
    if WA_resident == "YES":
        state_name = "Washington"
        birth_year = int(input("What is your birth year? (e.g. 1975): "))
        birth_month = int(input("What is your birth month? (e.g. 4 for April): "))
        if birth_month == 0 or birth_month > 12:
            print("Please enter in a valid month. ")
            birth_month = int(input("What is your birth month? (e.g. 4 for April): "))
        if birth_year == 1993 and birth_month == 3 or birth_year <= 1993 and birth_month <= 3:
            print("\nYou can actively enjoy your alcohol in the ENTIRE United States!")
            print("Congrats on your accomplishment!")
        if birth_year >= 1993 and birth_month > 3 or birth_year > 1993:
            print("\nI am sorry, you cannot legally consume alcohol in " +str(state_name)+ ".")
            print("Be patient and give it some time.")
            print("Sorry :(")
main()

## Short function to end the program ##
def endTool():
    print("\nThank you for using this tool!")
    input("Press enter to quit... goodbye.")
    
endTool()


 
