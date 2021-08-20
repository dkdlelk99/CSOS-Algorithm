for _ in range(int(input())):
    score = 0
    for i in input().split("X") :
        score += len(i)*(len(i)+1)//2
    print(score)

# 한줄코딩
# 이게 한줄이 되넹
# 한줄코딩을 잘 쓰면 메모리도 아끼고 시간도 줄일 수 있다... 메모리는 그대론데 시간은 4ms 줄었다.

# [print(sum(len(i)*(len(i)+1)//2 for i in input().split('X'))) for _ in range(int(input()))]
