'''
Откройте файл, содержащий в каждой строке шесть натуральных чисел. 
Определите сумму четных чисел в строке с наименьшим номером, для которой выполнены оба условия:
— В строке есть два числа, каждое из которых повторяется дважды, остальные числа различны;
— максимальное и минимальное значение в строке не повторяется в ней.
'''

from collections import Counter

for line in open("иглин.txt"):
    nums = list(map(int, line.split()))
    counts = Counter(nums)
    if list(counts.values()).count(2) == 2 and counts[max(nums)] == 1 and counts[min(nums)] == 1:
        print(sum(x for x in nums if x % 2 == 0))
        break
      