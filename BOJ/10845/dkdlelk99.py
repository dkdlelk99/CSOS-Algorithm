import sys, collections
# input
N = int(sys.stdin.readline())

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

de = collections.deque()
for _ in range(N):
    instruction = list(sys.stdin.readline().split())
    if instruction[0] == "push":
        de.append(int(instruction[1]))
    elif instruction[0] == "pop":
        print(-1 if len(de) == 0 else de.popleft())
    elif instruction[0] == "size":
        print(len(de))
    elif instruction[0] == "empty":
        print(1 if len(de) == 0 else 0)
    elif instruction[0] == "front":
        print(-1 if len(de) == 0 else de[0])
    elif instruction[0] == "back":
        print(-1 if len(de) == 0 else de[-1])
