import sys

N = int(sys.stdin.readline())
li = []

for i in range(N):
  li.append(list(map(int,sys.stdin.readline().split())))

for i in range(N):
  rank = 1
  for j in range(N):
    if li[i][0]<li[j][0] and li[i][1]<li[j][1]:
      rank = rank+1
  
  print(rank,end=" ")