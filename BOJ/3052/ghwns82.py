import sys

A= set()
for i in range(10):
    A.add(int(sys.stdin.readline())%42)
print(len(A))


# 한줄 코딩
# print(len({int(input())%42 for i in range(10)}))
