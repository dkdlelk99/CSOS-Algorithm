import sys
# input
N, M, v = map(int, input().split())
graph = [[0] * N for i in range(N)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x - 1][y - 1] = 1
    graph[y - 1][x - 1] = 1



# DFS
# initialize values
visited = [0] * N
answer = []


# search
def DFS(v):
    visited[v] = 1
    answer.append(v+1)
    for x in range(N):
        if graph[v][x] == 1 and visited[x] == 0:
            DFS(x)
    return 0


DFS(v-1)
print(*answer)


# BFS
# initialize values
visited =  [0] * N
answer = []

# search
q = [v-1]
visited[v-1] = 1
while len(q) != 0:
    y = q.pop(0)
    answer.append(y+1)
    for x in range(N):
        if graph[y][x] == 1 and visited[x] == 0:
            q.append(x)
            visited[x] = 1
print(*answer)