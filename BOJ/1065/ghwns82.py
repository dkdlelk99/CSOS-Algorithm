# 방법 1
# 4자리 수 이상 사용가능

# han_list = set()

# def han_num(num):
#     if num < 100:
#         return True

#     num_array = list(map(int, str(num)))
#     for i in range(len(num_array)-1):
#         if num_array[i+1] - num_array[i] != (d := num_array[1] - num_array[0]):
#             return False
#     return True


# for i in range(1, int(input())+1):
#     if han_num(i):
#         han_list.add(i)

# print(len(han_list))

# 방법 2

han_list = set()

for i in range(1, int(input())+1):
    # 등비수열 공식 이용
    if i//100 + i%10 == i//10%10 * 2  or i<100 :
        han_list.add(i)
# print(han_list)
print(len(han_list))

# 방법 3
# 한줄 코딩
# print(sum([i//100 + i%10 == i//10%10 * 2  or i<100 for i in range(1, int(input())+1)]))
