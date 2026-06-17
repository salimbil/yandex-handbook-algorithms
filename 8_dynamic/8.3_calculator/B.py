# Компилятор: Python 3.13.2
def solve():
    n = int(input())
    
    INF = 10**9
    dp = [INF] * (n + 1)
    dp[1] = 0
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i >= 2:
            dp[i] = min(dp[i], dp[i - 2] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
    
    print(dp[n])

if __name__ == "__main__":
    solve()
