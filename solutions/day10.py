import operator
from functools import reduce
from typing import List

joltages = sorted([int(line) for line in open("../inputs/day10sample2.txt").read().splitlines()])

# Part 1
ones = sum([1 for index, element in enumerate(joltages[1:]) if joltages[index] == element - 1])
threes = 1 + sum([1 for index, element in enumerate(joltages[1:]) if joltages[index] == element - 3])

for i, e in enumerate(joltages[1:]):
    print(i, e, joltages[i])

if joltages[0] == 1:
    ones += 1
else:
    threes += 1

print(ones, threes, ones * threes)

# Part 2

valid_choices = [sum(1
                     for j in joltages[i + 1:i + 3]
                     if j - joltages[i] <= 3)
                 for i in range(len(joltages) - 1)
                 ]

print(valid_choices)
print(reduce(operator.mul, valid_choices))
