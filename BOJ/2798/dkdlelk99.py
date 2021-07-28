N, M = map(int, input().split())
deck = list(map(int, input().split()))
ans, mindiff, cards = 0, 987654321, len(deck)
for i in range(cards):
    for j in range(i+1, cards):
        sum = 0
        for k in range(j+1, cards):
            sum = deck[i] + deck[j] + deck[k]
            if M-sum <= mindiff and sum <= M:
                mindiff = M - sum
                ans = sum
print(ans)