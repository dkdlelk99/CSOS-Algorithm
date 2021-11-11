a = [list(map(int, input().split())) for _ in range(int(input()))]

for i in range(1, len(a)):
    a[i][0] +=a[i-1][0]
    for j in range(1, len(a[i])):
        a[i][j] +=max(a[i-1][j-1:j+1])
print(max(a[-1]))
