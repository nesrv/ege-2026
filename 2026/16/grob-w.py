n_target = 1234567891011121314

# Для таких больших n массив не создать, но можно вычислить аналитически
# Но если строго по референсу — для демонстрации подхода с маленьким числом:

# Допустим, мы хотим для маленького n показать алгоритм:
small_n = 20
F = [0] * (small_n + 1)

for n in range(0, small_n + 1):
    if n < 10:
        F[n] = n
    elif n % 2 == 0:
        F[n] = F[n - 1]
    else:
        F[n] = F[n - 1] + 2

print(F[small_n])  # Для 20 будет 19

# А для большого числа:
if n_target < 10:
    result = n_target
elif n_target % 2 == 0:
    result = n_target - 1
else:
    result = n_target

print(result)