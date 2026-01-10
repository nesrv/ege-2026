s = open("24/107_24.txt").read().replace('AB','x').replace('CB','x')
k = m = 0
for c in s:
    if c == 'x':
        k += 1
        m = max(m, k)
    else:
        k = 0
print(m)


s = open('24/107_24.txt').read().replace('AB','x').replace('CB','x')
k = m = 0
for c in s:
    k = k + 1 if c == 'x' else 0
    m = max(m, k)
print(m)


s = open('24/107_24.txt').read().replace('AB','x').replace('CB','x')

print(max(len(part) for part in s.replace('A','|').replace('B','|').replace('C','|').split('|')))