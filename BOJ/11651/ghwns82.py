N = int(input())

dot = [list(map(int, input().split())) for _ in range(N)]

dot.sort(key = lambda x : (x[1], x[0]))

for i in dot:
    print(i[0], i[1])
