'''
Тройки: есть 2026, ровно одно = произведение двух других, сумма НЕ шестизначная.
'''
from pathlib import Path

nums = [int(x) for x in open(Path(__file__).parent / '17.txt')]

count = 0
max_sum = 0

for i in range(len(nums) - 2):
    a, b, c = nums[i], nums[i + 1], nums[i + 2]
    s = a + b + c
    products = (a == b * c) + (b == a * c) + (c == a * b)
    
    if 2026 in (a, b, c) and products == 1 and not (100000 <= s <= 999999):
        count += 1
        max_sum = max(max_sum, s)

print(count, max_sum)