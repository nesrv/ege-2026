

s = open(r"Апробация-1\24_27634.txt").read()

l = 0
z = 0
ans = len(s)  # заведомо большое значение

for r in range(len(s)):
    if s[r] == 'Z':
        z += 1

    while z >= 270:
        ans = min(ans, r - l + 1)
        if s[l] == 'Z':
            z -= 1
        l += 1

print(ans)

# 1058