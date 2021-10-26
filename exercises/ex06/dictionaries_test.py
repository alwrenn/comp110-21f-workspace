"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count
import pytest

__author__ = "730384411"


def test_invert_edge() -> None:
    """Testing invert with an edge case."""
    a: dict[str, str] = {'kris': 'jordan', 'michael': 'jordan'}
    with pytest.raises(KeyError): 
        invert(a)


def test_invert_single() -> None:
    """Testing invert with a single case."""
    a: dict[str, str] = {'cat': 'apple'}
    assert invert(a) == {'apple': 'cat'}


def test_invert_multiple() -> None:
    """Testing invert with multiple cases."""
    a: dict[str, str] = {'z': 'a', 'y': 'b', 'x': 'c'}
    assert invert(a) == {'a': 'z', 'b': 'y', 'c': 'x'}


def test_favorite_color_same() -> None:
    """Testing favorite_color with all same color."""
    c: dict[str, str] = {'ally': 'blue', 'ann': 'blue', 'evan': 'blue'}
    assert favorite_color(c) == 'blue'


def test_favorite_color_tie() -> None:
    """Testing favorite_color with a tie."""
    c: dict[str, str] = {'ally': 'blue', 'ann': 'blue', 'jake': 'green', 'chloe': 'green'}
    assert favorite_color(c) == 'blue'


def test_favorite_color_norm() -> None:
    """Testing favorite_color with a normal case."""
    c: dict[str, str] = {'mark': 'yellow', 'ally': 'blue', 'ann': 'blue'}
    assert favorite_color(c) == 'blue'


def test_count_edge() -> None:
    """Testing count with an edge case."""
    d: list[str] = ['blue', 'blue', 'blue']
    assert count(d) == {'blue': 3}


def test_count_two() -> None:
    """Testing count with two items."""
    d: list[str] = ['blue', 'green']
    assert count(d) == {'blue': 1, 'green': 1}


def test_count_three() -> None:
    """Testing count with three items."""
    d: list[str] = ['blue', 'green', 'yellow']
    assert count(d) == {'blue': 1, 'green': 1, 'yellow': 1}