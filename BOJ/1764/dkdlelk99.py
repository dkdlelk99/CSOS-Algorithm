import sys
# input
N, M = map(int, sys.stdin.readline().split())
known = set()
for _ in range(N):
    known.add(sys.stdin.readline().rstrip())
answer = [0]
for _ in range(M):
    check = sys.stdin.readline().rstrip()
    if check in known:
        answer.append(check)
        answer[0] += 1
# output
print(answer.pop(0))
for i in sorted(answer):
    print(i)