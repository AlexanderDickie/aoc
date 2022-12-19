from request import get_input

def part_1(inp):
    _rocks, jets = inp[:-1].split('\n\n\n')

    rocks = []
    for _rock in _rocks.split('\n\n'):
        rock = []
        lines = _rock.split('\n')[::-1]
        for yi, line in enumerate(lines):
            for xi, val in enumerate(line):
                if val == '#':
                    rock.append((yi, xi))
        rocks.append(rock)

    fallen = set()
    mx_height = 0
    mx_width = 7
    n_rocks = 0
    i = 0

    rock = [(r[0]+3, r[1]+2) for r in rocks[0]]
    while True:
        dir = jets[i%len(jets)]
        # pushed by jet
        dx = 1 if dir == '>' else -1
        potential_move = [(r[0], r[1]+dx) for r in rock]
        if len(set(potential_move).intersection(fallen)):
            pass
        elif min([r[1] for r in potential_move]) < 0:
            pass
        elif max(r[1] for r in potential_move) >= mx_width:
            pass
        else:
            rock = potential_move

        # fall down
        potential_move = [(r[0]-1, r[1]) for r in rock]
        if min([r[0] for r in potential_move]) < 0 or len(fallen.intersection(potential_move)):
            # cant move down, becomes fallen
            fallen = fallen.union(rock)
            mx_height = max(mx_height, max([r[0] for r in rock]))
            # build next rock
            n_rocks += 1
            rock = [(r[0]+mx_height+4, r[1]+2) for r in rocks[(n_rocks)%len(rocks)]]

            if n_rocks== 2022:
                break
        else:
            rock = potential_move
        i += 1
    return mx_height+1

print(part_1(get_input(17, 0)))
print(part_1(get_input(17, 1)))


# 1000.... is way too big to do any kind of simulation, so we need to find some repeated 
# state and then multiply this out to reach to 1000... For a repeated state we need to 
# be dropping the same rock, with the same position in the jets, onto the same top boundary 
# of the fallen rocks. First two are easy to hash and we can use bfs to create a hash of the 
# upper boundary for the third


def neighbours(coord):
    out = []
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        out.append((coord[0]+dy, coord[1]+dx))
    return out

# given fallen rocks, create a hash of the top outline of the shape of the fallen rocks
def hash_outline(fallen):
    _fallen = list(fallen)

    if _fallen:
        max_y = max(_fallen, key=lambda x: x[0])[0] 
    else:
        max_y = 0
    top_boundary = max_y +2

    start = (max_y+1, 0)
    hash = [start]
    seen = set([start])
    cur = [start]

    while cur:
        top = cur.pop()
        for neigh in neighbours(top):
            if neigh[0]>=top_boundary or neigh[0]<=-1 or neigh[1]<=-1 or neigh[1]>=7:
                pass

            elif neigh in fallen:
                pass
            elif neigh in seen:
                pass

            else:
                cur.append(neigh)
                hash.append(neigh)
                seen.add(neigh)
    # apply translation to hash, relative from start 
    out = []
    for coord in hash:
        out.append((coord[0]-start[0], coord[1]-start[1]))

    return tuple(out)

import matplotlib.pyplot as plt
def show_points(points):
    ys, xs = zip(*hash_outline(points))
    fig, ax = plt.subplots()
    ax.scatter(xs, ys, marker = 'o')
    plt.show()

def part_2(inp):
    _rocks, jets = inp[:-1].split('\n\n\n')

    rocks = []
    for _rock in _rocks.split('\n\n'):
        rock = []
        lines = _rock.split('\n')[::-1]
        for yi, line in enumerate(lines):
            for xi, val in enumerate(line):
                if val == '#':
                    rock.append((yi, xi))
        rocks.append(rock)

    fallen = set()
    hashes = {} # hash of outline, i%, n_rocks% -> n_rocks
    rock_heights = {} # n_rocks fallen -> current heigh

    mx_height = 0
    mx_width = 7
    n_rocks = 0
    i = 0

    rock = [(r[0]+3, r[1]+2) for r in rocks[0]]
    while True:
        dir = jets[i%len(jets)]
        # pushed by jet
        dx = 1 if dir == '>' else -1
        potential_move = [(r[0], r[1]+dx) for r in rock]
        if len(set(potential_move).intersection(fallen)):
            pass
        elif min([r[1] for r in potential_move]) < 0:
            pass
        elif max(r[1] for r in potential_move) >= mx_width:
            pass
        else:
            rock = potential_move

        # fall down
        potential_move = [(r[0]-1, r[1]) for r in rock]
        if min([r[0] for r in potential_move]) < 0 or len(fallen.intersection(potential_move)):
            # cant move down, becomes a fallen rock
            fallen = fallen.union(rock)
            n_rocks += 1

            mx_height = max(mx_height, max([r[0] for r in rock]))
            rock_heights[n_rocks] = mx_height

            # add hash of outline
            hsh = (hash_outline(fallen), i%len(jets), n_rocks%len(rocks))
            if hsh in hashes:
                # repeated state
                cur_n_rocks = n_rocks
                prev_n_rocks = hashes[hsh]

                cur_height = mx_height
                prev_height = rock_heights[prev_n_rocks]

                height_dif = cur_height-prev_height
                rocks_dif = cur_n_rocks-prev_n_rocks

                to_go = 1000000000000 - cur_n_rocks
                cycles_left = to_go // rocks_dif
                leftover = to_go % rocks_dif
                return cur_height + cycles_left*height_dif + rock_heights[leftover + prev_n_rocks] - rock_heights[prev_n_rocks] + 1
            else:
                hashes[hsh] = n_rocks

            # build next rock
            rock = [(r[0]+mx_height+4, r[1]+2) for r in rocks[(n_rocks)%len(rocks)]]

        else:
            rock = potential_move
        i += 1

print(part_2(get_input(17, 0)))
print(part_2(get_input(17, 1)))
