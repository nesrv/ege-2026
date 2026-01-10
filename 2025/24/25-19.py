s = open("24/24 (14).txt").read()
left = 0
max_len = 0
count_A = 0
for right in range(len(s)):   
    if s[right] == 'A':
        count_A += 1

    # Сжимаем окно слева, пока A > 1
    while count_A > 1:
        if s[left] == 'A':
            count_A -= 1
        left += 1

    # Обновляем максимум
    max_len = max(max_len, right - left + 1)

print(max_len)


s = s.split('A')
ans = max(len(s[i]) + len(s[i+1]) + 1 for i in range(len(s)-1))
print(ans)
