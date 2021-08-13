import sys

#방법 1
a = []
for i in range(9):
    a.append(int(sys.stdin.readline()))
print(max(a), a.index(max(a))+1)

#방법 2
# a = [int(sys.stdin.readline()) for i in range(9)]
# print(max(a), a.index(max(a))+1)

#방법 3 walrus 사용
# print(max(a:=[int(sys.stdin.readline()) for i in range(9)]), a.index(max(a))+1)
