def move (start, goal, rest, floor):
    if floor == 1:
        print(start, goal)
        return 0
    move(start, rest, goal, floor-1)
    move(start, goal, rest, 1) 
    move(rest, goal, start, floor-1)
    
    
num = int(input())
print(2**num-1)
move(1,3,2, num)
