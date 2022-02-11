# 2108
import sys
input = sys.stdin.readline
N= int(input())
array =[int(input()) for _ in range(N)]
array.sort()

print(round(sum(array)/N))
print(array[N//2])
from collections import Counter as cc
cnt = cc(array).most_common()
if len(cnt)>1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0]) # 상위 2개의 최빈값을 출력한다.
else:
    print(cnt[0][0])
print(max(array)-min(array))
