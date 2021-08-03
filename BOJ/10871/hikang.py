N, X =map(int,input().split())

# 수열 A
A = list(map(int, input().split()))

# X보다 작은 값을 A에서 찾아 출력
for i in range(N):
    if A[i] < X:
        print(A[i])
