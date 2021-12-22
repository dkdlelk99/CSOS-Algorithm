# 11866

n, k = map(int, input().split())

people = [i for i in range(1,n+1)]
yo_se = []

index=-1
while people:
    index = (index+k)%n
    yo_se.append(people.pop(index))
    index -=1
    n -=1

print(str(yo_se).replace("[", "<").replace("]", ">"))
