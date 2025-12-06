# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC...Z). Определите максимальное количество идущих подряд символов, среди которых нет ни одной буквы A и при этом не менее трёх букв E.

s = open("24/24 (15).txt").read()

s = s.split('A')

parts_with_3E = [part for part in s if part.count("E") >= 3]

longest = max(parts_with_3E, key=len)

print(len(longest))

