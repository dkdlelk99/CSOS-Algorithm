# 10816
# 성공
input()
cards = {}
for i in list(map(int, input().split())):
    if i in cards.keys():
        cards[i]+=1
    else:
        cards[i]=1
input()
for i in list(map(int, input().split())):
    if i in cards.keys():
        print(cards[i], end=" ")
    else:
        print(0, end=" ")
