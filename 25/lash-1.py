'''
(B. Лашин) Напишите программу, которая перебирает целые числа, большие 24 517 512, в порядке возрастания и ищет среди них числа, представленные в виде произведения 12 простых множителей, не обязательно различных.

В ответе в первом столбце таблицы запишите первые 5 найденных чисел в порядке возрастания, а во втором столбце — для каждого из них соответствующий наибольший из найденных множителей.
Количество строк в таблице для ответа избыточно.

'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_factors(n):
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


found = 0

for x in range(24_517_513, 30_000_000):
    factors = prime_factors(x)

    if len(factors) == 12:
        print(x, max(factors))
        found += 1

        if found == 5:
            break


'''
24517728 1051
24518400 1277
24519680 4789
24521472 367
24521616 53

'''