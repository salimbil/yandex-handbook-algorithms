# Компилятор: Python 3.11
n, K = map(int, input().split())
x = list(map(int, input().split()))
x.sort()

dp = [0] * n
dp[0] = K

for i in range(1, n):
    dist_sq = (x[i] - x[i-1]) ** 2
    dp[i] = min(dp[i-1] + K, dp[i-1] + dist_sq)

print(dp[-1])
