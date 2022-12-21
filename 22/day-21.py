from request import get_input

def part_1(inp):
    lines = inp[:-1].split('\n')

    exprs = {}
    for line in lines:
        line = line.split(' ')
        name = line[0][:-1]

        exprs[name] = ' '.join(line[1:])

    def rec(node):
        expr = exprs[node]
        parts = expr.split(' ')
    
        if len(parts) == 1:
            return int(expr)
        
        expr = expr.replace(parts[0], str(rec(parts[0])))
        expr = expr.replace(parts[2], str(rec(parts[2])))
        return int(eval(expr))

    return rec("root")

print(part_1(get_input(21, 0)))
print(part_1(get_input(21, 1)))

class Exp:
    # ax + b
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, n):
        self.b += n
        return self
    def __radd__(self, n):
        self.b += n
        return self

    def __mul__(self, n):
        self.a *= n
        self.b *= n
        return self
    def __rmul__(self, n):
        self.a *= n
        self.b *= n
        return self

    def __sub__(self, n):
        self.b -= n
        return self

    def __rsub__(self, n):
        self.a *= -1
        self.b = n - self.b
        return self

    def __truediv__(self, n):
        self.a /= n
        self.b /= n
        return self

    def __str__(self):
        return f"Exp({self.a}, {self.b})"


def part_2(inp):
    """
    This doesnt work if at any time we were to divide by a / b where b is an 
    ancestor of humn, this doesnt happen though, as it would give the equation multiple roots.
    """
    lines = inp[:-1].split('\n')
    exprs = {}
    for line in lines:
        line = line.split(' ')
        name = line[0][:-1]

        exprs[name] = ' '.join(line[1:])

    def rec(exp):
        parts = exp.split(' ')
        if len(parts) == 1:
            if parts[0].isnumeric():
                return parts[0]
            if parts[0] == "humn":
                return str(Exp(1, 0))
            return rec(str(exprs[parts[0]]))

        exp = exp.replace(parts[0], rec(parts[0]))
        exp = exp.replace(parts[2], rec(parts[2]))
        return str(eval(exp))

    top_expr = exprs["root"]
    parts = top_expr.split(' ')
    l = eval(rec(parts[0]))
    r = float(rec(parts[2]))

    return (1/l.a) * (r - l.b)


print(part_2(get_input(21, 0)))
print(part_2(get_input(21, 1)))
