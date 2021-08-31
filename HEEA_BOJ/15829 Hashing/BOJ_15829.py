l=int(input())
arr=list(input())

sum=0
power=1

for i in range(l):
    sum+=(ord(arr[i])-96)*power%1234567891
    power=power*31%1234567891 #거듭제곱 과정중에도 나눠주기

print(sum%1234567891)