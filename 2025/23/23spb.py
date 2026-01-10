def f(x, y, visited=set()):
    if x == y: 
        return 8 in visited and 20 in visited
    if x < y: 
        return 0
    visited = visited | {x}
    return f(x-1, y, visited) + f(x-3, y, visited) + f(x//2, y, visited)

print(f(31, 3))


def f(x, y, visited=None):
    if visited is None: 
        visited = set()
    if x == y: 
        return not (8 in visited and 20 in visited)
    if x < y: 
        return 0
    visited = visited | {x}
    return f(x-1, y, visited) + f(x-3, y, visited) + f(x//2, y, visited)

print(f(31, 3))




def f(x, y, visited):
    if x == y:
        return not (8 in visited and 20 in visited)
    if x < y: return 0
    visited = visited | {x}
    return f(x-1, y, visited) + f(x-3, y, visited) + f(x//2, y, visited)

print(f(31, 3, set()))



def f(x, y, visited):
    if x == y and not (8 in visited and 20 in visited):
        return 1
    if x < y:
        return 0
    visited = visited + [x]
    return f(x-1, y, visited) + f(x-3, y, visited) + f(x//2, y, visited)

print(f(31, 3, []))
