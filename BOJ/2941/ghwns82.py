C_alpha = ["c=", "c-", "dz=","d-","lj","nj","s=","z="]
my_txt = input()
for i in C_alpha:
    if i in my_txt:
        my_txt=my_txt.replace(i,"^")
print(len(my_txt))

# 오해한것

# 중국어의 성조처럼 =나 -가 있고, 중국어의 권설음인(ch, zh, sh) 처럼 하나의 크로아티아 알파벳의 dz도 한 문자로 된 것이 있음이라는 뜻으로 이해했었다.
# ez한 문제를 잘못 이해하면 이렇게 되는 구나를 오늘 느낌(5622번 다이얼 문제도 마찬가지)
