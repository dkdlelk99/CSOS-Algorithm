N = int(input())

user = [ [int((a:=input().split())[0]), a[1] ] for _ in range(N)]

user.sort(key=lambda x:int(x[0]))


for i in user:
  print(i[0], i[1])
