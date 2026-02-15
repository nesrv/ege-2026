P = range(25, 65)
Q = range(40, 116)

ans = 10**9

for a in range(0, 200):
    for b in range(a, 200):
        for x in range(0, 200):
            if not ((x in P) <= (((x in Q) and (x not in range(a, b + 1))) <= (x not in P))):
                break
        else:  # выполнится, если break НЕ сработал
            ans = min(ans, b - a)

print(ans)