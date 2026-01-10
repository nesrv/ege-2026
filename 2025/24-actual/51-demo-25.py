
t = open('24-actual/demo_2025_24.txt').read()

# Создаем регулярное выражение для корректных выражений
# (?:0|[6-9][0-9]*) - число без ведущих нулей
# (?:[-*]) - операция

# pattern = r'(?:0|[1-9][0-9]*)(?:[-*](?:0|[1-9][0-9]*))*'


pattern = r'[1-9][0-9]*([-*]+[1-9][0-9]*)*'

matches = findall(pattern, s)

max_length = max(matches , key=len)

print(len(max_length)  )


# Заменяем все запрещённые комбинации на 'x'

for bad in ['**','--','*-','-*','*0','0*','-0','0-','06','07','08','09']:
    t = t.replace(bad, 'x')

# Разбиваем на кандидаты
a = t.split('x')

# Считаем длину максимальной подпоследовательности, убирая '*' и '-' на концах
ml = max((len(i.strip('*-')) for i in a), default=0)

print(ml)

t = open('24-actual/demo_2025_24.txt').read()

for bad in ['**','--','*-','-*','*0','0*','-0','0-']:
    t = t.replace(bad,'x')

a = t.split('x')

ml = max(
    (len(i.strip('*-')) for i in a 
     if all(not (i[j] == '0' and j+1 < len(i) and i[j+1] in '6789') for j in range(len(i)))), 
    default=0
)

print(ml)