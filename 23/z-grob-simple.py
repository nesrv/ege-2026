'''Упрощённое решение: разбиваем путь на два отрезка — до (30,33) и после.'''
from functools import lru_cache

def mag(x, y):
    return (x + y) % 2 == 0

@lru_cache(None)
def to_checkpoint(x, y, m):
    '''Сколько путей из (x,y) в (30,33) с запасом m магических точек.'''
    if x > 30 or y > 33:
        return 0
    if x == 30 and y == 33:
        return 1
    if mag(x, y) and m == 0:
        return 0
    m2 = m - 1 if mag(x, y) else m
    return (to_checkpoint(x + 1, y, m2) +
            to_checkpoint(x, y + 1, m2) +
            to_checkpoint(x + 1, y + 1, m2))

@lru_cache(None)
def to_end(x, y, m):
    '''Сколько путей из (x,y) в (70,70) с запасом m магических точек.'''
    if x > 70 or y > 70:
        return 0
    if x == 70 and y == 70:
        return 1
    if mag(x, y) and m == 0:
        return 0
    m2 = m - 1 if mag(x, y) else m
    return (to_end(x + 1, y, m2) +
            to_end(x, y + 1, m2) +
            to_end(x + 1, y + 1, m2))

# Пути с ровно k магическими точками в 1-й части: c(k)-c(k-1)
# Умножаем на пути от (30,33) с бюджетом 5-k
c = [to_checkpoint(2, 5, k) for k in range(6)]
exact = [c[k] - (c[k-1] if k else 0) for k in range(6)]
print(sum(exact[k] * to_end(30, 33, 5 - k) for k in range(6)))
