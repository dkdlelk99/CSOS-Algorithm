import sys, collections
# input
N, K = map(int, sys.stdin.readline().split())

max = 100000

que = collections.deque()
closed_set = {N}
que.append(N)
log = []

answer = 0
while len(que) != 0:
    n = que.popleft()
    log.append(n)
    if n == K:
        break
    answer += 1
    if 0 <= n - 1 <= max and n - 1 not in closed_set:
        que.append(n - 1)
        closed_set.add(n - 1)
    if 0 <= n + 1 <= max and n + 1 not in closed_set:
        que.append(n + 1)
        closed_set.add(n + 1)
    if 0 <= n * 2 <= max and n * 2 not in closed_set:
        que.append(n * 2)
        closed_set.add(n * 2)

print(answer, log, closed_set)
print(len(log), len(closed_set))