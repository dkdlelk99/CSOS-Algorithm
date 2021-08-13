#방법 1
import sys
a = int(sys.stdin.readline())
my_score=0
for score in (b := list(map(int, sys.stdin.readline().split()))):
    my_score += score*100/max(b)
print(my_score/a)

#방법 2
import sys
a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
print(sum(b)*100/max(b)/a)
