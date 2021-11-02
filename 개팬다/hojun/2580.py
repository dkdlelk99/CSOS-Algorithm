https://www.acmicpc.net/problem/2580
  
  
from collections import deque
sudoku = [list(map(int, input().split())) for _ in range(9)]
work_list = deque()
for i1, v1 in enumerate(sudoku):
    for i2, v2 in enumerate(v1):
        if not v2:
            work_list.append([i1, i2, v2])
while work_list:
    work = work_list.popleft()
    print("work = ", work)
    if work[0] not in [i[0] for i in work_list]: 
        sudoku[work[0]][work[1]] = 45 - sum([sudoku[work[0]][j] for j in range(9)])
        print(11, work[0], work[1], sudoku[work[0]][work[1]])
    elif work[1] not in [i[1] for i in work_list]:
        sudoku[work[0]][work[1]] = 45 - sum([sudoku[j][work[1]] for j in range(9)])
        print(22, work[0], work[1], sudoku[work[0]][work[1]])
    elif [work[0]//3, work[1]//3] not in [[i[0]//3, i[1]//3] for i in work_list]:
        sudoku[work[0]][work[1]] = 45 - sum([sudoku[k][j] for k in range(work[0]//3*3, (work[0]+3)//3*3) for j in range(work[1]//3*3, (work[1]+3)//3*3)])
        print(33, work[0], work[1], sudoku[work[0]][work[1]])
        print(sum([sudoku[j][work[1]] for k in range(work[0]//3*3, (work[0]+3)//3*3) for j in range(work[1]//3*3, (work[1]+3)//3*3)]))
    else:
        work_list.append(work)
for i in sudoku:
    for j in i:
        print(j, end=' ')
    print()
