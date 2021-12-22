# 15829

CONSTANT = 96
input()
print(sum([(ord(v)- CONSTANT) * (31**i) for i,v in enumerate(input())])%1234567891)
