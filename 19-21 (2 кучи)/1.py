def f(s1,s2,n):
    if s1 + s2 >= 59 or n > 4:
        return n == 4 or n == 2
    h = f(s1+1, s2, n+1), \
        f(s1*2, s2, n+1), \
        f(s1, s2+1, n+1), \
        f(s1, s2*2, n+1)
    return any(h) if n % 2 else all(h)            

for s in range(1,70):
    if f(5,s,0):
        print(s)
      