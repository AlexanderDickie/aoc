from request import get_input

def part_1(inp):
    lines = inp[:-1].split('\n')

    output = [1]
    for line in lines:
        if line == "noop":
            output.append(output[-1])
            continue
        
        (_, v) = line.split(' ')
        output.append(output[-1])
        output.append(output[-1] + int(v))

    return sum([output[i] * (i+1) for i in range(19, len(output), 40)])

print(get_input(10, 0))
print(part_1(get_input(10, 0)))
print(part_1(get_input(10, 1)))

def part_2(inp):
    lines = inp[:-1].split('\n')

    output = [1]
    for line in lines:
        if line == "noop":
            output.append(output[-1])
            continue
        
        (_, v) = line.split(' ')
        output.append(output[-1])
        output.append(output[-1] + int(v))

    drawing = []
    for i, x in enumerate(output):
        i = i % 40
        if i >= x-1 and i <= x+1: 
            drawing.append('#')
        else:
            drawing.append('.')
    for i in range(len(drawing)//40):
        print("".join(drawing[40*i: 40*(i+1)]))

    return None 

print(part_2(get_input(10,0)))
print(part_2(get_input(10,2)))
