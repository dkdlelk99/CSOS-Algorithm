N = int(input())
room = 0 # 거쳐가야할 방의 개수
sum = 1 # N과 비교할 숫자
while N > sum:
    room += 1
    sum += room*6
print(room+1)
