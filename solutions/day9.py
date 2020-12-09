from typing import List


def pairs(source: List[int], distinct: bool = True):
    length = len(source)
    inner_offset = 1 if distinct else 0
    for i in range(length):
        for j in range(i + inner_offset, length):
            yield source[i], source[j]


def find_offender(source: list, preamble: int):
    return next(element for index, element in enumerate(source) if
                index >= preamble and not any(sum(j) == element for j in pairs(source[(index - preamble):index])))


numbers = [int(line) for line in open("../inputs/day9.txt").read().splitlines()]
offender = find_offender(numbers, 25)
print(offender)


# Part 2
def find_contiguous():
    for i in range(len(numbers)):
        acc = numbers[i]
        j = i
        while acc < offender:
            j += 1
            acc += numbers[j]

            if acc == offender:
                return numbers[i:j]


res = find_contiguous()
print(min(res) + max(res))
