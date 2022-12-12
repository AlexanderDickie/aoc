from os import wait
from request import get_input
from math import prod 

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

    lcm = prod(list(set(divisors)))
    for monkey in monkeys:
        for idx, item in enumerate(monkey[0]):
            monkey[0][idx] = item % lcm

    for i in range(10000):
        for monkey in monkeys:
            for item in monkey[0]:
                old = item
                item = eval(monkey[1])
                item %= lcm

                [div, true, false] = monkey[2]
                if item % div == 0:
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
print(part_2(get_input(11, 1)))
