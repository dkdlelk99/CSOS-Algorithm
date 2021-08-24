# 시험 본 과목 개수 N개, 해당 시험 성적
N = int(input())
grade = list(map(int, input().split()))

M = max(grade)
sum = 0
for i in range(N):
  # 새로운 평균을 구하는 식
  grade[i] = grade[i]/M*100
  sum+=grade[i]

print(sum/N)