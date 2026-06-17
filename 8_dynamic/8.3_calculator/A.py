# Компилятор: Python 3.13.2
def solve():
    n = int(input())
    
    INF = 10**9
    dp = [INF] * (n + 1)
    prev = [0] * (n + 1)
    
    dp[1] = 0
    prev[1] = -1
    
    for i in range(1, n + 1):
        # +1
        if i + 1 <= n and dp[i + 1] > dp[i] + 1:
            dp[i + 1] = dp[i] + 1
            prev[i + 1] = i
        
        # ×2
        if i * 2 <= n and dp[i * 2] > dp[i] + 1:
            dp[i * 2] = dp[i] + 1
            prev[i * 2] = i
        
        # ×3
        if i * 3 <= n and dp[i * 3] > dp[i] + 1:
            dp[i * 3] = dp[i] + 1
            prev[i * 3] = i
    
    # Восстановление пути
    path = []
    cur = n
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    
    print(dp[n])
    print(' '.join(map(str, path)))

if __name__ == "__main__":
    solve()
