import sys
from collections import deque

N = int(sys.stdin.readline())
list = deque()

for i in range(N):
  cmd = sys.stdin.readline().split()

  if cmd[0] == 'push_front':
    list.appendleft(cmd[1])
  if cmd[0] == 'push_back':
    list.append(cmd[1])
  if cmd[0] == 'pop_front':
    if int(len(list))>0:
      print(list.popleft())
    else:
      print(-1)
  if cmd[0] == 'pop_back':
    if int(len(list))>0:
      print(list.pop())
    else:
      print(-1)    
  if cmd[0] == 'size':
    print(int(len(list)))
  if cmd[0] == 'empty':
    if int(len(list)) == 0:
      print(1)
    else:
      print(0)
  if cmd[0] == 'front':
    if int(len(list)) != 0:
      print(list[0])
    else:
      print(-1)
  if cmd[0] == 'back':
    if int(len(list)) != 0:
      print(list[-1])
    else:
      print(-1)