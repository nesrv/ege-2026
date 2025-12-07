s = open("24.txt").read()
maxi = 0
for i in range(len(s)):
    j = i
    if s[j] == '0':
        j += 1
    elif s[j] in '6789':
        while j < len(s) and s[j] in '6789':
            j += 1
    else:
        continue
    while j < len(s) and s[j] in '*-':
        j += 1
        if j < len(s) and s[j] == '0':
            j += 1
        elif j < len(s) and s[j] in '6789':
            while j < len(s) and s[j] in '6789':
                j += 1
        else:
            break
    maxi = max(maxi, j - i)
print(maxi)
