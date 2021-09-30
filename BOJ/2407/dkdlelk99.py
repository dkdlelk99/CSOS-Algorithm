N, M = map(int, input().split())

pascal = [[1], [1, 1]]

for i in range(2, 102):
    next_level = [1]
    for j in range(i - 1):
        next_level.append(pascal[i - 1][j] + pascal[i - 1][j + 1])
    next_level.append(1)
    pascal.append(next_level)

print(pascal[N][M])
