# Компилятор: Python 3.11 (PyPy 7.3.19)

n = int(input())
a = input()
b = input()
print(''.join([a[i] + b[i] for i in range(len(a))]))
