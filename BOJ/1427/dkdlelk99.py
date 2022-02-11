import sys
# input
N = list(map(int, sys.stdin.readline().strip()))

print(*sorted(N, reverse=True), sep="")
