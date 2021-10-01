# 15652
import itertools

N,M =map(int, input().split())
for lst in itertools.combinations_with_replacement([i for i in range(1, N+1)], r=M):
    for elem in lst:
        print(elem, end=' ')
    print()
