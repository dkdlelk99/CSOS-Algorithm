# 그룹단어 체크함수
def check(word):
    b=set()
    for i in word:
        if i not in b:
            b.add(i)
            status = i
        elif status == i:
            continue
        else:
            return 0
    return 1
 
# 테스트 실행
print(sum([check(input()) for _ in range(int(input()))]))
