num = int(input())

pre_1, pre_2, now = 1,2,0

for i in range(3, num+1):
    now = (pre_1%15746 + pre_2%15746)%15746
    pre_1, pre_2 = pre_2, now
if num ==1:
    now=pre_1
elif num==2:
    now=pre_2
print(now)
