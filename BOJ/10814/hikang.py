N = int(input())

judge_list = []
for i in range(N):
  judge_list.append(list(input().split()))

# 나이 순으로 정렬 // int(x[0]) = 나이
judge_list.sort(key=lambda x:int(x[0]))

# 정렬된 리스트에서 나이, 이름 출력
for i in range(N):
  print(judge_list[i][0],judge_list[i][1])