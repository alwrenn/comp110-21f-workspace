"""Counting letters in a string."""

__author__ = "730384411"

letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")
count: int = 0
counter: int = 0

while counter < len(word): 
    if word[counter] == letter:
        count = count + 1
        counter = counter + 1
    else:
        counter = counter + 1

print("Count: " + str(count))