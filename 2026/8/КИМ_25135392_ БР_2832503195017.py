from collections import Counter
f = open("txt.txt")

c = 0
for line in f:
    line = list(map(int,line.split()))
    counts = list(Counter(line).values())


    if counts.count(3) == 1 and all(c==1 for c in counts if c != 3) and line.count(max(line))==1:
        c+=1


print (c)
       
