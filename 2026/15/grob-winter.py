ans = 10**9

c1, c2, c3 = 1768, 1240, 305

# Перебираем A
for A in range(1, 1000):
    # Перебираем x
    for x in range(0, 10000):
        # Упрощаем: p ↑ x = 0 равносильно (p & x) == 0
        # p ↑ x ≠ 0 равносильно (p & x) != 0
        
        term1 = ((c1 & x) == 0)
        term2 = (not ((c2 & x) != 0)) or ((c3 & x) == 0)
        term3 = ((A & x) != 0)
        
        if not (term1 or term2 or term3):
            break
    else:
        ans = min(ans, A)
        break

print(ans)