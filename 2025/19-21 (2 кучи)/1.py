def f(s,n):
    if s <= 25 or n > 4:
        return n == 4 or n == 2
    h = f(s-3,  n+1), \
        f(s-6,  n+1), \
        f(s//3, n+1)
        
    return any(h) if n % 2 else all(h)            

for s in range(26,170):
    if f(s,0):
        print(s)
      