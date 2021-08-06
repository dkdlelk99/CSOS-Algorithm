#N과 M(7)의 두번째 방식

from itertools import product

n,m=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
result=list(product(l,repeat=m))

for i in result:
    print(" ".join(map(str,i)))
