array = []

for _ in range(9):
  n = int(input())
  array.append(n)

print(max(array))
print(array.index(max(array)) + 1)

