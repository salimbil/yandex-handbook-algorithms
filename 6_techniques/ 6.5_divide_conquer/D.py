# Компилятор: Python 3.11
n = int(input())
a = list(map(int, input().split()))

max_sum = a[0]
current_sum = a[0]

for i in range(1, n):
    current_sum = max(a[i], current_sum + a[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)
