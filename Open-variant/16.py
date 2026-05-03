'''
Алгоритм вычисления значения функции F(n), где n — целое число, задан следующими соотношениями:

F(n) = 1 при n < 10;

F(n) = (n + 3) * F(n - 3), если n >= 10.

Чему равно значение выражения F(247563)/519 - 477 * F(247560)/F(247557)?
'''


from functools import *

import sys
from functools import *

sys.set_int_max_str_digits(10000)

@lru_cache
def f(n):
    if n < 10:
        return 1
    return (n + 3) * f(n - 3)

for i in range(10, 247563 + 1):
    f(i)

print((f(247563) // 519) - 477 * (f(247560) // f(247557)))