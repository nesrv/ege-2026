from itertools import product



words = product("АСТЕК",repeat=8)


for i,word in enumerate(words,1):
    word = ''.join(word)
    if word == 'АТТЕСТАТ':
        c1= i
    if ('ТЕСАК' in word and \
         not 'ТТ' in word and
         not 'КК' in word):
        c2 = i

print (c2-c1)

