import sys
N = int(sys.stdin.readline())
stack=[]

for i in range(N):
    cmd = sys.stdin.readline().split()
    
    # 명령에 따라 처리해주는 프로그램

    # 입력 받은 정수 cmd[1]을 스택에 넣어줌
    if cmd[0]=='push':
        stack.append(cmd[1])
    elif cmd[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if len(stack)==0:
            print(-1)
        # 스택 가장 위 stack[-1]을 프린트
        else:
            print(stack[-1])