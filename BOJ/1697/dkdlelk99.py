import sys, collections
# input
N, K = map(int, sys.stdin.readline().split())
max = 100000
que = collections.deque()

que.append(N)
dist = [0] * (max + 1) # 깊이(거리)를 위한 자료구조

while len(que) != 0: # 너비 우선 탐색
    n = que.popleft()
    if n == K:
        print(dist[n])
        break
    for dx in (n - 1, n + 1, n * 2):
        if 0 <= dx <= max and not dist[dx]:
            dist[dx] = dist[n] + 1
            que.append(dx)
