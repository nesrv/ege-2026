

s = open("24-actual/1_24.txt").read()

mx = cur = 1

for i in range(1, len(s)):
    cur = cur + 1 if s[i].isalpha() != s[i-1].isalpha() else 1
    mx = max(mx, cur)

print(mx)