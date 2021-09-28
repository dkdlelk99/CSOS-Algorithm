word = list(input())
t_list = []
temp = []
for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word) ):
        word1 = word[:i]
        word2 = word[i:j]
        word3 = word[j:]
        word1.reverse()
        word2.reverse()
        word3.reverse()
        temp.append(word1 + word2 + word3)
for w in temp:
    t_list.append("".join(w))
print(sorted(t_list)[0])
