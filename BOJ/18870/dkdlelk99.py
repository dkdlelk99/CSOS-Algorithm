import sys
# input
N = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
list = [] # '입력 받은' 대로의 인덱스 정보가 들어갈 list
for i, val in enumerate(x):
    list.append((val,i))
list.sort(key=lambda x:x[0]) # 입력받은 기존의 인덱스 정보가 담김, 즉 2차원
answer = [-1] * N
rank = 0
answer[list[0][1]] = rank # 가장 작은 값(= list[0][0])의 인덱스에 0 넣기

for i in range(1, N): # value가 같으면 rank의 값이 증가하지 않음
    if list[i-1][0] != list[i][0]:
        rank += 1
    answer[list[i][1]] = rank

print(' '.join(map(str, answer)))