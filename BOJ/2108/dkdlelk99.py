import sys
# input
N = int(sys.stdin.readline())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))
num.sort()

# check frequency
freq = dict()
for i in range(-4000,4001):
    freq[i] = 0
for i in num:
    freq[i] += 1

max_freq = sorted([k for k,v in freq.items() if max(freq.values()) == v])
answer = max_freq[0] if len(max_freq) == 1 else max_freq[1]
# output
print(round(sum(num)/len(num)), num[len(num)//2], answer, num[-1] - num[0], sep='\n')
