import sys
# input
N, M = map(int, sys.stdin.readline().split())
pocketmon = []      # 문제의 입력이 숫자일때 사용할 리스트
pocketmon_dict = {} # 문제의 입력이 이름일때 사용할 딕셔너리
for i in range(N): # 도감 입력
    pocketmon.append(sys.stdin.readline().rstrip()) # 리스트에 이름을 하나씩 추가
    pocketmon_dict[pocketmon[i]] = i + 1            # 딕셔너리에 추가된 이름에 해당하는 번호를 추가
for _ in range(M): # 퀴즈 풀기
    Q = sys.stdin.readline().rstrip()
    if Q.isdigit(): # 입력이 숫자라면
        print(pocketmon[int(Q) - 1]) # 리스트에서 해쉬
    else: # 입력이 이름이라면
        print(pocketmon_dict[Q]) # 딕셔너리에서 해쉬
