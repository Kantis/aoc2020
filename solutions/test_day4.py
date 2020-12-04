from contextlib import contextmanager

import pytest

from solutions.day4 import split_passports, calc_valid_passports, validate_range, validate_eye_color, \
    validate_hair_color, validate_height


def test_split_passports():
    assert len(split_passports("a\nb\n\nc")) == 2


def test_calc_valid_passports():
    assert calc_valid_passports("../inputs/day4.txt") == 153


@contextmanager
def does_not_raise():
    yield


@pytest.mark.parametrize(
    "val,expectation",
    [
        (3, pytest.raises(ValueError)),
        (2, does_not_raise()),
        (1, does_not_raise()),
        (0, pytest.raises(ValueError)),
    ],
)
def test_validate_range(val, expectation):
    with expectation:
        assert validate_range(val, 1, 2) is not None


@pytest.mark.parametrize(
    "val,expectation",
    [
        ("amb", does_not_raise()),
        ("blu", does_not_raise()),
        ("amber", pytest.raises(ValueError)),
        ("blue", pytest.raises(ValueError)),
        ("xyzamb", pytest.raises(ValueError)),
    ],
)
def test_validate_eye_color(val, expectation):
    with expectation:
        assert validate_eye_color(val) is not None


@pytest.mark.parametrize(
    "val,expectation",
    [
        ("#123123", does_not_raise()),
        ("#abcdef", does_not_raise()),
        ("#00000z", pytest.raises(ValueError)),
        ("#123123123", pytest.raises(ValueError)),
        ("#qweqwe", pytest.raises(ValueError)),
    ],
)
def test_validate_hair_color(val, expectation):
    with expectation:
        assert validate_hair_color(val) is not None


@pytest.mark.parametrize(
    "val,expectation",
    [
        ("58in", pytest.raises(ValueError)),
        ("59in", does_not_raise()),
        ("059in", does_not_raise()),
        ("76in", does_not_raise()),
        ("77in", pytest.raises(ValueError)),
        ("149cm", pytest.raises(ValueError)),
        ("150cm", does_not_raise()),
        ("193cm", does_not_raise()),
        ("194cm", pytest.raises(ValueError)),
        ("1150cm", pytest.raises(ValueError)),
    ],
)
def test_validate_height(val, expectation):
    with expectation:
        assert validate_height(val) is not None
