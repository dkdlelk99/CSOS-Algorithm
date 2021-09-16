import sys

M, N = map(int,sys.stdin.readline().split())
arr = []

# 주어진 수 탐색
for i in range(M, N+1):
  cnt=0
  # 숫자 1의 경우, 분류가 어려워 if문으로 뺌
  if i != 1:
    for j in range(2,i+1):
      if i%j == 0:
        cnt+=1
    if cnt==1:
      arr.append(i)

for i in arr:
  print(i)