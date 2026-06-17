# Компилятор: Python 3.11
n, k = map(int, input().split())

# C̅(n,k) = C(n+k-1, k)
# Вычисляем C(n+k-1, k)
N = n + k - 1
K = k

result = 1
for i in range(1, K + 1):
    result = result * (N - i + 1) // i

print(result)
