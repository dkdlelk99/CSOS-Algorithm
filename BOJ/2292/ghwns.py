import math

room_num=int(input())
room_floor_info=(room_num-1)/6
print(
    math.ceil((math.sqrt(room_floor_info * 8 + 1) + 1)/2)
)

# 접근방법
# 수학문제 풀듯이 접근
# 거리가 1씩 증가할때 방은 6, 12, 18... 씩 증가 이를 계차수열이라함 
# 거리에 따른 방의 개수에 대한 관계식을 구한다.
# 문제에서는 방번호를 주므로 올림을 사용하면 방의 개수를 알 수 있고 방의 개수를 구하여 역으로 거리를 계산할 수 있다.

 
