import sys
# input
N = int(sys.stdin.readline())
meetings = []
for _ in range(N):
    meetings.append(tuple(map(int, sys.stdin.readline().split())))
meetings.sort(key=lambda x:(x[1], x[0])) # 끝나는 시간순으로 정렬, 끝나는 시간이 같으면 시작 시간순으로 정렬

answer, fast = 0, 0 # fast는 다음 회의를 가장 빨리 시작할 수 있는 시간
for i in range(N):
    start, end = meetings[i][0], meetings[i][1]
    if fast <= start: # 시작할 수 있으면 시작해라
        answer += 1
        fast = end
print(answer)