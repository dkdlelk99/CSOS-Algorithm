def self_number(num):
    return num + sum(map(int, str(num)))

Self_num = set(range(1, 10001))
for i in range(1, 10001):
    if (a:= self_number(i)) < 10001:
        Self_num.discard(a)

for i in Self_num:
    print(i)
