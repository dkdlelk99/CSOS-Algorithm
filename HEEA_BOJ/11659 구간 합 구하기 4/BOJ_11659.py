import sys

n,m=map(int,sys.stdin.readline().split())
l=list(map(int,sys.stdin.readline().split()))
sum=[0]

for i in range(len(l)):
    sum.append(sum[i]+l[i])

for _ in range(m):
    start,end=map(int,sys.stdin.readline().split())
    print(sum[end]-sum[start-1])