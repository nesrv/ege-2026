s = open('24-compege/24_23762 (1).txt').read()
print('Total F:', s.count('F'))
print('Total even:', sum(1 for c in s if c in '02468'))
print('File length:', len(s))
