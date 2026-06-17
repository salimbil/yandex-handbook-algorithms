# Компилятор: Python 3.13.2

n = int(input())
a = input()
b = input()
print(''.join([a[i] + b[i] for i in range(len(a))]))
