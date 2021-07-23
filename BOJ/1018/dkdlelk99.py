import sys
#Input
N, M = map(int, sys.stdin.readline().split())
board = []
for i in range(N):
    board.append(sys.stdin.readline()[:-1])

line = ["BWBWBWBW", "WBWBWBWB"]
ans = 1250

# 문자열 비교 함수 (return 다른 문자 개수)
def diffNum(s1, s2):
    diff = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]: diff += 1
    return diff

# 8x8 mask를 모든 영역에 돌리기
for y in range(N-7):
    for x in range(M-7):
        a, b = 0, 0
        for n in range(8):  # 체스 보드 BW~~ 시작하면 다음줄은 WB~~ 임 그래서 % 써서 이를 만들어줌
            a += diffNum(line[n%2], board[y + n][x:x + 8])      # 케이스1 BW 시작
            b += diffNum(line[(n+1)%2], board[y + n][x:x + 8])  # 케이스2 WB 시작
        ans = min(a,b,ans)  # 가장 작게 바꿔도 되는 개수를 ans에 저장
print(ans)