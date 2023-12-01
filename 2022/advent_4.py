def contains(zone1, zone2):
    if int(zone1[0]) <= int(zone2[0]) and int(zone1[1]) >= int(zone2[1]):
        return True

def overlap(zone1, zone2):
    if int(zone1[1]) < int(zone2[0]) or int(zone2[1]) < int(zone1[0]):
        return True

# Puzzle 1
with open('input_4', 'r') as file:
    counter = 0
    for line in file:
        e1, e2 = line.strip('\n').split(',')
        e1 = e1.split('-')
        e2 = e2.split('-')
        if contains(e1, e2) or contains(e2, e1):
            counter += 1
    print(counter)


# Puzzle 2
with open('input_4', 'r') as file:
    counter = 0
    for line in file:
        e1, e2 = line.strip('\n').split(',')
        e1 = e1.split('-')
        e2 = e2.split('-')
        if overlap(e1, e2):
            counter += 1
    print(counter)
