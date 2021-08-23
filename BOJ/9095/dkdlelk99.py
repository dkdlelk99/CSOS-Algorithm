import sys
T = int(sys.stdin.readline())
def make(case): # answer에 가능한 경우의 수열 리스트를 집어 넣는 함수
    S = sum(case)
    if S == n: # 기저 조건(수열의 합이 입력 n과 같으면 answer에 append)
        answer.append(case)
        return
    else: # 1,2,3 더할 수 있으면 더하고 recursion
        if S + 1 <= n:
            case.append(1)
            make(case)
            case.pop()
        if S + 2 <= n:
            case.append(2)
            make(case)
            case.pop()
        if S + 3 <= n:
            case.append(3)
            make(case)
            case.pop()
        return
# solve
for i in range(T):
    n = int(sys.stdin.readline())
    arr = [] # 수열
    answer = [] # arr을 담을 리스트
    make(arr)
    print(len(answer))