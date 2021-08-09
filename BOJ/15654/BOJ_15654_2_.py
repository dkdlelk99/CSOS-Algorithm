#N과 M(5)의 두번째 방식
#리스트에 숫자를 입력받을때 문자로 입력 받아도 결과는 같게 나와서
#처음에 틀렸다고 했을때 이해가 되지 않았었는데 생각해보니
#만약 9과 11을 문자로 받는다면 오름차순으로 나타내면
#11 9로 숫자의 오름차순과 결과값이 틀리다
#따라서 입력은 숫자로 받고 정렬한 다음 출력시에만 문자로 출력한다

from itertools import permutations
n,m=map(int,input().split())
l=list(map(int,input().split()))
l=sorted(l)
result=list(permutations(l,m))

for i in result:
    print(" ".join(map(str,i)))