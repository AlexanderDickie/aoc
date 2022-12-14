from request import get_input

def part_1(inp):
    lines = inp[:-1].split('\n')
    rocks = set()
    for line in lines:
        points = line.split(' -> ')
        for i in range(len(points)-1):
            sx, sy = [int(c) for c in points[i].split(',')]
            fx, fy = [int(c) for c in points[i+1].split(',')]
            if sy == fy:
                for x in range(min(sx, fx), max(sx, fx)+1):
                    rocks.add((sy, x))
            if sx == fx:
                for y in range(min(sy, fy), max(sy, fy)+1):
                    rocks.add((y, sx))
    # simulate sand falling
    n = 0
    max_y = max([rock[0] for rock in rocks])
    sand = (0, 500)
    while True:
        sy, sx = sand
        # falls in to abbyss
        if sy > max_y:
            break

        # try fall down
        down =(sy+1, sx)
        diag_left = (sy+1, sx-1)
        diag_right = (sy+1, sx+1)
        if down not in rocks:
            sand = down 
        elif diag_left not in rocks:
            sand = diag_left 
        elif diag_right not in rocks:
            sand = diag_right 

        # sand cannot move, so turns into rock 
        else:
            rocks.add(sand)
            sand = (0, 500)
            n += 1
    return n

print(part_1(get_input(14,0)))
print(part_1(get_input(14,1)))
            
def part_2(inp):
    lines = inp[:-1].split('\n')
    rocks = set()
    for line in lines:
        points = line.split(' -> ')
        for i in range(len(points)-1):
            sx, sy = [int(c) for c in points[i].split(',')]
            fx, fy = [int(c) for c in points[i+1].split(',')]
            if sy == fy:
                for x in range(min(sx, fx), max(sx, fx)+1):
                    rocks.add((sy, x))
            if sx == fx:
                for y in range(min(sy, fy), max(sy, fy)+1):
                    rocks.add((y, sx))
    # simulate sand falling
    n = 0
    max_y = max([rock[0] for rock in rocks])
    sand = (0, 500)
    while True:
        sy, sx = sand

        # hits bottom
        if sy == max_y + 1:
            rocks.add(sand)
            sand = (0, 500)
            n += 1
            continue

        # try fall down
        down =(sy+1, sx)
        diag_left = (sy+1, sx-1)
        diag_right = (sy+1, sx+1)
        if down not in rocks:
            sand = down 
        elif diag_left not in rocks:
            sand = diag_left 
        elif diag_right not in rocks:
            sand = diag_right 

        # sand is stuck
        # sand stuck at top
        elif sand == (0, 500):
            n += 1
            break
        # sand stuck on rock
        else:
            rocks.add(sand)
            sand = (0, 500)
            n += 1
    return n

print(part_2(get_input(14, 0)))
print(part_2(get_input(14, 1)))

