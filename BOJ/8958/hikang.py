case = int(input())

for i in range(case):

  grade = 0
  count = 0
  for j in input():
    # 입력 받은 값에서 "O" count
    if j == "O":
      count += 1
      grade += count
    # "X"인 경우 count 초기화
    else:
      count = 0
  print(grade)
