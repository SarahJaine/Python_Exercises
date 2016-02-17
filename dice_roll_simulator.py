##Dice Rolling Simulator from http://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
##The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice.
##When the program runs, it will randomly choose a number between 1 and 6.

import random

roll_prompt = raw_input("Would you like to roll the die? ")

if roll_prompt.upper() == "YES":
        number_prompt = int(raw_input("How many times would you like to roll? "))
        roll_result=[]
        while number_prompt>0:
                dice = int(random.randrange(1,7))
                roll_result.append(dice)
                number_prompt = number_prompt-1
        print "Excellent choice!\nHere are your results: {}".format(roll_result)

elif roll_prompt.upper() == "NO":
        print "Fine, fine- wake me up when you actually need something."
else:
        print """Sorry, I didn't get that.
Please run the program again and answer the first question with 'yes' or 'no.'"""
