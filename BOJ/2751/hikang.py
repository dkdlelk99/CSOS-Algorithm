N = int(input())
unsorted_list = []

for i in range(N):
  unsorted_list.append(int(input()))

sorted_list = sorted(unsorted_list)

for i in sorted_list:
  print(i)

