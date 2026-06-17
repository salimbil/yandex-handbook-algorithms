# Компилятор: Python 3.13.2
MOD = 10**9 + 7

def solve():
    n, S, K = map(int, input().split())
    coins = list(map(int, input().split()))
    
    # dp[s][k] = количество способов набрать сумму s ровно k монетами
    dp = [[0] * (K + 1) for _ in range(S + 1)]
    dp[0][0] = 1
    
    for coin in coins:
        for s in range(coin, S + 1):
            for k in range(1, K + 1):
                dp[s][k] = (dp[s][k] + dp[s - coin][k - 1]) % MOD
    
    print(dp[S][K])

if __name__ == "__main__":
    solve()
