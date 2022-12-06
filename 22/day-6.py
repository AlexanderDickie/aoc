from request import get_input

def part_1(inp):
    line = inp[:-1]

    for i in range(len(line)-3):
        if len(set(list(line[i: i+4]))) == 4:
            return i + 4

print(get_input(6, 0))
print(part_1(get_input(6, 0)))
print(part_1(get_input(6, 1)))

def part_2(inp):
    line = inp[:-1]

    for i in range(len(line)-13):
        if len(set(list(line[i: i+14]))) == 14:
            return i + 14

print(part_2(get_input(6, 0)))
print(part_2(get_input(6, 2)))
