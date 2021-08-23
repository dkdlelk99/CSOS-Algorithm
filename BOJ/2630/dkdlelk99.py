import sys
# input
N = int(sys.stdin.readline())
paper = []
for i in range(N):
    paper.append(sys.stdin.readline().replace(" ", "").rstrip())


def is_paper(x,y,n):
    # 하나의 색종이인지 검사해서 맞으면 true 아니면 false를 리턴
    # x,y는 좌표, n은 가로 세로 크기
    check = paper[y][x]
    for i in range(n):
        for j in range(n):
            a = paper[y+i][x+j]
            if check != a:
                return False
    return True


answer = [0, 0]


# 풀이
def solution(x,y,n):
    if is_paper(x,y,n):
        # 더 이상 쪼갤 수 없는 색종이라면 답 추가
        if paper[y][x] == '0':
            answer[0] += 1
        else:
            answer[1] += 1
        return
    else:
        # 쪼갤 수 있으면 4분할 후 정복
        d = n//2
        solution(x,y,d)
        solution(x+d, y, d)
        solution(x, y+d, d)
        solution(x+d, y+d, d)

solution(0,0,N)
print(answer[0],answer[1],sep='\n')