def f(x, y, s):
    if x == y:
        if ',8,' in s and ',20,' in s:
            return 0
        else:
            return 1
    if x < y:
        return 0
    return f(x-1, y, s+str(x)+',')+f(x-3, y, s+str(x)+',')+f(x//2, y, s+str(x)+',')


print(f(31, 3, ','))

def f(x, y, visited):
    # Если достигли цели
    if x == y:       
        if 8 in visited and 20 in visited:
            return 0
        else:
            return 1 
    if x < y:
        return 0
    
    new_visited = visited | {x}

 
    total = 0
    total += f(x - 1, y, new_visited)
    total += f(x - 3, y, new_visited)
    total += f(x // 2, y, new_visited)

    return total


print(f(31, 3, set()))