"""
Подробное решение с визуализацией каждого шага.
"""

def simulate_mt_verbose():
    tape = ['λ'] + ['1'] * 57 + ['λ']
    pos = len(tape) - 1
    state = 0  # q₀
    
    step = 0
    print(f"Начальное состояние:")
    print(f"  Лента: {''.join(tape[1:-1])}")
    print(f"  Позиция: {pos} (символ '{tape[pos]}')")
    print(f"  Состояние: q_{state}\n")
    
    while True:
        step += 1
        symbol = tape[pos]
        old_state = state
        old_pos = pos
        
        if state == 0:
            if symbol == 'λ':
                pos -= 1
                state = 1
                action = f"λ → λ, L, q₁"
        
        elif state == 1:
            if symbol == '0':
                pos -= 1
                state = 3
                action = f"0 → 0, L, q₃"
            elif symbol == '1':
                pos -= 1
                state = 2
                action = f"1 → 1, L, q₂"
        
        elif state == 2:
            if symbol == 'λ':
                action = f"λ → λ, S, q₂ (СТОП)"
                print(f"Шаг {step}: q_{old_state}, символ '{symbol}' → {action}")
                break
            elif symbol == '1':
                pos -= 1
                state = 3
                action = f"1 → 1, L, q₃"
            elif symbol == '0':
                pos -= 1
                state = 3
                action = f"0 → 0, L, q₃"
        
        elif state == 3:
            if symbol == 'λ':
                action = f"λ → λ, S, q₃ (СТОП)"
                print(f"Шаг {step}: q_{old_state}, символ '{symbol}' → {action}")
                break
            elif symbol == '0':
                pos -= 1
                state = 2
                action = f"0 → 0, L, q₂"
            elif symbol == '1':
                pos -= 1
                state = 2
                action = f"1 → 1, L, q₂"
        
        # Показываем каждый шаг
        if step <= 20:  # Показываем первые 20 шагов
            print(f"Шаг {step}: q_{old_state}, позиция {old_pos}, символ '{symbol}' → {action}")
            print(f"  Новая позиция: {pos}, новое состояние: q_{state}")
        
        if step > 1000:
            print("Превышен лимит шагов!")
            break
    
    zeros = tape.count('0')
    ones = tape.count('1')
    
    print(f"\n{'='*50}")
    print(f"Итого шагов: {step}")
    print(f"Финальное состояние: q_{state}")
    print(f"Позиция головки: {pos}")
    print(f"\nКоличество нулей: {zeros}")
    print(f"Количество единиц: {ones}")
    print(f"{'='*50}\n")
    
    # Показываем фрагмент ленты
    start = max(1, pos - 10)
    end = min(len(tape) - 1, pos + 11)
    tape_visible = ''.join(tape[start:end])
    marker = ' ' * (pos - start) + '^'
    print(f"Фрагмент ленты вокруг головки:")
    print(f"  {tape_visible}")
    print(f"  {marker}")
    
    return zeros


if __name__ == '__main__':
    zeros = simulate_mt_verbose()
