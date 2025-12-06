def f(s, n):   
    if s <= 19 and n == 2:
        return 1
    if n > 2:
        return 0
    h = f(s-2, n+1), f(s-5, n+1), f(s//3, n+1)
    return any(h) if n == 1 else all(h)
    
for s in range(1, 100):
    if f(s,0):
        print(s)
        
   