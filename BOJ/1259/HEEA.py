while True:
    l=list(input())
    if(l[0]=='0'):
        break
    l_reverse=list(reversed(l))
    if(l==l_reverse):
        print("yes")
    else:
        print("no")