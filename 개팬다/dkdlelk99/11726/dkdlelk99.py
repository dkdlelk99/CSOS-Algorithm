n = int(input())
board = [0]*n
answer = [0]
# make answer
def make(index):
    if index == n:
        answer[0] += 1
        return
    else:
        left = n - index
        if left > 0:
            board[index] = 1
            make(index+1)
            board[index] = 0
        if left > 1:
            board[index] = 2
            board[index+1] = 2
            make(index + 2)
            board[index] = 0
            board[index+1] = 0


make(0)
print(answer[0]%10007)
