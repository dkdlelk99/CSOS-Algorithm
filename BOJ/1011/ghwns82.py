import math
for _ in range(int(input())):
    start, end = map(int, input().split())
    distance = end -start
    max_spped = math.floor(math.sqrt(distance))
    remainder = distance - max_spped*max_spped
    num = max_spped*2 -1
#     print(remainder)

    while remainder > 0:
        if remainder%max_spped:
            max_spped -=1
#             print("remainder%max_spped", remainder%max_spped)
        num+=remainder//max_spped
        remainder = remainder%max_spped
#         print("num+=remainder//max_spped", num)
#         print("remainder = remainder%max_spped", remainder)

    print(num)

# 접근방법

# 빨리 도착하기 위해서는 최대한 빠른 속도로 가면 된다. 

# 문제의 조건(처음과 마지막을 1의 속도로 하고 가속, 감속이 1밖에 안된다)을 고려한다면
# 속도를 2까지 낼 수 있는 거리는, 1 + 2 +  1 = 4광년, 4광년부터다.
# 속도를 3까지 낼 수 있는 거리는, 1 + 2 + 3 + 2 + 1 = 9광년부터다.

# 만약 거리가 8광년 이라면, 1+2+1 = 4광년, 나머지 4광년은 2의 속도로 두번 더 달리면 된다. 따라서 공간이동 기계를 작동시키는 횟수는 3+2 = 5번이다

# 공부하다가 미친 풀이과정 발견함.
# 이 공식을 쓰면 답이 한번에 나옴
# num = int(2*math.sqrt(distance - 0.5))
