f = open(r'2026\9py\9_23747.txt')

for s in f:
    nums = [int(x) for x in s.split()]
    a1 = [x for x in nums if nums.count(x) == 1]
    a3 = [x for x in nums if nums.count(x) == 3]
    if len(a3) == 3 and len(a1) == 4 and sum(a1) / 4 <= a3[0]:
        res = sum(nums)
        
print(res)

    