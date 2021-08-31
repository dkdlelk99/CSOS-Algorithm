import math

X = int(input())
inverse_X= (math.sqrt(X*8 + 1) - 1)/2
n = math.ceil(inverse_X) 
a_n = n*(n+1)//2
diff = a_n-X


if n%2:
    print(f"{diff+1}/{n-diff}")
else:
    print(f"{n-diff}/{diff+1}")
