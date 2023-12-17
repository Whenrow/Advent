import re
import math
# part 1
test = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

with open("input8.txt") as f:
    zcontent = f.readlines()
    sequence = zcontent[0].strip()
    # zcontent = test.splitlines()
    # sequence = zcontent[1]

    map = {}
    for node in zcontent[2:]:
        if not node:
            continue
        x, l, r = re.match(r"(\w{3}) = \((\w{3}), (\w{3})\)", node).groups()
        map[x] = (l, r)

    # part 1
    count = 0
    s_index = 0
    node = "AAA"
    while node != "ZZZ":
        count += 1
        if sequence[s_index] == "L":
            node = map[node][0]
        else:
            node = map[node][1]
        s_index += 1
        if s_index >= len(sequence):
            s_index = 0
    print("Part 1 : ", count)

    # part 2
    s_index = 0
    counts = []
    nodes = [x for x in map.keys() if re.match(r"\w{2}A", x)]
    for i, node in enumerate(nodes):
        count = 0
        while not re.match(r"\w{2}Z", node):
            count += 1
            if sequence[s_index] == "L":
                node = map[node][0]
            else:
                node = map[node][1]
            s_index += 1
            if s_index >= len(sequence):
                s_index = 0
        counts.append(count)
    print("Part 2 : ", math.lcm(*counts))


