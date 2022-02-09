import sys
# input
N = int(sys.stdin.readline())
nums = [0]*10001

for i in range(N):
    nums[int(sys.stdin.readline())] += 1

for i in range(len(nums)):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)
