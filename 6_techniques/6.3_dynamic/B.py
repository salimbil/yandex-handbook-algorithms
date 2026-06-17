# Компилятор: Python 3.11
n, m = map(int, input().split())

dp = [[False] * (m + 1) for _ in range(n + 1)]
dp[0][0] = False  # нет камней — проигрыш

for i in range(n + 1):
    for j in range(m + 1):
        if i == 0 and j == 0:
            continue
        
        can_win = False
        
        # Взять 1 из первого
        if i >= 1 and not dp[i-1][j]:
            can_win = True
        # Взять 1 из второго
        if j >= 1 and not dp[i][j-1]:
            can_win = True
        # Взять 2 из первого
        if i >= 2 and not dp[i-2][j]:
            can_win = True
        # Взять 2 из второго
        if j >= 2 and not dp[i][j-2]:
            can_win = True
        # Взять 2 из первого и 1 из второго
        if i >= 2 and j >= 1 and not dp[i-2][j-1]:
            can_win = True
        # Взять 1 из первого и 2 из второго
        if i >= 1 and j >= 2 and not dp[i-1][j-2]:
            can_win = True
        
        dp[i][j] = can_win

print("Win" if dp[n][m] else "Lose")
