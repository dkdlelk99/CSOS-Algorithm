result=0
for i in range(5):
    score=int(input())
    if(score>=40):
        result+=score
    else:
        result+=40
print(int(result//5))
