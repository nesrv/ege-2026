G = [0] * 150_001
F = [0] * 100_001

for n in range(1, 150_001):
    if n <= 6:
        G[n] = 5 ** n
    else:     
        G[n] = G[n-3] + 2
        

for n in range(1, 100_001):
    F[n] = G[n-50_000] + G[n+50_000] 
    

print(F[100_000])
 
# 152076