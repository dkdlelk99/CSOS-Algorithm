import sys


def search(x,y):
    # print("call by x:",x,"  y: ",y)
    visited.add((x, y))
    # 기저 조건 1: 범위
    if x > M - 1 or y + 1 > N or x < 0 or y < 0:
        return 0
    # 기저 조건 2: 배추가 아니다
    if bechu[y][x] == 0:
        return 0

    r,l,u,d = 1,1,1,1
    if (x+1, y) not in visited:
        r = search(x + 1, y)
    if (x, y+1) not in visited:
        d = search(x, y + 1)
    if (x-1, y) not in visited:
        l = search(x - 1, y)
    if (x, y-1) not in visited:
        u = search(x, y - 1)
    if r == 0 and d == 0 and l == 0 and u == 0:
        return 0


for _ in range(int(input())):
    # input
    M, N, K = map(int, sys.stdin.readline().split()) # 가로 세로 배추 수
    bechu = [[0] * M for i in range(N)]
    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        bechu[y][x] = 1

    visited = set()
    answer = 0

    for y in range(N):
        for x in range(M):
            if (x, y) not in visited and bechu[y][x] == 1:
                # print("\nstart search")
                search(x, y)
                answer += 1
                # print("end search\n")

    # print("visited : ", visited)
    print(answer)