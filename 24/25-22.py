# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество групп из идущих подряд не менее 12 символов, которые начинаются и заканчиваются буквой E 
# и не содержат других букв E (кроме первой и последней) и букв F.

s = open("24/24 (16).txt").read()

# Решение 1: Простой перебор
# count = 0
# for i in range(len(s)):
#     if s[i] == 'E':
#         for j in range(i + 11, len(s)):
#             if s[j] == 'E':
#                 middle = s[i+1:j]
#                 if 'E' not in middle and 'F' not in middle:
#                     count += 1
#                     break
# print("Решение 1:", count)

# # Решение 2: Через регулярные выражения
# import re
# pattern = r'E[^EF]{10,}?E'
# matches = re.findall(pattern, s)
# print("Решение 2:", len(matches))

# Решение 3: Через split и фильтрацию
parts = s.split('E')
count = 0
for x in parts:
    if len(x) >= 10 and 'F' not in x:
        count += 1
print("Решение 3:", count)