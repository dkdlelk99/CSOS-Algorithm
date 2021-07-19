a=int(input())
a_bin=format(a,'b') #2진수로 변환해주는 함수 bin()의 경우 접두오 #0b가 붙기 때문에 접두어를 제외한 수를 사용해야 하므로 format을 사용해서 제거하기
a_bin="".join(reversed(a_bin)) #문자열 반전 시키기
start=0 #지수 체크 변수
sum=0 #서로 다른 제곱수의 합
for i in a_bin:
    if(i=='0'):
        start+=1
    else:
        sum+=pow(3,start)
        start+=1
print(sum)
