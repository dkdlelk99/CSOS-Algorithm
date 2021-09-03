import sys

n,m=map(int,sys.stdin.readline().split())
information=dict()
for _ in range(n):
    l=list(sys.stdin.readline().split())
    information[l[0]]=l[1]

for _ in range(m):
    print(information[sys.stdin.readline().rstrip()])