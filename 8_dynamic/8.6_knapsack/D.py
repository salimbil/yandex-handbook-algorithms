# Компилятор: Python 3.13.2
def solve():
    W1, W2, n = map(int, input().split())
    weights = list(map(int, input().split()))
    
    dp = [[False] * (W2 + 1) for _ in range(W1 + 1)]
    dp[0][0] = True
    
    for w in weights:
        for a in range(W1, -1, -1):
            for b in range(W2, -1, -1):
                if not dp[a][b]:
                    continue
                if a + w <= W1:
                    dp[a + w][b] = True
                if b + w <= W2:
                    dp[a][b + w] = True
    
    # Находим максимальную сумму a + b
    max_weight = 0
    for a in range(W1 + 1):
        for b in range(W2 + 1):
            if dp[a][b]:
                max_weight = max(max_weight, a + b)
    
    print(max_weight)

if __name__ == "__main__":
    solve()
