# part 1
test = """
Time:      7  15   30
Distance:  9  40  200
"""
with open("input6.txt") as f:

    times = f.readline().split()[1:]
    distance = f.readline().split()[1:]

    # times = test.split('\n')[1].split()[1:]
    # distance = test.split('\n')[2].split()[1:]

     # Part 1
    score = 1
    for t, d in zip(times, distance):
        t = int(t)
        d = int(d)
        count = 0
        for tt in range(t + 1):
            if ((t - tt) * tt) > d:
                count += 1
        score *= count
    print("score: ", score)
    # Part 2

    # concat list of string
    times = ''.join(times)
    distance = ''.join(distance)

     # Part 1
    score = 1
    t = int(times)
    d = int(distance)
    count = 0
    for tt in range(t + 1):
        if ((t - tt) * tt) > d:
            count += 1
        elif count:
            break
    print('count :', count)
