import pytest

from solutions.day5 import get_row, get_col


@pytest.mark.parametrize(
    "val,expectation",
    [
        ("BFFFBBFRRR", 70),
        ("FFFBBBFRRR", 14),
        ("BBFFBBFRLL", 102),
        ("FBFBBFFRLR", 44),
        ("FFFFFFFFFF", 0),
        ("BBBBBBBBBB", 127),
    ],
)
def test_get_row(val, expectation):
    assert get_row(val) == expectation

@pytest.mark.parametrize(
    "val,expectation",
    [
        ("BFFFBBFRRR", 7),
        ("FFFBBBFRRR", 7),
        ("BBFFBBFRLL", 4),
        ("FBFBBFFRLR", 5),
        ("FFFFFFFLLL", 0),
    ],
)
def test_get_col(val, expectation):
    assert get_col(val) == expectation
