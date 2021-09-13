import sys, collections
# input
N, K = map(int, sys.stdin.readline().split())
que = collections.deque()
visited = [-1] * 100001
visited[N] = 0
que.append(N)
while len(que):
    parent = que.popleft()
    if parent != K:
        if parent * 2 < 100000:
            if visited[parent * 2] < 0:
                que.append(parent * 2)
                visited[parent * 2] = visited[parent] + 1
        if parent < 100000:
            if visited[parent + 1] < 0:
                que.append(parent + 1)
                visited[parent + 1] = visited[parent] + 1
        if visited[parent - 1] < 0:
            que.append(parent - 1)
            visited[parent - 1] = visited[parent] + 1
    else:
        break

print(visited[K])