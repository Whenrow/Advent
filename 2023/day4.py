from collections import defaultdict
import re
test = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
with open("input4.txt") as f:
    content = f.readlines()

    # Part 1
    somme = 0
    for line in content:
    # for line in test.split('\n')[1:-1]:
        data = line.split(":")
        winning, guesses = data[1].split("|")
        wining = set(winning.split(' '))
        guesses = set(guesses.strip('\n').split(' '))
        wining = wining.intersection(guesses) - set([''])
        if wining:
            score = 2**(len(wining) - 1)
            print(wining, ' -> ', score)
            somme += score

    print(somme)
    # Part 2
    somme = 0
    cards = defaultdict(int)
    for index, line in enumerate(content):
    # for index, line in enumerate(test.split('\n')[1:-1]):
        cards[index] += 1
        data = line.split(":")
        winning, guesses = data[1].split("|")
        wining = set(winning.split(' '))
        guesses = set(guesses.strip('\n').split(' '))
        wining = wining.intersection(guesses) - set([''])
        if wining:
            for i in range(len(wining)):
                cards[index + i + 1] += cards[index]

    print(cards, sum(cards.values()))
