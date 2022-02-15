Croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

test_word = input().strip()
answer = len(test_word)

for i in range(len(test_word)):
    for word in Croatia:
        if test_word[i:i + len(word)] == word:
            answer -= 1
            break
print(answer)
