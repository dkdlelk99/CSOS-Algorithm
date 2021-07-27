import sys
#Input
N = int(sys.stdin.readline())
deck = list(range(1, N+1))

while len(deck) != 1:
    deck.pop(0)
    deck.append(deck.pop(0))
print(deck[0])