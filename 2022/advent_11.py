import operator

OP = {'+': operator.add,
      '*': operator.mul}

def make_run(monkey):
    for m in monkey:
        m = monkey[m]
        def operation(x):
            if m['op'][1] == 'old':
                y = x
            else:
                y = int(m['op'][1])
            return OP[m['op'][0]](x, y)

        for item in m['items']:
            m['count'] += 1
            wl = operation(item)

            # Divide only in Part 1
            # wl = wl // 3

            # which monkey will get the item

            new_monkey = m[wl % m['test'] == 0]
            monkey[new_monkey]['items'].append(wl)
        m['items'] = []
    return monkey

with open('input_11', 'r') as file:
    monkey = {}
    for line in file:
        words = line.strip().split()
        if not words:
            continue
        match words[0]:
            case 'Monkey':
                monkey[int(words[1].strip(':'))] = {'count': 0}
                current_monkey = int(words[1].strip(':'))
            case 'Starting':
                monkey[current_monkey]['items'] = list(map(lambda x: int(x.strip(',')), words[2:],))
            case 'Operation:':
                monkey[current_monkey]['op'] = (words[4], words[5])
            case 'Test:':
                monkey[current_monkey]['test'] = int(words[-1])
            case 'If' if words[1] == 'true:':
                monkey[current_monkey][True] = int(words[-1])
            case 'If' if words[1] == 'false:':
                monkey[current_monkey][False] = int(words[-1])

# PART 1
# for run in range(20):
#     monkey = make_run(monkey)
# result = {m: monkey[m]['count'] for m in monkey}
# print(result, operator.mul(*sorted(result.values(), reverse=True)[0:2]))

    # PART 2
    for run in range(10000):
        if run == 105:
            print(monkey)
        monkey = make_run(monkey)
    result = {m: monkey[m]['count'] for m in monkey}
    print(result, operator.mul(*sorted(result.values(), reverse=True)[0:2]))

