#15650
import itertools

N,M =map(int, input().split())
for lst in itertools.combinations([i for i in range(1, N+1)],M):
    for elem in lst:
        print(elem, end=' ')
    print()
