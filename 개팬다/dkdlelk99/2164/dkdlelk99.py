import sys
#Input
N = int(sys.stdin.readline())
# deck = list(range(1, N+1))

ans = 0
for i in range(17):
    if N >= 2**(i+1):
        ans += 1
    else:
        break
print(2**ans)