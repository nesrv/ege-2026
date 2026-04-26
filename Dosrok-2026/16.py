from functools import *

@lru_cache(100)
def f(n):
    if n < 10:
        return 3
    return (n+4) * f(n-5)

for i in range(10, 257_487):
    f(i)


print( (f(257_487) // 683 + 67 * f(257_477)) // f(257_472))