import sys
#Input
N = int(sys.stdin.readline())
deck = list(range(1, N+1))

# while len(deck) != 1:
#     deck.pop(0)
#     deck.append(deck.pop(0))
# print(deck[0])
while len(deck) != 1:
    rec = list(range(0, len(deck), 2))
    rec.reverse()
    for i in rec:
        deck.pop(i)
    deck.reverse()
print(deck[0])