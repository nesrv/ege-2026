'''
В файле lashin-7.txt  содержится последовательность натуральных чисел.
Её элементы могут принимать целые значения от 1 до 100 000 включительно. 
Определите количество пар последовательности, в которых только один из элементов является трёхзначным числом, 
оба числа начинаются на чётную цифру, а сумма элементов пары кратна максимальному двухзначному элементу последовательности, 
оканчивающемуся на 3. 
В ответе запишите количество найденных пар, затем минимальную из сумм элементов таких пар. 
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
from pathlib import Path

def is_three_digit(n):
    return 100 <= n <= 999

def starts_even(n):
    return int(str(n)[0]) % 2 == 0

f = open('lashin-7.txt')
nums = [int(line) for line in f]

max_two_digit_ends3 = max(n for n in nums if 10 <= n <= 99 and n % 10 == 3)

count = 0
min_sum = None
for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]
    if is_three_digit(a) != is_three_digit(b) and (starts_even(a) and starts_even(b)) and a*b % max_two_digit_ends3 == 0:
        count += 1
        s = a + b
        if min_sum is None or s < min_sum: min_sum = s

print(count, min_sum)

# 7 6806

