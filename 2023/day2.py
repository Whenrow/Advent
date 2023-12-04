import re
test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
with open("input2.txt") as f:
    content = f.readlines()
    MAX_R = 12
    MAX_G = 13
    MAX_B = 14

    # Part 1
    sum = 0
    for line in content:
        id = re.match(r'Game (\d+)', line).group(1)
        plays = line.split(':')[1].split(';')
        do_break = False
        for play in plays:
            r = re.search(r'(\d+) red', play) and int(re.search(r'(\d+) red', play).group(1)) or 0
            b = re.search(r'(\d+) blue', play) and int(re.search(r'(\d+) blue', play).group(1)) or 0
            g = re.search(r'(\d+) green', play) and int(re.search(r'(\d+) green', play).group(1)) or 0
            if r > MAX_R or b > MAX_B or g > MAX_G:
                do_break = True
                break
        if do_break:
            continue
        sum += int(id)
    print(sum)

    # Part 2
    sum = 0
    for line in content:
        plays = line.split(':')[1].split(';')
        max_r, max_b, max_g = 0, 0, 0
        for play in plays:
            r = re.search(r'(\d+) red', play) and int(re.search(r'(\d+) red', play).group(1)) or 0
            if max_r == 0 or max_r < r:
                max_r = r
            b = re.search(r'(\d+) blue', play) and int(re.search(r'(\d+) blue', play).group(1)) or 0
            if max_b == 0 or max_b < b:
                max_b = b
            g = re.search(r'(\d+) green', play) and int(re.search(r'(\d+) green', play).group(1)) or 0
            if max_g == 0 or max_g < g:
                max_g = g
        power = max_r * max_b * max_g
        sum += power
    print(sum)
