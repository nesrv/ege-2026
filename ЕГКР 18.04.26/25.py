def is_prime(n):     
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def has_exactly_two_digits_three(num):
    """Проверка, что в записи числа ровно две цифры 3"""
    return str(num).count('3') == 2


for x in range(8_996_452, 9_020_000):
    for d in range(2, int(x**0.5) + 1):
        if x % d == 0 and is_prime(d) and is_prime(x//d):
            if has_exactly_two_digits_three(d) and has_exactly_two_digits_three(x//d):
                print(x, max(d, x//d))
                break
         
       
    
'''
9001609 24133
9002887 38639
9006149 38653
9012167 3853
9012373 23531
'''