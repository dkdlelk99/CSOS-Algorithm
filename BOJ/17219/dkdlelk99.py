import sys
N, M = map(int, sys.stdin.readline().split())
pw = dict()
for _ in range(N):
    site, password = map(str, sys.stdin.readline().split())
    pw[site] = password
for _ in range(M):
    print(pw[sys.stdin.readline().strip()])