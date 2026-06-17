# Компилятор: Python 3.13.2
import sys
import bisect

data = sys.stdin.buffer.read().split()
n = int(data[0])
S = int(data[1])
a = list(map(int, data[2:]))

a.sort()

count = 0
for i in range(n):
    target = S - a[i]
    # Ищем первый элемент больше target, начиная с i+1
    idx = bisect.bisect_right(a, target, i + 1, n)
    if idx > i + 1:
        count += idx - i - 1

sys.stdout.write(str(count))
