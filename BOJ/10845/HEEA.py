import sys
from collections import deque

queue=deque([])
n=int(sys.stdin.readline()) #sys.stdin.readline() 안쓰면 시간초과 남, 반드시 사용하기!!

for i in range(n):
    l=list(sys.stdin.readline().split())
    if(l[0]=='push'):
        queue.append(l[1])
    elif(l[0]=='pop'):
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif(l[0]=='size'):
        print(len(queue))
    elif(l[0]=='empty'):
        if(len(queue)==0):
            print(1)
        else:
            print(0)
    elif(l[0]=='front'):
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[0])
    else:
        if(len(queue)==0):
            print(-1)
        else:
            print(queue[len(queue)-1])
