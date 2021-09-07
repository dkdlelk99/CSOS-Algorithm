# 4153

while( sum(length_list:= list(map(int, input().split())))):
    if max(length_list)*2 >= sum(length_list):
        print("wrong")
    elif max(length_list)**2*2 == sum([i**2 for i in length_list]):
        print("right")
    else:
        print("wrong")
