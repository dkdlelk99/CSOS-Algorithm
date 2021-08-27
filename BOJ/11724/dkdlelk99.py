import sys
sys.setrecursionlimit(10**6) # 최대 재귀 깊이 설정 변경
# input
N, M = map(int, sys.stdin.readline().split())
graph = [[0]*N for i in range(N)]
visited = [0]*N
# make graph with 2d list
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

def DFS(index):
    for i in range(N):
        if visited[i] == 0 and graph[index][i]:
            visited[i] = 1
            DFS(i)
    return

# solution
answer = 0
# 연결된 그래프 순회 1회에 answer += 1
for i in range(N):
    if visited[i] == 0:
        answer += 1
        DFS(i)

print(answer)