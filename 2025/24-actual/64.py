s = open("24-actual/24 (17).txt").read()
s = s.replace('+', '*').split('*')
s = [x for x in s if x]
maxi = 0
for i in range(len(s)):
    for k in range(1, min(51, len(s) - i + 1)):
        nums = s[i:i + k]
        length = sum(len(n) for n in nums) + len(nums) - 1
        maxi = max(maxi, length)
print(maxi)
