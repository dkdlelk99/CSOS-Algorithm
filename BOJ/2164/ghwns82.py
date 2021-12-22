# 2164
# 성공
from collections import deque

cards = deque([i+1 for i in range(int(input()))])
while 1:
    if len(cards)==1:
        break
    cards.popleft()
    if len(cards)==1:
        break
    cards.append(cards.popleft())
print(cards.pop())
