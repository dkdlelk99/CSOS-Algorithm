N = input()

list = []
for i in N:
  list.append(i)

# 오름차순으로 정렬된 리스트의 순서 뒤집기 = 내림차순
list.sort(reverse=True)
print(''.join(list))