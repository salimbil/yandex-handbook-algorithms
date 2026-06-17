# Компилятор: Python 3.11
MOD = 1_000_000_007

N = int(input())

# dp[p2][p1] — количество строк длины len, заканчивающихся на p2, p1
# p2, p1 ∈ {0, 1, 2}
dp = [[0] * 3 for _ in range(3)]

if N == 1:
    print(3)
elif N == 2:
    print(9)
else:
    # Инициализация для длины 2
    for i in range(3):
        for j in range(3):
            dp[i][j] = 1
    
    for length in range(3, N + 1):
        new_dp = [[0] * 3 for _ in range(3)]
        for p2 in range(3):
            for p1 in range(3):
                if dp[p2][p1] == 0:
                    continue
                for c in range(3):
                    if c != p2:  # условие s[i] ≠ s[i-2]
                        new_dp[p1][c] = (new_dp[p1][c] + dp[p2][p1]) % MOD
        dp = new_dp
    
    ans = sum(dp[i][j] for i in range(3) for j in range(3)) % MOD
    print(ans)
