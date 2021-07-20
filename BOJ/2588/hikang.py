A = int(input())
B = int(input())

# (n자리수) * (세자리수) 경우의 곱셈 문제만 해당~!
print(A*(B%10),A*((B//10)%10),A*(B//100),A*B, sep = '\n')