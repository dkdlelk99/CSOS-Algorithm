#1764

name_list = {}
for _ in range(sum(list(map(int, input().split())))):
    if (name:=input()) in name_list.keys():
        name_list[name]+=1
    else:
        name_list[name] = 1

result = sorted([name for name in list(name_list.keys())  if name_list[name]==2])
print(len(result))
for i in result:
    print(i)
