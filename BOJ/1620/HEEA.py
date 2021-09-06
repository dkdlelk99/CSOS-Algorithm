import sys

n,m=map(int,sys.stdin.readline().split())
dic={}

for i in range(n):
    dic[sys.stdin.readline().rstrip()]=i+1
reverse_dic=dict(map(reversed, dic.items()))

for _ in range(m):
    q=input()
    if(q.isdigit()):
        print(reverse_dic[int(q)])
    else:
        print(dic[q])

# 시간복잡도 : set, dictionary (O(1))가 list, tuple (O(n))보다 더 빠른 속도