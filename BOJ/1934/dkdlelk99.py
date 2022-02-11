import sys
# input
T = int(input())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    answer = a * b
    while b != 0:
        a, b = b, a % b
    print(int(answer/a))
