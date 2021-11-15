import sys
# input
N, M = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))


def recursive(n, picked, depth=M):
    if depth == 0:
        print(*picked)
        return 0
    next_pick = 0 if len(picked) == 0 else nums.index(picked[-1])
    for i in range(next_pick, n):
        # if nums[i] not in picked:
        picked.append(nums[i])
        recursive(n, picked, depth - 1)
        picked.pop()


recursive(N, [])