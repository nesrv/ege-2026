def to_dec(s, p):
    result = 0
    for c in s:
        if c.isdigit():
            digit = int(c)
        else:
            digit = ord(c.upper()) - ord('A') + 10
        result = result * p + digit
    return result

for p in range(10, 37):
    kot = to_dec('KOT', p)
    golodni = to_dec('GOLODNI', p)
    meeow = to_dec('MEEOW', p)
    if kot + golodni == meeow * p**2 - 20194023088:
        print(f'p = {p}, PURR = {to_dec("PURR", p)}')
