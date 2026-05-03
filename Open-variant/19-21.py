
def f(s1,s2,n):
    if s1 + s2 >= 154 or n > 2:
        return  n == 2
    h = f(s1+4, s2, n+1), \
        f(s1*3, s2, n+1), \
        f(s1, s2+4, n+1), \
        f(s1, s2*3, n+1)
    return any(h)      

for s in range(1,143):
    if f(11,s,0):
        print(s)
        break
    
        
def f(s1,s2,n):
    if s1 + s2 >= 154 or n > 4:
        return  n == 4 or n == 2
    h = f(s1+4, s2, n+1), \
        f(s1*3, s2, n+1), \
        f(s1, s2+4, n+1), \
        f(s1, s2*3, n+1)   
    return any(h) if n % 2 else all(h)      

for s in range(1,143):
    if f(11,s,0):
        print(s) 