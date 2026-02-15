ans = 10**9


for A in range(1, 1000):
    for x in range(1, 200):
        for y in range(1, 200): 
            if (x >= A) and (x * y <= 50) and (x <= y + 10):
                # Нашли контрпример - это A не подходит
                break
        else:          
            continue
        #
      
        break
    else:
        # Внешний цикл по x завершился без break
        # Значит для всех x и y нет контрпримера
        ans = min(ans, A)

print(ans)