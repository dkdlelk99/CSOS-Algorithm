# 10870

N = int(input())
def piv(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        return piv(num-1) + piv(num-2)
print(piv(N))
