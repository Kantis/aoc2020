lines = open("../inputs/2017_2.txt").read().splitlines()
values_per_line = [list(map(int, line.split("\t"))) for line in lines]
divisible_per_line = [[int(x / y) for x in i for y in i if x % y == 0 and x != y] for i in values_per_line]

print(sum(max(line) - min(line) for line in values_per_line))
print(sum([x for line in divisible_per_line for x in line]))
