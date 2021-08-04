import sys, collections
# input
N = int(sys.stdin.readline())
# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.stack = []
de = collections.deque()
for _ in range(N):
    instruction = list(sys.stdin.readline().split())
    if instruction[0] == "push_front":
        de.appendleft(int(instruction[1]))
    elif instruction[0] == "push_back":
        de.append(int(instruction[1]))
    elif instruction[0] == "pop_front":
        print(-1 if len(de) == 0 else de.popleft())
    elif instruction[0] == "pop_back":
        print(-1 if len(de) == 0 else de.pop())
    elif instruction[0] == "size":
        print(len(de))
    elif instruction[0] == "empty":
        print(1 if len(de) == 0 else 0)
    elif instruction[0] == "front":
        print(-1 if len(de) == 0 else de[0])
    elif instruction[0] == "back":
        print(-1 if len(de) == 0 else de[-1])