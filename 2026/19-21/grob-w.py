from math import ceil, floor

def f(s,n):
    if 50 <=s <= 87 or n > 3:
        return n ==  3
    h = f(s+2,  n+1), \
        f(s+3,  n+1)
    if n % 2 == 0:
        h += f(ceil(s*2.5), n+1),
    else:
        h += f(floor(s*2.5), n+1),
     
    return any(h) if n % 2 == 0 else all(h)            

for s in range(1,50):
    if f(s,0):
        print(s)

# 19 +








      