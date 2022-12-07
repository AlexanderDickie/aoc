
from request import get_input

class Dir:
    def __init__(self, parent):
        self.parent = parent # parent dir
        self.children = {} # chld_name -> chlild dir
        self.files = {} # name -> size

def part_1(inp):
    lines = inp[:-1].split('\n')
    root = Dir(None)
    cur = root

    # build filesystem tree
    i = 0
    while i < len(lines):
        line = lines[i]
        print(line)
        if line == "$ ls":
            j = i + 1
            while j < len(lines) and lines[j][0] != "$":
                line = lines[j]
                if line[:3] == "dir":
                    child_name = line.split(' ')[1] 
                    if child_name not in cur.children:
                        cur.children[child_name] = Dir(cur)
                else:
                    size, file_name = line.split(' ')
                    if file_name not in cur.files:
                        cur.files[file_name] = int(size)
                j += 1

            i = j - 1

        elif line == "$ cd /":
            cur = root

        elif line == "$ cd ..":
            cur = cur.parent

        else: 
            child_name = line.split(' ')[2]
            if child_name not in cur.children:
                cur.children[child_name] = Dir(parent=cur)
            cur = cur.children[child_name]

        i += 1

    # create dict of directory -> size of directory
    
    dir_lns = {}
    def dfs(dir, size, dir_name):
        for name, ln in dir.files.items():
            size += ln
        for name, dir in dir.children.items():
            size += dfs(dir, 0, name)
        dir_lns[dir_name] = size
        return size
    dfs(root, 0, "root")

    sm = 0
    for _, ln in dir_lns.items():
        if ln <= 100000:
            sm += ln
    print("part 1 is ", sm)

    # part 2
    unused = 70000000 - dir_lns["root"]
    to_delete = 30000000 - unused
    mn = float("inf") 
    for _, ln in dir_lns.items():
        if ln >= to_delete:
            mn = min(mn, ln)
    print("part 2 is ", mn)
    return 

# print(get_input(7, 0))
# print(part_1(get_input(7, 0)))
# print(part_1(get_input(7,1)))

# cleaner way to build dict of directory sizes?
from collections import defaultdict

def part_1b(inp):
    lines = inp[:-1].split('\n')

    dir_lns = defaultdict(int) 
    path = "root"

    i = 0
    while i < len(lines):
        line = lines[i]

        if line == "$ ls":
            if path == "root":
                dir = "root" 
            else:
                dir = path.split('/')[-1]

            if dir not in dir_lns:
                j = i + 1
                file_sm = 0

                while j < len(lines) and lines[j][0] != '$':
                    line = lines[j]
                    if line[0] != "d":
                        file_size, _ = line.split(' ')
                        file_size = int(file_size)
                        file_sm += file_size
                    j += 1
                i = j - 1
                print(lines[i+1])

                # add file_sm to parent directorys, and this dir 
                for dir_name in path.split('/'):
                    dir_lns[dir_name] += file_sm
            else:
                # we have ls'ed on this directory multiple times now, ignore
                while i < len(lines) and lines[i] != '$':
                    i += 1
                i -= 1

        elif line == "$ cd /":
            path = "root"

        elif line == "$ cd ..":
            path = "".join(path.split("/")[:-1])

        else:
            print(line)
            child = line.split(' ')[2]
            path += "/" + child

        i += 1

    print(dir_lns)
    return 

part_1b(get_input(7, 1))
