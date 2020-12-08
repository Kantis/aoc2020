from dataclasses import dataclass


@dataclass
class Node:
    op: str
    operand: int


def parse(lines):
    nodes = []
    for line in lines:
        split = line.split(" ")
        nodes.append(Node(split[0], int(split[1])))

    return nodes


lines = open("../inputs/day8.txt").read().splitlines()

pc = 0
acc = 0
visited = [False for i in range(len(lines))]
program = parse(lines)


def eval(node):
    global pc
    global acc

    if 'nop' == node.op:
        pc += 1
        return
    elif 'acc' == node.op:
        pc += 1
        acc += node.operand
    elif 'jmp' == node.op:
        pc += node.operand


while not visited[pc]:
    visited[pc] = True
    eval(program[pc])

print(acc)

# Part 2
for i in range(len(program)):
    pc = 0
    acc = 0
    visited = [False for x in range(len(lines))]

    old_op = ''
    if 'acc' == program[i].op:
        continue
    elif 'nop' == program[i].op:
        old_op = 'nop'
        program[i].op = 'jmp'
    else:
        old_op = 'jmp'
        program[i].op = 'nop'

    while not visited[pc]:
        visited[pc] = True
        eval(program[pc])
        if pc == len(program):
            print(acc)
            exit(0)

    program[i].op = old_op

