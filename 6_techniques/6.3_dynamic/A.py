# Компилятор: Python 3.11
n, m = map(int, input().split())

# dp[i][j] = True, если позиция (i, j) выигрышная для текущего игрока
dp = [[False] * (m + 1) for _ in range(n + 1)]

# База: (0, 0) — проигрыш (нет камней, ход сделать нельзя)
dp[0][0] = False

for i in range(n + 1):
    for j in range(m + 1):
        if i == 0 and j == 0:
            continue
        
        # Проверяем все возможные ходы
        can_win = False
        
        # Взять 1 из первого набора
        if i > 0 and not dp[i-1][j]:
            can_win = True
        
        # Взять 1 из второго набора
        if j > 0 and not dp[i][j-1]:
            can_win = True
        
        # Взять по 1 из обоих
        if i > 0 and j > 0 and not dp[i-1][j-1]:
            can_win = True
        
        dp[i][j] = can_win

print("Win" if dp[n][m] else "Lose")
