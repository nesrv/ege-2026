
for A in range(1,32): #2
    for x in range(1,32): #1 2 3 4
        F = ((x & 29 != 0) <= ((x & 17 == 0) <= (x & A )))
        if not F:
            print(A,x)            
            break
    else:
        print(A)
        break
            
            