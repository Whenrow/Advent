import re
from itertools import zip_longest

def make_piles(data):
    stak = []
    for index, col in enumerate(zip_longest(*data, fillvalue=' ')):
        if index % 4 == 1:
            stak.append(list(filter(lambda x: x != ' ', col)))
    return stak

def apply_move_1(count, piles, f, t):
    for _ in range(count):
        piles[t] = [piles[f].pop(0)] + piles[t]
    return piles

def apply_move_2(count, piles, f, t):
    piles[t] = piles[f][:count] + piles[t]
    piles[f][:count] = []
    return piles

# Puzzle 1
with open('input_5', 'r') as file:
    setup_data = []
    line = file.readline()
    while not re.match("(\s\d+)+", line):
        setup_data.append(line)
        line = file.readline()

    piles = make_piles(setup_data)

    line = file.readline()
    line = file.readline()

    while line:
        m = re.match("move (\d+) from (\d+) to (\d+)", line)

        count = int(m.group(1))
        from_pile = int(m.group(2)) - 1
        to_pile = int(m.group(3)) - 1

        # piles = apply_move_1(count, piles, from_pile, to_pile)
        piles = apply_move_2(count, piles, from_pile, to_pile)

        line = file.readline()

    message = [p[0] for p in piles]
    print(''.join(message))

# Puzzle 2
# with open('input_4', 'r') as file:
#     counter = 0
#     for line in file:
#         e1, e2 = line.strip('\n').split(',')
#         e1 = e1.split('-')
#         e2 = e2.split('-')
#         if overlap(e1, e2):
#             counter += 1
#     print(counter)
