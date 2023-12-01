import re
from itertools import zip_longest
SECURITY_LEN = 14

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
with open('input_6', 'r') as file:
    for line in file:
        count = 0
        while len(set(line[count:count+SECURITY_LEN])) < SECURITY_LEN:
            count+=1
        print(count+SECURITY_LEN)

