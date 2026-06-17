# Компилятор: Python 3.11
n, k = map(int, input().split())

# C(n,k) = n! / (k! * (n-k)!)
result = 1
for i in range(1, k + 1):
    result = result * (n - i + 1) // i

print(result)
