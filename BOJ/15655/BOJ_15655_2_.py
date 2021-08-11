#N과 M(6)의 두번째 방식

from itertools import combinations

n,m=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)

result=list(combinations(l,m))

for i in result:
    print(" ".join(map(str,i)))