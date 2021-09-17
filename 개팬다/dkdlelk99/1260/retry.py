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


def BFS(index):
    que.append(index)
    visited = [index]
    while que:
        node = que.popleft()
        for i in range(N):
            if i in visited and graph[node][i] == 1:
                que.append(i)
                visited.append(i)
    return visited



def DFS(index, visited=[]):
    visited.append(index)
    for i in range(N):
        if index in visited and graph[index][i] == 1:
            visited.append(index)
            BFS(i)
    return visited


answer = DFS(V)
for i in answer:
    print(i, end=' ')
answer = BFS(V)
for i in answer:
    print(i, end=' ')
