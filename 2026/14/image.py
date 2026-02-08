for A in range(1, 100_000):   
    for x in range(1, 100_000):
        y = 78125 - 4*x
        # 78125  - 4x != y
        if 78125 - 4*x > 0 and ((A > x) and (A > y)) == False:           
            break
    else:
        print(A)
        break
