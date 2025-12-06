

f = [0]
for n in range(1,1001):
    if n % 2 == 0:
        f.append(f[n//2])
    else:
        f.append(1 + f[n-1])

# print(f.count(3))

f = [1,1]
for n in range(2,2025):   
    f.append(n * f[n-1])

print((f[2024] - f[2023]) // f[2022])


import sys
sys.setrecursionlimit(10**6)
def F(n):
    if n == 1: return 1
    else: return n * F(n - 1)
    
 
print((F(2024) - F(2023))//F(2022))