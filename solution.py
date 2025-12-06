f = open('24.txt', 'r')
s = f.read()
f.close()

max_len = 0

for i in range(len(s)):
    count_de = 0
    for j in range(i, len(s)):
        if s[j:j+2] == 'DE':
            count_de += 1
        if count_de > 240:
            break
        max_len = max(max_len, j - i + 1)

print(max_len)
