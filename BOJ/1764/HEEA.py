import sys

n,m=map(int,sys.stdin.readline().split())
n_list=[]
m_list=[]
for _ in range(n):
    n_list.append(sys.stdin.readline().rstrip())

for _ in range(m):
    m_list.append(sys.stdin.readline().rstrip())

result=list(set(n_list).intersection(m_list))
result.sort()

print(len(result))
for i in result:
    print(i)
