# 14888
import itertools


N = int(input())
A = input().split()
op_n = list(map(int, input().split()))
op=['+','-','*','/']
my_op = ""
for i in range(4):
    my_op += op[i]*op_n[i]

my_op2=list(set(itertools.permutations(list(my_op), N-1)))
results=[]
for j in range(len(my_op2)):
    result = int(A[0])
    for i in range(N-1): 
        if my_op2[j][i] == "/" and result<0:
            result = -(eval(str(-(result))+ '//' +A[i+1]))
        elif my_op2[j][i] == "/":
            result = eval(str(result)+ '//' +A[i+1])
        else:
            result = eval(str(result)+ my_op2[j][i]+A[i+1])
    results.append(result)
print(max(results), min(results), sep='\n')
