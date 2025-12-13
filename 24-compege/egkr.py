'''
Задание 24 (№25361).
'''

s = open('24-compege/24_25361.txt').read()
s = s.replace('0', '*').replace('2', '*').replace('4', '*').replace('6', '*').replace('8', '*')
parts = s.split('*')

res = [x for x in parts if 76 <= x.count('F') <= 77]

if res:
    print(len(max(res, key=len)))
else:
    print(0)
