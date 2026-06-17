# Компилятор: Python 3.11 (PyPy 7.3.19)
A = input().strip()
B = input().strip()

sum_dec = int(A, 2) + int(B, 2)
print(bin(sum_dec)[2:])
