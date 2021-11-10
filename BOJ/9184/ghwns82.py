memo = {}
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if (key:=" ".join(map(str,[a,b,c]))) in memo.keys():
        return memo[key]
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    if a < b and b < c:
        memo[key] = w(a,b,c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[key]    
    memo[key] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return memo[key]

while(1):
    a,b,c = map(int, input().split())
    if[a,b,c]==[-1,-1,-1]:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
