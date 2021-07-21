T = int(input()) # test case
for _ in range(T):
    k, n = int(input()), int(input()) #k: floor, n: room number
    floor = list(range(1, n+1))
    for i in range(k):
        sum = 0
        for room in range(n):
            sum += floor[room]
            floor[room] = sum
    print(sum)