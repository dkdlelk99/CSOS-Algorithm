import sys

N, M = map(int, sys.stdin.readline().split())

arr = [[] for i in range(N)]

for i in range(M):
  x,y = map(int, sys.stdin.readline().split())
  arr[x].append(y)
  arr[y].append(x)

#print(arr)

visited = [False for i in range(N)]

# 문제의 핵심
# A - B - C - D - E 이어져있는지
# 따라서, 깊이가 4이상이면 1을 출력하면 됨
def dfs(v, depth):
  global ans
  visited[v] = True
  if depth >= 4:
    ans = True
    return
  for nxt in arr[v]:
    if not visited[nxt]:
      dfs(nxt, depth + 1)
      visited[nxt] = False

ans = False

for i in range(N):
  dfs(i, 0)
  visited[i] = False
  if ans:
    break

if ans == True :
  print(1)
else:
  print(0)
