import sys, collections
# Input
N = int(sys.stdin.readline())
deck = collections.deque()
for i in range(1,N+1):
    deck.append(i)
# Problem Solving
while len(deck) != 1:
    deck.popleft()
    deck.append(deck.popleft())
# Output
print(deck[0])