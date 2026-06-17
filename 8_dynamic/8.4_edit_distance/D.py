# Компилятор: Python 3.13.2
import sys

data = sys.stdin.read().strip().splitlines()
s = data[0]
t = data[1]

n = len(s)
m = len(t)

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = i
for j in range(m + 1):
    dp[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cost = 0 if s[i - 1] == t[j - 1] else 1
        dp[i][j] = min(
            dp[i - 1][j - 1] + cost,
            dp[i - 1][j] + 1,
            dp[i][j - 1] + 1
        )

print(dp[n][m])

ops = []
i = n
j = m
while i > 0 or j > 0:
    if i > 0 and dp[i][j] == dp[i - 1][j] + 1:
        ops.append(f"DEL {s[i - 1]}")
        i -= 1
        continue
    if j > 0 and dp[i][j] == dp[i][j - 1] + 1:
        ops.append(f"INS {t[j - 1]}")
        j -= 1
        continue
    if i > 0 and j > 0:
        cost = 0 if s[i - 1] == t[j - 1] else 1
        if dp[i][j] == dp[i - 1][j - 1] + cost:
            if cost == 1:
                ops.append(f"REP {s[i - 1]} {t[j - 1]}")
            i -= 1
            j -= 1
            continue
    # fallback (не должно срабатывать)
    if j > 0:
        ops.append(f"INS {t[j - 1]}")
        j -= 1
    else:
        ops.append(f"DEL {s[i - 1]}")
        i -= 1

ops.reverse()
print(' '.join(ops))
