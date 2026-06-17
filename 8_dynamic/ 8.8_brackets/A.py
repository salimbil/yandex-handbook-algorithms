# Компилятор: Python 3.13.2
def solve():
    s = input().strip()
    n = len(s) // 2 + 1  # количество чисел
    nums = [int(s[i]) for i in range(0, len(s), 2)]
    ops = [s[i] for i in range(1, len(s), 2)]
    
    INF = 10**18
    dp_max = [[-INF] * n for _ in range(n)]
    dp_min = [[INF] * n for _ in range(n)]
    
    for i in range(n):
        dp_max[i][i] = dp_min[i][i] = nums[i]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                op = ops[k]
                for a in (dp_max[i][k], dp_min[i][k]):
                    for b in (dp_max[k+1][j], dp_min[k+1][j]):
                        if op == '+':
                            val = a + b
                        elif op == '-':
                            val = a - b
                        else:  # '*'
                            val = a * b
                        dp_max[i][j] = max(dp_max[i][j], val)
                        dp_min[i][j] = min(dp_min[i][j], val)
    
    print(dp_max[0][n-1])

if __name__ == "__main__":
    solve()
