st=input().split('-')

i=1
result=-1
if(st[0].find('+')==-1):
    result=int(st[0])
else:
    swap=st[0].split('+')
    result=int(swap[0])
    for j in range(1,len(swap)):
        result+=int(swap[j])

while True:
    if(i==len(st)):
        break
    if(st[i].find('+')!=-1):
        swap=st[i].split('+')
        dis=int(swap[0])
        for j in range(1,len(swap)):
            dis+=int(swap[j])
        result-=dis
    else:
        result-=int(st[i])
    i+=1
print(result)
