# author: Adam O'Brien
# date: 10/06/2018
# description: a simple dice throw simulation
# my first python program

# features to improve program
# give user a tally / result sheet of the numbers they rolled

# import required modules
import random
import math

# get amount of rolls the user wants to roll
rolls = input("How many rolls do you want to roll?  ")

# check if the user input contains only numbers
if rolls.isnumeric():
    # convert rolls to integer
    rolls = int(rolls)

# check that the user input is valid
if type(rolls) == int and rolls > 0:
    c = 0
    # keep rolling dice until amount of rolls is reached
    while rolls > c:
        # randomly choose dice number
        roll = random.randint(1,6)
        # increment roll counter
        c+=1
        # print roll result to the console
        print("You rolled a " + str(roll) + "!")
else:
    # inform user about invalid input
    print("Input must be a number (0-9 only)")