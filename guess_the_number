##Guess the Number from http://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
##The Goal: Similar to the first project, this project also uses the random module in Python.
##The program will first randomly generate a number unknown to the user. The user needs to guess what that number is.
##If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low).
##If the user guesses correctly, a positive indication should appear.

import random

correct_number = random.randrange(1,101)

def even_or_odd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"

guess_history = []
adjective = ["splendid", "bewitching", "crackerjack", "peachy", "super-duper", "sensational"]
noun = ["smarty-pants", "expert", "genius", "hot tamale", "virtuoso", "wiz", "boss"]

print "Let's play a game!\nI will give you 5 trys to guess the number I'm thinking of. If you guess the number correctly, I will shower you with praise!"

while len(guess_history) < 5:
    guess = raw_input("\nGuess a number between 1 and 100: ")
    guess_history.append(guess)
    try:
        guess=int(guess)
        if guess > 100 or guess < 1:
            print "Hey there, I need a number between 1 and 100.  Try again."
        else:
            if guess == correct_number:
                print "Congratulations, {0} is the number I was thinking of.\nYou're a {1} number-guessing {2}!".format(guess,random.choice(adjective),random.choice(noun))
                break
            elif guess <> correct_number:
                if len(guess_history) == 4:
                    if guess > correct_number:
                        print """That's too high. This is your last guess, so I'll give you an extra hint.\nThe number I'm thinking of is {}.""".format(even_or_odd(correct_number))
                    if guess < correct_number:
                        print """That's too low. This is your last guess, so I'll give you an extra hint.\nThe number I'm thinking of is {}.""".format(even_or_odd(correct_number))
                elif guess > correct_number:
                    print "Too high"
                elif guess < correct_number:
                    print "Too low"
    except ValueError:
        print "It looks like you didn't enter a number. Please try again."
        pass
else:
    print "\nSorry, you're out of guesses.  You guessed {0}.".format(guess_history)
    print "I was thinking of {0}.".format(correct_number)
