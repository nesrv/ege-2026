s = [' ' , *[1] * 57, ' ']

i = len(s) - 2
q = 1
while s[i] != ' ': 
    if s[i] == 0:
        if q == 1:
            s[i] = 0; q = 3
        elif q == 2:
            s[i] = 1; q = 3
        elif q == 3:
            s[i] = 0; q = 2
    
    elif s[i] == 1:
        if q == 1:
            s[i] = 1; q = 2
        elif q == 2:
            s[i] = 0; q = 3
        elif q == 3:
            s[i] = 1; q = 2
    
    i -= 1
    
print('Количество нулей:', s.count(0))