while True:
        a = list(map(int, input().split()))
        max_num = max(a)
        if sum(a) == 0:
                break
        a.remove(max_num) #제일 큰 값을 리스트에서 삭제시킴
        if a[0] ** 2 + a[1] ** 2 == max_num ** 2:
                print('right')
        else:
                print('wrong')
