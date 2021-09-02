import sys

n,new,p=map(int, sys.stdin.readline().split())
score=list(map(int,sys.stdin.readline().split()))
score.append(new)
score.sort(reverse=True)
sum=0
copy_score=score.copy()

num=list(filter(lambda x: score[x]==new, range(len(score)))) # 새로운 수의 등수 구하기


if(num[len(num)-1]>(p-1)):
    print(-1)
else:
    for i in score:
        copy_score=[j for j in copy_score if j!=i] # 동일한 점수 제거
        sum+=1
        if(i==new):
            break
    print(sum)

# 랭킹 리스트에 들어가는 순서와 등수 두 가지 개념이 이 문제에서 사용됨
# p는 순서를 체크하는 랭킹 리스트를 나타낸다.
# 예를 들어 10, 9, 8, 7로 n = 4, 새로운 점수는 7, 랭킹 리스트 p = 4라고 한다면
# 10, 9, 8, 7, 7 로 등수는 4지만, 순서는 5번째이다. 하지만 랭킹 리스트 p는 4로 5보다 작은 수 이므로 출력은 -1 (이 상황이 랭킹 리스트에 올라갈 수 없는 상황임)
