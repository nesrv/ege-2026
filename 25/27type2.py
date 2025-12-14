def is_prime(x):
    for d in range(2, int(x ** 0.5)+1):
        if x % d == 0:
            return False
    return True
        



for x in range(7_500_000, 7_501_000):
    divs = set()
    for d in range(2, x//2  + 1):
        if x%d == 0 and is_prime(d):
            divs.add(d)
    if divs and (min(divs) + max(divs)) % 100 == 32:
        print(x)
 

    
# [3, 5, 7, 71429]


# def prime_factors(x):
#     factors = []
#     d = 2
#     while d * d <= x:
#         while x % d == 0:
#             factors.append(d)
#             x //= d
#         d += 1
#     if x > 1:
#         factors.append(x)
#     return set(factors)

# for x in range(7_500_000, 7_501_000):
#     divs = prime_factors(x)
#     if divs and (min(divs) + max(divs)) % 100 == 32:
#         print(x)

    