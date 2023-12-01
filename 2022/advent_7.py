import json
from pprint import pprint

available_space = 70000000
needed_space    = 30000000

sizes = []

def get_space(disk):
    local_size = 0
    global sizes
    for item, value in disk.items():
        if type(value) == dict:
            size = get_space(value)
            local_size += size
        else:
            local_size += value
    sizes.append(local_size)
    return local_size

# Puzzle 1
with open('input_7', 'r') as file:
    # build disk
    disk = {'/': {}}
    current_pos = []
    for line in file:
        args = line.strip().split(' ')
        if args[0] == '$':
            if args[1] == 'cd':
                if args[2] == '..':
                    current_pos.pop(-1)
                else:
                    current_pos.append(args[2])
        elif args[0] == 'dir':
            temp_dict = disk
            for k in current_pos:
                temp_dict = temp_dict[k]
            temp_dict[args[1]] = {}
        else:
            temp_dict = disk
            for k in current_pos:
                temp_dict = temp_dict[k]
            temp_dict[args[1]] = int(args[0])

    # parse disk
    get_space(disk)

    # part 1
    filtered_space = list(filter(lambda s: s <= 100000, sizes))

    # part 2
    total_space= sizes[-1]
    free_space = available_space - total_space
    space_to_free = needed_space - free_space
    size_to_free = min(filter(lambda s: s > space_to_free, sizes))

    print(sum(filtered_space), size_to_free)
