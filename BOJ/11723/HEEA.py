import sys

m=int(sys.stdin.readline())
s=0

for _ in range(m):
    instructions=list(sys.stdin.readline().split())
    if(instructions[0]=='add'):
        s|=1<<int(instructions[1]) #우리 눈에는 bin()을 쓰지 않아 10진수로 보이지만 bin()을 해보면 실제 자리수 위치의 값이 달라짐(1혹은 0으로)
    elif(instructions[0]=='remove'):
        s&=~(1<<int(instructions[1]))
    elif(instructions[0]=='check'):
        if(s&(1<<int(instructions[1]))):
            print(1)
        else:
            print(0)
    elif(instructions[0]=='toggle'): #xor연산
        s^=1<<int(instructions[1])
    elif(instructions[0]=='all'):
        s=(1<<21)-1 #0부터 20번째 자리까지 1로 나타내기 위함
    else:
        s=0
