from collections import defaultdict

# part 1
test = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""
def my_sort(x):
    scale = '23456789TJQKA'
    hand = defaultdict(int)
    for card in x:
        hand[card] += 1
    score = sorted(list(hand.values()), reverse=True)
    for card in x:
        score.append(scale.index(card))
    return score

def my_sort2(x):
    scale = 'J23456789TQKA'
    hand = defaultdict(int)
    j_count = 0
    for card in x:
        if card == 'J':
            j_count += 1
            continue
        hand[card] += 1
    if hand:
        score = sorted(list(hand.values()), reverse=True)
        score[0] += j_count
    else:
        score = [5]
    for card in x:
        score.append(scale.index(card))
    return score

with open("input7.txt") as f:
    zcontent = f.readlines()
    # zcontent = test.splitlines()
    zcontent = [x.strip().split() for x in zcontent if x]

     # Part 1
    score = 1
    total = 0
    for hand, bid in sorted(zcontent, key=lambda x: my_sort(x[0])):
        total += score * int(bid)
        score += 1

    print('total 1 :', total)

    # Part 2
    score = 1
    total = 0
    for hand, bid in sorted(zcontent, key=lambda x: my_sort2(x[0])):
        total += score * int(bid)
        score += 1

    print('total 2 :', total)
