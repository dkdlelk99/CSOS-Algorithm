N = int(input())
for i in range(N):
    sum = 0
    for n in str(i):
        sum += int(n)
    if(sum + i) == N:
        print(i)
        break
    if i == N - 1:
        print(0)
