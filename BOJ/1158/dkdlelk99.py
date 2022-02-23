# input
N, K = map(int, input().split())
arr = list(range(1, N+1))
answer = []
# solution
count = 0
for t in range(N):
    count += K - 1
    if count >= len(arr):
        count = count % len(arr)
    answer.append(arr.pop(count))
# output
print("<", ", ".join(map(str, answer)), ">", sep="")
