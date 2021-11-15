n = int(input())
member_lst = []

for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member_lst.append((age,name)) # 튜플화

member_lst.sort(key = lambda member: (member[0])) # 정렬 목적으로하는 람다식 [0 ]= age로  sort

for member in member_lst:
    print(member[0], member[1])
