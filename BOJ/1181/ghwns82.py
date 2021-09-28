N = int(input())

word = list(set([ input() for _ in range(N)]))

sort_word = sorted([[len(i),i]for i in word])

for i in sort_word:
    print(i[1])
