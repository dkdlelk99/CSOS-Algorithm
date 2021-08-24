C = int(input())
count = 0

for i in range(C):
  grade = list(map(int,input().split()))
  average = sum(grade[1:])//grade[0]
  
  # 평균을 넘는 학생 count
  for j in grade[1:]:
    if average < j :
      count += 1
  
  # 평균을 넘는 학생의 비율
  print("%.3f%%"%((count/grade[0])*100))
  count = 0