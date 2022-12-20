from request import get_input

class Num: 
    def __init__(self, val):
        self.visited = False
        self.val = val
    def __str__(self):
        return format(self.val)

def part_1(inp):
    lines = inp[:-1].split('\n')
    nums = []
    for line in lines:
        nums.append(Num(int(line)))
    
    # we move our number into a gap between two numbers, this means that the gaps
    # each side of our number are effectively one gap. hence the mod (len(nums))-1
    # and minusing 1 if we are inserting our num in a place in front of our num
    i = 0
    while i < len(nums):
        num = nums[i]
        if num.visited:
            i += 1
            continue
        num.visited = True

        new_idx = (i + num.val) % (len(nums)-1)
        if new_idx >= i+1:
            new_idx += 1

        if new_idx > i:
            nums.insert(new_idx, num)
            nums.pop(i)
        else:
            nums.pop(i)
            nums.insert(new_idx, num)

    
    nums = list(map(lambda num: num.val, nums))
    for idx, n in enumerate(nums):
        if n == 0:
            return sum([nums[(1000*n + idx)%len(nums)] for n in range(1,4)])

print(part_1(get_input(20, 0)))
print(part_1(get_input(20, 1)))


def part_2(inp):
    lines = inp[:-1].split('\n')
    nums = []
    for line in lines:
        nums.append(Num(int(line)*811589153))
    initial_ordering = nums[:]
    # wanna make copy of nums, but still hold the same pointers/references to each num 

    for _ in range(10):
        for num in initial_ordering:
            i = nums.index(num)

            new_idx = (i + num.val) % (len(nums)-1)
            if new_idx >= i+1:
                new_idx += 1

            if new_idx > i:
                nums.insert(new_idx, num)
                nums.pop(i)
            else:
                nums.pop(i)
                nums.insert(new_idx, num)

    nums = list(map(lambda num: num.val, nums))
    for idx, n in enumerate(nums):
        if n == 0:
            return sum([nums[(1000*n + idx)%len(nums)] for n in range(1,4)])

print(part_2(get_input(20, 0)))
print(part_2(get_input(20, 1)))
