import sys
input = sys.stdin.readline

N = int(input())

Xdot = list(map(int, input().split()))
rank =sorted(set(Xdot))

dic = {rank[i]: i for i in range(len(rank))}

for i in Xdot:
    print(dic[i], end= ' ')
