from itertools import product

words = product("0123456", repeat=7)
c = 0

even = {'0', '2', '4', '6'}
odd = {'1', '3', '5'}

for word in words:
    if word[0] != '0':  # семизначное число (первая цифра не 0)
        count = 0
        for i in range(6):  # проверяем пары (0-1, 1-2, ..., 5-6)
            if word[i] in even and word[i + 1] in odd:
                count += 1
        if count == 2:
            c += 1


    

print(c)


# for word in words:
#     if word[0] != '0':
#         count = sum(word[i] in '0246' and word[i + 1] in '135' for i in range(6))
#         if count == 2:
#             c += 1