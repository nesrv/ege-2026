s = open("24-actual/demo_2025_24.txt").read()
for c in '012345':
    s = s.replace('0' + c, ' ')
    s = s.replace('-0', ' ')
    s = s.replace('*0', ' ')
s = s.replace('--', ' ').replace('**', ' ').replace('*-', ' ').replace('-*', ' ')
print(max(len(i) for i in s.split()))
