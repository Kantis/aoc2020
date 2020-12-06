import re
from functools import reduce


def split_groups(s):
    return re.split(r"\n\n", s)


lines = open("../inputs/day6.txt").read()

# Anyone answered
groups = [x.replace("\n", "") for x in split_groups(lines)]
print(sum([len(set(x)) for x in groups]))


# Everyone answered
groups2 = [x.split("\n") for x in split_groups(lines)]
print(sum([len(reduce(set.intersection, [set(person) for person in group])) for group in groups2]))
