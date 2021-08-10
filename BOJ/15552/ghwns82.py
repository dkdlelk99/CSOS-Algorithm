import sys

a = int(sys.stdin.readline())
for _ in range(a):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
    
#한줄코딩
[print(sum(map(int, sys.stdin.readline().split()))) for _ in range(int(sys.stdin.readline()))]
