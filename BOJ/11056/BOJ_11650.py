import sys

n=int(sys.stdin.readline())
l=[]
for _ in range(n):
    x,y=map(int, sys.stdin.readline().split())
    l.append([x,y])
l=sorted(l)
for i in l:
    print(i[0],i[1])
