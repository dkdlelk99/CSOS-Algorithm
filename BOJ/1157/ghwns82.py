a = input().upper()
b = list(set(a))
c = [a.count(i) for i in b]
if c.count(max(c)) >1:
    print("?")
else:
    print(b[c.index(max(c))])
