# part 1
test = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

with open("input9.txt") as f:
    zcontent = f.readlines()
    # zcontent = test.splitlines()
    zcontent = [list(map(int, x.strip().split())) for x in zcontent if x]

    # Part 1
    sum = 0
    for line in zcontent:
        tab = [line]
        new_line = line
        while not all(i == 0 for i in new_line):
            new_line = [j-i for j, i in zip(new_line[1:], new_line[:-1])]
            tab.append(new_line)
        tab[-1].append(0)
        tab.reverse()
        for index, l in enumerate(tab):
            if index == 0:
                continue
            tab[index].append(l[-1] + tab[index-1][-1])
        sum += tab[-1][-1]

    print('total 1 :', sum)

    # Part 2
    sum = 0
    for line in zcontent:
        tab = [line[::-1]]
        new_line = line
        while not all(i == 0 for i in new_line):
            new_line = [j-i for j, i in zip(new_line[1:], new_line[:-1])]
            tab.append(new_line[::-1])
        tab[-1].append(0)
        tab.reverse()
        for index, l in enumerate(tab):
            if index == 0:
                continue
            tab[index].append(l[-1] - tab[index-1][-1])
        sum += tab[-1][-1]

    print('total 2 :', sum)
