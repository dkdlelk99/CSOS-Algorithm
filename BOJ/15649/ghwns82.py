import itertools

N,M =map(int, input().split())
for lst in itertools.permutations([i for i in range(1, N+1)],M):
    for elem in lst:
        print(elem, end=' ')
    print()
