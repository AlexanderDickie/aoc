from request import get_input


def part_1(inp):
    top, bottom = inp[:-1].split('\n\n')
    top = top.split('\n')[:-1]
    bottom = bottom.split('\n')

    stacks = []
    for x in range(1, len(top[0]), 4):
        stacks.append([])
        for y in range(len(top)):
            if top[y][x] != ' ':
                stacks[-1].append(top[y][x])

    for line in bottom:
        line = line.split(' ')
        a, b, c = int(line[1]), int(line[3]), int(line[5])

        for i in range(a):
            mv = stacks[b-1].pop(0)
            stacks[c-1] = [mv] + stacks[c-1]

    return "".join([stack[0] for stack in stacks])

# 5. 30

print(part_1(get_input(5, 0)))
print(part_1(get_input(5, 1)))

def part_2(inp):
    top, bottom = inp[:-1].split('\n\n')
    top = top.split('\n')[:-1]
    bottom = bottom.split('\n')

    stacks = []
    for x in range(1, len(top[0]), 4):
        stacks.append([])
        for y in range(len(top)):
            if top[y][x] != ' ':
                stacks[-1].append(top[y][x])

    for line in bottom:
        line = line.split(' ')
        a, b, c = int(line[1]), int(line[3]), int(line[5])

        mv = []
        for i in range(a):
            mv.append(stacks[b-1].pop(0))
        stacks[c-1] = mv + stacks[c-1]


    return "".join([stack[0] for stack in stacks])

print(part_2(get_input(5, 0)))
print(part_2(get_input(5, 2)))
