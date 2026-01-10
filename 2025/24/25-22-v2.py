# Решение 2: Через регулярные выражения
import re
s = open("24/24 (16).txt").read()
pattern = r'E[^EF]{10,}?E'
matches = re.findall(pattern, s)
print(len(matches))