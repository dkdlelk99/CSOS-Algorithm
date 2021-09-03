bag = N = int(input())


for i in range(N//5+1):
    if (N - 5*i)%3 == 0:
        bag = min(bag, (N-5*i)//3+i)
if bag == N:
    print(-1)
else:
    print(bag)
