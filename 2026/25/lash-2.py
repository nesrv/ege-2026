'''


'''

def prime_factors(n):
    """Список простых множителей с учётом кратности"""
    factors = []
    for d in range(2, int(n ** 0.5) + 1):
        q, r = divmod(n, d)
        while r == 0:
            factors.append(d)
            n = q
            q, r = divmod(n, d)
    if n > 1:
        factors.append(n)
    return factors


def has_5(x):
    """Проверка: есть ли цифра 5 в записи числа"""
    return '5' in str(x)


found = 0

for x in range(13_475_125, 20_000_000):
    factors = prime_factors(x)

    if len(factors) == 5:
        ok = True
        for p in factors:
            if not has_5(p):
                ok = False
                break

        if ok:
            print(x, max(factors))
            found += 1

            if found == 5:
                break

'''
13476875 21563
13480625 21569
13485625 21577
13491875 21587
13493125 21589

'''