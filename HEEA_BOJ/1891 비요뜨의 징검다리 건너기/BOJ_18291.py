t=int(input()) #테스트 케이스의 수
l=[]

def power(result_bin):
    output=1 #징검다리를 건너는 경우의 수
    a=2 #거듭제곱의 밑
    if(result>=0):
        for i in result_bin: #거듭제곱
            if(i=='1'):
                output=int(a*output%1000000007)
            a=int(pow(a,2)%1000000007)
    return output

for i in range(t):
    n=int(input()) #징검다리의 개수
    result=n-2 #거듭제곱의 지수
    result_bin=format(result,'b')
    result_bin="".join(reversed(result_bin))
    l.append(power(result_bin))

for i in l:
    print(i)
