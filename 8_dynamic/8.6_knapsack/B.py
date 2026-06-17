# Компилятор: Python 3.13.2
def solve():
    W, n = map(int, input().split())
    weights = list(map(int, input().split()))
    
    dp = [0] * (W + 1)
    dp[0] = 1
    
    for w in weights:
        for s in range(W, w - 1, -1):
            if dp[s - w] > 0:
                dp[s] += dp[s - w]
    
    # Находим максимальный достижимый вес
    for s in range(W, -1, -1):
        if dp[s] > 0:
            print(dp[s])
            return

if __name__ == "__main__":
    solve()
