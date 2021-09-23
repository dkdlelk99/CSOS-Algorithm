import sys
from collections import deque
n,k=map(int,sys.stdin.readline().split())
result=[]
q=deque([])
for i in range(1,n+1):
    q.append(i)

while True:
    if(len(q)==1):
        break
    for i in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())
result.append(q[0])
print('<',end="")
for i in range(len(result)-1):
    print(result[i],end=", ")
print(str(result[len(result)-1])+'>')
