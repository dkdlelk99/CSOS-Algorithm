# 4949
# 성공
import re

while (line:= input()) !=".":
    line = re.sub('[0-9a-zA-Z ]', "",line)[:-1]

    while 1:
        if line.find("[]") == -1 and line.find("()")==-1 and line:
            print("no")
            break
        if not line:
            print("yes")
            break
        else:
            line=line.replace("[]","").replace("()","")
