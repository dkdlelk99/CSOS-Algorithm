import sys
# input
N = int(sys.stdin.readline())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline()))
num.sort()
# check frequency
freq = []
for i in list(set(num)):
    freq.append((num.count(i), i))
freq.sort(key=lambda x: (-x[0], x[1]))
# init mode
if N != 1:
    most_freq = freq[0][1] if freq[0][0] != freq[1][0] else freq[1][1]
else:
    most_freq = freq[0][1]
# output
print(sum(num)//len(num), num[len(num)//2], most_freq, num[-1] - num[0], sep='\n')