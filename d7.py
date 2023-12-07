from loader import load
import re

cardMap = {'A': 13, 'K': 12, 'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
step = 100


def d1() -> str:
    lines = load()
    out = 0

    hands = []

    for line in lines:
        cards, bet = line.split(" ")
        cardsHash = getType(cards) * step**5

        for i, c in enumerate(cards):
            cardsHash += cardMap[c] * step**(4-i)

        hands.append((cardsHash, int(bet)))

    hands.sort(key=lambda x: x[0])

    for i, hand in enumerate(hands):
        out += (i+1) * hand[1]

    return str(out)


def getType(cards: list[chr], jokers: bool = False) -> int:
    cardCount = dict()
    jokerCount = 0

    for card in cardMap.keys():
        cardCount[card] = 0

    if jokers:
        cardCount['J'] = -6

    for card in cards:

        if jokers and card == 'J':
            jokerCount += 1

        else:
            cardCount[card] += 1

    gotcards = list(cardCount.values())
    gotcards.sort(reverse=True)

    if gotcards[0] == 5 or (jokers and gotcards[0] + jokerCount == 5):
        return 6
    elif gotcards[0] == 4 or (jokers and gotcards[0] + jokerCount == 4):
        return 5
    elif (gotcards[0] == 3 and gotcards[1] == 2) or (jokers and (gotcards[0] + gotcards[1] + jokerCount == 5)):
        return 4
    elif gotcards[0] == 3 or (jokers and gotcards[0] + jokerCount) == 3:
        return 3
    elif (gotcards[0] == 2 and gotcards[1] == 2) or (jokers and (gotcards[0] + gotcards[1] + jokerCount == 4)):
        return 2
    elif gotcards[0] == 2 or (jokers and jokerCount >= 1):
        return 1
    else:
        return 0



def d2() -> str:
    cardMap['J'] = 0
    for i in cardMap.keys():
        cardMap[i] += 1
    lines = load()
    out = 0

    hands = []

    for line in lines:
        cards, bet = line.split(" ")
        cardsHash = getType(cards, jokers=True) * step**5

        for i, c in enumerate(cards):
            cardsHash += cardMap[c] * step**(4-i)

        hands.append((cardsHash, int(bet), cards))

    hands.sort(key=lambda x: x[0])

    for i, hand in enumerate(hands):
        out += (i+1) * hand[1]

    return str(out)


if __name__ == "__main__":
    print(d1())
    print("")
    print(d2())
