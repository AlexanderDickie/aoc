from request import get_input

def part_1(inp):
    lines = inp[:-1].split('\n')
    lines = [[int(i) for i in line] for line in lines]
    height = len(lines)
    width = len(lines[0])

    seen = set()
    # two passes horizontally
    for y in range(height):
        line = lines[y]

        mx = -1
        for x in range(width):
            if line[x] > mx:
                seen.add((y, x))
                mx = line[x]
        mx = -1
        for x in range(width-1, -1, -1):
            if line[x] > mx:
                seen.add((y, x))
                mx = line[x]
    # two passes vertically
    for x in range(width):

        mx = -1 
        for y in range(height):
            if lines[y][x] > mx:
                seen.add((y, x))
                mx = lines[y][x]
        mx = -1 
        for y in range(height-1, -1, -1):
            if lines[y][x] > mx:
                seen.add((y, x))
                mx = lines[y][x]
    return len(seen)

print(part_1(get_input(8, 0)))
print(part_1(get_input(8, 1)))

from math import prod

def part_2(inp):
    lines = inp[:-1].split('\n')
    grid = [[int(i) for i in line] for line in lines]
    width, height = len(grid[0]), len(grid)

    mx = 0
    for yi, row in enumerate(grid):
        for xi, val in enumerate(row):
            inter = [0,0,0,0]
            
            for x in range(xi+1, width):
                inter[0] += 1
                if row[x] >= val:
                    break
                
            for x in range(xi-1, -1, -1):
                inter[1] += 1
                if row[x] >= val:
                    break
            
            for y in range(yi+1, height):
                inter[2] += 1
                if grid[y][xi] >= val:
                    break

            for y in range(yi-1, -1, -1):
                inter[3] += 1
                if grid[y][xi] >= val:
                    break

            mx = max(mx, prod(inter))
    return mx
print(part_2(get_input(8, 0)))
print(part_2(get_input(8, 1)))
