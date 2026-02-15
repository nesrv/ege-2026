C = range(25, 65)      # [25, 64]
T = range(50, 121)     # [50, 120]

ans = 10**9

for a in range(0, 200):
    for b in range(a, 200):
        A = range(a, b + 1)
        
    
        for x in range(0, 200):
            # Упрощенное выражение: (x in C) <= (x in A) or (x in T)
            # или то же самое: not (x in C) or (x in A) or (x in T)
            
            # Проверяем условие: ¬((x∈C)→(x∈A)) → (x∈T)
            # Эквивалентно: (x in C) <= (x in A) or (x in T)
            if not (((x in C) <= (x in A)) or (x in T)):
                break
        else: 
            ans = min(ans, b - a + 1)

print(ans)