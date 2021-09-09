"""Repeating a beat in a loop."""

__author__ = "730384411"

counter: int = 0
beat: str = input("What beat do you want to repeat? ")
number: int = int(input("How many times do you want to repeat it? "))
repeat: str = " "

if counter < number:
    while counter < number:
        if 1 < number:
            repeat = repeat + beat + " "
            number = number - 1
        else:
            repeat = repeat + beat
            number = number - 1
    print(repeat)
else:
    print("No beat...")