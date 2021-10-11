"""List utility functions part 2."""

__author__ = "730384411"


def only_evens(number: list[int]) -> list[int]:
    """Construct a list of evens when given a list."""
    xs: list[int] = []
    for item in number:
        if item % 2 == 0:
            xs.append(item)
    return xs


def sub(ys: list[int], start: int, end: int) -> list[int]:
    """Create a new list of different length."""
    xs: list[int] = []
    length: int = len(ys)
    if start < 0:
        start = 0
    if end > length:
        end = length 
    while start < end:
        xs.append(ys[start])
        start += 1
    return xs


def concat(one: list[int], two: list[int]) -> list[int]:
    """Combine lists."""
    three: list[int] = []
    a: int = 0
    b: int = 0
    while a < len(one):
        three.append(one[a])
        a += 1
    while b < len(two):
        three.append(two[b])
        b += 1
    return three


print(sub([1, 2, 3], 0, 2))