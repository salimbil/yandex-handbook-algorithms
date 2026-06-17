# Компилятор: Python 3.13.2
def solve():
    W, n = map(int, input().split())
    weights = list(map(int, input().split()))
    
    INF = 10**9
    dp = [INF] * (W + 1)
    dp[0] = 0
    
    for w in weights:
        if w == 0:
            continue
        for s in range(W, w - 1, -1):
            if dp[s - w] != INF:
                if dp[s] > dp[s - w] + 1:
                    dp[s] = dp[s - w] + 1
    
    # Находим максимальный достижимый вес
    best_weight = 0
    for s in range(W, -1, -1):
        if dp[s] != INF:
            best_weight = s
            break
    
    print(dp[best_weight])

if __name__ == "__main__":
    solve()
