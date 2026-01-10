'''
Задание 24 (№25361).

Текстовый файл 24-compege\24_23762.txt состоит из десятичных цифр и заглавных букв латинского алфавита. Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых буква F встречается ровно 76 раз, четная цифра встречается ровно один раз, искомая последовательность начинается с этой единственной четной цифры.

В ответе запишите число – количество символов в найденной последовательности.

Для выполнения этого задания следует написать программу.

'''

def analyze_file():
    with open('24-compege/24_23762.txt') as f:
        s = f.read().strip()

    total_f_count = s.count('F')
    even_digits = set('02468')
    total_even_count = sum(1 for c in s if c in even_digits)

    print(f"Всего букв F: {total_f_count}")
    print(f"Всего четных цифр: {total_even_count}")

    max_length = 0
    n = len(s)

    for i in range(n):
        if s[i] in even_digits:
            f_count = 0
            even_count = 1
            for j in range(i + 1, n):
                if s[j] == 'F':
                    f_count += 1
                elif s[j] in even_digits:
                    even_count += 1
                if f_count > 76 or even_count > 1:
                    break
                if f_count == 76 and even_count == 1:
                    max_length = max(max_length, j - i + 1)
    return max_length

result = analyze_file()
print(f"Максимальная длина: {result}")

