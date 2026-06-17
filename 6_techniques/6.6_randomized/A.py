# Компилятор: Python 3.13.2
n = int(input())
a = list(map(int, input().split()))

pivot = a[0]
j = 0  # граница элементов <= pivot

for i in range(1, n):
    if a[i] <= pivot:
        j += 1
        a[i], a[j] = a[j], a[i]

# Ставим pivot на место
a[0], a[j] = a[j], a[0]

print(' '.join(map(str, a)))
