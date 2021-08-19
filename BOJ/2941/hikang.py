import sys

text = str(sys.stdin.readline())
Croatia_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

# 크로아티아 리스트에서
for i in range(len(Croatia_list)):
  # i번째에 있는 알파벳이 text에 존재
  for j in range(text.count(Croatia_list[i])):
    # '+' 문자로 대체(하나짜리 문자면 아무거나 상관 ㄴ)
    text = text.replace(Croatia_list[i],'+')

print(len(text))