from collections import deque
N, K = map(int, input().split())
que = deque(range(1,N+1))
answer = []

count = 1
while len(que) != 0:
    pop = que.popleft()
    if count%K == 0:
        answer.append(pop)
    else:
        que.append(pop)
    count += 1

print("<", end="")
print(*answer, sep=", ", end="")
print(">", end="")
