import sys, collections
# input
N, M, V = map(int, sys.stdin.readline().split())
que = collections.deque()
visited = [0] * (N+1)
graph = [[0]*(N+1) for i in range(N+1)]
# make graph with 2d list
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
answer = [[], []]
def BFS(index):
    for i in graph[index]:
        if visited[i] == 0 and graph[index][i]:
            visited[i] = 1
            answer[1].append(i + 1)
            BFS(i)
    return

que.append(V)
visited[V] = 1
while que:
    node = que.popleft()
    answer[0].append(node)
    for i in range(1, N):
        if visited[i] == 0 and graph[node][i]:
            que.append(i)
            visited[i] = 1
visited = [0] * (N+1)
BFS(V)
for i in graph:
    print(i)
print(answer)