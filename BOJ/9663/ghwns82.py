# 9663
N = int(input())

chess = [[0 for _ in range(N)]for i in range(N)]


def backT(idx):
    result=0
    if idx == N-1:
        return chess[idx].count(0)
    
    if 0 not in chess[idx]:
        return False
    
    for i in range(N):
        if chess[idx][i] ==0:
            chess_on_queen(idx, i, 1)
            result += backT(idx+1)
            chess_on_queen(idx, i, -1)
    return result
                
        
def chess_on_queen(x,y, take_place):
    for n in range(N):
        chess[n][y]+=take_place
        chess[x][n]+=take_place
        if 0<=(n+y-x)<N:
            chess[n][n+y-x]+=take_place
        if 0<=(y+x-n)<N:
            chess[n][y+x-n]+=take_place
print(backT(0))
