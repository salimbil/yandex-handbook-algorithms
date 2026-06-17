# Компилятор: Python 3.13.2
n, k = map(int, input().split())

# минимальная сумма для k различных чисел
min_sum = k * (k + 1) // 2
# остаток, который нужно распределить
extra = n - min_sum

# базовые числа: 1, 2, ..., k
a = list(range(1, k + 1))

# распределяем extra, добавляя к последним элементам
# каждое число можно увеличить на extra // k + ещё по одному
add = extra // k
rem = extra % k

for i in range(k):
    a[i] += add
for i in range(k - rem, k):
    a[i] += 1

print(' '.join(map(str, a)))
