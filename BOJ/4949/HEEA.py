import re

result=[]
while True:
    st=input()
    if(st=='.'):
        break
    st=re.sub('[ a-zA-Z0-9]+', '',st)
    while True:
        if(st.find("()")==-1 and st.find("[]")==-1):
            break
        st=st.replace("()","")
        st=st.replace("[]","")
    if(st=='.'):
        result.append('yes')
    else:
        result.append('no')

for i in result:
    print(i)
