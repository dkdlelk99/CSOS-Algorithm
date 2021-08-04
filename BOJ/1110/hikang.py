N = end_num = int(input())
cycle = 0

while True:
  f_num = N//10 + N%10
  s_num = (N%10)*10 + f_num%10
  cycle +=1
  N = s_num
  if s_num == end_num:
    break

print(cycle) 