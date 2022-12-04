from request import get_input

def part_1(inp):
    lines = inp[:-1].split('\n')
    count = 0
    for line in lines:
        a ,b = line.split(',')
        sa, fa = a.split('-')
        sb, fb = b.split('-')
        ss1  = set([i for i in range(int(sa), int(fa)+1)])
        ss2  = set([i for i in range(int(sb), int(fb)+1)])

        inter = ss1 & ss2
        if inter == ss1 or inter == ss2:
            count += 1

    return count

print(part_1(get_input(4,0)))
print(part_1(get_input(4,1)))

def part_2(inp):
    lines = inp[:-1].split('\n')
    count = 0
    for line in lines:
        a ,b = line.split(',')
        sa, fa = a.split('-')
        sb, fb = b.split('-')
        ss1  = set([i for i in range(int(sa), int(fa)+1)])
        ss2  = set([i for i in range(int(sb), int(fb)+1)])

        if ss1 - ss2 != ss1:
            count += 1

    return count

print(part_1(get_input(4,0)))
print(part_2(get_input(4,2)))
