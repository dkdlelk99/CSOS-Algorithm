a1,a2 = map(int, input().split())
b1,b2 = map(int, input().split())
c1,c2 = map(int, input().split())

x = [a1,b1,c1]
y = [a2,b2,c2]

print(2*sum(set(x)) - sum(x) ,2*sum(set(y)) - sum(y))
