A,B = map(int,input().split())

# 수 비교해서 알맞은 부등호 출력
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')