T = int(input())

for i in range (T):
  A, B = map(int,input().split())
  add = A + B
  print("Case #%s: %s"%(i+1, add))