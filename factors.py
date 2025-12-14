n = 7500045
factors = []
d = 2

while d * d <= n:
    while n % d == 0:
        factors.append(d)
        n //= d
    d += 1

if n > 1:
    factors.append(n)

print(factors)
print(set(factors))
