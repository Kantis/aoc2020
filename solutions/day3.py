def is_tree(x, y):
    return lines[y][x % len(lines[y])] == '#'


lines = open("../inputs/day3.txt").read().splitlines()
height = len(lines)

print(sum(is_tree(y, y) for y in range(1, height)))
print(sum(is_tree(y * 3, y) for y in range(1, height)))
print(sum(is_tree(y * 5, y) for y in range(1, height)))
print(sum(is_tree(y * 7, y) for y in range(1, height)))
print(sum(is_tree(int(y / 2), y) for y in range(2, height, 2)))
