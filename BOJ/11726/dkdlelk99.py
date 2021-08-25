answer = [1]*1000
answer[1] = 2
for i in range(2, 1000):
    answer[i] = answer[i-1] + answer[i-2]
print(answer[int(input()) - 1]%10007)
