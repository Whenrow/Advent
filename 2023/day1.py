import re
with open("input1.txt") as f:
    content = f.readlines()

    # Part 1
    sum = 0
    for line in content:
        a = re.sub(r'\D', '', line)
        sum += int(a[0] + a[-1])
    print(sum)

    # Part 2
    sum = 0
    map = {"one": "o1ne", "two": "t2wo", "three": "t3hree", "four": "f4our", "five": "f5ive", "six": "s6ix", "seven": "s7even", "eight": "e8ight", "nine": "n9ine"}
    for line in content:
        for k, v in map.items():
            line = line.replace(k, v)
        a = re.sub(r'\D', '', line)
        sum += int(a[0] + a[-1])
    print(sum)


