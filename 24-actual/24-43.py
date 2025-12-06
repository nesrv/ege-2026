# s = open('24-actual/24_2024.txt').readline().split('T')
# maxi = 0

# for i in range(len(s)-100):
#     r = 'T'.join(s[i:i+101])
#     maxi = max(maxi, len(r))
    
# print(maxi)

s = open('24-actual/24_2024.txt').readline()

# pos = [i for i, c in enumerate(s) if c == 'T']
# ans = 0

# for i in range(len(pos) - 99):
#     left = pos[i]
#     right = pos[i + 99]
#     ans = max(ans, right - left + 1)

# print(ans)

p = [i for i, c in enumerate(s) if c == 'T']
print(max(p[i+99] - p[i] + 1 for i in range(len(p) - 99)))

# «Перебери все группы из 100 подряд идущих T, 
# для каждой посчитай длину минимального фрагмента строки, который содержит эти 100 T, и выведи наибольшую такую длину»