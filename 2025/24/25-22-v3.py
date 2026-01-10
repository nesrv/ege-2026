# Решение 3: Через split и фильтрацию
s = open("24/24 (16).txt").read()
parts = s.split('E')
count = 0

for i in range(len(parts) - 1):
    if len(parts[i]) >= 10 and 'F' not in parts[i]:
        count += 1

print(count)