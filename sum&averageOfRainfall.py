#Olivia Millard - Homework 1b
#This program will collect rainfall data from a user and find the sum and average of the rainfall in that time period.

import math

##Welcome Message##
print("Hey there. I heard you've been collecting some rainfall data!\nInput your data and I'll find out how much total rainfall you've collected.")
print("I'll then take the average of that! Let's go!")
print("\n")

total_days = float(input("How many days of data collection do you have?\nEnter an integer: "))
if total_days > 1:
    total_days_string = str(total_days) + " days "
else:
    total_days_string = str(total_days) + " day "
print("\n")

n = 1
total = 0
while n <= total_days:
    individual_days = (float(input("Rainfall for Day " +str(n)+ " (in inches, please!): ")))
    n = n + 1
    total = individual_days + total
average = (total)/(total_days)
print("The total amount of rain that fell in " +str(total_days_string)+ "was: " +str(total)+ " inches.")
print("The average daily rainfall for this time period is: " +str(float(average))+ " inches.")

##Ending message##
print("\n")
print("I hope you enjoyed your experiment!")








