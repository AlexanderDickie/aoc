from request import get_input

def touching(coord):
    out = []
    for d in ([1, 0, 0], [-1, 0, 0], [0, 1, 0], 
              [0, -1, 0], [0, 0, 1], [0, 0, -1]):
        out.append([x+y for x, y in zip(coord, d)])
    return out
def part_1(inp):
    lines = inp[:-1].split('\n')
    seen = set()
    n_touching = 0
    for line in lines:
        x, y, z = line.split(',')
        coord = [int(x), int(y), int(z)]

        for touch in touching(coord):
            if tuple(touch) in seen:
                n_touching += 2
        seen.add(tuple(coord))

    return len(lines)*6 - n_touching
print(part_1(get_input(18, 0)))
print(part_1(get_input(18, 1)))

def part_2(inp):
    lines = inp[:-1].split('\n')
    cubes = set() 
    for line in lines:
        x, y, z = line.split(',')
        cubes.add((int(x), int(y), int(z)))

    min_x = min(list(cubes), key=lambda x: x[0])[0]
    max_x = max(list(cubes), key=lambda x: x[0])[0]

    min_y = min(list(cubes), key=lambda x: x[1])[1]
    max_y = max(list(cubes), key=lambda x: x[1])[1]

    min_z = min(list(cubes), key=lambda x: x[2])[2]
    max_z = max(list(cubes), key=lambda x: x[2])[2]

    # draw a boundary around the droplet, and then do a bfs to exhaust the area between the 
    # boundary and the droplet. When we bump into a droplet cube on our bfs, we can add one to 
    # counter.
    touched = 0

    start = (min_x-1, min_y-1, min_z-1)
    cur = [start]

    seen = set()
    seen.add(start)

    while cur:
        top = cur.pop()
        for neigh in touching(top):
            neigh = tuple(neigh)

            if neigh in cubes:
                touched += 1

            elif neigh in seen:
                pass
            
            elif neigh[0] < min_x - 1 or neigh[0] > max_x+1 or neigh[1]<min_y-1 or neigh[1]>max_y+1 or neigh[2] < min_z-1 or neigh[2]>max_z+1:
                pass

            else:
                seen.add(neigh)
                cur.append(neigh)

    return touched

print(part_2(get_input(18, 0)))
print(part_2(get_input(18, 1)))
