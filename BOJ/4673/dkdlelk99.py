def d(n):
    return n + sum(list(map(int, str(n))))


self_num = [0] * 10001

for i in range(1,10001):
    if self_num[i] == 0:
        a = i
        while d(a) <= 10000:
            a = d(a)
            self_num[a] = 1

for i in range(1, len(self_num)):
    if self_num[i] == 0:
        print(i)
