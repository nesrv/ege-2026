'''
Откройте файл, содержащий в каждой строке семь натуральных чисел. 

Определите сумму чисел в строке с наибольшим произведением неповторяющихся элементов, для которой выполнены оба условия:
— В строке есть одно число, которое повторяется трижды, остальные четыре числа различны;
— сумма неповторяющихся чисел строки не больше утроенного значения повторяющегося числа.
'''

from collections import Counter
from math import prod

max_mul = 0

for line in open("лашин5.txt"):
    nums = list(map(int, line.split()))
    counts = Counter(nums)
    if list(counts.values()).count(3) == 1 and len(counts)==5:
        not_repeats = list(k for k,v in counts.items() if v == 1)
        sum_not_repeats = sum(not_repeats)
        mul_not_repeats = prod(not_repeats)  
        x = max(counts, key=counts.get)       
        if mul_not_repeats >= max_mul:
             max_mul = mul_not_repeats             
             if sum_not_repeats <= x * 3 :
                print(sum(nums)) # 1171
        
      
      