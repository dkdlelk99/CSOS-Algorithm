"""
접근 방법
1. 인접하는 인덱스 값이 같으면 패스
2. i번째 값이 i+1부터 해당하는 문자열에 존재하면 입력 받은 N에 -1
"""

N = int(input())

for _ in range(N):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            pass
        elif word[i] in word[i+1:]:
            N-=1
            break
print(N)
