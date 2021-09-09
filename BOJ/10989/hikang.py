import sys

N = int(sys.stdin.readline())
unsorted_list = []

num = [0 for i in range(10001)]

# 메모리 초과 
# 이 문제에서 핵심 : 입력값의 개수를 해당 위치에 저장하기!
for i in range(N):
  x = int(sys.stdin.readline())
  num[x] += 1

for i in range(10001):
  for j in range(num[i]):
    print(i)