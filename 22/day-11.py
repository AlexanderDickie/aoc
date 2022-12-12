from os import wait
from request import get_input
from math import prod 

# greedy
def part_1(inp):
    infos = inp[:-1].split('\n\n')
    monkeys = []
    for info in infos:
        info = info.split('\n')
        info = [l.strip(' ') for l in info]

        items = []
        for s in info[1].split(' ')[2:]:
            items.append(int(s.strip(',')))

        operation = " ".join(info[2].split(' ')[3:])

        div = int(info[3].split(' ')[-1])
        true = int(info[4].split(' ')[-1])
        false = int(info[5].split(' ')[-1])

        monkey = [
                items,
                operation,
                [div, true, false],
                0
                ]
        monkeys.append(monkey)

    for _ in range(20):
        for monkey in monkeys:
            for item in monkey[0]:
                old = item
                item = eval(monkey[1])
                item //= 3
                
                [div, true, false] = monkey[2]
                if item % div == 0:
                    monkeys[true][0].append(item)
                else:
                    monkeys[false][0].append(item)
                monkey[-1] += 1
            monkey[0] = []
           
    inspections = [monkey[-1] for monkey in monkeys]
    inspections.sort()
    return prod(inspections[-2:])

print(get_input(11, 0))
print(part_1(get_input(11, 0)))
print(part_1(get_input(11, 1)))

# represent each item as combination of modulu from relevent divisors, this is all what matters
class Item:
    def __init__(self, divisors, initial_value):
        divisor_map = {}
        for divisor in divisors:
            divisor_map[divisor] = initial_value % divisor
        self.divisor_map = divisor_map

    def is_divisible(self, divisor):
        return self.divisor_map[divisor] == 0

    def update(self, expr):
        for k, v in self.divisor_map.items():
            old = v
            new_value = eval(expr)
            self.divisor_map[k] = new_value % k

def part_2(inp):
    infos = inp[:-1].split('\n\n')
    monkeys = []
    divisors = []
    for info in infos:
        info = info.split('\n')
        info = [l.strip(' ') for l in info]

        items = []
        for s in info[1].split(' ')[2:]:
            items.append(int(s.strip(',')))

        operation = " ".join(info[2].split(' ')[3:])

        div = int(info[3].split(' ')[-1])
        divisors.append(div)
        true = int(info[4].split(' ')[-1])
        false = int(info[5].split(' ')[-1])

        monkey = [
                items,
                operation,
                [div, true, false],
                0
                ]
        monkeys.append(monkey)

    # convert each monkeys integer item to class item
    for monkey in monkeys:
        new_items = []
        for item in monkey[0]:
            new_items.append(Item(divisors, item))
        monkey[0] = new_items

    for i in range(10000):
        print(i)
        for monkey in monkeys:
            for item in monkey[0]:
                item.update(monkey[1])

                [div, true, false] = monkey[2]
                if item.is_divisible(div):
                    monkeys[true][0].append(item)
                else:
                    monkeys[false][0].append(item)

                monkey[-1] += 1
            monkey[0] = []
        inspections = [monkey[-1] for monkey in monkeys]
           
    inspections = [monkey[-1] for monkey in monkeys]
    inspections.sort()
    return prod(inspections[-2:])

print(part_2(get_input(11, 0)))
print(part_2(get_input(11, 2)))
