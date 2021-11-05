str_name=input()
token=input()
len_t= len(token)
cnt=0
while str_name.find(token)!= -1 : 
    len_strip= str_name.find(token)+len_t
    str_name=str_name[len_strip:]
    cnt+=1
print(cnt)
