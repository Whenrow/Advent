with open('input_1', 'r') as file:
    all_values = []
    current_value = 1
    for line in file:
        if line == '' or line == '\n':
            all_values.append(current_value)
            current_value = 0
            continue
        current_value += int(line)
    print(max(all_values))
