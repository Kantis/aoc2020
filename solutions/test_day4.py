from solutions.day4 import split_passports


def test_split_passports():
    assert len(split_passports("a\nb\n\nc")) == 2
