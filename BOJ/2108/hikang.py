import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = []
for i in range(N):
  arr.append(int(sys.stdin.readline()))

# 산술 평균
print(round(sum(arr)/len(arr)))

# 중앙값
arr.sort()
print(arr[N//2])

# 최빈값
most_count = Counter(arr).most_common()
if len(arr)>1:
  if most_count[0][1] == most_count[1][1]:
    print(most_count[1][0])
  else:
    print(most_count[0][0])

# 범위
print(arr[-1] - arr[0])
