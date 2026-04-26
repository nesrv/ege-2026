F = [0] * 15235

for n in range(15235):
    if n < 10:
        F[n] = n
    if n > 10 and n % 2 == 0:
        F[n] = F[n//2] + 2*n-1
    if n > 2 and n % 2:
        F[n] = F[n-1] + 3*n-2

print(F[14853] - F[15234])
# 30795