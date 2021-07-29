import sys
#Input
N = int(sys.stdin.readline())
deck = list(range(1, N + 1))

isEven = True
while len(deck) != 1:
    temp = []
    len_deck = len(deck)
    if isEven:
        rec = list(range(1, len_deck, 2)) #1 3 5 7 ...
        for i in rec:
            temp.append(deck[i])
    else:
        rec = list(range(2, len_deck, 2)) #0 2 4 8 ...
        for i in rec:
            temp.append(deck[i])
    deck = temp


    isEven = True if len_deck % 2 == 0 else False

print(deck[0])