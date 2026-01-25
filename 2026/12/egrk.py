s = [' ', *list(bin(2028))[2:], ' ']
print (s)
trans = {
    (0, '1'): (0, '1'),
    (0, '0'): (0, '0'),
    (1, '1'): (1, '0'),
    ('1', '1'): ('1', '1')
}
i = 1
x, q = '1', '1'

while s[i] != ' ':
    print (s[i], x)
    q,x = trans[s[i], q]
    s[i] = x
    i += 1

print (s) # 8112

# print(s.count(0))
