# x, y = map(int,input().split())
x = int(input())
y = int(input())

# 사분면 생각!
if x > 0 and y > 0:
  print('1')
elif x > 0 and y <0:
  print('4')
elif x < 0 and y > 0:
  print('2')
else:
  print('3')