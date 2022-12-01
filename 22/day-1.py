from request import get_input
from heapq import heapify, heappop, heappush

def part_1(input: str):
    groups = input[:-1].split("\n\n")
    mx = 0
    for group in groups:
        group = group.split('\n')
        sm = 0
        for cal in group:
            sm += int(cal)
        mx = max(mx, sm)
    return mx


def part_2(input: str):
    groups = input[:-1].split("\n\n")
    min_heap = []
    heapify(min_heap)
    for group in groups:
        group = group.split('\n')
        sm = 0
        for cal in group:
            sm += int(cal)
        heappush(min_heap, sm)
        if len(min_heap) > 3:
            heappop(min_heap)
    return sum(min_heap) 

print(part_1(get_input(1, 0)))
print(part_1(get_input(1, 1)))
print(part_2(get_input(1, 2)))
