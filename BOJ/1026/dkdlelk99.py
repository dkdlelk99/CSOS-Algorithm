import sys
# input
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

sorted_A = sorted(A, reverse=True)
sorted_B = sorted(B)

answer = 0
for i in range(N):
    answer += sorted_A[i] * sorted_B[i]
print(answer)