"""Drawing forests in a loop."""

__author__ = "730384411"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
happytree: str = TREE
depth: int = int(input("Depth: "))
counter: int = 0

while depth > counter:
    print(happytree)
    happytree = happytree + TREE
    depth = depth - 1