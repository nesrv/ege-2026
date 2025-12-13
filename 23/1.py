def f(x, y, last):
    if x > y:
        return 0
    if x == y:
        return 1
    total = 0
    # Всегда можно добавить B (прибавить 3)
    total += f(x + 3, y, 2)
    # Всегда можно добавить C (умножить на 2)
    total += f(x * 2, y, 3)
    # Можно добавить A (вычесть 1), только если предыдущая команда НЕ была A
    if last != 1:  # если последняя команда не A
        total += f(x - 1, y, 1)
    return total

print(f(3, 12, 0))  