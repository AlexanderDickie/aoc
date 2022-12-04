from request import get_input

def part_1(inp):
    sm = 0
    for line in inp[:-1].split('\n'):
        ln = len(line)
        in_both = set(list(line[:ln//2])).intersection(list(line[ln//2:])).pop()
        if in_both.isupper():
            sm += ord(in_both) - ord('A') + 27
        else:
            sm += ord(in_both) - ord('a') + 1
    return sm

print(part_1(get_input(3, 0)))
print(part_1(get_input(3, 1)))

def part_2(inp):
    lines = inp[:-1].split('\n')

    sm = 0
    for i in range(0, len(lines), 3):
        a, b, c = lines[i: i+3]
        badge = set(a).intersection(b).intersection(c).pop()
        if badge.isupper():
            sm += ord(badge) - ord('A') + 27
        else:
            sm += ord(badge) - ord('a') + 1
    return sm

print(part_2(get_input(3, 0)))
print(part_2(get_input(3, 2)))
