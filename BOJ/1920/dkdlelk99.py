import sys
#Input
N = int(sys.stdin.readline())
nums = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))
for i in check:
    print("1" if i in nums else "0")
