# F(n) = n + 1, если n <= 3
# F(n) = F(n - 3) + n - 15, если n > 3 и n кратно 3
# F(n) = F(n + 3) + n * 2, если n > 3 и n не кратно 3 (бесконечная рекурсия - не определено!)

# F определена для: 1, 2, 3, 6, 9, 12, 15, ...

LIMIT = 10**5
F = {}

# База: n <= 3
for n in range(1, 4):
    F[n] = n + 1

# Для n > 3 и кратных 3: вычисляем снизу вверх
n = 6
while True:
    F[n] = F[n - 3] + n - 15
    if F[n] > LIMIT:
        break
    n += 3

# Считаем количество n, где F(n) <= 10^5
count = 0
for n, val in F.items():
    if val <= LIMIT:
        count += 1

print(f"Ответ: {count}")

# Проверка первых значений
print("\nПервые значения:")
for n in sorted(F.keys())[:15]:
    print(f"F({n}) = {F[n]}")
