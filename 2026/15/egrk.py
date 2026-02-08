


for A in range(2,2000):
    c = 0
    for x in range(1,101):
        for y in range(1,101):
            if ((78125 != (y + 4*x)) or ((A>x) and (A>y))):
                c+=1
    if c == 10_000:
        print(A)
        break
    
                