# Компилятор: Python 3.13.2
s = input().strip()
n = (len(s) + 1) // 2
nums = [int(s[i * 2]) for i in range(n)]
ops = [s[i * 2 + 1] for i in range(n - 1)]

dp = [[{} for _ in range(n)] for __ in range(n)]
for i in range(n):
    dp[i][i][nums[i]] = 1

for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1
        for k in range(l, r):
            op = ops[k]
            for left_val, left_cnt in dp[l][k].items():
                for right_val, right_cnt in dp[k + 1][r].items():
                    if op == '+':
                        val = left_val + right_val
                    elif op == '-':
                        val = left_val - right_val
                    else:
                        val = left_val * right_val
                    dp[l][r][val] = dp[l][r].get(val, 0) + left_cnt * right_cnt

max_val = max(dp[0][n - 1].keys())
print(dp[0][n - 1][max_val])
