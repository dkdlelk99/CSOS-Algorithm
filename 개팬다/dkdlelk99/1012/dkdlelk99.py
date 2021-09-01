import sys
# input
T = int(sys.stdin.readline())


def search(x,y):
    if x + 1 > M or y + 1 > N:
        return 0
    if bechu[y][x] == 0:
        return 0
    else:
        visited.add((x, y))
        if search(x + 1, y) == 0 and search(x, y + 1) == 0:
            answer[0] += 1


for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    bechu = [[0] * M for i in range(N)]
    visited = set()
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        bechu[y][x] = 1

    answer = [0]
    for y in range(N):
        for x in range(M):
            if (x, y) not in visited and bechu[y][x] == 1:
                search(x, y)
    print(answer[0])