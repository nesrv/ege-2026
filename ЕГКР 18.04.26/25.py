def is_prime(n):     
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def has_3(x1, x2):
    """Проверка, что в записи числа ровно две цифры 3"""
    return str(x1).count('3') == 2 and str(x2).count('3') == 2 


for x in range(8_996_452, 9_015_000):
    for d in range(2, int(x**0.5) + 1):
        if x % d == 0 and is_prime(d) and is_prime(x//d):
            if has_3(d, x//d):
                print(x, max(d, x//d))
                break
         
       
    
'''
9001609 24133
9002887 38639
9006149 38653
9012167 3853
9012373 23531
'''