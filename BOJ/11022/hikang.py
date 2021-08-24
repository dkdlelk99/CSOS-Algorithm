T = int(input())

for i in range (T):
  A, B = map(int,input().split())
  add = A + B
  print("Case #%s: %s + %s = %s"%(i+1,A,B,add))