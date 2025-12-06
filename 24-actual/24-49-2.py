f = open("24-actual/24.69902.txt")
words = f.read().replace('DE', 'D E').split()
f.close()

window = 241

if len(words) < window:
    max_length = sum(len(word) for word in words)
else:
    max_length = max(
        sum(len(word) for word in words[i:i + window])
        for i in range(len(words) - window + 1)
    )

print(max_length)