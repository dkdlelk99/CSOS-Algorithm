import sys
N = int(sys.stdin.readline())
sort = []
for i in range(N):
    sort.append(tuple(map(int, sys.stdin.readline().split())))
sort = sorted(sort, key=lambda x: (x[0], x[1]))
for i in sort:
    print(i[0], i[1])
