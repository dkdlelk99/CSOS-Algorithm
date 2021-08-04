import sys, collections
# input
N, K = map(int, sys.stdin.readline().split())
josephus = collections.deque(range(1, N+1))
answer = "<"
for _ in range(N): # N개의 숫자열을 만든다
    for k in range(K-1): # k-1번 돌리고
        josephus.append(josephus.popleft())
    answer += str(josephus.popleft()) + ", " # 뽑아서 넣는다
print(answer[:-2]+">")
