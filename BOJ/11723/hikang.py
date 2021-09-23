import sys

M = int(sys.stdin.readline())
S = set()

for i in range(M):
  arr = sys.stdin.readline().rstrip().split(' ')

  if arr[0] == "add":
    S.add(int(arr[1]))
  elif arr[0] == "remove":
    if int(arr[1]) in S:
      S.remove(int(arr[1]))
    else:
      pass
  elif arr[0] == "check":
    if int(arr[1]) in S:
      print(1)
    else:
      print(0)
  elif arr[0] == "toggle":
    if int(arr[1]) in S:
      S.remove(int(arr[1]))
    else:
      S.add(int(arr[1]))
  elif arr[0] == "all":
    S = set(range(1,21))
  elif arr[0] == "empty":
    S = set()