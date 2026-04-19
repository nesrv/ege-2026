N = 700_000
c = 0
for x in range(N, 10**10):
    for d in range(17, x//2+1, 10):
        if x % d == 0 and d % 10 == 7:
            print(x,d)
            c += 1
            if c == 5:
                exit()
            break