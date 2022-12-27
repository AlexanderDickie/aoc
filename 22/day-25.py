from request import get_input
"""
n may be represented as a5**0 + b5**1 + c5**2 ...
hence we know a since b*5**1, c*5**2, ... == 0 mod 5.
now subtract a*5**0. we now know b since  c*5**2, ... == 0 mod 25
and so on...
"""
def from_decimal(n):
    l = []
    i = 0
    while n != 0:
        mod = n % (5**(i+1))
        step = mod // (5**i)

        if step > 2:
            step = -(5 - step)
        if step == -2:
            l.append('=')
        elif step == -1:
            l.append('-')
        else:
            l.append(str(step))

        n -= step * (5**i)
        i += 1
    return "".join(l[::-1])

def to_decimal(n: str):
    out = 0
    for idx, c in enumerate(n[::-1]):
        if c == '=':
            out += -2 * 5**idx
        elif c == '-':
            out += -1 * 5**idx
        else:
            out += int(c) * 5**idx
    return out

def part_1(inp):
    lines = inp[:-1].split('\n')

    dec_sm = 0
    for l in lines:
        dec_sm += to_decimal(l)

    return from_decimal(dec_sm)

print(part_1(get_input(25, 0)))
print(part_1(get_input(25, 1)))
