"""Practice with dictionaries."""

__author__ = "730384411"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary."""
    result: dict[str, str] = {}
    for item in a:
        if a[item] in result:
            raise KeyError("Repeated keys")
        result[a[item]] = item
    return result


def favorite_color(c: dict[str, str]) -> str:
    """Return the common favorite color."""
    counter: dict[str, int] = {}
    result: str = ""
    big: int = 0
    for item in c:
        key: str = c[item]
        if key in counter:
            counter[key] += 1
        else:
            counter[key] = 1
    for key in counter:
        if counter[key] > big:
            big = counter[key]
            result = key
    return result 


def count(d: list[str]) -> dict[str, int]:
    """Count the appearances of a value in a list."""
    result: dict[str, int] = {}
    for item in d:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result