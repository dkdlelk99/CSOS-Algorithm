# 15651
import itertools

N,M =map(int, input().split())
for lst in itertools.product([i for i in range(1, N+1)], repeat=M):
    for elem in lst:
        print(elem, end=' ')
    print()
