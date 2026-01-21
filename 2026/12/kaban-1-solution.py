"""
Решение задачи про машину Тьюринга.

Начальное состояние:
- Лента: [λ] 111...111 (57 единиц) [λ]
- Головка на пустой ячейке справа от последовательности
- Начинаем с состояния q₀
"""

def simulate_mt():
    # Создаем ленту: пустая, 57 единиц, пустая
    # Используем пробел ' ' вместо λ для совместимости с кодировкой
    tape = [' '] + ['1'] * 57 + [' ']
    pos = len(tape) - 1  # Позиция головки (справа от единиц на пустой ячейке)
    state = 0  # q₀ = 0, q₁ = 1, q₂ = 2, q₃ = 3
    
    step = 0
    
    while True:
        step += 1
        symbol = tape[pos]
        
        # q₀: λ → λ, L, q₁
        if state == 0:
            if symbol == ' ':
                pos -= 1  # L (влево)
                state = 1  # q₁
            else:
                print(f"Ошибка: в состоянии q₀ встречен символ '{symbol}'")
                break
        
        # q₁: 0 → 0, L, q₃ | 1 → 1, L, q₂
        elif state == 1:
            if symbol == '0':
                pos -= 1  # L (влево)
                state = 3  # q₃
            elif symbol == '1':
                pos -= 1  # L (влево)
                state = 2  # q₂
            else:
                print(f"Ошибка: в состоянии q₁ встречен символ '{symbol}'")
                break
        
        # q₂: λ → λ, S, q₂ | 1 → 1, L, q₃ | 0 → 0, L, q₃
        elif state == 2:
            if symbol == ' ':
                # S (стоп) - остаемся в q₂
                break
            elif symbol == '1':
                pos -= 1  # L (влево)
                state = 3  # q₃
            elif symbol == '0':
                pos -= 1  # L (влево)
                state = 3  # q₃
            else:
                print(f"Ошибка: в состоянии q₂ встречен символ '{symbol}'")
                break
        
        # q₃: λ → λ, S, q₃ | 0 → 0, L, q₂ | 1 → 1, L, q₂
        elif state == 3:
            if symbol == ' ':
                # S (стоп) - остаемся в q₃
                break
            elif symbol == '0':
                pos -= 1  # L (влево)
                state = 2  # q₂
            elif symbol == '1':
                pos -= 1  # L (влево)
                state = 2  # q₂
            else:
                print(f"Ошибка: в состоянии q₃ встречен символ '{symbol}'")
                break
        
        # Защита от бесконечного цикла
        if step > 1000:
            print("Превышен лимит шагов!")
            break
    
    zeros = tape.count('0')
    ones = tape.count('1')
    
    print(f"Шагов выполнено: {step}")
    print(f"Финальное состояние: q_{state}")
    print(f"Позиция головки: {pos}")
    tape_fragment = ''.join(tape[max(0,pos-5):pos+6]).replace(' ', '_')
    print(f"Лента (фрагмент вокруг головки): ...{tape_fragment}...")
    print(f"\nКоличество нулей на ленте: {zeros}")
    print(f"Количество единиц на ленте: {ones}")
    
    # Показываем полную ленту (без крайних пустых ячеек)
    tape_content = ''.join(tape[1:-1])
    print(f"\nСодержимое ленты: {tape_content}")
    
    return zeros


if __name__ == '__main__':
    zeros = simulate_mt()
    print(f"\nОтвет: {zeros}")
