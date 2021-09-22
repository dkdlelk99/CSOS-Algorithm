# 2750
list_ =[]
for _ in range(int(input())):
    list_.append(int(input()))
for i in range(len(list_)):
    for j in range(i,len(list_)):
        if list_[i]> list_[j]:
            list_[i], list_[j] = list_[j], list_[i]

[print(i) for i in list_]
