def f(x,y):
    if x < y:
        return False
    if x == y:
        return True
    return f(x-1,y) + f(x//2,y)

print(f(40,17)*f(17,6))