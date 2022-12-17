from request import get_input

def man_dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])


def part_1(inp, yy):
    lines = inp[:-1].split('\n')
    pairs = []
    for line in lines:
        line = line.split(' ')
        sx = int(line[2][2:-1])
        sy = int(line[3][2:-1])

        bx = int(line[-2][2:-1])
        by = int(line[-1][2:])
        pairs.append([[sy, sx], [by, bx]])
    
    cannot_x = set()
    taken_positions = set()
    for s, b in pairs:
        if b[0] == yy:
            taken_positions.add(b[0])
        if s[0] == yy:
            taken_positions.add(s[0])
        dist = man_dist(s, b)
        below = s[0] - dist
        above = s[0] + dist
        right = s[0] + dist
        left = s[0] - dist
        if left < 0 or right > 4000000:
            continue

        # intersects
        if s[0] <= yy and yy <= above:
            leftover = above - yy
            for xx in range(0, leftover+1):
                cannot_x.add(s[1]+xx)
                cannot_x.add(s[1]-xx)
        elif below <= yy and yy <= s[0]:
            leftover = yy - below
            for xx in range(0, leftover+1):
                cannot_x.add(s[1]+xx)
                cannot_x.add(s[1]-xx)

    return len(cannot_x) - len(taken_positions)

from shapely.geometry import LineString, Point
def vertices(sensor, beacon):
    dist = man_dist(sensor, beacon)
    vertices = [
            (beacon[0]+dist, beacon[1]),
            (beacon[0], beacon[1]+dist),
            (beacon[0]-dist, beacon[1]),
            (beacon[0], beacon[1]-dist),
            ]
    return vertices

def part_2(inp):
    lines = inp[:-1].split('\n')
    pairs = []
    for line in lines:
        line = line.split(' ')

        sx = int(line[2][2:-1])
        sy = int(line[3][2:-1])
        sensor = [sy, sx]

        bx = int(line[-2][2:-1])
        by = int(line[-1][2:])
        beacon = (by, bx)

        pairs.append([beacon, sensor])

    # this is pretty scrappy, but -
    # each sensor beacon pair forms a square that is rotated 45deg, 
    # this square's boundary is formed from 4 lines 
    # possible places for only one undetected beacon are a point where four of 
    # the above lines intersect, where no two of these lines are from the same 
    # beacon, leaving just one gap in the middle. And another situation on the 
    # 0,4000000 boundarys. Trying the First
    # situaition first, just reading the output from sorting the intersections 
    # we can indeed see there is such a first scenario, so the x y is the mid x y 
    # coordinate
    lines = []
    inters = []
    for b, s in pairs:
        vs = vertices(b, s)
        cur_lines = []
        for i in range(4):
            v1 = vs[i-1]
            v2 = vs[i]

            line = LineString([v1, v2])
            cur_lines.append(line)

            for _line in lines:
                if type(line.intersection(_line)) == Point:
                    inters.append(line.intersection(_line))
        lines.extend(cur_lines)
    inters = [[p.y, p.x] for p in inters]
    inters.sort(key=lambda p: p[0])
    for i in range(len(inters)-1):
        if abs(inters[i][1] - inters[i+1][1]) < 5:
            print(inters[i:i+4])
            print()

print(part_2(get_input(15, 1)))
