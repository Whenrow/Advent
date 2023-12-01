import numpy as np

def seen_trees(tree, line):
    print(line, tree)
    index = 0
    while index < len(line):
        if tree > line[index]:
            index += 1
        else:
            return index + 1
    return index

# Puzzle 1
with open('input_8', 'r') as file:
    # build matrix
    forest = []
    for line in file:
        forest.append(list(map(int,list(line.strip()))))
    forest = np.array(forest)
    count = 0
    max_score = 0
    for i, row in enumerate(forest):
        for j, tree in enumerate(row):
            if i == 0 or i == len(forest) - 1 or j == 0 or j == len(row) - 1:
                count += 1
                continue
            # puzzle 1
            if tree > max(forest[:i,j]) \
            or tree > max(forest[i+1:,j]) \
            or tree > max(forest[i,j+1:]) \
            or tree > max(forest[i,:j]):
                count += 1

            # puzzle 2
            a = seen_trees(tree, list(reversed(forest[:i,j])))
            b = seen_trees(tree, forest[i+1:,j])
            c = seen_trees(tree, forest[i,j+1:])
            d = seen_trees(tree, list(reversed(forest[i,:j])))
            print(a,b,c,d)
            score = a*b*c*d
            if score > max_score:
                max_score = score


    print(count)
    print(max_score)
