from request import get_input

def compare(i1, i2):
    if type(i1) == int and type(i2) == int:
        if i1 < i2:
            return True
        elif i1 > i2:
            return False
        else:
            return None

    elif type(i1) == int:
        return compare([i1], i2)

    elif type(i2) == int:
        return compare(i1, [i2])

    else:
        for idx in range(min(len(i1), len(i2))):
            comp = compare(i1[idx], i2[idx])
            if comp == None:
                continue
            return comp

        if len(i1) < len(i2):
            return True
        elif len(i1) > len(i2):
            return False
        else:
            return None
        
def part_1(inp):
    _pairs = inp[:-1].split('\n\n')
    pairs = []
    for p in _pairs:
        i1, i2 = p.split('\n')
        pairs.append([eval(i1), eval(i2)])

    sm = 0
    for idx, pair in enumerate(pairs):
        i1, i2 = pair
        if compare(i1, i2):
            sm += idx + 1 
    return sm

def part_2(inp):
    lines = inp[:-1].split('\n')
    lines = list(filter(lambda l: l!='', lines))
    lines = [eval(l) for l in lines]
    lines.append([[2]])
    lines.append([[6]])

    def ms(x):
        if len(x) == 1:
            return x
        l = ms(x[:len(x)//2])
        r = ms(x[len(x)//2:])

        out = []
        ir = 0
        il = 0
        while True:
            if ir == len(r):
                return out + l[il:]
            elif il == len(l):
                return out + r[ir:]
            else:
                if compare(l[il], r[ir]) == True:
                    out.append(l[il])
                    il += 1
                else:
                    out.append(r[ir])
                    ir += 1
    lines = ms(lines) 

    return (lines.index([[2]]) + 1) * (lines.index([[6]]) + 1)

print(part_1(get_input(13, 0)))
print(part_1(get_input(13, 1)))

print(part_2(get_input(13, 0)))
print(part_2(get_input(13, 2)))

