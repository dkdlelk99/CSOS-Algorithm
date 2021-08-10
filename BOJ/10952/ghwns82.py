import sys

while True:
    A, B = map(int, sys.stdin.readline().split())
    if not A+B:
        break
    print(A+B)


# walrus 사용
while b:= sum(list(map(int, sys.stdin.readline().split()))):
    print(b)
