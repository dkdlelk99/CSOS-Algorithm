N,M = map(int, input().split())
chess = [input() for _ in range(N)]
count_list = []


for x in range(N-7):
    for y in range(M-7):
        idx1 = 0
        idx2 = 0
        for b in range(x, x + 8):
            for j in range(y, y + 8):              
                if (j + b)%2 == 0:
                    if chess[b][j] != 'W': idx1 += 1  
                    if chess[b][j] != 'B': idx2 += 1
                else :
                    if chess[b][j] != 'B': idx1 += 1
                    if chess[b][j] != 'W': idx2 += 1
        count_list.append(idx1)                          
        count_list.append(idx2)                          

print(min(count_list))               
