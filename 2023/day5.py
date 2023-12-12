# part 1
 with open("input5.txt") as f:
     seeds = f.readline().split()[1:]
     seeds = [int(s) for s in seeds]
     print(seeds)
     zcontent = f.readlines()

     current_map = []
     # Part 1
     for line in zcontent:
         if not line.strip():
             current_map = []
             maps.append(current_map)
             continue
         if line[0].isdigit():
             end, start, length = line.split()
             current_map.append((int(end), int(start), int(length)))
     for map in maps:
         map.sort(key=lambda x: x[1])
         for index, s in enumerate(seeds):
             for end, start, length in map:
                 if s >= start and s < start + length:
                     seeds[index] = end + s - start
                     break

     print("Part1: ", min(seeds))

with open("input5.txt") as f:
    seeds = f.readline().split()[1:]
    seeds = [int(s) for s in seeds]
    seeds = [x for x in zip(seeds[::2], seeds[1::2])]
    print(seeds)
    zcontent = f.readlines()
    maps = []
    #Part 2
    for line in zcontent:
        if not line.strip():
            current_map = []
            maps.append(current_map)
            continue
        if line[0].isdigit():
            end, start, length = line.split()
            current_map.append((int(end), int(start), int(length)))

    for map in maps:
        map.sort(key=lambda x: x[1])
        for index, s in enumerate(seeds):
            for end, start, length in map:
                if s[0] >= start and s[0] < start + length:
                    news1 = s[1]
                    if start + length <= s[0] + s[1]:
                        olds1 = s[1]
                        news1 = start + length - s[0]
                        seeds.append((start + length, olds1 - news1))
                    seeds[index] = (end + s[0] - start, news1)
                    break

    print("Part2 :", min(seeds))



