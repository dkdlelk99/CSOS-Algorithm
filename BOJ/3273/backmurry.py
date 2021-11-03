n = int(input())
n_lst = list(map(int, input().split(" ")))
n_lst.sort()

x = int(input())


left = 0
right = n - 1
cnt = 0
while left < right:
    temp= n_lst[left]+n_lst[right]
    if temp ==x : cnt +=1
    if temp < x : 
        left+= 1
        continue
    right-=1
print(cnt)
