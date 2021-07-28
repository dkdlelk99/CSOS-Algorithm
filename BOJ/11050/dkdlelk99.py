N, K = map(int, input().split())
numerator, denominator = 1, 1
for i in range(N, K, -1):
    numerator *= i
for j in range(1, N-K+1):
    denominator *= j
print(int(numerator/denominator))