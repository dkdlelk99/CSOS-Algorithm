import sys

n=int(sys.stdin.readline())

result=0
help=1000000007

def power(exp):
    if(exp<0): #미분한 식의 지수가 0보다 작으면 항이 사라짐
        return 0
    else: #2의 거듭제곱 구하기
        a=2
        value=1
        exp_bin=format(exp,'b')
        exp_bin="".join(reversed(exp_bin))
        for i in exp_bin:
            if(i=='1'):
                value=int(value*a%help)
            a=int(a**2%help)
        return value

for _ in range(n):
    c, k=map(int,sys.stdin.readline().split()) #항의 계수와 항의 차수 입력 받아 리스트에 저장
    result+=c*k*power(k-1)
    
print(int(result%help))