"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730384411"

from random import randint

print("Your fortune cookie says...")

i = randint(1, 4) 

if i == 1:
    print("The early bird gets the worm, but the second mouse gets the cheese.")
else:
    if i == 2:
        print("Your road to glory will be rocky, but fulfilling.")
    else:
        if i == 3:
            print("Nothing is impossible to a willing heart.")
        else:
            if i == 4: 
                print("Don't pursue happiness - create it.")

print("Now, go spread positive vibes!")