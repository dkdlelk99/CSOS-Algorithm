import sys
# input
M = int(sys.stdin.readline())
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.
S = set()
for _ in range(M):
    instruction = list(sys.stdin.readline().split())
    if len(instruction) > 1:
        instruction[1] = int(instruction[1])
    if instruction[0] == "add":
        S.add(instruction[1])
    elif instruction[0] == "remove":
        if instruction[1] in S:
            S.remove(instruction[1])
    elif instruction[0] == "check":
        print(1 if instruction[1] in S else 0)
    elif instruction[0] == "toggle":
        if instruction[1] in S:
            S.remove(instruction[1])
        else:
            S.add(instruction[1])
    elif instruction[0] == "all":
        S = set(range(1,21))
    else:
        S = set()