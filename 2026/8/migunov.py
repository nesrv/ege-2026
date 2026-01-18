from itertools import product

# Порядок букв для перечисления: А=0, С=1, Т=2, Е=3, К=4
alphabet = "АСЕТК"  # в порядке перечисления
order_map = {'А': 0, 'С': 1, 'Т': 2, 'Е': 3, 'К': 4}

# Часть 1: Найти индекс слова "АТТЕСТАТ"
word1 = "АТТЕСТАТ"

# Переводим слово в число в системе счисления с основанием 5
def word_to_index(word):
    base = len(alphabet)
    index = 0
    for letter in word:
        index = index * base + order_map[letter]
    return index + 1  # индексация с 1

index1 = word_to_index(word1)
print(f"Индекс слова {word1}: {index1}")

# Часть 2: Найти последнее слово, которое:
# - содержит "ТЕСАК" как подстроку
# - не содержит двух одинаковых букв подряд

words = product("АСЕТК", repeat=8)
last_index = 0

for i, word in enumerate(words, 1):
    word_str = ''.join(word)
    # Проверяем условие: содержит "ТЕСАК" и нет двух одинаковых букв подряд
    if 'ТЕСАК' in word_str:
        # Проверяем, нет ли двух одинаковых букв подряд
        has_double = any(word[j] == word[j+1] for j in range(7))
        if not has_double:
            last_index = i

print(f"Индекс последнего подходящего слова: {last_index}")
print(f"Разность: {abs(index1 - last_index)}")
