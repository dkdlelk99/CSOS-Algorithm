print([1 if (not i%4 and i%100 or not i%400) else 0 for i in [int(input())]][0])
