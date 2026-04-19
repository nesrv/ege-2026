from fnmatch import fnmatch

for x in range(0,10**8, 171):
    if fnmatch(str(x), '1*23??56'):
        print(x, x//171)