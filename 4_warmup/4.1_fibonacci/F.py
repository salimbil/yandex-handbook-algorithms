# Компилятор: Python 3.11
n = int(input())

fib = [1, 2]
while fib[-1] <= n:
    fib.append(fib[-1] + fib[-2])
fib.pop()  # последний больше n

res = ['0'] * len(fib)
for i in range(len(fib) - 1, -1, -1):
    if fib[i] <= n:
        res[i] = '1'
        n -= fib[i]

print(''.join(res[::-1]))
