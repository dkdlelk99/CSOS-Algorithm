import sys
l=[]
sum=0
start=1
while start<=100:
    for _ in range(start):
        l.append(start)
    start+=1

a,b=map(int, sys.stdin.readline().split())

for i in range(a-1,b):
    sum+=l[i]
print(sum)