# 서로 다른 N개의 자연수의 합
S = int(input())
N = 0

# point : 작은 수 부터 더해야지 가장 큰 N의 값을 출력할 수 있음, 등차수열
# ex) 1+2+3+4 = 10 / 1+2+3+4+5 = 15 => 10~14 수는 N이 4임
while True:
  N += 1
  sum1 = N*(N+1)/2
  sum2 = (N+1)*(N+2)/2

  if sum1 <= S and sum2 > S:
    break

print(N)