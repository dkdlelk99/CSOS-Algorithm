import sys

N = int(sys.stdin.readline())
list = []

for i in range(N):
  cmd = sys.stdin.readline().split()

  if cmd[0] == 'push':
    list.append(cmd[1])
  if cmd[0] == 'pop':
    if int(len(list))>0:
      print(list.pop(0))
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