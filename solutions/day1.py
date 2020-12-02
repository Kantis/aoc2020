def find_sum(expected_sum, nums):
    for x1 in range(len(values)):
        for x2 in range(x1 + 1, len(values)):
            for x3 in range(x2 + 1, len(values)):
                if values[x1] + values[x2] + values[x3] == expected_sum:
                    return x1, x2, x3


def find_sum_rec(expected_sum, nums_to_use):
    return next(i for i in find_sum_count(expected_sum, nums_to_use) if isinstance(i, list) and len(i) > 0)


def find_sum_count(expected_sum, nums_to_use, indexes_used=[]):
    if nums_to_use <= 0:
        return indexes_used if expected_sum == 0 else None

    max_index_used = indexes_used[-1] if len(indexes_used) > 0 else 0

    return [y for y in [find_sum_count(expected_sum - x, nums_to_use - 1, indexes_used + [index]) for index, x in
                        enumerated_values[max_index_used + 1:]] if y is not None and len(y) > 0]


def find_sum2(expected_sum, nums_to_use):
    if nums_to_use == 1:
        for val, index in enumerated_values:
            if val == expected_sum:
                return [index]
        return None


file = open('inputs/day1.txt')
values = [int(x) for x in file.readlines()]
enumerated_values = list(enumerate(values))

print(next(x * y for x in values for y in values if x + y == 2020))
print(next(x * y * z for x in values for y in values for z in values if x + y + z == 2020))

pos3, pos1, pos2 = find_sum(2020, values)
print(pos1, values[pos1])
print(pos2, values[pos2])
print(pos3, values[pos3])
print(values[pos1] * values[pos2] * values[pos3])

res2 = find_sum_rec(2020, 3)
print(res2)
