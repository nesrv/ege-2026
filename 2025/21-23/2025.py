# def f(s,n):
#     h = f(s-3, n+1), f(s-6, n+1), f(s//3, n+1)
#     if (s <= 25 and n==2) or (s <= 25 and n==4):
#         return True
#     if s > 25 or n > 4:
#         return False
#     return all(h) if n % 2 else any(h)

# for s in range(26,10):
#     if f(s,0):
#         print(s)
        
         


# def Win(n, m):
#     return 0 if m <= 25 else any([Lose(n-1, m-3), Lose(n-1, m-6), Lose(n-1, m//3)])

# def Lose(n, m):
#     return 1 if m <= 25 else 0 if  not n else\
#            all([Win(n-1, m-3), Win(n-1, m-6), Win(n-1, m//3)])
           
# print(min(m for m in range(26, 100) if not Lose(2, m) and Lose(4, m)))


# def game(n, m, is_win_turn):
#     if m <= 25:
#         return 0 if is_win_turn else 1
    
#     if n == 0:
#         return 0
    
#     moves = [m-3, m-6, m//3]
    
#     if is_win_turn:
#         return any(game(n-1, move, False) for move in moves)
#     else:
#         return all(game(n-1, move, True) for move in moves)

# print('19)', min(m for m in range(26, 100) if not game(1, m, True) and game(2, m, False)))


def game(n, m, is_win_turn):
    if m <= 25:
        return 0 if is_win_turn else 1
    
    if n == 0:
        return 0
    
    moves = [m-3, m-6, m//3]
    
    if is_win_turn:
        return any(game(n-1, move, False) for move in moves)
    else:
        return all(game(n-1, move, True) for move in moves)

# print('21)', min(m for m in range(26, 100) if not game(2, m, False) and game(4, m, False)))


# def win(n, m):
#     return m > 25 and any(not win(n-1, x) for x in [m-3, m-6, m//3])

# def lose(n, m):
#     return m <= 25 or n and all(win(n-1, x) for x in [m-3, m-6, m//3])

# print('21)', min(m for m in range(26, 100) if not lose(2, m) and lose(4, m)))


def f(n, m, w=1):
    if m <= 25: 
        return w == 0
    if not n: return w == 1
    moves = [m-3, m-6, m//3]
    return any(not f(n-1, x, w) for x in moves) if w else all(f(n-1, x, 1) for x in moves)

print('21)', min(m for m in range(26, 100) if not f(2, m, 0) and f(4, m, 0)))

def f(n, m):
    if m <= 25: return n % 2 == 0
    if not n: return True
    return any(not f(n-1, x) for x in [m-3, m-6, m//3])

print('21)', min(m for m in range(26, 100) if f(2, m) and not f(4, m)))


