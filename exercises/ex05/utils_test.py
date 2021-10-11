"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730384411"


def test_only_evens_edge() -> None:
    """Testing only_evens with an edge case."""
    number: list[int] = []
    assert only_evens(number) == 0


def test_only_evens_single() -> None:
    """Testing only_evens with single item."""
    number: list[int] = [110]
    assert only_evens(number) == 110


def test_only_evens_multiple() -> None:
    """Testing only_evens with multiple items."""
    number: list[int] = [1, 2, 3]
    assert only_evens(number) == 2


def test_sub_negative() -> None:
    """Testing sub with a negative number."""
    a_list: list[int] = [1, 2, 3]
    start: int = -1
    end: int = 1
    assert sub(a_list, start, end) == [1, 2]


def test_sub_large() -> None:
    """Testing sub with a too large number."""
    a_list: list[int] = [1, 2, 3]
    start: int = 0
    end: int = 4
    assert sub(a_list, start, end) == [1, 2]


def test_sub_three() -> None:
    """Testing sub with three items."""
    a_list: list[int] = [1, 2, 3]
    start: int = 0
    end: int = 1
    assert sub(a_list, start, end) == [1, 2]


def test_sub_five() -> None:
    """Testing sub with five items."""
    a_list: list[int] = [1, 2, 3, 4, 5]
    start: int = 2
    end: int = 4
    assert sub(a_list, start, end) == [3, 4, 5]


def test_concat_edge() -> None:
    """Testing concat with an edge case."""
    one: list[int] = []
    two: list[int] = [1]
    assert concat(one, two)


def test_concat_three() -> None:
    """Testing concat with three items."""
    one: list[int] = [1, 2, 3]
    two: list[int] = [4, 5, 6]
    assert concat(one, two) == [1, 2, 3, 4, 5, 6]


def test_concat_two() -> None:
    """Testing concat with two items."""
    one: list[int] = [1, 2]
    two: list[int] = [3, 4]
    assert concat(one, two) == [1, 2, 3, 4]


def test_concat_differ() -> None:
    """Testing concat with differing lengths."""
    one: list[int] = [1, 2, 3]
    two: list[int] = [4, 5]
    assert concat(one, two) == [1, 2, 3, 4, 5]