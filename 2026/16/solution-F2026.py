Q = [0] * 12000
G = [0] * 12000
F = [0] * 2100

# Q(n) = n + 4, если n < 21
# Q(n) = Q(n-4) + 2, если n >= 21
for n in range(12000):
    if n < 21:
        Q[n] = n + 4
    else:
        Q[n] = Q[n - 4] + 2

# G(n) = Q(n), если n >= 11240
# G(n) = G(n+3) + 2 при n < 11240
# Вычисляем сверху вниз
for n in range(11999, -1, -1):
    if n >= 11240:
        G[n] = Q[n]
    else:
        G[n] = G[n + 3] + 2

# F(n) = G(n+4), если n < 43
# F(n) = 2*F(n-2) - F(n-4) + 2, если n >= 43
for n in range(2100):
    if n < 43:
        F[n] = G[n + 4]
    else:
        F[n] = 2 * F[n - 2] - F[n - 4] + 2

print(F[2026])
