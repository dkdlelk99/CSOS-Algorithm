# 중복없는 집합
array = set()

# 입력 값의 나머지를 집합에 추가, set으로 중복 제거
for _ in range(10):
  array.add(int(input())%42)

print(len(array))