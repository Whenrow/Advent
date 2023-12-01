# Puzzle 1
def priority(key):
    p = ord(next(iter(key)))
    if p >= 97:
        p -= 96
    else:
        p -= 38
    return p

with open('input_3', 'r') as file:
    sum_priority = 0
    for line in file:
        sac1, sac2 = (list(line[:len(line) // 2]), list(line[len(line) // 2:]))
        dup = set(sac1) & set(sac2)
        sum_priority += priority(dup)

# Puzzle 2
GRP_LEN = 3
with open('input_3', 'r') as file:
    sum_priority = 0
    group_sacs = []
    for line in file:
        sac = set(filter(lambda x: x != '\n', line))
        group_sacs.append(sac)
        if len(group_sacs) == 3:
            key = group_sacs[0].intersection(*group_sacs)
            sum_priority += priority(next(iter(key)))
            group_sacs = []
    print(sum_priority)
