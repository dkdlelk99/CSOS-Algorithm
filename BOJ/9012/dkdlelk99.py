import sys
#Input
T = int(sys.stdin.readline())
PS = []
for i in range(T):
    PS.append(sys.stdin.readline()[:-1])

for str in PS:
    stack = []
    Check = True
    for c in str:
        if c == '(':
            stack.append("(")
        elif c == ')':
            if len(stack) == 0: # ( 이게 하나도 없는데 )가 먼저 튀어나오면 무조건 틀린거임 e.g. )()(() 이런거 잡아야됨
                Check = False
                continue
            stack.pop()
    if len(stack) != 0:
        Check = False
    print("YES" if Check else "NO")