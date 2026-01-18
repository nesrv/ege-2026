from itertools import product

words = product("0123456789ABCDEF", repeat=6)
c = 0

for word in words:
    if word[0] != '0' and len(set(word)) >= 5 and '7' in word:
        c += 1


    

print(c)