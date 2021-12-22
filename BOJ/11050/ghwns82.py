# 11050
# 성공
from itertools import combinations
n,k=map(int, input().split())
k = min(k, n-k)
result=1
for i in range(k):
    result *= n-i
    result /= i+1
print(int(result))
