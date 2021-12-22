# 1676

num = 1
count =0
for i in range(1, 1+int(input())):
    num *= i

while num%5==0:
    num = num // 5
    count+=1
    
print(count)
