s = open("24/107_24.txt").read().replace("AB", "X").replace("CB", "X")

parts = s.replace("A", " ").replace("B", " ").replace("C", " ").split()

print(max(len(part) for part in parts))