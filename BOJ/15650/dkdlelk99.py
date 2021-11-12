import sys
# input
N, M = map(int, sys.stdin.readline().split())

def recursive(n, picked, depth=M):
    if depth == 0:
        print(*picked)
        return 0
    next_pick = 1 if len(picked) == 0 else picked[-1] + 1
    for i in range(next_pick, n+1):
        picked.append(i)
        recursive(n, picked, depth - 1)
        picked.pop()


recursive(N, [])