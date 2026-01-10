import re

s = open("24/107_24.txt").read()
s = re.sub(r'[^ABC]', '', s)  # убираем лишние символы
matches = re.findall(r'(?:AB|CB)+', s)
print(max(len(match) // 2 for match in matches) if matches else 0)