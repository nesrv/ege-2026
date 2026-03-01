'''
В файле rogov-10.txt содержится последовательность натуральных чисел. 
Её элементы могут принимать целые значения от −100 000 до 100 000 включительно. 
Определите количество троек элементов последовательности, в которых не более двух четырехзначных чисел, 
а сумма элементов тройки меньше максимального элемента последовательности, оканчивающегося на 33.
В ответе запишите количество найденных троек чисел, затем максимальную из сумм элементов таких троек. 
В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
'''


def is_four_digit(n):
    return 1000 <= abs(n) <= 9999

def ends_with_33(n):
    return n % 100 == 33

f = open('rogov-10.txt')
nums = [int(line) for line in f]

max_ends33 = max(n for n in nums if n % 100 == 33)

count = 0
max_sum = None

for i in range(len(nums) - 2):
    a, b, c = nums[i], nums[i + 1], nums[i + 2]
    
    # Не более двух четырёхзначных (0, 1 или 2)
    four_digit_cnt = sum([is_four_digit(a), is_four_digit(b), is_four_digit(c)])
    if four_digit_cnt > 2:
        continue
    
    # Сумма < max_ends33
    s = a + b + c
    if s >= max_ends33:
        continue
    
    count += 1
    if max_sum is None or s > max_sum:
        max_sum = s

print(count, max_sum)
# 6626 94583
