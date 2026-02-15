


# for A in range(2,2000):
#     c = 0
#     for x in range(1,101):
#         for y in range(1,101):
#             if ((78125 != (y + 4*x)) or ((A>x) and (A>y))):
#                 c+=1
#     if c == 10_000:
#         print(A)
#         break
    


for A in range(0, 80000):
    for x in range(1, 20000):
        y = 78125 - 4*x
        if y >= 1:
            if not ((78125 != y + 4*x) or ((A > x) and (A > y))):
                break
    else:
        print(A)
        break
    