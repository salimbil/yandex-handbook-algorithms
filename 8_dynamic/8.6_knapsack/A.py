# Компилятор: Python 3.13.2
def solve():
    W, n = map(int, input().split())
    weights = list(map(int, input().split()))
    
    dp = [False] * (W + 1)
    dp[0] = True
    
    for w in weights:
        for s in range(W, w - 1, -1):
            if dp[s - w]:
                dp[s] = True
    
    # Находим максимальный достижимый вес
    for s in range(W, -1, -1):
        if dp[s]:
            print(s)
            return

if __name__ == "__main__":
    solve()
