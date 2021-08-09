import sys
a, b = map(int, sys.stdin.readline().split())
c = list(map(int, sys.stdin.readline().split()))

for i in c:
    if i < b:
        print(i)


# 한줄코딩 불가능, walrus 사용시 복잡도 증가
