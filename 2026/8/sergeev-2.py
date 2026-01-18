from itertools import product

words = product("ЕГЭ026", repeat=6)
c= 0

for word in words:
    sum_digits = [int(x) for x in word if x.isdigit()]
    if sum(sum_digits) == 8:
        c+=1

print(c)