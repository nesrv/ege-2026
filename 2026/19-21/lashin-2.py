
def f(s1,s2,n):
    if s1 + s2 >= 154 or n > 4:
        return n == 4 or n == 2
    h = f(s1+1, s2, n+1), \
        f(s1*3, s2, n+1), \
        f(s1, s2+1, n+1), \
        f(s1, s2*3, n+1)
    return any(h) if n % 2 else all(h)            

for s in range(1,70):
    if f(9,s,0):
        print(s)

# 17
# 46 49
# 48