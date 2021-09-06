num = int(input())
word_list = []

for i in range(num):
    word_list.append(input())
set_list = list(set(word_list))	
set_list.sort()
set_list.sort(key = len)

for i in set_list:
    print(i)
