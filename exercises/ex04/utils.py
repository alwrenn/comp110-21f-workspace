"""List utility functions."""

__author__ = "730384411"


def all(numbers: list[int], runner: int) -> bool:
    """State if all integers in the list are the same as an integer."""
    i: int = 0
    if len(numbers) == 0:
        return False
    while i < len(numbers):
        if runner == numbers[i]:
            i += 1
        else:
            return False
    if i == len(numbers):
        return True
    else:
        return False


def is_equal(one: list[int], two: list[int]) -> bool:
    """State if two lists are deeply equal."""
    i: int = 0
    lenone: int = len(one)
    lentwo: int = len(two)
    while i < lenone and i < lentwo:
        if one[i] == two[i]:
            i += 1
        else:
            return False
    if lenone == i and lentwo == i:
        return True
    else:
        return False


def max(input: list[int]) -> int:
    """Find max of a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    runner: int = input[0]
    while i < len(input):
        if input[i] > runner:
            runner = input[i]
        i += 1
    return runner