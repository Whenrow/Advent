import re
test = """
467....114
...*......
..35...633
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
with open("input3.txt") as f:
    content = f.readlines()

    # Part 1
    somme = []
    nbrs = []
    pieces = []
    current_nbr = ''
    # (546, (x,y), (x+2, y))
    for i_row, line in enumerate(content):
    # for i_row, line in enumerate(test.split('\n'):
        if current_nbr:
            nbrs.append([(i_row - 1 , i_col - len(current_nbr)), (i_row - 1, i_col - 1), int(current_nbr)])
        current_nbr = ''
        for i_col, char in enumerate(line):
            if char == '\n':
                break
            if char == '.':
                if current_nbr:
                    nbrs.append([(i_row, i_col - len(current_nbr)), (i_row, i_col - 1), int(current_nbr)])
                    current_nbr = ''
                continue
            elif re.match('\d', char):
                current_nbr += char
            else:
                pieces.append((i_row, i_col))
                if current_nbr:
                    nbrs.append([(i_row, i_col - len(current_nbr)), (i_row, i_col - 1), int(current_nbr)])
                    current_nbr = ''
                continue
    # print("nbrs :", nbrs)
    # print("pieces: ", pieces)
    for piece in pieces:
        for nbr in nbrs:
            if piece[0] in (nbr[0][0] - 1, nbr[0][0], nbr[0][0] + 1) and piece[1] >= nbr[0][1] - 1 and piece[1] <= nbr[1][1] + 1:
                somme.append(nbr[2])
                nbr[2] = 0

    # Part 2
    somme = []
    nbrs = []
    pieces = []
    current_nbr = ''
    # (546, (x,y), (x+2, y))
    for i_row, line in enumerate(content):
    # for i_row, line in enumerate(test.split('\n'):
        if current_nbr:
            nbrs.append([(i_row - 1 , i_col - len(current_nbr)), (i_row - 1, i_col - 1), int(current_nbr)])
        current_nbr = ''
        for i_col, char in enumerate(line):
            if char == '\n':
                break
            if char == '.':
                if current_nbr:
                    nbrs.append([(i_row, i_col - len(current_nbr)), (i_row, i_col - 1), int(current_nbr)])
                    current_nbr = ''
                continue
            elif re.match('\d', char):
                current_nbr += char
            elif char == '*':
                pieces.append((i_row, i_col))
                if current_nbr:
                    nbrs.append([(i_row, i_col - len(current_nbr)), (i_row, i_col - 1), int(current_nbr)])
                    current_nbr = ''
                continue
    # print("nbrs :", nbrs)
    # print("pieces: ", pieces)
    for piece in pieces:
        count = 0
        ratio = []
        for nbr in nbrs:
            if piece[0] in (nbr[0][0] - 1, nbr[0][0], nbr[0][0] + 1) and piece[1] >= nbr[0][1] - 1 and piece[1] <= nbr[1][1] + 1:
                count += 1
                ratio.append(nbr[2])
                nbr[2] = 0

        if count == 2:
            somme.append(ratio[0] * ratio[1])
    print("somme: ", somme, sum(somme))

