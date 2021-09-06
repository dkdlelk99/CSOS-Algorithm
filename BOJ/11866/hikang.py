import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())
q = deque()

for i in range(1, N+1):
    q.append(i)

print("<",end="")

while q:
  # K-1까지 큐에 append
  for i in range(K-1):
      q.append(q.popleft())
  # K번째는 출력 (append NO!)

  print(q.popleft(),end="") 
  if q:
    print(", ",end="")
  
print(">")
