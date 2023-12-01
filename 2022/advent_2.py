ITEMS = ['A', 'B', 'C']

def item_score(item):
    return(ord(item) - 64)

def match_score(elv_item, my_item):
    if elv_item == my_item:
        # Draw
        return 3
    elif (ITEMS.index(elv_item) + 1) % 3 == ITEMS.index(my_item):
        # I won
        return 6
    else:
        # I loose
        return 0

def get_item(elv_item, rule):
    if rule == 'X':
        return ITEMS[(ITEMS.index(elv_item) - 1) % 3]
    if rule == 'Y':
        return elv_item
    if rule == 'Z':
        return ITEMS[(ITEMS.index(elv_item) + 1) % 3]


with open('input_2', 'r') as file:
    total_score = 0
    for line in file:
        elv_item, my_item = (item.strip() for item in line.split(' '))
        # my_item = chr(ord(my_item) - 23) # shift my letters to use the same set
        my_item = get_item(elv_item, my_item) # Read the rule
        score = item_score(my_item) + match_score(elv_item.strip(), my_item)
        total_score += score


    print(total_score)
