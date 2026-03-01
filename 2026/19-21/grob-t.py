def f(s,g,n):
    if s >= g or n > 4:
        return n == 4 or n == 2
    h = f(s+1, g, n+1), \
        f(s+3, g, n+1), \
        f(s+2, g-2, n+1)       
    return any(h) if n % 2 else all(h)            

for s in range(1,109):
    if f(s,110,0):
        print(s)

# 102
# 101 102
# 103


