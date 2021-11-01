# 14889
import itertools
N = int(input())
synergy_table = [list(map(int, input().split())) for _ in range(N)]
teams=list(itertools.combinations([i for i in range(N)], N//2))
A_vs_B = [[teams[i], teams[-i-1]]for i in range(len(teams)//2)]

result=[]
for turn in A_vs_B:
    A=sum([synergy_table[i][j] for i in turn[0] for j in turn[0]])
    B=sum([synergy_table[i][j] for i in turn[1] for j in turn[1]])
    result.append(abs(A-B))
print(min(result))
