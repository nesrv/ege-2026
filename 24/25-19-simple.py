s = open("24/24 (14).txt").read()
max_len = 0

for i in range(len(s)):
    count_A = 0
    for j in range(i, len(s)):
        if s[j] == 'A':
            count_A += 1
        if count_A > 1:
            break
        l = j - i + 1
        max_len = max(max_len, l)

print(max_len)