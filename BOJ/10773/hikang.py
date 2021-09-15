import sys

K = int(sys.stdin.readline())
list = []

for i in range(K):
  element = int(sys.stdin.readline())
  if(element==0):
    list.pop()
  else:
    list.append(element)

print(sum(list))