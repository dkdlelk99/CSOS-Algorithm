table = [list(map(int, input().split())) for _ in range(int(input()))]
for i in table:
    rank = 1
    for j in table:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")
    
# table = [list(map(int, input().split())) for _ in range(int(input()))]
# new_table = table[:]
# new_table.sort(reverse=True)
# new_table[0].append(1)
# for i in range(1, len(new_table)):
#     if new_table[i-1][0] > new_table[i][0] and new_table[i-1][1] > new_table[i][1]:
#         new_table[i].append(i+1)
#     else:
#         new_table[i].append(new_table[i-1][2])
# for i in table:
#     print(i[2], end = "")
