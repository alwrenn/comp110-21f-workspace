"""A program that evaluates the relationship between two integers using relational operators."""

__author__ = "730384411"

left: str = input("Enter left-hand side integer ")

right: str = input("Enter right-hand side integer ")

print("Left-hand side: " + left)
print("Right-hand side: " + right)

print(left + " < " + right + " is " + str(left < right))
print(left + " >= " + right + " is " + str(left >= right))
print(left + " == " + right + " is " + str(left == right))
print(left + " != " + right + " is " + str(left != right))
