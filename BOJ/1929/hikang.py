# 이 유형의 경우 입력값이 백만개로 단순하게 풀면 시간 초과가 발생

# 에라토스테네스의 체 알고리즘을 사용
import sys

N, M = map(int,sys.stdin.readline().split())

MAX = 1000000
check = [0]*(MAX+1)

check[0] = check[1] = True

for i in range(2, MAX+1):
  # 소수인 경우 배수를 찾아 모두 지우는 과정
  if not check[i]:
    j = i+i
      while j <= MAX:
        check[j] = True
        j += i

for i in range(N,M+1):
    if not check[i]:
        print(i)