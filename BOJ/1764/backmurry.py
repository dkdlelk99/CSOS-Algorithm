def intersection(a,b):
    aa, bb = set(a), set(b)
    return list(aa & bb) 

n,m = map(int,input().split())
list1 = []
list2 = []

for _ in range(n):
    temp=input()
    list1.append(temp)
for _ in range(m):
    temp=input()
    list2.append(temp)

comm_list = sorted(intersection(list1, list2))
print(len(comm_list))

for i in comm_list:
    print(i)
