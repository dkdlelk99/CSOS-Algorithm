# 11650

N = int(input())
for i in sorted([list(map(int, input().split())) for _ in range(N)]):
    print(i[0], i[1])
