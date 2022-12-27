from request import get_input

def part_1(inp):
    mat = inp[:-1].split('\n')

    height = len(mat) - 2
    width = len(mat[0]) - 2
    
    def potential_moves(y, x, i):
        out = []

        moves = [(0, 0), (1, 0), (-1, 0), (0, -1), (0, 1)]
        for dy, dx in moves:
            ny, nx = y + dy, x + dx

            if ny < 0 or ny >= len(mat) or nx < 0 or nx >= len(mat[0]):
                continue

            # check if in bounds 
            if mat[ny][nx] == '#':
                continue

            # check for < 
            pos = ((nx - 1 + i) % width) + 1
            if mat[ny][pos] == '<':
                continue

            # check for > 
            pos = ((nx - 1 - i) % width) + 1
            if mat[ny][pos] == '>':
                continue

            # check for v
            pos = ((ny - 1 - i) % height) + 1
            if mat[pos][nx] == 'v':
                continue

            # check for ^
            pos = ((ny - 1 + i) % height) + 1
            if mat[pos][nx] == '^':
                continue
            
            out.append((ny, nx))
        return out

    # bfs 
    cur = [(0, 1)]
    nxt = []
    seen = {((0, 1), 0)} # (pos, i)

    i = 1
    while cur:
        for (y, x) in cur:
            for move in potential_moves(y, x, i):

                if move == (len(mat)-1, len(mat[0]) -2):
                    return i 

                if (move, (i-1) % width) not in seen:
                    nxt.append(move)
                    seen.add((move, (i-1) % width))

        # the start position is a safe spot
        cur = nxt + [(0, 1)]
        seen.add(((0, 1), i))
        nxt = []
        i += 1

print(get_input(24, 0))
print(part_1(get_input(24, 0)))
print(part_1(get_input(24, 1)))

def part_2(inp):
    mat = inp[:-1].split('\n')

    height = len(mat) - 2
    width = len(mat[0]) - 2
    
    def potential_moves(y, x, i):
        out = []

        moves = [(0, 0), (1, 0), (-1, 0), (0, -1), (0, 1)]
        for dy, dx in moves:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= len(mat) or nx < 0 or nx >= len(mat[0]):
                continue

            # check if in bounds 
            if mat[ny][nx] == '#':
                continue

            # check for < 
            pos = ((nx - 1 + i) % width) + 1
            if mat[ny][pos] == '<':
                continue

            # check for > 
            pos = ((nx - 1 - i) % width) + 1
            if mat[ny][pos] == '>':
                continue

            # check for v
            pos = ((ny - 1 - i) % height) + 1
            if mat[pos][nx] == 'v':
                continue

            # check for ^
            pos = ((ny - 1 + i) % height) + 1
            if mat[pos][nx] == '^':
                continue
            
            out.append((ny, nx))
        return out

    def time_taken(start, end, i):

        # bfs 
        cur = [start]
        nxt = []
        seen = {(start , (i-1) % width)} # (pos, i)

        while cur:
            for (y, x) in cur:
                for move in potential_moves(y, x, i):

                    if move == end:
                        return i 

                    if (move, (i-1) % width) not in seen:
                        nxt.append(move)
                        seen.add((move, (i-1) % width))

            # the start position is a safe spot
            cur = nxt + [start]
            seen.add((start, i))
            nxt = []
            i += 1

    start = (0, 1)
    end = (len(mat)-1, len(mat[0])-2)

    l1 = time_taken(start, end, 1)
    l2 = time_taken(end, start, l1+1)
    l3 = time_taken(start, end, l2+1)
    return l3


print(part_2(get_input(24, 1)))
