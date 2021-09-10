import sys

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

prime_cnt = 0

# 주어진 수 탐색
for i in arr:
  cnt=0
  # 숫자 1의 경우, 분류가 어려워 if문으로 뺌
  if i != 1:
    for j in range(2,i+1):
      if i%j == 0:
        cnt+=1
    if cnt==1:
      prime_cnt+=1

print(prime_cnt)

"""
처음 오답 코드
머리가 안돌아가~
for i in arr:
  if i!=1:
    for j in range(2,i):
      if i%j == 0:
        break
      else:
        prime_cnt+=1
        print(prime_cnt)
print(prime_cnt)
"""
