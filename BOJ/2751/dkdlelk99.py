import sys
N = int(sys.stdin.readline())
sort = []
for i in range(N):
    sort.append(int(sys.stdin.readline()))
for i in sorted(sort):
    print(i)