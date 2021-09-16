"""An exercise in remainders and boolean logic."""

__author__ = "730384411"

number: int = int(input("Enter an int: "))
remainderone: int = number % 2
remaindertwo: int = number % 7
counter: int = 0

if counter == remainderone and counter == remaindertwo:
    print("TAR HEELS ")
else:
    if remainderone == 0 or counter == remaindertwo:
        if remainderone == 0:
            print("TAR ")
        else:
            print("HEELS ")
    else:
        print("CAROLINA ")