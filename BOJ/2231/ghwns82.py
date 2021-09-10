N = input()
len_=len(N)
num=int(N)
for i in range(max(num-len_*9, 1) , num):
    if (i + sum(map(int, str(i)))) == num:
        print(i)
        break
else:
    print(0)
