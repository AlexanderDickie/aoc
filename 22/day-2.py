from request import get_input

def part_1(inp):
    lines = inp[:-1].split("\n") 
    opponent_wins = {
            'A': 'Z',
            'B': 'X',
            'C': 'Y',
            }

    sm = 0
    for line in lines:
        op, me = line.split(' ')
        sm += ord(me)-ord('X')+1
        if me == opponent_wins[op]:
            sm += 0
        elif ord(me) - ord('X') == ord(op) - ord('A'):
            sm += 3 
        else:
            sm += 6
    return sm

def part_2(inp):
    lines = inp[:-1].split("\n") 
    opponent_wins = {
            'A': 'Z',
            'B': 'X',
            'C': 'Y',
            }

    sm = 0
    for line in lines:
        op, outcome = line.split(' ')
        me_loose = opponent_wins[op]
        me_draw = chr(ord('X') + ord(op) - ord('A'))
        me_win = set(['X','Y','Z']).difference([me_loose, me_draw]).pop()

        if outcome == 'X':
            me = me_loose
            sm += 0
        elif outcome == 'Y':
            me = me_draw
            sm += 3
        else:
            me = me_win
            sm += 6

        sm += ord(me)-ord('X')+1

    return sm

print(part_1(get_input(2,0)))
print(part_1(get_input(2,1)))
print(part_2(get_input(2,0)))
print(part_2(get_input(2,2)))
