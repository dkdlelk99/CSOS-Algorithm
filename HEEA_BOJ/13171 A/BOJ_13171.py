a=int(input())
x=int(input())

x_bin=format(x,'b') #2진수로 변환
x_bin="".join(reversed(x_bin)) #변환한 2진수 반전

result=1

for i in x_bin:
    if(i=='1'):
        result=int((result*a)%1000000007) #2진수에서 1일 경우에만 해당된 거듭제곱 수를 곱함
    a=int(pow(a,2)%1000000007) #2진수로 만들었기 때문에 지수 역시 2의 거듭제곱으로 커지게 만듬
print(result)