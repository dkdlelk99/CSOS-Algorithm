import math
for _ in range(int(input())):
    k, n = int(input()), int(input())
    print(math.comb(k+n, n-1))
