# Решение 1: Простой перебор
s = open("24/24 (16).txt").read()
count = 0

for i in range(len(s)):
    if s[i] == 'E':
        for j in range(i + 11, len(s)):
            if s[j] == 'E':
                middle = s[i+1:j]
                if 'E' not in middle and 'F' not in middle:
                    count += 1
                    break

print(count)