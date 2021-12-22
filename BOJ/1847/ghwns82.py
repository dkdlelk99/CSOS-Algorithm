# 1847
# 성공
from collections import deque
n = int(input())

visted = [0] * 1_000_001
works= deque([n])
visted[n]=1
while 1:
    x = works.popleft()
    for i in [x/3, x/2, x-1]:
        if int(i)== i and visted[int(i)]==0:
            i=int(i)
            works.append(i)
            visted[i]=visted[x]+1
    if visted[1]:
        break
print(visted[1]-1)
