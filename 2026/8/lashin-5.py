from itertools import product
c = 0
words = product("СДАЙЕГЭ", repeat=6)

for i, word in enumerate(sorted(words),1):
    word = ''.join(word)  
    if 'ЕГЭ'in word:
        c+=i


print(c)

