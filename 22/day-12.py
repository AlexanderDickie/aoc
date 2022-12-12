from request import get_input


def part_1(inp):
    mat = inp[:-1].split('\n')
    mat = [list(s) for s in mat] 

    def neighbours(y, x):
        out = []
        for (yy, xx) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if y + yy < len(mat) and y + yy >= 0 and x + xx < len(mat[0]) and x + xx >= 0:
                out.append((y+yy, x+xx))
        return out
    for yi, row in enumerate(mat):
        for xi, val in enumerate(row):
            if val == 'S':
                start = (yi, xi)

    nxt = []
    cur = [start]
    seen = set([start])
    n = 0
    mat[start[0]][start[1]] = 'a'

    while cur:
        for coord in cur:
            y, x = coord
            if mat[y][x] == 'E':
                return n

            for neigh in neighbours(y, x):
                if neigh in seen:
                    continue

                ny, nx = neigh
                neigh_val = mat[ny][nx] 
                if neigh_val == 'E':
                    neigh_val = 'z'

                if ord(neigh_val) - ord(mat[y][x]) <= 1:
                    nxt.append(neigh)
                    seen.add(neigh)
        cur = nxt
        nxt = []
        n += 1
print(part_1(get_input(12, 0)))
print(part_1(get_input(12, 1)))

def part_2(inp):
    mat = inp[:-1].split('\n')
    mat = [list(s) for s in mat] 

    def neighbours(y, x):
        out = []
        for (yy, xx) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if y + yy < len(mat) and y + yy >= 0 and x + xx < len(mat[0]) and x + xx >= 0:
                out.append((y+yy, x+xx))
        return out

    starts = []
    for yi, row in enumerate(mat):
        for xi, val in enumerate(row):
            if val == 'S':
                mat[yi][xi] = 'a'
                starts.append((yi, xi))
            elif val == 'a':
                starts.append((yi, xi))

    nxt = []
    cur = starts 
    seen = set(starts)
    n = 0

    while cur:
        for coord in cur:
            y, x = coord
            if mat[y][x] == 'E':
                return n

            for neigh in neighbours(y, x):
                if neigh in seen:
                    continue

                ny, nx = neigh
                neigh_val = mat[ny][nx] 
                if neigh_val == 'E':
                    neigh_val = 'z'

                if ord(neigh_val) - ord(mat[y][x]) <= 1:
                    nxt.append(neigh)
                    seen.add(neigh)
        cur = nxt
        nxt = []
        n += 1
print(part_2(get_input(12, 0)))
print(part_2(get_input(12, 1)))
