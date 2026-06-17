# Компилятор: Python 3.13.2
MOD = 10**9 + 7

def solve():
    n, S, K = map(int, input().split())
    coins = []
    for _ in range(n):
        v, c = map(int, input().split())
        coins.append((v, c))
    
    # dp[k][s]
    dp = [[0] * (S + 1) for _ in range(K + 1)]
    dp[0][0] = 1
    
    for v, c in coins:
        new_dp = [row[:] for row in dp]  # копируем старые способы (без использования этого типа)
        
        for cnt in range(1, c + 1):
            total_value = cnt * v
            if total_value > S:
                break
            # идём от больших k и s, чтобы не учитывать одну монету несколько раз в этой итерации
            for k in range(K, cnt - 1, -1):
                for s in range(S, total_value - 1, -1):
                    if dp[k - cnt][s - total_value] > 0:
                        new_dp[k][s] = (new_dp[k][s] + dp[k - cnt][s - total_value]) % MOD
        dp = new_dp
    
    print(dp[K][S] % MOD)

if __name__ == "__main__":
    solve()
