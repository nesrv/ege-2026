from collections import Counter

c = 0
for line in open("txt.txt"):
    nums = list(map(int, line.split()))
    counts = Counter(nums)
    values = list(counts.values())  
    if values.count(3) == 1 and len(values) == 5  and counts[max(nums)] == 1:
        c += 1
      
       
  

print(c)
