"""A program that evaluates the relationship between two integers using numeric operators."""

__author__ = "730384411"

left: int = int(input("Enter left hand side numerator "))
right: int = int(input("Enter right hand side numerator "))

print("Left-hand side: " + str(left))
print("Right-hand side: " + str(right))

print(str(left) + " ** " + str(right) + " is " + str(left ** right))
print(str(left) + " / " + str(right) + " is " + str(left / right))
print(str(left) + " // " + str(right) + " is " + str(left // right))
print(str(left) + " % " + str(right) + " is " + str(left % right))