divisor_num =int(input())
divisor_list =list(map(int, input().split()))

if len(divisor_list) == 1 : 
    print(divisor_list[0]*divisor_list[0])
else:
    divisor_list.sort() 
    print(divisor_list[0]*divisor_list[-1])
