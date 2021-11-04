"""Utility functions."""

__author__ = "730384411"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result 


def column_values(table: list[dict[str, str]], name: str) -> list[str]:
    """Produce a list of all values in a column in a table."""
    result: list[str] = []
    for row in table:
        item: str = row[name]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], number: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first `N` rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        result[column] = table[column][:number]
    return result


def select(table: dict[str, list[str]], column: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for item in column:
        result[item] = table[item]
    return result


def concat(one: dict[str, list[str]], two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in one:
        result[column] = one[column]
    for column in two:
        if column in result:
            result[column] += two[column]
        else:
            result[column] = two[column]
    return result


def count(list: list[str]) -> dict[str, int]:
    """Count the appearances of a str in a list."""
    result: dict[str, int] = {}
    for item in list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result