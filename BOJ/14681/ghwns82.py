print([2,1,3,4][[i[0]//abs(i[0]) + (i[1]*2)//abs(i[1]) for i in [list(map(int, input().split()))]][0]//2])
