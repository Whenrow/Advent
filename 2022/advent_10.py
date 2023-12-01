from math import sqrt

STEPS = [20, 60, 100, 140, 180, 220]
def check_score(register, current):
    if current in STEPS:
        return current * register
    return 0

def new_cycle(crt, current_cycle):
    if current_cycle in [register-1, register, register+1]:
        crt += '#'
    else:
        crt += '.'
    if len(crt) == 40:
        print(crt)
        crt = ''
        current_cycle = 0
    else:
        current_cycle += 1
    return crt, current_cycle

with open('input_10', 'r') as file:
    score = 0
    crt = ''
    current_cycle = 0
    register = 1

    for line in file:
        crt, current_cycle = new_cycle(crt, current_cycle)

        score += check_score(register, current_cycle)
        if line.strip() != 'noop':
            qty = int(line.split(' ')[1])
            crt, current_cycle = new_cycle(crt, current_cycle)
            register += qty
            score += check_score(register, current_cycle)


# PART 1
print(score)

