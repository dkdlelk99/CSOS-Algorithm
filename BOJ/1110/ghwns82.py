future = [int(input())]
while True:
    future.append(future[-1]%10 *10 + (future[-1]//10 + future[-1]%10)%10)
    if future[0] == future[-1]:
        print(len(future)-1)
        break
