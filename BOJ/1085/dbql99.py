a,b,c,d = map(int,input("").split()) #a:한수의 x좌표 b: 한수의 y좌표 c: 꼭짓점 w좌표 d: 꼭짓점 h좌표


m = c-a #W-X
n = d-b #h-y

point = [a,b,m,n]
minValue = point[0]

for i in range (0, len(point)):

    if point[i] < minValue:
        minValue = point[i]

print(minValue)


