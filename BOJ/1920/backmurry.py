n = int(input())
n_lst = list(map(int, input().split(" ")))
n_lst.sort()

m = int(input())
m_lst = list(map(int, input().split(" ")))

for i in range(m):
    token =True
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if n_lst[mid] == m_lst[i]:
            token= False
            print(1)
            break
        if m_lst[i] < n_lst[mid]:
            right = mid-1
        elif m_lst[i] > n_lst[mid]:
            left = mid + 1
    if token:
        print(0)
