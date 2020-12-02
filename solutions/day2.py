# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: cccccccccc

import re

from dataclasses import dataclass
from functools import reduce

@dataclass
class Policy:
    min_times: int
    max_times: int
    char: str
    password: str


def split(x):
    match = re.search(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", x)
    return Policy(int(match.group(1)), int(match.group(2)), match.group(3), match.group(4))


def test_policy(x: Policy):
    relevant_chars = re.sub(f'[^{x.char}]', '', x.password)
    return x.min_times <= len(relevant_chars) <= x.max_times


def test_policy2(x: Policy):
    return len([y for y in [x.password[x.min_times - 1], x.password[x.max_times - 1]] if y == x.char]) == 1


lines = open("../inputs/day2.txt").readlines()

print(sum([test_policy(x) for x in map(split, lines)]))
print(sum([test_policy2(x) for x in map(split, lines)]))
