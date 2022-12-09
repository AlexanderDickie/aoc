from request import get_input

def part_1(inp):
    lines = inp[:-1].split('\n')
    moves = []
    for line in lines:
        dir, mag = line.split(' ')
        mag = int(mag)
        moves.append((dir, mag))

    # t initial position
    path = set([(0,0)]) 
   
    # (y, x)
    h = [0,0]
    t = [0,0]
    for move in moves:
        dir, mag = move

        for _ in range(mag):
            # head moves
            if dir == 'R':
                h[1] += 1
            elif dir == 'L':
                h[1] -= 1
            elif dir == 'U':
                h[0] += 1
            else:
                h[0] -= 1

            # touching
            if abs(h[0]-t[0]) <= 1 and abs(h[1] - t[1]) <= 1:
                continue

            # not touching, y moves
            if h[0] > t[0]:
                t[0] += 1
            elif h[0] < t[0]:
                t[0] -= 1

            if h[1] > t[1]:
                t[1] += 1
            elif h[1] < t[1]:
                t[1] -= 1
            path.add((t[0], t[1]))

    return len(path)
                    
print(part_1(get_input(9, 0)))
print(part_1(get_input(9, 1)))

def part_2(inp):
    lines = inp[:-1].split('\n')
    moves = []
    for line in lines:
        dir, mag = line.split(' ')
        mag = int(mag)
        moves.append((dir, mag))

    # t initial position
    path = set([(0, 0)]) 
    
    # (y, x)
    knots = [[0,0] for _ in range(10)]
    for move in moves:
        dir, mag = move

        for _ in range(mag):
            for i in range(9, 0, -1):
                h = knots[i]
                t = knots[i-1]

                # move true head
                if i == 9:
                    if dir == 'R':
                        h[1] += 1
                    elif dir == 'L':
                        h[1] -= 1
                    elif dir == 'U':
                        h[0] += 1
                    else:
                        h[0] -= 1
    
                # touching
                if abs(h[0]-t[0]) <= 1 and abs(h[1] - t[1]) <= 1:
                    continue
    
                # not touching, move t
                if h[0] > t[0]:
                    t[0] += 1
                elif h[0] < t[0]:
                    t[0] -= 1
    
                if h[1] > t[1]:
                    t[1] += 1
                elif h[1] < t[1]:
                    t[1] -= 1
    
            path.add((knots[0][0], knots[0][1]))

    return len(path)

print(part_2(get_input(9,0)))
print(part_2(get_input(9,2)))




