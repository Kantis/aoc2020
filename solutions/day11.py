from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


def calc_adjacent(x, y, world):
    lower_bounds = Point(max(x - 1, 0), max(y - 1, 0))
    upper_bounds = Point(min(x + 1, width - 1), min(y + 1, height - 1))
    return sum(1
               for row in range(lower_bounds.y, upper_bounds.y + 1)
               for col in range(lower_bounds.x, upper_bounds.x + 1)
               if world[row][col] == '#')


def calc_visible(p, dir, world):
    i = 1
    apply_dir = lambda p: Point(p.x + i * dir.x, p.y + i * dir.y)
    while (pp := apply_dir(p)).x < width and pp.y < height:
        if world[pp.y][pp.x] == '.':
            i += 1
            continue
        return world[pp.y][pp.x]
    return 'L'


def calc_next_state(old_state, taken_adjacent):
    if old_state == 'L' and taken_adjacent == 0:
        return '#'
    if old_state == '#' and taken_adjacent >= 5:
        return 'L'
    return old_state


def tick(world):
    next_world = copy_world(world)
    for row in range(height):
        for col in range(width):
            next_world[row][col] = calc_next_state(world[row][col], calc_adjacent(col, row, world))
    return next_world


def copy_world(world):
    return [x[:] for x in world[:]]


w = [[x for x in line] for line in open("../inputs/day11.txt").read().splitlines()]
width = len(w[0])
height = len(w)

# prev = w
# curr = tick(w)
# ticks = 0
# while prev != curr:
#     ticks += 1
#     prev = curr
#     curr = tick(curr)
#
# print(sum(1
#           for row in curr
#           for item in row
#           if item == '#'))

print(calc_visible(Point(0, 0), Point(1, 0), [['L', '.', '.', '#']]))
