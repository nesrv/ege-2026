def f(s1,n):
    if s1 >= 5110 or n > 4:
        return n == 4 or n ==   2
    h = f(s1+1,  n+1), \
        f(s1+4,  n+1), \
        f(s1 *2, n+1), \
     
    return any(h) if n % 2 else all(h)            

for s in range(1,5109):
    if f(s,0):
        print(s)

# 17
# 46 49
# 48