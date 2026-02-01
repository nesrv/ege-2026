
for x in range(1,27_001):
    N = 3 * 27**9 + 2 * 27 ** 6 + 27 ** 3 - x

    c = 0
    while N:
        N,ost = divmod(N,27)
        if ost == 0:
            c += 1
    if c == 6:
        print(x)
        break
    