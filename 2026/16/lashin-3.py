F = [0] * 4001



for n in range(1, 4001):
    if n < 10:
        F[n] = n  + 10
    else:
        F[n] = F[n-8] + 2**n
   
    

print((F[4000] + 2 * F[3992])//F[3984])
 
# 66048