n = int(input())
words = []
for i in range(n):
    word = input()
    if [word,len(word)] in words:
        continue
    words.append([word,len(word)])
words = sorted(words,key=lambda x:(x[1], x[0]))
for i in words:
    print(i[0])
